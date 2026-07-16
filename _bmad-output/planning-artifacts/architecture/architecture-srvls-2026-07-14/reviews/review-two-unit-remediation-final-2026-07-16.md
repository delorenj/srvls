---
title: "srvls Architecture Final Two-Unit Remediation Gate"
type: architecture-review
status: final
created: 2026-07-16
updated: 2026-07-16
reviewer: independent-configured-two-unit-reviewer
review_mode: final-adversarial-remediation-gate
reviewed_base_commit: d4515067af8314cadf979da7b17921fbafc92d21
reviewed_worktree_spine_sha256: 66e90f988cc607c1b90b2bb841ca6b1cdd7f7bdf49ccd74920a7e65916df436d
reviewed_artifact: _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md
verdict: changes-required
blocking_status: blocked
earlier_named_findings_closed: 7
rerun_findings_closed: 2
new_blocking_findings: 1
new_high_findings: 1
---

<!-- markdownlint-disable MD013 MD025 -->

# Architecture Review: Final Two-Unit Remediation Gate

## Verdict

**CHANGES REQUIRED. Blocking status: BLOCKED for final scoped-collection
implementation stories.**

The frozen 1,535-line revision closes both findings from the preceding rerun at
their primary seams:

- RERUN-B01 now maps every named pre-deadline worker transport failure to a
  coordinator-synthesized `invalid-output` CollectorReportV1 and maps deadline
  equality or later to `timed-out`, preserving ordinary AD-5 strictness,
  current-pointer, Brief, and baseline rules.
- RERUN-B02 now publishes a checksummed, gap-free recovery-owner attempt under
  an exclusive lock capability, binds a fresh FD4 request/result to that exact
  attempt and manifest revision, rejects stale or forged owners, and supports a
  second owner crash.

The seven earlier NEW-B/NEW-H findings also remain closed, and no new
ReleaseEvent or KnownGood contradiction was found.

Two final collection seams still allow independent implementations to diverge:

1. The synthetic WorkerTransportFailure diagnostic is not byte-total. AD-25
   fixes its code and some conditional parameters but not its subject,
   parameter-schema version and exact key set/order, source encounter, duplicate
   occurrence, or the timeout candidate's corresponding bytes. C-B
   implementations therefore persist different DiagnosticIds and Snapshot
   bytes for the same failure.
2. The one-shot barrier scheduler does not say whether all jobs assigned to
   slots free at the same instant are spawned/authenticated as one batch before
   a process job closes the gate. Sequential dispatch yields 62 seconds for the
   spine's claimed 61-second pathological example. The example selects one
   answer only for that fixture, not a general dispatch-epoch rule for every
   process position.

The first is blocking because it breaks the byte-level C-A/C-B contract and
deterministic Snapshot identity. The second is high because admission-time
cutoff validation can disagree with the runtime schedule and create false
timeouts. The spine correctly remains `draft`.

This review adds only this new report. It does not edit the spine, prior
reports, `tasks.md`, canonical product/UX artifacts, or product code.

## Review Target and Basis

The exact target is branch
`feature-prof-fiddlesticks-architecture-remediation`, base commit
`d4515067af8314cadf979da7b17921fbafc92d21`, and working-tree spine SHA-256:

`66e90f988cc607c1b90b2bb841ca6b1cdd7f7bdf49ccd74920a7e65916df436d`

The complete current spine was re-read from line 1 through EOF after verifying
that digest. The canonical PRD, addendum, DESIGN, and EXPERIENCE remained
unchanged in the working tree from the immediately preceding complete source
read and retained their governing precedence. The complete BMAD architecture
skill, headless reference, and reviewer-gate reference were re-read before this
final gate.

The final acceptance standard is literal interoperability. A named type,
reason, fixture, or worked example is insufficient when two units can still
choose different bytes, dispatch epochs, durable rows, current truth, public
events, or crash results.

## Independently Reconstructed Units

