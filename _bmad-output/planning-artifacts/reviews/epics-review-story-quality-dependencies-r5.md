---
type: epic-story-review
reviewedCommit: a01028a449a67b57c571d534e40721e8ee5da453
reviewedArtifact: _bmad-output/planning-artifacts/epics.md
observedSha256: 7d749899972903b90c76df2825bfbfaf0055e0f83544cd72cb7d648af8ad645c
verdict: FAIL
findingCount: 5
storyCount: 73
acceptanceCriterionCount: 146
declaredDependencyEdgeCount: 72
---

# R5 Story Quality and Dependency Review

## Verdict

**FAIL — 5 findings. PASS requires zero.**

The batch-4 revision closes four R4 findings, leaves three R4 findings open,
and leaves one R4 finding only partially closed. One additional FirstInstall
acceptance-owner gap remains. The declared story graph and normative registry
are mechanically sound, but the acceptance authorities and release-story
semantics are not yet deterministic enough for assignment. The artifact's
current `assignable: false` and `implementationAuthority: false` state is
therefore correct.

## Digest

| Check | Result |
| --- | --- |
| Commit | `a01028a449a67b57c571d534e40721e8ee5da453` |
| Commit subject | `fix(planning): close batch 4 authority and acceptance findings` |
| Artifact | `_bmad-output/planning-artifacts/epics.md` |
| Requested SHA-256 prefix | `7d749899` |
| Observed SHA-256 | `7d749899972903b90c76df2825bfbfaf0055e0f83544cd72cb7d648af8ad645c` |
| Digest disposition | Exact match |
| Git blob | `74160435982c5a87e65ee14e0823174e4a65e3c9` |
| Size | 3,974 lines; 206,820 bytes |

## Review Scope and Method

1. Pinned the review to the requested digest and HEAD commit, then reviewed the
   complete `4c26f29..a01028a` epic/story delta rather than accepting the
   remediation labels.
2. Re-audited R4-01 through R4-08 against the current story prose, ACs,
   Validation Expectations, registry rows, fixture contents, PRD, and
   architecture source precedence.
3. Parsed every Story heading and required section. The artifact contains seven
   epics and 73 unique stories in counts `10, 6, 11, 10, 9, 12, 15`. Every story
   has one user-value statement, Implementation Boundary, Requirement Mapping,
   Dependencies, Validation Expectations, Out of Scope, and exactly two
   numbered Given/When/Then criteria: 146 ACs total.
4. Parsed the declared dependency graph. Story 1.1 alone declares `None`; every
   later story names exactly one existing earlier Story ID. The result is 72
   declared edges, no unresolved reference, no forward edge, and no declared
   cycle.
5. Parsed the normative JSON registry in both directions. It contains 73 unique
   inventory stories, 84 unique AD-11 rows matching `canonicalCounts.ad11Rows`,
   213 requirement keys, reciprocal `coverageByStory` and
   `requirementCoverage`, no unknown owner, and no duplicate AD-11 ID.
6. Compared each AC's explicit fixture path with its Validation Expectations and
   owning AD-11 row. Exactly two explicit authority mismatches remain: Stories
   7.8 and 7.10.
7. Parsed the first and last transaction in the release authorities consumed by
   Stories 7.8 and 7.10. The named AC fixtures are FirstInstall authorities, not
   installed-prior authorities.
8. Ran four review layers. Blind adversarial, edge-case, and verification-gap
   layers completed and were independently triaged. The acceptance-auditor
   layer did not return after repeated completion requests and was stopped; no
   finding below relies on that failed layer.
9. Executed the repository's planning, architecture, and Host smoke validators.
   All pass, but none validates criterion-specific future fixture rows,
   AC-to-registry fixture agreement, or the semantic story dependency graph.

## R4 Finding Accounting

