---
title: "srvls Architecture Review: Independent Two-Unit Divergence"
type: architecture-review
status: final
created: 2026-07-16
updated: 2026-07-16
reviewer: Sir Fix-a-Lot
review_mode: independent-adversarial-two-unit-divergence
reviewed_artifact: _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md
verdict: changes-required
blocking_status: blocked
finding_count: 20
blocking_findings: 8
high_findings: 11
moderate_findings: 1
---

<!-- markdownlint-disable MD013 MD025 -->

# Architecture Review: Independent Two-Unit Divergence

## Verdict

**CHANGES REQUIRED.** The spine is materially stronger than the two July 16
inputs it absorbed, but it is not yet an enforceable one-level-down build
contract. All five requested seams admit at least two independent units that
obey every applicable AD literally and still cannot safely interoperate.

The attack produced **20 architecture holes: 8 blocking, 11 high, and 1
moderate**. No requested seam resisted divergence. The highest-risk failures
are mixed-time reconciliation, a current-Snapshot race between generations,
an undefined cross-process Action Plan handoff, an impossible unconditional
durable-outcome-on-shutdown promise, policy fingerprints with no canonical
preimage, and an upgrade window that can discard live writes on rollback.

**Blocking status: BLOCKED.** Promise/reconciliation integration, concurrent
Snapshot production, canonical action execution, historical policy reads, and
stateful install or rollback should not be divided into implementation stories
until the Tier 0 amendments in this report are incorporated into the spine.
Compatibility capture and a non-stateful Rust bootstrap remain separable, but
they do not close these seams.

This review is documentation-only. It does not amend the spine, its memlog,
`tasks.md`, product code, or any canonical PRD or UX artifact.

## Review Basis

The following inputs were read completely:

- `SPINE` — `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md`
- `PRD` — `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md`
- `ADD` — `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/addendum.md`
- `DESIGN` — `_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/DESIGN.md`
- `UX` — `_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md`
- `PRD-UX-REVIEW` — `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/reviews/review-prd-ux-reconciliation-2026-07-16.md`
- `OPS-REVIEW` — `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/reviews/review-live-operations-2026-07-16.md`

The spine's exact decision ranges used below are:

| Decision | Spine lines | Decision | Spine lines |
| --- | ---: | --- | ---: |
| AD-1 | 71–80 | AD-11 | 317–333 |
| AD-2 | 81–95 | AD-12 | 334–356 |
| AD-3 | 96–108 | AD-13 | 357–374 |
| AD-4 | 109–132 | AD-14 | 375–390 |
| AD-5 | 133–171 | AD-15 | 391–405 |
| AD-6 | 172–216 | AD-16 | 406–454 |
| AD-7 | 217–241 | AD-17 | 455–471 |
| AD-8 | 242–255 | AD-18 | 472–492 |
| AD-9 | 256–281 | AD-19 | 493–519 |
| AD-10 | 282–316 | AD-20 | 520–576 |

References such as `AD-17 (SPINE:455-471)` therefore identify both the exact
decision and its current text, rather than citing a general architecture
theme.

## Adversarial Method

For each high-risk seam, this review constructed independent implementation
units at the next level below the spine's Structural Seed. A unit was admitted
only when it met these conditions:

1. Dependencies point inward under AD-1.
2. Side effects cross an inward-owned port under AD-3.
3. Canonical aggregates, identities, outcomes, limits, and UX behavior are not
   renamed or weakened.
4. No unit relies on a forbidden Host, persistence, presentation, or shell
   shortcut.
5. Every unspecified shape, ownership boundary, transaction, time cut,
   ordering rule, or recovery choice is resolved locally in a reasonable way.

A divergence is viable when both units remain AD-literal in isolation but
cannot exchange data, make the same decision, preserve the same atomicity, or
recover the same state when integrated. Each viable divergence is an
architecture hole; implementation preference is not a valid closure.

The exercise deliberately did not assume that similarly named Rust structs
would converge by convention. If the spine does not define a shared type,
owner, ordering, or transaction, two stories are free to choose differently.

## Constructed Unit Pair 1: Promise Lifecycle vs Reconciliation and Storage

### Unit P-A — Promise Lifecycle Command Unit

`domain::promise` and `application::promises` accept declare, revise, renew,
release, complete, and revoke commands. The unit samples `Clock` and
`BootIdentity`, validates the actor and caller operation identity, creates a
UUIDv7 `EventId`, and calls `PromiseRepository` with an expected projection
revision. The SQLite adapter appends the event and updates the current
projection in one `BEGIN IMMEDIATE` transaction. Same-boot Lease and cadence
decisions use monotonic samples; wall time and boot identity are retained for
display and persistence.

