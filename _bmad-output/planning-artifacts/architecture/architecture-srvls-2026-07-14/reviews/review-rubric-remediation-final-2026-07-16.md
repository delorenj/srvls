---
title: "srvls Architecture Remediation Final Good-Spine Gate"
document_type: architecture_review
review_dimension: good_spine_remediation_final
status: final
verdict: changes-required
blocking: true
review_date: 2026-07-16
reviewer: rubric-gate
reviewed_base_commit: d4515067af8314cadf979da7b17921fbafc92d21
reviewed_worktree_spine_sha256: 66e90f988cc607c1b90b2bb841ca6b1cdd7f7bdf49ccd74920a7e65916df436d
reviewed_worktree_patch_id: ee300e4277e55d3cd6996dba05249189f45bd186
reviewed_artifact: _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md
finding_count: 2
blocking_findings: 0
high_findings: 0
moderate_findings: 2
---

<!-- markdownlint-disable MD013 MD025 -->

# srvls Architecture Remediation Final Good-Spine Gate

## Verdict

**CHANGES REQUIRED.** The newly frozen spine at exact SHA-256
`66e90f988cc607c1b90b2bb841ca6b1cdd7f7bdf49ccd74920a7e65916df436d`
preserves every previously closed blocker and high-severity contract. Its new
transport-report, process-tree, scheduling, and recovery-attempt rules close the
substantive safety gaps they target. Two moderate deterministic seams remain:

1. AD-25 requires one synthesized transport-failure report but does not choose
   one stable reason when frame/schema/size evidence overlaps the worker's exit
   or the parent's termination signal.
2. AD-10 and ARCH-LIM-3 name a 61-second process-first oracle, but the runtime
   rule does not require the complete same-time vacant-slot batch to be spawned
   and authenticated before the process request closes the spawn gate. A
   literal sequential dispatcher takes 62 seconds.

The parent gate requires zero blocker, high, or moderate gaps for approval, so
these two focused fixes prevent approval. The spine correctly remains
`status: draft` (`SPINE:1-10`).

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

The complete current 1,535-line spine was read from the frozen hash. The
complete BMAD architecture skill, headless rules, and reviewer gate were
reloaded. The unchanged complete memlog, canonical PRD/addendum, DESIGN,
EXPERIENCE, and three immutable acceptance reports remain the controlling
source set from the prior complete gate; relevant source contracts and all
prior finding dispositions were rechecked against the current Rules. This is a
semantic cross-unit review, not a requested-term presence check.

## Good-Spine Checklist

| Check | Result | Binding evidence |
| --- | --- | --- |
| Real divergence points one level down are fixed | **FAIL — MODERATE** | FINAL-M01 leaves transport reason selection divergent; FINAL-M02 leaves same-time worker batch startup divergent. |
| Every AD Rule is enforceable and prevents its stated divergence | **FAIL — MODERATE** | AD-25 fixes the outcome but not overlapping reason precedence; AD-10 fixes two numeric examples but not the dispatch event that makes the process-first result general. |
| Deferred cannot permit incompatible v1 stories | **PASS** | Every item preserves a concrete v1 choice and names a later trigger (`SPINE:1515-1535`). |
| Named technology is verified-current | **PASS** | The accepted same-day technology graph and exact stack remain unchanged (`SPINE:1381-1403`; `TECH-ACC:159-174`). |
| Brownfield behavior is ratified rather than contradicted | **PASS** | Raw routing, legacy arity, separate compatibility presenters, and the layered oracle remain closed (`SPINE:248-314`). |
| Canonical PRD and UX capabilities land semantically | **PASS WITH MODERATE DETERMINISM SEAMS** | FR-14 partial truth, NFR-1/NFR-3 bounded determinism, UJ-5 history, and release UX all have owners; FINAL-M01/M02 affect deterministic implementation, not capability presence. |
| No AD weakens or contradicts another | **PASS WITH MODERATE CLARIFICATIONS** | Prior AD-18/AD-21 and AD-7/AD-25 contradictions remain closed. The two findings are missing total orders, not weakened accepted contracts. |
| Deployment and environment envelope is decided | **PASS** | ABI proof, oldest runtime, consumer rewrites, release admission, recovery attempts, and one-Host scope remain binding (`SPINE:426-458`, `SPINE:928-1128`). |
| Provider and operational strategy is decided | **FAIL — MODERATE** | Process groups and barrier-aware limits are present, but FINAL-M02 leaves one dispatch-event order implicit (`SPINE:316-372`, `SPINE:782-828`). |
| State integrity and recovery are decided | **PASS** | SQLite initialization, plan admission, release owner publication, checksummed effects, KnownGood retention, and rollback remain total (`SPINE:621-689`, `SPINE:830-901`, `SPINE:928-1128`). |
| Security is decided at feature altitude | **PASS** | FD peer/executable checks, process-group identity, one-time capabilities, attempt-bound FD4, no-follow paths, and pre-SQLite gates remain binding (`SPINE:532-577`, `SPINE:940-1045`, `SPINE:1218-1349`). |
| Accessibility is decided | **PASS** | Text-first meaning, hostile-content handling, linear output, terminal ownership, and canonical UX authority are unchanged. |
| Structural Seed is minimal and code-owned | **PASS** | The Seed remains one implementation-shaped ownership map, not a second normative model (`SPINE:1405-1455`). |
| Status and finalization discipline are correct | **PASS** | The spine remains draft and the memlog has no false finalization event (`SPINE:1-10`; `MEMLOG:125-142`). |