| Pair | Unit | Independent responsibility |
| --- | --- | --- |
| Promise/reconciliation | P-A — Promise Lifecycle Command Unit | Validates lifecycle commands and atomically appends the next event plus authoritative Promise projection revision. |
| Promise/reconciliation | P-B — Reconciliation and State Unit | Consumes only the admitted plan and eligible reports, computes reconciliation and FR-27 changes, and requests atomic Snapshot/Findings/current truth. |
| Collection/reducer | C-A — Scoped Collection Worker Unit | Authenticates one-shot FD3, validates one byte-total assignment, performs only supplied Host work, and returns one bounded report/result. |
| Collection/reducer | C-B — Snapshot Reducer and Persistence Unit | Admits the plan, schedules one-shot workers, validates transport/results, synthesizes terminal reports, finalizes diagnostics/suppression, and persists collection truth. |
| Release/storage | I-A — Release Install Coordinator | Owns admission, recovery-owner publication, FD4 validation, transaction/event ordering, KnownGood publication, rollback, and recovery. |
| Release/storage | I-B — SQLite Migration and Recovery Adapter | Performs backup, migrate, restore, sidecar/integrity verification, exact readbacks, hashing, and fsync effects requested by I-A. |

No unit was allowed a late repository, wall-clock, configuration, discovery, or
owner-rebinding read not explicitly granted by the spine.

## RERUN Finding Closure

### RERUN-B01 — Outcome and current-truth seam closed; diagnostic bytes remain open

The principal contradiction is closed. AD-5 declares that every transport,
authentication, framing, schema, identity, abnormal-exit, and pre-deadline size
failure becomes the AD-25 synthetic `invalid-output` report and never a seventh
outcome or missing scope report (`SPINE:149-165`). AD-25 supplies:

- the exhaustive stable WorkerTransportFailureV1 reason set;
- exact zero Observations and zero trusted capture bytes;
- zero duration before dispatch and exact boottime elapsed duration after it;
- `invalid-output` before the half-open deadline;
- `timed-out` at deadline equality or later;
- no generation-level CollectionAttempt failure from transport alone; and
- ordinary AD-5 completeness, current-pointer, Brief, baseline and strictness
  semantics (`SPINE:1233-1266`).

That forces the public behavior:

| Condition | Terminal report | Strict behavior | Non-strict/current behavior |
| --- | --- | --- | --- |
| Any listed failure strictly before deadline | `invalid-output` | Fails for required and optional scopes under AD-5 | One incomplete scope report remains in the latest candidate; it may move current normally, but cannot support absence/mutation and is baseline-ineligible absent audited override. |
| Same failure at deadline equality or later | `timed-out` | Fails for required and optional scopes under AD-5 | Same ordinary incomplete-current rules with timeout evidence. |
| Setup/reduction/persistence failure outside the transport mapping | Failed CollectionAttempt | Not a synthesized scope result | Prior current pointer remains unchanged and visible only as stale. |

The transport reason inventory covers every named class, but FINAL-B01 records
that reason precedence and diagnostic bytes are not yet exhaustive:

| Failure class | Required reason |
| --- | --- |
| Spawn or process-group setup | `worker-spawn` |
| Pre-request encoding | `request-encode` |
| Request over 32 MiB | `worker-request-too-large` |
| FD3 type or peer authentication | `fd-peer-auth` |
| Zero, early EOF, trailing, second, or malformed frame | `frame-invalid` |
| Canonical schema | `schema-invalid` |
| Protocol version | `version-mismatch` |
| Plan/repository/generation/scope identity | `identity-mismatch` |
| One-use channel capability | `capability-mismatch` |
| ScopeAssignmentFingerprint or assignment | `assignment-mismatch` |
| Result over its computed cap | `worker-result-too-large` |
| Valid protocol-error result | `worker-protocol-error` |
| Valid worker-error result | `worker-internal-error` |
| Exit 64, 70, 77, or any other abnormal exit without a trusted result | The inventory contains `worker-exit` and more specific semantic reasons, but does not select one when only wait status or multiple failures are observed. |
| Abnormal signal | `worker-signal` |

