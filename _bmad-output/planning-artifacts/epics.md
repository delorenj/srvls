---
type: canonical-epics
status: remediated-draft
assignable: false
implementationAuthority: false
remediationBatch: batch-1
inputDocuments:
  - _bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md
  - _bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/addendum.md
  - _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/DESIGN.md
  - _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md
  - _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md
---

# srvls Canonical Epics and Stories

## Authority, Draft Status, and Path Override

This is the user-directed batch-1 canonical decomposition at
_bmad-output/planning-artifacts/epics.md. It replaces the planning-root
tombstone, explicitly rebutting architecture finding F-01. The override changes
only the artifact path and expected tombstone assertion. The retired archive,
digest, discovery globs, and every runtime architecture contract remain
binding. Until the quarantine validator is separately revised, its only
acceptable failure is planning-root tombstone does not fail closed.

This artifact is a remediated draft, nonassignable, and not implementation
authority. Concrete stories and GWT criteria are review contracts; no story may
be assigned until a later explicit promotion changes both authority fields.
Precedence is final PRD, addendum, final UX spines, final architecture spine
except the path override above, then this artifact.

Exactly seven user-value epics and 73 sequential stories follow. Dependencies
contain only exact earlier Story IDs. Each story retains user value,
Implementation Boundary, Requirement Mapping, Dependencies, Validation
Expectations, Out of Scope, and exactly two concrete GWT acceptance criteria.

## Closed Canonical Contracts

### Contract C-01: Compatibility Lanes and Fixed Goldens

Compatibility has exactly two lanes: inherited byte-exact comparison and one
explicitly typed, versioned approved-deviation replacement assertion. There is
no generic semantic normalizer. stdout, stderr, argv, ordering, escaping, exit,
and side effects remain byte exact outside the named replacement assertion.
Expected bytes are checked-in independent inputs produced by two independent
encoders; the Rust encoder under test may never generate, recapture, normalize,
or bless them.

### Contract C-02: Canonical Bytes and Search

CanonicalJsonV1 uses the architecture's exact key/scalar grammar and contains no
trailing newline. Hashes, fingerprints, manifests, JSONL, FD3, and FD4 use those
newline-free bytes; a presenter adds exactly one line terminator outside the
payload. Search records UTF-8 decode status. Valid UTF-8 uses Unicode 16.0 NFC,
full default case folding, NFC again, and Unicode-scalar substring. Invalid
bytes use lossless uppercase-percent display/query bytes. Locale lowering,
simple folding, NFKC, and lossy decoding are forbidden.

### Contract C-03: Collection Candidate and Snapshot Authority

CollectionCandidateV1 is an immutable non-current staging handoff containing
one admitted CollectionPlanV1, frozen cuts and schedule, eligible immutable
Collector reports, finalized diagnostics, normalized Observations, completeness,
resource evidence, and reconciliation material. It has no current-pointer
authority. Only Story 4.7 creates SnapshotV1 in the complete AD-16 transaction
and moves current by latest_requested_generation CAS. A superseded candidate
may remain attempt evidence but cannot become current. Collector, reducer,
Brief, baseline, and TUI paths never write the pointer.

### Contract C-04: Closed ActionKindV1 and Provider Matrix

ActionKindV1 is the sole closed lowercase wire enum: start, stop, restart,
disable, delete. Unknown casing, aliases, numeric values, signal, kill, remove,
or future values fail before planning. Direct-process signaling is ActionKindV1
stop with exact PID/birth and bounded signal parameters; signal is never a kind.
Menu, ActionPlanV1, SQLite, executor, audit, linear, machine, and fixtures all
consume this enum.

| Target authority | start | stop | restart | disable | delete |
| --- | --- | --- | --- | --- | --- |
| Promise with exact supported Launch Mechanism | yes | no | only when mechanism declares restart | no | no |
| cron Observation | no | no | no | no | no |
| systemd Observation | yes | yes | yes | yes | no |
| Docker Observation | yes | yes | yes | yes | no |
| PM2 Observation | yes | yes | yes | no | yes |
| direct-process Observation | no | yes through exact signal parameters | no | no | no |

Unsupported cells are absent and refused before any Provider launch.

### Contract C-05: Complete Confirmation and Availability Matrix

| First matching condition | Required behavior |
| --- | --- |
| unsupported Provider/action cell | absent; machine submission refused |
| stale Snapshot, incomplete identity, expired plan, or nonterminal target | disabled/refused with refresh or wait guidance |
| Safe-to-stop unsafe | disabled with every reason |
| Safe-to-stop unknown | cancel-first confirmation; exact lowercase resolved verb required |
| safe nondestructive start with no privilege/policy uncertainty | plan shown; Enter may submit without destructive confirmation |
| safe restart | cancel-first normal confirmation because Runtime is interrupted |
| safe stop, disable, or delete | cancel-first normal confirmation; PM2 delete and persistent-scheduler disable labelled destructive |

Cancel is initially focused, Esc cancels, and repeated shortcuts/y-as-confirm do
nothing. Safe-to-stop is recalculated during planning and immediately before
mutation. Baseline b opens baseline-dialog; Esc cancels; incomplete/incompatible
override requires nonempty reason plus exact typed word override; success
changes only baseline/audit and immediately recomputes Evidence Window.

### Contract C-06: Complete Action Outcome Precedence

| Precedence | Outcome | Total rule |
| ---: | --- | --- |
| 1 | verified | fresh OperationId-correlated post-launch evidence proves the exact postcondition regardless of diagnostics |
| 2 | refused | no Provider operation launched because confirmation, capability, authorization, duplicate, saturation, expiry, or immediate identity revalidation failed |
| 3 | timed-out | execution crossed its hard deadline, termination/reaping was attempted, and the postcondition was not verified in the bound |
| 4 | failed | Provider invocation could not start, or fresh evidence disproves the postcondition |
| 5 | executed-unverified | launch occurred but incomplete, unavailable, ambiguous, expired-window, interrupted, or replacement evidence cannot prove/disprove it |

Pre-launch drift is refused/stale-identity. Post-launch replacement is
executed-unverified. Diagnostics never create a sixth outcome.

### Contract C-07: SQLite, Storage, Retention, and Capacity

The database is XDG_STATE_HOME/srvls/state.sqlite3, defaulting to
~/.local/state/srvls/state.sqlite3; directory mode is 0700 and database/WAL/SHM
are 0600. Fresh and existing opens run outside a transaction: set
journal_mode=WAL and require returned wal; each connection reads journal_mode
and requires wal, sets synchronous=FULL and reads numeric 2, sets
foreign_keys=ON and reads 1, then sets the exact ARCH-LIM-14 busy timeout. No
transaction begins after a missing, differently typed, or mismatched readback.
The final spine does not define trusted_schema, application_id, or page-size
policy, so none is invented. Writers use BEGIN IMMEDIATE, deterministic typed-ID
order, CAS, exclusive migration, integrity checks, and typed read-only recovery.

Retention applies both age and count to eligible unpinned records in UTC terminal
time/typed-ID order. Current Snapshot, Accepted Baseline, active truth, and
dependent closure/admitted work are pinned. Physical capacity is the no-symlink
sum of st_blocks times 512 for SQLite, WAL, SHM, retained backups, and upgrade
manifests. After all eligible pruning, pinned excess has one mode: admitted
recovery/finalization may write; new Promises, candidate Snapshots, baseline
changes, and Host mutations are refused; stateless compatibility remains.
Pins are never deleted; archive, vacuum, reset, and alternate degraded modes do
not exist.

### Contract C-08: Exact Architecture Limits

| ID | Built-in default | Inclusive range or invariant |
| --- | --- | --- |
| ARCH-LIM-1 | collection concurrency 4 | 1-8 |
| ARCH-LIM-2 | cron scopes 10 s; systemd scopes 15 s; Docker 30 s; PM2 20 s; process 10 s | each 1-60 s; reserved epoch includes setup through terminal decision |
| ARCH-LIM-3 | scheduler margin 5 s; derived cutoff 40 s | margin 0-30 s; effective max(configured,1 ns); cutoff=makespan+margin |
| ARCH-LIM-4 | child stdout 4 MiB; stderr 256 KiB | stdout 64 KiB-16 MiB; stderr 16 KiB-1 MiB |
| ARCH-LIM-5 | inspect 256 KiB and 200 lines | 4 KiB-2 MiB and 10-2,000; earlier bound wins |
| ARCH-LIM-6 | 14 days and 256 historical Snapshots | 2-90 days and 16-4,096; current/baseline pinned |
| ARCH-LIM-7 | 90 days and 50,000 events/Promise | 30-365 days and 1,000-1,000,000 |
| ARCH-LIM-8 | Lease 12 h; Heartbeat 5 min; grace 5 min | 5 min-30 d; 10 s-1 h; 30 s-30 min; grace never extends Lease |
| ARCH-LIM-9 | stale no-use 24 h | 5 min-30 d; no positive evidence means no label |
| ARCH-LIM-10 | CPU 80%; memory 25%; 3 samples; 2 min | thresholds 1-100%; samples 1-12; window 1 min-1 h |
| ARCH-LIM-11 | systemd 100 s; Docker 45 s; PM2 30 s; process 10 s; Launch 120 s | systemd/Launch 5-600 s; Docker/PM2 5-300 s; process 1-60 s |
| ARCH-LIM-12 | verification 30 s; poll 500 ms | 5-120 s and 100-2,000 ms |
| ARCH-LIM-13 | graceful 2 s; forced observation 1 s | 100 ms-10 s and 100 ms-5 s; no D-state reap guarantee |
| ARCH-LIM-14 | SQLite busy 5 s | 100 ms-30 s; explicit unavailable/refused |
| ARCH-LIM-15 | plan TTL 5 min | 10 s-30 min; generation/identity/policy/expiry requires replan |
| ARCH-LIM-16 | process-scope stdout 8 MiB; stderr 512 KiB | stdout 64 KiB-64 MiB; stderr 16 KiB-4 MiB; at least child cap |
| ARCH-LIM-17 | generation stdout 32 MiB; stderr 2 MiB | stdout 256 KiB-256 MiB; stderr 64 KiB-16 MiB; at least concurrency times child cap |
| ARCH-LIM-18 | Promises 10,000; operations 10,000; events 1,000,000 | 100-100,000; 100-1,000,000; 10,000-10,000,000 |
| ARCH-LIM-19 | state ceiling 512 MiB | 64 MiB-8 GiB; st_blocks times 512 and pins |
| ARCH-LIM-20 | action concurrency 4 | 1-16; separate pool; saturation pre-launch |
| ARCH-LIM-21 | revalidation 5 s | 1-15 s; expiry pre-launch refused |
| ARCH-LIM-22 | finalization attempt 5 s | 1-30 s; remain alive and retry without reexecution |
| ARCH-LIM-23 | systemd 143 s; Docker 88 s; PM2 73 s; process 53 s; Launch 163 s | exact sum of revalidation, execution, verification, graceful, forced observation, one finalization attempt |
| ARCH-LIM-24 | release validation 120 s | 10-600 s; one persisted CLOCK_BOOTTIME cut for all four evidence classes |

The fixed default schedule has epochs 0,15,20,25 s, process gate [25,35),
makespan 35 s, cutoff 40 s. The near-tie reserves epoch 20, makespan 30 s,
cutoff 35 s even at 20 s minus 1 ns. A 60-second process plus seven one-second
scopes has makespan 61 s and zero-margin cutoff 61 s plus 1 ns.

### Contract C-09: Exact FD3 Worker Transport

Use socketpair(AF_UNIX, SOCK_STREAM | SOCK_CLOEXEC, 0), endpoints P0/C0,
SO_PASSCRED on P0, and map only C0 to child FD 3 for
__srvls-worker-v1. The worker proves SO_PEERCRED UID/parent PID and identical
executable device/inode, restores FD_CLOEXEC, and performs no Host work before
one Request. Ready's first byte carries one SCM_CREDENTIALS; the parent proves
owned PID/birth/executable/process group. Descriptor ownership, duplicate
rejection, shutdown/EOF/close, and cleanup are exactly AD-25.

Frames are u32be length plus newline-free CanonicalJsonV1 in exactly:
WorkerHelloV1, WorkerReadyV1, WorkerRequestV1, WorkerResultV1, EOF. Hello/Ready
cap is 4 KiB, Request 32 MiB, Result 16 MiB plus effective scope captures.
Exact key orders are:

- Hello: protocol, kind, request_id, capability,
  dispatch_schedule_fingerprint, worker_id, schedule_origin_boot_ns,
  reservation_epoch_offset_ns, reservation_budget_ns,
  full_budget_makespan_ns, generation_cutoff_offset_ns,
  absolute_scope_deadline_boot_ns, absolute_generation_cutoff_boot_ns,
  expected_worker.
- Ready: protocol, kind, request_id, capability, observed_worker.
- Request: protocol, request_id, capability, mode,
  collection_plan_fingerprint, dispatch_schedule_fingerprint,
  current_repository_revision, generation_id, scope_id,
  scope_assignment_fingerprint, obligation, worker_id,
  schedule_origin_boot_ns, reservation_epoch_offset_ns,
  reservation_budget_ns, full_budget_makespan_ns,
  generation_cutoff_offset_ns, absolute_scope_deadline_boot_ns,
  absolute_generation_cutoff_boot_ns, capture_reservation, self_process_set,
  provider_scope_input.
- Result: protocol, request_id, capability, collection_plan_fingerprint,
  dispatch_schedule_fingerprint, current_repository_revision, generation_id,
  scope_id, scope_assignment_fingerprint, reservation, result,
  diagnostic_candidates, capture_accounting.

Deadline equality is worker-timeout. Strictly-before primary order is:
worker-spawn, request-encode, worker-request-too-large, fd-peer-auth,
worker-result-too-large, frame-invalid, schema-invalid, version-mismatch,
identity-mismatch, capability-mismatch, assignment-mismatch,
worker-protocol-error, worker-internal-error, worker-signal, worker-exit.
WorkerTransportDiagnosticV1 has exactly request_id, worker_subcode, exit_code,
signal, termination_origin, measured_bytes, allowed_bytes. Expired reservations
allocate no RequestId/capability/socket/child/root/reap. Terminal report/candidate
freezes before cleanup; later WorkerReapEvidenceV1 cannot rewrite truth.

### Contract C-10: Action Persistence and Mutation Ownership

ActionPlanV1 has PlanId and no OperationId. Atomic submit revalidates, consumes
the plan by revision CAS, allocates OperationId, and creates planned. The only
durable nonterminal phases are planned, launch-authorized, executing, verifying.
Pre-launch refusal is an outcome, not queued/admitted/running/refused phase. The
bounded action pool exists before admission and is independent of collection.

All Host mutation runs in the lock-owning in-process owner: systemd D-Bus,
Docker socket, PM2 protocol, direct kernel APIs, and release filesystem/SQLite/
D-Bus/timer APIs. CommandRunner is read-only and never runs mutating systemctl.
Submitted work never detaches; the process remains alive until one terminal
outcome is durable, repeating bounded finalization without reexecuting mutation.
Only SIGKILL or fatal synchronous signal is exceptional.

### Contract C-11: Release Types, Locks, Consumers, Commands, and Results

Architecture-native names are ReleaseBinaryArtifactV1, UpgradeTransactionV1,
KnownGoodReleaseV1, FirstInstallAbsentV1, StableToolchainEvidenceV1, and
ManagedConsumerManifestV1; aliases are forbidden. Commands are exactly
srvls release install | upgrade | validate | status | rollback. recover does
not exist. Agent/linear use exact typed argv, deterministic stdout, human
stderr, fixed exits, and no stdin grammar.

ReleaseTerminalResultV1 is exactly pending, committed,
forward-failed-recovered, rolled-back, rollback-unavailable,
upgrade-recovery-required with AD-23 fields/key order. Public terminal output
excludes pending. KnownGood publishes only after durable CommitDecisionV1 and
contains no pointer extensions. Successful explicit rollback publishes the
displaced source pair as future KnownGood.

Admission uses one verified 0600 local-ext-family admission.lock descriptor and
traditional process POSIX record locks only: F_SETLK/F_SETLKW, SEEK_SET,
[0,1), F_RDLCK/F_WRLCK, FD_CLOEXEC proved by F_GETFD. flock, lockf, F_OFD,
reopen, dup, stdio, inherited descriptors, or closing another descriptor for the
inode are forbidden. Shared work drains before exclusive state sampling.

StableToolchainEvidenceV1 binds a freshly fetched official stable 1.97.1
manifest/components/compiler, Cargo.lock, source, and exact artifact hash. A
selected stale 1.97.0 compiler fails before compile. The admitted final artifact
alone gets checksum, readelf glibc-2.42 proof, and smoke.

ManagedConsumerManifestV1 freezes exactly two sorted metrics/snapshot
service/timer pairs before preimages. Migration replaces exactly two canonical
deployed-executable occurrences. Every other fragment, drop-in, shell operator,
timer property, enablement, and scalar is byte-identical; scripts and deviations
are rejected.

FirstInstallAbsentV1 requires exact prior link/version absence and no foreign
displacement, reserves ready generation zero, and freezes link, binary,
state/WAL/SHM, consumer, unit, enablement, and absence authority. Every removal
and readback is crash recoverable. Foreign/symlink replacement is refused without
deletion. Rollback from the sentinel returns byte-identical
rollback-unavailable with zero transaction/event/KnownGood/admission/filesystem/
database/unit/Host mutation.

