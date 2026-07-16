---
title: "srvls Architecture Remediation Reality Closure Good-Spine Gate"
document_type: architecture_review
review_dimension: good_spine_remediation_reality_closure
status: final
verdict: changes-required
blocking: true
review_date: 2026-07-16
reviewer: rubric-gate
reviewed_base_commit: d4515067af8314cadf979da7b17921fbafc92d21
reviewed_worktree_spine_sha256: 03b539cc80e98b7dac436360b324cb6e6f925a95e775571343b84b9cf2756a55
reviewed_worktree_patch_id: 466f877adf3c99e4f0577d4c7e6a17a562aca747
reviewed_spine_line_count: 1710
reviewed_artifact: _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md
finding_count: 1
blocking_findings: 1
high_findings: 0
moderate_findings: 0
---

<!-- markdownlint-disable MD013 MD025 -->

# srvls Architecture Remediation Reality Closure Good-Spine Gate

## Verdict

**CHANGES REQUIRED.** The exact frozen candidate at SHA-256
`03b539cc80e98b7dac436360b324cb6e6f925a95e775571343b84b9cf2756a55`
preserves every original acceptance closure and makes the Hello/Ready protocol,
pre-spawn budget, and transport evidence matrix substantially more precise. One
blocking process-ownership seam still prevents approval: the transport matrix
admits process-group/setup failure after a child exists, but SelfProcessSetV1
permits a worker root only after the dedicated group and all exact identity
fields are recorded. Cleanup may still be pending when a Ready process worker
is dispatched, leaving the failed child with no constructible self root.

The gate requires zero blocking, high, or moderate findings. The spine remains
correctly marked `status: draft` (`SPINE:1-10`).

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
- `CLOSURE-GATE` — `reviews/review-rubric-remediation-closure-2026-07-16.md`

The complete current 1,710-line spine was read at the frozen hash. The complete
BMAD architecture skill, headless rules, reviewer gate, memlog, canonical
PRD/addendum, DESIGN, EXPERIENCE, three source acceptance reports, and prior
remediation reports form the controlling review set. The walker replayed every
finding and tested the new handshake, root eligibility, dispatch timing,
half-open admission, and transport parameter/evidence-cut matrix as executable
state transitions. This is a semantic cross-unit gate, not a term-presence
review.

## Good-Spine Checklist

| Check | Result | Binding evidence |
| --- | --- | --- |
| Real divergence points one level down are fixed | **FAIL — BLOCKING** | REALITY-B01 permits wait-for-cleanup and dispatch-now implementations to collect different direct-process truth from the same spawned child. |
| Every AD Rule is enforceable and prevents its stated divergence | **FAIL — BLOCKING** | The Hello/Ready, timing, and diagnostic rules are enforceable, but one admitted post-spawn setup branch cannot construct the exact self root AD-10 requires. |
| Deferred cannot permit incompatible v1 stories | **PASS** | Every Deferred item preserves one v1 choice and names a later trigger (`SPINE:1690-1710`). |
| Named technology is verified-current | **PASS** | Exact 2026-07-16 stack targets, glibc ABI proof, and oldest-runtime smoke remain binding (`SPINE:482-506`, `SPINE:1554-1576`). |
| Brownfield behavior is ratified rather than contradicted | **PASS** | Raw routing, legacy arity and presenters, the Python oracle, and deployed consumer checks remain isolated compatibility contracts (`SPINE:244-315`, `SPINE:411-475`). |
| Canonical PRD and UX capabilities land semantically | **PASS WITH ONE BLOCKING OWNERSHIP SEAM** | Capability and trace tables cover the source set; REALITY-B01 affects deterministic worker self-observation rather than capability presence (`SPINE:1648-1688`). |
| No AD weakens or contradicts another | **FAIL — BLOCKING** | AD-10 says every spawned failed worker remains in SelfProcessSetV1, while AD-13 cannot construct that root for the AD-25 after-spawn group/setup failure branch. |
| Deployment and environment envelope is decided | **PASS** | ABI, managed consumer/timer validation, one-Host scope, release admission, and whole-pair recovery remain binding (`SPINE:482-506`, `SPINE:987-1188`, `SPINE:1526-1545`). |
| Provider and operational strategy is decided | **FAIL — BLOCKING** | Setup-failed child eligibility is not total across scheduler, self-set, and transport Rules (`SPINE:316-409`, `SPINE:583-618`, `SPINE:1277-1524`). |
| State integrity and recovery are decided | **PASS** | SQLite readbacks, atomic collection admission, crash-persistent release gating, checksummed effects, KnownGood, and rollback remain total (`SPINE:677-746`, `SPINE:887-986`, `SPINE:987-1188`). |
| Security is decided at feature altitude | **PASS** | Hello/Ready authenticates both directions with exact executable, peer, spawn, credentials, capability, and deadline evidence; FD4 and no-follow release controls remain unchanged (`SPINE:999-1067`, `SPINE:1277-1337`). |
| Accessibility is decided | **PASS** | Text-primary meaning, terminal ownership, linear output, and the canonical UX acceptance Host remain binding. |
| Structural Seed is minimal and code-owned | **PASS** | The Seed remains one implementation ownership map rather than a second normative model (`SPINE:1578-1630`). |
| Status and finalization discipline are correct | **PASS** | The spine remains draft and no review marks it final (`SPINE:1-10`). |

