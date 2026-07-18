---
title: "srvls Architecture Review: Final Two-Unit Divergence Acceptance"
type: architecture-review
status: final
created: 2026-07-16
updated: 2026-07-16
reviewer: Sir Fix-a-Lot
review_mode: independent-final-two-unit-divergence-acceptance
reviewed_commit: b917bcc89b5e386789cd0d0e8dfd01ce0cd42d0f
reviewed_artifact: _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md
prior_review: _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/reviews/review-two-unit-divergence-2026-07-16.md
verdict: changes-required
blocking_status: blocked
probe_count: 20
probes_closed: 14
probes_open: 6
finding_count: 13
blocking_findings: 4
high_findings: 7
moderate_findings: 2
---

<!-- markdownlint-disable MD013 MD025 -->

# Architecture Review: Final Two-Unit Divergence Acceptance

## Verdict

**CHANGES REQUIRED.** The AD-21 through AD-24 amendments close 14 of the 20
original probes, including the entire action planning/execution/shutdown pair.
They do not yet force all ten independently built units to interoperate. Six
original probes remain open: `DVG-B06`, `DVG-B07`, `DVG-B08`, `DVG-H02`,
`DVG-H04`, and `DVG-H07`.

The amendments also create or expose four blocking cross-unit seams that token
matching against the prior recommendations does not catch:

1. `CollectionPlanV1` freezes Promise and policy state but omits the Accepted
   Baseline and nonterminal-operation cuts required by canonical reconciliation.
2. `PolicyFingerprint` and Scope identities still lack byte-complete canonical
   encodings.
3. a crash releases the live release lease before any rule prevents an ordinary
   stateful command from writing into an unresolved upgrade transaction; and
4. the upgrade manifest has named phases but no atomic replacement or
   phase/effect ordering contract, so the journal itself can tear or lie.

Only constructed Pair 3 now satisfies the complete acceptance condition without
qualification. Pairs 2, 4, and 5 retain original probe failures. Pair 1's
original probes close, but its reconciliation unit still cannot consume all
canonical inputs from the new frozen plan. The spine therefore remains unsafe to
decompose across the affected boundaries.

This review is documentation-only. It does not amend the spine, its memlog,
`tasks.md`, product code, canonical PRD/UX artifacts, or prior reviews.

## Review Basis

The acceptance review was performed at exact commit
`b917bcc89b5e386789cd0d0e8dfd01ce0cd42d0f` in the isolated
`feature-sir-fix-a-lot-architecture-acceptance` worktree.

The following required artifacts were read completely:

- `SPINE` —
  `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md`
  (947 lines)
- `PRIOR` —
  `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/reviews/review-two-unit-divergence-2026-07-16.md`
  (553 lines)

Canonical sources were consulted only for disputed contracts:

- `PRD:418-425` confirms sampled resource evidence is an input to `hot`.
- `PRD:456-480` confirms the Accepted Baseline is an input to the Evidence
  Window, change set, and Brief.
- `PRD:446-454` confirms an in-flight conflicting operation is an input to
  Safe-to-stop.
- `PRD:629-636` confirms rollback to the prior known-good target is a supported
  operator contract.
- `PRD:702-704` confirms identical inputs, policy, and Accepted Baseline must
  produce identical findings and machine serialization.
- `EXPERIENCE:65-76`, `EXPERIENCE:185-191`, and `DESIGN:302-314` confirm the
  baseline, install/recovery, persistent phase-result, and machine-result
  surfaces affected by these seams.

Current decision ranges cited below are `AD-5` at `SPINE:139-183`, `AD-6` at
`SPINE:185-234`, `AD-10` at `SPINE:304-346`, `AD-11` at `SPINE:348-367`,
`AD-13` at `SPINE:395-417`, `AD-14` at `SPINE:419-438`, `AD-16` at
`SPINE:461-524`, `AD-17` at `SPINE:526-545`, `AD-18` at `SPINE:547-582`,
`AD-19` at `SPINE:584-612`, and `AD-21` through `AD-24` at
`SPINE:659-762`.

