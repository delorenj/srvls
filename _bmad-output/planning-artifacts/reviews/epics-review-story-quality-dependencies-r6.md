---
type: epic-story-review
reviewedCommit: ad723085bb29930789c19c589c770be89db73778
reviewedArtifact: _bmad-output/planning-artifacts/epics.md
observedSha256: 72c1b7dd7ea4941b98526aecc733e67d61de043b4492a0cbc0d8679d760e1cba
verdict: FAIL
findingCount: 9
storyCount: 75
acceptanceCriterionCount: 150
declaredDependencyEdgeCount: 74
---

# R6 Story Quality and Dependency Review

## Verdict

**FAIL — 9 findings covering 12 concrete issue instances. PASS requires zero.**

The batch-5 revision closes R5-02 through R5-05 at their original surfaces,
but R5-01 remains open in two independently observable ways. The two newly
added journey stories also expose duplicate ownership in their predecessor
gates, two stories name acceptance oracles that disagree with their normative
AD-11 rows, the FirstInstall story contradicts itself about the ready
generation, the prose inventory remains at 73, and four Validation Expectations
contain mechanically duplicated approval clauses. The artifact's current
`assignable: false` and `implementationAuthority: false` state remains correct.

## Digest

| Check | Result |
| --- | --- |
| Commit | `ad723085bb29930789c19c589c770be89db73778` |
| Commit subject | `fix(planning): close batch 5 assignment and traceability findings` |
| Artifact | `_bmad-output/planning-artifacts/epics.md` |
| Requested SHA-256 prefix | `72c1b7dd` |
| Observed SHA-256 | `72c1b7dd7ea4941b98526aecc733e67d61de043b4492a0cbc0d8679d760e1cba` |
| Digest disposition | Exact match |
| Git blob | `a8d3bee80ef75425bd88c9c56ba5b2120b7dce9f` |
| Size | 4,112 lines; 211,025 bytes |

## Review Scope and Method

1. Pinned the review to the requested digest and HEAD commit and reviewed the
   full `a01028a..ad72308` story delta: 315 insertions and 177 deletions.
2. Re-audited every R5 finding against the current contracts, story prose,
   acceptance criteria, Validation Expectations, normative JSON registry,
   fixture paths, architecture, and validators.
3. Parsed all 75 Story headings and required sections. Counts by epic are
   `10, 6, 11, 10, 10, 13, 15`. Every story has one user-value statement,
   Implementation Boundary, Requirement Mapping, Dependencies, Validation
   Expectations, Out of Scope, and exactly two numbered Given/When/Then
   criteria: 150 ACs total.
4. Parsed all dependencies. Story 1.1 alone declares `None`; every other story
   names exactly one existing earlier Story ID. The graph has 74 edges, no
   unresolved reference, no forward edge, and no cycle.
5. Parsed the normative JSON registry in both directions. It contains 75 unique
   stories in exact heading order, 87 unique AD-11 rows matching
   `canonicalCounts.ad11Rows`, 213 reciprocal requirement keys, no unknown
   owner, and no duplicate AD-11 ID.
6. Compared story-level owning-oracle prose with the normative AD-11 fixture
   owned by the same story. Stories 4.10 and 6.12 retain unexplained competing
   authority paths.
7. Searched the full repository for Contract C-23 row IDs,
   `fixture-approvals`, and approval enforcement. Outside `epics.md`, no
   implementation or validator references any of them.
8. Counted generic criteria across the complete backlog. Fifty-one positive
   ACs still execute only a "named fixture's positive scenario"; 58 negative
   ACs use a self-referential "concrete input and boundary"; 59 make the
   implementation test's rejection the expected outcome. Sixty-five of 87
   AD-11 fixture paths are absent at this commit.
9. Ran `python3 tests/validate_planning_quarantine.py`,
   `bash tests/validate_architecture_contracts.sh`, and the nested compatibility,
   contract, release, and Host smoke validators. All pass, but none parses the
   75 story blocks, validates AC row closure, compares story oracles with AD-11,
   or enforces Contract C-23 approvals.

