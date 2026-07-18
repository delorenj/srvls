---
title: "srvls Architecture Remediation Good-Spine Gate"
document_type: architecture_review
review_dimension: good_spine_remediation_gate
status: final
verdict: changes-required
blocking: true
review_date: 2026-07-16
reviewer: rubric-gate
reviewed_base_commit: d4515067af8314cadf979da7b17921fbafc92d21
reviewed_worktree_spine_sha256: d9128bcc347f553045198a5402f0b91f068013728460de64c6105ec3d57429b2
reviewed_worktree_patch_id: f6b7ae316614707aca78bf8870fba09b3735c238
reviewed_artifact: _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md
finding_count: 5
blocking_findings: 2
high_findings: 2
moderate_findings: 1
---

<!-- markdownlint-disable MD013 MD025 -->

# srvls Architecture Remediation Good-Spine Gate

## Verdict

**CHANGES REQUIRED.** The uncommitted remediation is mechanically clean and
closes the acceptance reports' technology, release-recovery, SQLite, trace, and
most collection seams. It is not yet safe to approve as the sole build
substrate. Two literal contradictions remain blocking:

1. the pure reconciliation engine is forbidden from reading a baseline after
   admission, but `AcceptedBaselineCutV1` retains only baseline identity and
   revision rather than the comparison projection the engine must consume; and
2. workers must echo a Collection Plan identity and the parent must reject a
   mismatch, but the enumerated `WorkerResultV1` has no plan identity field.

The post-evidence diagnostic ordering grammar and process-owner winner order
also remain under-specified. One bounded IPC disposition is missing for a valid
Collection Plan that exceeds the request-frame ceiling. These are focused
architecture edits. The accepted paradigm, AD-1 through AD-24 numbering,
operational limits, compatibility contracts, seed, and Deferred list do not
need broad reopening.

The spine correctly remains `status: draft` (`SPINE:1-10`).

## Review Basis

Citation keys:

- `SPINE` —
  `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md`
- `MEMLOG` — the sibling `.memlog.md`
- `PRD` —
  `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md`
- `ADD` — the canonical PRD `addendum.md`
- `DESIGN` — the canonical UX `DESIGN.md`
- `EXPERIENCE` — the canonical UX `EXPERIENCE.md`
- `TECH-ACC` — `reviews/review-technology-acceptance-2026-07-16.md`
- `DVG-ACC` — `reviews/review-two-unit-divergence-acceptance-2026-07-16.md`
- `RUBRIC-ACC` — `reviews/review-rubric-acceptance-2026-07-16.md`

The current 1,176-line worktree spine, complete 142-line memlog, complete PRD,
addendum, DESIGN, EXPERIENCE, all three immutable acceptance reports, and the
319-addition/90-deletion working-tree diff were read completely. The review
uses the good-spine checklist in the repository's `bmad-architecture` reviewer
gate. It judges semantic interoperability, not token presence.

## Good-Spine Checklist

| Check | Result | Evidence |
| --- | --- | --- |
| Real divergence points one level down are fixed | **FAIL — BLOCKING** | GATE-B01 and GATE-B02 leave a reconciliation input and an IPC result shape incompatible. |
| Every AD Rule is enforceable and prevents its stated divergence | **FAIL — BLOCKING** | AD-18/AD-21 cannot supply baseline comparison data under their own closed-input rule; AD-21/AD-25 require a result field AD-25 omits. |
| Deferred cannot permit incompatible v1 stories | **PASS** | Every item preserves a concrete v1 choice and has a scope/revisit condition (`SPINE:1156-1176`). |
| Named technology is verified-current | **PASS** | The immutable same-day technology acceptance accepts the corrected graph and current pins (`TECH-ACC:159-174`); this remediation does not change them (`SPINE:1020-1042`). |
| Brownfield behavior is ratified rather than contradicted | **PASS** | Raw routing and the layered compatibility oracle remain explicit (`SPINE:245-268`, `SPINE:284-308`). |
| Canonical PRD and UX capabilities land | **PASS WITH BLOCKING SEAMS** | Mechanical and semantic trace coverage is broad (`SPINE:1114-1154`), but GATE-B01 prevents FR-27/FR-28 execution from the declared pure input. |
| No AD weakens or contradicts another | **FAIL — BLOCKING** | GATE-B01 and GATE-B02 are direct cross-AD contradictions. |
| Deployment and environment envelope is decided | **PASS** | Target ABI, exact artifact proof, install ownership, release admission, timer consumers, rollback, and local Host scope are explicit (`SPINE:388-419`, `SPINE:788-881`). |
| Provider and operational strategy is decided | **PASS WITH HIGH CLARIFICATIONS** | Scheduling, privilege, subprocesses, cutoff, scopes, and IPC are present; GATE-H01 and GATE-H02 must make two decision rules total. |
| State integrity and recovery are decided | **PASS** | WAL/FULL/foreign-key readback, transactions, retention, capacity, release admission, journal ordering, known-good retention, and recovery ownership are explicit (`SPINE:509-578`, `SPINE:788-881`). |
| Security is decided at feature altitude | **PASS** | Absolute allowlisted executables, minimal environment, narrow privilege, FD3 peer checks, capability, no-discovery worker behavior, and no-symlink release paths are binding (`SPINE:488-507`, `SPINE:800-847`, `SPINE:947-990`). |
| Accessibility is decided | **PASS** | Text-first rendering, linear lane, terminal restoration, responsive ownership, and canonical UX authority remain closed (`SPINE:270-282`, `SPINE:467-486`, `SPINE:992-1002`). |
| Structural seed is minimal and code-owned | **PASS** | The seed names one composition shape and boundary ownership without adding a second normative data model (`SPINE:1044-1096`). |
| Status and finalization discipline are correct | **PASS** | Status remains draft and the memlog contains no new false finalization event (`SPINE:8`; `MEMLOG:125-142`). |