## Acceptance Standard

The same standard from `PRIOR:537-549` was applied without weakening it. For
each probe, both units must be forced to share:

- one versioned data shape;
- one entity owner;
- one state mutation path;
- one transaction or consistent read cut;
- one identity and time rule;
- one queue, cancellation, and cutoff rule;
- one output and recovery contract; and
- one deterministic cross-unit fixture.

In the matrix, **Y** means the cited rule removes the independent choice. **N**
means two literal implementations can still choose incompatibly. **N/A** means
the dimension is not exercised by that probe; it is not being used to excuse an
unknown seam. A probe closes only when every exercised dimension is **Y**.

## Same Ten Constructed Units

No unit was redesigned to make the amendments look better. The acceptance rerun
used the same ten next-level units and responsibilities as the prior review.

| Pair | Unit | Reconstructed responsibility under the amended spine |
| --- | --- | --- |
| 1 | P-A — Promise Lifecycle Command Unit | Accepts declare, revise, renew, release, complete, and revoke; samples Clock/BootIdentity; appends sequenced events and updates the authoritative Promise projection in one repository transaction. |
| 1 | P-B — Reconciliation and State Unit | Consumes a frozen plan plus eligible reports, runs the pure decision engine, and requests the atomic Snapshot/Findings/current-pointer transaction. |
| 2 | C-A — Scoped Collection Worker Unit | Receives one frozen scope assignment, runs supervised Provider work, and echoes the exact scope, obligation, deadline, diagnostics, Observations, and outcome. |
| 2 | C-B — Snapshot Reducer and Persistence Unit | Owns the frozen manifest, atomic result registry, timeout synthesis, cross-Provider reduction, latest-generation admission, and Snapshot transaction request. |
| 3 | A-A — Action Intent Coordinator | Creates and persists immutable `ActionPlanV1`, performs submit/revalidation, allocates the Operation, applies FR-40, and owns the terminal compare-and-swap. |
| 3 | A-B — Provider, Verification, and Terminal Effects Unit | Executes exact argv, emits launch/cancellation evidence, performs OperationId-correlated verification, and restores the terminal without inventing outcomes. |
| 4 | K-A — Effective Configuration Compiler | Parses all sources, merges typed policy, retains provenance, and emits complete `PolicySnapshotV1`, `PolicyFingerprint`, and `ProvenanceDigest`. |
| 4 | K-B — Historical Policy and Finding Reader | Loads versioned policy and materialized decision records, renders supported history unchanged, and returns typed read-only results for unsupported versions. |
| 5 | I-A — Release Install Coordinator | Owns release preflight, admission quiescence, staged activation, phase progression, consumer validation, rollback choice, and recovery orchestration. |
| 5 | I-B — SQLite Migration and Recovery Adapter | Implements typed backup, migration, restore, sidecar disposition, hashing, fsync, integrity, and schema verification effects. |

## Twenty-Probe Closure Matrix