## R5 Finding Accounting

| R5 finding | R6 disposition | Evidence |
| --- | --- | --- |
| R5-01 | **Open, split** | R6-01 and R6-02. C-23 names row IDs and an approval document, but the underlying ACs remain generic and no validator enforces the prerequisite. |
| R5-02 | Closed | Story 1.10 now distinguishes coherent review-time draft discovery from promoted-final discovery and matches `validate_planning_quarantine.py` (`epics.md:2596-2599`; validator `43-49`). |
| R5-03 | Closed at the reported surfaces | Stories 7.8 and 7.10 now name and consume installed-prior authorities (`epics.md:3942-3950`, `3988-3996`); no FirstInstall semantic forward edge remains there. |
| R5-04 | Closed | Story 7.4 AC2 now sequences preimage capture after exact ordered `ManagedConsumerUnitContractV1` and `BrownfieldConsumerPairsV1` readback (`epics.md:3856-3859`). |
| R5-05 | Closed at the missing-owner surface | Story 7.12 AC1 now owns successful FirstInstall publication, ready admission, terminal commit, and recovery cuts (`epics.md:4040-4041`), subject to R6-08. |

## All-Story AC and Dependency Accounting

`R6-01(P)` marks a generic positive fixture scenario. `R6-01(N)` marks a
self-referential input and/or test-rejection outcome. R6-02 is global and is
not repeated in every row. An em dash means no additional story-local finding.

| Story | Findings |
| --- | --- |
| 1.1 | R6-01(N) |
| 1.2 | R6-01(P), R6-01(N) |
| 1.3 | R6-01(P), R6-01(N) |
| 1.4 | R6-01(P), R6-01(N) |
| 1.5 | R6-01(P), R6-01(N) |
| 1.6 | R6-01(P), R6-01(N) |
| 1.7 | R6-01(P), R6-01(N) |
| 1.8 | R6-01(P), R6-01(N) |
| 1.9 | R6-01(P), R6-01(N) |
| 1.10 | R6-01(P) |
| 2.1 | R6-01(P) |
| 2.2 | R6-01(N) |
| 2.3 | R6-01(P) |
| 2.4 | R6-01(P), R6-01(N) |
| 2.5 | R6-01(P), R6-01(N) |
| 2.6 | R6-01(N) |
| 3.1 | R6-01(P), R6-01(N) |
| 3.2 | R6-01(P), R6-01(N) |
| 3.3 | R6-01(P) |
| 3.4 | R6-01(P) |
| 3.5 | R6-01(P) |
| 3.6 | R6-01(P), R6-01(N) |
| 3.7 | R6-01(P), R6-01(N) |
| 3.8 | R6-01(P) |
| 3.9 | R6-01(P), R6-01(N) |
| 3.10 | R6-01(N) |
| 3.11 | R6-01(N) |
| 4.1 | R6-01(P), R6-01(N) |
| 4.2 | R6-01(P), R6-01(N) |
| 4.3 | R6-01(P), R6-01(N) |
| 4.4 | R6-01(P), R6-01(N) |
| 4.5 | R6-01(P), R6-01(N) |
| 4.6 | R6-01(P), R6-01(N) |
| 4.7 | R6-01(P), R6-01(N) |
| 4.8 | R6-01(N) |
| 4.9 | R6-01(P), R6-01(N) |
| 4.10 | R6-01(N), R6-06 |
| 5.1 | R6-01(P), R6-01(N) |
| 5.2 | R6-01(P), R6-01(N) |
| 5.3 | R6-01(P), R6-01(N) |
| 5.4 | R6-01(P), R6-01(N) |
| 5.5 | R6-01(N) |
| 5.6 | R6-01(P), R6-01(N) |
| 5.7 | R6-01(P), R6-01(N) |
| 5.8 | R6-01(P), R6-01(N) |
| 5.9 | R6-01(N), R6-04 |
| 5.10 | R6-09 |
| 6.1 | R6-01(P), R6-01(N) |
| 6.2 | R6-01(P), R6-01(N) |
| 6.3 | R6-01(P), R6-01(N) |
| 6.4 | — |
| 6.5 | R6-01(P), R6-01(N) |
| 6.6 | R6-01(P) |
| 6.7 | R6-09 |
| 6.8 | R6-01(P), R6-01(N) |
| 6.9 | R6-01(P) |
| 6.10 | R6-01(P), R6-01(N) |
| 6.11 | R6-01(P), R6-01(N) |
| 6.12 | R6-01(N), R6-05, R6-07 |
| 6.13 | R6-09 |
| 7.1 | R6-01(P), R6-01(N) |
| 7.2 | R6-01(P), R6-01(N) |
| 7.3 | R6-01(P) |
| 7.4 | R6-01(N) |
| 7.5 | R6-01(N) |
| 7.6 | R6-01(N) |
| 7.7 | R6-01(P), R6-01(N) |
| 7.8 | R6-01(N) |
| 7.9 | R6-01(N) |
| 7.10 | R6-01(N) |
| 7.11 | R6-01(N) |
| 7.12 | R6-08, R6-09 |
| 7.13 | R6-01(N) |
| 7.14 | R6-01(P), R6-01(N) |
| 7.15 | R6-01(N) |

