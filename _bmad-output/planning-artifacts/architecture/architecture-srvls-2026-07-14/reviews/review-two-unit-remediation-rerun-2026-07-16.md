---
title: "srvls Architecture Two-Unit Remediation Rerun"
type: architecture-review
status: final
created: 2026-07-16
updated: 2026-07-16
reviewer: independent-configured-two-unit-reviewer
review_mode: adversarial-remediation-rerun
reviewed_base_commit: d4515067af8314cadf979da7b17921fbafc92d21
reviewed_worktree_spine_sha256: 818bea5f4770b3f913fbba3e2e688da14d5f42cb150b2d284c2eb00bc3bae862
reviewed_artifact: _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md
verdict: changes-required
blocking_status: blocked
named_findings_closed: 5
named_findings_open: 2
new_blocking_findings: 2
---

<!-- markdownlint-disable MD013 MD025 -->

# Architecture Review: Two-Unit Remediation Rerun

## Verdict

**CHANGES REQUIRED. Blocking status: BLOCKED for scoped collection IPC and
release crash-recovery implementation stories.**

The frozen revision closes five of the seven named remediation findings
literally. It embeds the complete accepted-baseline comparison projection and
forbids late baseline reads; makes diagnostic candidates constructible after
evidence; fixes the exact self-process set, worker-spawn barrier, suppression
winner, and retained conflict evidence; puts KnownGood publication after an
irreversible durable commit decision with a complete recovery truth table; and
maps every durable release step through public events, UX states, and final
machine results.

Two narrower residual choices prevent approval:

1. AD-25 gives oversized request and result frames stable terminal reason
   tokens, but does not choose how either token becomes AD-5's exhaustive
   Collector outcome and required one-terminal-report-per-scope contract.
2. AD-23 requires a pending candidate-validation effect to rerun after crash,
   but the new candidate authenticates its parent against the manifest's
   original PID/birth/executable release-owner identity. A replacement recovery
   owner cannot match it, and no authenticated owner-rebinding or mandatory
   pre-decision rollback rule resolves that edge.

Those are observable cross-unit choices, not editorial omissions: independent
reducers can persist different Snapshot/CollectionAttempt truth, and
independent release coordinators can produce rollback,
`upgrade-recovery-required`, or an uncontracted manifest rewrite at the same
crash point. The spine must remain `draft`.

This review adds only this report. It does not amend the spine, any prior
report, `tasks.md`, canonical product or UX artifacts, or product code.

## Review Target and Complete Source Basis

The target is the working-tree spine on branch
`feature-prof-fiddlesticks-architecture-remediation`, based on commit
`d4515067af8314cadf979da7b17921fbafc92d21`. The uncommitted review target was
re-pinned before and after semantic review by the exact 1,429-line SHA-256:

`818bea5f4770b3f913fbba3e2e688da14d5f42cb150b2d284c2eb00bc3bae862`

The interrupted analysis of the prior hash was discarded. These live sources
were then read completely from line 1 through EOF:

| Artifact | Lines |
| --- | ---: |
| Revised `ARCHITECTURE-SPINE.md` | 1,429 |
| Canonical `prd.md` | 823 |
| Canonical `addendum.md` | 63 |
| Canonical `DESIGN.md` | 329 |
| Canonical `EXPERIENCE.md` | 813 |

`AGENTS.md`, the complete BMAD architecture skill, and its complete headless
and reviewer-gate references had already been read for this review assignment.
The prior two-unit acceptance and remediation reports were used only to retain
the named probes; their conclusions were not used as proof.

Canonical precedence remained PRD, addendum, DESIGN/EXPERIENCE, then spine.
The acceptance standard remained literal independent-unit interoperability:
the contract must choose one data shape, byte representation, owner, read cut,
deadline, admission rule, terminal projection, and crash result wherever the
units meet.

## Independently Reconstructed Units

The rerun rebuilt the six requested units from the frozen sources rather than
repairing the earlier reviewer models in place.

