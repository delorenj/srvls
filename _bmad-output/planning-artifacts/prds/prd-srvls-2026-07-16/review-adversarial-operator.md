---
title: "srvls PRD adversarial operator review"
artifact_type: "adversarial-review"
date: "2026-07-16"
reviewer: "SyntaxSorcerer"
gate: "FAIL"
---

# Adversarial operator review

This review tests the current `prd.md` and `addendum.md` as a skeptical solo
operator contract. It uses the named live-evidence extract, landscape report,
source-input reconciliation, architecture spine, epics, and July 15 readiness
report. `project-context.md` is not present in this worktree, so no finding
claims support from that missing source.

The current PRD closes most of the earlier source-reconciliation blockers. It
now assigns Collection Obligations, defines orthogonal lifecycle and evidence
states, limits Runtime Promises to runtime liveness, fixes the morning window
to an Accepted Baseline, gives a positive `safe` rule, records inherited MVP
scope, layers the compatibility oracle, and gives start an explicit TUI path.
Those repairs are substantive. The gate still fails because two remaining
contract contradictions would force architecture, UX, or acceptance tests to
invent safety-relevant behavior.

## Findings by severity

No critical findings are supported by the reviewed evidence.

### High

#### H-1 — Blocker: closed survivors lack deterministic classification

The lifecycle contract collapses `released`, `completed`, and `revoked` into
`closed`, then says a surviving Observation is reconciled on the next refresh
(`prd.md:214-221`). The transition table defines only these terminal cases:
lease-expired plus a survivor is `abandoned`, and lease-expired without a
survivor is `inactive` (`prd.md:165-170`). `abandoned` itself is limited to an
expired Lease or lost Heartbeats (`prd.md:142`, `prd.md:423-430`). A Runtime
that survives an explicit release, completion, or revocation therefore matches
historical intent but has neither a Promise Outcome nor a required Observation
label. Treating it as `orphaned` would also contradict that historical match
(`prd.md:125`, `prd.md:137`, `prd.md:387-394`).

This is phase-blocking, not merely a storage-design question. The Brief,
attention ranking, Safe-to-stop input, filters, and fixtures cannot agree until
the product says how each closed reason combines with a surviving Observation.

Minimal remediation: add closed-reason transitions to the orthogonal model.
Specify the Promise Outcome and required Observation label for a survivor after
release, completion, and revocation, including incomplete-evidence behavior.
Do not make closure itself mutation authorization.

#### H-2 — Blocker: mutation outcome vocabularies disagree within the contract

FR-40 requires `verified`, `unverified`, `refused`, `timed-out`, `failed`, or
`completed-with-diagnostic` (`prd.md:580-587`). SM-3 instead declares that
every mutation case ends in only `verified`, `unverified`, `refused`,
`timed-out`, or `failed` (`prd.md:664-666`). The current architecture and epics
use another set: `ExecutedUnverified`, `Stale`, and `Failed` in the architecture
(`ARCHITECTURE-SPINE.md:75-79`), and `Verified`, `Executed-Unverified`, `Stale`,
`Refused`, or `Failed` in Story 3.5 (`epics.md:638-644`). Neither downstream
artifact represents the PRD's `timed-out` or `completed-with-diagnostic` as
canonical terminal states, while the PRD does not represent post-execution
replacement as `stale`.

This is phase-blocking because partial failure and a mutation race are exactly
where optimistic reporting becomes dangerous. Acceptance tests cannot prove
SM-3 while conforming to FR-40, and downstream work cannot map replacement,
timeout, successful execution without verification, and successful execution
with diagnostics without inventing aliases or precedence.

Minimal remediation: publish one canonical action-outcome enum and transition
table. Map command termination, postcondition result, replacement identity,
verification timeout, and diagnostics to exactly one outcome, then make FR-40,
SM-3, architecture, and epics use those names.

### Medium

#### M-1 — Downstream alignment blocker: canonical traceability stops at the PRD

The PRD says its `FR-*` and `NFR-*` identifiers are the stable identifiers
consumed by architecture, epics, stories, and readiness (`prd.md:10-16`). The
addendum maps all legacy `FR1` through `FR18` identifiers to the canonical set
(`addendum.md:30-55`), but `epics.md` still declares and traces only the legacy
IDs (`epics.md:21-149`) and its stories still cite them, for example Story 3.5
(`epics.md:616-618`). The July 15 readiness report warned that internally
consistent, non-canonical traceability can conceal omitted product requirements
(`implementation-readiness-report-2026-07-15.md:178-184`). The new Promise,
Lease, direct-process, reconciliation, baseline, and Brief requirements have no
story coverage in the current epic set.

This does not require another PRD decision. It blocks implementation readiness,
not PRD correction or the start of downstream design.

