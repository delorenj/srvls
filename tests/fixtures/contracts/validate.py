#!/usr/bin/env python3
"""Validate fixed pass-3 contract oracle bytes without product code."""

from __future__ import annotations

import hashlib
import json
import struct
import sys
import unicodedata
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parent
UNRESERVED = frozenset(b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~")


def fail(message: str) -> None:
    raise AssertionError(message)


def canonical(value: object) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        separators=(",", ":"),
    ).encode("utf-8")


def read_canonical(relative: str) -> tuple[object, bytes]:
    stored = (ROOT / relative).read_bytes()
    if stored.endswith(b"\r\n"):
        fail(f"{relative}: CRLF is not a valid fixture terminator")
    data = stored[:-1] if stored.endswith(b"\n") else stored
    if data.endswith(b"\n"):
        fail(f"{relative}: more than one repository text terminator")
    value = json.loads(data)
    if canonical(value) != data:
        fail(f"{relative}: bytes are not CanonicalJsonV1")
    return value, data


def domain_hash(domain: str, payload: bytes) -> str:
    return hashlib.sha256(domain.encode("ascii") + b"\0" + payload).hexdigest()


def percent(data: bytes) -> str:
    return "".join(chr(byte) if byte in UNRESERVED else f"%{byte:02X}" for byte in data)


def u16(value: int) -> bytes:
    return struct.pack(">H", value)


def u32(value: int) -> bytes:
    return struct.pack(">I", value)


def u64(value: int) -> bytes:
    return struct.pack(">Q", value)


def frame_fields(fields: list[bytes]) -> bytes:
    return b"\x01" + u16(len(fields)) + b"".join(
        u16(index) + u32(len(value)) + value
        for index, value in enumerate(fields, 1)
    )


def field_envelope(tag: int, value: bytes) -> bytes:
    return u16(tag) + u32(len(value)) + value


def scope_id(spec: dict[str, object]) -> bytes:
    provider = spec["provider"]
    if provider == "cron-user":
        return b"\x01\x01" + u32(int(spec["uid"]))
    if provider == "cron-root":
        return b"\x01\x02"
    if provider == "cron-system":
        return b"\x01\x03"
    if provider == "systemd-user":
        return b"\x01\x04" + u32(int(spec["uid"]))
    if provider == "systemd-system":
        return b"\x01\x05"
    if provider == "docker":
        endpoint = str(spec["endpoint"]).encode()
        context = str(spec["context"]).encode()
        return b"\x01\x06" + u32(len(endpoint)) + endpoint + u32(len(context)) + context
    if provider == "pm2":
        home = bytes.fromhex(str(spec["home_hex"]))
        return b"\x01\x07" + u32(len(home)) + home
    if provider == "process":
        host = bytes.fromhex(str(spec["host_identity_hex"]))
        if len(host) != 32:
            fail("process HostIdentity must be 32 bytes")
        return b"\x01\x08" + host
    fail(f"unknown scope Provider {provider}")
    raise AssertionError