| Pair | Unit | Independently derived responsibility |
| --- | --- | --- |
| Promise/reconciliation | P-A — Promise Lifecycle Command Unit | Validates lifecycle input and atomically appends the next gap-free event plus the current Promise projection revision. |
| Promise/reconciliation | P-B — Reconciliation and State Unit | Consumes only the admitted CollectionPlan plus eligible reports, computes axes, labels, Brief and baseline changes, then requests the atomic Snapshot/Findings/current-pointer write. |
| Collection/reducer | C-A — Scoped Collection Worker Unit | Authenticates FD3, validates one byte-total scope assignment, performs only its supplied Host reads, constructs report-local diagnostic references, and returns one bounded result. |
| Collection/reducer | C-B — Snapshot Reducer and Persistence Unit | Atomically admits and schedules the plan, builds assignments, validates results, closes deadlines, finalizes diagnostics and process suppression, and persists terminal collection truth. |
| Release/storage | I-A — Release Install Coordinator | Owns admission, transaction ordering, FD4 candidate validation, activation, consumer validation, KnownGood decision/publication, public events, rollback selection, and recovery. |
| Release/storage | I-B — SQLite Migration and Recovery Adapter | Implements backup, migration, restore, pragma/integrity verification, sidecar disposition, exact readbacks, hashes, and fsync effects requested by I-A. |

No unit was allowed to import another unit's implementation detail or perform a
repository, configuration, wall-clock, or discovery read not granted by its
declared interface.

## Named Remediation Finding Rerun

| Finding | Result | Literal result at the frozen hash |
| --- | --- | --- |
| NEW-B01 — embedded baseline comparison/no late lookup | **CLOSED** | `AcceptedBaselineCutV1` embeds the complete versioned comparison projection, exact row identities, baseline policy/scope/decision versions and canonical order; it is admitted and pinned atomically, and P-B is explicitly forbidden from a post-admission baseline lookup (`SPINE:801-835`, `824-854`). |
| NEW-B02 — bounded byte-total scope request with plan/assignment identity and oversize | **OPEN — BLOCKING RESIDUAL** | The bounded scope schema, both fingerprints, field bytes, result echo and one-byte-over detection are total, but the oversized terminal reasons are not mapped to AD-5's exhaustive Collector outcome/report contract (`SPINE:149-167`, `1154-1227`). See RERUN-B01. |
| NEW-B03 — KnownGood commit-decision crash truth | **CLOSED** | A staged candidate precedes durable `commit-decided`; publication follows it; the crash table chooses rollback before the decision and forward completion after it; explicit rollback is a new transaction (`SPINE:985-1015`). |
| NEW-H01 — diagnostic references, ordinal partition and byte grammar | **CLOSED** | Per-scope ordinal domain, byte-total subject and parameter grammars, duplicate occurrence, post-evidence local reference, final merge and atomic rewrite are all explicit (`SPINE:444-490`). |
| NEW-H02 — exact self set and deterministic winner | **CLOSED** | The generation-bound set, direct-process spawn barrier, unrelated-process exclusion, request/report echo, exact evidence rules, first-ascending winner, Provider order, conflicts and retained diagnostics are explicit (`SPINE:505-535`). |
| NEW-H03 — versioned authenticated read-only candidate bypass | **OPEN — BLOCKING RESIDUAL** | One live validation session is versioned, authenticated, bounded, read-only and fail-closed, but crash-resumed pending validation has no way to authenticate a replacement release owner against the original owner identity (`SPINE:912-950`, `961-971`). See RERUN-B02. |
| NEW-H04 — full step/event/UX/final-result mapping | **CLOSED** | Every forward, recovery and terminal step maps to one public phase and UX label; event-to-UX projection, skip/resume boundaries and the four final machine results are exhaustive (`SPINE:1017-1050`). |

**Named-finding result: five closed, two left open by narrower crash and
terminal-projection residuals.**

## Independent Pair Reconstructions

### P-A / P-B — Converged

P-A can commit a lifecycle event while P-B is waiting on collection without
changing P-B's generation: `admit_collection` holds one `BEGIN IMMEDIATE`,
captures Promise projection revisions and event sequences, and inserts the
complete plan or none (`SPINE:792-829`). A later lifecycle event belongs only
to the next generation.