| Probe | Versioned shape | Owner | Mutation path | Transaction/read cut | Identity/time | Queue/cutoff | Output | Recovery | Fixture | Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `DVG-B01` mixed-time truth | **Y** — `CollectionPlanV1` freezes Promise revisions and event sequences. | **Y** — reducer/reconciliation alone consumes the plan. | **Y** — later Promise writes belong to the next generation. | **Y** — one consistent repository read creates the plan (`AD-21`). | **Y** — GenerationId, boot sample, BootIdentity, and event sequence are captured. | **Y** — eligible reports close under the frozen generation. | **Y** — Findings carry the frozen decision/policy references. | **Y** — failed attempts leave prior current truth stale. | **Y** — AD-11 freezes the AD-21 read cut. | **CLOSED** |
| `DVG-B02` current Snapshot without Findings | **Y** — Snapshot transaction names plan, reports, diagnostics, Observations, samples, and Findings. | **Y** — reducer requests; SQLite repository owns commit. | **Y** — one AD-16 transaction. | **Y** — Findings and current-pointer CAS are atomic. | **Y** — all typed IDs and revisions are retained. | **Y** — only the latest requested generation may move current. | **Y** — materialized Findings and decision version persist together. | **Y** — pre-commit failure leaves the old pointer unchanged. | **Y** — AD-11 freezes the read cut and generation CAS. | **CLOSED** |
| `DVG-B03` two owners of current truth | **Y** — persisted `latest_requested_generation` and current pointer. | **Y** — coordinator/repository CAS, not presentation. | **Y** — only the latest generation can replace current. | **Y** — the pointer CAS is in the Snapshot transaction. | **Y** — gap-free GenerationId ordering. | **Y** — latest-wins coalescing and cancellation are explicit. | **Y** — repository and displayed current name the same committed Snapshot. | **Y** — superseded evidence may remain only as attempt/history. | **Y** — AD-11 names generation CAS. | **CLOSED** |
| `DVG-B04` Action Plan interoperability | **Y** — immutable `ActionPlanV1`, `PlanId`, and exact captured fields. | **Y** — ActionPlanRepository plus OperationCoordinator. | **Y** — persist, consume by revision CAS, create Operation. | **Y** — consumption and Operation creation share one transaction. | **Y** — PlanId/OperationId, target, generation, BootIdentity, and boot/wall samples. | **Y** — TTL, action pool, saturation, and duplicate-operation rules. | **Y** — retry returns the original plan or operation result. | **Y** — unconsumed expiry and nonterminal recovery are explicit. | **Y** — AD-11 freezes plan and launch handoffs. | **CLOSED** |
| `DVG-B05` durability versus shutdown bound | **Y** — durable operation phases and typed terminal outcomes. | **Y** — OperationCoordinator owns FR-40 and terminal CAS. | **Y** — every phase/evidence update is transactional. | **Y** — bounded write attempts no longer imply a successful terminal write. | **Y** — OperationId plus AD-20 phase deadlines. | **Y** — separate bounded action pool; no replay. | **Y** — last truthful nonterminal phase is allowed on storage failure. | **Y** — next-start fresh evidence resolves it conservatively. | **Y** — AD-11 names the storage-unavailable exception. | **CLOSED** |
| `DVG-B06` canonical policy fingerprint | **Y** — complete `PolicySnapshotV1` and named digest types. | **Y** — configuration compiler creates; repositories reference. | **Y** — complete snapshot insertion is transactional. | **Y** — artifacts reference one retained policy snapshot. | **N** — JSON string escaping is not fixed, so equivalent NFC strings can hash as literal UTF-8, `\u` escapes, or escaped solidus. | **N/A** | **N** — different compliant bytes yield different fingerprint output. | **Y** — unsupported versions are typed read-only. | **N** — one fixture cannot define the missing serialization grammar. | **OPEN** |
| `DVG-B07` upgrade-wide quiescence | **N** — the install-generation lease/bypass token has no versioned type, path, acquisition protocol, or persistent generation. | **Y** — `application::release` owns orchestration. | **N** — after a crash, an ordinary stateful entry may acquire a shared lease and write before recovery. | **N** — the exclusive lease disappears with the process; only a later release entry must inspect the manifest. | **N** — no durable admission generation binds post-crash entrants. | **N** — no rule blocks or upgrades shared admission while a nonterminal manifest exists. | **N** — ordinary commands have no required `upgrade-recovery-required` result. | **N** — a later restore can discard the intervening accepted write. | **Y** — AD-11 names upgrade quiescence, but the fixture cannot supply the missing gate. | **OPEN** |
| `DVG-B08` crash-recoverable install state | **Y** — `UpgradeTransactionV1` names fields and phases. | **Y** — release application owns phase recovery. | **N** — manifest replacement and phase-before/after-effect ordering are not specified. | **N** — mode and fsync do not prevent an in-place rewrite from tearing. | **Y** — transaction ID, target/schema identities, and hashes are retained. | **Y** — the live exclusive lease covers a non-crashed transaction. | **Y** — named phases can drive status output. | **N** — recovery cannot interpret an empty/torn manifest or a phase whose effect boundary is ambiguous. | **Y** — AD-11 names every crash phase, but not the missing write protocol. | **OPEN** |
| `DVG-H01` event/projection disagreement | **Y** — event sequence and projection revision are shared. | **Y** — repository transaction assigns sequence and updates projection. | **Y** — append plus projection update is atomic. | **Y** — projection through sequence N is authoritative. | **Y** — gap-free per-Promise sequence; monotonic time is provenance, not replay order. | **N/A** | **Y** — readers never refold in another order. | **Y** — persisted projection remains authority. | **Y** — AD-11 covers lifecycle/idempotency. | **CLOSED** |
| `DVG-H02` Scope identity | **N** — variants are named, but composite field framing and Docker/PM2 normalization are not. | **Y** — domain `ScopeIdV1` is shared. | **Y** — workers echo and reducer rejects mismatch. | **Y** — one ordered ScopeManifest is frozen. | **N** — AD-24 percent-encodes bytes but gives no component delimiter/length framing; `normalized PM2_HOME` and Docker endpoint normalization remain undefined. | **N** — LPT tie order can differ with different canonical bytes/cardinality. | **N** — public IDs and manifest fingerprints can differ. | **N** — baseline compatibility can disagree. | **N** — finite fixtures cannot define the absent normalization grammar. | **OPEN** |
| `DVG-H03` obligation time travel | **Y** — obligation is a field of frozen ScopeManifest/worker assignment. | **Y** — plan creator promotes; reducer only validates. | **Y** — later Promise writes affect only the next generation. | **Y** — one consistent plan read. | **Y** — obligation is generation-bound. | **Y** — worker echoes the frozen assignment. | **Y** — strictness and eligibility use one value. | **Y** — mismatch is rejected rather than recomputed. | **Y** — AD-11 freezes scope handoff. | **CLOSED** |
| `DVG-H04` diagnostic references | **Y** — `DiagnosticId = (GenerationId, ScopeIdV1, canonical_ordinal)`. | **N** — AD-13 says coordinator assigns each ordinal before dispatch; AD-21 gives only a range to a worker that discovers diagnostics later. | **Y** — workers echo; reducer rejects shape mismatch. | **Y** — range belongs to the frozen plan. | **N** — no canonical category/order rule maps an outcome-dependent diagnostic to the preassigned ordinal. | **Y** — assignment precedes dispatch. | **N** — two workers can attach the same ordinal to different diagnostics. | **Y** — malformed/mismatched reports are rejected. | **N** — fixtures freeze examples, not the total allocation rule. | **OPEN** |
| `DVG-H05` cutoff race | **Y** — typed report registered in coordinator registry. | **Y** — coordinator owns eligibility. | **Y** — registry acceptance is atomic. | **Y** — registration must precede both half-open deadlines. | **Y** — equality is timed-out under the same monotonic cut. | **Y** — mailbox order cannot affect eligibility. | **Y** — reducer synthesizes one terminal report. | **Y** — late output is stale evidence only. | **Y** — AD-11 freezes timeout equality. | **CLOSED** |
| `DVG-H06` supersession/admission | **Y** — persisted latest request and typed cancellation. | **Y** — collection coordinator owns admission. | **Y** — superseded generations cannot move current. | **Y** — current CAS is latest-only. | **Y** — monotonic GenerationId. | **Y** — latest-wins, cancel undispatched, request cancellation of running, retain diagnostics, admit newest queued. | **Y** — only newest committed truth displays current. | **Y** — attempt evidence may be retained without promotion. | **Y** — AD-11 names generation CAS. | **CLOSED** |
| `DVG-H07` cross-Provider deduplication | **N** — “bounded process ownership hints” has no shared fields or evidence grammar. | **Y** — reducer alone owns attribution/deduplication. | **Y** — worker cannot suppress locally. | **Y** — reduction waits for all eligible reports. | **N** — no rule defines exact ownership evidence or partial/conflicting behavior. | **Y** — only cutoff-eligible reports participate. | **N** — equally literal reducers can emit different direct-process Observations. | **N** — retained suppression diagnostic/evidence is not required. | **N** — no cross-unit fixture can infer the missing general rule. | **OPEN** |
| `DVG-H08` launch boundary | **Y** — `LaunchReceiptV1` and `VerificationRequestV1`. | **Y** — coordinator owns sequence/receipt; verifier owns evidence only. | **Y** — durable authorization precedes Provider launch. | **Y** — operation phase/evidence transactions preserve handoff. | **Y** — OperationId and monotonic launch/start ordering. | **Y** — verification starts strictly after launch sequence. | **Y** — receipt distinguishes spawn result or may-have-launched. | **Y** — nonterminal recovery obtains fresh targeted evidence. | **Y** — AD-11 freezes plan/launch handoffs. | **CLOSED** |
| `DVG-H09` terminal outcome ownership | **Y** — typed evidence, cancellation request, and terminal result. | **Y** — OperationCoordinator is sole FR-40 authority. | **Y** — one terminal revision CAS. | **Y** — durable repository truth is the render cut. | **Y** — OperationId correlates all evidence. | **Y** — late evidence is resolved by the sole coordinator. | **Y** — TUI renders committed truth only. | **Y** — storage failure retains nonterminal truth. | **Y** — AD-11 covers action races/signals. | **CLOSED** |
| `DVG-H10` historical decision version | **Y** — materialized Findings/Briefs plus `decision_contract_version`. | **Y** — reconciliation materializes; readers render. | **Y** — re-evaluation creates a new derived generation. | **Y** — historical records never consult current defaults/engine. | **Y** — stored version identifies decision semantics. | **N/A** | **Y** — old output is rendered unchanged. | **Y** — unsupported version is typed read-only. | **Y** — AD-11 freezes decision-version behavior. | **CLOSED** |
| `DVG-H11` backup/restore contract | **Y** — `StateBackupManifestV1` and typed effects. | **Y** — StateMigrationCoordinator. | **Y** — create, migrate, restore, verify are port effects. | **Y** — quiesced backup and no-live-connection restore. | **Y** — hashes, schema, sidecar disposition, and integrity are retained. | **Y** — release lease owns admission while live. | **Y** — effects return total typed results through AD-3. | **Y** — phase mapping chooses restore/verify behavior. | **Y** — AD-11 freezes sidecar restore. | **CLOSED** |
| `DVG-M01` artifact policy closure | **Y** — one complete `PolicySnapshotV1`, never subsets. | **Y** — configuration creates; artifacts reference. | **Y** — complete snapshot insertion is transactional. | **Y** — each artifact pins one historical policy. | **Y** — schema version and fingerprint identify it. | **N/A** | **Y** — supported readers never fill from current defaults. | **Y** — unsupported schema is typed read-only. | **Y** — AD-11 freezes policy bytes. | **CLOSED** |

