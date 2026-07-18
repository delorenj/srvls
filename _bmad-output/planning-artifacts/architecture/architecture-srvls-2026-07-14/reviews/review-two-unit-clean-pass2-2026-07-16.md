---
title: "srvls Architecture Two-Unit Clean Pass 2"
type: architecture-review
status: final
created: 2026-07-16
updated: 2026-07-16
reviewer: Sir Fix-a-Lot
review_mode: independent-final-two-unit-divergence-clean-pass2
reviewed_commit: 300ad193f88ab4fa7f5429c560d8f14794dd45a0
reviewed_spine_sha256: 401ebc30e64a41623d629a407b4260c0d21c7a3b7c3ae9ebc058cba0aad56206
reviewed_spine_line_count: 2011
reviewed_artifact: _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md
verdict: changes-required
blocking_status: blocked
finding_count: 7
blocking_findings: 4
high_findings: 3
moderate_findings: 0
low_findings: 0
---

<!-- markdownlint-disable MD013 MD025 -->

# Architecture Review: Two-Unit Clean Pass 2

## Verdict

**CHANGES REQUIRED. Blocking status: BLOCKED. Finding count: 7.**

The repaired frozen schedules converge for the documented default, silent,
one-nanosecond-early, and near-tie traces. Immediate non-process Ready
dispatch, the process gate, ordinary FD3 authentication and EOF, ScopeIdV1,
diagnostic ownership and deduplication, installed-to-installed release
recovery, SQLite pragma readbacks, and ordinary timer property readbacks also
converge.

Seven counterexamples remain. Independent implementations can encode different
PolicySnapshot, CollectionPlan, and ObservationId bytes; choose different
behavior when admission consumes an already-expired reservation; accept or
reject the same duplicated FD3 endpoint; accept a manual service start as a
timer-originated invocation; choose different timer-validation deadlines; and
either uninstall or fail when rolling back the KnownGood sentinel from a first
install. Each difference changes durable identity, diagnostic evidence, a
CollectorReport, or a release terminal result. PASS is therefore prohibited.

This review changed only this report. It did not edit the architecture spine,
memory log, task ledger, product code, or any prior report.

## Frozen Target and Review Isolation

| Property | Frozen value |
| --- | --- |
| Branch | `feature-sir-fix-a-lot-architecture-clean-pass2` |
| Commit | `300ad193f88ab4fa7f5429c560d8f14794dd45a0` |
| Spine | 2,011 lines; SHA-256 `401ebc30e64a41623d629a407b4260c0d21c7a3b7c3ae9ebc058cba0aad56206` |
| Architecture memory log | 145 lines; SHA-256 `dc2244ff89973ac1261caaa33fb47c7d7154ec3fd8117d3c1b8ca91b6828fba9` |
| Historical two-unit reports | Nine reports read through EOF |
| Peer clean-pass2 reports | Not read |

`AGENTS.md`, `tasks.md`, the complete configured BMAD architecture skill, and
its complete headless and reviewer-gate references were read before the
review. `ARCHITECTURE-SPINE.md` and `.memlog.md` were read through EOF. The nine
eligible historical reports were replayed only as counterexample history; no
prior verdict was accepted as proof. Neither other new clean-pass2 report was
opened, searched, diffed, or used.

The acceptance rule was literal interoperability. For each seam, the artifact
must force the same admitted bytes, absolute cut, process action, evidence,
durable state, and recovery result without a private convention shared between
the teams.

## Independent Reconstructions

| Team | Independent construction |
| --- | --- |
| Team A — Literal Compiler | Implements the declared schemas, transactions, schedule compiler, runtime, worker protocol, diagnostics, storage, and release state machine directly from normative sentences and tables. It does not infer unstated fields or rejection rules. |
| Team B — Recovery Verifier | Independently implements the same public contracts from crash edges, absolute cuts, canonical preimages, descriptor ownership, and terminal postconditions. It resolves an omission only when the spine states a deterministic rule. |