## Original and Prior-Finding Closure Audit

### Technology acceptance

| Finding | Result | Current binding closure |
| --- | --- | --- |
| T0-A — managed unit rewrite and timer postconditions | **CLOSED** | Every managed absolute ExecStart, including both named srvls services, is read back after reload; paired timer advance and successful service result are mandatory; failure restores and proves the whole pair (`SPINE:492-506`, `SPINE:1106-1116`). |
| T1-A — ordered SQLite pragma readback | **CLOSED** | Fresh and existing databases require WAL, FULL as numeric 2, foreign keys as 1, and busy timeout before any transaction (`SPINE:677-695`). |
| T2-A — exact glibc ABI gate | **CLOSED** | The final artifact receives the readelf GLIBC_2.42 import gate and oldest-supported runtime smoke (`SPINE:482-491`). |

### Two-unit divergence acceptance

| Finding | Result | Current binding closure |
| --- | --- | --- |
| ACC-B01 — Accepted Baseline absent from the frozen cut | **CLOSED** | AcceptedBaselineCutV1 embeds the complete identity-sorted comparison projection (`SPINE:893-938`). |
| ACC-B02 — nonterminal operations absent from the frozen cut | **CLOSED** | OperationCutV1 freezes repository revision, exact target, and durable phase for every nonterminal operation (`SPINE:919-921`). |
| ACC-B03 — release quiescence evaporates on crash | **CLOSED** | ReleaseAdmissionV1 gates every stateful entry before SQLite and persists recovery state across process death (`SPINE:999-1013`). |
| ACC-B04 — no single policy fingerprint stream | **CLOSED** | CanonicalJsonV1 and PolicySnapshotV1 define one byte-complete effective-policy stream and fingerprint (`SPINE:1201-1234`). |
| ACC-H01 — Scope identity not canonical | **CLOSED** | ScopeIdV1 tags, fields, paths, display, manifest sorting, and fingerprinting remain total (`SPINE:1252-1272`). |
| ACC-H02 — diagnostic ordinals not constructible | **CLOSED** | Candidates are created after evidence, locally referenced, globally sorted, assigned once per Scope, and atomically rewritten (`SPINE:522-568`). |
| ACC-H03 — process deduplication lacks a decision contract | **CLOSED EXCEPT NEW ROOT-ELIGIBILITY SEAM** | Exact ownership order, conflicts, weak-evidence refusal, and retained suppression evidence remain closed (`SPINE:606-633`); REALITY-B01 concerns whether a failed internal child can enter the self-root input at all. |
| ACC-H04 — resource history outside the frozen cut | **CLOSED** | ResourceHistoryCutV1 freezes and pins the eligible immutable samples (`SPINE:922-938`). |
| ACC-H05 — collection admission not atomic | **CLOSED** | One repository operation performs the entire plan admission under one BEGIN IMMEDIATE or commits none (`SPINE:887-947`). |
| ACC-H06 — upgrade journal can tear across effects | **CLOSED** | Checksummed same-directory atomic replacement plus pending-before and complete-after readback ordering remains explicit (`SPINE:1069-1104`). |
| ACC-H07 — validation can erase rollback target | **CLOSED** | Commit decision precedes publication and every successful commit retains exactly one KnownGoodReleaseV1 (`SPINE:1118-1150`). |
| ACC-M01 — collection wall sample has no boundary | **CLOSED** | CollectionPlanV1 carries the paired boot/UTC sample and absolute generation cutoff; later wall samples are diagnostic-only (`SPINE:893-898`, `SPINE:956-968`, `SPINE:1236-1250`). |
| ACC-M02 — recovery phases lack public mapping | **CLOSED** | Durable steps, public phases, UX labels, resumed recovery, and four terminal machine results remain total (`SPINE:1152-1188`). |

