---
title: "srvls Architecture Two-Unit Remediation Gate"
type: architecture-review
status: final
created: 2026-07-16
updated: 2026-07-16
reviewer: independent-configured-two-unit-reviewer
review_mode: adversarial-remediation-gate
reviewed_base_commit: d4515067af8314cadf979da7b17921fbafc92d21
reviewed_worktree_spine_sha256: d9128bcc347f553045198a5402f0b91f068013728460de64c6105ec3d57429b2
reviewed_artifact: _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md
verdict: changes-required
blocking_status: blocked
original_probe_count: 20
original_probes_closed: 18
original_probes_open: 2
finding_count: 7
blocking_findings: 3
high_findings: 4
---

<!-- markdownlint-disable MD013 MD025 -->

# Architecture Review: Two-Unit Remediation Gate

## Verdict

**CHANGES REQUIRED. Blocking status: BLOCKED for reconciliation, scoped
collection IPC, and release/recovery implementation stories.**

The redistillation closes the named technology findings and most of the prior
two-unit findings. Policy and Scope bytes are canonical, CollectionPlan
admission is one atomic repository operation, ordinary stateful entry is
crash-gated before SQLite, UpgradeTransaction replacement is checksummed and
write-ahead/write-after ordered, SQLite and ABI gates are explicit, managed
timer consumers have positive readback and rollback postconditions, UJ-5 is
repaired, and the requested fixture families are named.

It does not yet force all ten independently built units to interoperate. Two
original probes remain open: diagnostic allocation has no cross-process
pre-ID reference or ordinal partition, and process suppression has no unique
self set or selection direction. Five new literal seams also remain. Three are
blocking:

1. `AcceptedBaselineCutV1` freezes an ID and revision but not the baseline
   projection needed by a reconciler that is forbidden to read it later.
2. AD-25 omits the plan identity that AD-21 requires WorkerResultV1 to echo,
   does not define one byte-total nested envelope, and requires a complete valid
   CollectionPlan to fit a 32 MiB request despite no corresponding plan-size
   invariant.
3. AD-23 orders `persist known-good` before `commit transaction` while also
   requiring a successful release commit before KnownGood may be replaced.

The candidate-validator admission bypass and the release-event projection are
also not versioned enough for separate release and entry/presentation units.
The spine must remain `draft` until these seams close.

This review changes only this new report. It does not amend the spine, memlog,
`tasks.md`, product code, canonical PRD/UX artifacts, or any prior review.

## Review Target and Basis

The target is the frozen working-tree spine on branch
`feature-prof-fiddlesticks-architecture-remediation`, based on commit
`d4515067af8314cadf979da7b17921fbafc92d21`. Because the requested
redistillation was intentionally uncommitted during the independent gate, the
review pins the exact target by 1,176-line SHA-256
`d9128bcc347f553045198a5402f0b91f068013728460de64c6105ec3d57429b2`.

These required artifacts were read completely:

| Artifact | Lines |
| --- | ---: |
| Architecture `.memlog.md` | 142 |
| Current `ARCHITECTURE-SPINE.md` | 1,176 |
| Canonical `prd.md` | 823 |
| Canonical `addendum.md` | 63 |
| Canonical `DESIGN.md` | 329 |
| Canonical `EXPERIENCE.md` | 813 |
| `review-technology-acceptance-2026-07-16.md` | 193 |
| `review-two-unit-divergence-acceptance-2026-07-16.md` | 362 |
| `review-rubric-acceptance-2026-07-16.md` | 286 |

The BMAD architecture skill, headless contract, and reviewer-gate contract were
also read completely before review. Prior acceptance conclusions were treated
as immutable findings to retest, not as proof that matching words close the
underlying seam.

A parallel good-spine gate later converged on NEW-B01, the missing
WorkerResult plan echo, diagnostic byte grammar, process-owner ordering, and
oversized-plan disposition. This report confirms those findings independently.
It distinguishes NEW-B03, NEW-H03, and NEW-H04 as additional release seams
specific to literal I-A/I-B and release/presentation interoperability; the
rubric gate treated the higher-level release nouns as sufficient.