## Constructed-Unit Conclusion

| Constructed pair | Original probes | Acceptance conclusion |
| --- | --- | --- |
| P-A vs P-B — Promise lifecycle / reconciliation and storage | `DVG-B01`, `DVG-H01`, and `DVG-B02` close. | **Original pair closes**, but P-B still lacks baseline, operation, resource-history, and wall-time inputs in `CollectionPlanV1`; cross-pair integration remains blocked. |
| C-A vs C-B — collection workers / reduction and persistence | `DVG-H03`, `DVG-H05`, `DVG-B03`, and `DVG-H06` close; `DVG-H02`, `DVG-H04`, and `DVG-H07` remain open. | **NOT ACCEPTED.** The same report can still key scopes, assign diagnostics, and deduplicate process truth differently. |
| A-A vs A-B — action planning / execution, verification, shutdown | `DVG-B04`, `DVG-H08`, `DVG-H09`, and `DVG-B05` close. | **ACCEPTED.** The pair now shares a versioned plan, sole coordinator, durable launch and terminal handoffs, bounded queues, truthful output, and crash recovery. |
| K-A vs K-B — configuration / historical policy | `DVG-H10` and `DVG-M01` close; `DVG-B06` remains open. | **NOT ACCEPTED.** Both units share the logical policy fields but are not forced to hash the same bytes. |
| I-A vs I-B — installer / schema rollback | `DVG-H11` closes; `DVG-B07` and `DVG-B08` remain open. | **NOT ACCEPTED.** Live ownership is named, but crash admission, journal atomicity, and durable known-good rollback remain divergent. |