## Findings

1. **R6-01 — Contract C-23 labels rows but does not close the generic
   acceptance truth.** C-23 says each complete Given/When is the input and each
   complete Then/And is the observable result (`epics.md:503-514`). Across the
   150 criteria, 51 positive rows still say only that a named fixture's
   positive scenario executes, 58 negative rows refer to "the concrete input
   and boundary named in this criterion" without naming that input, and 59 use
   "the owning acceptance test rejects the implementation" as the result.
   Representative cases are Stories 1.2 (`2412-2415`), 4.10 (`3228-3231`),
   6.12 (`3739-3742`), and 7.15 (`4109-4112`). An approval hash can freeze a
   future test, but the current criterion still does not determine the row's
   exact input, product result, serialization/exit, or precedence. R5-01
   remains open.

2. **R6-02 — The new independent-approval prerequisite is prose-only and can
   be bypassed by promotion or assignment.** C-23 requires a fixture approval
   document and an explicit approval-commit dependency before assignment
   (`epics.md:508-514`), and every story repeats the requirement. A full-repo
   search finds no `fixture-approvals`, AC-row-ID, or C-23 consumer outside
   `epics.md`. `tests/validate_architecture_contracts.sh` only runs the existing
   compatibility, quarantine, contract, release, smoke, and optional Cargo
   tests (`tests/validate_architecture_contracts.sh:9-22`); the promotion
   validator accepts a coherent final triplet without checking approval files
   or commit dependencies (`tests/validate_planning_quarantine.py:43-49`). A
   change can set `status: final`, `assignable: true`, and
   `implementationAuthority: true` and pass the named gates with zero C-23
   approvals. The remediation therefore does not make R5-01's independent gate
   enforceable.

3. **R6-03 — The authoritative prose still declares 73 stories while the
   artifact contains 75.** The introduction says "73 sequential stories"
   (`epics.md:40`), while `canonicalCounts.stories` is 75 (`527`) and the file
   contains 75 unique headings. A consumer that trusts the prose instead of the
   JSON registry can omit new Stories 5.10 and 6.13 while believing the backlog
   complete.

4. **R6-04 — Story 5.9's positive AC still executes the complete morning
   journey that its boundary assigns to Story 5.10.** Story 5.9 limits itself
   to immutable read-only component goldens and budgets and explicitly says the
   end-to-end morning route belongs to Story 5.10 (`epics.md:3426`). Its AC1
   nevertheless runs entry, scan, filter, refresh, inspect, baseline, Stack,
   unmatched Promise/Observation, and exit (`3438-3439`). Story 5.10 then owns
   that same integrated route (`3449`, `3461-3462`). The earlier story cannot
   satisfy its AC without implementing or depending semantically on the later
   story, creating an undeclared forward edge and duplicate journey ownership.