### Rubric acceptance and remediation gates

| Finding | Result | Current binding closure |
| --- | --- | --- |
| NEW-B-1 — baseline and history omitted from frozen truth | **CLOSED** | Baseline, operations, history, prior current, Promise, policy, Scope, revision, and paired clock are fingerprinted in one plan (`SPINE:887-968`, `SPINE:1236-1250`). |
| NEW-B-2 — same-binary worker has no route or wire | **CLOSED** | Reserved routing and the four-frame authenticated FD3 protocol define Hello, Ready, Request, Result, stdio isolation, exits, signals, timeouts, mismatches, and no discovery (`SPINE:244-268`, `SPINE:1277-1524`). |
| NEW-M-1 — UJ-5 omits hot-history owners | **CLOSED** | UJ-5 names exact duplicate evidence and retained timestamped history under AD-5, AD-16, AD-18, and AD-20–AD-21 (`SPINE:1667`). |
| GATE-B01 — baseline comparison input incomplete | **CLOSED** | The embedded projection contains all comparison rows and versions and permits zero later baseline lookup (`SPINE:904-938`). |
| GATE-B02 — request/result plan identity incomplete | **CLOSED** | Plan and assignment fingerprints, revision, generation, Scope, deadlines, and reservations bind Request recomputation and Result admission (`SPINE:944-953`, `SPINE:1435-1505`). |
| GATE-H01 — diagnostic byte grammar incomplete | **CLOSED** | Subject, parameter, encounter, duplicate, local-reference, merge, and rewrite bytes remain total (`SPINE:522-568`). |
| GATE-H02 — process-owner winner has no direction | **CLOSED** | First-after-ascending strength, Provider, and Scope order remains explicit and retains every conflict (`SPINE:606-633`). |
| GATE-M01 — oversize request/result has no disposition | **CLOSED** | Exact caps, no truncation, measured size rows, and synthesized report behavior remain explicit (`SPINE:1293-1301`, `SPINE:1333-1337`, `SPINE:1392-1415`). |
| FINAL-M01 — transport precedence and diagnostic bytes incomplete | **CLOSED** | Deadline-first cause selection, FD3-before-wait classification, immutable failure cut, exhaustive seven-parameter matrix, and separate reaper evidence are total (`SPINE:1339-1433`). |
| FINAL-M02 — batch dispatch epoch unstated | **CLOSED** | Batch membership, continuous earliest-free epochs, pre-spawn budget, concurrent Ready barrier, root freeze, request order, and half-open headroom are explicit (`SPINE:321-377`, `SPINE:847-881`). |

## Reality Stress Matrix

