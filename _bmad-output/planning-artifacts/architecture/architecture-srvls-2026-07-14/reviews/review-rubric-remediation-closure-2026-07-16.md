---
title: "srvls Architecture Remediation Closure Good-Spine Gate"
document_type: architecture_review
review_dimension: good_spine_remediation_closure
status: final
verdict: approved
blocking: false
review_date: 2026-07-16
reviewer: rubric-gate
reviewed_base_commit: d4515067af8314cadf979da7b17921fbafc92d21
reviewed_worktree_spine_sha256: 29c1078802abaa66abb391d4257f3cd952d6905fc9bf11d1bcd85f9b773fb76a
reviewed_worktree_patch_id: b5bb07ff370089e3574508e1183797273512dec9
reviewed_spine_line_count: 1588
reviewed_artifact: _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md
finding_count: 0
blocking_findings: 0
high_findings: 0
moderate_findings: 0
---

<!-- markdownlint-disable MD013 MD025 -->

# srvls Architecture Remediation Closure Good-Spine Gate

## Verdict

**APPROVED.** The newly frozen architecture candidate at exact SHA-256
`29c1078802abaa66abb391d4257f3cd952d6905fc9bf11d1bcd85f9b773fb76a`
has zero blocking, high, or moderate findings. It closes every original
technology, two-unit divergence, and rubric-acceptance finding; every prior
remediation-gate finding; and the two findings from the final rerun. The
complete BMAD good-spine walker found no new contradiction, divergent owner,
unconstructible boundary, or untestable recovery branch.

This approval is for the frozen candidate only. It does not finalize the
architecture: the spine correctly remains `status: draft` (`SPINE:1-10`).

## Review Basis

Citation keys:

- `SPINE` —
  `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md`
- `MEMLOG` — the complete sibling `.memlog.md`
- `PRD` —
  `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md`
- `ADD` — the canonical PRD `addendum.md`
- `DESIGN` — the canonical UX `DESIGN.md`
- `EXPERIENCE` — the canonical UX `EXPERIENCE.md`
- `TECH-ACC` — `reviews/review-technology-acceptance-2026-07-16.md`
- `DVG-ACC` — `reviews/review-two-unit-divergence-acceptance-2026-07-16.md`
- `RUBRIC-ACC` — `reviews/review-rubric-acceptance-2026-07-16.md`
- `FIRST-GATE` — `reviews/review-rubric-remediation-gate-2026-07-16.md`
- `RERUN` — `reviews/review-rubric-remediation-rerun-2026-07-16.md`
- `FINAL-GATE` — `reviews/review-rubric-remediation-final-2026-07-16.md`

The complete current 1,588-line spine was read at the frozen hash. The complete
BMAD architecture skill, headless rules, reviewer gate, memlog, canonical
PRD/addendum, DESIGN, EXPERIENCE, all three source acceptance reports, and all
prior rubric remediation reports were read as the controlling review set. The
review walked Rules, limits, verification fixtures, release and state-machine
transitions, structural ownership, trace rows, Seed, and Deferred. This is a
semantic cross-unit review, not a requested-word presence check.

## Good-Spine Checklist