The teams shared no implementation, schema registry, field numbering, timeout
constant, fixture interpretation, or release shortcut. Both were tested with
the same frozen inputs and adversarial event traces.

## Requested Seam Matrix

| Seam | Team A | Team B | Result |
| --- | --- | --- | --- |
| Atomic CollectionPlan admission | Commits GenerationId, all cuts, policy, manifest, schedule, pins, plan, and latest pointer in one `BEGIN IMMEDIATE`. | Injects failure at every write and observes either the complete transaction or none. | **CONVERGED for atomicity; DIVERGED for admitted bytes.** AD-21 closes torn admission, but the nested plan and policy schemas are not byte-total. |
| Frozen schedule and absolute deadlines | Executes only persisted LPT reservations; an early result never advances an epoch. | Recompiles the schedule and compares canonical bytes before spawn. | **CONVERGED for documented traces; DIVERGED after late admission.** Default makespan/cutoff remain `35 s / 40 s`; the near-tie remains `30 s / 35 s`. No rule selects behavior after a member cut is already past. |
| Silent, early, late, and near-tie lanes | Dispatches each authenticated non-process Ready immediately and holds early-free slots. | Keeps the same epochs despite silence, failure, or Ready order and applies deadline-first result admission. | **CONVERGED except the already-expired spawn edge.** The historical early-completion counterexample is closed; the admission-latency edge is not. |
| Process gate and Ready dispatch | Closes the process gate only after every same-epoch parent-side spawn outcome and resolves unrootable children. | Dispatches ready non-process siblings without waiting and proves exact absence before process Host-read. | **CONVERGED.** No sibling Ready/result barrier or partial root remains. |
| FD3 framing, authentication, lifecycle, and EOF | Treats pre-Hello descriptor audit as a sanitizer in the duplicate acceptance fixture, then completes Result/EOF. | Treats any discovered duplicate as `fd-peer-auth`, closes it, and accepts no Hello. | **DIVERGED for duplicate fixtures.** Normal four-frame framing, credentials, deadline precedence, Result, exit, and EOF otherwise converge. |
| Policy and ScopeId grammar | Uses one plausible typed-policy declaration order and embeds obligations with each admitted scope. | Uses dotted-key order and the IDs-only ScopeManifestV1 grammar. | **DIVERGED for policy/plan bytes; CONVERGED for ScopeIdV1 itself.** |
| Evidence cuts, diagnostics, and deduplication | Freezes candidates after evidence, sorts the complete tuple, rewrites references once, and applies exact-owner suppression. | Reorders arrivals and cleanup/reap observations while retaining the same immutable cuts. | **CONVERGED for cuts and deduplication; DIVERGED for ObservationId bytes.** Provider field tags are not declared. |
| Release journal, crash recovery, and KnownGood | Replays pending effects by readback and treats first-install rollback as uninstall-to-absent. | Uses the same journal rules but cannot pass the mandatory staged-binary validator for an absent target. | **CONVERGED for installed pairs; DIVERGED for first-install-absent.** |
| SQLite and forward/rollback timer postconditions | Requires `wal`, numeric synchronous `2`, foreign keys `1`, exact unit properties, then accepts the temporal invocation sequence before its chosen cut. | Enforces the same SQLite and unit readbacks but requires timer causality and a different validation cut. | **CONVERGED for SQLite; DIVERGED for timer causality and deadline.** |

## Findings

### CLEAN2-B01 — CollectionPlanV1 and PolicySnapshotV1 are not byte-total

