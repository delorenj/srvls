---
type: epic-story-review
reviewer: SyntaxSorcerer
reviewedCommit: b959e2ada0f61d6928dc270a793280b0acd6217e
reviewedArtifact: _bmad-output/planning-artifacts/epics.md
requiredSha256: 0189960e42776cf3f5fe86dcf3cc3344ce307d987877d9c5600277b43b1f1523
observedSha256: 0189960e42776cf3f5fe86dcf3cc3344ce307d987877d9c5600277b43b1f1523
verdict: FAIL
findingCount: 18
storyCount: 55
acceptanceCriterionCount: 165
---

<!-- markdownlint-disable MD013 -->

# Canonical Epics Story-Quality and Dependency-Order Review

## Verdict

**FAIL — 18 findings.**

The gate rule is PASS only when the finding count is zero. The artifact passes
the digest, inventory, required-section, explicit textual ordering, exact-title
duplicate, TUI Action Menu, Promise-origin Start, and primary action
plan/execution-separation checks. It does not pass the complete story-quality
and dependency-order gate because 18 scoped findings remain.

## Settled Artifact and Digest

| Check | Result |
| --- | --- |
| Reviewed commit | b959e2ada0f61d6928dc270a793280b0acd6217e |
| Commit subject | docs(backlog): draft canonical epics and stories |
| Reviewed path | _bmad-output/planning-artifacts/epics.md |
| Required SHA-256 | 0189960e42776cf3f5fe86dcf3cc3344ce307d987877d9c5600277b43b1f1523 |
| SHA-256 from git show | 0189960e42776cf3f5fe86dcf3cc3344ce307d987877d9c5600277b43b1f1523 |
| SHA-256 from checked-out file | 0189960e42776cf3f5fe86dcf3cc3344ce307d987877d9c5600277b43b1f1523 |
| Digest disposition | MATCH |
| Artifact size | 2,810 lines; 144,820 bytes |

The review scope was the exact epics.md blob at the reviewed commit. No PRD,
architecture, UX artifact, retired backlog, implementation, or later commit was
used to fill gaps in the reviewed story text.

## Methodology

1. Pinned the review to commit b959e2a and verified both the Git blob stream and
   checked-out file against the required SHA-256.
2. Parsed every Epic and Story heading and reconciled the inventory to seven
   epics and 55 unique numbered stories.
3. Checked each story for a user-value statement, Implementation Boundary,
   Requirement Mapping, Dependencies, Validation Expectations, Out of Scope,
   and Acceptance Criteria.
4. Parsed all 165 numbered ACs and verified that every AC contains explicit
   Given, When, Then, and And clauses.
5. Reviewed each AC for an observable oracle, a determinate result, controlled
   preconditions, and freedom from an unspecified approval or external choice.
6. Built the declared dependency order from all 55 Dependencies fields,
   including ranges and epic prerequisites. Every explicitly numbered story
   reference resolves to an earlier story; no declared-field forward edge or
   declared-field cycle was found.
7. Built a second semantic ownership graph from the components each story says
   it implements or validates. This catches hidden ordering cycles that prose
   dependency fields do not expose.
8. Compared titles, user-value statements, implementation boundaries,
   transaction owners, and acceptance effects for exact and semantic
   duplication.
9. Reviewed the closed Host-action vocabulary, Action Menu, Promise-origin
   Start, confirmation behavior, ActionPlan versus ActionExecutor ownership,
   operation outcome vocabulary, read-only group behavior, bounded Host runner
   boundary, runtime orchestration, and release rollback behavior.
10. Assessed single-agent implementability by asking whether one story has one
    coherent value increment, one primary implementation owner, a bounded test
    surface, and no external approval needed to reach Done.
11. Applied the requested verdict rule mechanically: any finding produces
    FAIL; only zero findings can produce PASS.

## Inventory and Per-Epic Counts

Findings are counted once under their primary owning epic. Cross-epic finding
F-04 is counted under Epic 3, its first dependency whose prerequisite cannot be
resolved to a prior story. Cross-epic finding F-05 is counted under Epic 3, the
first story claiming the overlapping transaction.