P-B receives all comparison input without a late repository choice:

- `none` contains no invented baseline projection;
- `accepted` contains acceptance and Snapshot revisions plus the complete
  materialized Promise, Observation, and Finding comparison rows;
- rows have canonical identity order and carry policy, ScopeManifest and
  decision-contract versions;
- plan bytes and the domain-separated fingerprint include the projection; and
- baseline, operation, resource-history, current-pointer and later clock reads
  are explicitly forbidden after admission.

Two P-B implementations therefore receive the same FR-27 input and cannot
choose between dereferencing a baseline handle and using an embedded copy. The
concurrent-baseline-acceptance, later-Promise-event, later-resource-sample and
later-wall-clock probes all leave the admitted generation unchanged.

### C-A / C-B — Does Not Fully Converge

The main wire and evidence construction now converge:

1. Raw argv selects only `__srvls-worker-v1`; FD3 type, peer UID/PID, executable
   device/inode and one-use request/capability checks precede Host work.
2. C-B sends the bounded scope assignment, not CollectionPlanV1. The exact
   CanonicalJsonV1 request order includes plan fingerprint, repository
   revision, generation, ScopeId, assignment fingerprint, obligation,
   boottime deadline, reservations, SelfProcessSet and one Provider input.
3. `ProviderScopeInputV1` fixes every field tag, value kind, length, order,
   path normalization, command argv, environment set and empty-list form.
4. C-A recomputes the domain-separated assignment fingerprint before Host
   work and echoes every identity field. C-B rejects any byte mismatch.
5. Diagnostic candidates exist only after evidence. C-A sorts the complete
   tuple, assigns report-local refs and sends only same-report references; C-B
   re-sorts accepted candidates, assigns per-scope IDs once, and atomically
   rewrites refs.
6. The process worker is released only after all earlier live workers are
   authenticated and frozen into SelfProcessSetV1. The spawn barrier prevents a
   later worker from entering the half-open process cut, and the report echoes
   the complete set.

The boundary-size branch does not converge. C-B must obey both of these rules:

- AD-25 records terminal `worker-request-too-large` or
  `worker-result-too-large` for the exact scope (`SPINE:1154-1166`).
- AD-5 allows only six Collector outcomes, requires one terminal report per
  frozen scope for a fully reduced generation, and otherwise distinguishes a
  failed CollectionAttempt from an incomplete candidate Snapshot
  (`SPINE:149-167`).

Nothing chooses the bridge between those two contracts. That leaves the pair
not accepted.

### I-A / I-B — Does Not Fully Converge

The ordinary state and commit paths now converge:

- every ordinary stateful entry checks durable admission plus the transaction
  before SQLite;
- transaction replacement is checksummed, no-follow, file-fsynced,
  rename-atomic and directory-fsynced;
- every forward and rollback effect has durable pending evidence before the
  effect and complete evidence only after required readback;
- I-B's backup/migrate/restore checks schema, integrity, sidecars and hashes;
- staged KnownGood data does not replace the published record;
- completed `commit-decided` is the one irreversible boundary;
- recovery before that boundary validates and restores the whole prior pair;
  recovery after it must publish, set ready and terminally commit; and
- the release-event and final-result projections no longer leave I-A or a
  presenter to invent phase names.

The live FD4 bypass also converges: Unix-stream framing, peer identity,
one-time capability, transaction and generation, candidate hash, database and
schema, read-only mode, response echo, 1 MiB caps, EOF and mismatch behavior
are explicit (`SPINE:912-937`).

The crash-resumed pending-validation edge does not converge. The manifest
stores the release owner's PID, birth and executable identity
(`SPINE:939-944`). Candidate entry must match its current parent to that
manifest owner before SQLite (`SPINE:912-929`). Yet a pending validation effect
must rerun read-only during recovery (`SPINE:961-971`). After the original
owner crashes, the process holding exclusive recovery ownership necessarily has
a different PID/birth. No rule permits or orders an authenticated owner change.