### Contract C-12: Exact FD4 and One Release Validation Cut

The same-binary __srvls-release-validator-v1 uses AF_UNIX SOCK_STREAM FD 4,
authenticates SO_PEERCRED UID, parent PID, executable device/inode, and active
ReleaseRecoveryAttemptV1 before SQLite. It reuses AD-25 framing, caps request and
result at 1 MiB, returns one result then EOF.

ReleaseValidationRequestV1 key order is protocol, request_id, capability,
transaction_id, recovery_attempt_id, recovery_attempt_sequence,
manifest_revision, manifest_checksum, old_install_generation,
candidate_install_generation, candidate_binary_sha256, database_path,
allowed_database_schema, backup_manifest_hash, absolute_deadline_boot_ns, mode.
ReleaseValidationResultV1 key order is protocol, request_id, capability,
transaction_id, recovery_attempt_id, recovery_attempt_sequence,
manifest_revision, manifest_checksum, candidate_install_generation,
candidate_binary_sha256, result. Validated result keys are kind,
database_schema, integrity_result, read_only_proof_sha256; rejected keys are
kind, code. No consumer, phase, argv, trigger, output, inactive member, or other
extension is legal.

One persisted ARCH-LIM-24 CLOCK_BOOTTIME cut covers loaded-unit readback, timer
causality, terminal service evidence, and FD4. D-Bus order is acknowledged
NameOwnerChanged AddMatch, GetNameOwner, exact job/unit/property matches,
Manager.Subscribe reply, unchanged-owner recheck, queue-drain barrier, baseline,
then trigger. Owner change, sequence gap, wrong unit/job/invocation/timer,
deadline equality, or FD4 mismatch fails the same attempt.

### Contract C-13: Plane, Git, and Telemetry Boundary

Plane owns intended work, state, and scheduling. Git owns code changes and
reviewable history. Telemetry owns events and measurements. References are
display-only: srvls never fetches/mutates them or uses them as runtime identity,
health, reconciliation, ownership, or Safe-to-stop evidence.

### Contract C-14: Eight Brief Questions

1. BQ-1: What Agents created?
2. BQ-2: What changed?
3. BQ-3: What should be running?
4. BQ-4: What is actually running?
5. BQ-5: What is missing?
6. BQ-6: What is unexplained?
7. BQ-7: Which Heartbeats were lost?
8. BQ-8: Which Runtimes are duplicate, stale, abandoned, unmanaged, or hot?

Each row carries completeness, baseline/current IDs, Evidence Window, timezone,
multi-label counts, and exact drill-down IDs.

## Machine-Checkable Coverage Registry

The JSON block is normative. It explicitly distinguishes the 83 non-
accessibility UX IDs, five UX-A11Y IDs, and SR-A11Y-1, and maps every preserved
requirement plus every AD-11 row.