| Epic | Stories reviewed | ACs reviewed | Primary findings | Finding IDs |
| --- | ---: | ---: | ---: | --- |
| 1 — Trustworthy Rust and Durable Storage Foundation | 8 | 24 | 1 | F-01 |
| 2 — Runtime Promise Lifecycle | 5 | 15 | 2 | F-02, F-03 |
| 3 — Five-Provider Discovery Including Direct Processes | 9 | 27 | 2 | F-04, F-05 |
| 4 — Reconciliation, Baseline, and Morning Brief | 9 | 27 | 3 | F-06, F-07, F-08 |
| 5 — Interactive TUI | 7 | 21 | 1 | F-09 |
| 6 — Safe Exact-Target Actions | 8 | 24 | 5 | F-10 through F-14 |
| 7 — Release and Recovery | 9 | 27 | 4 | F-15 through F-18 |
| **Total** | **55** | **165** | **18** | **F-01 through F-18** |

## Cross-Cutting Checks

| Review dimension | Disposition | Evidence |
| --- | --- | --- |
| Required story sections | Satisfied | All 55 stories contain all six reviewed sections. |
| Concrete GWT shape | Structurally satisfied | All 165 ACs contain Given/When/Then/And; F-02, F-07, F-08, F-11, and F-13 identify substantive oracle gaps. |
| Explicit textual order | Satisfied with qualification | All explicitly numbered references point backward; F-04 identifies non-normalized capability/epic prose that prevents an exact graph. |
| Exact duplicate titles or bodies | None found | All 55 titles and normalized story bodies are unique. |
| Semantic duplicate/ambiguous ownership | Not satisfied | F-05, F-12, F-15, and F-16. |
| TUI Action Menu | Satisfied | Story 6.1 owns a read-only Action Menu and disabled explanations. |
| Promise-origin Start | Satisfied | Story 6.1 AC 2 provides an explicit Promise-detail Start path and prohibits inferred/direct-process Start. |
| Read-only groups | Satisfied | Stories 4.9, 5.2, and 6.1 prohibit group mutation and hidden bulk targets. |
| Closed canonical action kind | Not satisfied | F-10. |
| ActionPlan versus execution | Satisfied for the main Epic 6 pipeline | Stories 6.1–6.7 separate discovery, planning, preflight, admission, execution, and verification; F-12 identifies a pool-order defect and F-17 identifies a rollback exception. |
| Canonical Action Outcome names | Satisfied | verified, executed-unverified, refused, timed-out, and failed are used consistently. |
| Action Outcome precedence | Not testable | F-13. |
| Bounded runner versus orchestration | Not satisfied | F-01 combines the low-level Host runner with aggregate gate orchestration and premature budget ownership. |
| Single-agent sizing | Not satisfied | F-01, F-08, F-09, F-14, F-17, and F-18. |

## Findings

The finding order follows document order and is not a severity ranking.

1. **F-01 — Story 1.8 combines the bounded Host runner with aggregate
   verification orchestration and an unowned budget lane.** The boundary gives
   one story process spawning, capture limits, timeout escalation, descendant
   reaping, descriptor policy, privilege request typing, fake execution, the
   aggregate AD-11 coordinator, and ARCH-HOST-1 evidence. Its validation then
   requests 30-iteration p95 evidence while its Out of Scope excludes future
   gate matrices; AC 3 nevertheless requires a budget lane. This is more than
   one independently assignable implementation boundary, and the applicable
   runner-only measurement is not identified. Evidence: epics.md:670-714.
   Separate CommandRunner and its contract suite from aggregate foundation-gate
   wiring. Name only runner-owned measurements here and leave refresh/TUI/action
   budgets to their owning stories.

2. **F-02 — Story 2.2 AC 2 accepts two different results for the same stated
   preconditions.** For invalid persistent intent, the Then clause permits the
   policy to reject the request or retain it as unmanaged, but the Given clause
   does not identify a policy value that selects either branch. Two incompatible
   implementations can therefore satisfy the same AC. Evidence:
   epics.md:788-810. Add the exact policy enum/default to the Given clauses and
   split reject and retain-as-unmanaged into separate cases with deterministic
   machine results.