That leaves I-A unable to issue a request that both satisfies the old manifest
and proves the live recovery parent. I-B itself remains total for the database
effects it owns, but the pair cannot complete the required release transaction
without an I-A-only choice outside the contract.

## Required Edge Probes

### Direct-process worker-spawn barrier — PASS

The adversarial interleaving is now forced:

| Cut point | Required state |
| --- | --- |
| Before process-worker release | Coordinator authenticates every live worker, acquires the spawn barrier, and freezes coordinator plus worker PID/birth/device/inode identities. |
| Process request admission | Request carries the complete generation-bound set and its assignment fingerprint. |
| Half-open process Host-read cut | A worker already live is in the set; a new worker cannot spawn; an unrelated same-inode srvls process is not a member. |
| Report admission | Report echoes the same set; mismatch rejects it. |
| Cross-Provider reduction | Only cutoff-eligible exact PID/birth hints may suppress; first ascending exact-owner rule wins and all conflicts remain. |

The previous before-freeze/after-freeze worker race therefore has no legal
interleaving left.

### Bounded scope schema and plan identity — FAIL only at terminal projection

Exact-boundary and one-byte-over sizes are computable before allocation. A
worker cannot substitute a later plan, generation, scope, obligation,
deadline, reservation, self set, command, environment, read root or privilege
because the request bytes feed ScopeAssignmentFingerprint and the result echoes
both identities.

The one-byte-over branch itself has one remaining choice: whether it becomes a
synthetic `invalid-output`, `unavailable`, or another allowed Collector report,
or aborts the generation as a failed CollectionAttempt. RERUN-B01 records the
observable consequences.

### Candidate reference construction — PASS

The construction timeline no longer requires a future DiagnosticId:

`evidence -> candidate bytes -> deterministic local sort ->
DiagnosticCandidateRefV1 -> CollectorReportV1 -> eligible global merge ->
per-scope ordinal -> atomic reference rewrite -> Snapshot`

The subject tags, lengths and payloads are byte-total; parameter values are
tagged CanonicalJsonV1; duplicate occurrence is defined; coordinator-only
conditions without a real scope become CollectionAttempt results; dangling,
duplicate, cross-scope and rejected-report refs fail. C-A and C-B therefore
construct the same final IDs without a pre-dispatch range.

### Candidate bypass and commit crash edges — One PASS, one FAIL

The commit decision has a single truth table:

| Last durable edge | Required recovery result |
| --- | --- |
| Before candidate validation complete | Restore and validate the whole prior pair. |
| Validation complete, before `commit-decided` complete | Restore and validate the whole prior pair. |
| `commit-decided` pending only | Decision is not complete; restore the prior pair. |
| `commit-decided` complete, KnownGood absent or pending | Republish the staged candidate, verify, persist target ready, then commit. |
| KnownGood complete, admission recovering | Verify published checksum/generation, persist target ready, then commit. |
| Target ready, transaction nonterminal | Complete the original transaction as committed. |
| Any staged candidate, checksum or generation mismatch | Return `upgrade-recovery-required`; never choose an older file. |
| Explicit operator rollback | Create a new transaction targeting the retained pair; never repoint directly. |

No implementation may roll back after completed `commit-decided`, so NEW-B03
is closed.

The earlier `validate-candidate pending` edge remains contradictory. AD-23 says
to rerun validation, but the only authenticated manifest owner died. Skipping
the rerun and rolling back, rewriting the manifest owner and rerunning, or
failing with `upgrade-recovery-required` are three distinct outcomes permitted
by different clauses. RERUN-B02 is therefore blocking.

### Release step/event/UX/final result — PASS

The complete table assigns every internal step to stage, checksum, smoke,
activate, consumer-validation, recovery or commit. Pending is derived from a
future step; started/resumed is running; succeeded is passed only when every
applicable phase step completes; failed is failed; and skipped requires a
complete skipped step plus reason. Event emission is ordered after durable
pending/complete/failure/resume evidence. Recovery preserves the original
transaction and emits resumed plus its eventual result.