P-A treats successful repository commit order as lifecycle order. Its current
projection is authoritative for command responses. Events are immutable audit
evidence, but the spine gives them no domain sequence beyond UUIDv7, time
provenance, and repository revision compare-and-swap.

This unit obeys AD-1, AD-2, AD-3, AD-13, AD-16, AD-17, AD-19, and AD-20
literally. It never collects Host truth or writes a Snapshot.

### Unit P-B — Reconciliation and State Unit

`application::reconcile` receives an immutable `Snapshot`, loads the current
Promise projection and lifecycle events through repository ports, and invokes
the pure AD-18 engine. P-B orders same-boot lifecycle evidence by monotonic
sample and `EventId`, because AD-17 makes monotonic time defensible while
AD-13 makes `EventId` typed. It opens its Promise read transaction only after
collection reduction so it uses the freshest committed intent.

P-B persists the immutable Snapshot and current pointer in the exact atomic
unit required by AD-16. It then persists the pure Reconciliation Findings in a
second transaction: AD-16 explicitly names the Snapshot/current-pointer
transaction and a findings schema family, but never places findings in that
transaction or declares them read-time-only.

This unit obeys AD-1, AD-2, AD-3, AD-5, AD-13, AD-16, AD-18, AD-19, and AD-20
literally. It neither mutates a Promise nor invents a Provider result.

### Pair 1 divergence probes

1. **Mixed-time truth (`DVG-B01`).** Generation 41 freezes its Collector jobs
   while Promise revision 7 is `lease-active`. The Host Observation is sampled.
   Before reduction, P-A commits revision 8 as `closed/completed`. P-B is
   permitted to reconcile the pre-closure Observation with revision 8 and emit
   `inactive + abandoned`. An equally literal P-B implementation can freeze
   revision 7 when generation 41 starts and emit `healthy`. AD-5 defines a
   collection generation, AD-17 defines Promise transitions, and AD-18 names
   both inputs, but no AD defines their common read cut.

2. **Projection/event disagreement (`DVG-H01`).** Two accepted commands obtain
   monotonic samples before contending on the repository. P-A folds in
   successful CAS/commit order. P-B may refold the required lifecycle events
   in monotonic-sample and UUID order. AD-16 says revision compare-and-swap and
   deterministic ID order; AD-17 says explicit events plus one current
   projection; AD-18 consumes both. None says which is authoritative or gives
   lifecycle events a canonical per-Promise sequence.

3. **Current Snapshot without its findings (`DVG-B02`).** The Snapshot and
   pointer transaction commits, then the process crashes before P-B's findings
   transaction. On restart, the repository has current Host truth but no exact
   finding set or Brief that governed that pointer. Computing findings now can
   observe newer Promise state or code. Persisting findings in the first
   transaction is also AD-literal, so storage stories can choose incompatible
   atomic units.

## Constructed Unit Pair 2: Collection Workers vs Snapshot Reduction

### Unit C-A — Scoped Collection Worker Unit

Each worker receives a generation, raw Provider locator, effective obligation,
deadline, and capture reservations. It dispatches supervised same-binary work
through `CommandRunner`, normalizes Provider output, and returns one report.
Its natural report contract is:

```text
WorkerReport {
  generation: GenerationId,
  scope: { provider: Provider, locator: ProviderOwnedString },
  obligation: EffectiveObligation,
  outcome: CollectorOutcome,
  observations: Vec<Observation<LocalDiagnosticRef>>,
  diagnostics: Vec<(LocalDiagnosticRef, Diagnostic)>,
  completed_at: BootInstant,
  duration: Duration
}
```

The worker freezes obligation at dispatch, assigns diagnostic ordinals within
the report, and reports completion when the supervised invocation returns. A
process worker performs Provider-child suppression locally using the Provider
and parent evidence available when it runs. Superseding a generation drops
delivery but does not automatically cancel its supervised work.

C-A obeys AD-1, AD-2, AD-3, AD-5, AD-10, AD-13, AD-15, and AD-20 literally.

### Unit C-B — Snapshot Reducer and Persistence Unit

The reducer builds an ordered effective scope manifest, promotes optional
scopes from active Promises, schedules the exact LPT lanes, and waits until the
generation cutoff. Its natural contract uses canonical scope keys and
Snapshot-owned diagnostic identities:

```text
ReducedGeneration {
  generation: GenerationId,
  reports: BTreeMap<CanonicalScopeId, ScopeReport<DiagnosticId>>,
  observations: BTreeMap<ObservationId, Observation>,
  diagnostics: BTreeMap<DiagnosticId, Diagnostic>,
  policy_fingerprint: PolicyFingerprint,
  scope_set_fingerprint: ScopeSetFingerprint
}
```

C-B recomputes effective obligation at reduction so an active Promise created
during collection is not ignored. At the cutoff it accepts only reports
already received by the reducer, synthesizes the rest as `timed-out`, performs
cross-report deduplication, and commits every fully reduced candidate. It lets
presentation suppress a non-latest generation from displayed truth, because
AD-10 says only the latest may replace displayed truth while AD-5 says every
fully reduced candidate becomes current truth.

C-B obeys AD-1, AD-2, AD-3, AD-5, AD-10, AD-13, AD-16, AD-19, and AD-20
literally.

### Pair 2 divergence probes

1. **No shared scope identity (`DVG-H02`).** C-A's `{provider, locator}` can
   distinguish Docker by endpoint, context name, or both; C-B's
   `CanonicalScopeId` can key by configured alias. AD-10 requires a canonical
   scope ID for scheduling and AD-5 uses scope set for baseline compatibility,
   but neither defines its type, locator normalization, or equality. The units
   can disagree on cardinality, report lookup, LPT tie-breaking, and baseline
   compatibility while preserving every named outcome.

2. **Obligation time travel (`DVG-H03`).** C-A returns the effective obligation
   it was given, as AD-5 requires. C-B also implements AD-5's shared scope
   promotion and can recompute it from newer Promise state. A mid-generation
   declaration can therefore make the same failed report optional in one
   implementation and required in another, changing strict exit, absence
   claims, baseline eligibility, and mutation availability.

3. **Diagnostic reference mismatch (`DVG-H04`).** AD-5 says Snapshot owns
   diagnostics and Observations reference diagnostic IDs, but AD-13 does not
   define `DiagnosticId`. C-A can validly emit scope-local ordinals; C-B can
   validly require global UUIDs or generation-qualified keys. Sorting or
   merging without a shared remap contract can attach a diagnostic to the wrong
   Observation or make the units fail to integrate at all.

4. **Cutoff race (`DVG-H05`).** A worker can finish at the cutoff and enqueue a
   report that reaches C-B immediately after the reducer synthesizes
   `timed-out`. One implementation adjudicates by worker completion time;
   another by reducer receipt time. AD-10 says the reducer stops waiting and
   that completion order cannot affect content, but it defines no half-open
   boundary or atomic result-registration event.

5. **Two owners of current truth (`DVG-B03`).** Generation 42 is requested
   while 41 reduces. AD-5 says 41's fully reduced candidate commits and becomes
   current truth. AD-10 says only 42 may replace displayed truth. C-B can move
   the repository pointer to 41 while the TUI continues displaying its prior
   Snapshot under a latest-generation guard. Another reducer can CAS-reject
   41's pointer move. Both are literal; inspection, action planning, and the TUI
   can then disagree about what `current` means.

6. **Supersession and pool admission (`DVG-H06`).** AD-10 says dropped delivery
   is not cancellation and gives each generation typed cancellation, but it
   does not say whether a new refresh cancels undispatched old scopes, requests
   cancellation of running scopes, queues behind them, or coalesces requests.
   FIFO generations and latest-wins generations both satisfy the fixed pool and
   generation guards but give radically different freshness and starvation
   behavior.

7. **Cross-Provider process deduplication owner (`DVG-H07`).** AD-13 requires
   direct collection to deduplicate Provider-owned children. C-A can suppress
   candidates from local parent or command evidence before other reports
   exist. C-B can wait for exact systemd, Docker, and PM2 identities and dedupe
   globally. Under partial Provider evidence the two strategies emit different
   current Observations, yet the spine never assigns this policy to worker or
   reducer or defines retained suppression evidence.

## Constructed Unit Pair 3: Action Planning vs Execution, Verification, and Shutdown

### Unit A-A — Action Intent Coordinator