def observation_bytes(case: dict[str, object]) -> tuple[bytes, bytes | None, str | None]:
    provider = str(case["name"])
    scope = scope_id(case["scope"])
    inner: bytes | None = None
    inner_hash: str | None = None
    if provider == "cron":
        values = [bytes.fromhex(str(item)) for item in case["hash_fields_hex"]]
        inner = frame_fields(values)
        inner_hash = domain_hash("srvls-cron-entry-v1", inner)
        fields = [
            scope,
            bytes.fromhex(str(case["source_hex"])),
            u64(int(case["physical_line"])),
            bytes.fromhex(inner_hash),
            u32(int(case["duplicate_occurrence"])),
        ]
        tag = 1
    elif provider == "systemd":
        fields = [scope, unicodedata.normalize("NFC", str(case["unit"])).encode()]
        tag = 2
    elif provider == "docker":
        fields = [scope, bytes.fromhex(str(case["container_id_hex"]))]
        tag = 3
    elif provider == "pm2":
        values = [bytes.fromhex(str(item)) for item in case["hash_fields_hex"]]
        inner = frame_fields(values)
        inner_hash = domain_hash("srvls-pm2-birth-v1", inner)
        origin = 1 if case["birth_origin"] == "created_at" else 2
        fields = [scope, u32(int(case["pm_id"])), bytes([origin]) + u64(int(case["birth_utc_ms"])), bytes.fromhex(inner_hash)]
        tag = 4
    elif provider == "process":
        values = [bytes.fromhex(str(item)) for item in case["hash_fields_hex"]]
        inner = frame_fields(values)
        inner_hash = domain_hash("srvls-process-birth-v1", inner)
        fields = [
            scope,
            uuid.UUID(str(case["boot_id"])).bytes,
            u32(int(case["pid"])),
            u64(int(case["start_ticks"])),
            bytes.fromhex(inner_hash),
        ]
        tag = 5
    else:
        fail(f"unknown Observation Provider {provider}")
    return b"\x01" + bytes([tag]) + u16(len(fields)) + b"".join(
        field_envelope(index, value) for index, value in enumerate(fields, 1)
    ), inner, inner_hash


def framed_sequence(elements: list[bytes]) -> bytes:
    return u32(len(elements)) + b"".join(u32(len(item)) + item for item in elements)


def command_spec(command: dict[str, object]) -> bytes:
    executable = bytes.fromhex(str(command["executable_hex"]))
    arguments = [bytes.fromhex(str(item)) for item in command["arguments_hex"]]
    return u32(len(executable)) + executable + u32(len(arguments)) + b"".join(
        u32(len(argument)) + argument for argument in arguments
    )


def environment_entry(entry: dict[str, object]) -> bytes:
    name = str(entry["name"]).encode("ascii")
    value = bytes.fromhex(str(entry["value_hex"]))
    return u32(len(name)) + name + u32(len(value)) + value


def provider_scope_bytes(case: dict[str, object]) -> bytes:
    commands = [command_spec(item) for item in case["commands"]]
    environment = sorted(
        (environment_entry(item) for item in case["environment"]),
        key=lambda item: item[4 : 4 + int.from_bytes(item[:4], "big")],
    )
    roots = [bytes.fromhex(str(item)) for item in case["read_roots_hex"]]
    values = [
        (2, str(case["invocation_kind"]).encode()),
        (6, framed_sequence(commands)),
        (7, framed_sequence(environment)),
        (6, framed_sequence(roots)),
        (2, str(case["privilege"]).encode()),
    ]
    body = b"".join(
        u16(index) + bytes([kind]) + u32(len(value)) + value
        for index, (kind, value) in enumerate(values, 1)
    )
    return b"\x01" + bytes([int(case["provider_tag"])]) + u16(5) + body


def verify_manifest() -> None:
    for line in (ROOT / "manifest.sha256").read_text().splitlines():
        if not line:
            continue
        expected, relative = line.split("  ", 1)
        actual = hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
        if actual != expected:
            fail(f"manifest mismatch: {relative}")


def projection_field(row: dict[str, object], name: str) -> object:
    for field in row["fields"]:
        if field["name"] == name:
            return field["value"]["value"]
    fail(f"projection field absent: {name}")
    raise AssertionError


def verify_projection(projection: dict[str, object], label: str) -> None:
    row_domains = (
        ("promise_rows", "srvls-baseline-promise-row-v1"),
        ("observation_rows", "srvls-baseline-observation-row-v1"),
        ("finding_rows", "srvls-baseline-finding-row-v1"),
    )
    for key, domain in row_domains:
        if not projection[key]:
            fail(f"{label}: {key} is empty")
        for row in projection[key]:
            row_preimage = dict(row)
            row_fingerprint = row_preimage.pop("fingerprint")
            if domain_hash(domain, canonical(row_preimage)) != row_fingerprint:
                fail(f"{label}: {key} fingerprint mismatch")