Across the same ten units, the decisive new interleavings are:

1. **C-B to P-B baseline race.** Generation 42 freezes Promise/policy/scope state.
   While workers run, baseline acceptance moves from Snapshot 39 to 41. One P-B
   reads baseline 39 at plan start; another reads 41 when materializing the
   Brief. Both consume only the fields AD-21 actually freezes, yet emit different
   FR-27 change sets.
2. **A-A/A-B to P-B operation race.** A stop Operation becomes nonterminal while
   generation 42 runs. One P-B queries current operations before Safe-to-stop;
   another obeys AD-18 literally and consumes only the plan/reports, which carry
   no operation cut. They disagree on `safe` versus `unsafe/unknown` under
   `PRD:446-454`.
3. **C-B to P-B history race.** Retention or a concurrent Snapshot changes the
   prior resource samples available during reduction. One P-B embeds history in
   an extended plan; another queries retained history after reports close. Both
   satisfy AD-5's hot-window prose but classify `hot` differently.
4. **P-A to I-A/I-B crash race.** Release crashes after migration and the OS
   drops the exclusive lease. P-A acquires the now-free shared lease and commits
   a renewal. A later release entry follows AD-23 and restores the pre-migration
   backup, losing the accepted renewal even though every live process held the
   required lease.

## Tier 0 — Blocking Findings