Minimal remediation: regenerate the epic requirement inventory and coverage
map from canonical `FR-1` through `FR-43` and `NFR-1` through `NFR-16`, add
missing stories, and rerun readiness. Keep the legacy table only as migration
history.

#### M-2 — Downstream design work: public identity stability is unclear

The PRD requires stable Provider identities for correlation and exact-target
mutation (`prd.md:118`, `prd.md:360-367`, `prd.md:553-560`) and states that
Provider identity rules become public contracts once released
(`prd.md:762-767`). The current architecture defines a concrete `EntryId` but
says v1 IDs are not a durable external API (`ARCHITECTURE-SPINE.md:117-121`).
These claims can coexist only if the external stable identity, serialized ID,
and internal snapshot/generation identity are explicitly separated.

This is not a missing product outcome and does not block UX exploration. It
must close in architecture and schema design before machine contracts or
compatibility fixtures are frozen.

Minimal remediation: define which identity components are stable across
refresh, restart, provider recreation, and release versions; version any
serialized identifier; and state whether `EntryId` is internal while a separate
Provider identity is public.

#### M-3 — Downstream design work: incomplete-baseline acceptance

FR-27 correctly prevents ordinary refreshes from moving the Accepted Baseline
and makes incomplete Snapshots ineligible by default (`prd.md:451-461`). It
also permits an override that records missing scope, principal, timestamp, and
reason (`prd.md:460`). FR-28 promises an incomplete-window indication
(`prd.md:467-475`). What remains unspecified is the operator-facing acceptance
rule: whether the override is available non-interactively, what confirmation or
explicit flag it requires, and whether future deltas continue to carry the
baseline's missing-scope taint until a complete baseline is accepted.

This is downstream UX and command-contract work because the product has already
made the core policy choice: explicit override is permitted and audited. It is
not a reason to reopen Accepted Baseline semantics.

Minimal remediation: in UX and Agent/CLI contracts, require an explicit
override gesture or flag, display the lost comparison scope before acceptance,
and propagate baseline incompleteness in every Evidence Window derived from it.

### Low

#### L-1 — Downstream design work: cron discovery limits

The v1 table makes `/etc/crontab` and "readable `/etc/cron.d` files" required,
then says unreadable discovered files make the Brief incomplete
(`prd.md:309-315`). The qualifier leaves the directory-enumeration case
implicit: inability to list `/etc/cron.d` could otherwise prevent files from
being "discovered" and evade the unreadable-file rule. This is narrower than
the earlier coverage-scope blocker because the PRD now assigns obligations and
requires included and excluded permission boundaries to be listed
(`prd.md:324`).

Minimal remediation: make successful enumeration of `/etc/cron.d` part of the
required obligation, and classify enumeration denial or failure as incomplete.

## Areas tested without a supported defect

The following requested attack surfaces are now sufficiently explicit at the
product-contract level and do not justify invented findings:

- Collection Obligations are assigned by provider and sub-scope, including
  Promise-driven promotion and honest `out-of-scope` behavior
  (`prd.md:299-324`).
- Promise Lifecycle, Evidence Status, Promise Outcome, and Observation labels
  are orthogonal, with explicit lost-Heartbeat and incomplete-evidence rules
  except for H-1 (`prd.md:146-170`).
- Runtime Promises explicitly exclude arbitrary business or tool outcomes in
  v1 (`prd.md:127`, `prd.md:449`).
- Accepted Baseline refresh, first-run, incompatible-baseline, timezone, and
  retention behavior are specified (`prd.md:451-461`).
- The positive `safe` rule includes fresh identity, complete relevant
  collection, intent, dependencies, recreation policy, operation conflicts,
  and exact duplicate/release conditions (`prd.md:441-449`).
- Inherited TUI, mutation, Rust migration, and release scope is explicitly
  labeled owner-approved rather than inferred from the thesis
  (`prd.md:631-646`).
- The layered compatibility oracle distinguishes behavior inventory, frozen
  fixtures and goldens, live-host smoke, named consumers, and intentional
  deviations (`prd.md:335-345`, `prd.md:734-736`; `addendum.md:14-21`).
- Start has a discoverable TUI path through the Action Menu from a Runtime
  Promise with no Observation (`prd.md:531-538`).
- Refresh generations, operation identities, duplicate suppression, and
  independent verification establish the required mutation-race invariant at
  the product level (`prd.md:571-578`, `prd.md:726-728`).

## Phase gate

**FAIL.** H-1 and H-2 are unresolved product-contract blockers. M-1 blocks a
future implementation-readiness pass, while M-2, M-3, and L-1 are bounded
downstream design corrections and do not independently fail the PRD phase.
Resolve the two high findings in the canonical contract, reconcile the epics to
stable IDs, then rerun adversarial review and implementation readiness.