def verify_policy_and_plans() -> None:
    policy, policy_bytes = read_canonical("policy-snapshot-v1/default.preimage.json")
    expected = (ROOT / "policy-snapshot-v1/default.policy-fingerprint").read_text().strip()
    if domain_hash("srvls-policy-v1", policy_bytes) != expected:
        fail("PolicyFingerprint mismatch")
    for stem in ("minimal", "nonempty"):
        plan, plan_bytes = read_canonical(f"collection-plan-v1/{stem}.preimage.json")
        expected_plan = (ROOT / f"collection-plan-v1/{stem}.collection-plan-fingerprint").read_text().strip()
        if domain_hash("srvls-collection-plan-v1", plan_bytes) != expected_plan:
            fail(f"{stem}: CollectionPlanFingerprint mismatch")
        if plan["policy_snapshot"] != policy or plan["policy_fingerprint"] != expected:
            fail(f"{stem}: embedded policy mismatch")
        manifest = (ROOT / f"collection-plan-v1/{stem}.scope-manifest.bin").read_bytes()
        if percent(manifest) != plan["scope_manifest"]:
            fail(f"{stem}: ScopeManifest bytes mismatch")
        if domain_hash("srvls-scopes-v1", manifest) != plan["scope_manifest_fingerprint"]:
            fail(f"{stem}: ScopeManifestFingerprint mismatch")
        schedule = canonical(plan["dispatch_schedule"])
        if domain_hash("srvls-dispatch-schedule-v1", schedule) != plan["dispatch_schedule_fingerprint"]:
            fail(f"{stem}: DispatchScheduleFingerprint mismatch")
    nonempty, _ = read_canonical("collection-plan-v1/nonempty.preimage.json")
    if b"active-promise" not in (ROOT / "collection-plan-v1/nonempty.scope-manifest.bin").read_bytes():
        fail("nonempty: active-promise reason absent")
    rows = nonempty["resource_history_cut"]["rows"]
    if len(rows) != 1 or not str(rows[0]["observation_id"]).startswith("%"):
        fail("nonempty: complete ObservationId resource row absent")
    if nonempty["accepted_baseline_cut"]["kind"] != "accepted":
        fail("nonempty: accepted baseline branch absent")
    plan_projection = nonempty["accepted_baseline_cut"]["projection"]
    verify_projection(plan_projection, "nonempty plan projection")
    snapshot, snapshot_bytes = read_canonical("collection-plan-v1/nonempty.snapshot.preimage.json")
    expected_plan = (ROOT / "collection-plan-v1/nonempty.collection-plan-fingerprint").read_text().strip()
    if snapshot["collection_plan_fingerprint"] != expected_plan:
        fail("nonempty: SnapshotV1 does not name the frozen CollectionPlanFingerprint")
    fingerprint = snapshot["snapshot_fingerprint"]
    preimage = dict(snapshot)
    del preimage["snapshot_fingerprint"]
    if domain_hash("srvls-snapshot-v1", canonical(preimage)) != fingerprint:
        fail("nonempty: SnapshotFingerprint mismatch")
    if (ROOT / "collection-plan-v1/nonempty.snapshot-fingerprint").read_text().strip() != fingerprint:
        fail("nonempty: SnapshotFingerprint companion mismatch")
    projection = snapshot["baseline_projection"]
    verify_projection(projection, "nonempty snapshot projection")

    index, _ = read_canonical("observation-id-v1/cases.json")
    cron = next(case for case in index["cases"] if case["name"] == "cron")
    expected_observation = cron["display"]
    expected_birth = percent(bytes.fromhex(cron["inner_sha256"]))
    plan_observation = plan_projection["observation_rows"][0]
    snapshot_observation = projection["observation_rows"][0]
    exact_observation_references = (
        rows[0]["observation_id"],
        plan_observation["observation_id"],
        projection_field(plan_projection["promise_rows"][0], "runtime_locator"),
        projection_field(plan_observation, "native_locator"),
        projection_field(plan_projection["finding_rows"][0], "observation_ids")[0]["value"],
        snapshot["reports"][0]["observations"][0]["observation_id"],
        snapshot["observations"][0]["observation_id"],
        snapshot["resource_samples"][0]["observation_id"],
        snapshot_observation["observation_id"],
        projection_field(projection["promise_rows"][0], "runtime_locator"),
        projection_field(snapshot_observation, "native_locator"),
        projection_field(projection["finding_rows"][0], "observation_ids")[0]["value"],
    )
    if any(value != expected_observation for value in exact_observation_references):
        fail("nonempty: baseline references drifted from the raw cron ObservationId golden")
    if projection_field(plan_observation, "birth_evidence") != expected_birth:
        fail("nonempty: plan birth evidence drifted from raw HashTupleV1")
    if projection_field(snapshot_observation, "birth_evidence") != expected_birth:
        fail("nonempty: snapshot birth evidence drifted from raw HashTupleV1")