## Prior-Gate Closure Audit

| Prior gate | Result | Current binding evidence |
| --- | --- | --- |
| GATE-B01 — complete baseline comparison input | **CLOSED** | AcceptedBaselineCutV1 embeds the entire identity-sorted, versioned FR-27 comparison projection; the reducer performs zero later baseline lookup (`SPINE:845-879`, `SPINE:1177-1190`). |
| GATE-B02 — request/result plan identity | **CLOSED** | CollectionPlanFingerprint and ScopeAssignmentFingerprint remain in request, result, recomputation, and byte-equality admission (`SPINE:868-895`, `SPINE:1268-1331`). |
| GATE-H01 — diagnostic byte grammar and post-evidence allocation | **CLOSED** | Tagged subject/parameter bytes, encounter and duplicate order, local references, final merge, rewrite, and rejection remain total (`SPINE:471-517`). |
| GATE-H02 — process-owner winner order | **CLOSED** | First-after-ascending exact PID/cgroup/provider/Scope order remains explicit, with every conflict and rejected hint retained (`SPINE:550-577`). |
| GATE-M01 — oversize request/result disposition | **CLOSED** | Per-scope requests remain bounded; exact over-limit request/result branches synthesize one AD-5 report without truncation (`SPINE:884-890`, `SPINE:1233-1266`). FINAL-M01 concerns competing reason evidence after that disposition, not its existence. |

## Final Stress-Check Matrix