The application coordinator loads an exact target, immutable policy, safety
evidence, and source generation, then produces a read-only Action Plan. To keep
`action plan` read-only across separate CLI processes, A-A encodes the captured
plan as a versioned, self-contained textual `PlanRef` containing Snapshot ID,
target identity, verb, policy fingerprint, expiry, confirmation requirements,
and an integrity digest. It allocates an `OperationId` only when execute is
submitted. It expects Provider and verifier ports to return evidence; the
application coordinator alone applies FR-40 precedence and asks
`OperationRepository` to terminalize by revision CAS.

A-A obeys AD-1, AD-2, AD-3, AD-5, AD-6, AD-13, AD-16, AD-18, AD-19, and AD-20
literally. It performs no Host mutation while planning.

### Unit A-B — Provider, Verification, and Terminal Effects Unit

The effects unit resolves the exact Provider target, revalidates identity,
persists `launch-authorized` through an application callback, spawns the typed
argv operation, runs an OperationId-correlated targeted collection, and owns
the `TerminalSession` effect boundary. Its independently reasonable plan port
expects a structured `PlanKey { snapshot_id, target_id, verb, digest }` and
reconstructs the plan from the retained Snapshot and policy. It treats the
successful spawn call as the Provider launch boundary; another valid adapter
could treat `launch-authorized`, process creation, or first post-spawn poll as
that boundary.

Following AD-14, A-B maps phase-specific signals into a typed
`ShutdownDisposition`, including a proposed refused, failed, or
executed-unverified terminal result, and expects the application to persist it
before terminal restoration. At AD-20's finalization bound it restores the
terminal even if SQLite remains unavailable.

A-B obeys AD-1, AD-3, AD-6, AD-10, AD-13, AD-14, AD-15, AD-16, and AD-20
literally. It uses no shell, never retargets by display data, and never detaches
a submitted operation.

### Pair 3 divergence probes

1. **Action Plan is not an interoperable entity (`DVG-B04`).** AD-6 requires a
   plan with identity, generation, policy, lifetime, idempotent retry, and later
   execution. AD-13 defines Promise, Snapshot, Operation, and Event IDs but no
   `PlanId`; AD-16 defines operation phases but no Action Plan family; AD-5
   calls canonical planning read-only. A-A's self-contained plan and A-B's
   reconstructable key both satisfy those words, but they cannot exchange the
   UX-IP-11 `PLAN_ID`, preserve the same captured safety, or return the same
   original plan on retry.

2. **Provider launch boundary is not a shared fact (`DVG-H08`).** AD-6 requires
   verification evidence sampled after the Provider launch boundary and
   correlated to `OperationId`. AD-16 requires `launch-authorized` before the
   Provider may launch. Neither defines the typed launch receipt, whether spawn
   success means launch occurred, the monotonic ordering relation, or what a
   timeout proves. A verifier can admit pre-effect evidence that another
   verifier correctly rejects.

3. **Terminal outcome has competing semantic owners (`DVG-H09`).** AD-3 places
   action use cases in application, AD-6 defines terminal precedence, and
   AD-14 requires Update to implement phase-specific shutdown behavior. A-A can
   require raw execution and verification evidence so it alone chooses the
   outcome. A-B can reasonably return a typed shutdown outcome required by
   AD-14. If late verification proves success while a signal proposes
   executed-unverified, integration order rather than FR-40 precedence can win.

4. **Durability and shutdown bounds cannot both be unconditional
   (`DVG-B05`).** AD-14 requires exactly one durable truthful outcome and
   restoration; AD-16 says a submitted operation is terminalized durably and
   recovery never auto-replays; AD-20 gives finalization a bounded deadline.
   SQLite can remain busy, unavailable, full, or blocked past that bound. A-A
   can wait for durability and violate bounded shutdown. A-B can restore and
   exit at the bound, leaving only the last nonterminal phase. No implementation
   can guarantee both under the failures AD-16 itself requires the product to
   surface.

## Constructed Unit Pair 4: Configuration vs Historical Policy Interpretation

### Unit K-A — Effective Configuration Compiler

The config adapter parses and validates every source independently, merges in
AD-19 precedence, and creates a typed immutable `EffectivePolicy`. Each field
retains value, units, winning source, override chain, default, and range. K-A
computes `PolicyFingerprint` as SHA-256 over canonical effective typed values
in schema-declaration order; provenance is retained beside the fingerprint but
does not affect it. Equivalent values from a moved config file therefore keep
the same governing-policy identity.

K-A obeys AD-1, AD-3, AD-7, AD-19, and AD-20 literally.

### Unit K-B — Historical Policy and Finding Reader