## Acceptance Standard

The unchanged standard from the prior two-unit review is literal
interoperability. Each exercised seam must force both units to share:

- one versioned data shape and byte representation;
- one owner and state-mutation path;
- one transaction or immutable read cut;
- one identity and time rule;
- one queue, deadline, cancellation, and admission rule;
- one output and crash-recovery result; and
- one deterministic fixture that tests a complete rule rather than inventing it.

A named type, fixture, or phase is not sufficient if two implementations can
still choose incompatible fields, bytes, ordering, or recovery behavior.

## Same Ten Constructed Units

The same five pairs and ten next-level units were reconstructed without moving
responsibilities to make the remediation pass.

| Pair | Unit | Literal responsibility under the current spine |
| --- | --- | --- |
| 1 | P-A — Promise Lifecycle Command Unit | Validates declare/revise/renew/release/complete/revoke, samples Boot/Clock, and atomically appends the next sequenced lifecycle event plus projection revision. |
| 1 | P-B — Reconciliation and State Unit | Consumes the frozen plan and eligible reports, computes all canonical axes, labels, Brief, and change set, then requests the atomic Snapshot/Findings/current-pointer transaction. |
| 2 | C-A — Scoped Collection Worker Unit | Authenticates FD3, decodes one scope request, performs only scoped Host work, and returns a bounded typed report plus diagnostic candidates. |
| 2 | C-B — Snapshot Reducer and Persistence Unit | Admits plans, schedules scopes, validates worker results, closes cutoffs, assigns diagnostics, suppresses process duplicates, and requests the Snapshot transaction. |
| 3 | A-A — Action Intent Coordinator | Creates immutable ActionPlanV1, revalidates and consumes it, allocates OperationId, applies FR-40, and owns the terminal CAS. |
| 3 | A-B — Provider, Verification, and Terminal Effects Unit | Executes exact argv, emits launch/cancellation evidence, performs correlated verification, and restores the terminal without inventing an outcome. |
| 4 | K-A — Effective Configuration Compiler | Parses and merges sources, emits complete PolicySnapshotV1 bytes, PolicyFingerprint, and ProvenanceDigest. |
| 4 | K-B — Historical Policy and Finding Reader | Validates historical policy bytes and versions, renders materialized findings unchanged, and returns typed read-only results for unsupported versions. |
| 5 | I-A — Release Install Coordinator | Owns admission, transaction steps, activation, consumer validation, public events, known-good publication, rollback selection, and recovery orchestration. |
| 5 | I-B — SQLite Migration and Recovery Adapter | Implements backup, migration, restore, pragma/integrity verification, sidecar disposition, hashing, fsync, and exact effect readbacks. |

## Original Twenty-Probe Rerun