## Acceptance-Finding Closure Matrix

| Requested closure | Result | Current binding evidence |
| --- | --- | --- |
| Freeze accepted baseline in CollectionPlanV1 | **PARTIAL** | Identity, revision, compatibility, and pin are frozen, but comparison contents are not constructible under the no-later-read rule; GATE-B01 (`SPINE:728-744`, `SPINE:752-758`). |
| Freeze nonterminal operations | **CLOSED** | `OperationCutV1` freezes repository revision, sorted IDs, exact targets, and durable phases (`SPINE:730-731`). |
| Freeze resource history | **CLOSED** | `ResourceHistoryCutV1` carries revision plus sorted immutable sample IDs and rows, and admission pins them (`SPINE:732-744`). |
| Freeze current repository revision and prior current | **CLOSED** | Both global revision and pointer ID/revision are captured in the same read (`SPINE:721-735`). |
| Pair boot and UTC wall cuts | **CLOSED** | One `ClockSampleV1` is captured at admission and is the sole Snapshot, Evidence Window, sample, and Brief stamp (`SPINE:721-723`, `SPINE:756-758`). |
| One atomic plan admission | **CLOSED** | `admit_collection` uses one `BEGIN IMMEDIATE` transaction for ID allocation, cuts, plan insert, pins, and latest-requested update, or commits none (`SPINE:719-744`). |
| Reserve and authenticate same-binary worker route | **CLOSED** | Raw route precedes public routing; FD3 Unix stream, peer UID/PID, executable device/inode, and one-time capability are mandatory (`SPINE:245-252`, `SPINE:947-960`). |
| Versioned framing, stdio, exit, timeout, signal, mismatch, no-discovery | **PARTIAL** | Framing and behavior are explicit, but result-plan mismatch is not representable and oversize parent disposition is absent; GATE-B02 and GATE-M01 (`SPINE:962-990`). |
| Byte-complete PolicySnapshot JSON | **CLOSED** | Key order, NFC, escaping, controls, scalar rejection, integer and boolean grammar, null/float prohibition, separators, and fingerprint preimage are explicit (`SPINE:896-920`). |
| Byte-complete ScopeIdV1 and ScopeManifestV1 | **CLOSED** | Version/tag bytes, field framing, path/string rules, display encoding, order, manifest grammar, and hash preimage are explicit (`SPINE:922-940`). |
| Construct diagnostics after evidence | **PARTIAL** | Post-evidence allocation replaces impossible preallocation, but two sort fields lack a defined byte grammar; GATE-H01 (`SPINE:431-439`). |
| Deterministic process ownership, self suppression, conflicts, retention | **PARTIAL** | Shapes, evidence floor, suppression, conflicts, and retained diagnostics exist, but the selected-owner order lacks a winner direction; GATE-H02 (`SPINE:446-463`). |
| Crash-persistent ReleaseAdmissionV1 before SQLite | **CLOSED** | Every stateful entry retains shared admission and fails before SQLite on nonterminal or invalid recovery state; release alone owns exclusive recovery (`SPINE:800-816`). |
| Checksummed atomic UpgradeTransaction and effect ordering | **CLOSED** | O_EXCL temp write, file fsync, rename, directory fsync, checksum rejection, pending-before-effect, complete-after-readback, and may-have-executed recovery are binding (`SPINE:818-847`). |
| Exactly one KnownGoodReleaseV1 and explicit rollback transaction | **CLOSED** | The prior binary/state/consumers pair survives commit; rollback creates a new full transaction; only later successful commit replaces it (`SPINE:861-869`). |
| Durable internal-to-public release phase mapping | **CLOSED** | Public phases, event sequence/results, durable emission boundaries, resume behavior, recovery result, and ready transition are explicit (`SPINE:871-881`). |
| Ordered WAL/FULL/foreign-key readbacks on fresh/existing DBs | **CLOSED** | The adapter fails closed unless ordered values are `wal`, `2`, and `1` before any transaction (`SPINE:515-527`); fixtures are named (`SPINE:377-382`). |
| readelf ABI failure gate and oldest-runtime smoke | **CLOSED** | Exact artifact, maximum `GLIBC_2.42`, CI failure, and oldest supported runtime smoke are explicit (`SPINE:393-402`). |
| Managed absolute ExecStart rewrite and timer-triggered success | **CLOSED** | Both named services, loaded-path readback, paired trigger advancement, successful Result/status, whole-pair rollback, and proof are explicit (`SPINE:403-417`, `SPINE:849-859`). |
| UJ-5 and related traces | **CLOSED** | UJ-5 names Snapshot history owners and retained evidence; FR/SM/UX collection traces include AD-25 where applicable (`SPINE:1118-1154`). |
| Named property, concurrency, crash, IPC, timer, rollback fixtures | **CLOSED EXCEPT FINDING-SPECIFIC FIXTURES** | AD-11 lists the requested families (`SPINE:355-386`); GATE-B01/B02/H01/H02 require their fixture shapes to be tightened with the Rule fixes. |