The storage side persists a versioned JSON policy payload with each artifact.
It independently computes `PolicyFingerprint` over effective values plus the
ordered provenance chain, because AD-19 says artifacts retain both and says a
new policy invalidates plans. It stores only fields that affected the artifact:
collection fields for a Snapshot, reconciliation fields for a Finding, and
action fields for a plan or operation. When displaying old findings, K-B loads
the retained values and invokes the current pure AD-18 engine.

K-B obeys AD-1, AD-2, AD-3, AD-16, AD-18, AD-19, and AD-20 literally. It does
not substitute today's configuration values for retained values.

### Pair 4 divergence probes

1. **Policy fingerprint has no canonical preimage (`DVG-B06`).** AD-5 uses the
   governing policy fingerprint for baseline compatibility; AD-6 uses it for
   plan validity; AD-19 requires values, provenance, and a fingerprint. It does
   not name a hash, canonical serialization, field set, unit normalization,
   schema version, or whether provenance participates. K-A and K-B produce
   different fingerprints for identical effective behavior, causing needless
   baseline replacement and action refusal. The reverse choice can treat a
   provenance change as compatible when a story expected it to invalidate.

2. **Historical decisions are not version-pinned (`DVG-H10`).** Retaining old
   values does not prevent reinterpretation by a later AD-18 implementation.
   K-B can recompute an old Finding under current correlation, safety, or
   attention code while truthfully using the retained policy. Another unit can
   render the materialized stored Finding. AD-19 prevents later configuration
   reinterpretation but does not retain a decision-contract or engine version,
   so historical answers can change after upgrade.

3. **Artifact policy closure is undefined (`DVG-M01`).** “Governing values” can
   mean the complete effective policy or only fields observed by that artifact.
   Full snapshots make schema evolution and comparison predictable but repeat
   unrelated values; subsets minimize data but cannot prove that a newly added
   policy field was absent rather than defaulted. Both K-A and K-B preserve
   provenance literally, yet an older binary cannot reliably compare or
   explain a newer artifact.

## Constructed Unit Pair 5: Installer vs Schema Rollback

### Unit I-A — Release Install Coordinator

The installer stages one versioned binary, verifies SHA-256, runs compatibility
smoke, acquires a state lock, requests a validated pre-migration backup,
requests embedded migration, atomically repoints the executable symlink, runs
the named consumer checks, and either commits or requests rollback. It releases
the database lock before consumer validation so the activated candidate can
open state. It retains the old target and a backup path until checks pass.

I-A obeys AD-9, AD-11, AD-12, AD-15, and AD-20 literally.

### Unit I-B — SQLite Migration and Recovery Adapter

The state adapter takes an exclusive SQLite migration lock, uses the SQLite
backup API, validates integrity and schema, applies forward migrations in a
transaction, and records `schema_migrations`. It assumes the caller prevents
old binaries and other writers from opening state between backup and final
commit. Rollback restores the validated database image and removes or replaces
associated WAL and shared-memory state while no connection is open.

I-B obeys AD-1, AD-3, AD-12, AD-16, AD-19, and AD-20 literally.

### Pair 5 divergence probes

1. **No upgrade-wide quiescence boundary (`DVG-B07`).** AD-12 says “locks
   state” but does not define who participates or how long the lock lives. If
   I-A releases the SQLite lock for validation, an already running old TUI or a
   Promise command can write after the backup and before rollback. Restoring
   the matching backup then loses accepted lifecycle events or operation
   outcomes. Holding an exclusive SQLite lock through validation instead can
   make the new binary's state and consumer checks fail with the configured
   busy timeout. Both choices obey the current sequence.

2. **No crash-recoverable install state machine (`DVG-B08`).** A process can
   die after backup, after migration but before link swap, after activation but
   before validation, or during rollback. AD-12 names the happy-path order and
   final recovery result but defines no durable upgrade transaction ID, phase
   journal, fsync boundary, or idempotent resume rule. The database cannot own
   the only journal because rollback replaces it with the pre-upgrade backup.
   I-A and I-B can each recover their local artifact while choosing opposite
   binary/database pairs.

3. **Backup and restore are not one typed contract (`DVG-H11`).** AD-12
   requires a validated matching backup; AD-16 specifies WAL, sidecars, FULL
   synchronization, and exclusive migration. It does not assign checkpoint,
   backup API, database/WAL/SHM replacement, file and directory fsync, hash,
   schema metadata, or restore verification to a port. A file-copy installer
   and an online-backup adapter can both claim compliance but produce backups
   with different recovery guarantees.