| Requested stress check | Result | Evidence and conclusion |
| --- | --- | --- |
| Coordinator-synthesized AD-5 report for every FD3 transport branch | **PASS FOR OUTCOME AND SHAPE; MODERATE REASON GAP** | AD-5 keeps six outcomes and one report per scope (`SPINE:143-165`). AD-25 covers spawn/group setup, request encode/size, peer auth, framing, schema/version/identity/capability/assignment, result size, typed worker errors, exits, signals, and deadline equality with a complete zero-evidence report (`SPINE:1233-1266`). FINAL-M01 is the remaining overlapping-evidence precedence. |
| Barrier-aware one-shot LPT; default 35 seconds; pathological 61 seconds | **PARTIAL — MODERATE** | LPT, barrier idling, exact simulation, default 35, pathological 61, every-position fixtures, and near-deadline reads are named (`SPINE:321-340`, `SPINE:388-407`, `SPINE:793-824`). FINAL-M02 shows the runtime event order does not yet force the 61-second branch. |
| Process worker/child/grandchild self membership | **PASS** | Every authenticated worker is a process-group leader; frozen roots retain group IDs; exact PID/birth members in frozen groups are materialized and suppressed, while escaped descendants are emitted unless independently owned (`SPINE:532-562`, `SPINE:1222-1225`, `SPINE:1323-1344`). Property fixtures cover in-group descendants and escapes (`SPINE:395-400`). |
| ReleaseRecoveryAttemptV1 publication, PID reuse, and second crash | **PASS** | Exclusive lock capability, exact old-owner liveness, PID/birth reuse evidence, predecessor checksum, gap-free attempt append, readback-before-effect, crash-before/after publication, and repeated takeover are explicit (`SPINE:956-975`). Fixtures name old-PID reuse, forged publication, and a second recovery-owner crash (`SPINE:408-417`). |
| Attempt-bound FD4 validation and pending-validation recovery | **PASS** | Peer PID/birth/executable must match the active attempt; request/result echo attempt and manifest revision/checksum; old sockets and capabilities expire; recovery uses a fresh exchange after owner publication (`SPINE:977-1008`, `SPINE:1038-1045`). Fixtures cover crashes before result and after result-before-complete (`SPINE:408-417`). |
| Public release-event mapping unchanged | **PASS** | Owner publication is a control transition, not a public phase; resumed retains the pending step's existing phase. The seven internal-step/public-phase/UX rows and four terminal machine results remain unchanged (`SPINE:969-975`, `SPINE:1093-1128`). |
| Draft status, AD/ARCH-LIM, Seed/Deferred, and UJ-5 | **PASS** | Draft is retained; AD-1 through AD-25 and ARCH-LIM-1 through ARCH-LIM-23 are unique and contiguous; UJ-5 retains duplicate plus timestamped history owners (`SPINE:1-10`, `SPINE:1492`, `SPINE:1405-1455`, `SPINE:1515-1535`). |

## Tier 2 — Moderate Findings

### FINAL-M01 — Transport failure has one report but no total reason precedence

AD-25 now correctly requires exactly one coordinator-synthesized
CollectorReportV1 and exhaustively defines its safe shape (`SPINE:1245-1266`).
Several failures, however, expose more than one allowed reason before the
coordinator commits that report:

- a malformed or early-EOF result can be followed by worker exit `64`;
- an over-limit or identity-mismatched result causes parent termination and a
  resulting signal wait status; and
- a valid `worker-error` frame can be followed by exit `70`.

The Rule permits `frame-invalid`, `worker-result-too-large`,
`identity-mismatch`, `worker-internal-error`, `worker-exit`, and
`worker-signal`, and says exactly one report is produced, but it does not rank
those simultaneous facts (`SPINE:1245-1260`, `SPINE:1333-1344`). Deadline
equality does have explicit precedence (`SPINE:1261-1263`), which demonstrates
the missing rule for the other overlaps. A reader-first coordinator can retain
the frame cause while a wait-first coordinator can retain exit or signal; both
produce safe `invalid-output` completeness but different canonical diagnostics,
Snapshot bytes, and fixtures.

**Disposition: autofix.** Define a total precedence for competing transport
evidence. Preserve the originating parser/size/identity reason over a
parent-induced termination status, or choose another explicit order; retain
secondary exit/signal evidence only as declared parameters. Add combined cases
such as malformed-frame-plus-exit-64, oversize-plus-termination-signal, and
worker-error-plus-exit-70 to the transport fixture matrix.

### FINAL-M02 — The process-first 61-second oracle requires an unstated batch-start rule

AD-10 says each one-shot worker is dispatched in LPT order and that the
coordinator closes the spawn gate after it has spawned and authenticated **the
process worker** (`SPINE:321-333`). It does not say that all jobs assigned to
the other currently vacant slots are also spawned and authenticated before the
process request is released.

The difference is observable in the named counterexample (`SPINE:817-824`):

| Runtime interpretation | Default jobs | Process 60 s plus seven 1 s jobs |
| --- | ---: | ---: |
| Fill one dispatch-time batch, spawn/authenticate all four, then release requests | 35 s | 61 s |
| Dispatch sequentially; process-first request closes the gate immediately | 35 s | 62 s |