The remaining issue is not outcome projection; it is the bytes of the one
required DiagnosticCandidateV1. See FINAL-B01.

### RERUN-B02 — Closed

The replacement-owner sequence is now singular:

1. The new process acquires the exclusive admission lock.
2. `publish_recovery_owner` validates the unforgeable lock capability and the
   predecessor manifest checksum.
3. It refuses takeover if the prior PID still has the exact boot, birth and
   executable identity; absent PID or different birth proves a dead owner, and
   PID reuse is retained as evidence.
4. One checksummed atomic replacement appends the next gap-free attempt with
   UUID, sequence, current PID/birth/executable, lock device/inode, predecessor
   checksum and acquisition boottime.
5. Readback makes that attempt exclusively active before `resumed`, any effect,
   or validator launch.
6. A crash before publication leaves the old attempt authoritative; a crash
   after publication lets the next owner append one more attempt by the same
   rule (`SPINE:956-975`).

FD4 then binds protocol, request, capability, transaction, attempt UUID and
sequence, manifest revision/checksum, generations, candidate hash, database,
schema, backup hash, deadline and read-only mode. Peer PID/birth/executable
must equal the active attempt. A prior attempt's socket/request/capability is
invalid after publication (`SPINE:977-1008`).

The required pending-validation crashes converge:

| Crash edge | Required recovery |
| --- | --- |
| Before candidate result | Publish/read back new attempt, emit attempt-bound resumed, create fresh FD4/capability, rerun validation, then follow pre-decision rollback truth. |
| After result but before step complete | Discard the old-attempt result, publish/read back new attempt, rerun through a fresh attempt-bound FD4 exchange, then follow pre-decision rollback truth. |
| During recovery-owner publication | Prior rename-complete attempt remains authoritative; next owner retries from its checksum. |
| After new attempt publication, before resumed/effect | Next owner appends another attempt; no effect runs under the dead attempt. |
| Old PID reused | Different birth is not the old owner; reuse remains evidence and takeover proceeds under the new exact identity. |
| Forged/stale owner publication | Missing lock capability, stale predecessor, repeated sequence, or owner mismatch is refused. |

I-A and the candidate entry therefore share one owner, request, result, and
second-crash contract. I-B sees only effects admitted after that durable owner
transition.

## Earlier Seven-Finding Regression

| Finding | Final result | Evidence |
| --- | --- | --- |
| NEW-B01 — embedded accepted baseline/no late lookup | **CLOSED** | Complete immutable comparison projection is inside the atomic plan and P-B performs zero later baseline lookup (`SPINE:845-879`). |
| NEW-B02 — bounded byte-total scope assignment and oversize | **CLOSED AT ITS ORIGINAL SEAM** | Parent-only plan cuts, exact request/result identities, assignment fingerprint, byte caps and existing-outcome oversize projection remain (`SPINE:880-899`, `1233-1331`). FINAL-B01 is the narrower synthesized-diagnostic byte seam. |
| NEW-B03 — KnownGood commit-decision crash truth | **CLOSED** | Durable complete `commit-decided` is irreversible; KnownGood, ready and terminal commit follow; explicit rollback creates a new transaction (`SPINE:1059-1091`). |
| NEW-H01 — diagnostic references/ordinal/grammar | **CLOSED** | Post-evidence candidate refs, per-scope ordinals, byte grammars and atomic final rewrite remain (`SPINE:471-517`). |
| NEW-H02 — exact self set and owner winner | **CLOSED AT ITS ORIGINAL SEAM** | Exact roots/groups, descendants, escape behavior, first-ascending winner, conflicts and retained diagnostics remain (`SPINE:532-577`). FINAL-H01 concerns dispatch scheduling, not the suppression table. |
| NEW-H03 — versioned authenticated read-only bypass | **CLOSED** | Attempt-bound FD4 is versioned, peer-authenticated, one-use, read-only, no-forwarding and fail-closed across owner changes (`SPINE:956-1008`). |
| NEW-H04 — internal step/event/UX/final-result mapping | **CLOSED** | Attempt-aware events retain the complete phase table, projection rules, durable emission boundaries and four final results (`SPINE:1093-1128`). |