| Targeted seam | Result | Conclusion |
| --- | --- | --- |
| Hello/Ready framing and bidirectional authentication | **PASS** | Four frame directions are fixed; child proves the parent with SO_PEERCRED and executable identity; parent proves the child with owned PID/birth, executable, group, one Ready capability echo, and exactly one first-byte SCM_CREDENTIALS record (`SPINE:1277-1326`). |
| Ready replay, silence, exit 77, malformed credentials, and field mismatch | **PASS** | Each branch is strict-before both deadlines and maps to peer-authentication failure or deadline-first timeout without Host work (`SPINE:1319-1337`, `SPINE:1350-1377`). |
| Pre-spawn total scope budget | **PASS** | Epoch, capability, and deadlines precede spawn; setup, handshake, transfer, work, and failure all consume one scope budget (`SPINE:326-365`). |
| Dispatch timing and half-open cutoff | **PASS** | Step 1 continuously starts an epoch on the earliest free open-gate slots; runtime/configuration replay the same per-scope cuts and process barrier; exact makespan plus the greater of margin and one nanosecond prevents equality admission (`SPINE:321-377`, `SPINE:847-881`). |
| Spawned-root eligibility after Ready failure | **PASS WHEN ROOT FIELDS EXIST** | A spawned worker with exact PID/birth/executable/group stays frozen even when Ready fails or times out (`SPINE:583-597`). |
| Spawned-root eligibility after process-group/setup failure | **FAIL — BLOCKING** | The matrix admits an after-spawn failure before the dedicated group/root tuple is constructible, but process Host-read does not wait for absence proof. |
| Transport primary cause and evidence cut | **PASS** | Deadline wins first; frame classification precedes wait status; zero-byte EOF joins status; partial EOF fails immediately; trusted error results freeze their own cut; cleanup cannot mutate the candidate (`SPINE:1350-1377`). |
| Exhaustive diagnostic parameters | **PASS** | All seven keys, direct-wait exclusivity, exact two size rows, timeout variants, termination origin, and WorkerReapEvidence separation are complete (`SPINE:1379-1428`). |
| Completeness and public truth after transport failure | **PASS** | One synthesized six-outcome report participates in normal current-pointer, Brief, baseline, and strictness rules (`SPINE:1430-1433`). |

## Tier 0 — Blocking Finding

### REALITY-B01 — Post-spawn setup failure can leave a live child with no eligible self root

AD-13 creates `SpawnedWorkerRootV1` only after the parent has recorded the
child's PID, birth, executable identity, and dedicated process group
(`SPINE:583-597`). AD-25 separately admits
`process-group/setup fails after spawn` and immediately freezes a
`worker-spawn` diagnostic whose cleanup status is deferred to
WorkerReapEvidenceV1 (`SPINE:1392-1425`). The contract therefore permits a
child PID to exist while one of the fields required to create its root is
precisely the failed setup result.

Consider the second default batch, where a Ready process worker shares the
batch with another worker whose group setup fails after child creation. The
failed member is terminal for the batch, so AD-10 proceeds to root freeze and
dispatch. Parent cleanup need not yet have proved that PID or group absent.
Because no valid dedicated-group root exists, the process request cannot carry
that internal child in SelfProcessSetV1. The direct-process scan may emit it;
an implementation that happens to wait for reap may not. Recording the
inherited coordinator group instead is unsafe because it would suppress
unrelated exact members of a non-dedicated group.

Required closure: make dedicated-group and exact-root creation atomic with
spawn so failure returns no live child, define a safe exact-PID root variant
that is constructible before group proof, or prohibit process Host-read until
every unrootable spawned PID is proved absent. Add a fixture with an
after-child group/setup failure, pending cleanup, and a Ready process member in
the same batch; assert that the internal child can neither leak into an
Observation nor cause unrelated group suppression.

## Preserved Contracts