## Tier 0 — Blocking Findings

### GATE-B01 — The frozen baseline cut has identity but no comparison projection

AD-18 says the pure engine consumes only the frozen Collection Plan and eligible
reports (`SPINE:607-610`). AD-21 then forbids a later baseline read
(`SPINE:752-756`). `AcceptedBaselineCutV1`, however, enumerates only
`none | accepted`, acceptance identity/revision, baseline Snapshot identity and
revision, and compatibility (`SPINE:728-729`). Pinning that immutable Snapshot
prevents deletion, but a pointer is not the Promise/Observation/Finding change
projection needed to produce the FR-27 change set and FR-28 Brief
(`PRD:456-480`).

Two compliant units still diverge. One can load and embed a baseline comparison
projection during admission. Another can persist only the enumerated IDs and
dereference the pinned Snapshot during reduction. The latter violates the
no-later-read rule; the former adds an undeclared field to the shared shape.

**Disposition: autofix.** Make `AcceptedBaselineCutV1` contain the complete,
versioned, immutable baseline comparison projection required by FR-27 and
FR-28, or explicitly define an admission-time repository resolution that makes
that projection part of the pure engine input. State that `none` contains no
projection. Extend the concurrent baseline/retention fixture to prove the
engine performs no post-admission baseline lookup.

### GATE-B02 — WorkerResultV1 cannot echo or validate the Collection Plan identity

AD-21 requires workers to receive and echo the exact plan identity and says
reduction rejects any mismatch (`SPINE:749-751`). AD-25 likewise says the parent
rejects a plan mismatch (`SPINE:973-974`). The exhaustive `WorkerResultV1` field
order contains protocol version, request ID, capability, ScopeId, result kind,
Collector report, diagnostics, and capture accounting—but no Collection Plan
identity or fingerprint (`SPINE:967-972`). AD-5's Collector report shape names
generation and scope, not a complete plan identity (`SPINE:149-153`).

Request ID and capability authenticate the channel; they do not encode which
policy, baseline, operation, history, current revision, or scope manifest the
worker actually applied. A parent cannot implement the mandated plan-mismatch
comparison from the result shape.

**Disposition: autofix.** Define one stable `CollectionPlanIdV1` or
domain-separated fingerprint over the complete canonical plan, include it in
both request and result schema order, and require byte equality before accepting
evidence. Add wrong-plan/same-generation and wrong-plan/same-scope IPC fixtures.

## Tier 1 — High Findings

### GATE-H01 — DiagnosticCandidateV1 still lacks a total sorting grammar

The remediation correctly allocates diagnostics only after evidence exists, but
the sort tuple relies on “canonical subject bytes” and “AD-24 canonical
parameter bytes” (`SPINE:431-438`). AD-24 defines Policy/Provenance JSON and
Scope binary grammar, but it does not define a diagnostic subject union or a
diagnostic parameter encoding (`SPINE:883-945`). Codes, subjects, integers,
non-UTF-8 paths, byte evidence, and structured parameters can therefore be
encoded differently by independent worker and coordinator units while each
claims canonicality. That changes the assigned ordinal and every Observation
reference.