| Probe | Result | Current literal closure or remaining divergence |
| --- | --- | --- |
| `DVG-B01` mixed-time truth | **CLOSED EXCEPT ACC-B01 DERIVATIVE** | AD-21 atomically freezes Promise, policy, scope, operation, history, clock, and current revisions; the missing baseline projection is a narrower remaining input defect. |
| `DVG-B02` current Snapshot without Findings | **CLOSED** | AD-16 commits plan, reports, diagnostics, Observations, samples, Findings, decision references, and current CAS together. |
| `DVG-B03` two owners of current truth | **CLOSED** | Persisted latest-requested generation and the Snapshot pointer CAS are sole authority. |
| `DVG-B04` Action Plan interoperability | **CLOSED** | AD-22 defines PlanId, immutable captured fields, one consumption transaction, launch receipt, verification request, and terminal owner. |
| `DVG-B05` durability versus shutdown bound | **CLOSED** | AD-14 and AD-16 retain the last truthful nonterminal phase when storage or D-state work outlives the decision bound. |
| `DVG-B06` canonical policy fingerprint | **CLOSED** | AD-24 fixes object order, scalar normalization, exact escaping, integers, arrays, separators, domains, and rejection behavior. |
| `DVG-B07` upgrade-wide quiescence | **CLOSED FOR ORDINARY ENTRY; NEW-H03 OPEN FOR BYPASS** | ReleaseAdmissionV1 durably blocks all ordinary stateful entry before SQLite after a crash. The exceptional candidate bypass remains unbound. |
| `DVG-B08` crash-recoverable install state | **CLOSED FOR MANIFEST REPLACEMENT; NEW-B03 OPEN AT SUCCESS BOUNDARY** | Atomic replacement and pending/complete effects are explicit, but KnownGood publication contradicts the commit boundary. |
| `DVG-H01` event/projection disagreement | **CLOSED** | One Promise transaction assigns the gap-free sequence and projection revision. |
| `DVG-H02` Scope identity | **CLOSED** | AD-24 defines version, tags, field count, big-endian framing, raw-path normalization, display bytes, manifest order, and fingerprint. |
| `DVG-H03` obligation time travel | **CLOSED** | Obligation is frozen in the atomically admitted ScopeManifest and echoed by the worker. |
| `DVG-H04` diagnostic references | **OPEN** | Final sorting moved after evidence, but candidate-to-Observation references and ordinal partition remain unspecified. See NEW-H01. |
| `DVG-H05` cutoff race | **CLOSED** | Atomic registry acceptance precedes both half-open deadlines; equality times out. |
| `DVG-H06` supersession/admission | **CLOSED** | Atomic admission and persisted latest-wins coalescing prevent old truth promotion. |
| `DVG-H07` cross-Provider deduplication | **OPEN** | Hint fields and retained suppression evidence exist, but self membership and winner direction remain ambiguous. See NEW-H02. |
| `DVG-H08` launch boundary | **CLOSED** | Durable launch authorization, LaunchReceiptV1, monotonic sequence, and post-sequence VerificationRequestV1 are shared. |
| `DVG-H09` terminal outcome ownership | **CLOSED** | OperationCoordinator alone applies FR-40 and terminal CAS. |
| `DVG-H10` historical decision version | **CLOSED** | Materialized findings plus decision-contract version render unchanged; re-evaluation creates a new generation. |
| `DVG-H11` backup/restore contract | **CLOSED** | StateBackupManifestV1 and typed coordinator effects fix sidecars, hashes, schema, integrity, and fsync behavior. |
| `DVG-M01` artifact policy closure | **CLOSED** | Every governed artifact references one complete PolicySnapshotV1; unsupported versions are read-only. |

**Original-probe result: 18 of 20 closed.** The two failures are semantic;
the deterministic linter cannot detect them.

## Requested Remediation Seam Audit