## TRR-H01 Barrier and Schedule Probe

### Default schedule — PASS

For `[30, 20, 15, 15, 10, 10, 10, process=10]` and four slots, ordinary LPT
assigns:

| Job | Slot | Interval |
| --- | ---: | ---: |
| 30 | 0 | 0–30 |
| 20 | 1 | 0–20 |
| 15 | 2 | 0–15 |
| 15 | 3 | 0–15 |
| 10 | 2 | 15–25 |
| 10 | 3 | 15–25 |
| 10 | 1 | 20–30 |
| process 10 | 2 | 25–35 |

The process scope is the final equal-deadline job by ScopeId order. Its barrier
has no queued successor, so both scheduling interpretations yield the stated
35-second makespan and the five-second margin yields the default 40-second
cutoff (`SPINE:812-824`).

### Pathological schedule — FAILS literal convergence

For one 60-second process scope, seven 1-second scopes, four slots and zero
margin, the spine asserts a 61-second makespan and rejection of a 60-second
cutoff (`SPINE:818-824`). That number requires this runtime behavior:

1. At epoch zero, assign process plus three short jobs to all four free slots.
2. Spawn, establish process groups, and authenticate all four one-shot workers
   before releasing any request that closes the barrier.
3. Close the gate, freeze all roots, and dispatch the epoch.
4. Three short jobs finish at second 1; their slots stay idle until the process
   cut closes at second 60.
5. At second 60, batch-fill all four free slots with the four queued short jobs;
   they finish at second 61.

AD-10 does not state that dispatch-epoch batch rule. Its literal order is also
satisfied by selecting the first LPT job, spawning/authenticating the process
worker, closing the gate before releasing it, and only then considering the
next slot. That sequential implementation runs process alone from 0–60, four
short jobs from 60–61, and the final three from 61–62. The worked 61-second
example rejects that result for one input, but it does not specify the general
same-time fill rule needed at every later scheduling epoch.

### Every process position — open at equal-time dispatch epochs

The ambiguity is observable whenever the process job is next in LPT order and
two or more slots are free at the same event time:

- a batch implementation reserves and authenticates all jobs for those free
  slots before the process request closes spawn;
- a sequential implementation closes spawn after selecting the process job and
  leaves the other simultaneously free slots idle; and
- both otherwise use descending deadline, ScopeId tie-break, earliest slot,
  worker-ID tie-break, one-shot workers, and the half-open process cut.

The named “process in every LPT position” fixture cannot derive expected
timelines until the production Rule fixes that dispatch epoch.

### Process-group descendants and escape — PASS

| Process evidence | Required treatment |
| --- | --- |
| Coordinator or authenticated worker root with exact PID/birth/device/inode | Materialized self member. |
| Provider child or grandchild retaining a frozen worker process-group ID | Materialized self member under `collection-worker-pgrp`. |
| Frozen group not yet proven empty | Retained in roots through the process cut. |
| Group proven empty before the cut | May be absent from frozen roots. |
| Descendant that calls into another process group/session | Emitted as a direct Observation unless independent exact Provider ownership suppresses it. |
| Later one-shot worker | Cannot spawn while the gate is closed. |
| Unrelated same-inode, same-PID-number, same-parent-name, or same-command process | Not self without exact root or frozen-group membership. |

The process report echoes sorted roots and exact materialized members; a
mismatch is rejected. The reducer applies only cutoff-eligible hints and keeps
all rejected/conflicting evidence (`SPINE:532-577`, `1323-1348`). No descendant
or escape choice remains once the dispatch schedule itself is fixed.

## Release Event and KnownGood Recheck — PASS