3. **F-03 — Runtime lifecycle authentication and authorization have no
   implementation owner or testable trust boundary.** Story 2.3 requires an
   authenticated Heartbeat and unauthorized outcomes, while Story 2.4 requires
   an authorized principal for release, complete, and revoke. Their
   dependencies provide Owner fields, revisions, and leases, but no credential,
   operating-system principal, local-socket trust, key binding, or
   authorization rule. Matching a caller-supplied Owner value is not
   authentication. Evidence: epics.md:812-849 and epics.md:851-887. Assign the
   principal/authentication contract to a prior story, define how Owner is
   bound to that principal, and add impersonation, credential rotation, and
   authorization-boundary ACs.

4. **F-04 — The dependency grammar is not consistently explicit enough to
   produce one deterministic scheduling graph.** Examples include “Epic 1,
   especially Stories 1.3, 1.4, and 1.6,” “promoted Collection Obligations from
   Epic 2,” “Epic 3 generation contracts,” “exact Provider identities from Epic
   3,” “Epic 5 event loop,” “Epic 6 operation handoffs,” and “every prior epic
   aggregate gate.” The first phrase does not say whether the non-highlighted
   Epic 1 stories are blockers; the capability phrases do not identify their
   owning story at all. All named numbers are backward, but the complete edge
   set is not machine-resolvable or unambiguous. Evidence: epics.md:744,
   epics.md:962, epics.md:1915, epics.md:2060, epics.md:2147,
   epics.md:2277, epics.md:2469, and epics.md:2781. Replace capability prose and
   “especially” with exact story IDs or one explicitly defined “epic complete”
   gate whose owning story is named.

5. **F-05 — Stories 3.8 and 4.7 both claim overlapping Snapshot transaction
   authority without a named handoff.** Story 3.8 owns latest-generation CAS,
   accepted reports/diagnostics/samples, and a “Snapshot candidate
   transaction”; its AC says the entire accepted candidate commits atomically.
   Story 4.7 later owns SnapshotV1 atomic materialization of reports,
   diagnostics, Observations, samples, findings, and the latest-current CAS.
   The text does not say whether Story 3.8 writes a distinct staging aggregate,
   whether Story 4.7 copies or references those rows, or which transaction owns
   the current pointer. Evidence: epics.md:1236-1278 and epics.md:1579-1608.
   Define a distinct CollectionCandidateV1 and its immutable handoff to
   SnapshotV1, or give one story sole ownership of the shared rows and current
   CAS.

6. **F-06 — Story 4.3 cannot identify member-level “exact excess identities”
   without defining the loser-selection rule it places Out of Scope.** With an
   intended count of one and multiple equally exact running matches, naming
   particular members as excess necessarily chooses which member fills the
   intended slot. The story simultaneously prohibits choosing a duplicate
   loser or mutation target. Evidence: epics.md:1416-1451. Define the result as
   a duplicate set plus excess cardinality, with no member designated excess,
   or provide a deterministic membership rule and explicitly state that it is
   not an action recommendation.

7. **F-07 — Story 4.8 requires “all eight” morning answers without identifying
   the eight test oracles in the reviewed artifact.** FR-28, SM-1, the
   implementation boundary, and AC 1 repeat the count, but no eight question
   IDs or question texts appear in epics.md. A fixture can claim completeness
   while answering a different set. Evidence: epics.md:122-123,
   epics.md:203-204, and epics.md:1623-1668. Enumerate the eight question IDs in
   the story or cite one exact immutable source section and make each question
   a checked matrix row.

8. **F-08 — Story 4.9 mixes deterministic grouping implementation with an
   external Product Owner approval gate.** Grouping tiers, path normalization,
   candidate ordering, labels, facets, and Ungrouped behavior are assignable to
   one implementation agent. Producing an approved Provider-by-Provider impact
   baseline and Product Owner decision is a separate governance/research
   outcome outside that agent’s control. The story cannot reach Done
   independently. Evidence: epics.md:1671-1714. Split the impact decision into
   a non-implementation gate with a named approver and artifact, or make an
   already approved decision record an input dependency to the grouping story.

9. **F-09 — Story 5.7 is an oversized closure story with multiple independent
   owners.** It combines help-overlay product work, invalid-configuration
   recovery, the complete read-only state/component matrix, small-terminal
   behavior, resize coalescing, render/input instrumentation, the constrained
   host benchmark runner, golden-update governance, and the aggregate
   accessibility gate. Those are separately implementable UI, configuration,
   harness, performance, and governance increments. Evidence:
   epics.md:1984-2028. Split operator help/configuration recovery from
   state-matrix/golden coverage and from performance/aggregate gate closure.