**Evidence.** AD-21 freezes Promise projection revisions and event sequences,
builds a ScopeManifest with effective obligations, and persists the complete
plan (`SPINE:1023-1076`). AD-24 fixes only the CollectionPlan top-level keys and
generic nested-row rules (`SPINE:1462-1478`). It does not declare the
`promise_cut` object or row fields, the complete baseline row field order, or
the fingerprint preimages for materialized baseline rows. It also defines
ScopeManifestV1 as only sorted ScopeId bytes (`SPINE:1494-1498`), although AD-21
requires the manifest to carry effective obligations (`SPINE:1031-1033`).

PolicySnapshotV1 orders policy fields by the “AD-19 declaration order”
(`SPINE:1425-1430`), but AD-19 declares no exhaustive ordered field list
(`SPINE:938-960`) and AD-20 contains wildcard families such as
`collection.deadline.*` and `action.execution.*` (`SPINE:973-997`).

**Exact counterexample.** Team A encodes `promise_cut` rows as `promise_id`,
`projection_revision`, then `event_sequence`, expands deadline fields in
Provider-tag order, and stores obligations beside each scope. Team B embeds the
full current Promise projection, expands policy keys in dotted lexical order,
and encodes ScopeManifest as the IDs-only grammar. Both satisfy the stated
freezes and generic CanonicalJson rules. They produce different
PolicyFingerprint and CollectionPlanFingerprint values; Team A and Team B then
reject each other's persisted plan before spawn.

**Required correction.** Add exhaustive canonical schemas for
PolicySchemaV1/PolicySnapshotV1, PromiseCutV1, every admitted nested cut and
baseline row, and the obligation-bearing scope structure. Freeze exact keys,
variant fields, scalar encodings, row order, wildcard expansion, fingerprint
domains, and whether obligation bytes are inside ScopeManifestV1 or a separate
top-level plan field. Add cross-implementation golden preimages and hashes.

### CLEAN2-B02 — An already-expired reservation has two legal spawn outcomes

**Evidence.** Admission samples the sole schedule origin inside the SQLite
transaction (`SPINE:1023-1038`). Runtime may start late and reduce remaining
budget but cannot move the absolute deadline (`SPINE:349-368`). Neither section
sets an admission-latency bound or states what happens when no budget remains.
The diagnostic matrix separately permits timeout with no child and timeout with
a spawned child (`SPINE:1686-1687`).

**Exact counterexample.** Freeze epoch `0`, member budget `1 s`, and cutoff
`2 s`. A legal large admission commits and runtime resumes at cutoff equality.
Team A checks the cuts before spawn and synthesizes `worker-timeout` with
`termination_origin=none`. Team B follows “before each spawn,” creates the
child, then immediately applies deadline-first timeout and cleanup, yielding
`termination_origin=parent-cleanup`, OwnedSpawn/reap evidence, and possibly an
unrootable-child process barrier. The same plan produces different diagnostic
bytes and process-gate state.

**Required correction.** Before capability allocation, socket creation, or
spawn, sample `CLOCK_BOOTTIME` and require strict-before both the member
deadline and generation cutoff. At equality or later, create no child and
synthesize the no-child timeout at the earlier absolute cut. Define ascending
catch-up order for multiple missed epochs and terminalize expired reservations
before starting any still-live member.

### CLEAN2-B03 — ObservationId provider schemas never assign field tags

**Evidence.** AD-13 names each Provider's logical ObservationId fields, then
requires `field_count` and schema-declared fields in ascending `field_tag`
order (`SPINE:671-682`). No Provider table assigns those tags, counts, exact
integer widths, or value encodings. ObservationId bytes are diagnostic subjects
and baseline identities (`SPINE:633-638`, `SPINE:1048-1053`).

**Exact counterexample.** For one systemd-user observation, Team A assigns
ScopeId tag `1`, full unit tag `2`, occurrence tag `3`, and birth evidence tag
`4`. Team B assigns the full unit tag `1` and ScopeId tag `2`, with the same
values and otherwise valid ascending encoding. The observations are logically
identical but their ObservationIds, baseline row ordering, diagnostic subjects,
Snapshot bytes, and comparison identity differ.