Recovery-owner publication is explicitly a manifest control transition, not a
new effect or public phase. The first `resumed` event occurs only after attempt
publication/readback and retains the pending step's existing phase. Events now
carry active attempt UUID and sequence, so a second owner cannot append an
event under a stale attempt (`SPINE:969-975`, `1093-1118`).

KnownGood still has one irreversible boundary:

- before completed `commit-decided`, recovery restores and validates the prior
  whole pair;
- after completed `commit-decided`, recovery must finish KnownGood publication,
  target ready admission, and terminal commit;
- pending/absent publication is reconstructed from the staged candidate and
  verified;
- checksum/generation/candidate mismatch is
  `upgrade-recovery-required`, never accidental older-file selection; and
- explicit rollback is a new attempt-aware transaction targeting the retained
  pair (`SPINE:1059-1091`).

Owner attempts do not alter the staged candidate, commit decision, published
record, admission generation, final result set, or public phase table. No new
event sequence, phase, skip/resume, publication, or rollback contradiction was
found.

## Final Findings

### FINAL-B01 — Synthesized worker diagnostic identity and bytes are not canonical

- **Severity:** Tier 0 / blocking
- **Affected unit pair:** C-A / C-B and persisted P-B input
- **Related closure:** RERUN-B01 and NEW-H01
- **Evidence:** `SPINE:471-517`, `1245-1266`

AD-25 requires exactly one coordinator DiagnosticCandidateV1 and fixes its
WorkerTransportFailureV1 code. It conditionally says parameters retain request
ID, exit or signal, and measured/allowed bytes. It does not fix:

- `DiagnosticSubjectV1` tag and payload;
- the stable parameter-schema version;
- whether each failure code has a different key schema or one common schema;
- the complete key set and declaration order, including tagged `absent` values;
- whether a worker-provided protocol/error code is retained;
- the precedence when one exchange observes multiple failures, such as an
  oversized result followed by coordinator termination and `worker-signal`, or
  a malformed frame followed by exit 64;
- the exact reason for exit 64, 70, or 77 when no valid result supplies the
  child's more specific failure;
- source encounter;
- duplicate occurrence; or
- the byte-complete corresponding timeout candidate referenced as “existing.”

All of those fields participate in AD-13's unsigned sort and final per-scope
DiagnosticId. One reducer can use subject `none`, code-specific parameter
objects and encounter zero; another can use ScopeId subject, one common object
with tagged absent members and a different schema token. Both satisfy AD-25's
listed retained data but produce different candidate bytes, DiagnosticIds,
Snapshot serialization and baseline comparisons.

**Smallest total closure:** Define one `WorkerTransportDiagnosticV1` candidate
schema. For example, require producer `coordinator`, exact scope subject,
parameter schema `worker-transport-failure-v1`, source encounter `0`, duplicate
occurrence `0`, and one declared-order parameter object containing request ID,
worker subcode, exit, signal, measured bytes and allowed bytes as tagged values
with `absent` where inactive. Define the timeout candidate with the same degree
of byte completeness. Add one ordered primary-reason precedence so a causal
failure outranks the signal/exit produced by coordinator cleanup, and map bare
64/70/77 statuses exactly. State that no additional parameter is permitted. Make
the transport fixtures compare complete candidate bytes and final DiagnosticId,
not only reason/outcome/public behavior.

### FINAL-H01 — Barrier-aware LPT lacks a deterministic dispatch epoch

- **Severity:** Tier 1 / high
- **Affected unit pair:** C-B scheduler / configuration admission compiler
- **Related closure:** TRR-H01 and NEW-H02
- **Evidence:** `SPINE:321-340`, `388-407`, `812-824`

The revised spine correctly makes the barrier part of the cutoff simulation,
but the simulation and runtime can still choose sequential versus batch
same-time slot filling. The explicit 61-second example implies batch filling;
the general Rule does not require it. A configuration compiler can simulate
batch epochs while the runtime coordinator dispatches sequentially and produce
a generation cutoff one second below the runtime's valid worst case.