10. **F-10 — The Host action vocabulary is listed but never owned as one closed
    canonical action enum.** FR-36 and Story 6.1 list
    start/stop/restart/disable/delete/signal, ActionPlanV1 stores a generic
    “Provider capability/op,” and Story 6.5 repeats provider-specific subsets.
    No story defines a versioned ActionKind encoding, casing, unknown-variant
    behavior, or the exact Provider-by-ActionKind matrix. This permits transport,
    plan, audit, and executor vocabularies to drift while each local test still
    passes. Evidence: epics.md:144-146, epics.md:2042-2079,
    epics.md:2086-2127, and epics.md:2215-2257. Give one prior story ownership
    of the closed ActionKind contract and require menu, plan, storage, executor,
    machine output, and fixtures to consume it.

11. **F-11 — Story 6.2 leaves Restart confirmation behavior ambiguous.** Its
    validation claims all action types, but AC 2 enumerates stop, disable,
    delete, signal, and unknown-safety actions while omitting Restart from the
    capability set introduced by Story 6.1. The title says confirmation is
    required, yet no AC classifies Restart as destructive or non-destructive.
    Implementations can therefore confirm or immediately submit Restart and
    both argue conformance. Evidence: epics.md:2048-2052 and
    epics.md:2086-2127. State the confirmation and acknowledgement rule for
    every ActionKind, including Start and Restart, in a complete matrix.

12. **F-12 — Stories 6.4 and 6.6 invert and duplicate action-pool ownership.**
    Story 6.4 reserves an action-pool slot and validates pool-full behavior.
    Story 6.5 then executes operations. Story 6.6, which depends on both,
    finally implements the separate bounded action pool, per-operation task,
    queue states, fairness, and saturation behavior. Story 6.4 cannot validate
    its stated admission behavior against a component implemented only by a
    dependent later story. Evidence: epics.md:2173-2213 and
    epics.md:2259-2300. Move the bounded pool primitive and contract before
    admission, or make Story 6.4 own the pool and limit Story 6.6 to TUI/event
    integration.

13. **F-13 — Story 6.7 names the five outcomes but does not provide the
    canonical precedence matrix its AC requires.** AC 2 says incomplete,
    unavailable, timed-out, identity-changed, or contradictory verification
    becomes executed-unverified, timed-out, or failed “as the canonical matrix
    specifies.” No such matrix appears in the reviewed artifact, so exact
    identity-race, contradiction, and timeout results are not independently
    testable. Evidence: epics.md:154-157 and epics.md:2302-2346. Include the
    full ordered decision table or cite a stable table identifier and require a
    fixture for every row.

14. **F-14 — Story 6.8 is too large for one independent implementation agent.**
    It combines TUI integration, linear commands, machine commands, phase-aware
    quit and signal disposition, terminal restoration before external
    authorization, recover/status commands, every action state, screen-reader
    parity, UX budgets, PTY tests, FD3 tests, storage tests, and aggregate gate
    closure. These are transport, lifecycle, accessibility, performance, and
    integration-gate work packages. Evidence: epics.md:2348-2396. Split surface
    integration, signal/recovery behavior, human-linear parity, and final
    aggregate verification into independently completable stories.

15. **F-15 — Stories 7.3 and 7.4 form a semantic ordering cycle around managed
    consumer preimages.** Story 7.3 must capture exact consumer preimage
    identities and checksums before any replaceable effect. Story 7.4, which
    depends on Story 7.3, is where named managed consumers are inventoried and
    their invocation contracts and preimage receipts are frozen. Story 7.3
    cannot know it captured “every named managed consumer” until the later
    inventory exists. Evidence: epics.md:2497-2539 and epics.md:2541-2584.
    Freeze a canonical ManagedConsumerManifest before Story 7.3, or remove
    consumer preimages from Story 7.3 and give Story 7.4 the complete
    preimage-before-rewrite transaction.

16. **F-16 — Story 7.6 requires recovery coverage for a KnownGood effect that
    Story 7.7 implements only after depending on Story 7.6.** The Story 7.6
    validation matrix cuts owner power before and after KnownGood, but
    KnownGoodV1 publication, its CAS, pins, and publication audit belong to
    Story 7.7. This creates an implicit verification cycle even though the
    textual dependency fields point backward. Evidence: epics.md:2628-2671 and
    epics.md:2673-2714. Keep Story 7.6’s recovery engine generic and wire/test
    KnownGood crash cuts in Story 7.7 or a later integration story, or move the
    KnownGood effect contract before Story 7.6.