| Requested seam | Result | Evidence and attack result |
| --- | --- | --- |
| Accepted Baseline in CollectionPlanV1 | **FAIL** | ID/revision/compatibility are frozen, but the projection required to compute FR-27 changes is absent and later baseline reads are forbidden (`SPINE:728-755`). |
| Nonterminal operation cut | **PASS** | Exact target and durable phase for every nonterminal operation plus repository revision are frozen (`SPINE:730-742`). |
| Resource history cut | **PASS AS RECONCILIATION INPUT** | Eligible immutable sample IDs and rows plus revision are frozen and pinned (`SPINE:732-744`). Its full replication to workers creates NEW-B02. |
| Current repository and prior-current cuts | **PASS** | Repository revision, prior-current Snapshot, and pointer revision share admission (`SPINE:723-735`). |
| Paired boot and UTC wall cut | **PASS** | One ClockSampleV1 stamps Snapshot, Evidence Window, samples, and Brief; later wall reads are diagnostic-only (`SPINE:721-723`, `756-758`). |
| Atomic CollectionPlan admission | **PASS** | Generation allocation, all cuts, plan insert, pins, and latest-requested update are one BEGIN IMMEDIATE operation or none (`SPINE:719-744`). |
| Canonical PolicySnapshot JSON | **PASS** | Scalar, string, object, array, integer, separator, and rejection grammar is byte-complete (`SPINE:896-920`). |
| Canonical ScopeId/Manifest grammar | **PASS** | Tags, lengths, integer widths, Provider normalization, path bytes, display, order, and fingerprint are complete (`SPINE:922-940`). |
| Post-evidence diagnostic allocation | **FAIL** | Evidence-first sort exists, but no shared pre-ID reference and no per-scope/global ordinal partition exist (`SPINE:431-439`). |
| Deterministic process suppression | **FAIL** | Exact evidence and retained conflict output exist; self PID membership and winner direction do not (`SPINE:446-463`). |
| AD-25 routing, peer auth, framing, streams, exits, signals, no discovery | **FAIL AS A TOTAL WIRE CONTRACT** | Route and mechanics are explicit, but WorkerResult omits the required plan echo, nested JSON representations remain unbound, and a valid plan may exceed the request cap (`SPINE:947-990`). |
| ReleaseAdmissionV1 before SQLite | **PASS FOR ORDINARY ENTRY** | Shared admission rejects nonterminal/torn recovery state before any SQLite open (`SPINE:800-813`). |
| Candidate-validator bypass | **FAIL** | The exceptional inherited bypass has no versioned type, transport, peer binding, single-use rule, or cross-version rejection contract (`SPINE:814-816`). |
| Atomic UpgradeTransaction replacement | **PASS** | Unique same-directory temp, no-follow, file fsync, rename, directory fsync, checksum, and reader rejection are explicit (`SPINE:818-828`). |
| Pending/complete ordering for every effect | **PASS** | Every named effect records fsynced pending before execution and complete only after readback (`SPINE:830-847`). |
| KnownGood retention and explicit rollback | **FAIL AT PUBLICATION ORDER** | Exactly one bundle and rollback-as-new-transaction exist, but it is persisted before the commit required to replace it (`SPINE:830-869`). |
| Durable step to public event mapping | **FAIL** | Public phases and event fields exist, but most internal steps have no unique phase mapping and canonical UX `skipped-with-reason` has no event result (`SPINE:871-881`; `DESIGN:302-314`). |
| SQLite WAL/FULL/FK ordered readbacks | **PASS** | Fresh/existing initialization fails closed on `wal`, numeric `2`, and `1` before any transaction (`SPINE:518-532`). |
| GLIBC_2.42 ABI and oldest-runtime gate | **PASS** | Exact-artifact `readelf` threshold and same-artifact oldest-runtime smoke are required (`SPINE:393-402`). |
| Managed ExecStart and timer validation | **PASS** | Both named services and every managed absolute path are rewritten/read back; timer trigger, service result, status, and whole-pair rollback are required (`SPINE:406-417`, `852-859`). |
| UJ-5 and related traces | **PASS** | UJ-5 now names AD-5, AD-16, AD-18, AD-20, AD-21 and retained history (`SPINE:1129-1145`). |
| Named property/concurrency/crash/IPC/timer/rollback fixtures | **PRESENT, NOT CURATIVE** | AD-11 names every requested family (`SPINE:355-386`), but fixtures cannot choose the missing contracts identified below. |

## Tier 0 — Blocking Findings

### NEW-B01 — AcceptedBaselineCutV1 cannot supply the required change projection

AD-21 enumerates the frozen baseline cut as state, acceptance ID/revision,
baseline Snapshot ID/revision, and compatibility result (`SPINE:728-729`). It
does not include the compatible materialized baseline Snapshot/Findings
projection or the exact rows needed to compare new, resolved, changed, and
persisting truth. AD-18 and AD-21 then prohibit a later baseline repository
read (`SPINE:601-635`, `SPINE:752-758`).

Two P-B implementations cannot both satisfy this. One dereferences the pinned
Snapshot after worker completion, violating the no-late-read rule. The other
uses only the enumerated cut and cannot compute FR-27 or answer FR-28. A third
may silently interpret `Snapshot ID and revision` as an embedded projection,
but that is a different wire and persistence shape from the literal field list.