```json
{
  "schema": "srvls-backlog-coverage-v1",
  "canonicalCounts": {
    "epics": 7,
    "stories": 73,
    "functional": 43,
    "nonFunctional": 16,
    "journeys": 6,
    "uxCoreExcludingAccessibility": 83,
    "uxAccessibility": 5,
    "screenReader": 1,
    "architectureDecisions": 25,
    "architectureLimits": 24,
    "hostProfiles": 1,
    "supplementalMetrics": 9,
    "ad11Rows": 68
  },
  "inventory": {
    "functional": [
      "FR-1",
      "FR-2",
      "FR-3",
      "FR-4",
      "FR-5",
      "FR-6",
      "FR-7",
      "FR-8",
      "FR-9",
      "FR-10",
      "FR-11",
      "FR-12",
      "FR-13",
      "FR-14",
      "FR-15",
      "FR-16",
      "FR-17",
      "FR-18",
      "FR-19",
      "FR-20",
      "FR-21",
      "FR-22",
      "FR-23",
      "FR-24",
      "FR-25",
      "FR-26",
      "FR-27",
      "FR-28",
      "FR-29",
      "FR-30",
      "FR-31",
      "FR-32",
      "FR-33",
      "FR-34",
      "FR-35",
      "FR-36",
      "FR-37",
      "FR-38",
      "FR-39",
      "FR-40",
      "FR-41",
      "FR-42",
      "FR-43"
    ],
    "nonFunctional": [
      "NFR-1",
      "NFR-2",
      "NFR-3",
      "NFR-4",
      "NFR-5",
      "NFR-6",
      "NFR-7",
      "NFR-8",
      "NFR-9",
      "NFR-10",
      "NFR-11",
      "NFR-12",
      "NFR-13",
      "NFR-14",
      "NFR-15",
      "NFR-16"
    ],
    "journeys": [
      "UJ-1",
      "UJ-2",
      "UJ-3",
      "UJ-4",
      "UJ-5",
      "UJ-6"
    ],
    "uxCore83": [
      "UX-FND-1",
      "UX-FND-2",
      "UX-FND-3",
      "UX-FND-4",
      "UX-FND-5",
      "UX-FND-6",
      "UX-IA-1",
      "UX-IA-2",
      "UX-IA-3",
      "UX-IA-4",
      "UX-IA-5",
      "UX-IA-6",
      "UX-IA-7",
      "UX-IA-8",
      "UX-IA-9",
      "UX-IA-10",
      "UX-IA-11",
      "UX-IA-12",
      "UX-VT-1",
      "UX-VT-2",
      "UX-VT-3",
      "UX-VT-4",
      "UX-CP-1",
      "UX-CP-2",
      "UX-CP-3",
      "UX-CP-4",
      "UX-CP-5",
      "UX-CP-6",
      "UX-CP-7",
      "UX-CP-8",
      "UX-CP-9",
      "UX-CP-10",
      "UX-CP-11",
      "UX-CP-12",
      "UX-CP-13",
      "UX-CP-14",
      "UX-CP-15",
      "UX-CP-16",
      "UX-ST-1",
      "UX-ST-2",
      "UX-ST-3",
      "UX-ST-4",
      "UX-ST-5",
      "UX-ST-6",
      "UX-ST-7",
      "UX-ST-8",
      "UX-ST-9",
      "UX-ST-10",
      "UX-ST-11",
      "UX-ST-12",
      "UX-ST-13",
      "UX-ST-14",
      "UX-ST-15",
      "UX-ST-16",
      "UX-ST-17",
      "UX-ST-18",
      "UX-ST-19",
      "UX-ST-20",
      "UX-IP-1",
      "UX-IP-2",
      "UX-IP-3",
      "UX-IP-4",
      "UX-IP-5",
      "UX-IP-6",
      "UX-IP-7",
      "UX-IP-8",
      "UX-IP-9",
      "UX-IP-10",
      "UX-IP-11",
      "UX-IP-12",
      "UX-RP-1",
      "UX-RP-2",
      "UX-RP-3",
      "UX-RP-4",
      "UX-RP-5",
      "UX-RP-6",
      "UX-BUD-1",
      "UX-BUD-2",
      "UX-BUD-3",
      "UX-BUD-4",
      "UX-BUD-5",
      "UX-BUD-6",
      "UX-BUD-7"
    ],
    "uxAccessibility5": [
      "UX-A11Y-1",
      "UX-A11Y-2",
      "UX-A11Y-3",
      "UX-A11Y-4",
      "UX-A11Y-5"
    ],
    "screenReader": [
      "SR-A11Y-1"
    ],
    "architecture": [
      "AD-1",
      "AD-2",
      "AD-3",
      "AD-4",
      "AD-5",
      "AD-6",
      "AD-7",
      "AD-8",
      "AD-9",
      "AD-10",
      "AD-11",
      "AD-12",
      "AD-13",
      "AD-14",
      "AD-15",
      "AD-16",
      "AD-17",
      "AD-18",
      "AD-19",
      "AD-20",
      "AD-21",
      "AD-22",
      "AD-23",
      "AD-24",
      "AD-25"
    ],
    "architectureLimits": [
      "ARCH-LIM-1",
      "ARCH-LIM-2",
      "ARCH-LIM-3",
      "ARCH-LIM-4",
      "ARCH-LIM-5",
      "ARCH-LIM-6",
      "ARCH-LIM-7",
      "ARCH-LIM-8",
      "ARCH-LIM-9",
      "ARCH-LIM-10",
      "ARCH-LIM-11",
      "ARCH-LIM-12",
      "ARCH-LIM-13",
      "ARCH-LIM-14",
      "ARCH-LIM-15",
      "ARCH-LIM-16",
      "ARCH-LIM-17",
      "ARCH-LIM-18",
      "ARCH-LIM-19",
      "ARCH-LIM-20",
      "ARCH-LIM-21",
      "ARCH-LIM-22",
      "ARCH-LIM-23",
      "ARCH-LIM-24"
    ],
    "hostProfile": [
      "ARCH-HOST-1"
    ],
    "supplemental": [
      "SM-1",
      "SM-2",
      "SM-3",
      "SM-4",
      "SM-5",
      "SM-6",
      "SM-C1",
      "SM-C2",
      "SM-C3"
    ]
  },
  "storyInventory": [
    "Story 1.1",
    "Story 1.2",
    "Story 1.3",
    "Story 1.4",
    "Story 1.5",
    "Story 1.6",
    "Story 1.7",
    "Story 1.8",
    "Story 1.9",
    "Story 1.10",
    "Story 2.1",
    "Story 2.2",
    "Story 2.3",
    "Story 2.4",
    "Story 2.5",
    "Story 2.6",
    "Story 3.1",
    "Story 3.2",
    "Story 3.3",
    "Story 3.4",
    "Story 3.5",
    "Story 3.6",
    "Story 3.7",
    "Story 3.8",
    "Story 3.9",
    "Story 3.10",
    "Story 3.11",
    "Story 4.1",
    "Story 4.2",
    "Story 4.3",
    "Story 4.4",
    "Story 4.5",
    "Story 4.6",
    "Story 4.7",
    "Story 4.8",
    "Story 4.9",
    "Story 4.10",
    "Story 5.1",
    "Story 5.2",
    "Story 5.3",
    "Story 5.4",
    "Story 5.5",
    "Story 5.6",
    "Story 5.7",
    "Story 5.8",
    "Story 5.9",
    "Story 6.1",
    "Story 6.2",
    "Story 6.3",
    "Story 6.4",
    "Story 6.5",
    "Story 6.6",
    "Story 6.7",
    "Story 6.8",
    "Story 6.9",
    "Story 6.10",
    "Story 6.11",
    "Story 6.12",
    "Story 7.1",
    "Story 7.2",
    "Story 7.3",
    "Story 7.4",
    "Story 7.5",
    "Story 7.6",
    "Story 7.7",
    "Story 7.8",
    "Story 7.9",
    "Story 7.10",
    "Story 7.11",
    "Story 7.12",
    "Story 7.13",
    "Story 7.14",
    "Story 7.15"
  ],
  "coverageByStory": {
    "Story 1.1": [
      "AD-1",
      "AD-11",
      "AD-3",
      "FR-16"
    ],
    "Story 1.2": [
      "FR-16"
    ],
    "Story 1.3": [
      "AD-11",
      "AD-9",
      "FR-16",
      "NFR-14",
      "SM-4",
      "UX-FND-6"
    ],
    "Story 1.4": [
      "AD-11",
      "AD-13",
      "AD-24",
      "FR-16",
      "UX-FND-3"
    ],
    "Story 1.5": [
      "AD-11",
      "AD-19",
      "AD-20",
      "ARCH-LIM-1",
      "ARCH-LIM-10",
      "ARCH-LIM-11",
      "ARCH-LIM-12",
      "ARCH-LIM-13",
      "ARCH-LIM-14",
      "ARCH-LIM-15",
      "ARCH-LIM-16",
      "ARCH-LIM-17",
      "ARCH-LIM-18",
      "ARCH-LIM-19",
      "ARCH-LIM-2",
      "ARCH-LIM-20",
      "ARCH-LIM-21",
      "ARCH-LIM-22",
      "ARCH-LIM-23",
      "ARCH-LIM-24",
      "ARCH-LIM-3",
      "ARCH-LIM-4",
      "ARCH-LIM-5",
      "ARCH-LIM-6",
      "ARCH-LIM-7",
      "ARCH-LIM-8",
      "ARCH-LIM-9",
      "FR-16",
      "NFR-16"
    ],
    "Story 1.6": [
      "AD-11",
      "AD-16",
      "FR-16"
    ],
    "Story 1.7": [
      "AD-11",
      "AD-2",
      "FR-16",
      "NFR-9"
    ],
    "Story 1.8": [
      "AD-11",
      "FR-16",
      "NFR-11"
    ],
    "Story 1.9": [
      "AD-11",
      "FR-16",
      "NFR-4"
    ],
    "Story 1.10": [
      "AD-11",
      "FR-16",
      "NFR-13"
    ],
    "Story 2.1": [
      "AD-11",
      "AD-15",
      "FR-7"
    ],
    "Story 2.2": [
      "AD-11",
      "FR-1",
      "FR-2",
      "FR-7"
    ],
    "Story 2.3": [
      "AD-11",
      "AD-17",
      "FR-3",
      "FR-6",
      "FR-7",
      "NFR-10"
    ],
    "Story 2.4": [
      "FR-4",
      "FR-7"
    ],
    "Story 2.5": [
      "FR-5",
      "FR-7"
    ],
    "Story 2.6": [
      "FR-7",
      "NFR-7",
      "SM-5",
      "UJ-2",
      "UX-IA-10",
      "UX-IP-9"
    ],
    "Story 3.1": [
      "AD-11",
      "AD-21",
      "FR-14"
    ],
    "Story 3.2": [
      "AD-10",
      "AD-11",
      "AD-21",
      "FR-14",
      "NFR-3"
    ],
    "Story 3.3": [
      "AD-11",
      "AD-21",
      "AD-25",
      "FR-14"
    ],
    "Story 3.4": [
      "AD-11",
      "AD-21",
      "FR-14",
      "FR-8"
    ],
    "Story 3.5": [
      "AD-11",
      "AD-21",
      "FR-14",
      "FR-9"
    ],
    "Story 3.6": [
      "AD-11",
      "AD-21",
      "FR-10",
      "FR-14"
    ],
    "Story 3.7": [
      "AD-11",
      "AD-21",
      "FR-11",
      "FR-14"
    ],
    "Story 3.8": [
      "AD-11",
      "AD-21",
      "FR-12",
      "FR-14"
    ],
    "Story 3.9": [
      "AD-11",
      "AD-21",
      "FR-13",
      "FR-14"
    ],
    "Story 3.10": [
      "AD-11",
      "AD-21",
      "FR-14",
      "FR-17",
      "NFR-2",
      "SM-C2",
      "UX-CP-2",
      "UX-FND-4",
      "UX-ST-4",
      "UX-ST-5"
    ],
    "Story 3.11": [
      "AD-21",
      "FR-14",
      "FR-15",
      "UX-CP-7",
      "UX-IA-4",
      "UX-ST-17"
    ],
    "Story 4.1": [
      "AD-11",
      "AD-18",
      "FR-18",
      "FR-26",
      "NFR-1"
    ],
    "Story 4.2": [
      "AD-18",
      "FR-19",
      "FR-20",
      "FR-26",
      "SM-2",
      "UJ-3",
      "UX-FND-2"
    ],
    "Story 4.3": [
      "AD-11",
      "AD-18",
      "FR-21",
      "FR-22",
      "FR-26",
      "SM-C1",
      "UX-CP-14"
    ],
    "Story 4.4": [
      "AD-11",
      "AD-18",
      "FR-23",
      "FR-24",
      "FR-26",
      "UJ-5"
    ],
    "Story 4.5": [
      "AD-18",
      "FR-25",
      "FR-26",
      "SM-C3",
      "UX-FND-5"
    ],
    "Story 4.6": [
      "AD-18",
      "FR-26"
    ],
    "Story 4.7": [
      "AD-11",
      "AD-18",
      "AD-5",
      "FR-26",
      "FR-27"
    ],
    "Story 4.8": [
      "AD-11",
      "AD-18",
      "FR-26",
      "FR-27",
      "UX-CP-12",
      "UX-IA-7",
      "UX-IP-6",
      "UX-ST-16"
    ],
    "Story 4.9": [
      "AD-11",
      "AD-18",
      "FR-26",
      "FR-28",
      "SM-1",
      "UJ-1",
      "UX-CP-1",
      "UX-IA-1"
    ],
    "Story 4.10": [
      "AD-18",
      "AD-4",
      "FR-26",
      "FR-29",
      "UX-CP-4"
    ],
    "Story 5.1": [
      "AD-11",
      "AD-14",
      "AD-7",
      "FR-30",
      "FR-34",
      "NFR-6",
      "UX-FND-1",
      "UX-IP-1",
      "UX-RP-6"
    ],
    "Story 5.2": [
      "FR-34",
      "UX-CP-3",
      "UX-IA-2",
      "UX-RP-1",
      "UX-RP-2",
      "UX-RP-3",
      "UX-RP-4",
      "UX-RP-5"
    ],
    "Story 5.3": [
      "AD-11",
      "AD-8",
      "FR-31",
      "FR-34",
      "UX-A11Y-2",
      "UX-CP-8",
      "UX-IA-11",
      "UX-IA-5",
      "UX-IP-2",
      "UX-IP-3",
      "UX-ST-19",
      "UX-ST-7"
    ],
    "Story 5.4": [
      "FR-32",
      "FR-34",
      "SM-6",
      "UX-CP-5",
      "UX-CP-6",
      "UX-IA-3"
    ],
    "Story 5.5": [
      "AD-11",
      "FR-32",
      "FR-34"
    ],
    "Story 5.6": [
      "FR-34",
      "UX-ST-1",
      "UX-ST-2",
      "UX-ST-3",
      "UX-ST-6"
    ],
    "Story 5.7": [
      "AD-11",
      "FR-33",
      "FR-34",
      "NFR-8",
      "UX-A11Y-1",
      "UX-A11Y-4",
      "UX-A11Y-5",
      "UX-VT-1",
      "UX-VT-2"
    ],
    "Story 5.8": [
      "FR-34",
      "UX-CP-13",
      "UX-IA-12",
      "UX-IA-8",
      "UX-IP-12",
      "UX-ST-18",
      "UX-VT-3",
      "UX-VT-4"
    ],
    "Story 5.9": [
      "AD-11",
      "ARCH-HOST-1",
      "FR-34",
      "UX-BUD-1",
      "UX-BUD-2",
      "UX-BUD-3",
      "UX-BUD-7"
    ],
    "Story 6.1": [
      "AD-11",
      "AD-22",
      "AD-6",
      "FR-36",
      "FR-40"
    ],
    "Story 6.2": [
      "AD-22",
      "FR-35",
      "FR-40",
      "FR-41",
      "UX-CP-9",
      "UX-IA-6",
      "UX-IP-4"
    ],
    "Story 6.3": [
      "AD-11",
      "AD-22",
      "FR-38",
      "FR-40",
      "UX-CP-10",
      "UX-IP-5",
      "UX-ST-20"
    ],
    "Story 6.4": [
      "AD-22",
      "FR-26",
      "FR-37",
      "FR-40",
      "UX-ST-14"
    ],
    "Story 6.5": [
      "AD-11",
      "AD-22",
      "FR-40"
    ],
    "Story 6.6": [
      "AD-11",
      "AD-22",
      "FR-39",
      "FR-40",
      "NFR-12"
    ],
    "Story 6.7": [
      "AD-11",
      "AD-22",
      "FR-40",
      "NFR-5"
    ],
    "Story 6.8": [
      "AD-22",
      "FR-40",
      "UX-CP-11",
      "UX-IP-7",
      "UX-ST-8"
    ],
    "Story 6.9": [
      "AD-11",
      "AD-22",
      "FR-40",
      "SM-3",
      "UJ-4",
      "UX-ST-10",
      "UX-ST-11",
      "UX-ST-12",
      "UX-ST-13",
      "UX-ST-15",
      "UX-ST-9"
    ],
    "Story 6.10": [
      "AD-11",
      "AD-22",
      "FR-40",
      "UX-IP-10"
    ],
    "Story 6.11": [
      "AD-22",
      "FR-40",
      "UX-A11Y-3",
      "UX-CP-15",
      "UX-IP-11"
    ],
    "Story 6.12": [
      "AD-11",
      "AD-22",
      "FR-40",
      "SR-A11Y-1",
      "UX-BUD-4",
      "UX-BUD-5",
      "UX-BUD-6"
    ],
    "Story 7.1": [
      "AD-11",
      "AD-12",
      "FR-42",
      "FR-43",
      "NFR-15"
    ],
    "Story 7.2": [
      "AD-11",
      "AD-23",
      "FR-43"
    ],
    "Story 7.3": [
      "AD-23",
      "FR-43"
    ],
    "Story 7.4": [
      "AD-11",
      "AD-23",
      "FR-43"
    ],
    "Story 7.5": [
      "AD-23",
      "FR-43"
    ],
    "Story 7.6": [
      "AD-23",
      "FR-43"
    ],
    "Story 7.7": [
      "AD-11",
      "AD-23",
      "FR-43"
    ],
    "Story 7.8": [
      "AD-23",
      "FR-43"
    ],
    "Story 7.9": [
      "AD-11",
      "AD-23",
      "FR-43"
    ],
    "Story 7.10": [
      "AD-11",
      "AD-23",
      "FR-43"
    ],
    "Story 7.11": [
      "AD-23",
      "FR-43"
    ],
    "Story 7.12": [
      "AD-11",
      "AD-23",
      "FR-43"
    ],
    "Story 7.13": [
      "AD-23",
      "FR-43"
    ],
    "Story 7.14": [
      "AD-11",
      "AD-23",
      "FR-43"
    ],
    "Story 7.15": [
      "AD-11",
      "AD-23",
      "FR-43",
      "UJ-6",
      "UX-CP-16",
      "UX-IA-9",
      "UX-IP-8"
    ]
  },
  "requirementCoverage": {
    "FR-1": [
      "Story 2.2"
    ],
    "FR-2": [
      "Story 2.2"
    ],
    "FR-3": [
      "Story 2.3"
    ],
    "FR-4": [
      "Story 2.4"
    ],
    "FR-5": [
      "Story 2.5"
    ],
    "FR-6": [
      "Story 2.3"
    ],
    "FR-7": [
      "Story 2.1",
      "Story 2.2",
      "Story 2.3",
      "Story 2.4",
      "Story 2.5",
      "Story 2.6"
    ],
    "FR-8": [
      "Story 3.4"
    ],
    "FR-9": [
      "Story 3.5"
    ],
    "FR-10": [
      "Story 3.6"
    ],
    "FR-11": [
      "Story 3.7"
    ],
    "FR-12": [
      "Story 3.8"
    ],
    "FR-13": [
      "Story 3.9"
    ],
    "FR-14": [
      "Story 3.1",
      "Story 3.2",
      "Story 3.3",
      "Story 3.4",
      "Story 3.5",
      "Story 3.6",
      "Story 3.7",
      "Story 3.8",
      "Story 3.9",
      "Story 3.10",
      "Story 3.11"
    ],
    "FR-15": [
      "Story 3.11"
    ],
    "FR-16": [
      "Story 1.1",
      "Story 1.2",
      "Story 1.3",
      "Story 1.4",
      "Story 1.5",
      "Story 1.6",
      "Story 1.7",
      "Story 1.8",
      "Story 1.9",
      "Story 1.10"
    ],
    "FR-17": [
      "Story 3.10"
    ],
    "FR-18": [
      "Story 4.1"
    ],
    "FR-19": [
      "Story 4.2"
    ],
    "FR-20": [
      "Story 4.2"
    ],
    "FR-21": [
      "Story 4.3"
    ],
    "FR-22": [
      "Story 4.3"
    ],
    "FR-23": [
      "Story 4.4"
    ],
    "FR-24": [
      "Story 4.4"
    ],
    "FR-25": [
      "Story 4.5"
    ],
    "FR-26": [
      "Story 4.1",
      "Story 4.2",
      "Story 4.3",
      "Story 4.4",
      "Story 4.5",
      "Story 4.6",
      "Story 4.7",
      "Story 4.8",
      "Story 4.9",
      "Story 4.10",
      "Story 6.4"
    ],
    "FR-27": [
      "Story 4.7",
      "Story 4.8"
    ],
    "FR-28": [
      "Story 4.9"
    ],
    "FR-29": [
      "Story 4.10"
    ],
    "FR-30": [
      "Story 5.1"
    ],
    "FR-31": [
      "Story 5.3"
    ],
    "FR-32": [
      "Story 5.4",
      "Story 5.5"
    ],
    "FR-33": [
      "Story 5.7"
    ],
    "FR-34": [
      "Story 5.1",
      "Story 5.2",
      "Story 5.3",
      "Story 5.4",
      "Story 5.5",
      "Story 5.6",
      "Story 5.7",
      "Story 5.8",
      "Story 5.9"
    ],
    "FR-35": [
      "Story 6.2"
    ],
    "FR-36": [
      "Story 6.1"
    ],
    "FR-37": [
      "Story 6.4"
    ],
    "FR-38": [
      "Story 6.3"
    ],
    "FR-39": [
      "Story 6.6"
    ],
    "FR-40": [
      "Story 6.1",
      "Story 6.2",
      "Story 6.3",
      "Story 6.4",
      "Story 6.5",
      "Story 6.6",
      "Story 6.7",
      "Story 6.8",
      "Story 6.9",
      "Story 6.10",
      "Story 6.11",
      "Story 6.12"
    ],
    "FR-41": [
      "Story 6.2"
    ],
    "FR-42": [
      "Story 7.1"
    ],
    "FR-43": [
      "Story 7.1",
      "Story 7.2",
      "Story 7.3",
      "Story 7.4",
      "Story 7.5",
      "Story 7.6",
      "Story 7.7",
      "Story 7.8",
      "Story 7.9",
      "Story 7.10",
      "Story 7.11",
      "Story 7.12",
      "Story 7.13",
      "Story 7.14",
      "Story 7.15"
    ],
    "NFR-1": [
      "Story 4.1"
    ],
    "NFR-2": [
      "Story 3.10"
    ],
    "NFR-3": [
      "Story 3.2"
    ],
    "NFR-4": [
      "Story 1.9"
    ],
    "NFR-5": [
      "Story 6.7"
    ],
    "NFR-6": [
      "Story 5.1"
    ],
    "NFR-7": [
      "Story 2.6"
    ],
    "NFR-8": [
      "Story 5.7"
    ],
    "NFR-9": [
      "Story 1.7"
    ],
    "NFR-10": [
      "Story 2.3"
    ],
    "NFR-11": [
      "Story 1.8"
    ],
    "NFR-12": [
      "Story 6.6"
    ],
    "NFR-13": [
      "Story 1.10"
    ],
    "NFR-14": [
      "Story 1.3"
    ],
    "NFR-15": [
      "Story 7.1"
    ],
    "NFR-16": [
      "Story 1.5"
    ],
    "UJ-1": [
      "Story 4.9"
    ],
    "UJ-2": [
      "Story 2.6"
    ],
    "UJ-3": [
      "Story 4.2"
    ],
    "UJ-4": [
      "Story 6.9"
    ],
    "UJ-5": [
      "Story 4.4"
    ],
    "UJ-6": [
      "Story 7.15"
    ],
    "UX-FND-1": [
      "Story 5.1"
    ],
    "UX-FND-2": [
      "Story 4.2"
    ],
    "UX-FND-3": [
      "Story 1.4"
    ],
    "UX-FND-4": [
      "Story 3.10"
    ],
    "UX-FND-5": [
      "Story 4.5"
    ],
    "UX-FND-6": [
      "Story 1.3"
    ],
    "UX-IA-1": [
      "Story 4.9"
    ],
    "UX-IA-2": [
      "Story 5.2"
    ],
    "UX-IA-3": [
      "Story 5.4"
    ],
    "UX-IA-4": [
      "Story 3.11"
    ],
    "UX-IA-5": [
      "Story 5.3"
    ],
    "UX-IA-6": [
      "Story 6.2"
    ],
    "UX-IA-7": [
      "Story 4.8"
    ],
    "UX-IA-8": [
      "Story 5.8"
    ],
    "UX-IA-9": [
      "Story 7.15"
    ],
    "UX-IA-10": [
      "Story 2.6"
    ],
    "UX-IA-11": [
      "Story 5.3"
    ],
    "UX-IA-12": [
      "Story 5.8"
    ],
    "UX-VT-1": [
      "Story 5.7"
    ],
    "UX-VT-2": [
      "Story 5.7"
    ],
    "UX-VT-3": [
      "Story 5.8"
    ],
    "UX-VT-4": [
      "Story 5.8"
    ],
    "UX-CP-1": [
      "Story 4.9"
    ],
    "UX-CP-2": [
      "Story 3.10"
    ],
    "UX-CP-3": [
      "Story 5.2"
    ],
    "UX-CP-4": [
      "Story 4.10"
    ],
    "UX-CP-5": [
      "Story 5.4"
    ],
    "UX-CP-6": [
      "Story 5.4"
    ],
    "UX-CP-7": [
      "Story 3.11"
    ],
    "UX-CP-8": [
      "Story 5.3"
    ],
    "UX-CP-9": [
      "Story 6.2"
    ],
    "UX-CP-10": [
      "Story 6.3"
    ],
    "UX-CP-11": [
      "Story 6.8"
    ],
    "UX-CP-12": [
      "Story 4.8"
    ],
    "UX-CP-13": [
      "Story 5.8"
    ],
    "UX-CP-14": [
      "Story 4.3"
    ],
    "UX-CP-15": [
      "Story 6.11"
    ],
    "UX-CP-16": [
      "Story 7.15"
    ],
    "UX-ST-1": [
      "Story 5.6"
    ],
    "UX-ST-2": [
      "Story 5.6"
    ],
    "UX-ST-3": [
      "Story 5.6"
    ],
    "UX-ST-4": [
      "Story 3.10"
    ],
    "UX-ST-5": [
      "Story 3.10"
    ],
    "UX-ST-6": [
      "Story 5.6"
    ],
    "UX-ST-7": [
      "Story 5.3"
    ],
    "UX-ST-8": [
      "Story 6.8"
    ],
    "UX-ST-9": [
      "Story 6.9"
    ],
    "UX-ST-10": [
      "Story 6.9"
    ],
    "UX-ST-11": [
      "Story 6.9"
    ],
    "UX-ST-12": [
      "Story 6.9"
    ],
    "UX-ST-13": [
      "Story 6.9"
    ],
    "UX-ST-14": [
      "Story 6.4"
    ],
    "UX-ST-15": [
      "Story 6.9"
    ],
    "UX-ST-16": [
      "Story 4.8"
    ],
    "UX-ST-17": [
      "Story 3.11"
    ],
    "UX-ST-18": [
      "Story 5.8"
    ],
    "UX-ST-19": [
      "Story 5.3"
    ],
    "UX-ST-20": [
      "Story 6.3"
    ],
    "UX-IP-1": [
      "Story 5.1"
    ],
    "UX-IP-2": [
      "Story 5.3"
    ],
    "UX-IP-3": [
      "Story 5.3"
    ],
    "UX-IP-4": [
      "Story 6.2"
    ],
    "UX-IP-5": [
      "Story 6.3"
    ],
    "UX-IP-6": [
      "Story 4.8"
    ],
    "UX-IP-7": [
      "Story 6.8"
    ],
    "UX-IP-8": [
      "Story 7.15"
    ],
    "UX-IP-9": [
      "Story 2.6"
    ],
    "UX-IP-10": [
      "Story 6.10"
    ],
    "UX-IP-11": [
      "Story 6.11"
    ],
    "UX-IP-12": [
      "Story 5.8"
    ],
    "UX-RP-1": [
      "Story 5.2"
    ],
    "UX-RP-2": [
      "Story 5.2"
    ],
    "UX-RP-3": [
      "Story 5.2"
    ],
    "UX-RP-4": [
      "Story 5.2"
    ],
    "UX-RP-5": [
      "Story 5.2"
    ],
    "UX-RP-6": [
      "Story 5.1"
    ],
    "UX-BUD-1": [
      "Story 5.9"
    ],
    "UX-BUD-2": [
      "Story 5.9"
    ],
    "UX-BUD-3": [
      "Story 5.9"
    ],
    "UX-BUD-4": [
      "Story 6.12"
    ],
    "UX-BUD-5": [
      "Story 6.12"
    ],
    "UX-BUD-6": [
      "Story 6.12"
    ],
    "UX-BUD-7": [
      "Story 5.9"
    ],
    "UX-A11Y-1": [
      "Story 5.7"
    ],
    "UX-A11Y-2": [
      "Story 5.3"
    ],
    "UX-A11Y-3": [
      "Story 6.11"
    ],
    "UX-A11Y-4": [
      "Story 5.7"
    ],
    "UX-A11Y-5": [
      "Story 5.7"
    ],
    "SR-A11Y-1": [
      "Story 6.12"
    ],
    "AD-1": [
      "Story 1.1"
    ],
    "AD-2": [
      "Story 1.7"
    ],
    "AD-3": [
      "Story 1.1"
    ],
    "AD-4": [
      "Story 4.10"
    ],
    "AD-5": [
      "Story 4.7"
    ],
    "AD-6": [
      "Story 6.1"
    ],
    "AD-7": [
      "Story 5.1"
    ],
    "AD-8": [
      "Story 5.3"
    ],
    "AD-9": [
      "Story 1.3"
    ],
    "AD-10": [
      "Story 3.2"
    ],
    "AD-11": [
      "Story 1.1",
      "Story 1.3",
      "Story 1.4",
      "Story 1.5",
      "Story 1.6",
      "Story 1.7",
      "Story 1.8",
      "Story 1.9",
      "Story 1.10",
      "Story 2.1",
      "Story 2.2",
      "Story 2.3",
      "Story 3.1",
      "Story 3.2",
      "Story 3.3",
      "Story 3.4",
      "Story 3.5",
      "Story 3.6",
      "Story 3.7",
      "Story 3.8",
      "Story 3.9",
      "Story 3.10",
      "Story 4.1",
      "Story 4.3",
      "Story 4.4",
      "Story 4.7",
      "Story 4.8",
      "Story 4.9",
      "Story 5.1",
      "Story 5.3",
      "Story 5.5",
      "Story 5.7",
      "Story 5.9",
      "Story 6.1",
      "Story 6.3",
      "Story 6.5",
      "Story 6.6",
      "Story 6.7",
      "Story 6.9",
      "Story 6.10",
      "Story 6.12",
      "Story 7.1",
      "Story 7.2",
      "Story 7.4",
      "Story 7.7",
      "Story 7.9",
      "Story 7.10",
      "Story 7.12",
      "Story 7.14",
      "Story 7.15"
    ],
    "AD-12": [
      "Story 7.1"
    ],
    "AD-13": [
      "Story 1.4"
    ],
    "AD-14": [
      "Story 5.1"
    ],
    "AD-15": [
      "Story 2.1"
    ],
    "AD-16": [
      "Story 1.6"
    ],
    "AD-17": [
      "Story 2.3"
    ],
    "AD-18": [
      "Story 4.1",
      "Story 4.2",
      "Story 4.3",
      "Story 4.4",
      "Story 4.5",
      "Story 4.6",
      "Story 4.7",
      "Story 4.8",
      "Story 4.9",
      "Story 4.10"
    ],
    "AD-19": [
      "Story 1.5"
    ],
    "AD-20": [
      "Story 1.5"
    ],
    "AD-21": [
      "Story 3.1",
      "Story 3.2",
      "Story 3.3",
      "Story 3.4",
      "Story 3.5",
      "Story 3.6",
      "Story 3.7",
      "Story 3.8",
      "Story 3.9",
      "Story 3.10",
      "Story 3.11"
    ],
    "AD-22": [
      "Story 6.1",
      "Story 6.2",
      "Story 6.3",
      "Story 6.4",
      "Story 6.5",
      "Story 6.6",
      "Story 6.7",
      "Story 6.8",
      "Story 6.9",
      "Story 6.10",
      "Story 6.11",
      "Story 6.12"
    ],
    "AD-23": [
      "Story 7.2",
      "Story 7.3",
      "Story 7.4",
      "Story 7.5",
      "Story 7.6",
      "Story 7.7",
      "Story 7.8",
      "Story 7.9",
      "Story 7.10",
      "Story 7.11",
      "Story 7.12",
      "Story 7.13",
      "Story 7.14",
      "Story 7.15"
    ],
    "AD-24": [
      "Story 1.4"
    ],
    "AD-25": [
      "Story 3.3"
    ],
    "ARCH-LIM-1": [
      "Story 1.5"
    ],
    "ARCH-LIM-2": [
      "Story 1.5"
    ],
    "ARCH-LIM-3": [
      "Story 1.5"
    ],
    "ARCH-LIM-4": [
      "Story 1.5"
    ],
    "ARCH-LIM-5": [
      "Story 1.5"
    ],
    "ARCH-LIM-6": [
      "Story 1.5"
    ],
    "ARCH-LIM-7": [
      "Story 1.5"
    ],
    "ARCH-LIM-8": [
      "Story 1.5"
    ],
    "ARCH-LIM-9": [
      "Story 1.5"
    ],
    "ARCH-LIM-10": [
      "Story 1.5"
    ],
    "ARCH-LIM-11": [
      "Story 1.5"
    ],
    "ARCH-LIM-12": [
      "Story 1.5"
    ],
    "ARCH-LIM-13": [
      "Story 1.5"
    ],
    "ARCH-LIM-14": [
      "Story 1.5"
    ],
    "ARCH-LIM-15": [
      "Story 1.5"
    ],
    "ARCH-LIM-16": [
      "Story 1.5"
    ],
    "ARCH-LIM-17": [
      "Story 1.5"
    ],
    "ARCH-LIM-18": [
      "Story 1.5"
    ],
    "ARCH-LIM-19": [
      "Story 1.5"
    ],
    "ARCH-LIM-20": [
      "Story 1.5"
    ],
    "ARCH-LIM-21": [
      "Story 1.5"
    ],
    "ARCH-LIM-22": [
      "Story 1.5"
    ],
    "ARCH-LIM-23": [
      "Story 1.5"
    ],
    "ARCH-LIM-24": [
      "Story 1.5"
    ],
    "ARCH-HOST-1": [
      "Story 5.9"
    ],
    "SM-1": [
      "Story 4.9"
    ],
    "SM-2": [
      "Story 4.2"
    ],
    "SM-3": [
      "Story 6.9"
    ],
    "SM-4": [
      "Story 1.3"
    ],
    "SM-5": [
      "Story 2.6"
    ],
    "SM-6": [
      "Story 5.4"
    ],
    "SM-C1": [
      "Story 4.3"
    ],
    "SM-C2": [
      "Story 3.10"
    ],
    "SM-C3": [
      "Story 4.5"
    ]
  },
  "ad11Rows": [
    {
      "id": "AD11-CUR-01",
      "owner": "Story 1.3",
      "fixture": "tests/compat/fixtures/cli-matrix.json",
      "assertion": "assert_legacy_cli_matrix",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "current"
    },
    {
      "id": "AD11-CUR-02",
      "owner": "Story 1.3",
      "fixture": "tests/compat/fixtures/output-matrix.json",
      "assertion": "assert_legacy_output_bytes",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "current"
    },
    {
      "id": "AD11-CUR-03",
      "owner": "Story 1.3",
      "fixture": "tests/compat/fixtures/provider-matrix.json",
      "assertion": "assert_legacy_provider_matrix",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "current"
    },
    {
      "id": "AD11-CUR-04",
      "owner": "Story 1.3",
      "fixture": "tests/compat/fixtures/inspect-matrix.json",
      "assertion": "assert_legacy_inspect_matrix",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "current"
    },
    {
      "id": "AD11-CUR-05",
      "owner": "Story 1.3",
      "fixture": "tests/compat/fixtures/action-matrix.json",
      "assertion": "assert_legacy_action_matrix",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "current"
    },
    {
      "id": "AD11-CUR-06",
      "owner": "Story 1.4",
      "fixture": "tests/fixtures/contracts/manifest.sha256",
      "assertion": "assert_contract_manifest",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "current"
    },
    {
      "id": "AD11-CUR-07",
      "owner": "Story 1.4",
      "fixture": "tests/fixtures/contracts/policy-snapshot-v1",
      "assertion": "assert_policy_fixed_bytes",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "current"
    },
    {
      "id": "AD11-CUR-08",
      "owner": "Story 3.1",
      "fixture": "tests/fixtures/contracts/collection-plan-v1",
      "assertion": "assert_plan_scope_fixed_bytes",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "current"
    },
    {
      "id": "AD11-CUR-09",
      "owner": "Story 1.4",
      "fixture": "tests/fixtures/contracts/observation-id-v1",
      "assertion": "assert_identity_fixed_bytes",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "current"
    },
    {
      "id": "AD11-CUR-10",
      "owner": "Story 3.1",
      "fixture": "tests/fixtures/contracts/provider-scope-input-v1",
      "assertion": "assert_assignment_fixed_bytes",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "current"
    },
    {
      "id": "AD11-CUR-11",
      "owner": "Story 3.3",
      "fixture": "tests/fixtures/contracts/ipc-v1/complete-exchange",
      "assertion": "assert_fd3_four_frame_bytes",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "current"
    },
    {
      "id": "AD11-CUR-12",
      "owner": "Story 3.3",
      "fixture": "tests/fixtures/contracts/ipc-v1/preallocation-timeout",
      "assertion": "assert_fd3_no_allocation_cut",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "current"
    },
    {
      "id": "AD11-CUR-13",
      "owner": "Story 7.15",
      "fixture": "tests/fixtures/contracts/release-transaction-v1",
      "assertion": "assert_release_oracles",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "current"
    },
    {
      "id": "AD11-FUT-01",
      "owner": "Story 1.1",
      "fixture": "tests/architecture_boundaries.rs",
      "assertion": "assert_dependency_direction_and_owner",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-02",
      "owner": "Story 1.5",
      "fixture": "tests/fixtures/implementation/config-and-limits-v1",
      "assertion": "assert_all_config_limits",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-03",
      "owner": "Story 1.6",
      "fixture": "tests/fixtures/implementation/sqlite-init-v1",
      "assertion": "assert_fresh_existing_sqlite",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-04",
      "owner": "Story 1.7",
      "fixture": "tests/fixtures/implementation/repository-cas-v1",
      "assertion": "assert_atomic_cas_and_unavailable",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-05",
      "owner": "Story 1.8",
      "fixture": "tests/fixtures/implementation/retention-capacity-v1",
      "assertion": "assert_pins_watermarks_capacity",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-06",
      "owner": "Story 1.9",
      "fixture": "tests/fixtures/implementation/command-runner-v1",
      "assertion": "assert_runner_terminal_before_reap",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-07",
      "owner": "Story 2.1",
      "fixture": "tests/fixtures/implementation/principal-authorization-v1",
      "assertion": "assert_principal_owner_auth",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-08",
      "owner": "Story 2.2",
      "fixture": "tests/fixtures/implementation/promise-declare-revise-v1",
      "assertion": "assert_promise_idempotency",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-09",
      "owner": "Story 2.3",
      "fixture": "tests/fixtures/implementation/promise-lease-v1",
      "assertion": "assert_boot_clock_and_persistent_reject",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-10",
      "owner": "Story 3.2",
      "fixture": "tests/fixtures/implementation/dispatch-schedule-v1/default.json",
      "assertion": "assert_default_schedule",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-11",
      "owner": "Story 3.2",
      "fixture": "tests/fixtures/implementation/dispatch-schedule-v1/near-tie.json",
      "assertion": "assert_near_tie_schedule",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-12",
      "owner": "Story 3.2",
      "fixture": "tests/fixtures/implementation/dispatch-schedule-v1/sixty-second.json",
      "assertion": "assert_zero_margin_schedule",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-13",
      "owner": "Story 3.2",
      "fixture": "tests/fixtures/implementation/dispatch-schedule-v1/missed-cut.json",
      "assertion": "assert_no_post_cut_allocation",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-14",
      "owner": "Story 3.3",
      "fixture": "tests/fixtures/implementation/fd3-peer-v1",
      "assertion": "assert_peer_credentials_and_ready",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-15",
      "owner": "Story 3.3",
      "fixture": "tests/fixtures/implementation/fd3-descriptor-v1",
      "assertion": "assert_descriptor_ownership_and_eof",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-16",
      "owner": "Story 3.3",
      "fixture": "tests/fixtures/implementation/fd3-failure-v1",
      "assertion": "assert_total_failure_precedence",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-17",
      "owner": "Story 3.3",
      "fixture": "tests/fixtures/implementation/fd3-reap-v1",
      "assertion": "assert_report_immutable_before_reap",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-18",
      "owner": "Story 3.4",
      "fixture": "tests/fixtures/implementation/provider-cron-v1",
      "assertion": "assert_cron_matrix",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-19",
      "owner": "Story 3.5",
      "fixture": "tests/fixtures/implementation/provider-systemd-v1",
      "assertion": "assert_systemd_matrix",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-20",
      "owner": "Story 3.6",
      "fixture": "tests/fixtures/implementation/provider-docker-v1",
      "assertion": "assert_docker_identity_matrix",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-21",
      "owner": "Story 3.7",
      "fixture": "tests/fixtures/implementation/provider-pm2-v1",
      "assertion": "assert_pm2_identity_matrix",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-22",
      "owner": "Story 3.8",
      "fixture": "tests/fixtures/implementation/provider-process-v1",
      "assertion": "assert_process_suppression_matrix",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-23",
      "owner": "Story 3.9",
      "fixture": "tests/fixtures/implementation/collection-candidate-v1",
      "assertion": "assert_candidate_not_snapshot",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-24",
      "owner": "Story 3.10",
      "fixture": "tests/fixtures/implementation/collection-obligation-v1",
      "assertion": "assert_obligation_strict_matrix",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-25",
      "owner": "Story 4.1",
      "fixture": "tests/fixtures/implementation/reconciliation-correlation-v1",
      "assertion": "assert_correlation_vectors",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-26",
      "owner": "Story 4.3",
      "fixture": "tests/fixtures/implementation/reconciliation-orphan-duplicate-v1",
      "assertion": "assert_duplicate_set_cardinality",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-27",
      "owner": "Story 4.4",
      "fixture": "tests/fixtures/implementation/reconciliation-stale-hot-v1",
      "assertion": "assert_history_cut_races",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-28",
      "owner": "Story 4.7",
      "fixture": "tests/fixtures/implementation/snapshot-materialization-v1",
      "assertion": "assert_snapshot_current_cas",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-29",
      "owner": "Story 4.8",
      "fixture": "tests/fixtures/implementation/baseline-acceptance-v1",
      "assertion": "assert_baseline_races_and_override",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-30",
      "owner": "Story 4.9",
      "fixture": "tests/fixtures/implementation/brief-eight-questions-v1",
      "assertion": "assert_eight_brief_rows",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-31",
      "owner": "Story 5.1",
      "fixture": "tests/fixtures/implementation/presentation-routing-v1",
      "assertion": "assert_route_and_terminal_restore",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-32",
      "owner": "Story 5.3",
      "fixture": "tests/fixtures/implementation/tui-navigation-search-v1",
      "assertion": "assert_unicode_search_and_focus",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-33",
      "owner": "Story 5.5",
      "fixture": "tests/fixtures/implementation/external-boundary-v1",
      "assertion": "assert_plane_git_telemetry_boundary",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-34",
      "owner": "Story 5.7",
      "fixture": "tests/fixtures/implementation/tui-accessibility-v1",
      "assertion": "assert_accessibility_states",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-35",
      "owner": "Story 5.9",
      "fixture": "tests/fixtures/implementation/tui-state-budget-v1",
      "assertion": "assert_host_budgets_and_goldens",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-36",
      "owner": "Story 6.1",
      "fixture": "tests/fixtures/implementation/action-kind-v1",
      "assertion": "assert_action_enum_matrix",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-37",
      "owner": "Story 6.3",
      "fixture": "tests/fixtures/implementation/action-plan-confirmation-v1",
      "assertion": "assert_confirmation_matrix",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-38",
      "owner": "Story 6.5",
      "fixture": "tests/fixtures/implementation/action-pool-v1",
      "assertion": "assert_pool_before_admission",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-39",
      "owner": "Story 6.6",
      "fixture": "tests/fixtures/implementation/action-admission-v1",
      "assertion": "assert_operation_phases_and_ids",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-40",
      "owner": "Story 6.7",
      "fixture": "tests/fixtures/implementation/action-executor-v1",
      "assertion": "assert_in_process_mutation_owner",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-41",
      "owner": "Story 6.9",
      "fixture": "tests/fixtures/implementation/action-outcome-v1",
      "assertion": "assert_action_outcome_precedence",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-42",
      "owner": "Story 6.10",
      "fixture": "tests/fixtures/implementation/action-shutdown-recovery-v1",
      "assertion": "assert_no_detach_finalization",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-43",
      "owner": "Story 6.12",
      "fixture": "tests/fixtures/implementation/action-aggregate-v1",
      "assertion": "assert_sr_a11y_and_action_gate",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-44",
      "owner": "Story 7.1",
      "fixture": "tests/fixtures/contracts/release-transaction-v1/stable-toolchain-evidence.json",
      "assertion": "assert_stable_toolchain_and_abi",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-45",
      "owner": "Story 7.2",
      "fixture": "tests/fixtures/contracts/release-transaction-v1/admission-record-lock.trace.json",
      "assertion": "assert_traditional_posix_locks",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-46",
      "owner": "Story 7.4",
      "fixture": "tests/fixtures/contracts/release-transaction-v1/brownfield-consumer-pairs.json",
      "assertion": "assert_two_pair_consumer_rewrite",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-47",
      "owner": "Story 7.7",
      "fixture": "tests/fixtures/contracts/release-transaction-v1/fd4-request.json",
      "assertion": "assert_fd4_exact_bytes",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-48",
      "owner": "Story 7.7",
      "fixture": "tests/fixtures/contracts/release-transaction-v1/manager-subscription.trace.json",
      "assertion": "assert_dbus_handshake_shared_cut",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-49",
      "owner": "Story 7.9",
      "fixture": "tests/fixtures/contracts/release-transaction-v1/owner-takeover.transitions.jsonl",
      "assertion": "assert_owner_takeover_chronology",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-50",
      "owner": "Story 7.10",
      "fixture": "tests/fixtures/contracts/release-transaction-v1/known-good-publication-pending.manifest.json",
      "assertion": "assert_known_good_publication",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-51",
      "owner": "Story 7.12",
      "fixture": "tests/fixtures/contracts/release-transaction-v1/first-install-recovery.transitions.jsonl",
      "assertion": "assert_first_install_absence_matrix",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-52",
      "owner": "Story 7.14",
      "fixture": "tests/fixtures/contracts/release-transaction-v1/explicit-rollback.transitions.jsonl",
      "assertion": "assert_rollback_displaced_source",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-53",
      "owner": "Story 7.15",
      "fixture": "tests/fixtures/implementation/release-command-surface-v1",
      "assertion": "assert_release_commands_and_results",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-54",
      "owner": "Story 7.15",
      "fixture": "tests/fixtures/implementation/host-smoke-v1",
      "assertion": "assert_exact_artifact_host_smoke",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    },
    {
      "id": "AD11-FUT-55",
      "owner": "Story 7.15",
      "fixture": "tests/fixtures/implementation/service-manager-ci-v1",
      "assertion": "assert_isolated_service_manager_rows",
      "aggregateCommand": "bash tests/validate_architecture_contracts.sh",
      "delivery": "future"
    }
  ]
}
```

