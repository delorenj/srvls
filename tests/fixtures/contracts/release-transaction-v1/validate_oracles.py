#!/usr/bin/env python3
"""Independent integrity, semantic, and Linux-reality validator for release V1."""

from __future__ import annotations

import ctypes
import copy
import errno
import fcntl
import hashlib
import os
from pathlib import Path
import re
import select
import signal
import sys
import time
from typing import Any
import unicodedata
import uuid


ROOT = Path(__file__).resolve().parent
CONTRACT_ROOT = ROOT.parent
if str(CONTRACT_ROOT) not in sys.path:
    sys.path.insert(0, str(CONTRACT_ROOT))

from canonical_json_v1 import (  # noqa: E402
    CanonicalJsonError,
    CanonicalPercentError,
    canonical_json_bytes,
    parse_canonical_json,
    percent_decode,
    percent_decode_linux_path,
    percent_encode,
    validate_negative_vectors,
)


REPO_ROOT = ROOT.parents[3]
ARCHITECTURE_SPINE = (
    REPO_ROOT
    / "_bmad-output/planning-artifacts/architecture/"
    "architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md"
)
EXPECTED_ARCHITECTURE_BODY_SHA256 = (
    "06df98f6d201abd47289d6c6771e15b83fb9d8a6c856a3a67e2e20e178a670aa"
)
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
    "rollback_target",
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
ABSENT_UNIT_KEYS = [
    "schema_version",
    "pair_id",
    "unit_kind",
    "unit_name",
    "fragment",
    "drop_ins",
    "enablement_links",
    "drop_in_directories",
]
REGULAR_REMOVAL_KEYS = ["path", "expected_sha256"]
SYMLINK_REMOVAL_KEYS = ["path", "expected_target"]
DIRECTORY_REMOVAL_KEYS = ["path", "prior_state"]
PATH_EVIDENCE_KEYS = ["kind", "path", "state", "sha256", "symlink_target"]
CONSUMER_CONTRACT_KEYS = [
    "schema_version",
    "pair_id",
    "service",
    "timer",
    "enablement",
    "contract_hash",
]
SERVICE_CONTRACT_KEYS = ["unit_name", "fragment", "exec_start", "remain_after_exit"]
TIMER_CONTRACT_KEYS = [
    "unit_name",
    "fragment",
    "target_unit",
    "timers_monotonic",
    "timers_calendar",
    "on_clock_change",
    "on_timezone_change",
    "accuracy_usec",
    "randomized_delay_usec",
    "fixed_random_delay",
    "persistent",
    "wake_system",
    "remain_after_elapse",
    "defer_reactivation",
]
FRAGMENT_IDENTITY_KEYS = [
    "fragment_path",
    "fragment_content",
    "fragment_size_bytes",
    "fragment_sha256",
    "source_path",
    "drop_ins",
]
DROP_IN_IDENTITY_KEYS = ["path", "content", "size_bytes", "sha256"]
EXEC_START_KEYS = ["binary_path", "argv", "ignore_failure"]
TIMER_MONOTONIC_KEYS = ["base", "offset_usec"]
TIMER_CALENDAR_KEYS = ["base", "expression"]
ENABLEMENT_KEYS = [
    "unit_name",
    "mutation",
    "readback",
]
MUTATION_KEYS = ["operation", "runtime", "force"]
DBUS_READBACK_KEYS = ["kind", "unit_file_state"]
SYSTEMCTL_READBACK_KEYS = ["kind", "stdout_bytes", "exit_status"]
INSTALLED_RELEASE_KEYS = [
    "kind",
    "binary",
    "state_backup",
    "consumer_contracts",
    "release_tarball_sha256",
    "stable_toolchain_evidence_sha256",
    "install_generation",
    "bundle_hash",
]
STATE_BACKUP_KEYS = [
    "schema_version",
    "method",
    "source_database_path",
    "backup_database_path",
    "source_schema",
    "target_schema",
    "source_files",
    "backup_files",
    "integrity_result",
    "no_live_restore_connections",
    "file_fsync",
    "directory_fsync",
    "manifest_hash",
]
STATE_BACKUP_PLAN_KEYS = [
    "schema_version",
    "transaction_id",
    "backup_database_path",
    "source_schema",
    "target_schema",
]
CURRENT_CURSOR_KEYS = ["sequence", "step", "effect_attempt"]
ADMISSION_KEYS = [
    "schema_version",
    "install_generation",
    "status",
    "transaction_id",
    "checksum",
]
KNOWN_GOOD_KEYS = ["schema_version", "payload", "checksum"]
KNOWN_GOOD_PAYLOAD_KEYS = [
    "source_transaction_id",
    "published_install_generation",
    "candidate",
]
FD4_REQUEST_KEYS = [
    "protocol",
    "request_id",
    "capability",
    "transaction_id",
    "recovery_attempt_id",
    "recovery_attempt_sequence",
    "manifest_revision",
    "manifest_checksum",
    "old_install_generation",
    "candidate_install_generation",
    "candidate_binary_sha256",
    "database_path",
    "allowed_database_schema",
    "backup_manifest_hash",
    "absolute_deadline_boot_ns",
    "mode",
]
FD4_RESULT_KEYS = [
    "protocol",
    "request_id",
    "capability",
    "transaction_id",
    "recovery_attempt_id",
    "recovery_attempt_sequence",
    "manifest_revision",
    "manifest_checksum",
    "candidate_install_generation",
    "candidate_binary_sha256",
    "result",
]
OWNER_KEYS = [
    "boot_identity",
    "pid",
    "process_start_ticks",
    "executable_device",
    "executable_inode",
]
VALIDATION_ATTEMPT_KEYS = [
    "schema_version",
    "recovery_attempt_id",
    "recovery_attempt_sequence",
    "effect_attempt",
    "start_boot_ns",
    "timeout_ns",
    "absolute_deadline_boot_ns",
]
MATCH_RULE_KEYS = [
    "sequence",
    "sender",
    "path",
    "interface",
    "member",
    "arg0",
    "ack_boot_ns",
]
HANDSHAKE_KEYS = [
    "schema_version",
    "bus_scope",
    "client_unique_name",
    "manager_well_known_name",
    "manager_unique_owner",
    "match_rules",
    "subscribe_reply_owner",
    "owner_recheck",
    "drain_barrier_boot_ns",
    "status",
]
TIMER_BASELINE_KEYS = [
    "last_trigger_usec_monotonic",
    "invocation_id",
    "start_usec_monotonic",
    "captured_boot_ns",
]
TIMER_ACCEPTANCE_KEYS = [
    "schema_version",
    "validation_attempt",
    "handshake",
    "timer_unit",
    "service_unit",
    "baseline",
    "trigger_mode",
    "causality_proof",
    "terminal_sample",
]
TIMER_CAUSALITY_KEYS = [
    "schema_version",
    "manager_boot_id",
    "timer_unit",
    "service_unit",
    "job_id",
    "job_path",
    "job_type",
    "activation_details",
    "baseline_last_trigger_usec_monotonic",
    "accepted_last_trigger_usec_monotonic",
    "baseline_invocation_id",
    "accepted_invocation_id",
    "baseline_start_usec_monotonic",
    "accepted_start_usec_monotonic",
    "job_removed_result",
    "observation_boot_ns",
]
ACTIVATION_DETAIL_KEYS = ["key", "value"]
TIMER_TERMINAL_KEYS = [
    "invocation_id",
    "start_usec_monotonic",
    "result",
    "exec_main_code",
    "exec_main_status",
    "observed_boot_ns",
]
STATE_FILE_KEYS = ["role", "path", "disposition", "size_bytes", "sha256"]
RELEASE_PATHS_KEYS = [
    "canonical_link_path",
    "prior_versioned_binary_path",
    "candidate_versioned_binary_path",
    "database_path",
    "transaction_manifest_path",
    "known_good_path",
]
BINARY_ARTIFACT_KEYS = ["kind", "path", "sha256", "size_bytes"]
RELEASE_ARTIFACTS_KEYS = [
    "prior_binary",
    "candidate_binary",
    "prior_database_schema",
    "target_database_schema",
    "release_tarball_sha256",
    "stable_toolchain_evidence_sha256",
]
FIRST_INSTALL_KEYS = [
    "kind",
    "canonical_link_path",
    "versioned_binary_path",
    "state_disposition",
    "consumer_disposition",
    "prior_install_generation",
]
KNOWN_GOOD_CANDIDATE_KEYS = [
    "schema_version",
    "prior_release",
    "candidate_checksum",
]
COMMIT_DECISION_KEYS = [
    "kind",
    "candidate_checksum",
    "target_install_generation",
    "expected_known_good_checksum",
]
EVIDENCE_KEYS = {
    "path": ["kind", "path", "state", "sha256", "symlink_target"],
    "state": [
        "kind",
        "database_path",
        "schema",
        "integrity_result",
        "database_sha256",
        "wal",
        "shm",
    ],
    "backup": ["kind", "manifest_hash"],
    "admission": ["kind", "status", "install_generation", "transaction_id"],
    "consumer": ["kind", "pair_id", "contract_hash", "readback"],
    "timer": ["kind", "pair_id", "acceptance"],
    "fd4": ["kind", "request_id", "result", "evidence_sha256"],
    "smoke": ["kind", "artifact_sha256", "result", "stdout_sha256", "stderr_sha256"],
    "known-good": ["kind", "path", "checksum", "source_transaction_id"],
    "decision": [
        "kind",
        "candidate_checksum",
        "target_install_generation",
        "expected_known_good_checksum",
    ],
    "absence": [
        "kind",
        "canonical_link_absent",
        "versioned_binary_absent",
        "state_disposition",
        "consumer_units",
    ],
    "transaction": ["kind", "manifest_revision", "result"],
}
EVIDENCE_TAGS = {
    "path": 0x01,
    "state": 0x02,
    "backup": 0x03,
    "admission": 0x04,
    "consumer": 0x05,
    "timer": 0x06,
    "fd4": 0x07,
    "smoke": 0x08,
    "known-good": 0x09,
    "decision": 0x0A,
    "absence": 0x0B,
    "transaction": 0x0C,
}
RELEASE_REASONS = {
    "none",
    "no-prior-release",
    "resumed-after-owner-loss",
    "forward-effect-failed",
    "rollback-effect-failed",
    "checksum-mismatch",
    "smoke-failed",
    "backup-invalid",
    "migration-failed",
    "activation-mismatch",
    "consumer-contract-mismatch",
    "timer-causality-mismatch",
    "dbus-match-failed",
    "dbus-subscribe-failed",
    "dbus-owner-changed",
    "dbus-disconnected",
    "dbus-stream-discontinuity",
    "candidate-rejected",
    "deadline-expired",
    "foreign-path",
    "unknown-version",
    "recovery-readback-mismatch",
}
FD4_REJECTION_CODES = RELEASE_REASONS - {
    "none",
    "no-prior-release",
    "resumed-after-owner-loss",
}
STEP_PHASES = {
    "stage-binary": "stage",
    "verify-checksum": "checksum",
    "isolated-smoke": "smoke",
    "persist-recovering-admission": "activate",
    "create-backup": "activate",
    "migrate-and-verify-state": "activate",
    "activate-binary": "activate",
    "rewrite-consumers": "consumer-validation",
    "daemon-reload": "consumer-validation",
    "readback-consumers": "consumer-validation",
    "prove-timer-invocation": "consumer-validation",
    "validate-candidate": "consumer-validation",
    "stage-known-good-candidate": "commit",
    "commit-decided": "commit",
    "publish-known-good": "commit",
    "persist-ready-admission": "commit",
    "commit-transaction": "commit",
    "restore-binary": "recovery",
    "restore-state": "recovery",
    "restore-consumers": "recovery",
    "rollback-daemon-reload": "recovery",
    "validate-restored-pair": "recovery",
    "remove-first-install-consumers": "recovery",
    "first-install-daemon-reload": "recovery",
    "validate-first-install-absence": "recovery",
    "rollback-ready-admission": "recovery",
    "complete-rolled-back": "recovery",
}
BROWNFIELD_KEYS = [
    "schema_version",
    "source_basis",
    "source_install_generation",
    "candidate_install_generation",
    "pairs",
    "forward_pair_order",
    "rollback_pair_order",
    "forward_evidence",
    "rollback_evidence",
    "checksum",
]
BROWNFIELD_BASIS_KEYS = [
    "kind",
    "host",
    "captured_on",
    "home_substitution",
    "files",
]
BROWNFIELD_BASIS_FILE_KEYS = ["unit_name", "host_fragment_sha256"]
BROWNFIELD_PAIR_KEYS = ["pair_id", "source", "candidate"]
BROWNFIELD_FORWARD_KEYS = ["pair_id", "pre_contract_hash", "post_contract_hash"]
BROWNFIELD_ROLLBACK_KEYS = [
    "pair_id",
    "pre_contract_hash",
    "post_contract_hash",
    "reload_contract_hash",
    "validation_contract_hash",
]
TOOLCHAIN_KEYS = [
    "schema_version",
    "manifest_url",
    "manifest_date",
    "manifest_rust_release",
    "manifest_git_commit_hash",
    "rustc_component_xz_url",
    "rustc_component_xz_sha256",
    "rustc_version_verbose",
    "parsed",
    "checksum",
]
TOOLCHAIN_PARSED_KEYS = [
    "release",
    "commit_hash",
    "commit_date",
    "host",
    "llvm_version",
]
TRANSITION_FILES = {
    "forward.transitions.jsonl": (
        "ready-admission-pending.manifest.json",
        ("persist-ready-admission", "pending"),
        "committed",
    ),
    "owner-takeover.transitions.jsonl": (
        "owner-takeover-pending-validation.manifest.json",
        ("validate-candidate", "pending"),
        "committed",
    ),
    "first-install-recovery.transitions.jsonl": (
        "first-install-absent-pending-consumer-removal.manifest.json",
        ("remove-first-install-consumers", "pending"),
        "forward-failed-recovered",
    ),
    "explicit-rollback.transitions.jsonl": (
        "explicit-rollback-ready-admission-pending.manifest.json",
        ("rollback-ready-admission", "pending"),
        "rolled-back",
    ),
    "upgrade.transitions.jsonl": (
        "upgrade-ready-admission-pending.manifest.json",
        ("persist-ready-admission", "pending"),
        "committed",
    ),
    "upgrade-owner-takeover.transitions.jsonl": (
        "upgrade-owner-takeover-pending-validation.manifest.json",
        ("validate-candidate", "pending"),
        "committed",
    ),
    "upgrade-recovery.transitions.jsonl": (
        "upgrade-recovery-pending-restored-validation.manifest.json",
        ("validate-restored-pair", "pending"),
        "forward-failed-recovered",
    ),
}
CASES: dict[str, tuple[str | None, str | None, str, int, str]] = {
    "initial-transaction-created.manifest.json": (
        None,
        None,
        "first-install-absent",
        1,
        "absent",
    ),
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
    "upgrade-ready-admission-pending.manifest.json": (
        "persist-ready-admission",
        "pending",
        "installed",
        1,
        "present",
    ),
    "upgrade-owner-takeover-pending-validation.manifest.json": (
        "validate-candidate",
        "pending",
        "installed",
        2,
        "absent",
    ),
    "upgrade-recovery-pending-restored-validation.manifest.json": (
        "validate-restored-pair",
        "pending",
        "installed",
        1,
        "absent",
    ),
}

REQUIRED_POST_EVIDENCE: dict[str, set[str]] = {
    "stage-binary": {"path"},
    "verify-checksum": {"path"},
    "isolated-smoke": {"smoke"},
    "persist-recovering-admission": {"admission"},
    "create-backup": {"backup"},
    "migrate-and-verify-state": {"state"},
    "activate-binary": {"path"},
    "rewrite-consumers": {"consumer"},
    "daemon-reload": {"consumer"},
    "readback-consumers": {"consumer"},
    "prove-timer-invocation": {"timer"},
    "validate-candidate": {"fd4"},
    "stage-known-good-candidate": {"decision"},
    "commit-decided": {"decision"},
    "publish-known-good": {"known-good"},
    "persist-ready-admission": {"admission"},
    "commit-transaction": {"transaction"},
    "restore-binary": {"path"},
    "restore-state": {"state"},
    "restore-consumers": {"consumer"},
    "rollback-daemon-reload": {"consumer"},
    "validate-restored-pair": {"consumer", "timer", "fd4"},
    "remove-first-install-consumers": {"path"},
    "first-install-daemon-reload": {"consumer"},
    "validate-first-install-absence": {"absence"},
    "rollback-ready-admission": {"admission"},
    "complete-rolled-back": {"transaction"},
}

FORWARD_SEQUENCE = [
    "stage-binary",
    "verify-checksum",
    "isolated-smoke",
    "persist-recovering-admission",
    "create-backup",
    "migrate-and-verify-state",
    "activate-binary",
    "rewrite-consumers",
    "daemon-reload",
    "readback-consumers",
    "prove-timer-invocation",
    "validate-candidate",
    "stage-known-good-candidate",
    "commit-decided",
    "publish-known-good",
    "persist-ready-admission",
    "commit-transaction",
]
FIRST_INSTALL_RECOVERY_SEQUENCE = [
    "stage-binary",
    "verify-checksum",
    "isolated-smoke",
    "validate-candidate",
    "restore-binary",
    "restore-state",
    "remove-first-install-consumers",
    "first-install-daemon-reload",
    "validate-first-install-absence",
    "rollback-ready-admission",
    "complete-rolled-back",
]
INSTALLED_RECOVERY_SEQUENCE = [
    "restore-binary",
    "restore-state",
    "restore-consumers",
    "rollback-daemon-reload",
    "validate-restored-pair",
    "rollback-ready-admission",
    "complete-rolled-back",
]
EXPLICIT_ROLLBACK_SEQUENCE = [
    "persist-recovering-admission",
    "create-backup",
    "restore-binary",
    "restore-state",
    "restore-consumers",
    "rollback-daemon-reload",
    "validate-restored-pair",
    "stage-known-good-candidate",
    "commit-decided",
    "publish-known-good",
    "rollback-ready-admission",
    "complete-rolled-back",
]

# Exact evidence-kind relation for a non-skipped step. Pending rows use the
# same pre set and an empty post set; failed rows use the pre set and no post.
STEP_EVIDENCE: dict[tuple[str, str], tuple[set[str], set[str]]] = {
    ("stage-binary", "forward"): ({"path"}, {"path"}),
    ("verify-checksum", "forward"): ({"path"}, {"path"}),
    ("isolated-smoke", "forward"): ({"smoke"}, {"smoke"}),
    ("persist-recovering-admission", "forward"): ({"admission"}, {"admission"}),
    ("create-backup", "forward"): ({"backup"}, {"backup"}),
    ("migrate-and-verify-state", "forward"): ({"state"}, {"state"}),
    ("activate-binary", "forward"): ({"path"}, {"path"}),
    ("rewrite-consumers", "forward"): ({"consumer"}, {"consumer"}),
    ("daemon-reload", "forward"): ({"consumer"}, {"consumer"}),
    ("readback-consumers", "forward"): ({"consumer"}, {"consumer"}),
    ("prove-timer-invocation", "forward"): ({"timer"}, {"timer"}),
    ("validate-candidate", "forward"): ({"fd4"}, {"fd4"}),
    ("validate-candidate", "recovery"): ({"fd4"}, {"fd4"}),
    ("stage-known-good-candidate", "forward"): ({"decision"}, {"decision"}),
    ("commit-decided", "forward"): ({"decision"}, {"decision"}),
    ("publish-known-good", "forward"): ({"known-good"}, {"known-good"}),
    ("persist-ready-admission", "forward"): ({"admission"}, {"admission"}),
    ("commit-transaction", "forward"): (set(), {"transaction"}),
    ("stage-binary", "recovery"): ({"path"}, {"path"}),
    ("verify-checksum", "recovery"): ({"path"}, {"path"}),
    ("isolated-smoke", "recovery"): ({"smoke"}, {"smoke"}),
    ("persist-recovering-admission", "recovery"): (
        {"admission"},
        {"admission"},
    ),
    ("create-backup", "recovery"): ({"backup"}, {"backup"}),
    ("migrate-and-verify-state", "recovery"): ({"state"}, {"state"}),
    ("activate-binary", "recovery"): ({"path"}, {"path"}),
    ("rewrite-consumers", "recovery"): ({"consumer"}, {"consumer"}),
    ("daemon-reload", "recovery"): ({"consumer"}, {"consumer"}),
    ("readback-consumers", "recovery"): ({"consumer"}, {"consumer"}),
    ("prove-timer-invocation", "recovery"): ({"timer"}, {"timer"}),
    ("stage-known-good-candidate", "recovery"): (set(), {"decision"}),
    ("commit-decided", "recovery"): (set(), {"decision"}),
    ("publish-known-good", "recovery"): (set(), {"known-good"}),
    ("persist-ready-admission", "recovery"): (set(), {"admission"}),
    ("commit-transaction", "recovery"): (set(), {"transaction"}),
    ("restore-binary", "recovery"): ({"path"}, {"path"}),
    ("restore-state", "recovery"): ({"state"}, {"state"}),
    ("restore-consumers", "recovery"): ({"consumer"}, {"consumer"}),
    ("rollback-daemon-reload", "recovery"): ({"consumer"}, {"consumer"}),
    ("validate-restored-pair", "recovery"): (
        {"consumer", "timer", "fd4"},
        {"consumer", "timer", "fd4"},
    ),
    ("remove-first-install-consumers", "recovery"): ({"path"}, {"path"}),
    ("first-install-daemon-reload", "recovery"): (set(), {"consumer"}),
    ("validate-first-install-absence", "recovery"): (set(), {"absence"}),
    ("rollback-ready-admission", "recovery"): (set(), {"admission"}),
    ("complete-rolled-back", "recovery"): (set(), {"transaction"}),
    ("persist-recovering-admission", "explicit-rollback"): (set(), {"admission"}),
    ("create-backup", "explicit-rollback"): (set(), {"backup"}),
    ("restore-binary", "explicit-rollback"): ({"path"}, {"path"}),
    ("restore-state", "explicit-rollback"): ({"state"}, {"state"}),
    ("restore-consumers", "explicit-rollback"): ({"consumer"}, {"consumer"}),
    ("rollback-daemon-reload", "explicit-rollback"): ({"consumer"}, {"consumer"}),
    ("validate-restored-pair", "explicit-rollback"): (
        {"consumer", "timer", "fd4"},
        {"consumer", "timer", "fd4"},
    ),
    ("stage-known-good-candidate", "explicit-rollback"): (set(), {"decision"}),
    ("commit-decided", "explicit-rollback"): (set(), {"decision"}),
    ("publish-known-good", "explicit-rollback"): (set(), {"known-good"}),
    ("rollback-ready-admission", "explicit-rollback"): (set(), {"admission"}),
    ("complete-rolled-back", "explicit-rollback"): (set(), {"transaction"}),
}

SHA256_RE = re.compile(r"[0-9a-f]{64}\Z")


def fail(message: str) -> None:
    raise SystemExit(f"release oracle validation failed: {message}")