## Tier 0 — Blocking Findings and Smallest Enforceable Amendments

| ID | Architecture hole | Exact ADs | Smallest enforceable amendment |
| --- | --- | --- | --- |
| DVG-B01 | Promise state and collected evidence have no common reconciliation cut. | AD-5 (SPINE:133-171), AD-16 (SPINE:406-454), AD-17 (SPINE:455-471), AD-18 (SPINE:472-492), AD-19 (SPINE:493-519) | Add a versioned `CollectionPlan` created in one consistent repository read. It must freeze the Promise projection/event revision set, effective policy snapshot, scope manifest, boot identity, and generation start. Collect, promote obligations, reconcile, and persist only against that frozen cut; later Promise writes wait for the next generation. |
| DVG-B02 | Snapshot/current pointer and the findings that explain them can commit separately. | AD-2 (SPINE:81-95), AD-5 (SPINE:133-171), AD-16 (SPINE:406-454), AD-18 (SPINE:472-492) | Amend AD-16's Snapshot atomic unit to include scope reports, diagnostics, Observations, reconciliation inputs/revision references, materialized Findings, policy reference, and current-pointer CAS. Alternatively declare Findings never durable and remove their schema family; do not permit both models. |
| DVG-B03 | AD-5 and AD-10 allow persisted current truth and displayed latest truth to name different Snapshots. | AD-5 (SPINE:133-171), AD-10 (SPINE:282-316), AD-16 (SPINE:406-454) | Define one persisted `latest_requested_generation` and require current-pointer CAS to succeed only for that generation. A superseded candidate may be retained as historical attempt evidence but never becomes repository or displayed current truth. Amend AD-5's unconditional “becomes current” sentence accordingly. |
| DVG-B04 | Action Plan has no shared identity, representation, persistence, or submit boundary. | AD-3 (SPINE:96-108), AD-5 (SPINE:133-171), AD-6 (SPINE:172-216), AD-13 (SPINE:357-374), AD-16 (SPINE:406-454) | Add `PlanId`, `ActionPlan`, and `ActionPlanRepository` contracts. Specify exact fields, UUID/version, idempotency tuple, creation/expiry, consumption CAS, and that `OperationId` is allocated only at submit. Clarify that canonical planning is Host-read-only but may atomically persist this bounded immutable plan so the separate execute process can retrieve the original. |
| DVG-B05 | Exactly one durable terminal outcome and a hard finalization/exit bound cannot both be guaranteed when SQLite is unavailable. | AD-14 (SPINE:375-390), AD-16 (SPINE:406-454), AD-20 / ARCH-LIM-22–23 (SPINE:520-576) | State the failure exception explicitly: terminal restoration remains bounded; finalization makes bounded attempts; on storage failure the last durable `launch-authorized`, `executing`, or `verifying` phase remains and next-start recovery resolves it. Do not promise a durable terminal outcome before forced exit when the sole durable store cannot write. |
| DVG-B06 | `PolicyFingerprint` has no canonical preimage, so baseline and plan compatibility are implementation-defined. | AD-5 (SPINE:133-171), AD-6 (SPINE:172-216), AD-16 (SPINE:406-454), AD-19 (SPINE:493-519), AD-20 (SPINE:520-576) | Define `PolicySnapshotV1`, canonical field order and base units, canonical encoding, fingerprint algorithm/domain separator, exact governing field set, and whether provenance is excluded. Use a separate `ProvenanceDigest` if provenance changes must be visible without changing behavioral compatibility. |
| DVG-B07 | Upgrade does not quiesce old and new state writers across backup, migration, validation, and possible restore. | AD-12 (SPINE:334-356), AD-16 (SPINE:406-454), AD-20 / ARCH-LIM-14 (SPINE:520-576) | Add an install-generation admission lock outside ordinary SQLite transactions. Every stateful process holds a shared generation lease; installer obtains exclusive quiescence before backup and retains it through validation or rollback. Validation is explicitly read-only and receives a scoped bypass token. No lifecycle, baseline, Snapshot, or operation write is admitted in the rollback window. |
| DVG-B08 | Install/rollback has no durable, idempotent crash state machine. | AD-9 (SPINE:256-281), AD-12 (SPINE:334-356), AD-16 (SPINE:406-454) | Define a permission-restricted, fsynced `UpgradeTransactionV1` manifest that is explicitly exempted from SQLite domain truth. It binds transaction ID, old/new target and hashes, old/new schema, backup path/hash, link target, and phases `staged`, `backed-up`, `migrated`, `activated`, `validated`, `rollback-started`, `recovered`, `committed`. Every installer entry resumes or reverses it idempotently before new work. |