**Required correction.** Publish a complete ObservationIdV1 table per Provider
variant: provider tag, exact field count, every field tag/name, value kind,
fixed integer width, locator normalization, occurrence and birth variants, and
the fingerprint/display domain. Add golden bytes for every Provider.

### CLEAN2-B04 — First-install-absent KnownGood cannot run the mandatory rollback protocol

**Evidence.** KnownGoodCandidateV1 explicitly permits a
`first-install-absent` prior binary (`SPINE:1319-1324`). Explicit rollback must
create a new UpgradeTransaction whose candidate is the retained pair and run
the same admission, validation, decision, publication, event, and commit
protocol (`SPINE:1347-1351`). That protocol requires binary paths and hashes,
staging/checksum/smoke steps, and an exact staged executable that authenticates
the FD4 validator (`SPINE:1180-1211`, `SPINE:1213-1236`). No absent-target
variant defines which effects apply or how absence is validated.

**Exact counterexample.** After a successful first install, Team A interprets
rollback to the retained sentinel as uninstall: remove the link/binary, restore
prior state and consumer absence, mark binary validation steps skipped, and
return `rolled-back`. Team B cannot stage or launch the absent candidate and
returns `upgrade-recovery-required` without mutation. Both preserve the journal
rules, but they expose different filesystem state, admission generation,
KnownGood record, events, and terminal result.

**Required correction.** Either make first-install rollback unavailable with
one stable no-mutation result, or define AbsentReleaseV1 completely: ordered
removal and restore effects, state/sidecar/unit/enablement disposition, absence
readbacks, skipped-step reasons, admission generation, KnownGood transition,
events, recovery edges, and terminal postconditions.

### CLEAN2-H01 — FD3 duplicate acceptance contradicts fail-closed authentication

**Evidence.** AD-11's duplicate-parent-end and duplicate-child-end acceptance
cases require the pre-Hello audit to close injected references and then prove a
normal post-Result EOF (`SPINE:514-521`). AD-25 says any extra original,
duplicate, or opposite endpoint found at worker entry is `fd-peer-auth`, is
closed, and permits no Hello (`SPINE:1527-1541`). A no-Hello failure cannot also
complete the Result/EOF acceptance sequence.

**Exact counterexample.** Team A detects and closes the injected duplicate,
continues authentication, accepts one Hello/Ready/Request/Result exchange, and
proves EOF. Team B detects the same duplicate, freezes `fd-peer-auth`, closes
the lane, accepts no Hello, and synthesizes an invalid-output report. Both follow
one explicit normative clause; their CollectorReports and diagnostic bytes
differ.

**Required correction.** Choose one contract. For fail-closed authentication,
make every injected-duplicate case reject before Hello and assert failure-path
closure/EOF; move normal post-Result EOF acceptance to a descriptor-clean
fixture. If audit sanitation is intended to be accepted, explicitly exempt the
tracked injected references and define the exact cut at which their closure
restores an authentic lane.

### CLEAN2-H02 — Timer acceptance proves ordering but not timer causality

**Evidence.** The release sequence requires a fresh timer-originated candidate
invocation (`SPINE:1227-1232`). TimerInvocationAcceptanceV1 proves an advanced
LastTrigger, then a changed service InvocationID and start timestamp at or after
that trigger, followed by successful exit (`SPINE:1290-1306`). It stores no
causal identifier connecting the timer trigger to that service invocation.

**Exact counterexample.** The timer's LastTrigger advances, but that activation
fails before the service starts. An operator then manually starts the exact
service; it receives a new InvocationID, starts after the trigger, and exits
successfully. Team A accepts because every stated predicate passes. Team B
honors “timer-originated,” detects the unrelated manual start, and restores the
whole pair. The same Host trace commits in one implementation and rolls back in
the other.