**Disposition: autofix.** Define versioned tagged subject variants and a
byte-complete parameter grammar, including field order, raw-byte/path handling,
integer encoding, absent values, duplicate occurrence assignment, and unsigned
sort direction. Reuse AD-24 JSON only by saying exactly which diagnostic value
is encoded under that grammar. Expand the property fixture over arbitrary valid
subjects, parameters, duplicates, and worker/coordinator mixtures.

### GATE-H02 — Process-suppression winner order has no direction

AD-13 retains every hint, conflict, chosen owner, rule, and diagnostic, which
closes the evidence-loss problem. It says selection is by rule strength
`self < exact Provider PID < cgroup`, then Provider tag and ScopeId bytes
(`SPINE:454-461`), but it never says whether the minimum or maximum wins or
whether the subsequent byte orders are ascending or descending. Self is handled
by a separate unconditional branch, but two reducers can still choose an exact
PID claimant versus a cgroup claimant, or opposite Provider/Scope ties, and
persist different selected-owner output.

**Disposition: autofix.** Name the winning order explicitly—for example,
“choose the first item after sorting strength descending, Provider tag
ascending, unsigned ScopeId bytes ascending”—and keep conflict retention
unchanged. Add exact-PID-versus-cgroup and multi-Provider tie fixtures.

## Tier 2 — Moderate Finding

### GATE-M01 — A complete valid Collection Plan can exceed the request-frame limit without a disposition

`ResourceHistoryCutV1` carries eligible sample rows (`SPINE:732-733`), while
every worker request carries the complete Collection Plan and is capped at
32 MiB (`SPINE:962-970`). The supported state ceiling is 512 MiB and no
architecture rule proves the complete plan is bounded below 32 MiB. AD-25 says
an oversized received frame is invalid, but it does not say what the parent does
when it cannot encode an otherwise valid admitted plan without exceeding the
limit. Truncation, per-scope projection, failed attempt, and limit escalation
would yield different behavior.

**Disposition: discuss or autofix.** Either enforce and test a pre-admission
maximum canonical plan size below 32 MiB, send a versioned scope projection plus
the GATE-B02 plan fingerprint, or define a typed pre-dispatch failure that
terminalizes every scope/attempt without truncation. Add the exact-boundary and
one-byte-over fixtures.

## Preserved Contracts and Discipline

- AD-1 through AD-24 retain their numbers; the new worker contract is AD-25.
- ARCH-LIM-1 through ARCH-LIM-23 remain contiguous, internally referenced, and
  arithmetically unchanged.
- The accepted one-binary hexagonal and Elm-style paradigm remains intact.
- Brownfield table, JSON, Prometheus, Markdown, inspection, routing, action, and
  deployed-consumer contracts remain separate from new canonical surfaces.
- No Deferred item moves an MVP invariant out of the spine. Persistent grouping,
  themes, plugins, grouped legacy output, portability, multi-resource actions,
  interactive TUI elevation, remote/multi-user operation, and external content
  fetching all retain explicit v1 choices.
- The Structural Seed describes the cold-start ownership shape without becoming
  a second normative requirements document.
- The worktree diff changes only the spine before this review file; prior review
  reports, product code, memlog, and `tasks.md` were not altered.

## Validation Record

| Validation | Command or method | Result |
| --- | --- | --- |
| Frozen worktree identity | `git rev-parse HEAD`; SHA-256 and stable patch ID of the current spine diff | **PASS** — base `d4515067...`, spine `d9128bcc...`, patch `f6b7ae31...` |
| Required complete reads | Line-bounded reads through EOF for SPINE, MEMLOG, PRD, ADD, DESIGN, EXPERIENCE, and three acceptance reports | **PASS** |
| Current diff inspection | Complete `git diff -- ARCHITECTURE-SPINE.md` plus requested-term sweep | **PASS** — exact closures audited above |
| Architecture linter | `uv run .agents/skills/bmad-architecture/scripts/lint_spine.py --workspace _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14` | **PASS** — `ok: true`; zero findings |
| AD integrity | Range-expanded heading audit | **PASS** — AD-1 through AD-25, no duplicate or gap |
| ARCH-LIM integrity | Range-expanded table-definition audit | **PASS** — ARCH-LIM-1 through ARCH-LIM-23, no duplicate or gap |
| Draft status | Frontmatter inspection | **PASS** — `status: draft` |
| Whitespace/error check | `git diff --check` before report creation | **PASS** — no output |

## Closure Gate

A clean rerun requires GATE-B01 and GATE-B02 to close literally, GATE-H01 and
GATE-H02 to become total deterministic rules, and GATE-M01 to receive one
bounded disposition. The architecture linter, Markdown lint, diff check,
AD/ARCH-LIM integrity, requested-term sweep, and this independent rubric gate
should then be rerun against the final frozen worktree. The spine must remain
draft until the parent workflow decides finalization.