| Contract | Result | Binding evidence |
| --- | --- | --- |
| Six outcomes and one report per Scope | **PRESERVED** | AD-5 retains complete, partial, unavailable, denied, timed-out, and invalid-output only, with one terminal report per frozen Scope (`SPINE:143-178`). |
| Frozen baseline, operation, history, current revision, and paired time | **PRESERVED** | One atomic CollectionPlanV1 owns every admitted cut and its canonical fingerprint (`SPINE:887-968`, `SPINE:1236-1250`). |
| Canonical policy, Scope, and diagnostic bytes | **PRESERVED** | CanonicalJsonV1, PolicySnapshotV1, ScopeIdV1, and post-evidence diagnostic allocation remain byte-complete (`SPINE:522-568`, `SPINE:1189-1272`). |
| SQLite WAL, FULL, and foreign-key readbacks | **PRESERVED** | Both database states fail closed before transactions on any missing or mistyped readback (`SPINE:677-695`). |
| Crash-persistent release admission and attempts | **PRESERVED** | Pre-SQLite admission, owner publication, PID reuse, repeated takeover, and attempt-bound FD4 remain total (`SPINE:987-1067`). |
| Checksummed effects, KnownGood, rollback, and release events | **PRESERVED** | Pending/complete effect ordering, exactly one KnownGood, new-transaction rollback, phase mapping, and four machine results remain explicit (`SPINE:1069-1188`). |
| ABI, managed ExecStart, timer success, and whole-pair rollback | **PRESERVED** | Exact final-artifact ABI proof and every named consumer/timer validation remain required (`SPINE:482-506`, `SPINE:1106-1116`). |
| UJ-5 and related trace rows | **PRESERVED** | Duplicate and retained timestamped history ownership remains explicit (`SPINE:1648-1688`). |
| Property, crash, IPC, timer, and rollback fixtures | **PRESERVED BUT INCOMPLETE FOR ONE NEW COUNTEREXAMPLE** | Existing suites remain named (`SPINE:411-475`); REALITY-B01 requires the additional unrootable-child/process-sibling trace. |
| Seed and Deferred discipline | **PRESERVED** | Seed remains minimal and implementation-owned; Deferred does not reopen v1 (`SPINE:1578-1630`, `SPINE:1690-1710`). |

## Mechanical Validation Record

All commands ran from the review worktree against the exact candidate named in
this report.

| Command or check | Result |
| --- | --- |
| `sha256sum .../ARCHITECTURE-SPINE.md` before review | **PASS** — `03b539cc80e98b7dac436360b324cb6e6f925a95e775571343b84b9cf2756a55` |
| `sha256sum .../ARCHITECTURE-SPINE.md` after review | **PASS** — exact same hash |
| `wc -l .../ARCHITECTURE-SPINE.md` | **PASS** — 1,710 lines |
| `uv run .agents/skills/bmad-architecture/scripts/lint_spine.py --workspace _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14` | **PASS** — `ok: true`, zero mechanical findings |
| `git diff --check` | **PASS** — no whitespace errors |
| Stable patch ID over the spine diff | **PASS** — `466f877adf3c99e4f0577d4c7e6a17a562aca747` on base `d4515067af8314cadf979da7b17921fbafc92d21` |
| AD definition and reference walk | **PASS** — 25 unique contiguous definitions and references, AD-1 through AD-25 |
| ARCH-LIM definition and reference walk | **PASS** — 23 unique contiguous definitions and references, ARCH-LIM-1 through ARCH-LIM-23 |
| Dispatch timing and half-open trace replay | **PASS** — default makespan 35 s before cutoff 40 s; process-60 plus seven 1-second Scopes makes 61 s and requires cutoff 61 s plus 1 ns at zero margin |
| Requested contract and fixture sweep | **PASS FOR PRESENCE** — all requested contracts are normative; REALITY-B01 is a semantic root-construction failure |
| Markdown lint on this report | **PASS** — project configuration, zero findings |

## Closure Gate

Approval remains blocked by REALITY-B01. The exact frozen candidate has one
blocking finding, zero high findings, and zero moderate findings. Remediate the
root-construction state-machine seam, freeze a new SHA, and rerun this
reality closure gate; do not mark the spine final before a zero-finding verdict.