**Required correction.** Add one authoritative causal proof that binds the
advanced timer activation to the accepted service job/invocation, including its
canonical stored fields and readback source. Reject an intervening manual or
unrelated activation and add that race to both forward and rollback fixtures.

### CLEAN2-H03 — Timer validation has no frozen deadline derivation

**Evidence.** Every timer sample must be strictly before “the validation
deadline” (`SPINE:1290-1303`), but no release limit, default, range, clock
domain, or derivation defines that cut. FD4 carries an absolute boot-time
deadline (`SPINE:1190-1195`), but the artifact neither derives it nor equates it
to the timer deadline. Recovery explicitly takes fresh timer baselines
(`SPINE:1242-1249`) without saying whether it retains or renews the cut.

**Exact counterexample.** A correct paired timer produces its fresh successful
invocation at `45 s`. Team A chooses a `30 s` validation deadline and restores
the whole pair. Team B chooses `120 s` and commits. During explicit rollback,
the same choice yields `upgrade-recovery-required` versus `rolled-back`.

**Required correction.** Define a typed release-validation duration with exact
default/range and `CLOCK_BOOTTIME` arithmetic. Persist the absolute attempt or
effect cut before validation, bind timer and FD4 evidence to it, and state
whether each recovery owner receives a new attempt-bound cut. Use the same rule
for forward validation, pre-decision restore, and explicit rollback.

## Closed Adversarial Cases

- Frozen DispatchScheduleV1 compilation now holds early-free slots and produces
  byte-identical default and near-tie reservations across configuration,
  admission, and runtime (`SPINE:321-347`, `SPINE:458-494`).
- A Ready non-process member dispatches without sibling Ready/result delay;
  process waits only for same-epoch spawn outcomes and exact root/absence proof
  (`SPINE:369-392`, `SPINE:1586-1612`).
- Ordinary FD3 lanes authenticate both peers, enforce four-frame order, apply
  deadline-first failure precedence, require complete Result plus clean EOF and
  exit zero, and exclude later cleanup from immutable evidence
  (`SPINE:1543-1584`, `SPINE:1625-1705`).
- ScopeIdV1 provider tags, path normalization, ordering, and manifest
  fingerprint are complete (`SPINE:1480-1498`).
- Candidate allocation, reference rewrite, exact-owner deduplication,
  unrootable-child handling, and process suppression are arrival-order
  independent (`SPINE:623-669`, `SPINE:684-759`).
- The release journal's pending/complete protocol, recovery-owner takeover,
  installed-pair KnownGood boundary, and checksum/readback rules select one
  recovery truth (`SPINE:1143-1250`, `SPINE:1319-1351`).
- Fresh and existing SQLite connections must read back `journal_mode=wal`,
  numeric `synchronous=2`, and `foreign_keys=1` before a transaction; forward
  and rollback unit property mismatches fail the whole pair
  (`SPINE:803-872`, `SPINE:1257-1317`).

## Mechanical Validation

| Check | Result |
| --- | --- |
| Exact base commit and clean starting tree | PASS |
| Architecture spine lint | PASS |
| Canonical Markdown lint for this report | PASS |
| `git diff --check` and staged diff check | PASS |
| AD identifier sequence and uniqueness | PASS: AD-1 through AD-25, one defining heading each |
| ARCH-LIM identifier sequence and uniqueness | PASS: ARCH-LIM-1 through ARCH-LIM-23, one defining row each |
| Review finding identifier uniqueness | PASS: seven distinct defining headings |
| Structural uniqueness | PASS: one spine Structural Seed, one worker adapter path, one release adapter path, and one report title/verdict/findings structure |
| Changed-path isolation | PASS: only this report |

## Final Gate

The clean-pass2 acceptance gate requires zero findings. The seven exact
counterexamples above survive both independent implementations, so the verdict
is **CHANGES REQUIRED**. Correct the normative contracts and rerun two fresh,
isolated units against the resulting commit; prior reports and this review are
not substitutes for that rerun.