## Tier 1 — High Findings and Smallest Enforceable Amendments

| ID | Architecture hole | Exact ADs | Smallest enforceable amendment |
| --- | --- | --- | --- |
| DVG-H01 | Lifecycle event replay can disagree with the transactionally maintained projection. | AD-13 (SPINE:357-374), AD-16 (SPINE:406-454), AD-17 (SPINE:455-471), AD-18 (SPINE:472-492) | Give every accepted event a repository-assigned, gap-free per-Promise `event_sequence` and `prior_projection_revision`. Declare the projection through sequence N authoritative; reconciliation uses events only as evidence and never refolds them in a different order. |
| DVG-H02 | Scope identity, normalization, and equality are undefined. | AD-5 (SPINE:133-171), AD-10 (SPINE:282-316), AD-13 (SPINE:357-374), AD-20 / ARCH-LIM-3 (SPINE:520-576) | Add a domain `ScopeIdV1` tagged union with exact Provider locator fields and normalization, plus a canonical ordered `ScopeManifestV1`. The same manifest must drive LPT scheduling, report validation, scope-set fingerprinting, baseline compatibility, and persistence. |
| DVG-H03 | Effective Collection Obligation can change between dispatch and reduction. | AD-5 (SPINE:133-171), AD-17 (SPINE:455-471), AD-19 (SPINE:493-519) | Compute obligation once in the frozen `CollectionPlan` from its Promise revision and policy. Workers echo it; the reducer rejects a mismatch and never promotes against newer state. |
| DVG-H04 | Snapshot-owned diagnostic references have no type or remap rule. | AD-2 (SPINE:81-95), AD-5 (SPINE:133-171), AD-13 (SPINE:357-374), AD-16 (SPINE:406-454) | Define `DiagnosticId = (GenerationId, ScopeIdV1, u32 canonical_ordinal)` and the point at which the ordinal is assigned. Worker Observations and reducer persistence must use that exact type; no post-hoc positional remap is allowed. |
| DVG-H05 | Deadline equality and late report registration are nondeterministic. | AD-5 (SPINE:133-171), AD-10 (SPINE:282-316), AD-20 / ARCH-LIM-2–3 (SPINE:520-576) | Add a coordinator-owned atomic result registry and half-open rule: a report is eligible only when registered before both its scope deadline and generation cutoff; equality times out. Reducer mailbox delivery order cannot determine eligibility. |
| DVG-H06 | Overlapping generation admission, cancellation, and fairness are unspecified. | AD-5 (SPINE:133-171), AD-10 (SPINE:282-316), AD-20 / ARCH-LIM-1–3 (SPINE:520-576) | Specify latest-wins coalescing: persist the newest request, cancel undispatched older jobs, request typed cancellation of running old jobs, transfer blocked children to the bounded reaper at their cut, and admit only the newest queued generation. Define whether superseded attempt evidence is retained. |
| DVG-H07 | Provider-child suppression can occur locally or after cross-Provider reduction and yields different direct-process truth. | AD-5 (SPINE:133-171), AD-13 (SPINE:357-374), AD-18 (SPINE:472-492) | Assign cross-Provider attribution and deduplication to the reducer after all reports. The process worker emits bounded raw candidates plus ownership hints; reducer rules name exact identity evidence, partial-evidence behavior, and retained suppression diagnostics. |
| DVG-H08 | Provider launch boundary and OperationId-correlated verification have no shared data contract. | AD-3 (SPINE:96-108), AD-6 (SPINE:172-216), AD-10 (SPINE:282-316), AD-16 (SPINE:406-454) | Add `LaunchReceiptV1` and `VerificationRequestV1`. The coordinator records durable authorization, CommandRunner records spawn success or may-have-launched plus monotonic launch sequence, and verification registers a sample start strictly after that sequence. Every evidence row carries OperationId and verification generation. |
| DVG-H09 | Application, Adapter, and TUI shutdown can each appear to own the terminal Action Outcome. | AD-3 (SPINE:96-108), AD-6 (SPINE:172-216), AD-14 (SPINE:375-390), AD-16 (SPINE:406-454) | Name `OperationCoordinator` as the sole outcome authority. TUI emits only navigation or `CancellationRequest`; adapters emit only typed execution/cancellation evidence; verifier emits only evidence. The coordinator applies FR-40 and performs one terminal revision CAS; Update renders only the committed result. |
| DVG-H10 | Retained configuration does not pin the historical reconciliation algorithm. | AD-11 (SPINE:317-333), AD-16 (SPINE:406-454), AD-18 (SPINE:472-492), AD-19 (SPINE:493-519) | Persist a stable `decision_contract_version` with materialized Findings and Brief projections. Historical reads render stored results. Re-evaluation under a newer engine creates a new derived generation and never silently rewrites or relabels the old one. |
| DVG-H11 | Backup creation and restoration are not an owned typed port, including WAL/SHM and fsync rules. | AD-3 (SPINE:96-108), AD-12 (SPINE:334-356), AD-16 (SPINE:406-454) | Add `StateMigrationCoordinator` with `create_backup`, `migrate`, `restore`, and `verify` total results plus `StateBackupManifestV1`. Require SQLite backup API or an explicitly equivalent checkpointed method, database and parent-directory fsync, no live connections during restore, sidecar disposition, hashes, schema versions, and post-restore integrity verification. |