### ACC-B01 — The frozen reconciliation cut omits the Accepted Baseline

`AD-21` binds baselines but `CollectionPlanV1` does not retain a baseline
acceptance ID/revision, exact baseline Snapshot, compatibility result, or
no-baseline state (`SPINE:659-680`). `AD-18` nevertheless requires the Brief to
name the baseline (`SPINE:580-582`), and canonical FR-27/NFR-1 make it an input
to deterministic change results (`PRD:456-466`, `PRD:702-704`). Freeze a
versioned `AcceptedBaselineCutV1` in the same consistent read, and include its
reference in the atomic Snapshot/Findings/Brief materialization.

### ACC-B02 — The frozen reconciliation cut omits nonterminal operations

Canonical Safe-to-stop requires that no conflicting operation is in flight
(`PRD:446-454`). `AD-18` permits only the frozen CollectionPlan and eligible
reports as inputs, but `AD-21` captures no operation revision/set. Two pure
engines must therefore either ignore a canonical input or perform an undeclared
repository read. Add a frozen exact-target nonterminal-operation cut, including
the repository revision at which it was read, or explicitly move Safe-to-stop
to a separately versioned later cut and bind every presenter/action planner to
that one choice.

### ACC-B03 — Release quiescence evaporates on crash

`AD-23` requires only a **release entry** to resume or reverse a nonterminal
manifest (`SPINE:726-730`). The live exclusive lease is released by the kernel
when the installer dies. No rule requires an ordinary stateful entry to inspect
the manifest before acquiring a shared lease and writing. This preserves the
exact write-loss interleaving from `DVG-B07`, only across a crash. Define one
versioned admission protocol and lock location: every stateful entry must first
detect a nonterminal manifest and either acquire exclusive recovery ownership or
return a typed read-only/refused result before opening SQLite.