| R4 finding | R5 disposition | Evidence |
| --- | --- | --- |
| R4-01 | **Open** | R5-01. The rewritten template still defers positive and negative acceptance truth to future story-authored fixtures and tests. |
| R4-02 | **Open, transformed** | R5-02. The override branch was reversed, but Story 1.10 now requires non-final canonical state to fail while its named validator explicitly accepts that state. |
| R4-03 | Closed | The general precedence chain is restored and the artifact records exact post-source decision `UD-EPIC-C-1`, including both selected alternatives (`epics.md:33-38`). No separate decision-ledger contract exists. |
| R4-04 | Closed | Contract C-19 now defines required, optional, and forbidden argv, confirmation, success result, and exit behavior for all five verbs (`epics.md:435-457`); Story 7.3 binds to that matrix (`3683-3698`). |
| R4-05 | Closed | AD11-FUT-49 and Story 7.9 consistently use installed-prior pre-decision takeover, exclude FirstInstall and KnownGood work, and name only the two allowed terminals (`2082-2087`, `3821-3836`). |
| R4-06 | **Open** | R5-03. Stories 7.8 and 7.10 still consume FirstInstall AC authorities before Stories 7.11-7.12 own FirstInstall. |
| R4-07 | **Partially open** | R5-04. Story 7.4's title, value, boundary, and oracle were repaired, but AC2 still sequences work against undefined "the manifest." |
| R4-08 | Closed | Story 6.2 now explicitly opens the Action Menu for one exact target and emits only an immutable selection into Story 6.3 (`3374-3395`). |

## All-Story AC and Dependency Accounting

R5-01 applies across the backlog. Fifty-five positive ACs still execute only a
generic "named fixture's positive scenario." Sixty negative ACs now state only
that "the owning acceptance test rejects the implementation," without fixing
criterion-specific result tokens, serialization, exit status, failure
precedence, or exact rows. Seventy-two Validation Expectations say that the
story begins by checking in fixture rows before production implementation, but
that prose does not identify the rows or enforce an independent approval gate.
Sixty-two of the 84 normative AD-11 fixture paths are absent at the reviewed
commit.

Additional story-specific findings are exhaustive below; `—` means no
additional finding beyond R5-01 where applicable.

| Stories | Additional findings |
| --- | --- |
| 1.1-1.9 | — |
| 1.10 | R5-02 |
| 2.1-7.3 | — |
| 7.4 | R5-04 |
| 7.5-7.7 | — |
| 7.8 | R5-03 |
| 7.9 | — |
| 7.10 | R5-03 |
| 7.11 | — |
| 7.12 | R5-05 |
| 7.13-7.15 | — |

The declared 72-edge graph passes. R5-03 creates semantic forward dependencies
from Stories 7.8 and 7.10 into Stories 7.11-7.12, while the declared chain makes
7.11-7.12 transitively depend on 7.10. That semantic cycle is not represented in
the declared dependency fields.

## Findings

1. **R5-01 — Acceptance truth remains deferred to future story-authored
   fixtures and tests.** The batch-4 rewrite changes 72 Validation Expectations
   to say that each story begins by checking in fixture rows and expected bytes
   "for independent review before production implementation." It does not name
   those rows, expected bytes, an independent owner, an approval artifact, or a
   dependency that prevents production work before approval. Sixty-two of 84
   AD-11 fixture paths are absent. Fifty-five positive ACs still invoke only
   "the named fixture's positive scenario." Sixty negative ACs were weakened
   from an observable product result to "the owning acceptance test rejects the
   implementation," leaving result token, serialization, exit status, and
   failure precedence to the future test author. Representative evidence is
   Story 1.1 (`epics.md:2287-2296`), Story 2.3 (`2563-2572`), Story 4.3
   (`2962-2971`), Story 6.2 (`3386-3395`), and Story 7.15 (`3965-3974`). The
   same assignee can author a favorable or implementation-shaped fixture first
   and then satisfy it. R4-01 therefore remains open. Close this by fixing each
   criterion's row identity and observable expected result before assignment,
   and by making independent fixture acceptance an enforceable prerequisite.

2. **R5-02 — Story 1.10's non-final rejection AC contradicts its named live
   validator.** Story 1.10 AC2 says a missing or non-final canonical `epics.md`
   makes the validator exit 1 (`epics.md:2500-2503`). The reviewed artifact is
   explicitly `status: remediated-draft`, `assignable: false`, and
   `implementationAuthority: false` (`epics.md:1-6`), while
   `tests/validate_planning_quarantine.py:43-49` explicitly accepts either that
   draft triplet or the final triplet. The current non-final artifact therefore
   passes both the validator and aggregate. This is not merely missing future
   evidence: the story names the existing script as its owning oracle
   (`epics.md:2494`), and the remediation modified that script while leaving it
   opposite to the AC. R4-02 remains open in a new form. The story must either
   distinguish review-time draft discovery from promotion-time final authority
   or make its oracle reject every non-final state as written.