def verify_observation_ids() -> None:
    index, _ = read_canonical("observation-id-v1/cases.json")
    for case in index["cases"]:
        observed, inner, inner_hash = observation_bytes(case)
        name = case["name"]
        if observed != (ROOT / f"observation-id-v1/{name}.bin").read_bytes():
            fail(f"{name}: ObservationId bytes mismatch")
        if observed.hex() != case["observation_hex"] or percent(observed) != case["display"]:
            fail(f"{name}: ObservationId display mismatch")
        if domain_hash("srvls-observation-id-v1", observed) != case["fingerprint"]:
            fail(f"{name}: ObservationIdFingerprint mismatch")
        if inner is not None:
            if inner.hex() != case["hash_tuple_hex"] or inner_hash != case["inner_sha256"]:
                fail(f"{name}: raw inner hash derivation mismatch")


def verify_provider_scope_inputs() -> None:
    index, _ = read_canonical("provider-scope-input-v1/cases.json")
    for case in index["cases"]:
        payload = provider_scope_bytes(case)
        name = case["name"]
        if payload != (ROOT / f"provider-scope-input-v1/{name}.bin").read_bytes():
            fail(f"{name}: ProviderScopeInput bytes mismatch")
        if payload.hex() != case["provider_scope_input_hex"] or percent(payload) != case["display"]:
            fail(f"{name}: ProviderScopeInput display mismatch")
        assignment = case["assignment_preimage"]
        if assignment["provider_scope_input"]["bytes"] != case["display"]:
            fail(f"{name}: assignment does not embed exact ProviderScopeInput")
        if domain_hash("srvls-scope-assignment-v1", canonical(assignment)) != case["scope_assignment_fingerprint"]:
            fail(f"{name}: ScopeAssignmentFingerprint mismatch")


FRAME_KEYS = {
    "hello": ["protocol", "kind", "request_id", "capability", "dispatch_schedule_fingerprint", "worker_id", "schedule_origin_boot_ns", "reservation_epoch_offset_ns", "reservation_budget_ns", "full_budget_makespan_ns", "generation_cutoff_offset_ns", "absolute_scope_deadline_boot_ns", "absolute_generation_cutoff_boot_ns", "expected_worker"],
    "ready": ["protocol", "kind", "request_id", "capability", "observed_worker"],
    "request": ["protocol", "request_id", "capability", "mode", "collection_plan_fingerprint", "dispatch_schedule_fingerprint", "current_repository_revision", "generation_id", "scope_id", "scope_assignment_fingerprint", "obligation", "worker_id", "schedule_origin_boot_ns", "reservation_epoch_offset_ns", "reservation_budget_ns", "full_budget_makespan_ns", "generation_cutoff_offset_ns", "absolute_scope_deadline_boot_ns", "absolute_generation_cutoff_boot_ns", "capture_reservation", "self_process_set", "provider_scope_input"],
    "result": ["protocol", "request_id", "capability", "collection_plan_fingerprint", "dispatch_schedule_fingerprint", "current_repository_revision", "generation_id", "scope_id", "scope_assignment_fingerprint", "reservation", "result", "diagnostic_candidates", "capture_accounting"],
}


