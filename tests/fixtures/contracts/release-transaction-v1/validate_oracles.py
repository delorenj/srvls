#!/usr/bin/env python3
"""Independent integrity and semantic validator for fixed release v1 oracles."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
OUTER_KEYS = ["schema_version", "payload", "checksum"]
PAYLOAD_KEYS = [
    "transaction_id",
    "manifest_revision",
    "predecessor_checksum",
    "intent",
    "original_owner",
    "recovery_attempts",
    "active_recovery_attempt_id",
    "old_install_generation",
    "target_install_generation",
    "prior_release",
    "paths",
    "artifacts",
    "state_backup",
    "consumers",
    "known_good_candidate",
    "commit_decision",
    "current_step",
    "step_records",
    "release_events",
    "terminal_result",
]
ATTEMPT_KEYS = [
    "schema_version",
    "attempt_id",
    "sequence",
    "owner",
    "admission_lock_device",
    "admission_lock_inode",
    "predecessor_manifest_checksum",
    "acquisition_boot_ns",
]
STEP_KEYS = [
    "schema_version",
    "sequence",
    "step",
    "direction",
    "state",
    "effect_attempt",
    "idempotency_key",
    "recovery_attempt_id",
    "validation_attempt",
    "pre_effect_evidence",
    "post_effect_evidence",
    "reason_code",
]
EVENT_KEYS = [
    "schema_version",
    "transaction_id",
    "sequence",
    "recovery_attempt_id",
    "recovery_attempt_sequence",
    "manifest_revision",
    "manifest_step",
    "public_phase",
    "status",
    "reason_code",
]
CASES = {
    "owner-takeover-pending-validation.manifest.json": (
        "validate-candidate",
        "pending",
        "first-install-absent",
        2,
        "absent",
    ),
    "first-install-absent-pending-consumer-removal.manifest.json": (
        "remove-first-install-consumers",
        "pending",
        "first-install-absent",
        1,
        "absent",
    ),
    "commit-decided-complete.manifest.json": (
        "commit-decided",
        "complete",
        "first-install-absent",
        1,
        "present",
    ),
    "known-good-publication-pending.manifest.json": (
        "publish-known-good",
        "pending",
        "first-install-absent",
        1,
        "present",
    ),
    "known-good-publication-complete.manifest.json": (
        "publish-known-good",
        "complete",
        "first-install-absent",
        1,
        "present",
    ),
    "ready-admission-pending.manifest.json": (
        "persist-ready-admission",
        "pending",
        "first-install-absent",
        1,
        "present",
    ),
    "explicit-rollback-ready-admission-pending.manifest.json": (
        "rollback-ready-admission",
        "pending",
        "installed",
        1,
        "present",
    ),
}


def fail(message: str) -> None:
    raise SystemExit(f"release oracle validation failed: {message}")


def pairs_no_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            fail(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def load_exact(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    if not raw.endswith(b"\n") or raw.endswith(b"\n\n"):
        fail(f"{path.name}: expected exactly one repository line feed")
    try:
        value = json.loads(raw[:-1], object_pairs_hook=pairs_no_duplicates)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        fail(f"{path.name}: invalid JSON: {exc}")
    canonical = json.dumps(
        value, ensure_ascii=False, separators=(",", ":")
    ).encode("utf-8")
    if raw[:-1] != canonical:
        fail(f"{path.name}: bytes are not canonical/minified in declared order")
    if not isinstance(value, dict):
        fail(f"{path.name}: top level is not an object")
    return value


def digest(domain: str, value: Any) -> str:
    preimage = json.dumps(
        value, ensure_ascii=False, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(domain.encode("ascii") + b"\0" + preimage).hexdigest()


def walk(value: Any):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def without(value: dict[str, Any], key: str) -> dict[str, Any]:
    return {name: child for name, child in value.items() if name != key}


def validate_nested_hashes(root: dict[str, Any], path: Path) -> None:
    payload = root["payload"]
    backup = payload["state_backup"]["value"]
    expected = digest(
        "srvls-state-backup-manifest-v1", without(backup, "manifest_hash")
    )
    if backup["manifest_hash"] != expected:
        fail(f"{path.name}: StateBackupManifestV1 hash mismatch")

    for value in walk(root):
        if value.get("schema_version") == "srvls-managed-consumer-unit-contract-v1":
            expected = digest(
                "srvls-managed-consumer-unit-contract-v1",
                without(value, "contract_hash"),
            )
            if value["contract_hash"] != expected:
                fail(f"{path.name}: consumer contract hash mismatch")

    candidate_union = payload["known_good_candidate"]
    if candidate_union["kind"] == "present":
        candidate = candidate_union["value"]
        if candidate["prior_release"] != payload["prior_release"]:
            fail(f"{path.name}: candidate prior release differs from recovery authority")
        expected = digest(
            "srvls-known-good-candidate-v1",
            without(candidate, "candidate_checksum"),
        )
        if candidate["candidate_checksum"] != expected:
            fail(f"{path.name}: KnownGoodCandidateV1 checksum mismatch")
        known_payload = {
            "source_transaction_id": payload["transaction_id"],
            "published_install_generation": payload["target_install_generation"],
            "candidate": candidate,
        }
        known_hash = digest("srvls-known-good-release-v1", known_payload)
        decision = payload["commit_decision"]
        if decision["kind"] == "decided" and (
            decision["candidate_checksum"] != candidate["candidate_checksum"]
            or decision["expected_known_good_checksum"] != known_hash
        ):
            fail(f"{path.name}: commit decision checksum mismatch")
        for atom in walk(payload["step_records"]):
            if atom.get("kind") == "known-good" and atom["checksum"] != known_hash:
                fail(f"{path.name}: KnownGood evidence checksum mismatch")


def validate_manifest(path: Path, expected_case: tuple[Any, ...]) -> None:
    root = load_exact(path)
    if list(root) != OUTER_KEYS or root["schema_version"] != "srvls-upgrade-transaction-v1":
        fail(f"{path.name}: outer schema/key order mismatch")
    payload = root["payload"]
    if list(payload) != PAYLOAD_KEYS:
        fail(f"{path.name}: payload key order mismatch")
    if root["checksum"] != digest("srvls-upgrade-transaction-v1", payload):
        fail(f"{path.name}: outer checksum mismatch")

    attempts = payload["recovery_attempts"]
    if [row["sequence"] for row in attempts] != list(range(len(attempts))):
        fail(f"{path.name}: recovery attempt sequence is not gap-free")
    if any(list(row) != ATTEMPT_KEYS for row in attempts):
        fail(f"{path.name}: recovery attempt key order mismatch")
    if payload["active_recovery_attempt_id"] != attempts[-1]["attempt_id"]:
        fail(f"{path.name}: active recovery attempt is not the final row")

    steps = payload["step_records"]
    events = payload["release_events"]
    if [row["sequence"] for row in steps] != list(range(len(steps))):
        fail(f"{path.name}: step sequence is not gap-free")
    if [row["sequence"] for row in events] != list(range(len(events))):
        fail(f"{path.name}: event sequence is not gap-free")
    if any(list(row) != STEP_KEYS for row in steps):
        fail(f"{path.name}: step key order mismatch")
    if any(list(row) != EVENT_KEYS for row in events):
        fail(f"{path.name}: event key order mismatch")
    attempt_sequences = {row["attempt_id"]: row["sequence"] for row in attempts}
    for step, event in zip(steps, events):
        if event["manifest_step"] != step["step"]:
            fail(f"{path.name}: event/step mismatch")
        if event["recovery_attempt_id"] != step["recovery_attempt_id"]:
            fail(f"{path.name}: event/step owner mismatch")
        if event["recovery_attempt_sequence"] != attempt_sequences[step["recovery_attempt_id"]]:
            fail(f"{path.name}: event owner sequence mismatch")

    expected_step, expected_state, prior_kind, attempt_count, candidate_kind = expected_case
    final = steps[-1]
    if payload["current_step"] != expected_step or final["step"] != expected_step:
        fail(f"{path.name}: wrong frozen crash-cut step")
    if final["state"] != expected_state:
        fail(f"{path.name}: wrong frozen crash-cut state")
    if payload["prior_release"]["kind"] != prior_kind:
        fail(f"{path.name}: wrong prior-release variant")
    if len(attempts) != attempt_count:
        fail(f"{path.name}: wrong recovery-owner count")
    if payload["known_good_candidate"]["kind"] != candidate_kind:
        fail(f"{path.name}: wrong candidate presence")

    if prior_kind == "first-install-absent":
        first = payload["prior_release"]["value"]
        consumer_disposition = first["consumer_disposition"]
        if consumer_disposition["kind"] != "absent" or not consumer_disposition["units"]:
            fail(f"{path.name}: missing nonempty prior-consumer absence records")
        kinds = [unit["unit_kind"] for unit in consumer_disposition["units"]]
        if kinds != ["service", "timer"]:
            fail(f"{path.name}: absent service/timer order mismatch")

    if path.name.startswith("owner-takeover"):
        if final["recovery_attempt_id"] != attempts[-1]["attempt_id"]:
            fail(f"{path.name}: pending replay is not bound to replacement owner")
    if path.name.startswith("first-install-absent"):
        if any(row["direction"] != "recovery" for row in steps[-3:]):
            fail(f"{path.name}: absent restoration steps are not recovery-owned")

    validate_nested_hashes(root, path)


def validate_lock_trace() -> None:
    value = load_exact(ROOT / "admission-record-lock.trace.json")
    lock = value["lock"]
    if (
        lock["command"] != "F_SETLK"
        or lock["blocking_command"] != "F_SETLKW"
        or [lock["whence"], lock["start"], lock["length"]] != ["SEEK_SET", 0, 1]
        or lock["forbidden"] != ["flock", "F_OFD_SETLK", "F_OFD_SETLKW"]
    ):
        fail("admission record-lock grammar drift")
    if [row["lease"] for row in value["cases"]] != ["shared", "exclusive"]:
        fail("admission trace does not cover shared then exclusive")
    for row in value["cases"]:
        if (
            row["child_state"] != "stopped-before-first-action"
            or row["audit_after"] != {"type": "F_UNLCK"}
            or row["contender"] != "acquired-while-child-stopped"
        ):
            fail("stopped-child takeover proof drift")


def validate_dbus_trace() -> None:
    value = load_exact(ROOT / "manager-subscription.trace.json")
    order = value["required_order"]
    if order.index("manager-subscribe-success") > order.index("capture-baselines"):
        fail("Subscribe occurs after baseline")
    if order.index("capture-baselines") > order.index("trigger-or-await"):
        fail("trigger occurs before baseline")
    handshake = value["success"]["handshake"]
    if (
        handshake["manager_unique_owner"] != handshake["subscribe_reply_owner"]
        or handshake["manager_unique_owner"] != handshake["owner_recheck"]
        or [row["sequence"] for row in handshake["match_rules"]] != list(range(5))
        or handshake["status"] != "ready"
    ):
        fail("manager owner/match/Subscribe proof drift")
    expected_failures = {
        "dbus-subscribe-failed",
        "dbus-owner-changed",
        "dbus-stream-discontinuity",
        "dbus-disconnected",
    }
    if {row["result"] for row in value["failures"]} != expected_failures:
        fail("manager loss result vocabulary drift")


def validate_file_hashes() -> None:
    sums = ROOT / "SHA256SUMS"
    listed: set[str] = set()
    for line in sums.read_text(encoding="ascii").splitlines():
        expected, name = line.split("  ", 1)
        listed.add(name)
        actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        if actual != expected:
            fail(f"SHA256SUMS mismatch for {name}")
    expected_files = {
        path.name
        for path in ROOT.iterdir()
        if path.is_file() and path.name != "SHA256SUMS"
    }
    if listed != expected_files:
        fail("SHA256SUMS file inventory mismatch")


def main() -> None:
    for name, expected in CASES.items():
        validate_manifest(ROOT / name, expected)
    unavailable = load_exact(ROOT / "rollback-unavailable.result.json")
    if unavailable != {"kind": "rollback-unavailable", "reason": "no-prior-release"}:
        fail("rollback-unavailable result drift")
    validate_lock_trace()
    validate_dbus_trace()
    validate_file_hashes()
    print(f"release oracle validation: PASS ({len(CASES)} manifests, 2 traces, 1 result)")


if __name__ == "__main__":
    main()