17. **F-17 — Story 7.8 combines two recovery products and collapses rollback
    planning, confirmation, execution, verification, and recovery into one
    story.** First-install absence recovery and installed rollback are
    independently valuable paths. The installed path also crosses the
    plan/effect boundary that Epic 6 carefully separates: it plans, confirms,
    locks, restores binary/state/consumers, validates FD4, writes receipts, and
    recovers interruptions in one assignment. Evidence: epics.md:2716-2759.
    Split FirstInstall recovery from rollback, then split immutable rollback
    plan/confirmation from restore/verification/recovery execution or explicitly
    reuse the existing plan/admission/executor contracts.

18. **F-18 — Story 7.9 combines aggregate release verification with four
    operator command surfaces and the evidence bundle.** Wiring the complete
    release/fault-injection matrix into AD-11 is a closure task. Implementing
    status, recover, install, and rollback linear/machine interfaces and the
    runbook/evidence bundle is separate product-surface work with different
    acceptance and test owners. The story also maps every NFR, a strong signal
    that it is acting as a residual catch-all rather than one bounded increment.
    Evidence: epics.md:2761-2810. Move each command surface to the story owning
    its use case and retain a final story that only wires and proves the
    aggregate release gate.

## Complete Per-Story Review Ledger

“Clear” means no finding was identified for that story under the dimensions in
this review. It is not implementation evidence and does not override the
artifact-level FAIL.

| Story | Review result |
| --- | --- |
| 1.1 | Clear |
| 1.2 | Clear |
| 1.3 | Clear |
| 1.4 | Clear |
| 1.5 | Clear |
| 1.6 | Clear |
| 1.7 | Clear |
| 1.8 | F-01 |
| 2.1 | F-04 |
| 2.2 | F-02 |
| 2.3 | F-03 |
| 2.4 | F-03 |
| 2.5 | Clear |
| 3.1 | F-04 |
| 3.2 | Clear |
| 3.3 | Clear |
| 3.4 | Clear |
| 3.5 | Clear |
| 3.6 | Clear |
| 3.7 | Clear |
| 3.8 | F-05 |
| 3.9 | Clear |
| 4.1 | Clear |
| 4.2 | Clear |
| 4.3 | F-06 |
| 4.4 | Clear |
| 4.5 | Clear |
| 4.6 | Clear |
| 4.7 | F-05 |
| 4.8 | F-07 |
| 4.9 | F-08 |
| 5.1 | Clear |
| 5.2 | Clear |
| 5.3 | Clear |
| 5.4 | Clear |
| 5.5 | F-04 |
| 5.6 | Clear |
| 5.7 | F-09 |
| 6.1 | F-04, F-10 |
| 6.2 | F-10, F-11 |
| 6.3 | F-04, F-10 |
| 6.4 | F-12 |
| 6.5 | F-10, F-12 |
| 6.6 | F-04, F-12 |
| 6.7 | F-13 |
| 6.8 | F-14 |
| 7.1 | Clear |
| 7.2 | F-04 |
| 7.3 | F-15 |
| 7.4 | F-15 |
| 7.5 | Clear |
| 7.6 | F-16 |
| 7.7 | F-16 |
| 7.8 | F-17 |
| 7.9 | F-04, F-18 |

## Gate Closure Conditions

The next revision can receive PASS only after:

1. Every F-01 through F-18 correction is reflected in the canonical story set
   or is rebutted by concrete text in that same settled artifact.
2. The revised artifact has a newly settled SHA-256 and is reviewed from that
   exact blob.
3. The declared and semantic dependency graphs both contain only prior
   dependencies and no ownership cycle.
4. Every action and outcome branch is backed by a closed type and complete
   matrix.
5. Every story is independently assignable without an external approval and
   has one bounded implementation/test owner.
6. The repeated structural checks still reconcile to the intended story count
   with no missing sections, malformed ACs, or duplicate stories.

Until those conditions are met, commit b959e2a remains **FAIL** for story
quality and dependency order.