def load_exact(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    if not raw.endswith(b"\n") or raw.endswith(b"\n\n"):
        fail(f"{path.name}: expected exactly one repository line feed")
    try:
        value = parse_canonical_json(raw[:-1])
    except CanonicalJsonError as exc:
        fail(f"{path.name}: {exc}")
    if not isinstance(value, dict):
        fail(f"{path.name}: top level is not an object")
    return value


def digest(domain: str, value: Any) -> str:
    preimage = canonical_json_bytes(value)
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


def require_sha256(value: Any, context: str) -> None:
    if not isinstance(value, str) or SHA256_RE.fullmatch(value) is None:
        fail(f"{context}: expected lowercase SHA-256")


def require_unsigned(value: Any, context: str) -> None:
    if type(value) is not int or not 0 <= value <= (1 << 64) - 1:
        fail(f"{context}: expected unsigned 64-bit integer")


def require_nfc_text(value: Any, context: str) -> None:
    if not isinstance(value, str) or not value or unicodedata.normalize("NFC", value) != value:
        fail(f"{context}: expected nonempty NFC text")


def require_uuid(value: Any, context: str) -> None:
    if not isinstance(value, str) or re.fullmatch(
        r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
        value,
    ) is None:
        fail(f"{context}: expected lowercase hyphenated UUID")


def decoded_raw(value: Any, context: str) -> bytes:
    try:
        return percent_decode(value)
    except CanonicalPercentError as exc:
        fail(f"{context}: {exc}")
    raise AssertionError("unreachable")


def decoded_linux_path(value: Any, context: str) -> bytes:
    try:
        return percent_decode_linux_path(value)
    except CanonicalPercentError as exc:
        fail(f"{context}: {exc}")
    raise AssertionError("unreachable")


def decoded_canonical_content(value: Any, context: str) -> bytes:
    """Decode AD-24 raw content while rejecting every alternate spelling."""
    return decoded_raw(value, context)


def validate_owner(value: dict[str, Any], context: str) -> None:
    if list(value) != OWNER_KEYS:
        fail(f"{context}: process identity key order mismatch")
    require_uuid(value["boot_identity"], f"{context}.boot_identity")
    for key in ("pid", "process_start_ticks", "executable_device", "executable_inode"):
        require_unsigned(value[key], f"{context}.{key}")
    if value["pid"] == 0:
        fail(f"{context}: process PID is zero")


def validate_binary_artifact(
    value: dict[str, Any], context: str, expected_kind: str | None = None
) -> tuple[bytes, str, int] | None:
    if list(value) != BINARY_ARTIFACT_KEYS:
        fail(f"{context}: binary-artifact key order mismatch")
    kind = value["kind"]
    if expected_kind is not None and kind != expected_kind:
        fail(f"{context}: binary-artifact presence mismatch")
    if kind == "absent":
        if any(value[key] != {"kind": "absent"} for key in ("path", "sha256", "size_bytes")):
            fail(f"{context}: absent binary carries path/hash/size")
        return None
    if kind != "present":
        fail(f"{context}: unknown binary-artifact kind")
    for key in ("path", "sha256", "size_bytes"):
        if list(value[key]) != ["kind", "value"] or value[key].get("kind") != "present":
            fail(f"{context}: present binary lacks tagged {key}")
    path = decoded_linux_path(value["path"]["value"], f"{context}.path")
    require_sha256(value["sha256"]["value"], f"{context}.sha256")
    require_unsigned(value["size_bytes"]["value"], f"{context}.size_bytes")
    if value["size_bytes"]["value"] == 0:
        fail(f"{context}: present binary has zero size")
    return path, value["sha256"]["value"], value["size_bytes"]["value"]


def validate_release_paths_and_artifacts(
    payload: dict[str, Any], path: Path
) -> None:
    context = path.name
    paths = payload["paths"]
    if list(paths) != RELEASE_PATHS_KEYS:
        fail(f"{context}: release-paths key order mismatch")
    canonical = decoded_linux_path(paths["canonical_link_path"], f"{context}: canonical link")
    candidate_path = decoded_linux_path(
        paths["candidate_versioned_binary_path"], f"{context}: candidate path"
    )
    database_path = decoded_linux_path(paths["database_path"], f"{context}: database path")
    transaction_path = decoded_linux_path(
        paths["transaction_manifest_path"], f"{context}: transaction path"
    )
    known_good_path = decoded_linux_path(
        paths["known_good_path"], f"{context}: KnownGood path"
    )
    if len({canonical, candidate_path, database_path, transaction_path, known_good_path}) != 5:
        fail(f"{context}: release paths alias one another")
    prior_path_union = paths["prior_versioned_binary_path"]
    if prior_path_union == {"kind": "absent"}:
        prior_path = None
    elif list(prior_path_union) == ["kind", "value"] and prior_path_union.get("kind") == "present":
        prior_path = decoded_linux_path(prior_path_union["value"], f"{context}: prior path")
    else:
        fail(f"{context}: prior-versioned path tagged union mismatch")
    if canonical != b"/home/test/.local/bin/srvls":
        fail(f"{context}: canonical link path differs from the frozen Host layout")
    if database_path != b"/home/test/.local/state/srvls/state.sqlite3":
        fail(f"{context}: database path differs from the frozen Host layout")
    if transaction_path != (
        b"/home/test/.local/state/srvls/upgrade/upgrade-transaction-v1.json"
    ):
        fail(f"{context}: transaction path differs from the frozen Host layout")
    if known_good_path != b"/home/test/.local/state/srvls/upgrade/known-good-v1.json":
        fail(f"{context}: KnownGood path differs from the frozen Host layout")
    versioned_pattern = rb"/home/test/\.local/lib/srvls/[^/]+/srvls"
    if re.fullmatch(versioned_pattern, candidate_path) is None:
        fail(f"{context}: candidate binary escapes the versioned-binary layout")
    if prior_path is not None and (
        re.fullmatch(versioned_pattern, prior_path) is None
        or prior_path == candidate_path
    ):
        fail(f"{context}: prior binary path is aliased or outside its layout")

    artifacts = payload["artifacts"]
    if list(artifacts) != RELEASE_ARTIFACTS_KEYS:
        fail(f"{context}: release-artifacts key order mismatch")
    prior_binary = validate_binary_artifact(
        artifacts["prior_binary"], f"{context}: prior binary"
    )
    candidate_binary = validate_binary_artifact(
        artifacts["candidate_binary"], f"{context}: candidate binary", "present"
    )
    assert candidate_binary is not None
    if candidate_binary[0] != candidate_path:
        fail(f"{context}: candidate path differs from candidate artifact")
    if (prior_binary is None) != (prior_path is None):
        fail(f"{context}: prior path/artifact presence differs")
    if prior_binary is not None and prior_binary[0] != prior_path:
        fail(f"{context}: prior path differs from prior artifact")
    for key in ("prior_database_schema", "target_database_schema"):
        require_unsigned(artifacts[key], f"{context}: artifacts.{key}")
    require_sha256(artifacts["release_tarball_sha256"], f"{context}: tarball hash")
    require_sha256(
        artifacts["stable_toolchain_evidence_sha256"], f"{context}: toolchain hash"
    )


def validate_validation_attempt(
    value: dict[str, Any],
    context: str,
    owners: dict[str, int] | None = None,
    step: dict[str, Any] | None = None,
) -> None:
    if list(value) != VALIDATION_ATTEMPT_KEYS:
        fail(f"{context}: validation-attempt key order mismatch")
    if value["schema_version"] != "srvls-release-validation-attempt-v1":
        fail(f"{context}: validation-attempt schema mismatch")
    require_uuid(value["recovery_attempt_id"], f"{context}.recovery_attempt_id")
    for key in (
        "recovery_attempt_sequence",
        "effect_attempt",
        "start_boot_ns",
        "timeout_ns",
        "absolute_deadline_boot_ns",
    ):
        require_unsigned(value[key], f"{context}.{key}")
    if value["timeout_ns"] == 0:
        fail(f"{context}: validation timeout is zero")
    if value["start_boot_ns"] + value["timeout_ns"] != value["absolute_deadline_boot_ns"]:
        fail(f"{context}: validation deadline is not checked start plus timeout")
    if owners is not None and owners.get(value["recovery_attempt_id"]) != value[
        "recovery_attempt_sequence"
    ]:
        fail(f"{context}: validation attempt does not bind a persisted recovery owner")
    if step is not None and (
        value["recovery_attempt_id"] != step["recovery_attempt_id"]
        or value["effect_attempt"] != step["effect_attempt"]
    ):
        fail(f"{context}: validation attempt differs from its step owner/effect")


def systemd_unit_object_path(unit_name: str, context: str) -> str:
    require_nfc_text(unit_name, context)
    encoded = "".join(
        chr(byte)
        if (ord("A") <= byte <= ord("Z") or ord("a") <= byte <= ord("z") or ord("0") <= byte <= ord("9"))
        else f"_{byte:02x}"
        for byte in unit_name.encode("utf-8")
    )
    return f"/org/freedesktop/systemd1/unit/{encoded}"


def validate_invocation_id(value: Any, context: str) -> bytes:
    decoded = decoded_raw(value, context)
    if len(decoded) != 16:
        fail(f"{context}: InvocationID is not exactly 16 bytes")
    return decoded


def validate_manager_handshake(
    value: dict[str, Any],
    context: str,
    timer_unit: str,
    service_unit: str,
    validation_attempt: dict[str, Any] | None,
) -> None:
    if list(value) != HANDSHAKE_KEYS:
        fail(f"{context}: manager handshake key order mismatch")
    if (
        value["schema_version"] != "srvls-manager-subscription-handshake-v1"
        or value["bus_scope"] != "user"
        or value["manager_well_known_name"] != "org.freedesktop.systemd1"
        or value["status"] != "ready"
    ):
        fail(f"{context}: manager handshake authority drift")
    owner = value["manager_unique_owner"]
    client = value["client_unique_name"]
    if not isinstance(owner, str) or re.fullmatch(r":[0-9]+\.[0-9]+", owner) is None:
        fail(f"{context}: manager unique owner is malformed")
    if not isinstance(client, str) or re.fullmatch(r":[0-9]+\.[0-9]+", client) is None:
        fail(f"{context}: client unique name is malformed")
    if client == owner:
        fail(f"{context}: client and manager unique names are identical")
    if value["subscribe_reply_owner"] != owner or value["owner_recheck"] != owner:
        fail(f"{context}: Subscribe reply or owner recheck differs from bound owner")
    expected = [
        (
            "org.freedesktop.DBus",
            "/org/freedesktop/DBus",
            "org.freedesktop.DBus",
            "NameOwnerChanged",
            {"kind": "present", "value": "org.freedesktop.systemd1"},
        ),
        (
            owner,
            "/org/freedesktop/systemd1",
            "org.freedesktop.systemd1.Manager",
            "JobNew",
            {"kind": "absent"},
        ),
        (
            owner,
            "/org/freedesktop/systemd1",
            "org.freedesktop.systemd1.Manager",
            "JobRemoved",
            {"kind": "absent"},
        ),
        (
            owner,
            systemd_unit_object_path(timer_unit, f"{context}.timer_unit"),
            "org.freedesktop.DBus.Properties",
            "PropertiesChanged",
            {"kind": "absent"},
        ),
        (
            owner,
            systemd_unit_object_path(service_unit, f"{context}.service_unit"),
            "org.freedesktop.DBus.Properties",
            "PropertiesChanged",
            {"kind": "absent"},
        ),
    ]
    rules = value["match_rules"]
    if len(rules) != len(expected):
        fail(f"{context}: manager match-rule count mismatch")
    acknowledgements: list[int] = []
    for sequence, (rule, fields) in enumerate(zip(rules, expected)):
        if list(rule) != MATCH_RULE_KEYS or rule["sequence"] != sequence:
            fail(f"{context}: match rule {sequence} key order/sequence mismatch")
        sender, path, interface, member, arg0 = fields
        if (
            rule["sender"] != sender
            or rule["path"] != path
            or rule["interface"] != interface
            or rule["member"] != member
            or rule["arg0"] != arg0
        ):
            fail(f"{context}: match rule {sequence} authority mismatch")
        require_unsigned(rule["ack_boot_ns"], f"{context}.match_rules[{sequence}].ack_boot_ns")
        acknowledgements.append(rule["ack_boot_ns"])
    if acknowledgements != sorted(acknowledgements) or len(set(acknowledgements)) != len(
        acknowledgements
    ):
        fail(f"{context}: match acknowledgements are not strictly ordered")
    require_unsigned(value["drain_barrier_boot_ns"], f"{context}.drain_barrier_boot_ns")
    if value["drain_barrier_boot_ns"] <= acknowledgements[-1]:
        fail(f"{context}: drain barrier does not follow every match acknowledgement")
    if validation_attempt is not None:
        start = validation_attempt["start_boot_ns"]
        deadline = validation_attempt["absolute_deadline_boot_ns"]
        if acknowledgements[0] <= start or value["drain_barrier_boot_ns"] >= deadline:
            fail(f"{context}: manager handshake is outside its validation attempt")


def validate_timer_acceptance(
    value: dict[str, Any], context: str, pair_id: str
) -> None:
    if list(value) != TIMER_ACCEPTANCE_KEYS:
        fail(f"{context}: timer acceptance key order mismatch")
    if value["schema_version"] != "srvls-timer-invocation-acceptance-v1":
        fail(f"{context}: timer acceptance schema mismatch")
    attempt = value["validation_attempt"]
    validate_validation_attempt(attempt, f"{context}.validation_attempt")
    timer_unit = value["timer_unit"]
    service_unit = value["service_unit"]
    if timer_unit != f"srvls-{pair_id}.timer" or service_unit != f"srvls-{pair_id}.service":
        fail(f"{context}: timer/service units do not bind the evidence pair")
    validate_manager_handshake(
        value["handshake"],
        f"{context}.handshake",
        timer_unit,
        service_unit,
        attempt,
    )
    baseline = value["baseline"]
    if list(baseline) != TIMER_BASELINE_KEYS:
        fail(f"{context}: timer baseline key order mismatch")
    for key in ("last_trigger_usec_monotonic", "start_usec_monotonic", "captured_boot_ns"):
        require_unsigned(baseline[key], f"{context}.baseline.{key}")
    baseline_invocation = validate_invocation_id(
        baseline["invocation_id"], f"{context}.baseline.invocation_id"
    )
    if baseline["captured_boot_ns"] <= value["handshake"]["drain_barrier_boot_ns"]:
        fail(f"{context}: baseline precedes the clean subscription barrier")
    if value["trigger_mode"] not in {"force", "await"}:
        fail(f"{context}: unknown timer trigger mode")
    proof = value["causality_proof"]
    if list(proof) != TIMER_CAUSALITY_KEYS:
        fail(f"{context}: timer causality key order mismatch")
    if proof["schema_version"] != "srvls-timer-causality-proof-v1":
        fail(f"{context}: timer causality schema mismatch")
    require_uuid(proof["manager_boot_id"], f"{context}.causality.manager_boot_id")
    require_unsigned(proof["job_id"], f"{context}.causality.job_id")
    if (
        proof["timer_unit"] != timer_unit
        or proof["service_unit"] != service_unit
        or proof["job_path"] != f"/org/freedesktop/systemd1/job/{proof['job_id']}"
        or proof["job_type"] != "start"
        or proof["job_removed_result"] != "done"
    ):
        fail(f"{context}: timer causal job identity drift")
    details = proof["activation_details"]
    if not details or any(list(row) != ACTIVATION_DETAIL_KEYS for row in details):
        fail(f"{context}: activation details are empty or malformed")
    for index, row in enumerate(details):
        require_nfc_text(row["key"], f"{context}.activation_details[{index}].key")
        require_nfc_text(row["value"], f"{context}.activation_details[{index}].value")
    if details != sorted(details, key=canonical_json_bytes):
        fail(f"{context}: activation details are not canonical-byte sorted")
    if {"key": "trigger_unit", "value": timer_unit} not in details:
        fail(f"{context}: activation details lack the exact trigger_unit pair")
    for key in (
        "baseline_last_trigger_usec_monotonic",
        "accepted_last_trigger_usec_monotonic",
        "baseline_start_usec_monotonic",
        "accepted_start_usec_monotonic",
        "observation_boot_ns",
    ):
        require_unsigned(proof[key], f"{context}.causality.{key}")
    accepted_invocation = validate_invocation_id(
        proof["accepted_invocation_id"], f"{context}.causality.accepted_invocation_id"
    )
    if validate_invocation_id(
        proof["baseline_invocation_id"], f"{context}.causality.baseline_invocation_id"
    ) != baseline_invocation:
        fail(f"{context}: causal baseline invocation differs from captured baseline")
    if (
        proof["baseline_last_trigger_usec_monotonic"]
        != baseline["last_trigger_usec_monotonic"]
        or proof["baseline_start_usec_monotonic"] != baseline["start_usec_monotonic"]
        or proof["accepted_last_trigger_usec_monotonic"]
        <= proof["baseline_last_trigger_usec_monotonic"]
        or proof["accepted_start_usec_monotonic"] < proof["accepted_last_trigger_usec_monotonic"]
        or accepted_invocation == baseline_invocation
        or not any(accepted_invocation)
        or proof["observation_boot_ns"] <= baseline["captured_boot_ns"]
    ):
        fail(f"{context}: causal baseline/accepted transition mismatch")
    terminal = value["terminal_sample"]
    if list(terminal) != TIMER_TERMINAL_KEYS:
        fail(f"{context}: terminal timer sample key order mismatch")
    for key in ("start_usec_monotonic", "exec_main_status", "observed_boot_ns"):
        require_unsigned(terminal[key], f"{context}.terminal_sample.{key}")
    if (
        validate_invocation_id(
            terminal["invocation_id"], f"{context}.terminal_sample.invocation_id"
        )
        != accepted_invocation
        or terminal["start_usec_monotonic"] != proof["accepted_start_usec_monotonic"]
        or terminal["result"] != "success"
        or terminal["exec_main_code"] != "CLD_EXITED"
        or terminal["exec_main_status"] != 0
        or terminal["observed_boot_ns"] < proof["observation_boot_ns"]
    ):
        fail(f"{context}: terminal sample differs from the accepted causal job")
    if not (
        attempt["start_boot_ns"]
        < value["handshake"]["match_rules"][0]["ack_boot_ns"]
        < value["handshake"]["drain_barrier_boot_ns"]
        < baseline["captured_boot_ns"]
        < proof["observation_boot_ns"]
        <= terminal["observed_boot_ns"]
        < attempt["absolute_deadline_boot_ns"]
    ):
        fail(f"{context}: timer evidence is not strictly inside one deadline")


def validate_terminal_result(
    value: dict[str, Any], payload: dict[str, Any] | None, context: str
) -> None:
    kind = value.get("kind")
    if kind == "pending":
        if value != {"kind": "pending"}:
            fail(f"{context}: pending terminal result has inactive fields")
        return
    if kind == "committed":
        if list(value) != ["kind", "target_install_generation"]:
            fail(f"{context}: committed terminal key order mismatch")
        require_unsigned(value["target_install_generation"], f"{context}.target")
        if payload is not None:
            steps = payload["step_records"]
            if (
                payload["intent"] not in {"install", "upgrade"}
                or value["target_install_generation"]
                != payload["target_install_generation"]
                or not steps
                or steps[-1]["step"] != "commit-transaction"
                or steps[-1]["state"] != "complete"
            ):
                fail(f"{context}: committed terminal generation/direction mismatch")
        return
    if kind == "forward-failed-recovered":
        if list(value) != ["kind", "failing_step", "restored_install_generation"]:
            fail(f"{context}: recovered terminal key order mismatch")
        if value["failing_step"] not in REQUIRED_POST_EVIDENCE:
            fail(f"{context}: recovered terminal names an unknown step")
        require_unsigned(value["restored_install_generation"], f"{context}.restored")
        if payload is not None:
            failed_steps = [
                step
                for step in payload["step_records"]
                if step["state"] == "failed" and step["step"] in FORWARD_SEQUENCE
            ]
            steps = payload["step_records"]
            if (
                payload["intent"] not in {"install", "upgrade"}
                or value["restored_install_generation"]
                != payload["old_install_generation"]
                or len(failed_steps) != 1
                or failed_steps[0]["step"] != value["failing_step"]
                or not steps
                or steps[-1]["step"] != "complete-rolled-back"
                or steps[-1]["state"] != "complete"
            ):
                fail(f"{context}: recovered terminal generation/direction mismatch")
        return
    if kind == "rolled-back":
        if list(value) != [
            "kind",
            "source_install_generation",
            "target_install_generation",
        ]:
            fail(f"{context}: rolled-back terminal key order mismatch")
        require_unsigned(value["source_install_generation"], f"{context}.source")
        require_unsigned(value["target_install_generation"], f"{context}.target")
        if payload is not None:
            steps = payload["step_records"]
            if (
                payload["intent"] != "rollback"
                or value["source_install_generation"]
                != payload["old_install_generation"]
                or value["target_install_generation"]
                != payload["target_install_generation"]
                or not steps
                or steps[-1]["step"] != "complete-rolled-back"
                or steps[-1]["state"] != "complete"
            ):
                fail(f"{context}: rolled-back terminal generation/direction mismatch")
        return
    if kind == "rollback-unavailable":
        if value != {"kind": "rollback-unavailable", "reason": "no-prior-release"}:
            fail(f"{context}: rollback-unavailable terminal mismatch")
        if payload is not None:
            fail(f"{context}: rollback-unavailable cannot be transaction-embedded")
        return
    if kind == "upgrade-recovery-required":
        if list(value) != ["kind", "last_step", "reason"]:
            fail(f"{context}: recovery-required terminal key order mismatch")
        if value["last_step"] not in REQUIRED_POST_EVIDENCE or value["reason"] not in (
            RELEASE_REASONS - {"none", "no-prior-release", "resumed-after-owner-loss"}
        ):
            fail(f"{context}: recovery-required terminal step/reason mismatch")
        return
    fail(f"{context}: unknown release terminal result {kind!r}")


def validate_state_file_atom(value: dict[str, Any], role: str, context: str) -> None:
    if list(value) != STATE_FILE_KEYS or value["role"] != role:
        fail(f"{context}: state-file key order/role mismatch")
    decoded_linux_path(value["path"], f"{context}.path")
    disposition = value["disposition"]
    if disposition == "absent":
        if value["size_bytes"] != {"kind": "absent"} or value["sha256"] != {
            "kind": "absent"
        }:
            fail(f"{context}: absent state file carries size/hash")
    elif disposition in {"copied", "checkpointed"}:
        if list(value["size_bytes"]) != ["kind", "value"] or value["size_bytes"].get(
            "kind"
        ) != "present":
            fail(f"{context}: retained state file lacks a size")
        require_unsigned(value["size_bytes"]["value"], f"{context}.size_bytes")
        if value["size_bytes"]["value"] == 0:
            fail(f"{context}: retained state file has zero size")
        if list(value["sha256"]) != ["kind", "value"] or value["sha256"].get(
            "kind"
        ) != "present":
            fail(f"{context}: retained state file lacks a hash")
        require_sha256(value["sha256"]["value"], f"{context}.sha256")
    else:
        fail(f"{context}: unknown state-file disposition")


def validate_path_atom(atom: dict[str, Any], context: str) -> None:
    if list(atom) != EVIDENCE_KEYS["path"]:
        fail(f"{context}: path evidence key order mismatch")
    decoded_linux_path(atom["path"], f"{context}.path")
    state = atom["state"]
    sha256 = atom["sha256"]
    target = atom["symlink_target"]
    if state in {"absent", "directory"}:
        if sha256 != {"kind": "absent"} or target != {"kind": "absent"}:
            fail(f"{context}: {state} path carries a hash or symlink target")
    elif state == "regular":
        if list(sha256) != ["kind", "value"] or sha256.get("kind") != "present":
            fail(f"{context}: regular path lacks a present hash")
        require_sha256(sha256["value"], f"{context}.sha256")
        if target != {"kind": "absent"}:
            fail(f"{context}: regular path carries a symlink target")
    elif state == "symlink":
        if sha256 != {"kind": "absent"} or list(target) != ["kind", "value"] or target.get(
            "kind"
        ) != "present":
            fail(f"{context}: symlink path option matrix mismatch")
        if not decoded_raw(target["value"], f"{context}.symlink_target"):
            fail(f"{context}: symlink target is empty")
    else:
        fail(f"{context}: unknown path state")


def validate_evidence_atom(
    atom: dict[str, Any], payload: dict[str, Any], context: str
) -> None:
    kind = atom.get("kind")
    expected_keys = EVIDENCE_KEYS.get(kind)
    if expected_keys is None or list(atom) != expected_keys:
        fail(f"{context}: unknown evidence kind or key order")
    if kind == "path":
        validate_path_atom(atom, context)
    elif kind == "state":
        decoded_linux_path(atom["database_path"], f"{context}.database_path")
        require_unsigned(atom["schema"], f"{context}.schema")
        if atom["integrity_result"] not in {"ok", "unavailable", "failed"}:
            fail(f"{context}: unknown state integrity result")
        database_hash = atom["database_sha256"]
        if database_hash == {"kind": "absent"}:
            pass
        elif list(database_hash) == ["kind", "value"] and database_hash.get(
            "kind"
        ) == "present":
            require_sha256(database_hash["value"], f"{context}.database_sha256")
        else:
            fail(f"{context}: database hash tagged union mismatch")
        validate_state_file_atom(atom["wal"], "wal", f"{context}.wal")
        validate_state_file_atom(atom["shm"], "shm", f"{context}.shm")
    elif kind == "backup":
        require_sha256(atom["manifest_hash"], f"{context}.manifest_hash")
    elif kind == "admission":
        if atom["status"] not in {"ready", "recovering"}:
            fail(f"{context}: unknown admission status")
        require_unsigned(atom["install_generation"], f"{context}.install_generation")
        transaction = atom["transaction_id"]
        if atom["status"] == "ready":
            if transaction != {"kind": "absent"}:
                fail(f"{context}: ready admission carries a transaction")
        elif list(transaction) != ["kind", "value"] or transaction.get("kind") != "present":
            fail(f"{context}: recovering admission lacks a transaction")
        else:
            require_uuid(transaction["value"], f"{context}.transaction_id")
    elif kind == "consumer":
        if not isinstance(atom["pair_id"], str) or re.fullmatch(
            r"[a-z0-9][a-z0-9-]*", atom["pair_id"]
        ) is None:
            fail(f"{context}: consumer pair ID is not stable ASCII")
        require_sha256(atom["contract_hash"], f"{context}.contract_hash")
        if atom["readback"] not in {"intended", "loaded-match", "absent"}:
            fail(f"{context}: unknown consumer readback")
    elif kind == "timer":
        if not isinstance(atom["pair_id"], str) or re.fullmatch(
            r"[a-z0-9][a-z0-9-]*", atom["pair_id"]
        ) is None:
            fail(f"{context}: timer pair ID is not stable ASCII")
        validate_timer_acceptance(atom["acceptance"], f"{context}.acceptance", atom["pair_id"])
    elif kind == "fd4":
        require_uuid(atom["request_id"], f"{context}.request_id")
        if atom["result"] not in {"validated", "rejected"}:
            fail(f"{context}: unknown FD4 evidence result")
        require_sha256(atom["evidence_sha256"], f"{context}.evidence_sha256")
    elif kind == "smoke":
        for key in ("artifact_sha256", "stdout_sha256", "stderr_sha256"):
            require_sha256(atom[key], f"{context}.{key}")
        if atom["result"] not in {"passed", "failed"}:
            fail(f"{context}: unknown smoke result")
    elif kind == "known-good":
        decoded_linux_path(atom["path"], f"{context}.path")
        require_sha256(atom["checksum"], f"{context}.checksum")
        require_uuid(atom["source_transaction_id"], f"{context}.source_transaction_id")
    elif kind == "decision":
        require_sha256(atom["candidate_checksum"], f"{context}.candidate_checksum")
        require_unsigned(atom["target_install_generation"], f"{context}.target_generation")
        require_sha256(
            atom["expected_known_good_checksum"], f"{context}.expected_known_good_checksum"
        )
    elif kind == "absence":
        if type(atom["canonical_link_absent"]) is not bool or type(
            atom["versioned_binary_absent"]
        ) is not bool:
            fail(f"{context}: absence flags are not booleans")
        state = atom["state_disposition"]
        if state == {"kind": "absent"}:
            pass
        elif list(state) == ["kind", "backup_manifest", "schema"] and state.get(
            "kind"
        ) == "restore-recorded":
            validate_state_backup(state["backup_manifest"], Path("evidence"), context)
            require_unsigned(state["schema"], f"{context}.state_schema")
        else:
            fail(f"{context}: absence state disposition mismatch")
        units = atom["consumer_units"]
        names: list[str] = []
        for index, unit in enumerate(units):
            if list(unit) != ["unit_name", "paths_absent", "unit_file_state"]:
                fail(f"{context}: absence unit {index} key order mismatch")
            require_nfc_text(unit["unit_name"], f"{context}.consumer_units[{index}].unit_name")
            if unit["paths_absent"] is not True or unit[
                "unit_file_state"
            ] != "no-such-unit-file":
                fail(f"{context}: absence unit {index} readback mismatch")
            names.append(unit["unit_name"])
        if not names or names != sorted(names) or len(names) != len(set(names)):
            fail(f"{context}: absence units are not sorted and unique")
    elif kind == "transaction":
        require_unsigned(atom["manifest_revision"], f"{context}.manifest_revision")
        validate_terminal_result(atom["result"], payload, f"{context}.result")


def evidence_sort_key(atom: dict[str, Any]) -> tuple[int, bytes, bytes]:
    kind = atom["kind"]
    if kind == "path":
        primary = decoded_raw(atom["path"], "evidence sort path")
    elif kind == "state":
        primary = decoded_raw(atom["database_path"], "evidence sort database")
    elif kind == "backup":
        primary = bytes.fromhex(atom["manifest_hash"])
    elif kind == "admission":
        primary = atom["install_generation"].to_bytes(8, "big") + canonical_json_bytes(
            atom["transaction_id"]
        )
    elif kind in {"consumer", "timer"}:
        primary = atom["pair_id"].encode("utf-8")
    elif kind == "fd4":
        primary = uuid.UUID(atom["request_id"]).bytes
    elif kind == "smoke":
        primary = bytes.fromhex(atom["artifact_sha256"])
    elif kind == "known-good":
        primary = decoded_raw(atom["path"], "evidence sort KnownGood path")
    elif kind == "decision":
        primary = bytes.fromhex(atom["candidate_checksum"])
    elif kind == "absence":
        primary = b"\0"
    elif kind == "transaction":
        primary = atom["manifest_revision"].to_bytes(8, "big")
    else:
        raise AssertionError(kind)
    return EVIDENCE_TAGS[kind], primary, canonical_json_bytes(atom)


def validate_evidence_array(
    atoms: list[dict[str, Any]], payload: dict[str, Any], context: str
) -> None:
    if not isinstance(atoms, list):
        fail(f"{context}: evidence is not an array")
    for index, atom in enumerate(atoms):
        if not isinstance(atom, dict):
            fail(f"{context}: evidence atom {index} is not an object")
        validate_evidence_atom(atom, payload, f"{context}[{index}]")
    if atoms != sorted(atoms, key=evidence_sort_key):
        fail(f"{context}: evidence atoms are not in canonical tag/identity order")
    encoded = [canonical_json_bytes(atom) for atom in atoms]
    if len(encoded) != len(set(encoded)):
        fail(f"{context}: duplicate evidence atom")
    singleton_kinds = {
        "state",
        "backup",
        "admission",
        "fd4",
        "smoke",
        "known-good",
        "decision",
        "absence",
        "transaction",
    }
    for kind in singleton_kinds:
        if sum(atom["kind"] == kind for atom in atoms) > 1:
            fail(f"{context}: repeated singleton {kind} evidence")
    path_identities = [
        decoded_linux_path(atom["path"], f"{context}: path identity")
        for atom in atoms
        if atom["kind"] == "path"
    ]
    if len(path_identities) != len(set(path_identities)):
        fail(f"{context}: repeated path evidence identity")
    for kind in ("consumer", "timer"):
        pair_ids = [atom["pair_id"] for atom in atoms if atom["kind"] == kind]
        if len(pair_ids) != len(set(pair_ids)):
            fail(f"{context}: repeated {kind} pair evidence")


def validate_content_identity(
    content: Any, size_bytes: Any, sha256: Any, context: str
) -> None:
    decoded = decoded_canonical_content(content, f"{context}.content")
    require_unsigned(size_bytes, f"{context}.size_bytes")
    if size_bytes != len(decoded):
        fail(f"{context}: decoded content size mismatch")
    require_sha256(sha256, f"{context}.sha256")
    if hashlib.sha256(decoded).hexdigest() != sha256:
        fail(f"{context}: decoded content SHA-256 mismatch")


def validate_fragment_identity(value: dict[str, Any], context: str) -> None:
    if list(value) != FRAGMENT_IDENTITY_KEYS:
        fail(f"{context}: fragment identity key order mismatch")
    decoded_linux_path(value["fragment_path"], f"{context}.fragment_path")
    validate_content_identity(
        value["fragment_content"],
        value["fragment_size_bytes"],
        value["fragment_sha256"],
        f"{context}.fragment",
    )
    source = value["source_path"]
    if source == {"kind": "absent"}:
        pass
    elif list(source) == ["kind", "value"] and source.get("kind") == "present":
        decoded_linux_path(source["value"], f"{context}.source_path")
    else:
        fail(f"{context}: source path tagged union mismatch")
    drop_ins = value["drop_ins"]
    require_sorted_paths(drop_ins, f"{context}.drop_ins")
    for index, drop_in in enumerate(drop_ins):
        drop_context = f"{context}.drop_ins[{index}]"
        if list(drop_in) != DROP_IN_IDENTITY_KEYS:
            fail(f"{drop_context}: drop-in identity key order mismatch")
        decoded_linux_path(drop_in["path"], f"{drop_context}.path")
        validate_content_identity(
            drop_in["content"],
            drop_in["size_bytes"],
            drop_in["sha256"],
            drop_context,
        )


def validate_enablement(value: dict[str, Any], context: str) -> None:
    if list(value) != ENABLEMENT_KEYS:
        fail(f"{context}: enablement key order mismatch")
    mutation = value["mutation"]
    if list(mutation) != MUTATION_KEYS:
        fail(f"{context}: unit-file mutation key order mismatch")
    operation = mutation["operation"]
    if operation not in {"none", "enable", "disable", "mask", "unmask"}:
        fail(f"{context}: unknown unit-file mutation")
    if type(mutation["runtime"]) is not bool or type(mutation["force"]) is not bool:
        fail(f"{context}: mutation flags are not booleans")
    if operation in {"none", "disable", "unmask"} and mutation["force"]:
        fail(f"{context}: forbidden force flag for {operation}")
    readback = value["readback"]
    if readback.get("kind") == "dbus-unit-file-state":
        if list(readback) != DBUS_READBACK_KEYS or readback["unit_file_state"] not in {
            "enabled",
            "enabled-runtime",
            "linked",
            "linked-runtime",
            "alias",
            "static",
            "disabled",
            "indirect",
            "generated",
            "transient",
            "masked",
            "masked-runtime",
            "bad",
            "not-found",
        }:
            fail(f"{context}: malformed D-Bus unit-file readback")
    elif readback.get("kind") == "systemctl-one-unit":
        if list(readback) != SYSTEMCTL_READBACK_KEYS:
            fail(f"{context}: systemctl readback key order mismatch")
        decoded = decoded_canonical_content(
            readback["stdout_bytes"], f"{context}.stdout_bytes"
        )
        if not decoded.endswith(b"\n"):
            fail(f"{context}: systemctl stdout does not retain its line feed")
        if type(readback["exit_status"]) is not int or not 0 <= readback["exit_status"] <= 255:
            fail(f"{context}: systemctl exit status is not u8")
    else:
        fail(f"{context}: unknown unit-file readback kind")


def validate_consumer_contract(value: dict[str, Any], context: str) -> None:
    if list(value) != CONSUMER_CONTRACT_KEYS:
        fail(f"{context}: consumer contract key order mismatch")
    if value["schema_version"] != "srvls-managed-consumer-unit-contract-v1":
        fail(f"{context}: consumer contract schema mismatch")
    pair_id = value["pair_id"]
    if not isinstance(pair_id, str) or re.fullmatch(r"[a-z0-9][a-z0-9-]*", pair_id) is None:
        fail(f"{context}: pair ID is not stable ASCII")
    service = value["service"]
    timer = value["timer"]
    if list(service) != SERVICE_CONTRACT_KEYS:
        fail(f"{context}: service contract key order mismatch")
    if list(timer) != TIMER_CONTRACT_KEYS:
        fail(f"{context}: timer contract key order mismatch")
    require_nfc_text(service["unit_name"], f"{context}.service.unit_name")
    require_nfc_text(timer["unit_name"], f"{context}.timer.unit_name")
    if not service["unit_name"].endswith(".service"):
        fail(f"{context}: service unit name lacks .service suffix")
    if not timer["unit_name"].endswith(".timer"):
        fail(f"{context}: timer unit name lacks .timer suffix")
    validate_fragment_identity(service["fragment"], f"{context}.service")
    validate_fragment_identity(timer["fragment"], f"{context}.timer")
    if not service["exec_start"] or any(
        list(command) != EXEC_START_KEYS for command in service["exec_start"]
    ):
        fail(f"{context}: ExecStart contract is empty or malformed")
    for index, command in enumerate(service["exec_start"]):
        command_context = f"{context}.service.exec_start[{index}]"
        decoded_linux_path(command["binary_path"], f"{command_context}.binary_path")
        if not isinstance(command["argv"], list):
            fail(f"{command_context}: argv is not an ordered list")
        for argv_index, argument in enumerate(command["argv"]):
            decoded_raw(argument, f"{command_context}.argv[{argv_index}]")
        if type(command["ignore_failure"]) is not bool:
            fail(f"{command_context}: ignore_failure is not boolean")
    if service["remain_after_exit"] is not False:
        fail(f"{context}: service RemainAfterExit must be false")
    if timer["target_unit"] != service["unit_name"]:
        fail(f"{context}: timer target differs from service unit")
    monotonic = timer["timers_monotonic"]
    calendar = timer["timers_calendar"]
    if not isinstance(monotonic, list) or any(
        not isinstance(row, dict) or list(row) != TIMER_MONOTONIC_KEYS
        for row in monotonic
    ):
        fail(f"{context}: monotonic timer rows are malformed")
    if not isinstance(calendar, list) or any(
        not isinstance(row, dict) or list(row) != TIMER_CALENDAR_KEYS
        for row in calendar
    ):
        fail(f"{context}: calendar timer rows are malformed")
    for index, row in enumerate(monotonic):
        require_nfc_text(row["base"], f"{context}.timer.timers_monotonic[{index}].base")
        require_unsigned(
            row["offset_usec"],
            f"{context}.timer.timers_monotonic[{index}].offset_usec",
        )
    for index, row in enumerate(calendar):
        require_nfc_text(row["base"], f"{context}.timer.timers_calendar[{index}].base")
        require_nfc_text(
            row["expression"],
            f"{context}.timer.timers_calendar[{index}].expression",
        )
    if monotonic != sorted(monotonic, key=canonical_json_bytes):
        fail(f"{context}: monotonic timer rows are not canonical-byte sorted")
    if calendar != sorted(calendar, key=canonical_json_bytes):
        fail(f"{context}: calendar timer rows are not canonical-byte sorted")
    for field in ("accuracy_usec", "randomized_delay_usec"):
        require_unsigned(timer[field], f"{context}.timer.{field}")
    for field in (
        "on_clock_change",
        "on_timezone_change",
        "fixed_random_delay",
        "persistent",
        "wake_system",
        "remain_after_elapse",
        "defer_reactivation",
    ):
        if type(timer[field]) is not bool:
            fail(f"{context}.timer.{field}: expected boolean")
    enablement = value["enablement"]
    if len(enablement) != 2:
        fail(f"{context}: enablement contract is not the exact two-row schema")
    for index, row in enumerate(enablement):
        validate_enablement(row, f"{context}.enablement[{index}]")
    if [row["unit_name"] for row in enablement] != [
        service["unit_name"],
        timer["unit_name"],
    ]:
        fail(f"{context}: enablement rows are not service then timer")
    if enablement[0]["readback"].get("kind") != "dbus-unit-file-state":
        fail(f"{context}: service does not exercise D-Bus readback")
    if enablement[1]["readback"].get("kind") != "systemctl-one-unit":
        fail(f"{context}: timer does not exercise one-unit systemctl readback")
    expected = digest(
        "srvls-managed-consumer-unit-contract-v1",
        without(value, "contract_hash"),
    )
    if value["contract_hash"] != expected:
        fail(f"{context}: consumer contract hash mismatch")


def expect_contract_rejected(value: dict[str, Any], label: str) -> None:
    try:
        validate_consumer_contract(value, f"negative oracle {label}")
    except SystemExit:
        return
    fail(f"negative consumer oracle accepted {label}")


def validate_consumer_negative_oracles(contract: dict[str, Any]) -> None:
    """Prove hash-only and mismatched contracts fail without product code."""
    fragment_hash_only = copy.deepcopy(contract)
    fragment_hash_only["service"]["fragment"].pop("fragment_content")
    fragment_hash_only["service"]["fragment"].pop("fragment_size_bytes")
    expect_contract_rejected(fragment_hash_only, "hash-only-fragment")

    drop_in_hash_only = copy.deepcopy(contract)
    drop_in_hash_only["service"]["fragment"]["drop_ins"][0].pop("content")
    drop_in_hash_only["service"]["fragment"]["drop_ins"][0].pop("size_bytes")
    expect_contract_rejected(drop_in_hash_only, "hash-only-drop-in")

    mismatched_content = copy.deepcopy(contract)
    mismatched_content["service"]["fragment"]["fragment_content"] += "%0A"
    expect_contract_rejected(mismatched_content, "fragment-content-mismatch")

    mismatched_size = copy.deepcopy(contract)
    mismatched_size["service"]["fragment"]["fragment_size_bytes"] += 1
    expect_contract_rejected(mismatched_size, "fragment-size-mismatch")

    mismatched_hash = copy.deepcopy(contract)
    mismatched_hash["service"]["fragment"]["fragment_sha256"] = "0" * 64
    expect_contract_rejected(mismatched_hash, "fragment-hash-mismatch")

    mismatched_drop_in = copy.deepcopy(contract)
    mismatched_drop_in["service"]["fragment"]["drop_ins"][0]["content"] += "%0A"
    expect_contract_rejected(mismatched_drop_in, "drop-in-content-mismatch")

    overescaped_content = copy.deepcopy(contract)
    fragment = overescaped_content["service"]["fragment"]
    fragment["fragment_content"] = fragment["fragment_content"].replace(
        "srvls", "%73rvls", 1
    )
    expect_contract_rejected(overescaped_content, "noncanonical-content-encoding")

    contract_hash_stale = copy.deepcopy(contract)
    fragment = contract_hash_stale["service"]["fragment"]
    fragment["fragment_content"] += "%0A"
    fragment["fragment_size_bytes"] += 1
    fragment["fragment_sha256"] = hashlib.sha256(
        decoded_canonical_content(fragment["fragment_content"], "negative content")
    ).hexdigest()
    expect_contract_rejected(contract_hash_stale, "content-not-bound-to-contract-hash")

    reversed_schedule = copy.deepcopy(contract)
    reversed_schedule["timer"]["timers_monotonic"].reverse()
    reversed_schedule["contract_hash"] = digest(
        "srvls-managed-consumer-unit-contract-v1",
        without(reversed_schedule, "contract_hash"),
    )
    expect_contract_rejected(reversed_schedule, "rehashed-reversed-timer-schedule")

    string_accuracy = copy.deepcopy(contract)
    string_accuracy["timer"]["accuracy_usec"] = "60000000"
    string_accuracy["contract_hash"] = digest(
        "srvls-managed-consumer-unit-contract-v1",
        without(string_accuracy, "contract_hash"),
    )
    expect_contract_rejected(string_accuracy, "rehashed-string-accuracy")

    string_persistence = copy.deepcopy(contract)
    string_persistence["timer"]["persistent"] = "false"
    string_persistence["contract_hash"] = digest(
        "srvls-managed-consumer-unit-contract-v1",
        without(string_persistence, "contract_hash"),
    )
    expect_contract_rejected(string_persistence, "rehashed-string-persistence")

    string_ignore_failure = copy.deepcopy(contract)
    string_ignore_failure["service"]["exec_start"][0]["ignore_failure"] = "false"
    string_ignore_failure["contract_hash"] = digest(
        "srvls-managed-consumer-unit-contract-v1",
        without(string_ignore_failure, "contract_hash"),
    )
    expect_contract_rejected(string_ignore_failure, "rehashed-string-ignore-failure")


def require_sorted_paths(rows: list[dict[str, Any]], context: str) -> None:
    decoded = [decoded_linux_path(row["path"], f"{context}.path") for row in rows]
    if decoded != sorted(decoded) or len(decoded) != len(set(decoded)):
        fail(f"{context}: paths are not decoded-byte sorted and unique")


def validate_tagged_presence(root: dict[str, Any], path: Path) -> None:
    exempt_shapes = {
        ("kind", "path", "sha256", "size_bytes"),
        ("kind", "units"),
    }
    for value in walk(root):
        if value.get("kind") not in {"absent", "present"}:
            continue
        keys = tuple(value)
        if keys in exempt_shapes:
            continue
        expected = ("kind",) if value["kind"] == "absent" else ("kind", "value")
        if keys != expected:
            fail(f"{path.name}: malformed global tagged-presence object {keys!r}")


def validate_path_evidence(root: dict[str, Any], path: Path) -> None:
    """Enforce the closed ReleaseEvidenceAtomV1 path-state option matrix."""
    for atom in walk(root["payload"]["step_records"]):
        if atom.get("kind") != "path":
            continue
        context = f"{path.name}: path evidence"
        if list(atom) != PATH_EVIDENCE_KEYS:
            fail(f"{context}: key order mismatch")
        decoded_linux_path(atom["path"], f"{context}.path")
        state = atom["state"]
        sha256 = atom["sha256"]
        target = atom["symlink_target"]
        if state in {"absent", "directory"}:
            if sha256 != {"kind": "absent"} or target != {"kind": "absent"}:
                fail(f"{context}: {state} carries a hash or symlink target")
        elif state == "regular":
            if list(sha256) != ["kind", "value"] or sha256["kind"] != "present":
                fail(f"{context}: regular file lacks a present hash")
            require_sha256(sha256["value"], f"{context}.sha256")
            if target != {"kind": "absent"}:
                fail(f"{context}: regular file carries a symlink target")
        elif state == "symlink":
            if sha256 != {"kind": "absent"}:
                fail(f"{context}: symlink carries a hash")
            if list(target) != ["kind", "value"] or target["kind"] != "present":
                fail(f"{context}: symlink lacks a present raw readlink target")
            if not decoded_raw(target["value"], f"{context}.symlink_target"):
                fail(f"{context}: symlink target is empty")
        else:
            fail(f"{context}: unknown path state {state!r}")


def validate_regular_removal(value: dict[str, Any], context: str) -> None:
    if list(value) != REGULAR_REMOVAL_KEYS:
        fail(f"{context}: regular-removal key order mismatch")
    decoded_linux_path(value["path"], f"{context}.path")
    require_sha256(value["expected_sha256"], f"{context}.expected_sha256")


def validate_symlink_removal(value: dict[str, Any], context: str) -> None:
    if list(value) != SYMLINK_REMOVAL_KEYS:
        fail(f"{context}: symlink-removal key order mismatch")
    decoded_linux_path(value["path"], f"{context}.path")
    if not decoded_raw(value["expected_target"], f"{context}.expected_target"):
        fail(f"{context}: expected symlink target is empty")


def validate_directory_removal(value: dict[str, Any], context: str) -> None:
    if list(value) != DIRECTORY_REMOVAL_KEYS:
        fail(f"{context}: directory-removal key order mismatch")
    decoded_linux_path(value["path"], f"{context}.path")
    if value["prior_state"] not in {"absent", "directory"}:
        fail(f"{context}: unknown prior directory state")


def direct_parent(path: str, context: str) -> bytes:
    decoded = decoded_linux_path(path, context)
    parent, separator, name = decoded.rpartition(b"/")
    if separator != b"/" or not parent or not name:
        fail(f"{context}: managed path has no direct absolute parent")
    return parent


def validate_state_backup(
    value: dict[str, Any],
    path: Path,
    context: str,
    *,
    expected_database_path: str | None = None,
    expected_transaction_id: str | None = None,
    expected_source_schema: int | None = None,
    expected_target_schema: int | None = None,
) -> None:
    if list(value) != STATE_BACKUP_KEYS:
        fail(f"{path.name}: {context} key order mismatch")
    if value["schema_version"] != "srvls-state-backup-manifest-v1":
        fail(f"{path.name}: {context} schema mismatch")
    if value["method"] not in {"sqlite-backup-api", "checkpointed-equivalent"}:
        fail(f"{path.name}: {context} method mismatch")
    if value["integrity_result"] != "ok" or any(
        type(value[key]) is not bool or value[key] is not True
        for key in ("no_live_restore_connections", "file_fsync", "directory_fsync")
    ):
        fail(f"{path.name}: {context} durability/integrity proof mismatch")
    for key in ("source_schema", "target_schema"):
        require_unsigned(value[key], f"{path.name}: {context}.{key}")
    if expected_source_schema is not None and value["source_schema"] != expected_source_schema:
        fail(f"{path.name}: {context} source schema differs from transaction")
    if expected_target_schema is not None and value["target_schema"] != expected_target_schema:
        fail(f"{path.name}: {context} target schema differs from transaction")
    source_path = decoded_linux_path(
        value["source_database_path"], f"{context}.source_database_path"
    )
    if expected_database_path is not None and value["source_database_path"] != expected_database_path:
        fail(f"{path.name}: {context} source database differs from transaction path")
    backup_path = decoded_linux_path(
        value["backup_database_path"], f"{context}.backup_database_path"
    )
    match = re.fullmatch(
        rb"/home/test/\.local/state/srvls/upgrade/backups/"
        rb"(?P<transaction>[0-9a-f-]{36})/state\.sqlite3",
        backup_path,
    )
    if match is None:
        fail(f"{path.name}: {context} is not under a transaction-unique backup path")
    transaction_component = match.group("transaction").decode("ascii")
    require_uuid(transaction_component, f"{path.name}: {context}.backup transaction")
    if expected_transaction_id is not None and transaction_component != expected_transaction_id:
        fail(f"{path.name}: {context} backup path names another transaction")
    backup_parent = backup_path.rpartition(b"/")[0]
    expected_paths = {
        "source_files": [source_path, source_path + b"-wal", source_path + b"-shm"],
        "backup_files": [backup_path, backup_path + b"-wal", backup_path + b"-shm"],
    }
    for rows_name in ("source_files", "backup_files"):
        rows = value[rows_name]
        if [row.get("role") for row in rows] != ["database", "wal", "shm"]:
            fail(f"{path.name}: {context}.{rows_name} role order mismatch")
        for index, (role, row) in enumerate(zip(("database", "wal", "shm"), rows)):
            validate_state_file_atom(row, role, f"{context}.{rows_name}[{index}]")
            row_path = decoded_linux_path(
                row["path"], f"{context}.{rows_name}[{index}].path"
            )
            if row_path != expected_paths[rows_name][index]:
                fail(f"{path.name}: {context}.{rows_name} path relation mismatch")
            if rows_name == "backup_files" and row_path.rpartition(b"/")[0] != backup_parent:
                fail(f"{path.name}: backup file escapes its immutable bundle directory")
        if rows[0]["disposition"] not in {"copied", "checkpointed"}:
            fail(f"{path.name}: {context}.{rows_name} omits retained database")
    expected = digest("srvls-state-backup-manifest-v1", without(value, "manifest_hash"))
    if value["manifest_hash"] != expected:
        fail(f"{path.name}: {context} hash mismatch")


def validate_installed_release(value: dict[str, Any], path: Path, context: str) -> None:
    if list(value) != INSTALLED_RELEASE_KEYS or value["kind"] != "installed":
        fail(f"{path.name}: {context} installed-bundle key order mismatch")
    validate_binary_artifact(value["binary"], f"{path.name}: {context}.binary", "present")
    validate_state_backup(value["state_backup"], path, f"{context}.state_backup")
    contracts = value["consumer_contracts"]
    pair_ids = [row["pair_id"] for row in contracts]
    if not contracts or pair_ids != sorted(pair_ids) or len(pair_ids) != len(set(pair_ids)):
        fail(f"{path.name}: {context} consumer contracts are not sorted and unique")
    for index, contract in enumerate(contracts):
        validate_consumer_contract(contract, f"{context}.consumer_contracts[{index}]")
    require_sha256(value["release_tarball_sha256"], f"{context}.release_tarball_sha256")
    require_sha256(
        value["stable_toolchain_evidence_sha256"],
        f"{context}.stable_toolchain_evidence_sha256",
    )
    require_unsigned(value["install_generation"], f"{path.name}: {context}.generation")
    if value["install_generation"] == 0:
        fail(f"{path.name}: {context} uses reserved FirstInstall generation zero")
    expected = digest("srvls-installed-prior-release-v1", without(value, "bundle_hash"))
    if value["bundle_hash"] != expected:
        fail(f"{path.name}: {context} bundle hash mismatch")


def validate_known_good_candidate_value(
    value: dict[str, Any],
    path: Path,
    context: str,
    expected_prior_release: dict[str, Any] | None = None,
) -> None:
    if list(value) != KNOWN_GOOD_CANDIDATE_KEYS:
        fail(f"{path.name}: {context} key order mismatch")
    if value["schema_version"] != "srvls-known-good-candidate-v1":
        fail(f"{path.name}: {context} schema mismatch")
    if expected_prior_release is not None and value["prior_release"] != expected_prior_release:
        fail(f"{path.name}: {context} prior release differs from transaction")
    expected = digest(
        "srvls-known-good-candidate-v1", without(value, "candidate_checksum")
    )
    if value["candidate_checksum"] != expected:
        fail(f"{path.name}: {context} checksum mismatch")


def validate_commit_decision(value: dict[str, Any], path: Path, context: str) -> None:
    if value == {"kind": "undecided"}:
        return
    if list(value) != COMMIT_DECISION_KEYS or value.get("kind") != "decided":
        fail(f"{path.name}: {context} tagged union/key order mismatch")
    require_sha256(value["candidate_checksum"], f"{path.name}: {context}.candidate")
    require_unsigned(value["target_install_generation"], f"{path.name}: {context}.generation")
    require_sha256(
        value["expected_known_good_checksum"], f"{path.name}: {context}.KnownGood"
    )


def validate_first_install(
    value: dict[str, Any],
    path: Path,
    *,
    expected_transaction_id: str | None = None,
    expected_canonical_link_path: str | None = None,
    expected_versioned_binary_path: str | None = None,
) -> None:
    if list(value) != FIRST_INSTALL_KEYS or value["kind"] != "first-install-absent":
        fail(f"{path.name}: FirstInstall key order/kind mismatch")
    decoded_linux_path(value["canonical_link_path"], f"{path.name}: FirstInstall link")
    decoded_linux_path(
        value["versioned_binary_path"], f"{path.name}: FirstInstall versioned binary"
    )
    if (
        expected_canonical_link_path is not None
        and value["canonical_link_path"] != expected_canonical_link_path
    ):
        fail(f"{path.name}: FirstInstall canonical link differs from transaction")
    if (
        expected_versioned_binary_path is not None
        and value["versioned_binary_path"] != expected_versioned_binary_path
    ):
        fail(f"{path.name}: FirstInstall versioned binary differs from transaction")
    require_unsigned(value["prior_install_generation"], f"{path.name}: FirstInstall generation")
    if value["prior_install_generation"] != 0:
        fail(f"{path.name}: FirstInstall generation is not reserved zero")
    state = value["state_disposition"]
    if state == {"kind": "absent"}:
        pass
    elif list(state) == ["kind", "plan", "schema"] and state["kind"] == "restore-planned":
        plan = state["plan"]
        if list(plan) != STATE_BACKUP_PLAN_KEYS:
            fail(f"{path.name}: FirstInstall backup plan key order mismatch")
        if plan["schema_version"] != "srvls-state-backup-plan-v1":
            fail(f"{path.name}: FirstInstall backup plan schema mismatch")
        require_uuid(plan["transaction_id"], f"{path.name}: FirstInstall plan transaction")
        require_unsigned(plan["source_schema"], f"{path.name}: FirstInstall plan source schema")
        require_unsigned(plan["target_schema"], f"{path.name}: FirstInstall plan target schema")
        require_unsigned(state["schema"], f"{path.name}: FirstInstall plan schema")
        if (
            state["schema"] != plan["source_schema"]
            or (
                expected_transaction_id is not None
                and plan["transaction_id"] != expected_transaction_id
            )
        ):
            fail(f"{path.name}: FirstInstall backup plan authority mismatch")
        backup_path = decoded_linux_path(plan["backup_database_path"], "backup plan path")
        plan_match = re.fullmatch(
            rb"/home/test/\.local/state/srvls/upgrade/backups/"
            rb"(?P<transaction>[0-9a-f-]{36})/state\.sqlite3",
            backup_path,
        )
        if plan_match is None:
            fail(f"{path.name}: FirstInstall plan path escapes the backup layout")
        plan_transaction = plan_match.group("transaction").decode("ascii")
        require_uuid(plan_transaction, f"{path.name}: FirstInstall plan path transaction")
        if (
            expected_transaction_id is not None
            and plan_transaction != expected_transaction_id
        ):
            fail(f"{path.name}: FirstInstall plan path names another transaction")
    elif (
        list(state) == ["kind", "backup_manifest", "schema"]
        and state["kind"] == "restore-recorded"
    ):
        validate_state_backup(state["backup_manifest"], path, "FirstInstall backup")
        require_unsigned(state["schema"], f"{path.name}: FirstInstall recorded schema")
        if (
            state["schema"] != state["backup_manifest"]["source_schema"]
            or (
                expected_transaction_id is not None
                and expected_transaction_id.encode("ascii")
                not in decoded_linux_path(
                    state["backup_manifest"]["backup_database_path"],
                    f"{path.name}: FirstInstall recorded backup path",
                )
            )
        ):
            fail(f"{path.name}: FirstInstall recorded schema mismatch")
    else:
        fail(f"{path.name}: malformed FirstInstall state disposition")
    consumer = value["consumer_disposition"]
    if list(consumer) != ["kind", "units"] or consumer["kind"] != "absent":
        fail(f"{path.name}: prior consumer absence is not an exact tagged branch")
    units = consumer["units"]
    if not units:
        fail(f"{path.name}: empty FirstInstall consumer absence records")
    unit_order = [
        (row["pair_id"].encode("ascii"), 0 if row["unit_kind"] == "service" else 1)
        for row in units
    ]
    if unit_order != sorted(unit_order) or len(unit_order) != len(set(unit_order)):
        fail(f"{path.name}: absent consumer units are not pair/kind sorted and unique")
    pair_kinds: dict[str, list[str]] = {}
    for unit in units:
        pair_kinds.setdefault(unit["pair_id"], []).append(unit["unit_kind"])
    if any(kinds != ["service", "timer"] for kinds in pair_kinds.values()):
        fail(f"{path.name}: each FirstInstall pair must contain service then timer")
    all_paths: set[bytes] = set()
    required_parents: set[bytes] = set()
    recorded_parents: set[bytes] = set()
    for index, unit in enumerate(units):
        context = f"{path.name}: absent unit {index}"
        if list(unit) != ABSENT_UNIT_KEYS:
            fail(f"{context}: key order mismatch")
        if unit["schema_version"] != "srvls-absent-managed-consumer-unit-v1":
            fail(f"{context}: schema mismatch")
        if re.fullmatch(r"[a-z0-9][a-z0-9-]*", unit["pair_id"]) is None:
            fail(f"{context}: pair ID is not stable ASCII")
        require_nfc_text(unit["unit_name"], f"{context}.unit_name")
        if not unit["unit_name"].endswith(f".{unit['unit_kind']}"):
            fail(f"{context}: unit name suffix differs from unit kind")
        validate_regular_removal(unit["fragment"], f"{context}.fragment")
        require_sorted_paths(unit["drop_ins"], f"{context}.drop_ins")
        require_sorted_paths(unit["enablement_links"], f"{context}.enablement_links")
        require_sorted_paths(
            unit["drop_in_directories"], f"{context}.drop_in_directories"
        )
        for row_index, row in enumerate(unit["drop_ins"]):
            validate_regular_removal(row, f"{context}.drop_ins[{row_index}]")
        for row_index, row in enumerate(unit["enablement_links"]):
            validate_symlink_removal(row, f"{context}.enablement_links[{row_index}]")
        for row_index, row in enumerate(unit["drop_in_directories"]):
            validate_directory_removal(
                row, f"{context}.drop_in_directories[{row_index}]"
            )
        required_parents.update(
            direct_parent(row["path"], f"{context}.managed child")
            for row in [*unit["drop_ins"], *unit["enablement_links"]]
        )
        recorded_parents.update(
            decoded_linux_path(row["path"], f"{context}.recorded parent")
            for row in unit["drop_in_directories"]
        )
        owned = [
            unit["fragment"],
            *unit["drop_ins"],
            *unit["enablement_links"],
            *unit["drop_in_directories"],
        ]
        for row in owned:
            decoded = decoded_linux_path(row["path"], f"{context}.owned path")
            if decoded in all_paths:
                fail(f"{context}: duplicate owned removal path")
            all_paths.add(decoded)
    if recorded_parents != required_parents:
        fail(f"{path.name}: complete transaction-created parent set differs")


def validate_absence_matches_target(
    first_install: dict[str, Any],
    target_contracts: dict[str, dict[str, Any]],
    path: Path,
) -> None:
    expected_units: dict[str, dict[str, Any]] = {}
    for contract in target_contracts.values():
        for unit_kind in ("service", "timer"):
            unit = contract[unit_kind]
            fragment = unit["fragment"]
            expected_units[unit["unit_name"]] = {
                "pair_id": contract["pair_id"],
                "unit_kind": unit_kind,
                "fragment": {
                    "path": fragment["fragment_path"],
                    "expected_sha256": fragment["fragment_sha256"],
                },
                "drop_ins": [
                    {"path": row["path"], "expected_sha256": row["sha256"]}
                    for row in fragment["drop_ins"]
                ],
            }
    actual_units = {
        row["unit_name"]: row
        for row in first_install["consumer_disposition"]["units"]
    }
    if set(actual_units) != set(expected_units):
        fail(f"{path.name}: first-install removal units differ from target contracts")
    for unit_name, expected in expected_units.items():
        actual = actual_units[unit_name]
        if (
            actual["pair_id"] != expected["pair_id"]
            or actual["unit_kind"] != expected["unit_kind"]
            or actual["fragment"] != expected["fragment"]
            or actual["drop_ins"] != expected["drop_ins"]
        ):
            fail(
                f"{path.name}: first-install removal identities do not bind "
                f"target content for {unit_name}"
            )


def validate_nested_hashes(root: dict[str, Any], path: Path) -> None:
    payload = root["payload"]
    validate_release_paths_and_artifacts(payload, path)
    artifacts = payload["artifacts"]
    backup_union = payload["state_backup"]
    backup_hash: str | None = None
    if backup_union["kind"] == "present":
        backup = backup_union["value"]
        validate_state_backup(
            backup,
            path,
            "transaction state backup",
            expected_database_path=payload["paths"]["database_path"],
            expected_transaction_id=payload["transaction_id"],
            expected_source_schema=artifacts["prior_database_schema"],
            expected_target_schema=artifacts["target_database_schema"],
        )
        backup_hash = backup["manifest_hash"]
    elif backup_union != {"kind": "absent"}:
        fail(f"{path.name}: transaction state-backup tagged union mismatch")

    consumer_contracts = [
        value
        for value in walk(root)
        if value.get("schema_version") == "srvls-managed-consumer-unit-contract-v1"
    ]
    if not consumer_contracts:
        fail(f"{path.name}: transaction has no managed consumer contract")
    for index, contract in enumerate(consumer_contracts):
        validate_consumer_contract(contract, f"{path.name}: consumer contract {index}")

    target_rows = payload["consumers"]
    target_pair_ids = [row["pair_id"] for row in target_rows]
    if (
        not target_rows
        or target_pair_ids != sorted(target_pair_ids, key=lambda value: value.encode("ascii"))
        or len(target_pair_ids) != len(set(target_pair_ids))
    ):
        fail(f"{path.name}: target consumer contracts are not pair-ID sorted and unique")
    target_contracts = {row["pair_id"]: row for row in target_rows}
    validate_consumer_negative_oracles(target_rows[0])
    for step in payload["step_records"]:
        for field in ("pre_effect_evidence", "post_effect_evidence"):
            atoms = step[field]
            for kind in ("consumer", "timer"):
                pair_ids = [atom["pair_id"] for atom in atoms if atom.get("kind") == kind]
                if pair_ids and pair_ids != target_pair_ids:
                    fail(
                        f"{path.name}: {step['step']} {field} {kind} pair set "
                        "differs from transaction consumers"
                    )
    prior = payload["prior_release"]
    if list(prior) != ["kind", "value"]:
        fail(f"{path.name}: prior-release tagged union key order mismatch")
    if prior["kind"] == "first-install-absent":
        if payload["intent"] != "install":
            fail(f"{path.name}: FirstInstall authority used outside install")
        validate_first_install(
            prior["value"],
            path,
            expected_transaction_id=payload["transaction_id"],
            expected_canonical_link_path=payload["paths"]["canonical_link_path"],
            expected_versioned_binary_path=payload["paths"][
                "candidate_versioned_binary_path"
            ],
        )
        validate_absence_matches_target(prior["value"], target_contracts, path)
        if (
            payload["old_install_generation"] != 0
            or artifacts["prior_binary"] != {
                "kind": "absent",
                "path": {"kind": "absent"},
                "sha256": {"kind": "absent"},
                "size_bytes": {"kind": "absent"},
            }
            or payload["paths"]["prior_versioned_binary_path"] != {"kind": "absent"}
        ):
            fail(f"{path.name}: FirstInstall prior path/artifact/generation mismatch")
        state = prior["value"]["state_disposition"]
        prior_schema = (
            state["schema"] if state.get("kind") in {"restore-planned", "restore-recorded"}
            else artifacts["prior_database_schema"]
        )
        if artifacts["prior_database_schema"] != prior_schema:
            fail(f"{path.name}: FirstInstall prior database schema mismatch")
        if state["kind"] == "restore-planned" and (
            state["plan"]["source_schema"] != artifacts["prior_database_schema"]
            or state["plan"]["target_schema"] != artifacts["target_database_schema"]
        ):
            fail(f"{path.name}: FirstInstall plan schema direction mismatch")
        if state["kind"] == "restore-recorded":
            if backup_hash is None or state["backup_manifest"] != backup_union["value"]:
                fail(f"{path.name}: first-install backup authority mismatch")
    elif prior["kind"] == "installed":
        if payload["intent"] not in {"upgrade", "rollback"}:
            fail(f"{path.name}: installed prior used outside upgrade/rollback")
        validate_installed_release(prior["value"], path, "prior_release")
        prior_value = prior["value"]
        if (
            prior_value["install_generation"] != payload["old_install_generation"]
            or prior_value["binary"] != artifacts["prior_binary"]
            or payload["paths"]["prior_versioned_binary_path"]
            != prior_value["binary"]["path"]
            or artifacts["prior_database_schema"]
            != prior_value["state_backup"]["target_schema"]
        ):
            fail(f"{path.name}: installed prior path/artifact/schema/generation mismatch")
    else:
        fail(f"{path.name}: unknown prior-release kind")

    if payload["intent"] != "rollback":
        prior_contracts = (
            {
                row["pair_id"]: row
                for row in prior["value"]["consumer_contracts"]
            }
            if prior["kind"] == "installed"
            else {}
        )
        for step in payload["step_records"]:
            for field in ("pre_effect_evidence", "post_effect_evidence"):
                for atom in step[field]:
                    if atom.get("kind") != "consumer":
                        continue
                    pair_id = atom["pair_id"]
                    if (
                        step["step"] == "rewrite-consumers"
                        and field == "pre_effect_evidence"
                        and prior["kind"] == "installed"
                    ):
                        expected_contract = prior_contracts.get(pair_id)
                    elif step["step"] == "restore-consumers":
                        expected_contract = (
                            target_contracts.get(pair_id)
                            if field == "pre_effect_evidence"
                            else prior_contracts.get(pair_id)
                        )
                    elif step["step"] in {
                        "rollback-daemon-reload",
                        "validate-restored-pair",
                    }:
                        expected_contract = prior_contracts.get(pair_id)
                    else:
                        expected_contract = target_contracts.get(pair_id)
                    if (
                        expected_contract is None
                        or atom["contract_hash"]
                        != expected_contract["contract_hash"]
                    ):
                        fail(
                            f"{path.name}: {step['step']} {field} consumer hash "
                            "does not bind the directional contract"
                        )

    rollback_target = payload["rollback_target"]
    if payload["intent"] == "rollback":
        if rollback_target.get("kind") != "present":
            fail(f"{path.name}: rollback has no retained target bundle")
        target = rollback_target["value"]
        validate_installed_release(target, path, "rollback_target")
        if (
            target["install_generation"] != payload["target_install_generation"]
            or target["consumer_contracts"] != payload["consumers"]
            or target["binary"] != payload["artifacts"]["candidate_binary"]
            or target["release_tarball_sha256"]
            != payload["artifacts"]["release_tarball_sha256"]
            or target["stable_toolchain_evidence_sha256"]
            != payload["artifacts"]["stable_toolchain_evidence_sha256"]
        ):
            fail(f"{path.name}: rollback target bytes drift from staged target")
    elif rollback_target != {"kind": "absent"}:
        fail(f"{path.name}: non-rollback transaction carries rollback target")

    candidate_union = payload["known_good_candidate"]
    if candidate_union["kind"] == "present":
        candidate = candidate_union["value"]
        validate_known_good_candidate_value(
            candidate,
            path,
            "KnownGoodCandidateV1",
            payload["prior_release"],
        )
        known_payload = {
            "source_transaction_id": payload["transaction_id"],
            "published_install_generation": payload["target_install_generation"],
            "candidate": candidate,
        }
        known_hash = digest("srvls-known-good-release-v1", known_payload)
        decision = payload["commit_decision"]
        validate_commit_decision(decision, path, "CommitDecisionV1")
        expected_decision_evidence = {
            "kind": "decision",
            "candidate_checksum": candidate["candidate_checksum"],
            "target_install_generation": payload["target_install_generation"],
            "expected_known_good_checksum": known_hash,
        }
        if decision["kind"] == "decided" and (
            decision["candidate_checksum"] != candidate["candidate_checksum"]
            or decision["expected_known_good_checksum"] != known_hash
            or decision["target_install_generation"]
            != payload["target_install_generation"]
        ):
            fail(f"{path.name}: commit decision checksum mismatch")
        for atom in walk(payload["step_records"]):
            if atom.get("kind") == "decision" and atom != expected_decision_evidence:
                fail(f"{path.name}: decision evidence checksum mismatch")
            if atom.get("kind") == "known-good" and atom["checksum"] != known_hash:
                fail(f"{path.name}: KnownGood evidence checksum mismatch")
    else:
        if candidate_union != {"kind": "absent"}:
            fail(f"{path.name}: KnownGood candidate tagged union mismatch")
        validate_commit_decision(payload["commit_decision"], path, "CommitDecisionV1")
        if payload["commit_decision"]["kind"] == "decided":
            fail(f"{path.name}: decided commit has no KnownGood candidate")


def _require_prefix(actual: list[str], expected: list[str], context: str) -> None:
    if actual != expected[: len(actual)]:
        fail(f"{context}: step order differs from the closed state machine")


def validate_step_machine(payload: dict[str, Any], path: Path) -> None:
    steps = payload["step_records"]
    tokens = [step["step"] for step in steps]
    failed = [index for index, step in enumerate(steps) if step["state"] == "failed"]
    if len(failed) > 1:
        fail(f"{path.name}: state machine has multiple failed effects")

    if payload["intent"] == "rollback":
        _require_prefix(tokens, EXPLICIT_ROLLBACK_SEQUENCE, path.name)
        if any(step["direction"] != "explicit-rollback" for step in steps):
            fail(f"{path.name}: explicit rollback carries another direction")
        if failed or any(step["state"] == "skipped" for step in steps):
            fail(f"{path.name}: explicit rollback uses an unsupported failure/skip path")
    elif failed:
        failed_index = failed[0]
        if (
            failed_index >= len(FORWARD_SEQUENCE)
            or tokens[: failed_index + 1] != FORWARD_SEQUENCE[: failed_index + 1]
        ):
            fail(f"{path.name}: failed effect is outside the ordered forward path")
        recovery = (
            FIRST_INSTALL_RECOVERY_SEQUENCE
            if payload["prior_release"]["kind"] == "first-install-absent"
            else INSTALLED_RECOVERY_SEQUENCE
        )
        _require_prefix(tokens[failed_index + 1 :], recovery, path.name)
        if any(step["direction"] != "recovery" for step in steps[failed_index + 1 :]):
            fail(f"{path.name}: post-failure restore path is not recovery-directed")
        if payload["prior_release"]["kind"] == "first-install-absent":
            for offset, token in enumerate(FIRST_INSTALL_RECOVERY_SEQUENCE[:4]):
                index = failed_index + 1 + offset
                if index >= len(steps):
                    break
                step = steps[index]
                if step["step"] != token or step["state"] != "skipped":
                    fail(f"{path.name}: FirstInstall no-prior effect is not durably skipped")
        elif any(step["state"] == "skipped" for step in steps[failed_index + 1 :]):
            fail(f"{path.name}: installed-prior recovery contains a skipped effect")
    else:
        _require_prefix(tokens, FORWARD_SEQUENCE, path.name)
        if any(step["state"] in {"failed", "skipped"} for step in steps):
            fail(f"{path.name}: successful forward path contains failure/skip")
        directions = [step["direction"] for step in steps]
        if any(direction not in {"forward", "recovery"} for direction in directions):
            fail(f"{path.name}: forward path carries explicit-rollback direction")
        if "recovery" in directions:
            first_recovery = directions.index("recovery")
            if (
                len(payload["recovery_attempts"]) < 2
                or directions[:first_recovery] != ["forward"] * first_recovery
                or directions[first_recovery:] != ["recovery"] * (
                    len(directions) - first_recovery
                )
            ):
                fail(f"{path.name}: owner-takeover direction is not one-way")

    for index, step in enumerate(steps):
        if step["state"] == "pending" and index != len(steps) - 1:
            fail(f"{path.name}: non-final step remains pending")
        if step["state"] not in {"complete", "pending", "failed", "skipped"}:
            fail(f"{path.name}: unknown state-machine step state")

    terminal = payload["terminal_result"]["kind"]
    if terminal == "committed" and (
        tokens != FORWARD_SEQUENCE or not steps or steps[-1]["state"] != "complete"
    ):
        fail(f"{path.name}: committed terminal does not complete the forward machine")
    if terminal == "forward-failed-recovered":
        failed_index = failed[0] if failed else -1
        recovery = (
            FIRST_INSTALL_RECOVERY_SEQUENCE
            if payload["prior_release"]["kind"] == "first-install-absent"
            else INSTALLED_RECOVERY_SEQUENCE
        )
        if (
            failed_index < 0
            or tokens[failed_index + 1 :] != recovery
            or steps[-1]["state"] != "complete"
        ):
            fail(f"{path.name}: recovered terminal does not complete the restore machine")
    if terminal == "rolled-back" and (
        tokens != EXPLICIT_ROLLBACK_SEQUENCE
        or not steps
        or steps[-1]["state"] != "complete"
    ):
        fail(f"{path.name}: rolled-back terminal does not complete explicit rollback")


def evidence_kinds(step: dict[str, Any], field: str = "post_effect_evidence") -> set[str]:
    return {atom["kind"] for atom in step[field]}


def validate_step_semantics(
    payload: dict[str, Any], path: Path
) -> None:
    validate_step_machine(payload, path)
    steps = payload["step_records"]
    events = payload["release_events"]
    attempts = {
        row["attempt_id"]: row for row in payload["recovery_attempts"]
    }
    attempt_sequences = {
        attempt_id: row["sequence"] for attempt_id, row in attempts.items()
    }
    event_index = 0
    for step_index, step in enumerate(steps):
        if list(step) != STEP_KEYS or step["schema_version"] != "srvls-release-step-record-v1":
            fail(f"{path.name}: step {step_index} schema/key order mismatch")
        token = step["step"]
        required = REQUIRED_POST_EVIDENCE.get(token)
        if required is None:
            fail(f"{path.name}: unknown release step {token!r}")
        if step["sequence"] != step_index:
            fail(f"{path.name}: step sequence is not gap-free")
        if step["direction"] not in {"forward", "recovery", "explicit-rollback"}:
            fail(f"{path.name}: unknown release direction")
        if step["state"] not in {"pending", "complete", "failed", "skipped"}:
            fail(f"{path.name}: unknown release step state")
        require_unsigned(step["effect_attempt"], f"{path.name}: {token}.effect_attempt")
        require_uuid(step["idempotency_key"], f"{path.name}: {token}.idempotency_key")
        require_uuid(step["recovery_attempt_id"], f"{path.name}: {token}.recovery_attempt_id")
        owner = attempts.get(step["recovery_attempt_id"])
        if owner is None:
            fail(f"{path.name}: {token} names an unknown recovery owner")
        if step["reason_code"] not in RELEASE_REASONS:
            fail(f"{path.name}: {token} carries an unknown reason")
        validation = step["validation_attempt"]
        if validation == {"kind": "absent"}:
            if (
                step["state"] != "skipped"
                and token
                in {"prove-timer-invocation", "validate-candidate", "validate-restored-pair"}
            ):
                fail(f"{path.name}: {token} lacks its persisted validation attempt")
        elif list(validation) == ["kind", "value"] and validation.get("kind") == "present":
            if token not in {"prove-timer-invocation", "validate-candidate", "validate-restored-pair"}:
                fail(f"{path.name}: {token} carries an inapplicable validation attempt")
            validate_validation_attempt(
                validation["value"],
                f"{path.name}: {token}.validation_attempt",
                attempt_sequences,
                step,
            )
            if validation["value"]["start_boot_ns"] <= owner["acquisition_boot_ns"]:
                fail(f"{path.name}: {token} validation begins before owner publication")
        else:
            fail(f"{path.name}: {token} validation-attempt tagged union mismatch")
        validate_evidence_array(
            step["pre_effect_evidence"], payload, f"{path.name}: {token}.pre"
        )
        validate_evidence_array(
            step["post_effect_evidence"], payload, f"{path.name}: {token}.post"
        )
        if token in {"stage-binary", "verify-checksum", "activate-binary"}:
            expected_path_count = 1
        elif token == "restore-binary":
            expected_path_count = (
                2
                if payload["prior_release"]["kind"] == "first-install-absent"
                else 1
            )
        elif token == "remove-first-install-consumers":
            expected_path_count = len(
                expected_owned_atoms(payload["prior_release"]["value"])
            )
        else:
            expected_path_count = None
        if expected_path_count is not None and step["state"] != "skipped":
            pre_paths = sum(
                atom["kind"] == "path" for atom in step["pre_effect_evidence"]
            )
            post_paths = sum(
                atom["kind"] == "path" for atom in step["post_effect_evidence"]
            )
            required_post_paths = (
                expected_path_count if step["state"] == "complete" else 0
            )
            if pre_paths != expected_path_count or post_paths != required_post_paths:
                fail(f"{path.name}: {token} path-evidence cardinality mismatch")
        if step["state"] == "skipped":
            if step["pre_effect_evidence"] or step["post_effect_evidence"]:
                fail(f"{path.name}: skipped {token} carries effect evidence")
        else:
            expected_evidence = STEP_EVIDENCE.get((token, step["direction"]))
            if expected_evidence is None:
                fail(f"{path.name}: {token} is illegal for direction {step['direction']}")
            expected_pre, expected_post = expected_evidence
            if evidence_kinds(step, "pre_effect_evidence") != expected_pre:
                fail(f"{path.name}: {token} pre-evidence relation mismatch")
            required_post = expected_post if step["state"] == "complete" else set()
            if evidence_kinds(step) != required_post:
                fail(f"{path.name}: {token} post-evidence relation mismatch")
        timer_atoms = [
            atom
            for atom in [*step["pre_effect_evidence"], *step["post_effect_evidence"]]
            if atom["kind"] == "timer"
        ]
        if timer_atoms and validation.get("kind") != "present":
            fail(f"{path.name}: {token} timer evidence has no persisted attempt")
        for atom in timer_atoms:
            if atom["acceptance"]["validation_attempt"] != validation["value"]:
                fail(f"{path.name}: {token} timer evidence uses another validation attempt")
        if step["state"] == "pending" and step["post_effect_evidence"]:
            fail(f"{path.name}: pending {token} has post-effect evidence")
        if step["state"] in {"pending", "complete"} and step["reason_code"] != "none":
            fail(f"{path.name}: successful/pending {token} carries a failure reason")
        if step["state"] == "failed" and step["reason_code"] in {
            "none",
            "no-prior-release",
            "resumed-after-owner-loss",
        }:
            fail(f"{path.name}: failed {token} lacks a stable failure reason")
        if step["state"] == "skipped" and step["reason_code"] != "no-prior-release":
            fail(f"{path.name}: skipped {token} lacks no-prior-release reason")
        admission_atoms = [
            atom
            for atom in [*step["pre_effect_evidence"], *step["post_effect_evidence"]]
            if atom["kind"] == "admission"
        ]
        if token == "persist-recovering-admission" and any(
            atom["status"] != "recovering"
            or atom["install_generation"] != payload["old_install_generation"]
            or atom["transaction_id"]
            != {"kind": "present", "value": payload["transaction_id"]}
            for atom in admission_atoms
        ):
            fail(f"{path.name}: recovering admission evidence direction mismatch")
        if token in {"persist-ready-admission", "rollback-ready-admission"}:
            ready_generation = (
                payload["target_install_generation"]
                if token == "persist-ready-admission" or payload["intent"] == "rollback"
                else payload["old_install_generation"]
            )
            for atom in step["pre_effect_evidence"]:
                if atom["kind"] == "admission" and (
                    atom["status"] != "recovering"
                    or atom["install_generation"] != payload["old_install_generation"]
                ):
                    fail(f"{path.name}: ready-admission precondition direction mismatch")
            for atom in step["post_effect_evidence"]:
                if atom["kind"] == "admission" and (
                    atom["status"] != "ready"
                    or atom["install_generation"] != ready_generation
                ):
                    fail(f"{path.name}: ready-admission postcondition direction mismatch")
        for atom in [*step["pre_effect_evidence"], *step["post_effect_evidence"]]:
            if atom["kind"] == "transaction" and atom["result"] != payload["terminal_result"]:
                fail(f"{path.name}: transaction evidence differs from terminal truth")
        if step["state"] == "skipped":
            expected_statuses = ["skipped"]
        elif step["state"] == "pending":
            expected_statuses = [{"started", "resumed"}]
        else:
            expected_statuses = [
                {"started", "resumed"},
                "succeeded" if step["state"] == "complete" else "failed",
            ]
        for offset, expected_status in enumerate(expected_statuses):
            if event_index >= len(events):
                fail(f"{path.name}: {token} lacks its durable event transition")
            event = events[event_index]
            if list(event) != EVENT_KEYS or event["schema_version"] != "srvls-release-event-v1":
                fail(f"{path.name}: event {event_index} schema/key order mismatch")
            require_unsigned(event["sequence"], f"{path.name}: event.sequence")
            require_unsigned(event["recovery_attempt_sequence"], f"{path.name}: event.owner_sequence")
            require_unsigned(event["manifest_revision"], f"{path.name}: event.revision")
            if (
                event["transaction_id"] != payload["transaction_id"]
                or event["sequence"] != event_index
                or event["recovery_attempt_sequence"]
                != attempt_sequences.get(event["recovery_attempt_id"])
                or event["manifest_revision"] != event_index + 1
                or event["public_phase"] != STEP_PHASES[token]
                or event["reason_code"] not in RELEASE_REASONS
            ):
                fail(f"{path.name}: event {event_index} scalar/cross-record mismatch")
            if (
                event["manifest_step"] != token
                or event["recovery_attempt_id"] != step["recovery_attempt_id"]
            ):
                fail(f"{path.name}: event/step owner or token mismatch")
            allowed = expected_status if isinstance(expected_status, set) else {expected_status}
            if event["status"] not in allowed:
                fail(f"{path.name}: {token} event state transition mismatch")
            if event["status"] == "resumed":
                if offset != 0 or step["direction"] != "recovery":
                    fail(f"{path.name}: resumed event is not a recovery start")
                if event["reason_code"] != "resumed-after-owner-loss":
                    fail(f"{path.name}: resumed event lacks stable reason")
            elif event["status"] == "failed":
                if event["reason_code"] != step["reason_code"]:
                    fail(f"{path.name}: failed event reason differs from step")
            elif event["status"] == "skipped":
                if event["reason_code"] != "no-prior-release":
                    fail(f"{path.name}: skipped event lacks stable reason")
            elif event["reason_code"] != "none":
                fail(f"{path.name}: successful/start event carries failure reason")
            event_index += 1
    if event_index != len(events):
        fail(f"{path.name}: release event history has unbound extra rows")


def observed_boot_times(value: Any) -> list[int]:
    """Return actual observations, excluding future deadline/timeout cuts."""
    keys = {
        "start_boot_ns",
        "ack_boot_ns",
        "drain_barrier_boot_ns",
        "captured_boot_ns",
        "observation_boot_ns",
        "observed_boot_ns",
    }
    result: list[int] = []
    if isinstance(value, dict):
        for key, child in value.items():
            if key in keys and type(child) is int:
                result.append(child)
            result.extend(observed_boot_times(child))
    elif isinstance(value, list):
        for child in value:
            result.extend(observed_boot_times(child))
    return result


def validate_payload_semantics(payload: dict[str, Any], path: Path) -> None:
    require_uuid(payload["transaction_id"], f"{path.name}: transaction_id")
    require_unsigned(payload["manifest_revision"], f"{path.name}: manifest_revision")
    if payload["intent"] not in {"install", "upgrade", "rollback"}:
        fail(f"{path.name}: unknown transaction intent")
    validate_owner(payload["original_owner"], f"{path.name}: original_owner")
    require_unsigned(payload["old_install_generation"], f"{path.name}: old generation")
    require_unsigned(payload["target_install_generation"], f"{path.name}: target generation")
    if payload["intent"] in {"install", "upgrade"}:
        if payload["target_install_generation"] != payload["old_install_generation"] + 1:
            fail(f"{path.name}: forward generations are not source plus one")
        if payload["intent"] == "install" and payload["old_install_generation"] != 0:
            fail(f"{path.name}: install does not start at reserved generation zero")
        if payload["intent"] == "upgrade" and payload["old_install_generation"] == 0:
            fail(f"{path.name}: upgrade has no installed source generation")
    elif payload["old_install_generation"] != payload["target_install_generation"] + 1:
        fail(f"{path.name}: rollback generations are not source minus one")
    attempts = payload["recovery_attempts"]
    if not attempts:
        fail(f"{path.name}: recovery owner history is empty")
    acquisition_times: list[int] = []
    for index, attempt in enumerate(attempts):
        context = f"{path.name}: recovery_attempts[{index}]"
        if list(attempt) != ATTEMPT_KEYS:
            fail(f"{context}: key order mismatch")
        if attempt["schema_version"] != "srvls-release-recovery-attempt-v1":
            fail(f"{context}: schema mismatch")
        require_uuid(attempt["attempt_id"], f"{context}.attempt_id")
        require_unsigned(attempt["sequence"], f"{context}.sequence")
        if attempt["sequence"] != index:
            fail(f"{context}: sequence is not gap-free")
        validate_owner(attempt["owner"], f"{context}.owner")
        for key in ("admission_lock_device", "admission_lock_inode", "acquisition_boot_ns"):
            require_unsigned(attempt[key], f"{context}.{key}")
        predecessor = attempt["predecessor_manifest_checksum"]
        if index == 0:
            if predecessor != {"kind": "absent"}:
                fail(f"{context}: first owner has a predecessor")
        elif list(predecessor) != ["kind", "value"] or predecessor.get("kind") != "present":
            fail(f"{context}: replacement owner lacks a predecessor")
        else:
            require_sha256(predecessor["value"], f"{context}.predecessor")
        acquisition_times.append(attempt["acquisition_boot_ns"])
    if acquisition_times != sorted(acquisition_times) or len(set(acquisition_times)) != len(
        acquisition_times
    ):
        fail(f"{path.name}: recovery-owner acquisition times are not strictly increasing")
    if payload["active_recovery_attempt_id"] != attempts[-1]["attempt_id"]:
        fail(f"{path.name}: active recovery owner is not the final row")
    steps = payload["step_records"]
    for index, attempt in enumerate(attempts[1:], 1):
        first_owned = next(
            (
                step_index
                for step_index, step in enumerate(steps)
                if step["recovery_attempt_id"] == attempt["attempt_id"]
            ),
            None,
        )
        if first_owned is None:
            fail(f"{path.name}: published recovery owner has no step")
        prior_observations = observed_boot_times(steps[:first_owned])
        if prior_observations and attempt["acquisition_boot_ns"] <= max(prior_observations):
            fail(f"{path.name}: replacement owner predates persisted prior observations")
    validate_terminal_result(payload["terminal_result"], payload, f"{path.name}: terminal")
    validate_step_semantics(payload, path)


def expected_owned_atoms(first: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for unit in first["consumer_disposition"]["units"]:
        regular = [unit["fragment"], *unit["drop_ins"]]
        for row in regular:
            rows.append(
                {
                    "kind": "path",
                    "path": row["path"],
                    "state": "regular",
                    "sha256": {"kind": "present", "value": row["expected_sha256"]},
                    "symlink_target": {"kind": "absent"},
                }
            )
        for row in unit["enablement_links"]:
            rows.append(
                {
                    "kind": "path",
                    "path": row["path"],
                    "state": "symlink",
                    "sha256": {"kind": "absent"},
                    "symlink_target": {
                        "kind": "present",
                        "value": row["expected_target"],
                    },
                }
            )
        for row in unit["drop_in_directories"]:
            rows.append(
                {
                    "kind": "path",
                    "path": row["path"],
                    "state": "directory",
                    "sha256": {"kind": "absent"},
                    "symlink_target": {"kind": "absent"},
                }
            )
    return sorted(rows, key=lambda row: decoded_raw(row["path"], "owned evidence"))


def validate_first_install_cut(payload: dict[str, Any], path: Path) -> None:
    steps = {row["step"]: row for row in payload["step_records"]}
    restore_binary = steps["restore-binary"]
    post_paths = restore_binary["post_effect_evidence"]
    expected_paths = {
        payload["prior_release"]["value"]["canonical_link_path"],
        payload["prior_release"]["value"]["versioned_binary_path"],
    }
    if {row["path"] for row in post_paths} != expected_paths or any(
        row["kind"] != "path"
        or row["state"] != "absent"
        or row["sha256"] != {"kind": "absent"}
        or row["symlink_target"] != {"kind": "absent"}
        for row in post_paths
    ):
        fail(f"{path.name}: completed first-install binary restoration is not absent")
    prior_schema = payload["prior_release"]["value"]["state_disposition"]["schema"]
    restored_state = steps["restore-state"]["post_effect_evidence"]
    if len(restored_state) != 1 or restored_state[0].get("schema") != prior_schema:
        fail(f"{path.name}: completed first-install state restoration has wrong schema")
    removal = steps["remove-first-install-consumers"]
    expected = expected_owned_atoms(payload["prior_release"]["value"])
    if removal["pre_effect_evidence"] != expected:
        fail(f"{path.name}: pending consumer removal identities are not exact")
    parent_states = {
        row["prior_state"]
        for unit in payload["prior_release"]["value"]["consumer_disposition"]["units"]
        for row in unit["drop_in_directories"]
    }
    if parent_states != {"absent", "directory"}:
        fail(f"{path.name}: first-install cut does not exercise both parent states")


def validate_explicit_rollback(
    payload: dict[str, Any], path: Path, *, require_checkpoint: bool = True
) -> None:
    current_binary = "%2Fhome%2Ftest%2F.local%2Flib%2Fsrvls%2F1.0.0%2Fsrvls"
    target_binary = "%2Fhome%2Ftest%2F.local%2Flib%2Fsrvls%2F0.9.0%2Fsrvls"
    source = payload["prior_release"]["value"]
    target = payload["rollback_target"]["value"]
    if (
        payload["old_install_generation"] != 8
        or payload["target_install_generation"] != 7
        or source["install_generation"] != 8
        or target["install_generation"] != 7
        or source["binary"]["path"] != {"kind": "present", "value": current_binary}
        or target["binary"]["path"] != {"kind": "present", "value": target_binary}
        or payload["paths"]["prior_versioned_binary_path"]
        != {"kind": "present", "value": current_binary}
        or payload["paths"]["candidate_versioned_binary_path"] != target_binary
        or payload["artifacts"]["prior_binary"]["path"]
        != {"kind": "present", "value": current_binary}
        or payload["artifacts"]["candidate_binary"]["path"]
        != {"kind": "present", "value": target_binary}
    ):
        fail(f"{path.name}: explicit rollback source/target authority drift")
    target_contracts = {row["pair_id"]: row for row in payload["consumers"]}
    retained_contracts = {
        row["pair_id"]: row for row in target["consumer_contracts"]
    }
    source_contracts = {
        row["pair_id"]: row for row in source["consumer_contracts"]
    }
    if target_contracts != retained_contracts or set(target_contracts) != set(source_contracts):
        fail(f"{path.name}: explicit rollback consumer pair set drift")
    pair_order = [row["pair_id"] for row in payload["consumers"]]
    source_evidence = [
        {
            "kind": "consumer",
            "pair_id": pair_id,
            "contract_hash": source_contracts[pair_id]["contract_hash"],
            "readback": "loaded-match",
        }
        for pair_id in pair_order
    ]
    target_evidence = [
        {
            "kind": "consumer",
            "pair_id": pair_id,
            "contract_hash": target_contracts[pair_id]["contract_hash"],
            "readback": "loaded-match",
        }
        for pair_id in pair_order
    ]
    for pair_id, target_contract in target_contracts.items():
        source_contract = source_contracts[pair_id]
        target_contents = [
            target_contract["service"]["fragment"]["fragment_content"],
            target_contract["timer"]["fragment"]["fragment_content"],
            *[
                row["content"]
                for row in target_contract["service"]["fragment"]["drop_ins"]
            ],
        ]
        source_contents = [
            source_contract["service"]["fragment"]["fragment_content"],
            source_contract["timer"]["fragment"]["fragment_content"],
            *[
                row["content"]
                for row in source_contract["service"]["fragment"]["drop_ins"]
            ],
        ]
        if (
            target_contract["contract_hash"] == source_contract["contract_hash"]
            or target_contents == source_contents
        ):
            fail(
                f"{path.name}: explicit rollback does not exercise byte-distinct "
                f"target/prior consumer content for {pair_id}"
            )
    backup_union = payload["state_backup"]
    if (
        payload["artifacts"]["prior_database_schema"] != 2
        or payload["artifacts"]["target_database_schema"] != 1
    ):
        fail(f"{path.name}: explicit rollback state direction drift")
    if backup_union["kind"] == "present":
        backup = backup_union["value"]
        if backup["source_schema"] != 2 or backup["target_schema"] != 1:
            fail(f"{path.name}: explicit rollback backup direction drift")
    steps = {row["step"]: row for row in payload["step_records"]}
    if require_checkpoint:
        for required_step in {
            "persist-recovering-admission",
            "create-backup",
            "stage-known-good-candidate",
            "commit-decided",
            "publish-known-good",
            "rollback-ready-admission",
        }:
            if required_step not in steps:
                fail(f"{path.name}: explicit rollback omits {required_step}")

    restore = steps.get("restore-consumers")
    if restore is not None:
        if restore["pre_effect_evidence"] != source_evidence:
            fail(f"{path.name}: restore-consumers pre-effect is not generation 8 source")
        expected_post = target_evidence if restore["state"] == "complete" else []
        if restore["post_effect_evidence"] != expected_post:
            fail(f"{path.name}: restore-consumers post-effect is not generation 7 target")

    reload_step = steps.get("rollback-daemon-reload")
    if reload_step is not None:
        if reload_step["pre_effect_evidence"] != target_evidence:
            fail(f"{path.name}: rollback-daemon-reload pre-effect is not restored target")
        expected_post = target_evidence if reload_step["state"] == "complete" else []
        if reload_step["post_effect_evidence"] != expected_post:
            fail(f"{path.name}: rollback-daemon-reload post-effect is not restored target")

    restored = steps.get("validate-restored-pair")
    if restored is not None:
        pre_consumers = [
            atom
            for atom in restored["pre_effect_evidence"]
            if atom.get("kind") == "consumer"
        ]
        if (
            pre_consumers != target_evidence
            or {atom["kind"] for atom in restored["pre_effect_evidence"]}
            != {"consumer", "timer", "fd4"}
        ):
            fail(f"{path.name}: restored-pair pre-effect is not generation 7 target")
        post_consumers = [
            atom
            for atom in restored["post_effect_evidence"]
            if atom.get("kind") == "consumer"
        ]
        if restored["state"] == "complete":
            if (
                post_consumers != target_evidence
                or evidence_kinds(restored) != {"consumer", "timer", "fd4"}
            ):
                fail(f"{path.name}: restored-pair post-effect is not generation 7 target")
        elif restored["post_effect_evidence"]:
            fail(f"{path.name}: incomplete restored-pair carries post-effect evidence")
    elif require_checkpoint:
        fail(f"{path.name}: explicit rollback omits validate-restored-pair")

    admission_step = steps.get("persist-recovering-admission")
    if admission_step is not None and admission_step["state"] == "complete":
        admission = admission_step["post_effect_evidence"]
        if not any(
            row.get("kind") == "admission"
            and row["status"] == "recovering"
            and row["install_generation"] == 8
            for row in admission
        ):
            fail(f"{path.name}: rollback transaction is not anchored to generation 8")


def expect_explicit_rollback_rejected(payload: dict[str, Any], label: str) -> None:
    try:
        validate_explicit_rollback(
            payload, Path(f"negative-explicit-rollback:{label}"), require_checkpoint=True
        )
    except SystemExit:
        return
    fail(f"negative explicit rollback oracle accepted {label}")


def validate_explicit_rollback_negative_oracles(payload: dict[str, Any]) -> None:
    source_hash = payload["prior_release"]["value"]["consumer_contracts"][0][
        "contract_hash"
    ]
    target_hash = payload["rollback_target"]["value"]["consumer_contracts"][0][
        "contract_hash"
    ]

    same = copy.deepcopy(payload)
    same_steps = {row["step"]: row for row in same["step_records"]}
    same_steps["restore-consumers"]["pre_effect_evidence"][0][
        "contract_hash"
    ] = target_hash
    expect_explicit_rollback_rejected(same, "same-target-hash-on-both-sides")

    swapped = copy.deepcopy(payload)
    swapped_steps = {row["step"]: row for row in swapped["step_records"]}
    swapped_steps["restore-consumers"]["pre_effect_evidence"][0][
        "contract_hash"
    ] = target_hash
    swapped_steps["restore-consumers"]["post_effect_evidence"][0][
        "contract_hash"
    ] = source_hash
    expect_explicit_rollback_rejected(swapped, "swapped-source-and-target-hashes")

    wrong = copy.deepcopy(payload)
    wrong_steps = {row["step"]: row for row in wrong["step_records"]}
    wrong_steps["restore-consumers"]["pre_effect_evidence"][0][
        "contract_hash"
    ] = "0" * 64
    expect_explicit_rollback_rejected(wrong, "wrong-source-hash")

    wrong_reload = copy.deepcopy(payload)
    wrong_reload_steps = {row["step"]: row for row in wrong_reload["step_records"]}
    wrong_reload_steps["rollback-daemon-reload"]["pre_effect_evidence"][0][
        "contract_hash"
    ] = source_hash
    expect_explicit_rollback_rejected(wrong_reload, "wrong-reload-hash")

    wrong_validation = copy.deepcopy(payload)
    wrong_validation_steps = {
        row["step"]: row for row in wrong_validation["step_records"]
    }
    validation_consumer = next(
        atom
        for atom in wrong_validation_steps["validate-restored-pair"][
            "pre_effect_evidence"
        ]
        if atom.get("kind") == "consumer"
    )
    validation_consumer["contract_hash"] = source_hash
    expect_explicit_rollback_rejected(wrong_validation, "wrong-validation-hash")


def validate_manifest(path: Path, expected_case: tuple[Any, ...]) -> None:
    root = load_exact(path)
    if list(root) != OUTER_KEYS or root["schema_version"] != "srvls-upgrade-transaction-v1":
        fail(f"{path.name}: outer schema/key order mismatch")
    payload = root["payload"]
    if list(payload) != PAYLOAD_KEYS:
        fail(f"{path.name}: payload key order mismatch")
    if root["checksum"] != digest("srvls-upgrade-transaction-v1", payload):
        fail(f"{path.name}: outer checksum mismatch")
    validate_tagged_presence(root, path)
    validate_path_evidence(root, path)

    attempts = payload["recovery_attempts"]
    if not attempts or [row["sequence"] for row in attempts] != list(range(len(attempts))):
        fail(f"{path.name}: recovery attempt sequence is not nonempty and gap-free")
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
    for index, event in enumerate(events):
        if event["recovery_attempt_id"] not in attempt_sequences:
            fail(f"{path.name}: event names unknown recovery owner")
        if event["recovery_attempt_sequence"] != attempt_sequences[event["recovery_attempt_id"]]:
            fail(f"{path.name}: event owner sequence mismatch")
        if event["manifest_revision"] != index + 1:
            fail(f"{path.name}: event revision is not the exact replacement revision")
    if payload["manifest_revision"] != len(events):
        fail(f"{path.name}: manifest revision does not equal complete event chain")
    validate_payload_semantics(payload, path)

    expected_step, expected_state, prior_kind, attempt_count, candidate_kind = expected_case
    current = payload["current_step"]
    if expected_step is None:
        if (
            current != {"kind": "absent"}
            or steps
            or events
            or payload["manifest_revision"] != 0
            or payload["predecessor_checksum"] != {"kind": "absent"}
            or payload["state_backup"] != {"kind": "absent"}
        ):
            fail(f"{path.name}: initial transaction-created cut is not effect-free")
    else:
        final = steps[-1]
        expected_cursor = {
            "kind": "present",
            "value": {
                "sequence": final["sequence"],
                "step": final["step"],
                "effect_attempt": final["effect_attempt"],
            },
        }
        if current != expected_cursor:
            fail(f"{path.name}: current-step tagged union drift")
        if final["step"] != expected_step or final["state"] != expected_state:
            fail(f"{path.name}: wrong frozen crash-cut step/state")
    if payload["prior_release"]["kind"] != prior_kind:
        fail(f"{path.name}: wrong prior-release variant")
    if len(attempts) != attempt_count:
        fail(f"{path.name}: wrong recovery-owner count")
    if payload["known_good_candidate"]["kind"] != candidate_kind:
        fail(f"{path.name}: wrong candidate presence")

    if prior_kind == "first-install-absent":
        validate_first_install(payload["prior_release"]["value"], path)
    if "owner-takeover" in path.name:
        final = steps[-1]
        event = events[-1]
        if (
            final["recovery_attempt_id"] != attempts[-1]["attempt_id"]
            or final["direction"] != "recovery"
            or event["status"] != "resumed"
            or event["reason_code"] != "resumed-after-owner-loss"
        ):
            fail(f"{path.name}: replacement-owner replay is not a resumed event")
    if path.name.startswith("first-install-absent"):
        if any(row["direction"] != "recovery" for row in steps[-3:]):
            fail(f"{path.name}: absent restoration steps are not recovery-owned")
        validate_first_install_cut(payload, path)
    if path.name.startswith("explicit-rollback"):
        validate_explicit_rollback(payload, path)

    validate_nested_hashes(root, path)


class NativeFlock(ctypes.Structure):
    """Linux native struct flock for the canonical 64-bit Host ABI."""

    _fields_ = [
        ("l_type", ctypes.c_short),
        ("l_whence", ctypes.c_short),
        ("l_start", ctypes.c_longlong),
        ("l_len", ctypes.c_longlong),
        ("l_pid", ctypes.c_int),
    ]


def lock_call(fd: int, command: int, lock_type: int) -> NativeFlock:
    request = NativeFlock(lock_type, os.SEEK_SET, 0, 1, 0)
    result = fcntl.fcntl(fd, command, bytes(request))
    return NativeFlock.from_buffer_copy(result)


def process_state(pid: int) -> str:
    try:
        for line in Path(f"/proc/{pid}/status").read_text().splitlines():
            if line.startswith("State:"):
                return line.split()[1]
    except FileNotFoundError:
        return "missing"
    return "unknown"


def child_retains_inode(pid: int, expected: os.stat_result) -> bool:
    try:
        descriptors = Path(f"/proc/{pid}/fd").iterdir()
        for descriptor in descriptors:
            try:
                actual = descriptor.stat()
            except FileNotFoundError:
                continue
            if (actual.st_dev, actual.st_ino) == (expected.st_dev, expected.st_ino):
                return True
    except FileNotFoundError:
        return False
    return False


def read_pipe_line(fd: int, timeout_seconds: float) -> bytes:
    deadline = time.monotonic() + timeout_seconds
    data = bytearray()
    while b"\n" not in data:
        remaining = deadline - time.monotonic()
        if remaining <= 0 or not select.select([fd], [], [], remaining)[0]:
            fail("Linux lock proof timed out waiting for nested owner")
        chunk = os.read(fd, 4096)
        if not chunk:
            break
        data.extend(chunk)
    return bytes(data).split(b"\n", 1)[0]


def create_memfd(name: str, initial: bytes = b"") -> int:
    flags = getattr(os, "MFD_CLOEXEC", 0x0001)
    if hasattr(os, "memfd_create"):
        fd = os.memfd_create(name, flags)
    else:
        libc = ctypes.CDLL(None, use_errno=True)
        function = getattr(libc, "memfd_create", None)
        if function is None:
            fail("live Linux proofs require memfd_create")
        function.argtypes = [ctypes.c_char_p, ctypes.c_uint]
        function.restype = ctypes.c_int
        fd = function(name.encode("ascii"), flags)
        if fd < 0:
            error = ctypes.get_errno()
            raise OSError(error, os.strerror(error))
    if initial:
        os.pwrite(fd, initial, 0)
        os.ftruncate(fd, len(initial))
        os.fsync(fd)
    return fd


def write_memfd(fd: int, value: bytes) -> None:
    os.ftruncate(fd, 0)
    os.pwrite(fd, value, 0)
    os.ftruncate(fd, len(value))
    os.fsync(fd)


def read_memfd(fd: int) -> bytes:
    return os.pread(fd, os.fstat(fd).st_size, 0)


def prove_one_lock_mode(
    lock_type: int, query_type: int, expected_type: int, label: str
) -> None:
    child_pid: int | None = None
    owner_pid: int | None = None
    audit_fd: int | None = None
    lock_fd = create_memfd(f"srvls-{label}-admission-lock")
    try:
        pipe_read, pipe_write = os.pipe2(os.O_CLOEXEC)
        owner_pid = os.fork()
        if owner_pid == 0:
            try:
                os.close(pipe_read)
                owner_fd = os.dup(lock_fd)
                os.close(lock_fd)
                lock_call(owner_fd, fcntl.F_SETLK, lock_type)
                nested_pid = os.fork()
                if nested_pid == 0:
                    # This signal syscall is deliberately the child's first action.
                    os.kill(os.getpid(), signal.SIGSTOP)
                    os._exit(0)
                waited_pid, status = os.waitpid(nested_pid, os.WUNTRACED)
                if waited_pid != nested_pid or not os.WIFSTOPPED(status):
                    raise RuntimeError("nested child did not stop")
                os.write(pipe_write, f"OK {nested_pid}\n".encode("ascii"))
                while True:
                    signal.pause()
            except BaseException as exc:  # pragma: no cover - child error channel
                try:
                    os.write(pipe_write, f"ERR {type(exc).__name__}\n".encode("ascii"))
                finally:
                    os._exit(111)

        try:
            os.close(pipe_write)
            response = read_pipe_line(pipe_read, 5.0).decode("ascii", "replace")
            os.close(pipe_read)
            if not response.startswith("OK "):
                fail(f"Linux {label} lock owner failed: {response}")
            child_pid = int(response.split()[1])
            inode = os.fstat(lock_fd)
            if process_state(child_pid) not in {"T", "t"}:
                fail(f"Linux {label} child is not stopped before its first file action")
            if not child_retains_inode(child_pid, inode):
                fail(f"Linux {label} child did not retain the admission descriptor")

            audit_fd = os.dup(lock_fd)
            before = lock_call(audit_fd, fcntl.F_GETLK, query_type)
            if (
                before.l_type != expected_type
                or before.l_pid != owner_pid
                or before.l_whence != os.SEEK_SET
                or before.l_start != 0
                or before.l_len != 1
            ):
                fail(f"Linux {label} F_GETLK did not identify the isolated owner/range")

            os.kill(owner_pid, signal.SIGKILL)
            waited_pid, _ = os.waitpid(owner_pid, 0)
            if waited_pid != owner_pid:
                fail(f"Linux {label} owner was not reaped")
            owner_pid = None
            if process_state(child_pid) not in {"T", "t"}:
                fail(f"Linux {label} child did not remain stopped after owner death")
            if not child_retains_inode(child_pid, inode):
                fail(f"Linux {label} child lost its inherited descriptor unexpectedly")

            after = lock_call(audit_fd, fcntl.F_GETLK, query_type)
            if after.l_type != fcntl.F_UNLCK:
                fail(f"Linux {label} lock survived its process owner")
            lock_call(audit_fd, fcntl.F_SETLK, fcntl.F_WRLCK)
            if process_state(child_pid) not in {"T", "t"}:
                fail(f"Linux {label} contender waited for the stopped child")
            lock_call(audit_fd, fcntl.F_SETLK, fcntl.F_UNLCK)
        finally:
            if owner_pid is not None:
                try:
                    os.kill(owner_pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                try:
                    os.waitpid(owner_pid, 0)
                except ChildProcessError:
                    pass
            if child_pid is not None:
                try:
                    os.kill(child_pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
            if audit_fd is not None:
                os.close(audit_fd)
    finally:
        os.close(lock_fd)


def validate_linux_record_lock_semantics() -> None:
    if not sys.platform.startswith("linux") or not Path("/proc/self").exists():
        fail("the admission record-lock proof requires Linux with procfs")
    prove_one_lock_mode(fcntl.F_RDLCK, fcntl.F_WRLCK, fcntl.F_RDLCK, "shared")
    prove_one_lock_mode(fcntl.F_WRLCK, fcntl.F_RDLCK, fcntl.F_WRLCK, "exclusive")


def validate_lock_trace() -> None:
    value = load_exact(ROOT / "admission-record-lock.trace.json")
    lock = value["lock"]
    if (
        lock["command"] != "F_SETLK"
        or lock["blocking_command"] != "F_SETLKW"
        or [lock["whence"], lock["start"], lock["length"]] != ["SEEK_SET", 0, 1]
        or lock["forbidden"]
        != ["flock", "lockf", "F_OFD_GETLK", "F_OFD_SETLK", "F_OFD_SETLKW"]
    ):
        fail("admission record-lock grammar drift")
    cases = value["cases"]
    if [row["lease"] for row in cases] != ["shared", "exclusive"]:
        fail("admission trace does not cover shared then exclusive")
    expected_before = [
        ("F_WRLCK", {"type": "F_RDLCK", "owner_pid": 4100}),
        ("F_RDLCK", {"type": "F_WRLCK", "owner_pid": 4200}),
    ]
    for row, (query, expected) in zip(cases, expected_before):
        if (
            row["audit_query"] != query
            or row["audit_before"] != expected
            or row["child_state"] != "stopped-before-first-action"
            or row["audit_after"] != {"type": "F_UNLCK"}
            or row["contender"] != "acquired-while-child-stopped"
        ):
            fail("stopped-child takeover proof drift")
    validate_linux_record_lock_semantics()


def validate_dbus_trace() -> None:
    value = load_exact(ROOT / "manager-subscription.trace.json")
    expected_order = [
        "connect-user-bus",
        "addmatch-name-owner-changed-ack",
        "get-name-owner-bind",
        "addmatch-job-new-ack",
        "addmatch-job-removed-ack",
        "addmatch-timer-properties-ack",
        "addmatch-service-properties-ack",
        "manager-subscribe-success",
        "get-name-owner-unchanged",
        "drain-discontinuity-markers",
        "capture-baselines",
        "trigger-or-await",
    ]
    if value["required_order"] != expected_order:
        fail("manager owner/match/Subscribe ordering drift")
    handshake = value["success"]["handshake"]
    validate_manager_handshake(
        handshake,
        "manager-subscription.trace.json",
        "srvls-metrics.timer",
        "srvls-metrics.service",
        {
            "schema_version": "srvls-release-validation-attempt-v1",
            "recovery_attempt_id": "00000000-0000-7000-8000-000000000010",
            "recovery_attempt_sequence": 0,
            "effect_attempt": 0,
            "start_boot_ns": 2000000000,
            "timeout_ns": 120000000000,
            "absolute_deadline_boot_ns": 122000000000,
        },
    )
    if (
        handshake["manager_unique_owner"] != handshake["subscribe_reply_owner"]
        or handshake["manager_unique_owner"] != handshake["owner_recheck"]
        or [row["sequence"] for row in handshake["match_rules"]] != list(range(5))
        or handshake["status"] != "ready"
        or value["success"]["baseline_allowed"] is not True
        or value["success"]["trigger_allowed"] is not True
    ):
        fail("manager owner/match/Subscribe proof drift")
    expected_failures = {
        "addmatch-method-error": "dbus-match-failed",
        "subscribe-method-error": "dbus-subscribe-failed",
        "stale-owner-subscribe-reply": "dbus-owner-changed",
        "owner-away-and-back": "dbus-owner-changed",
        "unexpected-unsubscribe": "dbus-stream-discontinuity",
        "receive-dropped-marker": "dbus-stream-discontinuity",
        "receive-overflow-marker": "dbus-stream-discontinuity",
        "receive-sequence-gap": "dbus-stream-discontinuity",
        "disconnect-before-terminal-sample": "dbus-disconnected",
    }
    actual_failures = {row["cut"]: row["result"] for row in value["failures"]}
    if actual_failures != expected_failures or any(
        row["baseline_allowed"] is not False or row["trigger_allowed"] is not False
        for row in value["failures"]
    ):
        fail("manager failure/loss behavior drift")


def load_jsonl_exact(path: Path) -> list[dict[str, Any]]:
    raw = path.read_bytes()
    if not raw.endswith(b"\n") or raw.endswith(b"\n\n"):
        fail(f"{path.name}: expected exactly one final line feed")
    rows: list[dict[str, Any]] = []
    for index, line in enumerate(raw.splitlines()):
        try:
            value = parse_canonical_json(line)
        except CanonicalJsonError as exc:
            fail(f"{path.name}:{index + 1}: {exc}")
        if not isinstance(value, dict):
            fail(f"{path.name}:{index + 1}: line is not one canonical object")
        rows.append(value)
    if not rows:
        fail(f"{path.name}: transition chain is empty")
    return rows


def same_step_identity(left: dict[str, Any], right: dict[str, Any]) -> bool:
    ignored = {"state", "post_effect_evidence", "reason_code"}
    return all(left[key] == right[key] for key in STEP_KEYS if key not in ignored)


def validate_transition_pair(
    previous: dict[str, Any], current: dict[str, Any], path: Path, revision: int
) -> None:
    before = previous["payload"]
    after = current["payload"]
    if after["manifest_revision"] != revision:
        fail(f"{path.name}: revision sequence is not gap-free")
    if after["predecessor_checksum"] != {
        "kind": "present",
        "value": previous["checksum"],
    }:
        fail(f"{path.name}: predecessor does not name exact prior envelope checksum")
    if after["release_events"][:-1] != before["release_events"]:
        fail(f"{path.name}: transition rewrites prior events")
    event = after["release_events"][-1]
    if (
        event["sequence"] != revision - 1
        or event["manifest_revision"] != revision
    ):
        fail(f"{path.name}: appended event does not bind replacement revision")
    immutable = {
        "transaction_id",
        "intent",
        "original_owner",
        "old_install_generation",
        "target_install_generation",
        "rollback_target",
        "paths",
        "artifacts",
        "consumers",
    }
    for key in immutable:
        if after[key] != before[key]:
            fail(f"{path.name}: transition mutates immutable {key}")

    before_steps = before["step_records"]
    after_steps = after["step_records"]
    status = event["status"]
    if status in {"started", "resumed"}:
        if (
            len(after_steps) != len(before_steps) + 1
            or after_steps[:-1] != before_steps
            or after_steps[-1]["state"] != "pending"
            or after_steps[-1]["post_effect_evidence"]
        ):
            fail(f"{path.name}: start/resume does not append one pending step")
    elif status == "skipped":
        if (
            len(after_steps) != len(before_steps) + 1
            or after_steps[:-1] != before_steps
            or after_steps[-1]["state"] != "skipped"
        ):
            fail(f"{path.name}: skip does not append one skipped step")
    elif status in {"succeeded", "failed"}:
        expected_state = "complete" if status == "succeeded" else "failed"
        if (
            len(after_steps) != len(before_steps)
            or after_steps[:-1] != before_steps[:-1]
            or not before_steps
            or before_steps[-1]["state"] != "pending"
            or after_steps[-1]["state"] != expected_state
            or not same_step_identity(before_steps[-1], after_steps[-1])
        ):
            fail(f"{path.name}: terminal event does not finalize pending step")
    else:
        fail(f"{path.name}: unknown event status in transition chain")

    if status == "resumed":
        if (
            len(after["recovery_attempts"]) != len(before["recovery_attempts"]) + 1
            or after["recovery_attempts"][:-1] != before["recovery_attempts"]
            or after["recovery_attempts"][-1]["predecessor_manifest_checksum"]
            != {"kind": "present", "value": previous["checksum"]}
            or after["active_recovery_attempt_id"]
            != after["recovery_attempts"][-1]["attempt_id"]
        ):
            fail(f"{path.name}: resumed transition lacks exact owner publication")
    elif after["recovery_attempts"] != before["recovery_attempts"]:
        fail(f"{path.name}: non-resume transition changes recovery owner")

    changed_state = before["state_backup"] != after["state_backup"]
    changed_prior = before["prior_release"] != after["prior_release"]
    if changed_state or changed_prior:
        if (
            event["manifest_step"] != "create-backup"
            or status != "succeeded"
            or before["state_backup"] != {"kind": "absent"}
            or after["state_backup"].get("kind") != "present"
        ):
            fail(f"{path.name}: backup authority changes outside completed backup")
        if changed_prior:
            before_state = before["prior_release"]["value"]["state_disposition"]
            after_state = after["prior_release"]["value"]["state_disposition"]
            if (
                before_state.get("kind") != "restore-planned"
                or after_state.get("kind") != "restore-recorded"
                or before_state["plan"]["backup_database_path"]
                != after_state["backup_manifest"]["backup_database_path"]
            ):
                fail(f"{path.name}: FirstInstall backup does not finalize its frozen plan")

    candidate_changed = before["known_good_candidate"] != after["known_good_candidate"]
    if candidate_changed and not (
        event["manifest_step"] == "stage-known-good-candidate"
        and status == "succeeded"
        and before["known_good_candidate"] == {"kind": "absent"}
        and after["known_good_candidate"].get("kind") == "present"
    ):
        fail(f"{path.name}: KnownGood candidate changes outside its completed step")
    decision_changed = before["commit_decision"] != after["commit_decision"]
    if decision_changed and not (
        event["manifest_step"] == "commit-decided"
        and status == "succeeded"
        and before["commit_decision"] == {"kind": "undecided"}
        and after["commit_decision"].get("kind") == "decided"
    ):
        fail(f"{path.name}: commit decision changes outside its completed step")
    terminal_changed = before["terminal_result"] != after["terminal_result"]
    if terminal_changed and not (
        event["manifest_step"] in {"commit-transaction", "complete-rolled-back"}
        and status == "succeeded"
        and before["terminal_result"] == {"kind": "pending"}
        and after["terminal_result"].get("kind") != "pending"
    ):
        fail(f"{path.name}: terminal result changes outside terminal completion")


def validate_transition_root(root: dict[str, Any], path: Path, revision: int) -> None:
    if list(root) != OUTER_KEYS or root["schema_version"] != "srvls-upgrade-transaction-v1":
        fail(f"{path.name}: transition outer schema/key order mismatch")
    payload = root["payload"]
    if list(payload) != PAYLOAD_KEYS:
        fail(f"{path.name}: transition payload key order mismatch")
    if root["checksum"] != digest("srvls-upgrade-transaction-v1", payload):
        fail(f"{path.name}: transition checksum mismatch")
    if payload["manifest_revision"] != revision:
        fail(f"{path.name}: transition revision mismatch")
    validate_payload_semantics(payload, path)
    validate_tagged_presence(root, path)
    validate_path_evidence(root, path)
    validate_nested_hashes(root, path)
    events = payload["release_events"]
    if len(events) != revision or [row["sequence"] for row in events] != list(range(revision)):
        fail(f"{path.name}: event history does not cover every replacement")
    if any(row["manifest_revision"] != index + 1 for index, row in enumerate(events)):
        fail(f"{path.name}: event revision history is not exact")
    steps = payload["step_records"]
    if [row["sequence"] for row in steps] != list(range(len(steps))):
        fail(f"{path.name}: transition step history is not gap-free")
    if any(list(row) != STEP_KEYS for row in steps):
        fail(f"{path.name}: transition step key order mismatch")
    if any(list(row) != EVENT_KEYS for row in events):
        fail(f"{path.name}: transition event key order mismatch")
    attempts = payload["recovery_attempts"]
    if (
        not attempts
        or [row["sequence"] for row in attempts] != list(range(len(attempts)))
        or any(list(row) != ATTEMPT_KEYS for row in attempts)
        or payload["active_recovery_attempt_id"] != attempts[-1]["attempt_id"]
    ):
        fail(f"{path.name}: transition recovery-owner history mismatch")
    if payload["prior_release"]["kind"] == "first-install-absent":
        validate_first_install(payload["prior_release"]["value"], path)
    if payload["intent"] == "rollback":
        validate_explicit_rollback(payload, path, require_checkpoint=False)
    if steps:
        final = steps[-1]
        expected_cursor = {
            "kind": "present",
            "value": {
                "sequence": final["sequence"],
                "step": final["step"],
                "effect_attempt": final["effect_attempt"],
            },
        }
        if payload["current_step"] != expected_cursor:
            fail(f"{path.name}: transition current-step cursor mismatch")
    elif payload["current_step"] != {"kind": "absent"}:
        fail(f"{path.name}: empty transition has a current-step cursor")


def validate_transition_chains() -> None:
    forward_cuts = {
        ("commit-decided", "complete"): "commit-decided-complete.manifest.json",
        ("publish-known-good", "pending"): "known-good-publication-pending.manifest.json",
        ("publish-known-good", "complete"): "known-good-publication-complete.manifest.json",
        ("persist-ready-admission", "pending"): "ready-admission-pending.manifest.json",
    }
    terminal_roots: dict[str, dict[str, Any]] = {}
    for name, (cut_name, cut_state, terminal_kind) in TRANSITION_FILES.items():
        path = ROOT / name
        rows = load_jsonl_exact(path)
        if rows[0]["payload"]["predecessor_checksum"] != {"kind": "absent"}:
            fail(f"{name}: revision zero has a predecessor")
        snapshots: dict[tuple[str, str], dict[str, Any]] = {}
        for revision, root in enumerate(rows):
            label = Path(f"{name}:{revision}")
            validate_transition_root(root, label, revision)
            if revision:
                validate_transition_pair(rows[revision - 1], root, label, revision)
            steps = root["payload"]["step_records"]
            if steps:
                snapshots[(steps[-1]["step"], steps[-1]["state"])] = root
        if rows[-1]["payload"]["terminal_result"].get("kind") != terminal_kind:
            fail(f"{name}: chain does not reach its declared terminal truth")
        cut = snapshots.get(cut_state)
        if cut is None or cut != load_exact(ROOT / cut_name):
            fail(f"{name}: named crash cut is not an exact chain envelope")
        if name == "forward.transitions.jsonl":
            for identity, manifest_name in forward_cuts.items():
                if snapshots.get(identity) != load_exact(ROOT / manifest_name):
                    fail(f"{name}: {manifest_name} is not its exact chain envelope")
        final_path = Path(f"{name}:terminal")
        validate_tagged_presence(rows[-1], final_path)
        validate_path_evidence(rows[-1], final_path)
        validate_payload_semantics(rows[-1]["payload"], final_path)
        validate_nested_hashes(rows[-1], final_path)
        terminal_roots[name] = rows[-1]
    validate_release_semantic_negative_oracles(terminal_roots)


def expect_release_semantics_rejected(root: dict[str, Any], label: str) -> None:
    try:
        root["checksum"] = digest("srvls-upgrade-transaction-v1", root["payload"])
    except CanonicalJsonError:
        return
    try:
        validate_transition_root(
            root,
            Path(f"negative-release:{label}"),
            root["payload"]["manifest_revision"],
        )
    except SystemExit:
        return
    fail(f"checksum-resealed negative release semantic oracle accepted {label}")


def validate_release_semantic_negative_oracles(
    roots: dict[str, dict[str, Any]]
) -> None:
    wrong_trigger = copy.deepcopy(roots["forward.transitions.jsonl"])
    trigger_atom = next(
        atom
        for step in wrong_trigger["payload"]["step_records"]
        for atom in step["post_effect_evidence"]
        if atom.get("kind") == "timer"
    )
    trigger_atom["acceptance"]["causality_proof"]["activation_details"][0][
        "value"
    ] = "srvls-wrong.timer"
    expect_release_semantics_rejected(wrong_trigger, "wrong-trigger-unit")

    wrong_job_path = copy.deepcopy(roots["forward.transitions.jsonl"])
    job_atom = next(
        atom
        for step in wrong_job_path["payload"]["step_records"]
        for atom in step["post_effect_evidence"]
        if atom.get("kind") == "timer"
    )
    job_rule = next(
        row
        for row in job_atom["acceptance"]["handshake"]["match_rules"]
        if row["member"] == "JobNew"
    )
    job_rule["path"] = "/org/freedesktop/systemd1/unit/srvls_2dwrong_2eservice"
    expect_release_semantics_rejected(wrong_job_path, "wrong-jobnew-object-path")

    string_admission = copy.deepcopy(roots["forward.transitions.jsonl"])
    admission_atom = next(
        atom
        for step in string_admission["payload"]["step_records"]
        for atom in step["post_effect_evidence"]
        if atom.get("kind") == "admission"
    )
    admission_atom["install_generation"] = "0"
    expect_release_semantics_rejected(string_admission, "string-admission-generation")

    swapped_terminal = copy.deepcopy(roots["explicit-rollback.transitions.jsonl"])
    swapped = {
        "kind": "rolled-back",
        "source_install_generation": 7,
        "target_install_generation": 8,
    }
    swapped_terminal["payload"]["terminal_result"] = swapped
    for step in swapped_terminal["payload"]["step_records"]:
        for atom in step["post_effect_evidence"]:
            if atom.get("kind") == "transaction":
                atom["result"] = copy.deepcopy(swapped)
    expect_release_semantics_rejected(swapped_terminal, "swapped-terminal-direction")

    impossible_takeover = copy.deepcopy(roots["owner-takeover.transitions.jsonl"])
    impossible_takeover["payload"]["recovery_attempts"][-1][
        "acquisition_boot_ns"
    ] = 1100000000
    expect_release_semantics_rejected(impossible_takeover, "predating-owner-takeover")

    wrong_deadline = copy.deepcopy(roots["forward.transitions.jsonl"])
    for value in walk(wrong_deadline["payload"]["step_records"]):
        if value.get("schema_version") == "srvls-release-validation-attempt-v1":
            value["absolute_deadline_boot_ns"] += 1
    expect_release_semantics_rejected(wrong_deadline, "unchecked-validation-deadline")

    mislabeled_upgrade = copy.deepcopy(roots["upgrade.transitions.jsonl"])
    mislabeled_upgrade["payload"]["intent"] = "install"
    expect_release_semantics_rejected(mislabeled_upgrade, "upgrade-mislabeled-install")

    unknown_path_field = copy.deepcopy(roots["upgrade.transitions.jsonl"])
    unknown_path_field["payload"]["paths"]["future_default"] = {"kind": "absent"}
    expect_release_semantics_rejected(unknown_path_field, "unknown-release-path-field")

    aliased_artifact = copy.deepcopy(roots["upgrade.transitions.jsonl"])
    aliased_artifact["payload"]["artifacts"]["candidate_binary"]["path"] = copy.deepcopy(
        aliased_artifact["payload"]["artifacts"]["prior_binary"]["path"]
    )
    expect_release_semantics_rejected(aliased_artifact, "artifact-path-alias")

    unnormalized_path = copy.deepcopy(roots["upgrade.transitions.jsonl"])
    unnormalized_path["payload"]["paths"]["database_path"] = (
        "%2Fhome%2Ftest%2F%2F.local%2Fstate%2Fsrvls%2Fstate.sqlite3"
    )
    expect_release_semantics_rejected(unnormalized_path, "unnormalized-linux-path")

    wrong_backup_path = copy.deepcopy(roots["upgrade.transitions.jsonl"])
    backup = wrong_backup_path["payload"]["state_backup"]["value"]
    backup["source_files"][1]["path"] = (
        "%2Fhome%2Ftest%2F.local%2Fstate%2Fsrvls%2Fwrong.sqlite3-wal"
    )
    backup["manifest_hash"] = digest(
        "srvls-state-backup-manifest-v1", without(backup, "manifest_hash")
    )
    for step in wrong_backup_path["payload"]["step_records"]:
        for atom in [*step["pre_effect_evidence"], *step["post_effect_evidence"]]:
            if atom.get("kind") == "backup":
                atom["manifest_hash"] = backup["manifest_hash"]
    expect_release_semantics_rejected(wrong_backup_path, "unbound-backup-sidecar-path")

    open_candidate = copy.deepcopy(roots["upgrade.transitions.jsonl"])
    open_candidate["payload"]["known_good_candidate"]["value"]["future"] = True
    expect_release_semantics_rejected(open_candidate, "open-known-good-candidate")

    wrong_decision = copy.deepcopy(roots["upgrade.transitions.jsonl"])
    wrong_decision["payload"]["commit_decision"]["target_install_generation"] = 7
    expect_release_semantics_rejected(wrong_decision, "unbound-commit-decision")

    wrong_order = copy.deepcopy(roots["upgrade.transitions.jsonl"])
    steps = wrong_order["payload"]["step_records"]
    steps[0], steps[1] = steps[1], steps[0]
    steps[0]["sequence"], steps[1]["sequence"] = 0, 1
    expect_release_semantics_rejected(wrong_order, "swapped-step-order")

    wrong_direction = copy.deepcopy(roots["upgrade.transitions.jsonl"])
    wrong_direction["payload"]["step_records"][6]["direction"] = "recovery"
    expect_release_semantics_rejected(wrong_direction, "forward-direction-flip")

    repeated_pair = copy.deepcopy(roots["upgrade.transitions.jsonl"])
    consumer_step = next(
        step
        for step in repeated_pair["payload"]["step_records"]
        if step["step"] == "daemon-reload"
    )
    duplicate = copy.deepcopy(consumer_step["post_effect_evidence"][0])
    duplicate["readback"] = "intended"
    consumer_step["post_effect_evidence"].append(duplicate)
    consumer_step["post_effect_evidence"] = sorted(
        consumer_step["post_effect_evidence"], key=evidence_sort_key
    )
    expect_release_semantics_rejected(repeated_pair, "repeated-consumer-pair-evidence")

    embedded_unavailable = copy.deepcopy(roots["upgrade.transitions.jsonl"])
    embedded_unavailable["payload"]["terminal_result"] = {
        "kind": "rollback-unavailable",
        "reason": "no-prior-release",
    }
    expect_release_semantics_rejected(
        embedded_unavailable, "transaction-embedded-rollback-unavailable"
    )

    wrong_failing_step = copy.deepcopy(roots["upgrade-recovery.transitions.jsonl"])
    wrong_failing_step["payload"]["terminal_result"]["failing_step"] = "isolated-smoke"
    for step in wrong_failing_step["payload"]["step_records"]:
        for atom in step["post_effect_evidence"]:
            if atom.get("kind") == "transaction":
                atom["result"] = copy.deepcopy(
                    wrong_failing_step["payload"]["terminal_result"]
                )
    expect_release_semantics_rejected(wrong_failing_step, "wrong-terminal-failing-step")

    first_install_generation = copy.deepcopy(roots["forward.transitions.jsonl"])
    first_install_generation["payload"]["prior_release"]["value"][
        "prior_install_generation"
    ] = 1
    expect_release_semantics_rejected(
        first_install_generation, "first-install-nonzero-generation"
    )

    first_install_unit = copy.deepcopy(roots["forward.transitions.jsonl"])
    first_install_unit["payload"]["prior_release"]["value"]["consumer_disposition"][
        "units"
    ][0]["future"] = False
    expect_release_semantics_rejected(first_install_unit, "open-first-install-unit")

    initial = copy.deepcopy(
        load_jsonl_exact(ROOT / "first-install-recovery.transitions.jsonl")[0]
    )
    initial["payload"]["prior_release"]["value"]["state_disposition"]["plan"][
        "transaction_id"
    ] = "00000000-0000-7000-8000-000000000099"
    expect_release_semantics_rejected(initial, "first-install-plan-transaction-mismatch")

    overflow = copy.deepcopy(roots["upgrade.transitions.jsonl"])
    overflow["payload"]["target_install_generation"] = 1 << 64
    expect_release_semantics_rejected(overflow, "u64-overflow")


def replace_text_tree(value: Any, old: str, new: str) -> Any:
    if isinstance(value, str):
        return value.replace(old, new)
    if isinstance(value, list):
        return [replace_text_tree(child, old, new) for child in value]
    if isinstance(value, dict):
        return {
            key: replace_text_tree(child, old, new) for key, child in value.items()
        }
    return value


def validate_first_install_multi_pair_positive() -> None:
    root = load_jsonl_exact(ROOT / "first-install-recovery.transitions.jsonl")[0]
    first = copy.deepcopy(root["payload"]["prior_release"]["value"])
    source_units = copy.deepcopy(first["consumer_disposition"]["units"])
    extra_units = replace_text_tree(source_units, "metrics", "snapshot")
    # timers.target.wants is shared; the earliest metrics row owns its one
    # prior-directory disposition while both links remain independently frozen.
    extra_units[1]["drop_in_directories"] = []
    first["consumer_disposition"]["units"].extend(extra_units)
    validate_first_install(
        first,
        Path("positive-two-pair-first-install"),
        expected_transaction_id=root["payload"]["transaction_id"],
        expected_canonical_link_path=root["payload"]["paths"]["canonical_link_path"],
        expected_versioned_binary_path=root["payload"]["paths"][
            "candidate_versioned_binary_path"
        ],
    )


def validate_admission(value: dict[str, Any], path: Path, expected_status: str) -> None:
    if list(value) != ADMISSION_KEYS or value["schema_version"] != "srvls-release-admission-v1":
        fail(f"{path.name}: admission schema/key order mismatch")
    if value["status"] != expected_status:
        fail(f"{path.name}: admission status mismatch")
    require_unsigned(value["install_generation"], f"{path.name}: install_generation")
    transaction = value["transaction_id"]
    if expected_status == "ready" and transaction != {"kind": "absent"}:
        fail(f"{path.name}: ready admission carries a transaction")
    if expected_status == "ready" and value["install_generation"] != 1:
        fail(f"{path.name}: ready admission generation drift")
    if expected_status == "recovering":
        if list(transaction) != ["kind", "value"] or transaction.get("kind") != "present":
            fail(f"{path.name}: recovering admission lacks a transaction")
        require_uuid(transaction["value"], f"{path.name}: transaction_id")
        if value["install_generation"] != 0:
            fail(f"{path.name}: recovering admission generation drift")
    expected = digest("srvls-release-admission-v1", without(value, "checksum"))
    if value["checksum"] != expected:
        fail(f"{path.name}: admission checksum mismatch")


def validate_known_good(value: dict[str, Any], path: Path, prior_kind: str) -> None:
    if list(value) != KNOWN_GOOD_KEYS or value["schema_version"] != "srvls-known-good-release-v1":
        fail(f"{path.name}: KnownGood schema/key order mismatch")
    payload = value["payload"]
    if list(payload) != KNOWN_GOOD_PAYLOAD_KEYS:
        fail(f"{path.name}: KnownGood payload key order mismatch")
    require_uuid(payload["source_transaction_id"], f"{path.name}: source transaction")
    require_unsigned(
        payload["published_install_generation"], f"{path.name}: published generation"
    )
    if value["checksum"] != digest("srvls-known-good-release-v1", payload):
        fail(f"{path.name}: KnownGood checksum mismatch")
    candidate = payload["candidate"]
    validate_known_good_candidate_value(candidate, path, "KnownGood candidate")
    prior = candidate["prior_release"]
    if list(prior) != ["kind", "value"] or prior["kind"] != prior_kind:
        fail(f"{path.name}: KnownGood prior variant mismatch")
    if prior_kind == "installed":
        validate_installed_release(prior["value"], path, "KnownGood installed prior")
        if abs(
            payload["published_install_generation"]
            - prior["value"]["install_generation"]
        ) != 1:
            fail(f"{path.name}: KnownGood generation is not adjacent to retained prior")
    else:
        validate_first_install(prior["value"], path)
        if payload["published_install_generation"] != 1:
            fail(f"{path.name}: FirstInstall KnownGood generation is not one")


def validate_fd4_pair(
    request: dict[str, Any], result: dict[str, Any], name: str, kind: str
) -> None:
    if list(request) != FD4_REQUEST_KEYS or request["protocol"] != "srvls-release-validation-v1":
        fail(f"{name}: FD4 request schema/key order mismatch")
    if request["mode"] != "read-only-release-validation":
        fail(f"{name}: FD4 request mode drift")
    for key in ("request_id", "transaction_id", "recovery_attempt_id"):
        require_uuid(request[key], f"{name}: fd4-request.{key}")
    if not isinstance(request["capability"], str) or re.fullmatch(
        r"[0-9a-f]{64}", request["capability"]
    ) is None:
        fail(f"{name}: FD4 capability is not exact 256-bit lowercase hex")
    for key in (
        "recovery_attempt_sequence",
        "manifest_revision",
        "old_install_generation",
        "candidate_install_generation",
        "allowed_database_schema",
        "absolute_deadline_boot_ns",
    ):
        require_unsigned(request[key], f"{name}: fd4-request.{key}")
    if request["absolute_deadline_boot_ns"] == 0:
        fail(f"{name}: FD4 deadline is zero")
    for key in ("manifest_checksum", "candidate_binary_sha256", "backup_manifest_hash"):
        require_sha256(request[key], f"{name}: fd4-request.{key}")
    decoded_linux_path(request["database_path"], f"{name}: fd4-request.database_path")
    echo_keys = [
        "protocol",
        "request_id",
        "capability",
        "transaction_id",
        "recovery_attempt_id",
        "recovery_attempt_sequence",
        "manifest_revision",
        "manifest_checksum",
        "candidate_install_generation",
        "candidate_binary_sha256",
    ]
    if list(result) != FD4_RESULT_KEYS:
        fail(f"{name}: FD4 result key order mismatch")
    if any(result[key] != request[key] for key in echo_keys):
        fail(f"{name}: FD4 echo differs from request")
    body = result["result"]
    if kind == "validated":
        if list(body) != [
            "kind",
            "database_schema",
            "integrity_result",
            "read_only_proof_sha256",
        ] or body["kind"] != "validated" or body["integrity_result"] != "ok":
            fail(f"{name}: validated result shape mismatch")
        require_unsigned(body["database_schema"], f"{name}: result.database_schema")
        if body["database_schema"] != request["allowed_database_schema"]:
            fail(f"{name}: validated database schema differs from request authority")
        require_sha256(body["read_only_proof_sha256"], f"{name}: read-only proof")
    elif (
        list(body) != ["kind", "code"]
        or body.get("kind") != "rejected"
        or body.get("code") not in FD4_REJECTION_CODES
    ):
        fail(f"{name}: rejected result shape/code mismatch")


def validate_fd4_manifest_binding(request: dict[str, Any], name: str) -> None:
    revision = request["manifest_revision"]
    matches: list[tuple[str, dict[str, Any]]] = []
    for transition_name in TRANSITION_FILES:
        rows = load_jsonl_exact(ROOT / transition_name)
        if revision < len(rows) and rows[revision]["checksum"] == request["manifest_checksum"]:
            matches.append((transition_name, rows[revision]))
    if len(matches) != 1:
        fail(f"{name}: FD4 request does not bind exactly one transition envelope")
    transition_name, root = matches[0]
    payload = root["payload"]
    step = payload["step_records"][-1]
    if step["step"] not in {"validate-candidate", "validate-restored-pair"} or step[
        "state"
    ] != "pending":
        fail(f"{name}: FD4 manifest is not the pending validation cut")
    validation = step["validation_attempt"]
    if validation.get("kind") != "present":
        fail(f"{name}: FD4 manifest lacks a persisted validation attempt")
    attempt = validation["value"]
    request_evidence = [
        atom
        for atom in step["pre_effect_evidence"]
        if atom.get("kind") == "fd4"
    ]
    if (
        len(request_evidence) != 1
        or request_evidence[0]["result"] != "validated"
        or request["request_id"] != request_evidence[0]["request_id"]
    ):
        fail(f"{name}: FD4 request identity differs from persisted step evidence")
    backup = payload["state_backup"]
    if backup.get("kind") != "present":
        fail(f"{name}: FD4 manifest lacks a persisted state backup")
    if step["step"] == "validate-candidate":
        candidate_generation = payload["target_install_generation"]
        candidate_artifact = payload["artifacts"]["candidate_binary"]
        allowed_schema = payload["artifacts"]["target_database_schema"]
    elif payload["intent"] == "rollback":
        candidate_generation = payload["target_install_generation"]
        candidate_artifact = payload["artifacts"]["candidate_binary"]
        allowed_schema = payload["artifacts"]["target_database_schema"]
    else:
        candidate_generation = payload["old_install_generation"]
        candidate_artifact = payload["artifacts"]["prior_binary"]
        allowed_schema = payload["artifacts"]["prior_database_schema"]
    if candidate_artifact.get("kind") != "present":
        fail(f"{name}: FD4 validation role has no present candidate artifact")
    expected = {
        "transaction_id": payload["transaction_id"],
        "recovery_attempt_id": attempt["recovery_attempt_id"],
        "recovery_attempt_sequence": attempt["recovery_attempt_sequence"],
        "manifest_revision": payload["manifest_revision"],
        "manifest_checksum": root["checksum"],
        "old_install_generation": payload["old_install_generation"],
        "candidate_install_generation": candidate_generation,
        "candidate_binary_sha256": candidate_artifact["sha256"]["value"],
        "database_path": payload["paths"]["database_path"],
        "allowed_database_schema": allowed_schema,
        "backup_manifest_hash": backup["value"]["manifest_hash"],
        "absolute_deadline_boot_ns": attempt["absolute_deadline_boot_ns"],
    }
    for key, value in expected.items():
        if request[key] != value:
            fail(
                f"{name}: FD4 {key} differs from {transition_name} persisted authority"
            )


def expect_fd4_rejected(
    request: dict[str, Any], result: dict[str, Any], label: str
) -> None:
    try:
        validate_fd4_pair(request, result, f"negative oracle {label}", "validated")
    except SystemExit:
        return
    fail(f"negative FD4 oracle accepted {label}")


def expect_fd4_binding_rejected(
    request: dict[str, Any], result: dict[str, Any], label: str
) -> None:
    try:
        validate_fd4_pair(request, result, f"negative binding {label}", "validated")
        validate_fd4_manifest_binding(request, f"negative binding {label}")
    except SystemExit:
        return
    fail(f"negative FD4 manifest-binding oracle accepted {label}")


def validate_fd4_negative_oracles(
    request: dict[str, Any], validated: dict[str, Any]
) -> None:
    string_sequence_request = copy.deepcopy(request)
    string_sequence_result = copy.deepcopy(validated)
    string_sequence_request["recovery_attempt_sequence"] = "0"
    string_sequence_result["recovery_attempt_sequence"] = "0"
    expect_fd4_rejected(
        string_sequence_request,
        string_sequence_result,
        "string-recovery-attempt-sequence",
    )

    string_revision_request = copy.deepcopy(request)
    string_revision_result = copy.deepcopy(validated)
    string_revision_request["manifest_revision"] = "23"
    string_revision_result["manifest_revision"] = "23"
    expect_fd4_rejected(string_revision_request, string_revision_result, "string-revision")

    string_generation_request = copy.deepcopy(request)
    string_generation_result = copy.deepcopy(validated)
    string_generation_request["candidate_install_generation"] = "1"
    string_generation_result["candidate_install_generation"] = "1"
    expect_fd4_rejected(
        string_generation_request,
        string_generation_result,
        "string-candidate-generation",
    )

    string_deadline_request = copy.deepcopy(request)
    string_deadline_result = copy.deepcopy(validated)
    string_deadline_request["absolute_deadline_boot_ns"] = "312000000000"
    expect_fd4_rejected(string_deadline_request, string_deadline_result, "string-deadline")

    string_allowed_schema_request = copy.deepcopy(request)
    string_allowed_schema_result = copy.deepcopy(validated)
    string_allowed_schema_request["allowed_database_schema"] = "2"
    expect_fd4_rejected(
        string_allowed_schema_request,
        string_allowed_schema_result,
        "string-allowed-schema",
    )

    string_result_schema_request = copy.deepcopy(request)
    string_result_schema_result = copy.deepcopy(validated)
    string_result_schema_result["result"]["database_schema"] = "2"
    expect_fd4_rejected(
        string_result_schema_request,
        string_result_schema_result,
        "string-result-schema",
    )

    invalid_uuid_request = copy.deepcopy(request)
    invalid_uuid_result = copy.deepcopy(validated)
    invalid_uuid_request["request_id"] = "NOT-A-UUID"
    invalid_uuid_result["request_id"] = "NOT-A-UUID"
    expect_fd4_rejected(invalid_uuid_request, invalid_uuid_result, "invalid-request-uuid")


def validate_fd4_envelopes() -> None:
    specifications = [
        ("fd4-request.json", "fd4-validated-result.json"),
        ("fd4-upgrade-request.json", "fd4-upgrade-validated-result.json"),
        ("fd4-rollback-request.json", "fd4-rollback-validated-result.json"),
        ("fd4-recovery-request.json", "fd4-recovery-validated-result.json"),
    ]
    loaded: dict[str, tuple[dict[str, Any], dict[str, Any]]] = {}
    for request_name, result_name in specifications:
        request = load_exact(ROOT / request_name)
        validated = load_exact(ROOT / result_name)
        validate_fd4_pair(request, validated, result_name, "validated")
        validate_fd4_manifest_binding(request, request_name)
        loaded[request_name] = (request, validated)

    request, validated = loaded["fd4-request.json"]
    rejected = load_exact(ROOT / "fd4-rejected-result.json")
    validate_fd4_pair(request, rejected, "fd4-rejected-result.json", "rejected")
    alternate_rejection = copy.deepcopy(rejected)
    alternate_rejection["result"]["code"] = "deadline-expired"
    validate_fd4_pair(
        request, alternate_rejection, "fd4-alternate-rejection-code", "rejected"
    )
    invalid_rejection = copy.deepcopy(rejected)
    invalid_rejection["result"]["code"] = "not-a-release-reason"
    try:
        validate_fd4_pair(
            request, invalid_rejection, "negative unknown rejection code", "rejected"
        )
    except SystemExit:
        pass
    else:
        fail("negative FD4 oracle accepted an unknown rejection code")
    validate_fd4_negative_oracles(request, validated)
    wrong_deadline = copy.deepcopy(request)
    wrong_deadline["absolute_deadline_boot_ns"] += 1
    expect_fd4_binding_rejected(
        wrong_deadline, validated, "deadline-differs-from-persisted-attempt"
    )
    rollback_request, rollback_result = loaded["fd4-rollback-request.json"]
    wrong_rollback_generation = copy.deepcopy(rollback_request)
    wrong_rollback_result = copy.deepcopy(rollback_result)
    wrong_rollback_generation["candidate_install_generation"] = rollback_request[
        "old_install_generation"
    ]
    wrong_rollback_result["candidate_install_generation"] = wrong_rollback_generation[
        "candidate_install_generation"
    ]
    expect_fd4_binding_rejected(
        wrong_rollback_generation,
        wrong_rollback_result,
        "explicit-rollback-old-generation-used-as-target",
    )
    recovery_request, recovery_result = loaded["fd4-recovery-request.json"]
    wrong_recovery_generation = copy.deepcopy(recovery_request)
    wrong_recovery_result = copy.deepcopy(recovery_result)
    wrong_recovery_generation["candidate_install_generation"] = 8
    wrong_recovery_result["candidate_install_generation"] = 8
    expect_fd4_binding_rejected(
        wrong_recovery_generation,
        wrong_recovery_result,
        "installed-recovery-target-generation-used-as-restored-source",
    )
    swapped_manifest = copy.deepcopy(rollback_request)
    swapped_result = copy.deepcopy(rollback_result)
    swapped_manifest["manifest_revision"] = recovery_request["manifest_revision"]
    swapped_manifest["manifest_checksum"] = recovery_request["manifest_checksum"]
    swapped_result["manifest_revision"] = recovery_request["manifest_revision"]
    swapped_result["manifest_checksum"] = recovery_request["manifest_checksum"]
    expect_fd4_binding_rejected(
        swapped_manifest, swapped_result, "swapped-direction-manifest-authority"
    )


def validate_brownfield_consumer_value(value: dict[str, Any], context: str) -> None:
    if list(value) != BROWNFIELD_KEYS:
        fail(f"{context}: brownfield authority key order mismatch")
    if value["schema_version"] != "srvls-brownfield-consumer-pairs-v1":
        fail(f"{context}: brownfield authority schema mismatch")
    basis = value["source_basis"]
    if list(basis) != BROWNFIELD_BASIS_KEYS or {
        "kind": basis["kind"],
        "host": basis["host"],
        "captured_on": basis["captured_on"],
        "home_substitution": basis["home_substitution"],
    } != {
        "kind": "live-user-systemd-normalized",
        "host": "big-chungus",
        "captured_on": "2026-07-17",
        "home_substitution": "/home/delorenj=>/home/test",
    }:
        fail(f"{context}: brownfield source basis drift")
    basis_files = basis["files"]
    expected_units = [
        "srvls-metrics.service",
        "srvls-metrics.timer",
        "srvls-snapshot.service",
        "srvls-snapshot.timer",
    ]
    if [row.get("unit_name") for row in basis_files] != expected_units or any(
        list(row) != BROWNFIELD_BASIS_FILE_KEYS for row in basis_files
    ):
        fail(f"{context}: brownfield source-file inventory mismatch")
    for row in basis_files:
        require_sha256(
            row["host_fragment_sha256"],
            f"{context}: {row['unit_name']} Host fragment",
        )
    basis_hashes = {
        row["unit_name"]: row["host_fragment_sha256"] for row in basis_files
    }
    require_unsigned(value["source_install_generation"], f"{context}: source generation")
    require_unsigned(
        value["candidate_install_generation"], f"{context}: candidate generation"
    )
    if value["candidate_install_generation"] != value["source_install_generation"] + 1:
        fail(f"{context}: brownfield generations are not consecutive")
    pairs = value["pairs"]
    pair_ids = [row.get("pair_id") for row in pairs]
    if pair_ids != ["metrics", "snapshot"] or any(
        list(row) != BROWNFIELD_PAIR_KEYS for row in pairs
    ):
        fail(f"{context}: brownfield pairs are not exact sorted metrics/snapshot")
    forward: list[dict[str, Any]] = []
    rollback: list[dict[str, Any]] = []
    for row in pairs:
        pair_id = row["pair_id"]
        source = row["source"]
        candidate = row["candidate"]
        if source.get("pair_id") != pair_id or candidate.get("pair_id") != pair_id:
            fail(f"{context}: {pair_id} nested pair ID mismatch")
        validate_consumer_contract(source, f"{context}.{pair_id}.source")
        validate_consumer_contract(candidate, f"{context}.{pair_id}.candidate")
        expected_candidate = copy.deepcopy(source)
        source_path = "%2Fhome%2Ftest%2Fcode%2Finfra%2Fbin%2Fsrvls"
        candidate_path = "%2Fhome%2Ftest%2F.local%2Fbin%2Fsrvls"
        fragment = expected_candidate["service"]["fragment"]
        replacement_count = fragment["fragment_content"].count(source_path)
        fragment["fragment_content"] = fragment["fragment_content"].replace(
            source_path, candidate_path
        )
        for command in expected_candidate["service"]["exec_start"]:
            replacement_count += command["binary_path"].count(source_path)
            command["binary_path"] = command["binary_path"].replace(
                source_path, candidate_path
            )
            for index, argument in enumerate(command["argv"]):
                replacement_count += argument.count(source_path)
                command["argv"][index] = argument.replace(source_path, candidate_path)
        if replacement_count != 2:
            fail(f"{context}: {pair_id} source does not expose exactly two path rewrites")
        fragment_bytes = decoded_canonical_content(
            fragment["fragment_content"], f"{context}.{pair_id}.expected_candidate"
        )
        fragment["fragment_size_bytes"] = len(fragment_bytes)
        fragment["fragment_sha256"] = hashlib.sha256(fragment_bytes).hexdigest()
        expected_candidate["contract_hash"] = digest(
            "srvls-managed-consumer-unit-contract-v1",
            without(expected_candidate, "contract_hash"),
        )
        if candidate != expected_candidate:
            fail(
                f"{context}: {pair_id} candidate differs from the exact path-only transformation"
            )
        if source["contract_hash"] == candidate["contract_hash"]:
            fail(f"{context}: {pair_id} source/candidate contracts are not byte-distinct")
        source_content = decoded_canonical_content(
            source["service"]["fragment"]["fragment_content"],
            f"{context}.{pair_id}.source.fragment",
        )
        candidate_content = decoded_canonical_content(
            candidate["service"]["fragment"]["fragment_content"],
            f"{context}.{pair_id}.candidate.fragment",
        )
        if b"/home/test/code/infra/bin/srvls" not in source_content:
            fail(f"{context}: {pair_id} source omits deployed binary path")
        if b"/home/test/.local/bin/srvls" not in candidate_content:
            fail(f"{context}: {pair_id} candidate omits canonical binary path")
        if b"/home/test/code/infra/bin/srvls" in candidate_content:
            fail(f"{context}: {pair_id} candidate retains deployed source path")
        for unit_kind in ("service", "timer"):
            unit = source[unit_kind]
            normalized_fragment = decoded_canonical_content(
                unit["fragment"]["fragment_content"],
                f"{context}.{pair_id}.source.{unit_kind}.fragment",
            )
            host_fragment = normalized_fragment.replace(
                b"/home/test", b"/home/delorenj"
            )
            if b"/home/test" in host_fragment or hashlib.sha256(
                host_fragment
            ).hexdigest() != basis_hashes[unit["unit_name"]]:
                fail(
                    f"{context}: {unit['unit_name']} Host provenance hash "
                    "does not derive from normalized source bytes"
                )
        if pair_id == "metrics" and any(
            token not in source_content or token not in candidate_content
            for token in (b"srvls.prom.tmp", b"&& mv ")
        ):
            fail(f"{context}: metrics pair loses atomic textfile replacement")
        if pair_id == "snapshot" and any(
            token not in source_content or token not in candidate_content
            for token in (b"$(date +%%F)", b"ExecStartPost=", b"git commit")
        ):
            fail(f"{context}: snapshot pair loses date or Git post-action bytes")
        forward.append(
            {
                "pair_id": pair_id,
                "pre_contract_hash": source["contract_hash"],
                "post_contract_hash": candidate["contract_hash"],
            }
        )
        rollback.append(
            {
                "pair_id": pair_id,
                "pre_contract_hash": candidate["contract_hash"],
                "post_contract_hash": source["contract_hash"],
                "reload_contract_hash": source["contract_hash"],
                "validation_contract_hash": source["contract_hash"],
            }
        )
    if value["forward_pair_order"] != pair_ids or value["rollback_pair_order"] != pair_ids:
        fail(f"{context}: pair effect order differs from sorted authority")
    if any(list(row) != BROWNFIELD_FORWARD_KEYS for row in value["forward_evidence"]):
        fail(f"{context}: forward evidence key order mismatch")
    if any(list(row) != BROWNFIELD_ROLLBACK_KEYS for row in value["rollback_evidence"]):
        fail(f"{context}: rollback evidence key order mismatch")
    if value["forward_evidence"] != forward:
        fail(f"{context}: forward evidence does not bind source to candidate")
    if value["rollback_evidence"] != rollback:
        fail(f"{context}: rollback evidence does not bind candidate to source")
    expected_checksum = digest(
        "srvls-brownfield-consumer-pairs-v1", without(value, "checksum")
    )
    if value["checksum"] != expected_checksum:
        fail(f"{context}: brownfield authority checksum mismatch")


def expect_brownfield_rejected(value: dict[str, Any], label: str) -> None:
    try:
        validate_brownfield_consumer_value(value, f"negative oracle {label}")
    except SystemExit:
        return
    fail(f"negative brownfield oracle accepted {label}")


def rehash_brownfield(value: dict[str, Any]) -> None:
    value["checksum"] = digest(
        "srvls-brownfield-consumer-pairs-v1", without(value, "checksum")
    )


def validate_brownfield_consumer_pairs() -> None:
    value = load_exact(ROOT / "brownfield-consumer-pairs.json")
    validate_brownfield_consumer_value(value, "brownfield-consumer-pairs.json")

    missing_snapshot = copy.deepcopy(value)
    missing_snapshot["pairs"] = missing_snapshot["pairs"][:1]
    rehash_brownfield(missing_snapshot)
    expect_brownfield_rejected(missing_snapshot, "missing-snapshot-pair")

    swapped_direction = copy.deepcopy(value)
    row = swapped_direction["rollback_evidence"][0]
    row["pre_contract_hash"], row["post_contract_hash"] = (
        row["post_contract_hash"],
        row["pre_contract_hash"],
    )
    rehash_brownfield(swapped_direction)
    expect_brownfield_rejected(swapped_direction, "swapped-rollback-direction")

    same_direction = copy.deepcopy(value)
    row = same_direction["rollback_evidence"][0]
    row["pre_contract_hash"] = row["post_contract_hash"]
    rehash_brownfield(same_direction)
    expect_brownfield_rejected(same_direction, "same-rollback-direction")

    wrong_reload = copy.deepcopy(value)
    wrong_reload["rollback_evidence"][1]["reload_contract_hash"] = (
        wrong_reload["pairs"][1]["candidate"]["contract_hash"]
    )
    rehash_brownfield(wrong_reload)
    expect_brownfield_rejected(wrong_reload, "candidate-reload-hash")

    wrong_validation = copy.deepcopy(value)
    wrong_validation["rollback_evidence"][1]["validation_contract_hash"] = (
        wrong_validation["pairs"][1]["candidate"]["contract_hash"]
    )
    rehash_brownfield(wrong_validation)
    expect_brownfield_rejected(wrong_validation, "candidate-validation-hash")

    wrong_basis_hash = copy.deepcopy(value)
    wrong_basis_hash["source_basis"]["files"][0]["host_fragment_sha256"] = "0" * 64
    rehash_brownfield(wrong_basis_hash)
    expect_brownfield_rejected(wrong_basis_hash, "unbound-source-basis-hash")

    shell_masking = copy.deepcopy(value)
    candidate = shell_masking["pairs"][0]["candidate"]
    fragment = candidate["service"]["fragment"]
    fragment["fragment_content"] = fragment["fragment_content"].replace(
        "%27%0A", "%20%7C%7C%20true%27%0A", 1
    )
    candidate["service"]["exec_start"][0]["argv"][1] += "%20%7C%7C%20true"
    fragment_bytes = decoded_canonical_content(
        fragment["fragment_content"], "negative shell masking fragment"
    )
    fragment["fragment_size_bytes"] = len(fragment_bytes)
    fragment["fragment_sha256"] = hashlib.sha256(fragment_bytes).hexdigest()
    candidate["contract_hash"] = digest(
        "srvls-managed-consumer-unit-contract-v1", without(candidate, "contract_hash")
    )
    source_hash = shell_masking["pairs"][0]["source"]["contract_hash"]
    candidate_hash = candidate["contract_hash"]
    shell_masking["forward_evidence"][0]["post_contract_hash"] = candidate_hash
    rollback = shell_masking["rollback_evidence"][0]
    rollback.update(
        {
            "pre_contract_hash": candidate_hash,
            "post_contract_hash": source_hash,
            "reload_contract_hash": source_hash,
            "validation_contract_hash": source_hash,
        }
    )
    rehash_brownfield(shell_masking)
    expect_brownfield_rejected(shell_masking, "rehashed-shell-failure-masking")


def validate_toolchain_value(value: dict[str, Any], context: str) -> None:
    if list(value) != TOOLCHAIN_KEYS:
        fail(f"{context}: toolchain evidence key order mismatch")
    if value["schema_version"] != "srvls-stable-toolchain-evidence-v1":
        fail(f"{context}: toolchain evidence schema mismatch")
    expected_authority = {
        "manifest_url": "https://static.rust-lang.org/dist/channel-rust-stable.toml",
        "manifest_date": "2026-07-16",
        "manifest_rust_release": "1.97.1 (8bab26f4f 2026-07-14)",
        "manifest_git_commit_hash": "8bab26f4f68e0e26f0bb7960be334d5b520ea452",
        "rustc_component_xz_url": (
            "https://static.rust-lang.org/dist/2026-07-16/"
            "rustc-1.97.1-x86_64-unknown-linux-gnu.tar.xz"
        ),
        "rustc_component_xz_sha256": (
            "9819d0a32d56bd339585319c80260e332779f5541fd66838ab7e016d6c814819"
        ),
    }
    if {key: value[key] for key in expected_authority} != expected_authority:
        fail(f"{context}: official stable manifest/component identity drift")
    require_sha256(
        value["rustc_component_xz_sha256"],
        f"{context}: rustc component archive hash",
    )
    verbose_bytes = decoded_canonical_content(
        value["rustc_version_verbose"], f"{context}.rustc_version_verbose"
    )
    try:
        verbose = verbose_bytes.decode("utf-8")
    except UnicodeDecodeError:
        fail(f"{context}: rustc verbose output is not UTF-8")
    lines = verbose.splitlines()
    if not lines or lines[0] != "rustc 1.97.1 (8bab26f4f 2026-07-14)":
        fail(f"{context}: rustc verbose release line mismatch")
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if ": " not in line:
            fail(f"{context}: malformed rustc verbose field")
        key, field_value = line.split(": ", 1)
        if key in fields:
            fail(f"{context}: duplicate rustc verbose field")
        fields[key] = field_value
    expected_fields = {
        "binary": "rustc",
        "commit-hash": "8bab26f4f68e0e26f0bb7960be334d5b520ea452",
        "commit-date": "2026-07-14",
        "host": "x86_64-unknown-linux-gnu",
        "release": "1.97.1",
        "LLVM version": "22.1.6",
    }
    if fields != expected_fields:
        fail(f"{context}: complete rustc verbose fields mismatch")
    parsed = value["parsed"]
    if list(parsed) != TOOLCHAIN_PARSED_KEYS or parsed != {
        "release": fields["release"],
        "commit_hash": fields["commit-hash"],
        "commit_date": fields["commit-date"],
        "host": fields["host"],
        "llvm_version": fields["LLVM version"],
    }:
        fail(f"{context}: parsed compiler identity differs from verbose output")
    if parsed["release"] not in value["manifest_rust_release"]:
        fail(f"{context}: compiler release differs from manifest")
    if parsed["commit_hash"] != value["manifest_git_commit_hash"]:
        fail(f"{context}: compiler commit differs from manifest")
    if value["checksum"] != digest(
        "srvls-stable-toolchain-evidence-v1", without(value, "checksum")
    ):
        fail(f"{context}: toolchain evidence checksum mismatch")


def expect_toolchain_rejected(value: dict[str, Any], label: str) -> None:
    try:
        validate_toolchain_value(value, f"negative oracle {label}")
    except SystemExit:
        return
    fail(f"negative toolchain oracle accepted {label}")


def rehash_toolchain(value: dict[str, Any]) -> None:
    value["checksum"] = digest(
        "srvls-stable-toolchain-evidence-v1", without(value, "checksum")
    )


def validate_stable_toolchain_evidence() -> None:
    value = load_exact(ROOT / "stable-toolchain-evidence.json")
    validate_toolchain_value(value, "stable-toolchain-evidence.json")

    stale_manifest = copy.deepcopy(value)
    stale_manifest["manifest_rust_release"] = "1.97.0 (deadbeef0 2026-06-01)"
    rehash_toolchain(stale_manifest)
    expect_toolchain_rejected(stale_manifest, "stale-manifest-release")

    mismatched_parsed_commit = copy.deepcopy(value)
    mismatched_parsed_commit["parsed"]["commit_hash"] = "0" * 40
    rehash_toolchain(mismatched_parsed_commit)
    expect_toolchain_rejected(mismatched_parsed_commit, "parsed-commit-mismatch")

    wrong_component_hash = copy.deepcopy(value)
    wrong_component_hash["rustc_component_xz_sha256"] = "0" * 64
    rehash_toolchain(wrong_component_hash)
    expect_toolchain_rejected(wrong_component_hash, "component-hash-mismatch")


def validate_standalone_authorities() -> None:
    validate_admission(load_exact(ROOT / "admission-ready.json"), ROOT / "admission-ready.json", "ready")
    validate_admission(
        load_exact(ROOT / "admission-recovering.json"),
        ROOT / "admission-recovering.json",
        "recovering",
    )
    validate_known_good(
        load_exact(ROOT / "known-good-first-install.json"),
        ROOT / "known-good-first-install.json",
        "first-install-absent",
    )
    validate_known_good(
        load_exact(ROOT / "known-good-installed.json"),
        ROOT / "known-good-installed.json",
        "installed",
    )
    validate_fd4_envelopes()
    validate_brownfield_consumer_pairs()
    validate_stable_toolchain_evidence()


def validate_systemd_job_recovery_trace() -> None:
    value = load_exact(ROOT / "systemd-job-recovery.trace.json")
    if list(value) != ["schema_version", "pending_job", "events", "restart_on", "result"]:
        fail("systemd job recovery trace key order mismatch")
    if value["schema_version"] != "srvls-systemd-job-recovery-trace-v1":
        fail("systemd job recovery trace schema mismatch")
    job = value["pending_job"]
    if list(job) != [
        "schema_version",
        "unit_name",
        "method",
        "intended_target_state",
        "recovery_attempt_id",
        "effect_attempt",
    ] or job["schema_version"] != "srvls-pending-systemd-job-v1":
        fail("pending systemd job schema mismatch")
    if (
        job["unit_name"] != "srvls-metrics.timer"
        or job["method"] != "StartUnit"
        or job["intended_target_state"] != "active"
        or job["recovery_attempt_id"] != "00000000-0000-7000-8000-000000000010"
        or job["effect_attempt"] != 0
    ):
        fail("pending systemd job authority drift")
    if value["events"] != [
        "old-owner-disappeared",
        "fresh-connection-established",
        "name-owner-match-installed",
        "manager-owner-bound",
        "job-property-matches-installed",
        "manager-subscribe-success",
        "manager-owner-rechecked",
        "manager-roundtrip-complete",
        "listjobs-observed",
        "jobremoved-drained",
        "manager-roundtrip-complete",
        "listjobs-empty",
        "loaded-readback-stable",
        "retry-eligible",
    ]:
        fail("systemd recovery barrier order drift")
    if value["restart_on"] != [
        "bus-disconnect",
        "manager-owner-change",
        "new-matching-job",
        "unstable-loaded-readback",
    ] or value["result"] != "barrier-complete":
        fail("systemd recovery restart/final truth drift")


def cleanup_process(pid: int | None) -> None:
    if pid is None:
        return
    try:
        os.kill(pid, signal.SIGKILL)
    except ProcessLookupError:
        return


def prove_negative_action_handoff() -> None:
    lock_fd = create_memfd("srvls-negative-action-lock")
    admission_fd = create_memfd("srvls-negative-admission", b"7\n")
    marker_fd = create_memfd("srvls-negative-marker")
    pid_read, pid_write = os.pipe2(os.O_CLOEXEC)
    result_read, result_write = os.pipe2(os.O_CLOEXEC)
    submitter = os.fork()
    executor: int | None = None
    if submitter == 0:
        try:
            os.close(pid_read)
            os.close(result_read)
            submitter_fd = os.dup(lock_fd)
            os.close(lock_fd)
            lock_call(submitter_fd, fcntl.F_SETLK, fcntl.F_RDLCK)
            child = os.fork()
            if child == 0:
                # The stop is deliberately the executor's first syscall.
                os.kill(os.getpid(), signal.SIGSTOP)
                os.close(pid_write)
                executor_fd = os.dup(submitter_fd)
                os.close(submitter_fd)
                lock_call(executor_fd, fcntl.F_SETLK, fcntl.F_RDLCK)
                generation = read_memfd(admission_fd)
                if generation != b"7\n":
                    os.write(result_write, b"REFUSED\n")
                else:
                    write_memfd(marker_fd, b"mutated\n")
                    os.write(result_write, b"MUTATED\n")
                lock_call(executor_fd, fcntl.F_SETLK, fcntl.F_UNLCK)
                os.close(executor_fd)
                os._exit(0)
            os.write(pid_write, f"{child}\n".encode("ascii"))
            while True:
                signal.pause()
        except BaseException:
            os._exit(111)
    try:
        os.close(pid_write)
        os.close(result_write)
        executor = int(read_pipe_line(pid_read, 5.0))
        os.close(pid_read)
        deadline = time.monotonic() + 5.0
        while process_state(executor) not in {"T", "t"}:
            if time.monotonic() >= deadline:
                fail("negative handoff executor did not stop before lease acquisition")
            time.sleep(0.01)
        os.kill(submitter, signal.SIGKILL)
        os.waitpid(submitter, 0)
        submitter = -1
        release_fd = os.dup(lock_fd)
        lock_call(release_fd, fcntl.F_SETLK, fcntl.F_WRLCK)
        write_memfd(admission_fd, b"8\n")
        lock_call(release_fd, fcntl.F_SETLK, fcntl.F_UNLCK)
        os.close(release_fd)
        os.kill(executor, signal.SIGCONT)
        result = read_pipe_line(result_read, 5.0)
        os.close(result_read)
        if result != b"REFUSED" or read_memfd(marker_fd):
            fail("late action executor mutated after admission generation changed")
    finally:
        if submitter > 0:
            cleanup_process(submitter)
            try:
                os.waitpid(submitter, 0)
            except ChildProcessError:
                pass
        cleanup_process(executor)
        for fd in (lock_fd, admission_fd, marker_fd):
            os.close(fd)


def prove_positive_action_handoff() -> None:
    lock_fd = create_memfd("srvls-positive-action-lock")
    admission_fd = create_memfd("srvls-positive-admission", b"8\n")
    marker_fd = create_memfd("srvls-positive-marker")
    pid_read, pid_write = os.pipe2(os.O_CLOEXEC)
    ack_read, ack_write = os.pipe2(os.O_CLOEXEC)
    go_read, go_write = os.pipe2(os.O_CLOEXEC)
    done_read, done_write = os.pipe2(os.O_CLOEXEC)
    submitter = os.fork()
    executor: int | None = None
    if submitter == 0:
        try:
            for fd in (pid_read, ack_read, go_write, done_read):
                os.close(fd)
            submitter_fd = os.dup(lock_fd)
            os.close(lock_fd)
            lock_call(submitter_fd, fcntl.F_SETLK, fcntl.F_RDLCK)
            child = os.fork()
            if child == 0:
                os.close(pid_write)
                executor_fd = os.dup(submitter_fd)
                os.close(submitter_fd)
                lock_call(executor_fd, fcntl.F_SETLK, fcntl.F_RDLCK)
                if read_memfd(admission_fd) != b"8\n":
                    os.write(ack_write, b"BAD-GENERATION\n")
                    os._exit(112)
                os.write(ack_write, b"ACK\n")
                if read_pipe_line(go_read, 5.0) != b"GO":
                    os._exit(113)
                write_memfd(marker_fd, b"mutated\n")
                if read_memfd(marker_fd) != b"mutated\n":
                    os._exit(114)
                lock_call(executor_fd, fcntl.F_SETLK, fcntl.F_UNLCK)
                os.close(executor_fd)
                os.write(done_write, b"DONE\n")
                os._exit(0)
            os.write(pid_write, f"{child}\n".encode("ascii"))
            while True:
                signal.pause()
        except BaseException:
            os._exit(111)
    release_fd: int | None = None
    try:
        for fd in (pid_write, ack_write, go_read, done_write):
            os.close(fd)
        executor = int(read_pipe_line(pid_read, 5.0))
        os.close(pid_read)
        if read_pipe_line(ack_read, 5.0) != b"ACK":
            fail("positive handoff lacks executor acknowledgement")
        os.close(ack_read)
        os.kill(submitter, signal.SIGKILL)
        os.waitpid(submitter, 0)
        submitter = -1
        release_fd = os.dup(lock_fd)
        try:
            lock_call(release_fd, fcntl.F_SETLK, fcntl.F_WRLCK)
        except OSError as exc:
            if exc.errno not in {errno.EACCES, errno.EAGAIN}:
                raise
        else:
            fail("exclusive release was admitted while ActionExecutor held its lease")
        os.write(go_write, b"GO\n")
        os.close(go_write)
        if read_pipe_line(done_read, 5.0) != b"DONE":
            fail("positive handoff did not complete mutation and readback")
        os.close(done_read)
        lock_call(release_fd, fcntl.F_SETLK, fcntl.F_WRLCK)
        if read_memfd(marker_fd) != b"mutated\n":
            fail("positive handoff marker readback differs")
        lock_call(release_fd, fcntl.F_SETLK, fcntl.F_UNLCK)
    finally:
        if release_fd is not None:
            os.close(release_fd)
        if submitter > 0:
            cleanup_process(submitter)
            try:
                os.waitpid(submitter, 0)
            except ChildProcessError:
                pass
        cleanup_process(executor)
        for fd in (lock_fd, admission_fd, marker_fd):
            os.close(fd)


def validate_action_executor_handoff() -> None:
    value = load_exact(ROOT / "action-executor-handoff.trace.json")
    if list(value) != ["schema_version", "negative", "positive"]:
        fail("ActionExecutor handoff trace key order mismatch")
    if value["schema_version"] != "srvls-action-executor-handoff-trace-v1":
        fail("ActionExecutor handoff trace schema mismatch")
    negative = value["negative"]
    if (
        negative["authorized_generation"] != 7
        or negative["published_generation"] != 8
        or negative["executor_stopped_before_lease"] is not True
        or negative["submitter_killed"] is not True
        or negative["executor_revalidated_generation"] is not True
        or negative["marker_mutated"] is not False
        or negative["result"] != "generation-changed-before-mutation"
    ):
        fail("ActionExecutor negative handoff trace drift")
    positive = value["positive"]
    acknowledgement = positive["acknowledgement"]
    if list(acknowledgement) != [
        "schema_version",
        "operation_id",
        "install_generation",
        "lock_device",
        "lock_inode",
        "executor_pid",
        "executor_process_start_ticks",
        "executable_device",
        "executable_inode",
        "status",
    ] or acknowledgement != {
        "schema_version": "srvls-action-executor-handoff-v1",
        "operation_id": "00000000-0000-7000-8000-000000000800",
        "install_generation": 8,
        "lock_device": 2049,
        "lock_inode": 9001,
        "executor_pid": 5100,
        "executor_process_start_ticks": 123456,
        "executable_device": 2049,
        "executable_inode": 9100,
        "status": "acknowledged",
    }:
        fail("ActionExecutor acknowledgement schema drift")
    if not all(
        positive[key] is True
        for key in (
            "executor_acknowledged",
            "submitter_killed",
            "exclusive_blocked_while_executor_held",
            "marker_mutated",
            "readback_equal",
            "exclusive_acquired_after_executor_release",
        )
    ) or positive["authorized_generation"] != 8:
        fail("ActionExecutor positive handoff trace drift")
    if not sys.platform.startswith("linux") or not Path("/proc/self").exists():
        fail("ActionExecutor handoff proof requires Linux with procfs")
    prove_negative_action_handoff()
    prove_positive_action_handoff()


def validate_file_hashes() -> None:
    sums = ROOT / "SHA256SUMS"
    listed: list[str] = []
    for line in sums.read_text(encoding="ascii").splitlines():
        try:
            expected, name = line.split("  ", 1)
        except ValueError:
            fail("SHA256SUMS has a malformed row")
        require_sha256(expected, f"SHA256SUMS:{name}")
        if name == "SHA256SUMS" or "/" in name or name.startswith("."):
            fail(f"SHA256SUMS has an invalid inventory entry {name!r}")
        listed.append(name)
        candidate = ROOT / name
        if candidate.is_symlink() or not candidate.is_file():
            fail(f"SHA256SUMS entry is not a regular file: {name}")
        actual = hashlib.sha256(candidate.read_bytes()).hexdigest()
        if actual != expected:
            fail(f"SHA256SUMS mismatch for {name}")
    if listed != sorted(listed) or len(listed) != len(set(listed)):
        fail("SHA256SUMS inventory is not sorted and unique")
    expected_files = sorted(
        path.name
        for path in ROOT.iterdir()
        if path.is_file() and path.name != "SHA256SUMS"
    )
    if listed != expected_files:
        fail("SHA256SUMS file inventory mismatch")


def validate_architecture_binding() -> None:
    raw = ARCHITECTURE_SPINE.read_bytes()
    delimiter = b"\n---\n"
    if not raw.startswith(b"---\n") or raw.count(delimiter) != 1:
        fail("architecture frontmatter delimiter is not unique")
    body = raw.split(delimiter, 1)[1]
    actual = hashlib.sha256(body).hexdigest()
    if actual != EXPECTED_ARCHITECTURE_BODY_SHA256:
        fail("current normative architecture body differs from release provenance")
    provenance = (ROOT / "PROVENANCE.md").read_text(encoding="utf-8")
    if provenance.count(EXPECTED_ARCHITECTURE_BODY_SHA256) != 1:
        fail("release provenance does not name the exact architecture-body digest")


def main() -> None:
    validate_negative_vectors()
    validate_architecture_binding()
    actual_manifests = {path.name for path in ROOT.glob("*.manifest.json")}
    if actual_manifests != set(CASES):
        fail("release manifest inventory does not match the declared frozen cuts")
    for name, expected in CASES.items():
        validate_manifest(ROOT / name, expected)
    validate_first_install_multi_pair_positive()
    rollback_cut = load_exact(ROOT / "explicit-rollback-ready-admission-pending.manifest.json")
    validate_explicit_rollback_negative_oracles(rollback_cut["payload"])
    validate_transition_chains()
    validate_standalone_authorities()
    unavailable = load_exact(ROOT / "rollback-unavailable.result.json")
    if unavailable != {"kind": "rollback-unavailable", "reason": "no-prior-release"}:
        fail("rollback-unavailable result drift")
    validate_lock_trace()
    validate_action_executor_handoff()
    validate_dbus_trace()
    validate_systemd_job_recovery_trace()
    validate_file_hashes()
    print(
        "release oracle validation: PASS "
        f"({len(CASES)} crash cuts, {len(TRANSITION_FILES)} complete chains, "
        "15 standalone authorities, 4 traces, 1 result, "
        "2 live Linux lock modes, 2 live ActionExecutor handoff modes, "
        "1 positive two-pair FirstInstall proof, "
        "5 rollback direction mutations, 12 FD4 scalar/binding mutations, "
        "22 checksum-resealed release semantic mutations, "
        "7 brownfield-pair mutations, 3 toolchain mutations, "
        "25 CanonicalJsonV1, 1 key-order, and 11 percent/path mutations)"
    )


if __name__ == "__main__":
    main()