This remains the exact compatible-baseline-projection portion of ACC-B01. The
fix is to include the immutable, schema-versioned baseline comparison
projection in `AcceptedBaselineCutV1` during `admit_collection`, or define an
equally explicit repository snapshot handle whose reads are part of the same
frozen transaction semantics. The fixture must prove the reducer performs no
post-admission baseline lookup.

### NEW-B02 — The worker envelope cannot prove plan identity and is not total

AD-21 requires every worker to echo the exact plan identity and requires
reduction to reject a mismatch (`SPINE:749-751`). AD-25 also says the parent
rejects a plan mismatch (`SPINE:973-974`), but the exhaustive WorkerResultV1
order has protocol version, request ID, capability, ScopeId, result kind,
CollectorReport, diagnostic list, and capture accounting—no CollectionPlan ID
or fingerprint (`SPINE:967-972`). Request ID and capability authenticate one
exchange; they do not identify the policy, baseline, operation, history,
current-pointer, and ScopeManifest cut the worker claims it used. The required
comparison is impossible from the declared result shape.

AD-25 defines the outer length frame and field order, but not one JSON type and
encoding for several fields: UUID request ID, random 256-bit capability,
binary ScopeIdV1, absolute boottime value, reservations, tagged result/error
variant, or nested Provider payload/report. `AD-24 JSON rules apply` cannot
resolve those choices: AD-24 defines canonical PolicySnapshot/provenance JSON
and Scope binary/display bytes, but never says whether the IPC Scope or
capability is a percent string, hex string, byte array, or another typed object
(`SPINE:896-940`, `SPINE:962-974`). Schema order alone is not a versioned data
shape.

The request also requires the **complete** CollectionPlanV1 while capping the
frame at 32 MiB (`SPINE:962-969`). A valid plan can include the complete
Promise cut, up to 10,000 nonterminal operations, and every eligible retained
resource-sample row under a state ceiling far above 32 MiB. No plan-size
invariant or admission outcome makes those contracts compatible. One parent
can prune history and send a plan reference, one can reject collection, and one
can raise the cap; each choice violates a different literal rule.

Close this by defining one domain-separated CollectionPlan ID/fingerprint in
both request and result, byte-level field types, and tagged-union presence
rules. Then send the worker a bounded `CollectionScopeRequestV1` containing
that plan fingerprint/revision and only its frozen scope assignment and
Provider inputs.
Keep baseline, operation, and history cuts in the parent/reducer plan. Or bind
a CollectionPlan size limit and one typed pre-dispatch failure, with admission
validation proving every valid plan fits. Add maximum-valid-plan and nested
byte-vector goldens, not only malformed-frame tests.

### NEW-B03 — KnownGoodReleaseV1 crosses the wrong success boundary

The ordered effect list persists KnownGood before ready admission and commit
(`SPINE:830-837`). The later rule says only a successful release commit may
replace the single KnownGood record (`SPINE:861-869`). Both cannot be literal.

If the process or storage fails after `persist known-good` completes but before
ready admission or transaction commit, I-A can recover forward and keep the
new record, while another conforming recovery can select rollback and still
find the old rollback record already erased. This is exactly the supported
post-validation rollback boundary; successful validation is necessary but the
spine itself says successful commit is the publication condition.

Close this with a staged KnownGood candidate owned by UpgradeTransactionV1 and
one explicit publication point after the commit decision. If atomic publication
cannot share one rename with admission/transaction files, specify the
write-ahead pointer/generation protocol and recovery truth table for every
crash between validation, KnownGood publication, ready admission, and terminal
commit. The existing post-validation rollback fixture must crash at each edge.

## Tier 1 — High Findings

### NEW-H01 — Diagnostic IDs still lack a cross-unit construction protocol