def verify_ipc() -> None:
    index, _ = read_canonical("ipc-v1/complete-exchange/index.json")
    for item in index["frames"]:
        value, payload = read_canonical(item["payload"])
        if list(value) != FRAME_KEYS[item["frame_type"]]:
            fail(f"{item['payload']}: frame key order mismatch")
        expected_frame = u32(len(payload)) + payload
        if expected_frame != (ROOT / item["frame"]).read_bytes():
            fail(f"{item['frame']}: frame bytes mismatch")
        if item["frame_type"] == "result":
            report = value["result"]["value"]
            if list(report) != ["schema", "generation_id", "scope_id", "obligation", "observations", "duration_ns", "diagnostic_references", "outcome", "process_extension"]:
                fail(f"{item['payload']}: CollectorReportV1 key order mismatch")
            observation = report["observations"][0]
            if list(observation) != ["schema", "observation_id", "scope_id", "encounter_ordinal", "display_name", "lifecycle", "schedule", "health", "project", "source", "ownership_hints", "resources", "provider_detail", "diagnostic_references"]:
                fail(f"{item['payload']}: ObservationV1 key order mismatch")
            candidate = value["diagnostic_candidates"][0]
            if list(candidate) != ["schema", "producer", "scope_id", "code", "parameter_schema", "subject", "source_encounter", "parameters", "duplicate_occurrence"]:
                fail(f"{item['payload']}: DiagnosticCandidateV1 key order mismatch")
            capture = value["capture_accounting"]
            if list(capture) != ["stdout", "stderr"]:
                fail(f"{item['payload']}: CaptureAccountingV1 key order mismatch")
    timeout_index, _ = read_canonical("ipc-v1/preallocation-timeout/index.json")
    parameters, _ = read_canonical("ipc-v1/preallocation-timeout/parameters.json")
    candidate, _ = read_canonical("ipc-v1/preallocation-timeout/candidate.json")
    report, _ = read_canonical("ipc-v1/preallocation-timeout/report.json")
    state, _ = read_canonical("ipc-v1/preallocation-timeout/state-cuts.json")
    expected_parameter_keys = ["request_id", "worker_subcode", "exit_code", "signal", "termination_origin", "measured_bytes", "allowed_bytes"]
    if list(parameters) != expected_parameter_keys or parameters["request_id"] != {"type": "absent"}:
        fail("preallocation timeout request_id is not exactly tagged absent")
    if candidate["parameters"] != parameters or candidate["code"] != "worker-timeout":
        fail("preallocation timeout candidate mismatch")
    if report["outcome"] != "timed-out" or report["observations"]:
        fail("preallocation timeout report mismatch")
    for cut in ("equal", "after"):
        row = state[cut]
        if row["request_id"] != {"type": "absent"} or any(row[name] for name in ("capabilities", "sockets", "children", "roots", "reap_records")):
            fail(f"preallocation timeout {cut} cut allocated state")
    if state["before"]["request_id"]["type"] != "id":
        fail("one-nanosecond-before cut did not allocate the real RequestId")
    scope = (ROOT / "ipc-v1/preallocation-timeout/scope.bin").read_bytes()
    subject = b"\x01\x01" + u32(len(scope)) + scope
    if scope.hex() != timeout_index["scope_hex"] or subject != (ROOT / "ipc-v1/preallocation-timeout/subject.bin").read_bytes():
        fail("preallocation timeout scope/subject bytes mismatch")


def main() -> int:
    verify_manifest()
    verify_policy_and_plans()
    verify_observation_ids()
    verify_provider_scope_inputs()
    verify_ipc()
    print("contract oracles: PASS")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, KeyError, ValueError, OSError, json.JSONDecodeError) as error:
        print(f"contract oracles: FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