| Check | Result | Binding evidence |
| --- | --- | --- |
| Real divergence points one level down are fixed | **PASS** | Frozen collection admission, FD3 worker execution, diagnostic allocation, process ownership, SQLite initialization, and release recovery each have one named owner and one total transition (`SPINE:316-451`, `SPINE:485-716`, `SPINE:856-1402`). |
| Every AD Rule is enforceable and prevents its stated divergence | **PASS** | Each Rule names observable inputs, ordering, typed outcomes, and deterministic fixtures; the architecture linter reports zero findings. |
| Deferred cannot permit incompatible v1 stories | **PASS** | Every deferred item preserves a decided v1 boundary and names a later trigger (`SPINE:1568-1588`). |
| Named technology is verified-current | **PASS** | The accepted 2026-07-16 stack remains exact, including glibc 2.42 ABI and oldest-runtime gates (`SPINE:452-484`, `SPINE:1432-1454`). |
| Brownfield behavior is ratified rather than contradicted | **PASS** | Raw routing, legacy arity and presenters, current output contracts, and the compatibility corpus remain outward adapters rather than alternate domain owners (`SPINE:244-315`, `SPINE:395-450`). |
| Canonical PRD and UX capabilities land semantically | **PASS** | Capability and canonical-contract trace tables retain every PRD, journey, success-measure, and UX family (`SPINE:1526-1566`). |
| No AD weakens or contradicts another | **PASS** | AD-5 completeness, AD-10 batch epochs, AD-13 identity, AD-16 persistence, AD-21 truth cuts, AD-23 recovery, AD-24 bytes, and AD-25 transport compose without a second owner. |
| Deployment and environment envelope is decided | **PASS** | Exact artifact ABI proof, oldest-runtime smoke, managed consumer/timer validation, one-Host scope, and whole-pair recovery are binding (`SPINE:452-484`, `SPINE:954-1154`, `SPINE:1404-1414`). |
| Provider and operational strategy is decided | **PASS** | One-shot workers, batch dispatch epochs, process-group ownership, deadlines, output caps, and exact worker request/result validation are total (`SPINE:316-393`, `SPINE:806-854`, `SPINE:1243-1402`). |
| State integrity and recovery are decided | **PASS** | Ordered SQLite readbacks, one atomic collection admission, crash-persistent release admission, checksummed effect journal, recovery ownership, KnownGood, and rollback are explicit (`SPINE:647-716`, `SPINE:856-927`, `SPINE:954-1154`). |
| Security is decided at feature altitude | **PASS** | FD3 and FD4 peer/executable authentication, one-time capabilities, no-follow paths, least privilege, and pre-SQLite recovery gating fail closed (`SPINE:605-625`, `SPINE:966-1048`, `SPINE:1243-1402`). |
| Accessibility is decided | **PASS** | Text-primary meaning, terminal ownership, complete linear output, and canonical UX acceptance remain binding (`SPINE:244-289`, `SPINE:605-625`, `SPINE:1404-1414`, `SPINE:1547-1566`). |
| Structural Seed is minimal and code-owned | **PASS** | The Seed is one implementation-shaped ownership map, not a second normative model (`SPINE:1456-1508`). |
| Status and finalization discipline are correct | **PASS** | The spine remains draft; this report approves the candidate without marking the architecture final (`SPINE:1-10`). |

## Original Acceptance-Finding Closure Matrix

### Technology acceptance

| Finding | Result | Current binding closure |
| --- | --- | --- |
| T0-A — managed unit rewrite and timer success postconditions | **CLOSED** | Every managed absolute `ExecStart`, explicitly including `srvls-metrics.service` and `srvls-snapshot.service`, is rewritten and read back after reload; each paired timer must advance and its service must report success; any failure restores and proves the whole prior pair (`SPINE:467-481`, `SPINE:1073-1083`). |
| T1-A — ordered SQLite pragma initialization and readback | **CLOSED** | Fresh and existing databases both require WAL, then every connection reads WAL, sets and reads `synchronous=FULL` as `2`, sets and reads foreign keys as `1`, and sets busy timeout before any transaction (`SPINE:653-665`). |
| T2-A — glibc support ABI gate | **CLOSED** | Release CI runs `readelf --version-info` on the exact final artifact, rejects any import beyond `GLIBC_2.42`, and smokes that same artifact in the pinned oldest-supported glibc 2.42 runtime (`SPINE:457-466`). |

### Two-unit divergence acceptance

| Finding | Result | Current binding closure |
| --- | --- | --- |
| ACC-B01 — Accepted Baseline omitted from the frozen cut | **CLOSED** | AcceptedBaselineCutV1 freezes tagged `none` or `accepted` and embeds the complete immutable identity-sorted comparison projection (`SPINE:862-886`). |
| ACC-B02 — nonterminal operations omitted from the frozen cut | **CLOSED** | OperationCutV1 freezes repository revision plus every nonterminal OperationId, exact target, and phase (`SPINE:887-888`). |
| ACC-B03 — release quiescence evaporates on crash | **CLOSED** | ReleaseAdmissionV1 durably persists `recovering`; every stateful entry gates before SQLite and only release recovery may restore `ready` (`SPINE:966-980`). |
| ACC-B04 — no single policy fingerprint byte stream | **CLOSED** | CanonicalJsonV1 and byte-complete PolicySnapshotV1 define one ordered effective-policy stream and domain-separated fingerprint (`SPINE:1169-1201`). |
| ACC-H01 — noncanonical Scope identity | **CLOSED** | ScopeIdV1 has fixed tags, field encodings, raw-path normalization and rejection, display encoding, manifest order, and fingerprint bytes (`SPINE:1218-1236`). |
| ACC-H02 — diagnostic ordinals unconstructible | **CLOSED** | Candidates are created only after evidence, locally sorted into refs, merged after the evidence cut, assigned once per scope, and atomically rewritten before persistence (`SPINE:497-543`). |
| ACC-H03 — deduplication lacks a decision contract | **CLOSED** | Exact process hints, self suppression, strength/provider/Scope ordering, conflict retention, selected ownership, and incomplete-evidence emission are deterministic (`SPINE:558-603`). |
| ACC-H04 — historical resource samples outside the frozen cut | **CLOSED** | ResourceHistoryCutV1 freezes revision and sorted eligible immutable samples; admission pins them and later history changes affect only the next generation (`SPINE:889-903`). |
| ACC-H05 — collection request creation is not atomic | **CLOSED** | One repository `admit_collection` executes under one `BEGIN IMMEDIATE`, inserts the complete plan and pins, advances latest requested, or commits none (`SPINE:862-905`). |
| ACC-H06 — upgrade journal tears or crosses effects | **CLOSED** | Every manifest is checksummed atomic replacement; every effect is preceded by durable `pending` and followed only after required readback by durable `complete` (`SPINE:1036-1071`). |
| ACC-H07 — successful validation can erase rollback target | **CLOSED** | Commit decision precedes atomic KnownGood publication; successful commit retains exactly one pinned KnownGoodReleaseV1 and never deletes it (`SPINE:1085-1117`). |
| ACC-M01 — collection wall time has no sample boundary | **CLOSED** | CollectionPlanV1 carries one paired boot/UTC wall ClockSampleV1; the frozen UTC sample stamps all public collection time and later samples are diagnostic-only (`SPINE:862-866`, `SPINE:920-924`, `SPINE:1203-1216`). |
| ACC-M02 — release phases are not mapped through recovery | **CLOSED** | Every durable internal step maps to one public phase and UX label; persisted event state maps to public state; recovery emits `resumed` plus one of four total terminal results (`SPINE:1119-1154`). |