The terminal set is closed: `committed`, `forward-failed-recovered`,
`rolled-back`, and `upgrade-recovery-required`. The final result retains the
failing step, recovered pair, generations, or last durable mismatch as
applicable. No fifth resumed alias remains.

## Blocking Residual Findings

### RERUN-B01 — Oversized worker failures have no canonical Collector projection

- **Severity:** Tier 0 / blocking
- **Affected named finding:** NEW-B02
- **Units:** C-A / C-B, with observable P-B and presentation consequences
- **Evidence:** `SPINE:149-167`, `1154-1166`

AD-25 correctly says a one-byte-over request is never sent and a one-byte-over
result is never allocated or parsed. It records a stable terminal reason and
measured/allowed sizes. AD-5 separately says every Collector report has exactly
one of six outcomes and every fully reduced scope has one terminal report; a
setup/reduction failure instead records a failed CollectionAttempt and keeps
the prior current pointer.

The bridge is absent. Two independently conforming reducers can do this:

1. synthesize `invalid-output` with zero Observations and persist an incomplete
   candidate/current Snapshot according to obligation; or
2. treat inability to send or parse the scope exchange as reduction failure,
   persist only CollectionAttempt, and leave current truth stale.

A third can choose `unavailable`. Those choices change strict-mode exit,
Evidence Status, absence claims, baseline eligibility, current-pointer
movement and Brief content. The exact-boundary fixture names the reason but
cannot infer the missing outcome and persistence rule.

**Smallest total closure:** For both reason tokens, choose exactly one of:

- a specified synthetic CollectorReportV1 outcome with exact zero/retained
  evidence, duration and diagnostic fields, then state that AD-5 reduction and
  strictness apply normally; or
- a specified generation-level failed CollectionAttempt with no candidate
  Snapshot and unchanged current pointer.

Name whether required, optional and strict invocations differ. Add one fixture
for request-too-large and one for result-too-large that asserts terminal report
or attempt rows, current-pointer behavior, strict exit and Brief completeness.

### RERUN-B02 — Pending candidate validation cannot authenticate a new recovery owner

- **Severity:** Tier 0 / blocking
- **Affected named finding:** NEW-H03
- **Units:** I-A / candidate entry, with I-B recovery effects downstream
- **Evidence:** `SPINE:908-937`, `939-971`, `1001-1010`

The live parent-child session is strong. The crash edge is not total:

1. UpgradeTransactionV1 stores original owner PID, birth and executable.
2. Original owner persists `validate-candidate pending` and launches the staged
   candidate.
3. Original owner crashes before `complete` is durable.
4. A new process acquires exclusive recovery ownership.
5. Recovery is required to rerun pending validation read-only.
6. The candidate must authenticate its parent against the manifest's original
   owner identity before SQLite.

The new owner has a different PID and birth. Updating the manifest owner,
ignoring PID/birth, skipping the mandated rerun and rolling back, or failing
closed are all unstated choices. They produce different ReleaseEvents and final
machine results.

**Smallest total closure:** Choose one crash rule:

- **Authenticated retry:** retain immutable original owner identity, add a
  versioned current recovery-attempt owner identity and attempt number, persist
  it under exclusive ownership before `resumed`, bind a fresh request UUID and
  capability to that attempt, require PID/birth/executable equality against
  that attempt owner, and then rerun validation; or
- **No retry before decision:** state that a pending candidate-validation step
  after owner death is never rerun, remove validation from the generic pending
  rerun rule for this edge, and mandate verified whole-pair rollback with the
  exact recovery events and `forward-failed-recovered` result.

Add the crash fixture at `validate-candidate pending` after candidate process
start but before result and again after result but before manifest complete.
Assert owner authentication, request/capability lifetime, events, admission,
restored or target pair, and final result.

## Preserved Contracts and Contradiction Probe

No new divergence was found in these already-closed seams:

| Contract | Rerun result |
| --- | --- |
| Atomic GenerationId, plan, pins and latest-requested admission | Preserved |
| Promise/event revision cut and later-write isolation | Preserved |
| Current Snapshot/Findings/current-pointer atomicity | Preserved |
| Nonterminal operation and resource-history cuts | Preserved |
| Paired boot/UTC wall stamping | Preserved |
| ScopeIdV1, ScopeManifestV1 and PolicySnapshotV1 bytes | Preserved |
| Half-open scope/generation deadline equality | Preserved |
| Supersession and latest-generation pointer CAS | Preserved |
| Diagnostic candidate byte grammar and final ID stability | Preserved |
| Direct-process self suppression and ownership conflicts | Preserved |
| Ordinary ReleaseAdmissionV1 gate before SQLite | Preserved |
| Atomic checksummed UpgradeTransaction replacement | Preserved |
| Every non-validation pending/complete/readback recovery effect | Preserved |
| KnownGood commit decision and explicit rollback transaction | Preserved |
| Public release phase/event/UX/final-result projection | Preserved |
| SQLite WAL/FULL/foreign-key ordered readbacks | Preserved |
| Exact-artifact GLIBC_2.42 and oldest-runtime gates | Preserved |
| Managed ExecStart/timer readback and whole-pair rollback | Preserved |

The direct-process barrier introduces no deadlock contract: generation cutoff
already includes queue time, and the barrier only delays later worker spawn
until the process Host-read cut closes. It introduces no hidden self member:
membership requires PID, birth and executable device/inode, not inode alone.

The KnownGood truth table introduces no split success owner: only completed
`commit-decided` changes recovery direction, while published file, ready
admission and terminal commit remain ordered and verified. The event projection
does not reinterpret durable state; it reads manifest steps and results.

The two blocking findings above are the only new contradictions found in the
requested P, C and I pair surfaces.

## Required Closure Gate

An APPROVED rerun requires both remaining choices to become literal:

1. Map each oversized worker-envelope reason to one exhaustive AD-5 terminal
   report or one failed CollectionAttempt rule, including strictness and current
   pointer behavior.
2. Define candidate-validation behavior after original release-owner death:
   authenticated persisted recovery-owner rebinding with a fresh one-use
   request, or mandatory pre-decision rollback with no validation rerun.
3. Extend the named boundary and crash fixtures to assert those complete rules,
   not only the reason token or frame rejection.

All five named findings marked closed and every preserved contract above must
remain unchanged. No new technology research or product/UX change is required.

## Validation Record

| Validation | Command or method | Result |
| --- | --- | --- |
| Branch and target pin | `git branch --show-current`; `git rev-parse HEAD`; `sha256sum .../ARCHITECTURE-SPINE.md` | **PASS** — requested branch, base commit and exact frozen hash. |
| Required complete reads | Line-bounded reads through EOF for the 1,429-line spine and all four canonical sources | **PASS** — 3,457 live-source lines read after discarding prior-hash analysis. |
| BMAD architecture linter | `uv run .agents/skills/bmad-architecture/scripts/lint_spine.py --workspace .../architecture-srvls-2026-07-14` | **PASS** — `ok: true`, zero findings. |
| AD integrity | Ordered AD heading extraction compared with `seq 1 25` | **PASS** — AD-1 through AD-25 exactly once and in order. |
| ARCH-LIM integrity | Unique numeric ARCH-LIM extraction compared with `seq 1 23` | **PASS** — ARCH-LIM-1 through ARCH-LIM-23 all present with no unexpected ID. |
| Markdown lint | `markdownlint-cli2 --config .../.markdownlint-cli2.jsonc .../review-two-unit-remediation-rerun-2026-07-16.md` | **PASS** — one file, zero errors. |
| Whitespace/error check | `git diff --check` plus `git diff --no-index --check /dev/null <report>` | **PASS** — tracked diff and untracked report emit no whitespace errors. |
| Changed-file scope | `git status --short`; report path comparison | **PASS** — this reviewer added only this rerun report; the revised spine and other prior/concurrent reports were already present and remain untouched. |

## Final Blocking Status

**BLOCKED. Verdict: CHANGES REQUIRED.** Five named findings are literally
closed, but NEW-B02 and NEW-H03 retain one independently observable choice each.
An APPROVED result would waive the exact oversize and crash-recovery probes and
would not satisfy the two-independent-unit gate.