### ACC-B04 — AD-24 does not define one fingerprint byte stream

`AD-24` fixes field order, primitive units, NFC, and whitespace, but not JSON
string escaping (`SPINE:749-758`). Literal UTF-8 versus `\u` escapes and `/`
versus `\/` are different byte streams satisfying the written rules. The same
gap affects the provenance preimage. Adopt a named canonical-JSON standard or
spell out exact key/string escaping, Unicode emission, and invalid-code-point
rejection. Expand cross-unit tests from example bytes to grammar/property cases.

## Tier 1 — High Findings

### ACC-H01 — Scope identity is still not canonical

`AD-21` says Docker uses resolved endpoint plus context and PM2 uses normalized
`PM2_HOME`, but never defines either normalization (`SPINE:668-674`). `AD-24`
percent-encodes component bytes but supplies no tag encoding, component framing,
numeric encoding, or separator (`SPINE:745-750`). Define the exact tagged binary
or textual grammar, Docker endpoint/context equivalence, PM2 path rules, and
non-UTF-8 Host-path behavior. Use those bytes for equality, ordering, display,
and the ScopeManifest fingerprint.

### ACC-H02 — Diagnostic ordinals are not constructible as specified

`AD-13` says the coordinator assigns each canonical ordinal before worker
dispatch (`SPINE:403-406`), while `AD-21` says the worker receives a diagnostic
range (`SPINE:672-674`). The coordinator cannot assign outcome-dependent
diagnostics it has not observed, and no canonical category/order maps a later
diagnostic into that range. Choose one enforceable model: fixed typed diagnostic
slots allocated in the plan, or worker-local deterministic ordering under a
fully specified grammar. Keep the exact `DiagnosticId` and forbid remapping.

### ACC-H03 — Deduplication has an owner but no decision contract

The reducer alone now owns cross-Provider attribution and deduplication, which
closes the ownership half of `DVG-H07`. The shape and semantics of “bounded
process ownership hints,” exact ownership evidence, partial/conflicting
evidence, self-suppression, and retained suppression diagnostics remain absent
(`SPINE:413-415`, `SPINE:675-677`). Define those inputs and a deterministic
decision table before freezing the AD-11 fixture.

### ACC-H04 — Historical resource samples are outside the frozen read cut

`AD-5` requires hot classification to read the configured window from immutable
Snapshot history (`SPINE:168-170`), and FR-24 makes metric, sample time,
threshold, and source product output (`PRD:418-425`). `CollectionPlanV1` contains
no retained-history revision or exact sample set, while `AD-18` allows no other
input. Freeze the eligible historical sample IDs/rows in the consistent read and
pin them through the Snapshot transaction, or declare and version a separate
history read cut.

### ACC-H05 — Collection request creation is not one atomic admission

`AD-10` persists monotonic GenerationIds with `latest_requested_generation`,
while `AD-21` creates and later persists/references a `CollectionPlanV1`. No rule
makes GenerationId allocation, the consistent Promise/policy/baseline read, plan
insertion, and latest-requested update one transaction. A crash may leave a
latest generation without its plan, or a plan that was never admitted as
latest. Define one repository operation and recovery result for that admission.

### ACC-H06 — The upgrade journal can tear or cross its effect boundary

Mode `0600` plus file and directory fsync does not make an in-place manifest
rewrite atomic. `AD-23` also does not say whether each phase is durably recorded
before or after its corresponding effect, although recovery treats phases as
completed facts (`SPINE:722-734`). Require a versioned/checksummed temp-write,
file-fsync, atomic-rename, directory-fsync protocol and define write-ahead versus
write-after ordering for every phase/effect edge.

### ACC-H07 — Successful validation can erase the supported rollback target