## Epics and Stories

## Epic 1: Trust the Rust replacement before it touches Host truth

Operators and maintainers can prove compatibility, configuration, storage, limits, and bounded read-only execution before any Provider or release mutation.

### Story 1.1: Operator-visible architecture preflight

As a srvls Operator or maintainer,
I want operator-visible architecture preflight,
So that forbidden outward dependencies, alternate side-effect owners, and missing release-CI ownership are rejected while the prescribed graph passes.

**Implementation Boundary:** Create the prescribed Rust 2024 crate/module boundaries, private defaults, locked dependencies, and exact architecture-boundary test and aggregate entry points.

**Requirement Mapping:** AD-1, AD-11, AD-3, FR-16.

**Dependencies:** None.

**Validation Expectations:** The owning oracle is tests/architecture_boundaries.rs and cargo test --locked --test architecture_boundaries; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Provider implementations and product behavior.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/architecture_boundaries.rs and cargo test --locked --test architecture_boundaries, **When** the story
   capability is exercised, **Then** forbidden outward dependencies, alternate side-effect owners, and missing release-CI ownership are rejected while the prescribed graph passes, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** a Provider module imports presentation or writes Host state directly, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 1.2: Checked-in inherited behavior inventory

As a srvls Operator or maintainer,
I want checked-in inherited behavior inventory,
So that every inventory row names its source behavior, fixture, oracle, consumer, lane, and versioned additive fields.