The coordinator now correctly allocates after evidence, but
`DiagnosticCandidateV1` has no stable pre-ID reference used by an Observation
inside WorkerResultV1. C-A can reference a candidate-list index, its full tuple,
or a worker-local key; C-B can expect any other choice. AD-5's final Snapshot
requires Observations to reference DiagnosticIds, which do not exist when C-A
encodes its report.

The ordinal domain is also unstated. Because DiagnosticId already contains
ScopeIdV1, one coordinator can reset `u32` ordinals to zero per scope while
another assigns one generation-global sequence after sorting all candidates.
Both satisfy “gap-free ordinals from zero exactly once” at `SPINE:431-439`, but
persist different IDs. Coordinator diagnostics without a natural Provider
scope make the choice observable.

The sort tuple itself is not byte-total. “Canonical subject bytes” does not
define a tagged subject union, and “AD-24 canonical parameter bytes” points to
a section that defines Policy/Provenance JSON and Scope bytes, not diagnostic
integer, raw-byte, path, absent-value, or structured-parameter variants. Two
producers can therefore sort the same evidence differently before the
coordinator ever reaches the ordinal-partition choice.

Define one candidate key/reference in CollectorReportV1, a tagged byte-complete
subject and parameter grammar, the exact duplicate-occurrence rule, the ordinal
partition, and how generation-level coordinator diagnostics obtain a ScopeId
or a separate ID variant. Then make the property fixture compare C-A bytes to
C-B final references.

### NEW-H02 — Process suppression does not define one self set or winner

AD-13 requires a self hint to match executable device/inode, but never limits
“self” to the current parent/worker PID set. One process worker can suppress
only the collection invocation and descendants; another can suppress every
concurrent `srvls` process using the same installed inode. Both satisfy
`self-executable` at `SPINE:446-455`, but the latter hides an unrelated runtime.

For non-self conflicts, the rule says select by strength
`self < exact Provider PID < cgroup`, then Provider tag and Scope bytes, without
saying whether the least or greatest value wins (`SPINE:454-461`). One reducer
selects the exact-PID claimant; another selects the cgroup claimant. Suppression
survives in both, but selected ownership, conflict evidence, correlation, and
Snapshot bytes differ.

Define the exact self PID/birth set carried in CollectionPlan or worker payload,
state whether the first or last ordered rule wins, and give every Provider tag
an explicit tie order. Retain the current weak-evidence and conflict behavior.

### NEW-H03 — The candidate-validator bypass can diverge or bypass the gate

ReleaseAdmissionV1 correctly gates ordinary entry, then creates one exceptional
“transaction-bound inherited read-only bypass” for the candidate validator
(`SPINE:800-816`). No versioned type, FD or handle, peer identity, capability,
single-use rule, install-generation binding, schema compatibility, or stable
failure result is defined.

I-A may pass an environment token, inherited FD, argv value, or implicit parent
state. The candidate entry may expect another mechanism. An environment-only
implementation is also forgeable by the same local principal and weakens the
guarantee that every stateful entry is gated before SQLite. This seam crosses
old and candidate binary versions, so shared in-process types do not close it.

Define `ReleaseValidationBypassV1` with one authenticated inherited transport,
transaction/install generation and candidate hash, one read-only capability,
one-use lifetime, no forwarding to timer consumers, and fail-closed mismatch
behavior before SQLite. Add forged, replayed, stale-generation, old-version,
and attempted-write fixtures.

### NEW-H04 — ReleaseEventV1 does not completely project durable steps to UX

AD-23 lists seven public phases and four event results, but maps only rollback
steps to recovery (`SPINE:871-881`). It does not uniquely map persist-recovering,
backup, migrate/verify, consumer rewrite, daemon reload, loaded readback, timer
activation, candidate validation, KnownGood publication, ready admission, or
commit. Two I-A implementations can assign migration to `activate` or
`recovery`, and KnownGood publication to `recovery` or `commit`, while obeying
the written list.