### Rubric acceptance

| Finding | Result | Current binding closure |
| --- | --- | --- |
| NEW-B-1 — baseline and history absent from frozen truth | **CLOSED** | AcceptedBaselineCutV1, ResourceHistoryCutV1, prior current, Promise and operation cuts, revision, policy, scopes, and one paired clock are admitted and fingerprinted together (`SPINE:862-924`, `SPINE:1203-1216`). |
| NEW-B-2 — same-binary worker lacks route and wire | **CLOSED** | Reserved `__srvls-worker-v1` routing authenticates the exact binary over FD3; framing, sizes, request, result, capture isolation, exits, timeout, signals, mismatches, and no-discovery behavior are versioned and total (`SPINE:1243-1402`). |
| NEW-M-1 — UJ-5 omits hot-history owners | **CLOSED** | UJ-5 now names AD-5, AD-16, AD-18, and AD-20–AD-21, exact duplicate evidence, and retained timestamped resource history (`SPINE:1545`). |

## Prior Remediation-Gate Closure Audit

| Finding | Result | Current binding closure |
| --- | --- | --- |
| GATE-B01 — complete baseline comparison input | **CLOSED** | Baseline rows contain every Promise, Observation, and Finding comparison field plus fingerprints and governing versions; no later baseline lookup is permitted (`SPINE:871-905`). |
| GATE-B02 — request/result plan identity | **CLOSED** | CollectionPlanFingerprint, repository revision, generation, ScopeId, and ScopeAssignmentFingerprint bind request, recomputation, result echo, and byte-equality admission (`SPINE:907-920`, `SPINE:1320-1384`). |
| GATE-H01 — diagnostic byte grammar and post-evidence allocation | **CLOSED** | Subject and parameter grammars are byte-complete; encounter, duplicates, local references, final merge, rewrite, and invalid-reference rejection are total (`SPINE:497-543`). |
| GATE-H02 — process-owner winner direction | **CLOSED** | The selected owner is the first item after explicit ascending strength, Provider tag, and unsigned ScopeId bytes; all conflicts and rejected hints remain evidence (`SPINE:576-603`). |
| GATE-M01 — oversize request/result disposition | **CLOSED** | Exact-bound request and result limits are defined; one-byte-over input is neither sent nor allocated, never truncated, and becomes one synthesized report with measured and allowed bytes (`SPINE:1259-1280`, `SPINE:1297-1318`). |

## Final-Finding Closure Proof

### FINAL-M01 — total transport-failure precedence and byte-complete diagnostic

**CLOSED.** AD-25 now makes every transport branch produce exactly one complete
AD-5 CollectorReportV1, never a seventh outcome or generation-level failure
(`SPINE:1271-1280`, `SPINE:1315-1318`). The report preserves the frozen
generation, Scope, and obligation; contains zero Observations and zero trusted
capture bytes; uses zero duration before an epoch or exact boot-nanosecond
elapsed duration after dispatch; and imports no untrusted partial result.