**Implementation Boundary:** Freeze every inherited table, flat JSON, Prometheus, Markdown, inspect, executable, ordering, escaping, argv, exit, and explicit-action behavior as source/test inventory.

**Requirement Mapping:** FR-16.

**Dependencies:** Story 1.1.

**Validation Expectations:** The owning oracle is tests/compat/manifest.json and tests/compat/SHA256SUMS; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Implementing the Rust replacement.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/compat/manifest.json and tests/compat/SHA256SUMS, **When** the story
   capability is exercised, **Then** every inherited surface has a source behavior, fixed fixture, independent oracle, live consumer, lane, and version, while any new field is additive only in a new version and leaves inherited bytes unchanged, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** an inherited surface or consumer has no fixed row, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 1.3: Two-lane compatibility oracle

As a srvls Operator or maintainer,
I want two-lane compatibility oracle,
So that the frozen corpus and live smoke compare exact bytes except for a specifically typed deviation row.

**Implementation Boundary:** Implement Contract C-01 with byte-exact replay and only typed approved-deviation replacement assertions.

**Requirement Mapping:** AD-11, AD-9, FR-16, NFR-14, SM-4, UX-FND-6.

**Dependencies:** Story 1.2.

**Validation Expectations:** The owning oracle is tests/compat/validate.sh; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** New canonical product contracts outside inherited compatibility.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/compat/validate.sh, **When** the story
   capability is exercised, **Then** the frozen corpus and live smoke compare exact bytes except for a specifically typed deviation row, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** a generic semantic normalizer, self-captured golden, or unlisted difference is attempted, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 1.4: Canonical encodings and typed identities

As a srvls Operator or maintainer,
I want canonical encodings and typed identities,
So that canonicalJsonV1 remains newline-free, presenters add one terminator, and independent encoders agree on every fixed byte.

**Implementation Boundary:** Implement Contract C-02 and AD-24 canonical JSON, binary identities, fingerprints, ObservationIdV1 variants, and independent fixed goldens.

**Requirement Mapping:** AD-11, AD-13, AD-24, FR-16, UX-FND-3.

**Dependencies:** Story 1.3.

**Validation Expectations:** The owning oracle is tests/fixtures/contracts/validate.py; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Provider collection and presentation layouts.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/contracts/validate.py, **When** the story
   capability is exercised, **Then** CanonicalJsonV1 remains newline-free, presenters add one terminator, and independent encoders agree on every fixed byte, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** an unknown key, wrong order, mutable identity field, self-generated expected byte, or trailing newline appears, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 1.5: Typed configuration and all limits

As a srvls Operator or maintainer,
I want typed configuration and all limits,
So that built-in, system, user, explicit, environment, and CLI values resolve in fixed order with complete provenance and exact derived cuts.

**Implementation Boundary:** Implement AD-19 precedence/provenance and every Contract C-08 default, inclusive range, formula, and visible failure.

**Requirement Mapping:** AD-11, AD-19, AD-20, ARCH-LIM-1, ARCH-LIM-10, ARCH-LIM-11, ARCH-LIM-12, ARCH-LIM-13, ARCH-LIM-14, ARCH-LIM-15, ARCH-LIM-16, ARCH-LIM-17, ARCH-LIM-18, ARCH-LIM-19, ARCH-LIM-2, ARCH-LIM-20, ARCH-LIM-21, ARCH-LIM-22, ARCH-LIM-23, ARCH-LIM-24, ARCH-LIM-3, ARCH-LIM-4, ARCH-LIM-5, ARCH-LIM-6, ARCH-LIM-7, ARCH-LIM-8, ARCH-LIM-9, FR-16, NFR-16.

**Dependencies:** Story 1.4.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/config-and-limits-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Hot reload and Host mutation.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/config-and-limits-v1, **When** the story
   capability is exercised, **Then** built-in, system, user, explicit, environment, and CLI values resolve in fixed order with complete provenance and exact derived cuts, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** an unknown, duplicate, malformed, out-of-range, hidden lower-precedence, or clamped value is supplied, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 1.6: Fail-closed SQLite initialization

As a srvls Operator or maintainer,
I want fail-closed sqlite initialization,
So that fresh and existing databases accept only the exact WAL, synchronous, foreign-key, busy-timeout, schema, and permission contract.

**Implementation Boundary:** Implement Contract C-07 path, modes, pragma sequence/readbacks, BEGIN IMMEDIATE, exclusive migration, and read-only recovery.

**Requirement Mapping:** AD-11, AD-16, FR-16.

**Dependencies:** Story 1.5.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/sqlite-init-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Repositories for later aggregates and release backup.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/sqlite-init-v1, **When** the story
   capability is exercised, **Then** fresh and existing databases accept only the exact WAL, synchronous, foreign-key, busy-timeout, schema, and permission contract, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** a pragma type/value, mode, integrity, migration, or invariant mismatches, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 1.7: Atomic repositories and current-pointer CAS

As a srvls Operator or maintainer,
I want atomic repositories and current-pointer cas,
So that promise, policy, plan, operation, baseline, and Snapshot transactions are atomic and only latest_requested_generation can move current.

**Implementation Boundary:** Implement architecture-native repository ports, revision CAS, deterministic typed-ID order, transaction ownership, and one current-generation gate.

**Requirement Mapping:** AD-11, AD-2, FR-16, NFR-9.

**Dependencies:** Story 1.6.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/repository-cas-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Collection reduction, retention policy, and release manifests.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/repository-cas-v1, **When** the story
   capability is exercised, **Then** Promise, policy, plan, operation, baseline, and Snapshot transactions are atomic and only latest_requested_generation can move current, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** a stale writer, late Collector, or concurrent replacement attempts a newer-truth overwrite, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 1.8: Deterministic retention and capacity mode

As a srvls Operator or maintainer,
I want deterministic retention and capacity mode,
So that eligible unpinned rows prune oldest-first and pinned excess refuses only the canonical new-write classes while admitted finalization continues.

**Implementation Boundary:** Implement only Contract C-07 pinning, age/count pruning, watermarks, physical accounting, and one capacity-exhausted behavior.

**Requirement Mapping:** AD-11, FR-16, NFR-11.

**Dependencies:** Story 1.7.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/retention-capacity-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Command execution and aggregate gates.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/retention-capacity-v1, **When** the story
   capability is exercised, **Then** eligible unpinned rows prune oldest-first and pinned excess refuses only the canonical new-write classes while admitted finalization continues, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** a pin is selected, an archive/vacuum/reset path appears, or alternate degraded admission is chosen, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 1.9: Bounded read-only CommandRunner

As a srvls Operator or maintainer,
I want bounded read-only commandrunner,
So that stdout/stderr drain independently, terminal result freezes at the decision cut, and later reap evidence cannot rewrite it.

**Implementation Boundary:** Implement AD-10 typed argv capture with exact deadlines, caps, process groups, termination, immutable terminal result, and separate pending reaper.

**Requirement Mapping:** AD-11, FR-16, NFR-4.

**Dependencies:** Story 1.8.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/command-runner-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Aggregate gate composition and Host mutations.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/command-runner-v1, **When** the story
   capability is exercised, **Then** stdout/stderr drain independently, terminal result freezes at the decision cut, and later reap evidence cannot rewrite it, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** shell interpolation, mutating Provider use, unbounded capture, sequential drain, or reap-before-result is attempted, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 1.10: Foundation contract gate

As a srvls Operator or maintainer,
I want foundation contract gate,
So that every registry row owned by Epic 1 is discovered and missing, duplicate, stale, or self-generated evidence fails closed.

**Implementation Boundary:** Compose boundary, compatibility, canonical-byte, configuration, limits, SQLite, repository, retention, and CommandRunner rows under the exact aggregate command.

**Requirement Mapping:** AD-11, FR-16, NFR-13.

**Dependencies:** Story 1.9.

**Validation Expectations:** The owning oracle is tests/validate_architecture_contracts.sh; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Implementing later epics or changing quarantine policy.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/validate_architecture_contracts.sh, **When** the story
   capability is exercised, **Then** every registry row owned by Epic 1 is discovered and missing, duplicate, stale, or self-generated evidence fails closed, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** the user override is active or another planning quarantine invariant changes, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

## Epic 2: Let Agents own runtime intent deterministically

Agents can declare, renew, query, and close authenticated Runtime Promises with defensible Lease semantics and retry-safe machine contracts.

### Story 2.1: Authenticated local principal and owner binding

As a srvls Agent,
I want authenticated local principal and owner binding,
So that declare, revise, renew, and close bind actor and owner to verified local credentials with deterministic unauthorized outcomes.

**Implementation Boundary:** Define the local principal, Owner, Durable Ownership, credential proof, impersonation refusal, authorization, and rotation contract before any lifecycle mutation.

**Requirement Mapping:** AD-11, AD-15, FR-7.

**Dependencies:** Story 1.10.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/principal-authorization-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Promise fields and reconciliation.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/principal-authorization-v1, **When** the story
   capability is exercised, **Then** declare, revise, renew, and close bind actor and owner to verified local credentials with deterministic unauthorized outcomes, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** credentials are stale, rotated, mismatched, replayed, or attempt another owner, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 2.2: Declare and revise complete Runtime Promises

As a srvls Agent,
I want declare and revise complete runtime promises,
So that valid declare/revise returns the original PromiseId and Lease on retry while every field error is ordered and machine stable.

**Implementation Boundary:** Persist complete required intent, provenance, revision, event sequence, caller idempotency, and deterministic human/machine results.

**Requirement Mapping:** AD-11, FR-1, FR-2, FR-7.

**Dependencies:** Story 2.1.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/promise-declare-revise-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Heartbeat and close.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/promise-declare-revise-v1, **When** a valid declaration or idempotent retry is submitted, **Then** the human result labels the PromiseId and current Lease state and the CanonicalJsonV1 machine result carries the same typed values while retry preserves the original PromiseId, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** a required field, locator, owner, mechanism, count, or opaque-reference type is invalid, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 2.3: Finite Leases and valid persistence

As a srvls Agent,
I want finite leases and valid persistence,
So that omitted lifetime creates the exact finite Lease and valid persistent intent records its durable authority.

**Implementation Boundary:** Implement CLOCK_BOOTTIME Lease defaults, suspend/boot discontinuity rules, and reject persistent intent lacking both Durable Ownership and inspectable Launch Mechanism.

**Requirement Mapping:** AD-11, AD-17, FR-3, FR-6, FR-7, NFR-10.

**Dependencies:** Story 2.2.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/promise-lease-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Heartbeat transport and UI.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/promise-lease-v1, **When** the story
   capability is exercised, **Then** omitted lifetime creates the exact finite Lease and valid persistent intent records its durable authority, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** invalid persistent intent is submitted or wall rollback would extend ownership, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 2.4: Idempotent Heartbeats

As a srvls Agent,
I want idempotent heartbeats,
So that same actor and idempotency key returns the original renewal without duplicate event and never extends beyond the Lease rule.

**Implementation Boundary:** Renew one owned Promise with caller identity, event sequence, cadence, grace, Lease ceiling, and exact late/unauthorized/malformed/closed/unknown outcomes.

**Requirement Mapping:** FR-4, FR-7.

**Dependencies:** Story 2.3.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/promise-heartbeat-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Promise closure and Agent commands.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/promise-heartbeat-v1, **When** the story
   capability is exercised, **Then** same actor and idempotency key returns the original renewal without duplicate event and never extends beyond the Lease rule, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** Heartbeat arrives after Lease, after close, under another owner, or across invalid boot evidence, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 2.5: Close intent without Host mutation

As a srvls Agent,
I want close intent without host mutation,
So that retry returns the same close result and history preserves one reason, actor, sequence, and prior revision.

**Implementation Boundary:** Append exactly one released, completed, or revoked close event and retain the projection/history without stopping a Runtime.

**Requirement Mapping:** FR-5, FR-7.

**Dependencies:** Story 2.4.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/promise-close-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Automatic cleanup and lifecycle actions.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/promise-close-v1, **When** the story
   capability is exercised, **Then** retry returns the same close result and history preserves one reason, actor, sequence, and prior revision, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** a second reason, unknown Promise, unauthorized actor, or Provider mutation is requested, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 2.6: Exact Agent lifecycle commands

As a srvls Agent,
I want exact agent lifecycle commands,
So that each command and retry maps to one documented result/exit and references the same canonical lifecycle aggregates.

**Implementation Boundary:** Expose typed argv declare, revise, query, renew, close, and validate with deterministic JSON/linear stdout, human stderr, stable framing, exits, and no ambiguous stdin grammar.

**Requirement Mapping:** FR-7, NFR-7, SM-5, UJ-2, UX-IA-10, UX-IP-9.

**Dependencies:** Story 2.5.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/agent-lifecycle-cli-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** TUI and release commands.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/agent-lifecycle-cli-v1, **When** the story
   capability is exercised, **Then** each command and retry maps to one documented result/exit and references the same canonical lifecycle aggregates, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** unknown argv, stdin payload, ANSI/progress on stdout, or an undocumented interactive gate is introduced, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

## Epic 3: See the actual work running on the Host

Operators receive bounded, complete-or-explicitly-incomplete evidence for cron, systemd, Docker, PM2, and direct processes without mixed-time truth.

### Story 3.1: Frozen scope manifest and collection admission

As a srvls Operator or maintainer,
I want frozen scope manifest and collection admission,
So that the plan fingerprint and all cuts are immutable before spawn and no later truth lookup changes obligation or input.

**Implementation Boundary:** Under one BEGIN IMMEDIATE transaction allocate GenerationId, ClockSampleV1, repository revision, Promise/policy/baseline/operation/history/current cuts, ScopeManifestV1, DispatchScheduleV1, and CollectionPlanV1.

**Requirement Mapping:** AD-11, AD-21, FR-14.

**Dependencies:** Story 2.6.

**Validation Expectations:** The owning oracle is tests/fixtures/contracts/collection-plan-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Worker transport and Provider logic.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/contracts/collection-plan-v1, **When** the story
   capability is exercised, **Then** the plan fingerprint and all cuts are immutable before spawn and no later truth lookup changes obligation or input, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** any cut, wall clock, policy, Promise, baseline, operation, history, or current pointer is read after admission, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 3.2: Deterministic DispatchSchedule and reservations

As a srvls Operator or maintainer,
I want deterministic dispatchschedule and reservations,
So that epochs, worker IDs, LPT positions, process gate, makespan, margin, and cutoff match all three exact vectors.

**Implementation Boundary:** Compile Contract C-08 default, near-tie, 60-second, latency, half-open gate, latest-generation, and no-post-cut-allocation rules.

**Requirement Mapping:** AD-10, AD-11, AD-21, FR-14, NFR-3.

**Dependencies:** Story 3.1.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/dispatch-schedule-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** FD3 framing and collection results.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/dispatch-schedule-v1, **When** the story
   capability is exercised, **Then** epochs, worker IDs, LPT positions, process gate, makespan, margin, and cutoff match all three exact vectors, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** a completion timing changes a frozen reservation or equality at a cut allocates work, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 3.3: Authenticated same-binary FD3 exchange

As a srvls Operator or maintainer,
I want authenticated same-binary fd3 exchange,
So that all four frames and exact key orders interoperate and each injected failure selects one total diagnostic without post-cut rewrite.

**Implementation Boundary:** Implement every Contract C-09 descriptor, credential, frame, schema, size, deadline, failure-precedence, EOF, cleanup, and immutable-report rule.

**Requirement Mapping:** AD-11, AD-21, AD-25, FR-14.