FR-43 promises an operator rollback to the prior known-good target
(`PRD:629-636`). `AD-23` cleans a committed manifest before new work, and AD-12
retains prior target/recovery material only until checks pass (`SPINE:390-392`,
`SPINE:726-731`). It does not define the durable known-good record, backup/binary
retention, or how explicit `release rollback` starts after successful
validation. Add a bounded versioned known-good release record and make rollback
create a new UpgradeTransaction from that retained pair.

## Tier 2 — Moderate Findings

### ACC-M01 — Collection wall time has no single sample boundary

`CollectionPlanV1` captures a generation-start boot sample but not the UTC wall
sample used for persisted/displayed Snapshot time, Evidence Window end, sample
provenance, and timezone rendering. `AD-16` merely says rows retain wall-time
provenance. Capture boot and wall samples together at the plan boundary and
define later wall samples as display-only diagnostics so two units cannot stamp
the same generation at different lifecycle points.

### ACC-M02 — Release phase output is not mapped to recovery phases

UX requires persistent stage, checksum, smoke, activation, validation, and
recovery results (`EXPERIENCE:185-191`, `DESIGN:308-314`). `UpgradeTransactionV1`
uses a different internal phase vocabulary and AD-9 only promises a versioned
deterministic envelope. Define the versioned mapping, stable reason codes, and
which manifest phase/result is emitted after crash recovery so I-A and I-B do
not report incompatible release histories.

## Required Closure Gate

A PASS rerun requires all of the following:

1. Close the six open original probes, with byte-complete Policy and Scope
   encodings, an implementable DiagnosticId allocation rule, deterministic
   deduplication inputs/rules, and crash-safe release admission/journaling.
2. Extend `CollectionPlanV1` to freeze every canonical decision input: Accepted
   Baseline, nonterminal operations, eligible resource history, and paired boot
   plus wall samples.
3. Make CollectionPlan admission one repository transaction with GenerationId
   allocation and `latest_requested_generation` update.
4. Require every stateful process entry to gate on a nonterminal
   `UpgradeTransactionV1`, then define atomic manifest replacement and every
   phase/effect fsync edge.
5. Retain one bounded prior known-good binary/state pair under a typed rollback
   record after validation.
6. Add cross-unit property/crash fixtures for serialization grammar, Scope
   normalization, diagnostic allocation, deduplication, baseline/operation/history
   races, plan admission, non-release crash entry, torn manifests, and explicit
   post-validation rollback.

## Validation Record

| Validation | Command or method | Result |
| --- | --- | --- |
| Commit pin | `git rev-parse HEAD` | **PASS** — `b917bcc89b5e386789cd0d0e8dfd01ce0cd42d0f` |
| Required artifact reads | Complete line-numbered reads of SPINE and PRIOR | **PASS** — 947 + 553 lines |
| Canonical dispute reads | Numbered PRD/UX ranges listed under Review Basis | **PASS** — only disputed contracts consulted |
| Constructed-unit identity | Manual comparison to `PRIOR:101-461` | **PASS** — same 5 pairs / 10 units |
| Probe inventory | Exact unique-ID extraction plus matrix audit | **PASS** — 8 blocking + 11 high + 1 moderate = 20/20 |
| Architecture linter | `uv run .agents/skills/bmad-architecture/scripts/lint_spine.py --workspace _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14` | **PASS** — `ok: true`; `total_findings: 0` |
| Markdown lint | `markdownlint-cli2 --config _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/.markdownlint-cli2.jsonc _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/reviews/review-two-unit-divergence-acceptance-2026-07-16.md` | **PASS** — one file; zero errors |
| Whitespace/error check | `git diff --check` | **PASS** — no output |
| Changed-file scope | `git status --short` and `git diff --name-only` | **PASS** — only this acceptance report |

The deterministic architecture linter proves the spine's mechanical form. It
does not close the semantic two-unit divergences above.

## Final Blocking Status

**BLOCKED. Verdict: CHANGES REQUIRED.** The acceptance report is final, but the
spine does not yet force all ten units to share one interoperable and
crash-recoverable contract.