**Smallest total closure:** Define a dispatch epoch as follows:

1. When the spawn gate is open, choose the earliest effective time at which one
   or more slots are free; after a barrier, use the barrier-close time.
2. Collect every slot free at or before that time, sorted by worker ID.
3. Assign up to that many queued scopes in frozen LPT order as one batch.
4. Spawn, establish process groups, and authenticate every worker in the batch
   before dispatching any batch request.
5. If the batch contains the process scope, close the spawn gate and freeze all
   existing plus batch roots after all authentications and before dispatch.
6. Dispatch batch requests in one named order, such as ascending worker ID.
7. While the gate is closed, completed slots remain idle. At barrier close,
   begin the next batch epoch with all then-free slots.
8. Configuration simulates those exact epochs, assuming the process Host-read
   barrier lasts its full configured scope deadline.

That rule yields 35 seconds for the default, 61 seconds for the pathological
case, and one answer for the process scope at every LPT position. The existing
named fixtures can then assert production and configuration timelines from the
same event trace.

## Pair Verdicts

| Pair | Verdict | Reason |
| --- | --- | --- |
| P-A / P-B | **ACCEPTED** | Atomic plan admission, embedded baseline input, versioned decision truth, later-write isolation and Snapshot transaction remain singular. |
| C-A / C-B | **NOT ACCEPTED** | Worker outcome/current semantics and process suppression converge, but synthetic diagnostic bytes and same-time one-shot dispatch epochs remain choices. |
| I-A / I-B | **ACCEPTED** | Attempt-bound recovery ownership, fresh FD4 validation, effect ordering, KnownGood truth and event/final-result projections converge across every requested crash. |

## Required Closure Gate

An APPROVED rerun requires only these two narrow fixes:

1. Spell the complete canonical WorkerTransportFailure and timeout diagnostic
   candidate schemas through final DiagnosticId.
2. Add the deterministic batch-fill/dispatch-epoch rule shared by runtime and
   configuration simulation.

Retain both closed rerun findings, all seven earlier findings, process-group
descendant/escape behavior, recovery-owner publication, event mapping and
KnownGood truth unchanged. No product/UX or technology-version research is
needed.

## Validation Record

| Validation | Command or method | Result |
| --- | --- | --- |
| Frozen target identity | Branch, base commit and SHA-256 before/after semantic review | **PASS** — requested branch/base and exact `66e90f...436d` digest retained. |
| Complete source read | Current 1,535-line spine through EOF; governing canonical sources verified unchanged from preceding complete read | **PASS** |
| Architecture linter | BMAD `lint_spine.py` against the architecture workspace | **PASS** — `ok: true`, zero findings. |
| AD integrity | Ordered AD heading extraction | **PASS** — AD-1 through AD-25 exactly once and in order. |
| ARCH-LIM integrity | Unique ordered ARCH-LIM extraction | **PASS** — ARCH-LIM-1 through ARCH-LIM-23 all present with no unexpected ID. |
| Schedule probes | Default, pathological, every-position/equal-time dispatch, descendant and escape interleavings | **FAIL** — exact default; pathological exposes sequential/batch divergence. |
| Crash probes | New owner, old-owner live, PID reuse, forged/stale takeover, second crash, pending validation before/after result | **PASS** |
| Markdown lint | `markdownlint-cli2` with canonical UX configuration | **PASS** — one file, zero errors. |
| Whitespace/error check | `git diff --check` plus no-index report check | **PASS** — tracked diff and untracked report emit no whitespace errors. |
| Changed-file scope | `git status --short`; report path comparison | **PASS** — this reviewer added only this final report; the spine and other prior/concurrent reports were already present and remain untouched. |

## Final Blocking Status

**BLOCKED. Verdict: CHANGES REQUIRED.** The release pair now converges and the
worker transport maps to ordinary collection truth, but C-B cannot yet produce
one canonical diagnostic or one barrier-aware runtime schedule from the frozen
Rule.