The canonical install-phase contract also permits `pending`, `running`,
`passed`, `failed`, and `skipped-with-reason`, while ReleaseEventV1 exposes only
`started`, `succeeded`, `failed`, and `resumed` (`DESIGN:302-314`). There is no
mapping for pending or skipped and no rule for a resumed step's public running
state. The named event fixture cannot infer these choices.

Add a complete internal-step-to-public-phase table, event-to-UX-state table,
skip representation, and final machine-result rule for every forward failure,
automatic recovery, resumed recovery, and explicit rollback path.

## Constructed-Pair Conclusion

| Pair | Verdict | Reason |
| --- | --- | --- |
| P-A vs P-B | **NOT ACCEPTED** | Promise, operation, history, and clock cuts interoperate, but P-B cannot compute baseline change truth from the enumerated no-late-read plan. |
| C-A vs C-B | **NOT ACCEPTED** | Scope identity and cutoff close, but the FD3 nested shape/size, diagnostic reference partition, and process suppression still diverge. |
| A-A vs A-B | **ACCEPTED** | No new incompatibility was found in plan consumption, launch evidence, verification ordering, FR-40 ownership, or shutdown recovery. |
| K-A vs K-B | **ACCEPTED** | PolicySnapshot and Provenance canonical bytes now force one fingerprint and historical read contract. |
| I-A vs I-B | **NOT ACCEPTED** | Ordinary admission, transaction replacement, SQLite, ABI, and timer recovery close, but bypass, KnownGood publication, and public event projection do not. |

## Required Closure Gate

A PASS rerun requires all of the following:

1. Put the immutable compatible baseline comparison projection in the admitted
   plan and prove no late baseline read.
2. Make WorkerRequestV1 byte-total and size-total for every admitted plan, or
   send one bounded scope request while retaining full reconciliation cuts in
   the parent.
3. Define DiagnosticCandidate references and ordinal partition, plus the exact
   self PID set and winner direction for process suppression.
4. Version and authenticate the candidate-validator read-only bypass across
   release and candidate binary versions.
5. Publish KnownGood only at one crash-recoverable successful-commit boundary.
6. Map every internal release step and result to the canonical public and UX
   phase states, including skip and resumed recovery.
7. Extend the existing named fixtures with the exact maximum-size, cross-version,
   crash-edge, and cross-unit cases above.

Preserve all contracts marked closed in this report. No new broad technology
research is required.

## Validation Record

| Validation | Command or method | Result |
| --- | --- | --- |
| Branch and target pin | `git branch --show-current`; `git rev-parse HEAD`; SHA-256 of current spine | **PASS** — requested branch, base commit, and exact working-tree hash recorded. |
| Required complete reads | Line-bounded reads through EOF for memlog, spine, canonical PRD/addendum/UX, and three acceptance reports | **PASS** — every required artifact read completely. |
| Architecture linter | `uv run .agents/skills/bmad-architecture/scripts/lint_spine.py --workspace _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14` | **PASS** — `ok: true`; zero findings. |
| AD integrity | Ordered heading extraction | **PASS** — AD-1 through AD-25 exactly once; no gap or duplicate. |
| ARCH-LIM integrity | Ordered table-ID extraction | **PASS** — ARCH-LIM-1 through ARCH-LIM-23 exactly once; no gap or duplicate. |
| Semantic two-unit review | Same ten units and twenty probes plus every requested remediation seam | **FAIL** — NEW-B01 through NEW-B03 and NEW-H01 through NEW-H04. |
| Markdown lint | `markdownlint-cli2` with the canonical UX config against this report | **PASS** — one file, zero errors. |
| Whitespace/error check | `git diff --check` | **PASS** — no output. |
| Changed-file scope | `git status --short`; `git diff --name-only` | **PASS** — this reviewer added only this report; the spine and concurrent rubric/technology gate reports were already in the shared worktree, and all prior reports remain untouched. |

## Final Blocking Status

**BLOCKED. Verdict: CHANGES REQUIRED.** The remediation materially improves
the architecture and closes the named technology gate, but the current draft
is not yet a single interoperable build substrate for all ten lower units.