In the sequential interpretation, only the process worker is live at time zero.
At 60 seconds four one-second workers run, and the remaining three cannot start
until 61 seconds. In the batched interpretation, three one-second workers are
already live under the barrier; all four remaining jobs run at 60 seconds and
finish at 61. The explicit 61-second sentence supplies one oracle, but it does
not define the general event rule needed by the runtime scheduler, configuration
simulator, or the “process scope in every LPT position” fixtures
(`SPINE:335-340`, `SPINE:388-394`).

**Disposition: autofix.** Define one dispatch event explicitly. For the stated
61-second result: at each timestamp, select the complete LPT assignment for all
vacant slots; spawn and authenticate that entire batch; if it contains the
process scope, freeze roots and close the gate only after every batch worker is
authenticated; then release requests in deterministic slot order. Require the
runtime and configuration simulator to consume the same event transition and
fixture expectations. Alternatively choose sequential startup and correct the
oracle and cutoff formula consistently.

## Preserved Contracts and Discipline

- Accepted baseline, operation, resource-history, current-revision, prior
  current, and paired clock cuts remain one atomic `BEGIN IMMEDIATE` admission.
- Canonical PolicySnapshot, CollectionPlan, ScopeId, ScopeManifest, diagnostic,
  request, result, and fingerprint bytes remain closed.
- SQLite WAL/FULL/foreign-key readback, exact-artifact GLIBC gate,
  oldest-runtime smoke, managed ExecStart/timer validation, whole-pair rollback,
  crash-persistent release admission, checksummed pending/complete effects,
  one KnownGoodReleaseV1, and explicit rollback-as-new-transaction remain closed.
- ReleaseRecoveryAttemptV1 strengthens recovery ownership without changing the
  accepted public release phase or final-result vocabulary.
- The direct-process worker barrier now covers authenticated workers and their
  supervised in-group children and grandchildren without suppressing escaped or
  unrelated processes.
- AD-1 through AD-25 retain stable numbering. ARCH-LIM-1 through ARCH-LIM-23
  retain stable numbering and values. The accepted paradigm, compatibility
  lanes, minimal Seed, disciplined Deferred list, and UJ-5 trace remain intact.
- This review edits no spine, prior report, memlog, product code, or `tasks.md`.

## Validation Record

| Validation | Command or method | Result |
| --- | --- | --- |
| Frozen spine identity | `sha256sum .../ARCHITECTURE-SPINE.md` | **PASS** — exact required SHA-256 `66e90f98...436d`. |
| Base and spine patch | `git rev-parse HEAD`; spine-only stable patch ID | **PASS** — base `d4515067...`; patch `ee300e42...`. |
| Complete current read | Line-bounded reads through EOF | **PASS** — 1,535/1,535 lines. |
| Architecture linter | `uv run .agents/skills/bmad-architecture/scripts/lint_spine.py --workspace _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14` | **PASS** — `ok: true`; zero findings. |
| AD integrity | Definition and reference inventory | **PASS** — AD-1 through AD-25 exactly once; no out-of-range reference. |
| ARCH-LIM integrity | Definition and reference inventory | **PASS** — ARCH-LIM-1 through ARCH-LIM-23 exactly once; no out-of-range reference. |
| Requested-term and diff inspection | Full current Rule read plus focused diff and term sweep | **PASS** — every requested contract is present; the two semantic seams are recorded above. |
| Independent timing model | Batched and sequential event simulations over the two named workloads | **FAIL AS A TOTAL CONTRACT** — both yield default 35 s; batched yields 61 s and literal sequential dispatch yields 62 s. |
| Draft status | Frontmatter inspection | **PASS** — `status: draft`. |
| Whitespace/error check | `git diff --check` before report creation | **PASS** — no output. |

## Closure Gate

A clean final rerun requires one total AD-25 transport-failure reason
precedence and one explicit AD-10 same-time worker-batch transition that makes
the runtime, simulator, 35-second default, 61-second counterexample, and
every-process-position fixtures identical. No other accepted contract needs
reopening, and the spine must remain draft until the parent workflow decides
finalization.