5. **R6-05 — Story 6.12's positive AC still executes the complete action
   journey that its boundary assigns to Story 6.13.** Story 6.12 says it owns
   only accessibility, responsive preservation, confirmation/help,
   disposition, and UX-BUD-4/5/6 and explicitly assigns the complete journey to
   Story 6.13 (`epics.md:3727`). AC1 still runs the "full plan-to-outcome
   journey" across TUI, linear, JSON, raw mode, modal, refresh, replacement,
   all five outcomes, and timing limits (`3739-3740`). Story 6.13 then owns the
   same select-through-outcome integration (`3750`, `3762-3763`). This is
   another semantic forward edge hidden by the mechanically linear dependency
   graph.

6. **R6-06 — Story 4.10 names an owning oracle different from its normative
   AD-11 row.** Validation Expectations call
   `tests/fixtures/implementation/brief-grouping-v1` the owning oracle
   (`epics.md:3222`), but AD11-FUT-63 assigns Story 4.10 to
   `tests/fixtures/implementation/grouping-v1` and
   `assert_stack_ungrouped_properties` (`2274-2278`). Neither path exists and no
   aggregate or alias relation is defined. C-23 approval therefore has two
   competing candidates for the same story's expected bytes.

7. **R6-07 — Story 6.12 names an owning oracle different from its normative
   AD-11 row.** Validation Expectations call
   `tests/fixtures/implementation/action-aggregate-v1` the owner
   (`epics.md:3733`), while AD11-FUT-73 assigns Story 6.12 to
   `tests/fixtures/implementation/action-accessibility-budget-v1` and
   `assert_action_budgets_and_accessibility` (`2354-2358`). Neither path exists
   and no composition rule links them. The story cannot identify which fixture
   and expected-result hash an independent reviewer must approve.

8. **R6-08 — Story 7.12's boundary requires ready generation zero while its
   success AC requires ready generation one.** The boundary says FirstInstall
   proves complete absence "before ready generation zero" (`epics.md:4028`).
   AC1 says a successful FirstInstall publishes KnownGood generation 1 and
   persists/read-backs ready admission before `committed` (`4040-4041`), which
   matches the architecture's target-generation rule. Reserved generation zero
   belongs to restored-absence recovery, not successful readiness. The current
   boundary does not scope its generation-zero statement to failure recovery,
   so an implementation cannot satisfy both readings deterministically.

9. **R6-09 — Four Validation Expectations contain duplicated approval prose
   and malformed `.;` joins.** Stories 5.10, 6.7, 6.13, and 7.12 each retain an
   older approval sentence and then append the generic C-23 sentence after
   `.;` (`epics.md:3455`, `3618`, `3756`, `4034`). Story 6.7's retained clause
   still describes the old "checked in for independent review" process rather
   than the new approval artifact, while the other three redundantly declare
   C-23 approval twice. These are four concrete story-quality defects and make
   the normative Validation Expectations ambiguous about whether one or two
   approval mechanisms apply.

## Passing Evidence

- The requested digest, Git blob, file size, heading inventory, required
  sections, AC count, declared dependency grammar, earlier-only ordering, and
  declared acyclicity pass.
- The normative registry's story order/count, AD-11 row count, unique IDs,
  owner existence, reciprocal requirement coverage, and AD-11 owner
  reciprocity pass.
- Stories 5.10 and 6.13 are present in the story inventory, reciprocal coverage
  maps, dependency chain, and AD-11 registry as AD11-FUT-72 and AD11-FUT-43.
- R5-02 through R5-05 are closed at their original reported surfaces as
  detailed above.
- `python3 tests/validate_planning_quarantine.py` passes.
- `bash tests/validate_architecture_contracts.sh` passes, including compatibility,
  planning quarantine, contract oracles, release oracles, and Host smoke.

## Final Gate

**FAIL. Finding count: 9. Concrete issue instances: 12. PASS threshold: 0.**