**Dependencies:** Story 3.2.

**Validation Expectations:** The owning oracle is tests/fixtures/contracts/ipc-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Provider-specific Host reads.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/contracts/ipc-v1, **When** the story
   capability is exercised, **Then** all four frames and exact key orders interoperate and each injected failure selects one total diagnostic without post-cut rewrite, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** a duplicate FD, replay, wrong credential, size boundary, expired reservation, bare exit, signal, or late reap occurs, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 3.4: Cron scope collection

As a srvls Operator or maintainer,
I want cron scope collection,
So that complete and failed scopes normalize deterministic cron ObservationIdV1 values and never expose a mutation capability.

**Implementation Boundary:** Collect user, root, system, and drop-in cron with exact Schedule, source, principal, command identity, provenance, obligation, and diagnostic contracts.

**Requirement Mapping:** AD-11, AD-21, FR-14, FR-8.

**Dependencies:** Story 3.3.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/provider-cron-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Other Providers and reconciliation.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/provider-cron-v1, **When** the story
   capability is exercised, **Then** complete and failed scopes normalize deterministic cron ObservationIdV1 values and never expose a mutation capability, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** permissions, non-UTF-8 paths, duplicate physical rows, malformed schedules, or partial sources occur, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 3.5: Systemd scope collection

As a srvls Operator or maintainer,
I want systemd scope collection,
So that d-Bus/read-only evidence yields stable unit/timer Observations and scoped failure outcomes.

**Implementation Boundary:** Collect system/user services and timers with exact unit identity, enablement, active/sub states, health, schedule, invocation, scope, and provenance.

**Requirement Mapping:** AD-11, AD-21, FR-14, FR-9.

**Dependencies:** Story 3.4.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/provider-systemd-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Systemd mutation and release validation.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/provider-systemd-v1, **When** the story
   capability is exercised, **Then** D-Bus/read-only evidence yields stable unit/timer Observations and scoped failure outcomes, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** manager ownership changes, unit properties disappear, access denies, or paired timer evidence conflicts, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 3.6: Docker scope collection

As a srvls Operator or maintainer,
I want docker scope collection,
So that restart of the same full container identity preserves ObservationId while runtime evidence changes.

**Implementation Boundary:** Use endpoint/context plus immutable full container ID as Docker ObservationIdV1; creation/start/StartedAt remain observational evidence.

**Requirement Mapping:** AD-11, AD-21, FR-10, FR-14.

**Dependencies:** Story 3.5.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/provider-docker-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Docker actions.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/provider-docker-v1, **When** the story
   capability is exercised, **Then** restart of the same full container identity preserves ObservationId while runtime evidence changes, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** a mutable timestamp, short ID, name, image, PID, or Compose label enters identity, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 3.7: PM2 scope collection

As a srvls Operator or maintainer,
I want pm2 scope collection,
So that pM2 restarts preserve or change identity only according to the exact birth tuple and retain bounded state/restart evidence.

**Implementation Boundary:** Use PM2_HOME, PM2 ID, created_at or pm_uptime birth origin, normalized executable, and NFC name as PM2 ObservationIdV1; OS PID is evidence only.

**Requirement Mapping:** AD-11, AD-21, FR-11, FR-14.

**Dependencies:** Story 3.6.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/provider-pm2-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** PM2 actions.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/provider-pm2-v1, **When** the story
   capability is exercised, **Then** PM2 restarts preserve or change identity only according to the exact birth tuple and retain bounded state/restart evidence, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** OS PID, mutable uptime, display order, or namespace alone becomes identity, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 3.8: Direct-process collection and exact suppression

As a srvls Operator or maintainer,
I want direct-process collection and exact suppression,
So that frozen SelfProcessSetV1 and ownership hints suppress exact duplicates while unrelated or escaped processes remain observable.

**Implementation Boundary:** Collect PID plus birth/executable identity and suppress only exact srvls roots and in-group worker/provider descendants; emit escaped descendants unless independently Provider-owned.

**Requirement Mapping:** AD-11, AD-21, FR-12, FR-14.

**Dependencies:** Story 3.7.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/provider-process-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Process signaling and action planning.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/provider-process-v1, **When** the story
   capability is exercised, **Then** frozen SelfProcessSetV1 and ownership hints suppress exact duplicates while unrelated or escaped processes remain observable, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** weak parent/name/cwd evidence, whole-descendant suppression, PID reuse, or unresolved child cleanup occurs, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 3.9: Immutable CollectionCandidate reduction

As a srvls Operator or maintainer,
I want immutable collectioncandidate reduction,
So that late/superseded reports cannot alter frozen candidate bytes and candidate creation performs no Snapshot CAS.

**Implementation Boundary:** Normalize eligible reports into one Contract C-03 CollectionCandidateV1 with final diagnostics, Observations, completeness, resources, and no current pointer.

**Requirement Mapping:** AD-11, AD-21, FR-13, FR-14.

**Dependencies:** Story 3.8.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/collection-candidate-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Snapshot persistence and presentation.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/collection-candidate-v1, **When** the story
   capability is exercised, **Then** late/superseded reports cannot alter frozen candidate bytes and candidate creation performs no Snapshot CAS, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** a Collector, worker reap, reducer retry, or display layer rewrites candidate truth, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 3.10: Complete obligation and strict policy

As a srvls Operator or maintainer,
I want complete obligation and strict policy,
So that default and promoted scopes retain usable successes while withheld conclusions and strict failure rows are explicit.

**Implementation Boundary:** Apply the exact per-scope required/optional/not-applicable default and promotion table, report every scope outcome/duration/diagnostic, preserve partial truth, and derive strict exit deterministically.

**Requirement Mapping:** AD-11, AD-21, FR-14, FR-17, NFR-2, SM-C2, UX-CP-2, UX-FND-4, UX-ST-4, UX-ST-5.

**Dependencies:** Story 3.9.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/collection-obligation-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Provider detail inspection and reconciliation.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/collection-obligation-v1, **When** obligation policy is compiled, **Then** invoking-user cron, /etc cron, system/user systemd, and visible direct processes are required; root cron is optional-promotable; Docker and PM2 are optional until detection or active Promise; other-user systemd and PM2 are not-applicable/out-of-scope; and only supported optional scopes may be promoted to required, **And** every complete, partial, unavailable, denied, timed-out, or invalid-output result retains duration, diagnostic, applicable reason, usable evidence, and withheld conclusions.
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** incomplete evidence is treated as empty, absent, healthy, or safe, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 3.11: Bounded Provider evidence inspection

As a srvls Operator or maintainer,
I want bounded provider evidence inspection,
So that inspection is stable by typed ID and visibly names truncation/redaction and the winning bound.

**Implementation Boundary:** Expose sanitized typed detail, separate captures, provenance, diagnostics, redaction, and earlier-of byte/line bounds for one exact Observation.

**Requirement Mapping:** AD-21, FR-14, FR-15, UX-CP-7, UX-IA-4, UX-ST-17.

**Dependencies:** Story 3.10.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/provider-inspect-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** TUI layout and Host mutation.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/provider-inspect-v1, **When** the story
   capability is exercised, **Then** inspection is stable by typed ID and visibly names truncation/redaction and the winning bound, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** raw control bytes, unrestricted logs, secrets, row identity, or another Observation's failure leaks, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

## Epic 4: Reconcile intended and actual runtime truth

Operators get explainable findings, one immutable Snapshot, an explicit Accepted Baseline, and a Brief that answers all eight morning questions.

### Story 4.1: Pure intent-to-observation correlation

As a srvls Operator or maintainer,
I want pure intent-to-observation correlation,
So that exact Provider identity or locator anchors and ordered secondary evidence produce deterministic edges without summing or UI influence.

**Implementation Boundary:** Run the AD-18 lexicographic exact-anchor evidence engine over only the frozen plan and candidate reports, retaining conflicts and ambiguity.

**Requirement Mapping:** AD-11, AD-18, FR-18, FR-26, NFR-1.

**Dependencies:** Story 3.11.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/reconciliation-correlation-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Lifecycle labels and actions.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/reconciliation-correlation-v1, **When** the story
   capability is exercised, **Then** exact Provider identity or locator anchors and ordered secondary evidence produce deterministic edges without summing or UI influence, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** provider/anchor conflict, equal maxima, weak name-only evidence, or later state lookup occurs, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 4.2: Orthogonal lifecycle, evidence, and Promise outcomes

As a srvls Operator or maintainer,
I want orthogonal lifecycle, evidence, and promise outcomes,
So that healthy requires intended exact count and sufficient evidence; broken requires sufficient absence; otherwise unresolved remains explicit.

**Implementation Boundary:** Classify lifecycle, Evidence Status, healthy, broken, and unresolved axes without collapsing partial collection into absence.

**Requirement Mapping:** AD-18, FR-19, FR-20, FR-26, SM-2, UJ-3, UX-FND-2.

**Dependencies:** Story 4.1.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/reconciliation-outcomes-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Observation labels and cleanup.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/reconciliation-outcomes-v1, **When** the story
   capability is exercised, **Then** healthy requires intended exact count and sufficient evidence; broken requires sufficient absence; otherwise unresolved remains explicit, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** Collector failure, near match, expired Lease, or conflicting identity is presented as healthy/broken certainty, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 4.3: Orphan and duplicate-set findings

As a srvls Operator or maintainer,
I want orphan and duplicate-set findings,
So that all duplicate members retain identity and labels while excess count is intended-count arithmetic only.

**Implementation Boundary:** Identify orphan Observations and duplicates as an unordered exact duplicate set plus excess cardinality, with no designated loser or action recommendation.

**Requirement Mapping:** AD-11, AD-18, FR-21, FR-22, FR-26, SM-C1, UX-CP-14.

**Dependencies:** Story 4.2.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/reconciliation-orphan-duplicate-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Stale/hot and action choice.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/reconciliation-orphan-duplicate-v1, **When** the story
   capability is exercised, **Then** all duplicate members retain identity and labels while excess count is intended-count arithmetic only, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** a member is named excess, selected for deletion, or claimed Agent-created without evidence, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 4.4: Positive-evidence stale and hot findings

As a srvls Operator or maintainer,
I want positive-evidence stale and hot findings,
So that stale requires supported positive no-use evidence and hot requires enough retained timestamped samples.

**Implementation Boundary:** Apply exact ARCH-LIM-9/10 windows, samples, thresholds, timestamps, policy provenance, and insufficient-evidence rules.

**Requirement Mapping:** AD-11, AD-18, FR-23, FR-24, FR-26, UJ-5.

**Dependencies:** Story 4.3.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/reconciliation-stale-hot-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Unmanaged/abandoned and safety.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/reconciliation-stale-hot-v1, **When** the story
   capability is exercised, **Then** stale requires supported positive no-use evidence and hot requires enough retained timestamped samples, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** missing samples, one spike, age alone, or UI color produces a label, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 4.5: Unmanaged and abandoned truth without cleanup

As a srvls Operator or maintainer,
I want unmanaged and abandoned truth without cleanup,
So that each label names its exact positive and missing evidence and coexists with other findings.

**Implementation Boundary:** Classify from Durable Ownership, Launch Mechanism, Lease, Heartbeat, and explicit closure evidence while retaining all truth and performing no stop.

**Requirement Mapping:** AD-18, FR-25, FR-26, SM-C3, UX-FND-5.

**Dependencies:** Story 4.4.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/reconciliation-unmanaged-abandoned-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Safe-to-stop and operations.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/reconciliation-unmanaged-abandoned-v1, **When** the story
   capability is exercised, **Then** each label names its exact positive and missing evidence and coexists with other findings, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** expiry, closure, orphan, or unmanaged state triggers mutation or deletes evidence, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 4.6: Explainable conservative Safe-to-stop

As a srvls Operator or maintainer,
I want explainable conservative safe-to-stop,
So that the same frozen truth yields identical assessment/reasons and changed refresh truth recomputes it.

**Implementation Boundary:** Compute safe, unsafe, or unknown with identity, contradictions, missing evidence, ownership, purpose, lifetime, mechanism, policy, and provenance; recalculate after refresh.

**Requirement Mapping:** AD-18, FR-26.

**Dependencies:** Story 4.5.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/safe-to-stop-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Immediate pre-mutation revalidation.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/safe-to-stop-v1, **When** the story
   capability is exercised, **Then** the same frozen truth yields identical assessment/reasons and changed refresh truth recomputes it, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** a label, group, opaque reference, expired Lease, or prior assessment authorizes mutation, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 4.7: Sole Snapshot materialization and current CAS

As a srvls Operator or maintainer,
I want sole snapshot materialization and current cas,
So that latest requested generation commits reports, diagnostics, Observations, resources, findings, Brief material, revisions, and current together.

**Implementation Boundary:** Transform exactly one eligible CollectionCandidateV1 into architecture-native SnapshotV1 in the complete AD-16 transaction and own the only current-pointer CAS.

**Requirement Mapping:** AD-11, AD-18, AD-5, FR-26, FR-27.

**Dependencies:** Story 4.6.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/snapshot-materialization-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Baseline acceptance and TUI.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/snapshot-materialization-v1, **When** the story
   capability is exercised, **Then** latest requested generation commits reports, diagnostics, Observations, resources, findings, Brief material, revisions, and current together, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** a superseded candidate, partial transaction, other layer, or late report attempts current, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 4.8: Explicit Accepted Baseline and Evidence Window

As a srvls Operator or maintainer,
I want explicit accepted baseline and evidence window,
So that eligible accept and audited incomplete override update only baseline/audit and recompute new/resolved/changed/persisting against the accepted Snapshot.

**Implementation Boundary:** Implement b-entry baseline-dialog, eligibility, cancel-first focus, typed override, audit, baseline-pointer-only mutation, and immediate Evidence Window recomputation.

**Requirement Mapping:** AD-11, AD-18, FR-26, FR-27, UX-CP-12, UX-IA-7, UX-IP-6, UX-ST-16.

**Dependencies:** Story 4.7.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/baseline-acceptance-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Host mutation and automatic acceptance.

**Acceptance Criteria:**

1. **Given** an eligible complete current Snapshot and the fixed baseline-acceptance fixtures, **When** b opens baseline-dialog or the deterministic baseline command addresses that exact Snapshot, **Then** Cancel is initially focused, Esc cancels, successful confirmation changes only baseline/audit, and the Brief immediately recomputes new/resolved/changed/persisting with baseline/current timestamps and configured timezone, **And** refresh, exit, scheduled candidates, and actions never advance the baseline.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** an incomplete or incompatible Snapshot lacks every missing scope, a nonempty reason, principal, timestamp, and the exact typed word override, or when first-run/incompatible truth attempts to invent a change set, **Then** acceptance fails with baseline unchanged and no Host mutation, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 4.9: Eight-question deterministic Brief

As a srvls Operator or maintainer,
I want eight-question deterministic brief,
So that all BQ-1 through BQ-8 rows answer the exact question and withhold clean claims when required evidence is incomplete.

**Implementation Boundary:** Materialize every Contract C-14 row with completeness, baseline/current IDs, timezone, Evidence Window, multi-label counts, and drill-down identities.

**Requirement Mapping:** AD-11, AD-18, FR-26, FR-28, SM-1, UJ-1, UX-CP-1, UX-IA-1.

**Dependencies:** Story 4.8.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/brief-eight-questions-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Grouping and TUI rendering.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/brief-eight-questions-v1, **When** the story
   capability is exercised, **Then** all BQ-1 through BQ-8 rows answer the exact question and withhold clean claims when required evidence is incomplete, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** a row is missing, renamed, double-counted, or answered from display/group state, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 4.10: Deterministic attention, Stack, and Ungrouped grouping

As a srvls Operator or maintainer,
I want deterministic attention, stack, and ungrouped grouping,
So that identical findings produce identical grouping/order and group rows remain read-only.

**Implementation Boundary:** Order attention first, infer Stack only from evidence, normalize paths, apply deterministic candidates/facets, and retain ambiguity as inspectable Ungrouped.

**Requirement Mapping:** AD-18, AD-4, FR-26, FR-29, UX-CP-4.

**Dependencies:** Story 4.9.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/brief-grouping-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Presentation styling and mutation.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/brief-grouping-v1, **When** the story
   capability is exercised, **Then** identical findings produce identical grouping/order and group rows remain read-only, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** a benchmark-dependent branch, group action, or hidden ambiguity is introduced, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

## Epic 5: Navigate one accessible terminal product

Operators can route, explore, search, inspect, refresh, recover configuration, and use the product without relying on color, Unicode, motion, or a large terminal.

### Story 5.1: Deterministic output routing and terminal ownership

As a srvls Operator or maintainer,
I want deterministic output routing and terminal ownership,
So that bare, explicit format, TUI, deprecated fzf, help, internal worker, and namespace argv select one exact profile with clean stdout.

**Implementation Boundary:** Route raw argv before effects, preserve legacy noninteractive output, enter TUI only when eligible, and use one RAII terminal owner for every exit/panic/signal path.

**Requirement Mapping:** AD-11, AD-14, AD-7, FR-30, FR-34, NFR-6, UX-FND-1, UX-IP-1, UX-RP-6.