Primary reason selection is total and first-match (`SPINE:1282-1295`):

1. At deadline equality or later, `worker-timeout` wins over every other fact
   and the outcome is `timed-out`.
2. Before the deadline, the first present reason is selected in this exact
   order: `worker-spawn`, `request-encode`, `worker-request-too-large`,
   `fd-peer-auth`, `worker-result-too-large`, `frame-invalid`, `schema-invalid`,
   `version-mismatch`, `identity-mismatch`, `capability-mismatch`,
   `assignment-mismatch`, `worker-protocol-error`, `worker-internal-error`,
   `worker-signal`, `worker-exit`; the outcome is `invalid-output`.
3. With no earlier evidence, bare exits 77, 64, and 70 normalize to peer-auth,
   frame, and internal failure; another nonzero exit or signal uses its named
   fallback.
4. Parent-cleanup exit or signal remains secondary evidence and cannot replace
   the parser, size, identity, or trusted-result cause that triggered cleanup.

Every such report owns exactly one `WorkerTransportDiagnosticV1` candidate
(`SPINE:1297-1313`). Its complete identity is coordinator producer `0x00`, the
actual report ScopeId, code equal to the primary reason, schema token
`worker-transport-diagnostic-v1`, subject bytes `0x01 || 0x01 || length:u32be ||
ScopeIdV1`, source encounter `0`, and duplicate occurrence `0`. Its parameter
object has exactly these ordered tagged keys and no others:

| Key | Tagged type and presence rule |
| --- | --- |
| `request_id` | `id`, always present because allocation precedes spawn |
| `worker_subcode` | tagged `absent` or `text`; text only from a trusted typed worker result |
| `exit_code` | tagged `absent` or `u64`; retains observed wait evidence |
| `signal` | tagged `absent` or `u64`; retains observed wait evidence |
| `termination_origin` | tagged text token `none`, `parent-cleanup`, or `worker` |
| `measured_bytes` | tagged `absent` or `u64`; present only for measured size evidence |
| `allowed_bytes` | tagged `absent` or `u64`; present only for measured size evidence |

Inactive fields use tagged `absent`; timeout uses the same schema. AD-13 then
performs the sole local sort, reference rewrite, and final per-scope DiagnosticId
allocation. Combined fixtures explicitly cover malformed-frame plus exit 64,
oversize plus parent-cleanup signal, and trusted worker-error plus exit 70, and
assert the complete report, candidate bytes, final ID, precedence, current
pointer, Brief, and strict-mode effects (`SPINE:423-433`). There is no remaining
implementation choice about outcome, primary cause, secondary evidence,
diagnostic bytes, or completeness propagation.

### FINAL-M02 — deterministic batch spawn/authentication dispatch epochs

**CLOSED.** Runtime and configuration now consume the same explicit
dispatch-epoch transition (`SPINE:316-361`):

1. Choose the earliest effective open-gate time and collect every then-free slot
   in ascending worker-ID order.
2. Take one batch from the frozen LPT queue and spawn, establish process groups,
   and authenticate every batch worker before dispatching any request.
3. If the process Scope is in the batch, close the spawn gate and freeze all
   existing and batch self roots only after all batch authentication and before
   any request.
4. Capture one `dispatch_epoch_boot_ns`, dispatch in worker-ID order, and derive
   every absolute deadline from that shared epoch.
5. While the process Host-read gate is closed, live workers continue but
   completed slots stay idle. Reopen at the half-open process cut and form the
   next batch from every then-free slot.

Every batch spawn/authentication is attempted before the epoch; failed members
receive their synthesized AD-25 report, authenticated members still dispatch,
and the process gate closes only for an authenticated process member
(`SPINE:343-349`). Scope time, queue time, and spawn-barrier time are explicitly
owned, while configuration runs the same barrier-aware event simulation
(`SPINE:351-361`).

| Oracle | Deterministic epoch trace | Result |
| --- | --- | --- |
| Default deadlines `[30,20,15,15,10,10,10,10]`, four workers | Frozen LPT batches place the process Scope as the final equal-10-second dispatch; no queued successor exists behind its gate | exact makespan 35 s; plus 5 s margin = 40 s cutoff (`SPINE:843-848`) |
| Process 60 s plus seven 1 s Scopes, four workers, zero margin | Epoch 0 dispatches process plus three 1 s workers; those three idle behind the process gate until t=60; epoch 1 dispatches the remaining four Scopes | exact makespan 61 s; a 60 s cutoff is rejected (`SPINE:848-850`) |