## Tier 2 — Moderate Finding and Smallest Enforceable Amendment

| ID | Architecture hole | Exact ADs | Smallest enforceable amendment |
| --- | --- | --- | --- |
| DVG-M01 | Artifacts can retain full policy or incompatible artifact-specific subsets. | AD-5 (SPINE:133-171), AD-6 (SPINE:172-216), AD-16 (SPINE:406-454), AD-19 (SPINE:493-519) | Store one complete normalized `PolicySnapshotV1` per unique fingerprint and reference it from Snapshots, Findings, baselines, plans, and operations. Readers that do not support its schema return typed `unsupported-policy-version` and remain read-only; they do not infer missing fields from current defaults. |

## Why No Seam Earned PASS

No requested seam reached the “cannot diverge” condition:

| Seam | Result | First irreducible divergence |
| --- | --- | --- |
| Promise lifecycle vs reconciliation/storage | Diverged | No common Promise/Snapshot read cut (`DVG-B01`) |
| Collection workers vs Snapshot reduction/persistence | Diverged | No shared scope or diagnostic identity, then conflicting current-generation semantics (`DVG-H02`, `DVG-B03`) |
| Action planning vs execution/verification/TUI shutdown | Diverged | No interoperable Action Plan entity and an impossible durability/bound combination (`DVG-B04`, `DVG-B05`) |
| Configuration vs historical policy interpretation | Diverged | No canonical policy fingerprint or decision-engine version (`DVG-B06`, `DVG-H10`) |
| Installer vs schema rollback | Diverged | No upgrade-wide quiescence or crash journal (`DVG-B07`, `DVG-B08`) |

Several lower-level contracts are already closed and were not findings:
Provider mutation targets are exact rather than display-derived under AD-6 and
AD-13; FR-40's five outcomes and precedence are explicit in AD-6; collection
and action pools are separate and bounded under AD-10 and AD-20; and SQLite is
the sole domain-state owner under AD-16. Those rules prevented weaker attacks,
but they do not determine the inter-unit handoffs above.

## Required Amendment Order

The smallest safe closure order is:

1. Define the frozen `CollectionPlan`, common Promise revision cut, canonical
   `ScopeManifest`, and latest-generation pointer CAS. This closes the input
   truth consumed by both collection and reconciliation.
2. Define the Snapshot transaction to include its exact materialized Findings
   and retained policy/decision references.
3. Define Action Plan identity and persistence, Operation submit boundary,
   launch/verification receipts, sole outcome owner, and the storage-failure
   exception to bounded shutdown.
4. Define canonical policy serialization/fingerprinting and historical
   decision-contract versioning.
5. Define upgrade-wide quiescence, the external upgrade transaction manifest,
   and the state-adapter-owned backup/restore port.
6. Add deterministic cross-unit contract fixtures for every type, cut, CAS,
   crash point, timeout equality, signal race, fingerprint, and rollback phase
   under AD-11 before decomposing the seams into stories.

## Blocking Gate

The review can become **PASS** only when a rerun can construct the same ten
primary units and show that each pair is forced to share:

- one versioned data shape;
- one entity owner;
- one state mutation path;
- one transaction or consistent read boundary;
- one identity and time rule;
- one queue, cancellation, and cutoff rule;
- one output and recovery contract; and
- one deterministic fixture proving the boundary.

Until then, downstream implementation units can remain individually correct
and still produce an unrecoverable combined system. That is precisely the
architecture failure this review was designed to expose.