3. **R5-03 — Stories 7.8 and 7.10 still consume FirstInstall authorities before
   the stories that own FirstInstall.** The new registry rows correctly name
   installed-prior future authorities for Story 7.8 (`epics.md:2258-2263`) and
   Story 7.10 (`2090-2095`). Their ACs do not use them. Story 7.8 Validation
   Expectations name `installed-prior-forward-v1`, but AC1 directly consumes
   `forward.transitions.jsonl` (`3804`, `3810-3811`); its 35 rows all have
   `intent=install`, `prior_release.kind=first-install-absent`, generation 0 to
   1, and the last row is `committed`, beyond Story 7.8's `commit-decided`
   boundary. Story 7.10 excludes FirstInstall and names
   `installed-prior-known-good-v1`, but AC1 directly consumes
   `known-good-publication-pending.manifest.json` (`3850-3857`), whose sole
   transaction is FirstInstall generation 0 to 1. Stories 7.11-7.12 own
   FirstInstall later (`3861-3905`). The declared graph is acyclic, but the AC
   authorities create a semantic cycle and force earlier stories to implement
   later ownership. R4-06 remains open.

4. **R5-04 — Story 7.4 retains an undefined manifest as a normative sequencing
   authority.** The title, user value, and boundary now correctly name managed
   consumer unit discovery, ordered `ManagedConsumerUnitContractV1` rows, and
   `BrownfieldConsumerPairsV1` hashes (`epics.md:3700-3714`). AC2 still rejects
   preimage capture that "precedes the manifest" (`3720-3721`). Contract C-21
   allows only the ordered unit-contract rows, pair authority, transaction
   consumers, and hashes, and explicitly forbids `ManagedConsumerManifestV1`
   (`469-478`). Because AC2 does not identify which allowed authority it calls
   "the manifest," an implementation may reintroduce the forbidden aggregate or
   have no defined sequencing antecedent. R4-07 is only partially closed; AC2
   must name the exact ordered row/pair readback completion.

5. **R5-05 — No story AC owns successful FirstInstall terminalization.** Contract
   C-21 requires post-`commit-decided` KnownGood publication, ready admission,
   terminal commit, and their recovery cuts to be owned together
   (`epics.md:469-478`). Story 7.10 owns that installed-prior cut but explicitly
   excludes FirstInstall (`3850-3858`). Story 7.12 owns FirstInstall execution
   and absence recovery (`3884-3898`), yet both ACs cover only failed forward
   execution restoring declared absence (`3900-3905`). No Story 7.12 criterion
   accepts the successful FirstInstall path through KnownGood publication,
   generation-1 ready admission, and terminal `committed`, even though the
   architecture's exact successful path requires those effects. A successful
   FirstInstall can therefore reach `commit-decided` without an assignable AC
   owner for the required terminal cut. Add the success authority to the
   FirstInstall owner without moving installed-prior ownership backward.

## Passing Evidence

- Digest, story inventory, required-section inventory, AC count, declared
  dependency grammar, declared ordering, and declared acyclicity pass.
- The normative registry's inventory count, AD-11 count, unique IDs, owner
  existence, coverage inverse, and AD-11 owner reciprocity pass.
- R4-03, R4-04, R4-05, and R4-08 are closed as detailed above.
- Story 7.9 no longer consumes the FirstInstall-through-committed takeover
  corpus; its installed-prior pre-decision ownership is internally consistent.
- `python3 tests/validate_planning_quarantine.py` passes.
- `bash tests/validate_architecture_contracts.sh` passes after compatibility,
  planning discovery/quarantine, contract-oracle, release-oracle, and Host
  smoke validation.
- `bash tests/test_smoke.sh` passes independently.

## Dismissed Review Noise

Four candidate claims were rejected during triage:

1. `UD-EPIC-C-1` was not rejected solely because it lacks a second copy. The
   artifact records the exact post-source choice, and no canonical decision
   ledger is required by the input contracts.
2. The install/upgrade confirmation tokens were not required to encode every
   immutable plan field. Contract C-19 requires confirmation in the active plan
   context but does not require a cryptographic plan identifier in the token.
3. Broad requirement mappings on end-to-end gate stories were not treated as
   ownership theft; their boundaries explicitly invoke prior story gates rather
   than re-owning those implementations.
4. Stale `remediationBatch: batch-2` metadata is inaccurate but does not change
   story behavior, acceptance authority, or dependency reachability in this
   review scope.

## Final Gate

**FAIL. Finding count: 5. PASS threshold: 0.**