Cross-unit fixtures require runtime and configuration to compare the same batch
assignment, authentication, root-freeze, epoch, barrier, and completion trace,
including the pathological schedule, every process LPT position, and
near-deadline Host reads (`SPINE:409-416`). The prior sequential 62-second
interpretation is no longer permitted.

## Preserved Contracts and Required Fixture Coverage

| Contract | Result | Binding evidence |
| --- | --- | --- |
| Six collection outcomes and one terminal report per frozen Scope | **PRESERVED** | AD-5 retains exactly six outcomes, half-open deadlines, no stale carry-forward, and current-pointer CAS (`SPINE:143-178`). |
| Process ownership, self suppression, and retained conflicts | **PRESERVED** | Exact PID/birth and group membership govern suppression; escaped descendants emit; weak hints never suppress; all rejected hints and conflicts persist (`SPINE:558-603`). |
| Crash-persistent pre-SQLite release gate | **PRESERVED** | Every stateful entry fails closed before SQLite unless admission is ready and no transaction is nonterminal (`SPINE:966-980`). |
| Recovery ownership, PID reuse, second recovery crash, and FD4 attempt binding | **PRESERVED** | Gap-free owner publication, old-owner liveness, PID-reuse evidence, repeated takeover, active-attempt peer identity, and fresh attempt capability are total (`SPINE:982-1034`). |
| Checksummed atomic effects and recovery | **PRESERVED** | Atomic replacement, file and directory fsync, pending-before-effect, complete-after-readback, may-have-executed recovery, and no phase-name inference remain explicit (`SPINE:1036-1071`). |
| KnownGood and explicit rollback | **PRESERVED** | Exactly one KnownGoodReleaseV1 is pinned after commit; rollback is a new UpgradeTransactionV1 using the same protocol (`SPINE:1085-1117`). |
| Public release events and terminal results | **PRESERVED** | Internal phases, UX labels, durable event states, recovery results, and four terminal machine results remain total (`SPINE:1119-1154`). |
| Canonical policy, plan, Scope, and diagnostics | **PRESERVED** | CanonicalJsonV1, complete PolicySnapshotV1, CollectionPlanV1 field order, ScopeIdV1 bytes, and post-evidence diagnostic grammar remain byte-complete (`SPINE:497-543`, `SPINE:1156-1236`). |
| Required property, concurrency, crash, IPC, timer, and rollback fixtures | **PRESERVED** | AD-11 names byte properties, diagnostic/process ownership properties, admission and LPT races, FD3 boundaries and mismatches, SQLite/crash/recovery edges, ABI proof, every managed unit/timer check, whole-pair rollback, and KnownGood rollback (`SPINE:395-450`). |
| UJ-5 and related traces | **PRESERVED** | UJ-5 names exact duplicate evidence and retained timestamped history; capability, success-measure, UX, and limit traces remain complete (`SPINE:1526-1566`). |
| Seed and Deferred discipline | **PRESERVED** | Seed remains implementation-shaped; Deferred retains only post-v1 triggers without reopening a v1 decision (`SPINE:1456-1508`, `SPINE:1568-1588`). |

## Mechanical Validation Record

All commands ran from the review worktree against the candidate named in this
report.

| Command or check | Result |
| --- | --- |
| `sha256sum .../ARCHITECTURE-SPINE.md` | **PASS** — `29c1078802abaa66abb391d4257f3cd952d6905fc9bf11d1bcd85f9b773fb76a` |
| `wc -l .../ARCHITECTURE-SPINE.md` | **PASS** — 1,588 lines |
| `uv run .agents/skills/bmad-architecture/scripts/lint_spine.py --workspace _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14` | **PASS** — `ok: true`, zero findings |
| `git diff --check` | **PASS** — no whitespace errors |
| Stable patch-ID over the spine diff | **PASS** — `b5bb07ff370089e3574508e1183797273512dec9` on base `d4515067af8314cadf979da7b17921fbafc92d21` |
| AD definition and reference walk | **PASS** — 25 unique contiguous definitions and references `AD-1..AD-25`; no out-of-range identifier |
| ARCH-LIM definition and reference walk | **PASS** — 23 unique contiguous definitions and references `ARCH-LIM-1..ARCH-LIM-23`; no out-of-range identifier |
| Requested-term and diff inspection | **PASS** — every acceptance term resolves to a normative Rule or named fixture; no source report, task file, or product code is part of this candidate diff |
| Markdown lint on this closure report | **PASS** — project configuration, zero findings |

## Closure

The exact frozen candidate has **zero findings**. All original acceptance and
all prior rerun/final findings are closed without weakening any already-closed
contract. The BMAD architecture remediation closure gate is **APPROVED**; the
architecture spine remains intentionally draft.