**Dependencies:** Story 4.10.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/presentation-routing-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Surface layout and lifecycle actions.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/presentation-routing-v1, **When** the story
   capability is exercised, **Then** bare, explicit format, TUI, deprecated fzf, help, internal worker, and namespace argv select one exact profile with clean stdout, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** invalid config, explicit TUI failure, redirect, TERM=dumb, panic, or signal could fall through or corrupt terminal, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 5.2: Responsive Brief and Explorer layouts

As a srvls Operator or maintainer,
I want responsive brief and explorer layouts,
So that 120x30, 80x24, 60x20, below-minimum, live-resize, and redirected fixtures match exact component/layout rules.

**Implementation Boundary:** Render full, compact, narrow, below-minimum, resize, and redirected contracts with stable reading order, identity, completeness, modal, and focus state.

**Requirement Mapping:** FR-34, UX-CP-3, UX-IA-2, UX-RP-1, UX-RP-2, UX-RP-3, UX-RP-4, UX-RP-5.

**Dependencies:** Story 5.1.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/tui-responsive-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Search and Host mutation.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/tui-responsive-v1, **When** the story
   capability is exercised, **Then** 120x30, 80x24, 60x20, below-minimum, live-resize, and redirected fixtures match exact component/layout rules, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** resize loses model/focus, hides modal semantics, or turns color/icon/geometry into meaning, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 5.3: Keyboard, facets, focus, and exact Unicode search

As a srvls Operator or maintainer,
I want keyboard, facets, focus, and exact unicode search,
So that valid Unicode and raw-byte fixtures return stable rows and Esc/focus/Clear-all behavior matches UX-IA-11 and UX-ST-19.

**Implementation Boundary:** Implement complete navigation/filter keys, deterministic facet composition, Contract C-02 matching, filtered-empty recovery, and identity-based focus fallback.

**Requirement Mapping:** AD-11, AD-8, FR-31, FR-34, UX-A11Y-2, UX-CP-8, UX-IA-11, UX-IA-5, UX-IP-2, UX-IP-3, UX-ST-19, UX-ST-7.

**Dependencies:** Story 5.2.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/tui-navigation-search-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Provider collection and mutation.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/tui-navigation-search-v1, **When** the story
   capability is exercised, **Then** valid Unicode and raw-byte fixtures return stable rows and Esc/focus/Clear-all behavior matches UX-IA-11 and UX-ST-19, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** simple fold, NFKC, locale, lossy bytes, row-index focus, or action retargeting occurs, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 5.4: Runtime and evidence detail surfaces

As a srvls Operator or maintainer,
I want runtime and evidence detail surfaces,
So that enter/Esc/Ctrl-F/n/N/PgUp/PgDn operate within the selected typed aggregate and missing evidence is a visible row.

**Implementation Boundary:** Render Promise and Observation axes, bounded evidence/provider detail, provenance, redaction, diagnostics, and exact return paths without identity merging.

**Requirement Mapping:** FR-32, FR-34, SM-6, UX-CP-5, UX-CP-6, UX-IA-3.

**Dependencies:** Story 5.3.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/tui-detail-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Collection or action execution.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/tui-detail-v1, **When** the story
   capability is exercised, **Then** Enter/Esc/Ctrl-F/n/N/PgUp/PgDn operate within the selected typed aggregate and missing evidence is a visible row, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** friendly name, group, opaque reference, or raw content becomes identity/truth, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 5.5: Affirmative external-system boundary

As a srvls Operator or maintainer,
I want affirmative external-system boundary,
So that plane intended work, Git code changes, and Telemetry events/measurements render as labeled display-only metadata.

**Implementation Boundary:** Display Plane, Git, and Telemetry references only under Contract C-13 and test each affirmative owner and prohibited runtime use.

**Requirement Mapping:** AD-11, FR-32, FR-34.

**Dependencies:** Story 5.4.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/external-boundary-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** External API integration.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/external-boundary-v1, **When** opaque references are rendered, **Then** Plane remains authoritative for intended work, Git for code changes, and Telemetry for events/measurements; each reference is labeled display-only and never affects Runtime identity, health, reconciliation, safety, or mutation authority, **And** repeated runs over identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** srvls fetches, mutates, interprets health from, reconciles with, or authorizes from any reference, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 5.6: Nonblocking refresh and explicit application states

As a srvls Operator or maintainer,
I want nonblocking refresh and explicit application states,
So that loading, refreshing, stale, partial-failure, unavailable-Provider, empty, and bounded-detail fixtures render exact recovery guidance.

**Implementation Boundary:** Keep committed truth visible during loading/refresh, show generation progress, stale/partial/unavailable/empty states, and disable stale actions without optimistic mutation.

**Requirement Mapping:** FR-34, UX-ST-1, UX-ST-2, UX-ST-3, UX-ST-6.

**Dependencies:** Story 5.5.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/tui-refresh-states-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Action outcome states.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/tui-refresh-states-v1, **When** the story
   capability is exercised, **Then** loading, refreshing, stale, partial-failure, unavailable-Provider, empty, and bounded-detail fixtures render exact recovery guidance, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** refresh blocks navigation, clears current truth, advances baseline, or presents incomplete as empty, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 5.7: Text-first accessibility and hostile-text safety

As a srvls Operator or maintainer,
I want text-first accessibility and hostile-text safety,
So that keyboard/screen-reader, TERM=dumb, NO_COLOR, non-UTF-8, control-byte, and motion-free fixtures preserve all meaning.

**Implementation Boundary:** Implement NO_COLOR, ASCII, motion-free progress, sanitized hostile text, semantic reading order, persistent focus, and terminal restoration.

**Requirement Mapping:** AD-11, FR-33, FR-34, NFR-8, UX-A11Y-1, UX-A11Y-4, UX-A11Y-5, UX-VT-1, UX-VT-2.

**Dependencies:** Story 5.6.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/tui-accessibility-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Action submission and release progress.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/tui-accessibility-v1, **When** the story
   capability is exercised, **Then** keyboard/screen-reader, TERM=dumb, NO_COLOR, non-UTF-8, control-byte, and motion-free fixtures preserve all meaning, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** color, glyph, animation, cursor motion, large geometry, or trusted Host text is required, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 5.8: Help and invalid-configuration recovery

As a srvls Operator or maintainer,
I want help and invalid-configuration recovery,
So that question-mark/Esc restores prior focus and invalid config emits one deterministic linear/JSON error before TUI, collection, SQLite, or mutation.

**Implementation Boundary:** Provide complete help-overlay and pre-side-effect config validation/explain with field, redacted value, source, type, range, precedence, default, correction, and restart guidance.

**Requirement Mapping:** FR-34, UX-CP-13, UX-IA-12, UX-IA-8, UX-IP-12, UX-ST-18, UX-VT-3, UX-VT-4.

**Dependencies:** Story 5.7.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/help-config-recovery-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** State goldens and benchmarks.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/help-config-recovery-v1, **When** the story
   capability is exercised, **Then** question-mark/Esc restores prior focus and invalid config emits one deterministic linear/JSON error before TUI, collection, SQLite, or mutation, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** help omits a key/safety/linear/exit rule or config silently clamps/hides a lower source, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 5.9: State/component goldens and UX budget gate

As a srvls Operator or maintainer,
I want state/component goldens and ux budget gate,
So that all UX-ST read-only states/components match immutable goldens and 30 post-warm-up iterations meet each UX-BUD default/range/p95 on the four-vCPU 8-GiB glibc-2.42 profile.

**Implementation Boundary:** Own fixed read-only state/component goldens separately from the constrained ARCH-HOST-1 benchmark and aggregate UX/accessibility gate.

**Requirement Mapping:** AD-11, ARCH-HOST-1, FR-34, UX-BUD-1, UX-BUD-2, UX-BUD-3, UX-BUD-7.

**Dependencies:** Story 5.8.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/tui-state-budget-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Lifecycle action implementation.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/tui-state-budget-v1, **When** the story
   capability is exercised, **Then** all UX-ST read-only states/components match immutable goldens and 30 post-warm-up iterations meet each UX-BUD default/range/p95 on the four-vCPU 8-GiB glibc-2.42 profile, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** a golden is self-recoded, benchmark evidence is incomplete, or any state/budget/SR row is missing, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

## Epic 6: Act on one exact runtime safely

Operators can plan, confirm, submit, observe, verify, and recover one exact supported action with no detached mutation or ambiguous outcome.

### Story 6.1: One closed ActionKindV1 vocabulary

As a srvls Operator or maintainer,
I want one closed actionkindv1 vocabulary,
So that all Provider-by-kind cells and lowercase encodings match the complete matrix.

**Implementation Boundary:** Implement Contract C-04 once and require capability, plan, storage, executor, event, linear, machine, and fixture code to import it.

**Requirement Mapping:** AD-11, AD-22, AD-6, FR-36, FR-40.

**Dependencies:** Story 5.9.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/action-kind-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Planning confirmation and execution.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/action-kind-v1, **When** the story
   capability is exercised, **Then** all Provider-by-kind cells and lowercase encodings match the complete matrix, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** signal, alias, unknown, wrong case, provider-local enum, or unsupported cell is accepted, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 6.2: Discoverable exact-target Action Menu

As a srvls Operator or maintainer,
I want discoverable exact-target action menu,
So that supported/unsafe/unknown/stale/pending cells render exactly and accelerators enter the same plan path.

**Implementation Boundary:** Open a only for one exact Promise/Observation, show supported cells and disabled safety reasons, keep all groups read-only, and permit Promise-origin start.

**Requirement Mapping:** AD-22, FR-35, FR-40, FR-41, UX-CP-9, UX-IA-6, UX-IP-4.

**Dependencies:** Story 6.1.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/action-menu-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Plan persistence and mutation.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/action-menu-v1, **When** the story
   capability is exercised, **Then** supported/unsafe/unknown/stale/pending cells render exactly and accelerators enter the same plan path, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** row, name, group, cron, incomplete identity, or unsupported action widens a target, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 6.3: Immutable ActionPlan and complete confirmation matrix

As a srvls Operator or maintainer,
I want immutable actionplan and complete confirmation matrix,
So that start, Restart, Stop, Disable, Delete and every safety state select the exact availability/token/focus rule.

**Implementation Boundary:** Persist ActionPlanV1 with PlanId only, exact target/generation/policy/BootIdentity/TTL/actor/idempotency and Contract C-05 confirmation.

**Requirement Mapping:** AD-11, AD-22, FR-38, FR-40, UX-CP-10, UX-IP-5, UX-ST-20.

**Dependencies:** Story 6.2.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/action-plan-confirmation-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Pool, submit, and Host execution.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/action-plan-confirmation-v1, **When** the story
   capability is exercised, **Then** Start, Restart, Stop, Disable, Delete and every safety state select the exact availability/token/focus rule, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** OperationId is allocated, Cancel is not focused, Esc submits, or confirmation can be bypassed, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 6.4: Immediate identity, capability, and safety revalidation

As a srvls Operator or maintainer,
I want immediate identity, capability, and safety revalidation,
So that unchanged exact evidence authorizes submit while stale/reused/missing/ambiguous/expired/unsafe drift refuses with no launch.

**Implementation Boundary:** After confirmation and strictly before mutation re-resolve every captured identity/capability/generation/policy/BootIdentity and recompute Safe-to-stop within ARCH-LIM-21.

**Requirement Mapping:** AD-22, FR-26, FR-37, FR-40, UX-ST-14.

**Dependencies:** Story 6.3.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/action-revalidation-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Pool ownership and Provider mutation.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/action-revalidation-v1, **When** confirmation completes and immediately before mutation, **Then** the implementation re-resolves exact identity/capability/generation/policy/BootIdentity and recomputes Safe-to-stop from fresh evidence; only an unchanged safe result authorizes submit while stale/reused/missing/ambiguous/expired/unsafe drift refuses with no launch, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** display name, row, cached assessment, or post-deadline evidence passes, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 6.5: Separate bounded action pool primitive

As a srvls Operator or maintainer,
I want separate bounded action pool primitive,
So that available slots reserve deterministically and saturation returns pre-launch refusal without creating a running task.

**Implementation Boundary:** Implement the fair ARCH-LIM-20 pool before admission, independent of collection, with no unbounded queue or Provider effect.

**Requirement Mapping:** AD-11, AD-22, FR-40.

**Dependencies:** Story 6.4.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/action-pool-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Atomic submit and UI.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/action-pool-v1, **When** the story
   capability is exercised, **Then** available slots reserve deterministically and saturation returns pre-launch refusal without creating a running task, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** collection slots, late admission, hidden queue, starvation, or Provider launch consumes capacity, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 6.6: Atomic operation admission and handoff

As a srvls Operator or maintainer,
I want atomic operation admission and handoff,
So that retry returns the same operation and phase/evidence transitions are gap-free and architecture-native.

**Implementation Boundary:** Consume a valid plan by CAS, allocate OperationId only at submit, enforce exact-target/idempotency uniqueness, and persist only planned/launch-authorized/executing/verifying.

**Requirement Mapping:** AD-11, AD-22, FR-39, FR-40, NFR-12.

**Dependencies:** Story 6.5.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/action-admission-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Provider execution and final outcome.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/action-admission-v1, **When** the story
   capability is exercised, **Then** retry returns the same operation and phase/evidence transitions are gap-free and architecture-native, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** queued/admitted/running/refused durable aliases, duplicate target, expired plan, or launch before launch-authorized occurs, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 6.7: In-process exact-target executors

As a srvls Operator or maintainer,
I want in-process exact-target executors,
So that each supported matrix cell invokes only its exact D-Bus/socket/protocol/kernel target and records LaunchReceiptV1.

**Implementation Boundary:** Execute systemd/Docker/PM2/direct-process/Launch-Mechanism effects only in the lock-owning owner under Contract C-10, with direct signal encoded as stop parameters.

**Requirement Mapping:** AD-11, AD-22, FR-40, NFR-5.

**Dependencies:** Story 6.6.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/action-executor-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Verification and presentation.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/action-executor-v1, **When** the story
   capability is exercised, **Then** each supported matrix cell invokes only its exact D-Bus/socket/protocol/kernel target and records LaunchReceiptV1, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** CommandRunner, shell, mutating systemctl child, raw command, signal kind, broad privilege, or wrong identity is used, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 6.8: Operation-status surface integration

As a srvls Operator or maintainer,
I want operation-status surface integration,
So that 100-ms submit acknowledgement and periodic phase updates retain exact operation/target and durable repository truth.

**Implementation Boundary:** Bind operation-status by OperationId across navigation/refresh, show pending/executing/verifying truth, suppress duplicate input, and never change resource state optimistically.

**Requirement Mapping:** AD-22, FR-40, UX-CP-11, UX-IP-7, UX-ST-8.

**Dependencies:** Story 6.7.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/action-status-surface-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Outcome decision and shutdown.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/action-status-surface-v1, **When** the story
   capability is exercised, **Then** 100-ms submit acknowledgement and periodic phase updates retain exact operation/target and durable repository truth, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** focus move, refresh, resize, repeated key, or concurrent operation misattributes or hides status, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 6.9: Fresh verification and total outcome precedence

As a srvls Operator or maintainer,
I want fresh verification and total outcome precedence,
So that every verification predicate and race resolves to exactly one ordered outcome with evidence, reason, and next safe step.

**Implementation Boundary:** Collect OperationId-correlated post-launch Provider evidence and apply Contract C-06 as the sole OperationCoordinator terminal CAS.

**Requirement Mapping:** AD-11, AD-22, FR-40, SM-3, UJ-4, UX-ST-10, UX-ST-11, UX-ST-12, UX-ST-13, UX-ST-15, UX-ST-9.

**Dependencies:** Story 6.8.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/action-outcome-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Shutdown recovery and aggregate gate.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/action-outcome-v1, **When** the story
   capability is exercised, **Then** every verification predicate and race resolves to exactly one ordered outcome with evidence, reason, and next safe step, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** command exit alone verifies, a diagnostic creates an alias, or replacement becomes stale-identity, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 6.10: Signal, exit, and durable finalization recovery

As a srvls Operator or maintainer,
I want signal, exit, and durable finalization recovery,
So that pre-launch exit refuses; executing/verifying uncertainty resolves conservatively; storage failure keeps the owner alive until terminal truth persists.

**Implementation Boundary:** Apply phase-specific cancellation and Contract C-10 no-detach behavior, restore terminal, and retry bounded finalization without reexecuting mutation.

**Requirement Mapping:** AD-11, AD-22, FR-40, UX-IP-10.

**Dependencies:** Story 6.9.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/action-shutdown-recovery-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Human-linear parity.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/action-shutdown-recovery-v1, **When** the story
   capability is exercised, **Then** pre-launch exit refuses; executing/verifying uncertainty resolves conservatively; storage failure keeps the owner alive until terminal truth persists, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** q/Esc detaches, repeated signal changes truth, orderly exit leaves a nonterminal operation, or mutation replays, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 6.11: Human-linear and machine action parity

As a srvls Operator or maintainer,
I want human-linear and machine action parity,
So that tUI, --linear, and --json share ActionKind, PlanId/OperationId, phases, outcome, evidence, and reasons.

**Implementation Boundary:** Expose exact typed action plan, execute, status, acknowledgement, outcome, stdout/stderr, and exit contracts with no alternate stdin grammar.

**Requirement Mapping:** AD-22, FR-40, UX-A11Y-3, UX-CP-15, UX-IP-11.

**Dependencies:** Story 6.10.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/action-linear-machine-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Aggregate action gate.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/action-linear-machine-v1, **When** the story
   capability is exercised, **Then** TUI, --linear, and --json share ActionKind, PlanId/OperationId, phases, outcome, evidence, and reasons, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** a surface renames a kind/outcome, accepts raw stdin, emits ANSI/progress, or bypasses confirmation, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 6.12: Complete action and SR-A11Y-1 gate

As a srvls Operator or maintainer,
I want a complete action and SR-A11Y-1 gate,
So that TERM=dumb and NO_COLOR fixtures answer all eight Brief questions, locate withheld truth, inspect, review safety, submit an exact plan, and retrieve all five outcomes.

**Implementation Boundary:** Run enum, matrix, plan, pool, admission, executor, status, outcome, shutdown, parity, budgets, and complete linear morning/action journey under one gate.

**Requirement Mapping:** AD-11, AD-22, FR-40, SR-A11Y-1, UX-BUD-4, UX-BUD-5, UX-BUD-6.

**Dependencies:** Story 6.11.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/action-aggregate-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Release implementation.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/action-aggregate-v1, **When** the story
   capability is exercised, **Then** TERM=dumb and NO_COLOR fixtures answer all eight Brief questions, locate withheld truth, inspect, review safety, submit exact plan, and retrieve all five outcomes, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** any UX-BUD-4/5/6, UX-IP, UX-ST action row, accessibility case, or AD-11 action row is omitted, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

## Epic 7: Upgrade and recover the installed pair without split truth

Operators can install, upgrade, validate, recover, and roll back one exact binary/state/consumer pair through crash-safe architecture-native transactions.

### Story 7.1: Stable toolchain and exact release artifact

As a srvls Operator or maintainer,
I want stable toolchain and exact release artifact,
So that the admitted final artifact alone binds compiler/component/manifest/source/Cargo.lock/checksum/ABI/smoke evidence.

**Implementation Boundary:** Build Contract C-11 StableToolchainEvidenceV1 and ReleaseBinaryArtifactV1 from fresh official Rust stable 1.97.1 evidence, locked source, exact hash, readelf glibc-2.42 proof, and smoke.

**Requirement Mapping:** AD-11, AD-12, FR-42, FR-43, NFR-15.

**Dependencies:** Story 6.12.

**Validation Expectations:** The owning oracle is tests/fixtures/contracts/release-transaction-v1/stable-toolchain-evidence.json; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Installation mutation and consumer migration.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/contracts/release-transaction-v1/stable-toolchain-evidence.json, **When** the story
   capability is exercised, **Then** the admitted final artifact alone binds compiler/component/manifest/source/Cargo.lock/checksum/ABI/smoke evidence, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** cached 1.97.0, stale manifest, another artifact, generic ldd, or compile-before-evidence is selected, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 7.2: Traditional POSIX admission and action handoff

As a srvls Operator or maintainer,
I want traditional posix admission and action handoff,
So that traditional [0,1) record-lock fixtures prove conflict, EINTR, owner loss, CLOEXEC, shared drain, and handoff.

**Implementation Boundary:** Implement Contract C-11 shared/exclusive lock, exact descriptor invariants, drain-before-cut, owner-loss semantics, and ActionExecutorHandoffV1.

**Requirement Mapping:** AD-11, AD-23, FR-43.

**Dependencies:** Story 7.1.

**Validation Expectations:** The owning oracle is tests/fixtures/contracts/release-transaction-v1/admission-record-lock.trace.json; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Transaction planning and release commands.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/contracts/release-transaction-v1/admission-record-lock.trace.json, **When** the story
   capability is exercised, **Then** traditional [0,1) record-lock fixtures prove conflict, EINTR, owner loss, CLOEXEC, shared drain, and handoff, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** flock/lockf/OFD, reopen/dup/stdio/inheritance/close, state sampling before drain, or detach occurs, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 7.3: Canonical release command surfaces

As a srvls Operator or maintainer,
I want canonical release command surfaces,
So that each exact verb and argument set routes to one application command and deterministic non-TUI record.

**Implementation Boundary:** Parse exactly release install, upgrade, validate, status, rollback and their typed Agent/linear argv/result/exit contracts without mutation implementation.

**Requirement Mapping:** AD-23, FR-43.

**Dependencies:** Story 7.2.

**Validation Expectations:** The owning oracle is tests/fixtures/implementation/release-command-surface-v1; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Transaction execution and aggregate gate.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/implementation/release-command-surface-v1, **When** the story
   capability is exercised, **Then** each exact verb and argument set routes to one application command and deterministic non-TUI record, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** recover, stdin grammar, ambiguous namespace, alternate phase/result name, ANSI, or TUI entry is accepted, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 7.4: Managed consumer manifest before preimages

As a srvls Operator or maintainer,
I want managed consumer manifest before preimages,
So that manifest readback names every byte/hash/path/enablement and exists before any UpgradeTransactionV1 preimage.

**Implementation Boundary:** Discover and freeze ManagedConsumerManifestV1 with exactly the sorted metrics and snapshot service/timer pairs and exact two executable occurrences.

**Requirement Mapping:** AD-11, AD-23, FR-43.

**Dependencies:** Story 7.3.

**Validation Expectations:** The owning oracle is tests/fixtures/contracts/release-transaction-v1/brownfield-consumer-pairs.json; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Consumer replacement and rollback.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/contracts/release-transaction-v1/brownfield-consumer-pairs.json, **When** the story
   capability is exercised, **Then** manifest readback names every byte/hash/path/enablement and exists before any UpgradeTransactionV1 preimage, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** an extra consumer, missing occurrence, script, ambiguous path, or preimage capture precedes the manifest, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 7.5: UpgradeTransaction planning, preimages, and staging

As a srvls Operator or maintainer,
I want upgradetransaction planning, preimages, and staging,
So that all preimages and checksums are immutable/read back before the first effect and every manifest replacement is file-fsync/rename/directory-fsync crash safe.

**Implementation Boundary:** Create architecture-native UpgradeTransactionV1 from ReleaseBinaryArtifactV1 and ManagedConsumerManifestV1, freeze complete binary/state/consumer/admission authorities, backup, and staged candidate before mutation.

**Requirement Mapping:** AD-23, FR-43.

**Dependencies:** Story 7.4.

**Validation Expectations:** The owning oracle is tests/fixtures/contracts/release-transaction-v1/initial-transaction-created.manifest.json; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Forward activation, validation, and recovery.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/contracts/release-transaction-v1/initial-transaction-created.manifest.json, **When** the story
   capability is exercised, **Then** all preimages and checksums are immutable/read back before the first effect and every manifest replacement is file-fsync/rename/directory-fsync crash safe, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** a preimage is absent/late, type alias appears, capacity is insufficient, or stage differs from admitted artifact, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 7.6: Exact in-owner consumer migration

As a srvls Operator or maintainer,
I want exact in-owner consumer migration,
So that candidate and readback hashes differ only at the two manifest-authorized byte spans.

**Implementation Boundary:** Replace exactly the two canonical executable occurrences and keep every other consumer byte/property/enablement unchanged using in-process filesystem and manager ownership.

**Requirement Mapping:** AD-23, FR-43.

**Dependencies:** Story 7.5.

**Validation Expectations:** The owning oracle is tests/fixtures/contracts/release-transaction-v1/brownfield-consumer-pairs.json; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** FD4 validation and recovery.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/contracts/release-transaction-v1/brownfield-consumer-pairs.json, **When** the story
   capability is exercised, **Then** candidate and readback hashes differ only at the two manifest-authorized byte spans, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** script/config normalization, bounded deviation, extra replacement, mutating child systemctl, or partial pair appears, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 7.7: Closed FD4 candidate validation and shared D-Bus cut

As a srvls Operator or maintainer,
I want closed fd4 candidate validation and shared d-bus cut,
So that forward, installed-prior recovery, and explicit rollback bind exact directional generations/artifact/schema and all four evidence classes to one attempt.

**Implementation Boundary:** Implement Contract C-12 exact request/result, peer/parent authentication, D-Bus handshake, pair causality, and one ARCH-LIM-24 deadline.

**Requirement Mapping:** AD-11, AD-23, FR-43.

**Dependencies:** Story 7.6.

**Validation Expectations:** The owning oracle is tests/fixtures/contracts/release-transaction-v1/fd4-request.json; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Commit decision and recovery policy.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/contracts/release-transaction-v1/fd4-request.json, **When** the story
   capability is exercised, **Then** forward, installed-prior recovery, and explicit rollback bind exact directional generations/artifact/schema and all four evidence classes to one attempt, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** extra field, replay, wrong peer/owner/order/generation/hash/schema/deadline, manager change, sequence gap, or trailing byte occurs, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 7.8: Forward install and upgrade execution

As a srvls Operator or maintainer,
I want forward install and upgrade execution,
So that each pending/complete effect and event/revision advances in exact AD-23 order to committed or starts pre-decision restore.

**Implementation Boundary:** Run the staged checksum, smoke, quiesced state migration, exact consumer activation, reload, paired timer trigger, FD4 validation, and durable decision sequence in the exclusive owner.

**Requirement Mapping:** AD-23, FR-43.

**Dependencies:** Story 7.7.

**Validation Expectations:** The owning oracle is tests/fixtures/contracts/release-transaction-v1/forward.transitions.jsonl; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** KnownGood publication and crash takeover.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/contracts/release-transaction-v1/forward.transitions.jsonl, **When** the story
   capability is exercised, **Then** each pending/complete effect and event/revision advances in exact AD-23 order to committed or starts pre-decision restore, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** a mutating child, split pair, skipped readback, forward-only evidence reuse, or terminal alias appears, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 7.9: Generic owner takeover and recovery engine

As a srvls Operator or maintainer,
I want generic owner takeover and recovery engine,
So that each crash cut resumes from readback and ends committed, forward-failed-recovered, rolled-back, or upgrade-recovery-required as applicable.

**Implementation Boundary:** Recover any nonterminal UpgradeTransactionV1 from its durable envelope with a later active owner, exact step idempotency, no reexecution of complete effects, and one canonical terminal.

**Requirement Mapping:** AD-11, AD-23, FR-43.

**Dependencies:** Story 7.8.

**Validation Expectations:** The owning oracle is tests/fixtures/contracts/release-transaction-v1/owner-takeover.transitions.jsonl; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** KnownGood-specific and FirstInstall branches.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/contracts/release-transaction-v1/owner-takeover.transitions.jsonl, **When** the story
   capability is exercised, **Then** each crash cut resumes from readback and ends committed, forward-failed-recovered, rolled-back, or upgrade-recovery-required as applicable, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** generic recovery assumes KnownGood publication, rewinds a complete effect, invents restored/failed-needs-manual, or detaches, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 7.10: Commit-bound KnownGood publication and recovery

As a srvls Operator or maintainer,
I want commit-bound knowngood publication and recovery,
So that publication happens only after decision and no extra pointer field exists; resumed cuts preserve the sole canonical candidate.

**Implementation Boundary:** After durable CommitDecisionV1 publish exact KnownGoodReleaseV1, recover its pending/complete cuts, verify checksum/generation/source, then make admission ready.

**Requirement Mapping:** AD-11, AD-23, FR-43.

**Dependencies:** Story 7.9.

**Validation Expectations:** The owning oracle is tests/fixtures/contracts/release-transaction-v1/known-good-publication-pending.manifest.json; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** FirstInstall and explicit rollback.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/contracts/release-transaction-v1/known-good-publication-pending.manifest.json, **When** the story
   capability is exercised, **Then** publication happens only after decision and no extra pointer field exists; resumed cuts preserve the sole canonical candidate, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** policy/evidence extension, pre-decision publish, older accidental selection, or ready-before-readback occurs, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 7.11: FirstInstall absence planning

As a srvls Operator or maintainer,
I want firstinstall absence planning,
So that only exact absence with no foreign displacement creates the sentinel and restore plan.

**Implementation Boundary:** Prove and freeze complete FirstInstallAbsentV1 link/binary/state/WAL/SHM/consumer/unit/enablement absence with reserved generation zero before effects.

**Requirement Mapping:** AD-23, FR-43.

**Dependencies:** Story 7.10.

**Validation Expectations:** The owning oracle is tests/fixtures/contracts/release-transaction-v1/first-install-absent-pending-consumer-removal.manifest.json; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** FirstInstall forward/recovery execution.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/contracts/release-transaction-v1/first-install-absent-pending-consumer-removal.manifest.json, **When** the story
   capability is exercised, **Then** only exact absence with no foreign displacement creates the sentinel and restore plan, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** foreign file/symlink, partial absence, fabricated prior binary, nonzero generation, or deletion occurs, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 7.12: FirstInstall execution and absence recovery

As a srvls Operator or maintainer,
I want firstinstall execution and absence recovery,
So that failure restores byte-total declared absence and returns forward-failed-recovered only after all readbacks.

**Implementation Boundary:** Execute FirstInstall forward activation and every automatic absent-restore crash cut, refuse foreign replacements without deletion, and prove complete absence before ready generation zero.

**Requirement Mapping:** AD-11, AD-23, FR-43.

**Dependencies:** Story 7.11.

**Validation Expectations:** The owning oracle is tests/fixtures/contracts/release-transaction-v1/first-install-recovery.transitions.jsonl; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Explicit rollback planning.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/contracts/release-transaction-v1/first-install-recovery.transitions.jsonl, **When** the story
   capability is exercised, **Then** failure restores byte-total declared absence and returns forward-failed-recovered only after all readbacks, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** a sidecar/unit/enablement/path remains, foreign replacement is deleted, absent binary is invoked, or partial recovery terminalizes, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 7.13: Explicit rollback plan and confirmation

As a srvls Operator or maintainer,
I want explicit rollback plan and confirmation,
So that installed target freezes source/target generations and byte-equal retained bundle; sentinel retry returns identical no-transaction result.

**Implementation Boundary:** Read the current KnownGoodReleaseV1, refuse FirstInstall sentinel with byte-identical zero-mutation rollback-unavailable, or create a new exact reverse UpgradeTransactionV1 after explicit confirmation.

**Requirement Mapping:** AD-23, FR-43.

**Dependencies:** Story 7.12.

**Validation Expectations:** The owning oracle is tests/fixtures/contracts/release-transaction-v1/explicit-rollback-ready-admission-pending.manifest.json; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Rollback execution and validation.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/contracts/release-transaction-v1/explicit-rollback-ready-admission-pending.manifest.json, **When** the story
   capability is exercised, **Then** installed target freezes source/target generations and byte-equal retained bundle; sentinel retry returns identical no-transaction result, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** rollback repoints directly, lacks confirmation, creates work for sentinel, or reuses the forward transaction, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 7.14: Explicit rollback execution and displaced-source publication

As a srvls Operator or maintainer,
I want explicit rollback execution and displaced-source publication,
So that successful rollback returns rolled-back with exact generations and preserves future reversal direction.

**Implementation Boundary:** Run the full reverse transaction, fresh FD4/D-Bus validation, decision, event, and commit; publish the displaced installed source pair as future KnownGood.

**Requirement Mapping:** AD-11, AD-23, FR-43.

**Dependencies:** Story 7.13.

**Validation Expectations:** The owning oracle is tests/fixtures/contracts/release-transaction-v1/explicit-rollback.transitions.jsonl; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Aggregate release gate.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/fixtures/contracts/release-transaction-v1/explicit-rollback.transitions.jsonl, **When** the story
   capability is exercised, **Then** successful rollback returns rolled-back with exact generations and preserves future reversal direction, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** forward evidence substitutes for reverse evidence, old target remains KnownGood, pair is partial, or rollback alias appears, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.

### Story 7.15: Release aggregate and Host smoke gate

As a srvls Operator or maintainer,
I want release aggregate and host smoke gate,
So that every AD-11 release registry row and exact final-artifact Host smoke passes, with current versus future deliverables distinguished.

**Implementation Boundary:** Wire commands, locks, toolchain, artifact, manifest, forward, FD4, D-Bus, takeover, KnownGood, FirstInstall, rollback, all seven transition histories, exact terminal mapping, and future service-manager rows into the aggregate.

**Requirement Mapping:** AD-11, AD-23, FR-43, UJ-6, UX-CP-16, UX-IA-9, UX-IP-8.

**Dependencies:** Story 7.14.

**Validation Expectations:** The owning oracle is tests/validate_architecture_contracts.sh; expected bytes
and assertions are fixed independently of the implementation under test.

**Out of Scope:** Publishing or deploying release artifacts, and changing the user override.

**Acceptance Criteria:**

1. **Given** the fixed positive fixtures in tests/validate_architecture_contracts.sh, **When** the story
   capability is exercised, **Then** every AD-11 release registry row and exact final-artifact Host smoke passes, with current versus future deliverables distinguished, **And** repeated runs over
   identical input produce identical typed results and evidence.
2. **Given** the fixed negative, boundary, race, and crash-cut fixtures for this
   story, **When** a registry row, fixture, assertion, command, terminal, consumer, crash cut, or quarantine expectation is omitted, **Then** the capability fails closed with its
   exact typed result before any unauthorized side effect, **And**
   bash tests/validate_architecture_contracts.sh rejects any missing owning row.
