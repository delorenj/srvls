---
type: epic-story-review
reviewedCommit: 30ce86dab2e73b2cefb30b8ff7616797b873a232
reviewedArtifact: _bmad-output/planning-artifacts/epics.md
observedSha256: 8debf05b8fd24bc19a00dfc6ce56961050d56b97ea972613135616df4eaedbd4
verdict: FAIL
findingCount: 8
storyCount: 73
acceptanceCriterionCount: 146
declaredDependencyEdgeCount: 72
---

# R4 Story Quality and Dependency Review

## Verdict

**FAIL — 8 findings. PASS requires zero.**

The batch-3 revision closes six R3 findings and leaves seven R3 findings open
across six current findings. Two additional story-quality or ownership
defects remain in the reviewed artifact. The backlog is structurally complete,
but its acceptance authorities, precedence, and release-command ownership are
not deterministic enough for assignment. The artifact's own `assignable: false`
and `implementationAuthority: false` state is therefore correct.

## Digest

| Check | Result |
| --- | --- |
| Commit | `30ce86dab2e73b2cefb30b8ff7616797b873a232` |
| Commit subject | `fix(planning): close batch 3 semantic owner edges` |
| Artifact | `_bmad-output/planning-artifacts/epics.md` |
| Requested SHA-256 prefix | `8debf05b` |
| Observed SHA-256 | `8debf05b8fd24bc19a00dfc6ce56961050d56b97ea972613135616df4eaedbd4` |
| Digest disposition | Exact match |
| Git blob | `d3530ce3f08c045d3a726729f1e71d6b8c4d14e6` |
| Size | 3,940 lines; 203,141 bytes |

## Methods and Complete Accounting

1. Pinned the review to the requested digest and current commit, then reviewed
   the complete `c237a2a..30ce86d` artifact delta rather than accepting the
   remediation labels.
2. Parsed every Story heading and required section. The artifact has seven
   epics and 73 unique stories in counts `10,6,11,10,9,12,15`. Every story has
   one user-value statement, Implementation Boundary, Requirement Mapping,
   Dependencies, Validation Expectations, Out of Scope, and exactly two
   numbered Given/When/Then criteria: 146 ACs total.
3. Parsed the declared dependency graph. Story 1.1 alone declares `None`; every
   later story names exactly one existing earlier Story ID. The result is 72
   declared edges, no unresolved references, no forward edge, and no cycle.
4. Parsed the normative JSON registry and checked both coverage directions.
   `storyInventory` has 73 unique values; `ad11Rows` has 82 unique rows and
   agrees with `canonicalCounts.ad11Rows`; every `coverageByStory` edge has the
   reciprocal `requirementCoverage` edge; every AD-11 row owner maps AD-11.
5. Re-audited R3-01 through R3-13 individually against the current contracts,
   story boundaries, ACs, referenced fixture paths and contents, PRD, and
   architecture. This included parsing the first and last transaction in every
   release JSONL authority used by Stories 7.8-7.10.
6. Executed `python3 tests/validate_planning_quarantine.py` and
   `bash tests/validate_architecture_contracts.sh`. Both exit 1 at
   `planning-root tombstone does not fail closed`. Compatibility replay within
   the aggregate passes before that failure. No repository-provided epics
   registry validator exists, so the registry checks above were executed with
   an independent read-only parser. The standalone contract validator, release
   oracle validator, and legacy Host smoke all pass.

## R3 Finding Accounting

| R3 finding | R4 disposition | Evidence |
| --- | --- | --- |
| R3-01 | **Open** | R4-01. The wording changed, but 69 negative ACs still depend on an unspecified "named fixture corpus" and 55 positive ACs still invoke a generic positive scenario. |
| R3-02 | **Open** | R4-02. Story 1.10 still owns the red aggregate and its AC2 contradicts the authorized override. |
| R3-03 | **Open** | R4-03. The PRD's reject-or-retain alternative remains; the epics document tries to reverse canonical precedence. |
| R3-04 | **Open** | R4-03. The PRD's exact-excess-safe rule remains; the epics document tries to reverse canonical precedence. |
| R3-05 | Closed | Story 5.2 now says redirected output belongs only to Story 5.1 (`epics.md:3101`); its ACs contain no redirected-output ownership. |
| R3-06 | Closed | Story 6.12 now reciprocally owns the action portions of UX-RP-5 and UX-A11Y-1/2/5 (`epics.md:3554-3576`), while Stories 5.2/5.3/5.7 retain pre-action ownership. |
| R3-07 | Closed, with new naming defect | Story 7.4 now names `consumer-discovery-v1` and Story 7.6 owns `brownfield-consumer-pairs.json`; R4-07 covers the remaining forbidden-manifest wording. |
| R3-08 | **Open** | R4-05. Story 7.9's prose excludes FirstInstall and terminal commit, but AD11-FUT-49 still assigns it the FirstInstall-through-committed owner-takeover corpus. |
| R3-09 | **Open** | R4-06. Stories 7.8 and 7.10 claim installed-prior scope but their AC/registry authorities remain FirstInstall corpora that reach or approach terminal commit. |
| R3-10 | Closed | Stories 7.11 and 7.13 now consistently name revision-zero planning authorities in both Validation Expectations and AC1 (`epics.md:3834-3844`, `3882-3892`). |
| R3-11 | **Open** | R4-04. The verb list changed, but the per-verb argv/confirmation matrix remains undefined. |
| R3-12 | Closed | C-14 contains BQ-1 through BQ-8 and their row contract before C-15 begins (`epics.md:377-391`). |
| R3-13 | Closed | `canonicalCounts.ad11Rows` is 82 and the registry contains 82 unique rows; owner reciprocity also passes. |

## All-Story AC and Ownership Accounting

R4-01 applies to all stories except 2.1, 5.9, 6.7, and 7.3 because 69 stories
retain the generic negative-criterion template. Its positive-template defect
appears in 55 stories. Additional story-specific findings are exhaustive below;
`—` means no additional finding beyond R4-01 where applicable.

| Stories | Additional findings |
| --- | --- |
| 1.1-1.9 | — |
| 1.10 | R4-02 |
| 2.1-5.9 | — |
| 6.1 | — |
| 6.2 | R4-08 |
| 6.3-7.2 | — |
| 7.3 | R4-04 |
| 7.4 | R4-07 |
| 7.5-7.7 | — |
| 7.8 | R4-06 |
| 7.9 | R4-05 |
| 7.10 | R4-06 |
| 7.11-7.15 | — |

R4-03 is authority-wide and directly affects Stories 2.3, 4.3, and 4.6; it is
not a defect in the declared 72-edge graph. R4-02 also reaches Story 7.15 because
that story names the same failing aggregate as its owning oracle
(`epics.md:3918-3940`).

## Findings

1. **R4-01 — The backlog-wide AC template still delegates acceptance truth to
   unspecified future corpora.** Sixty-nine negative ACs say only "the named
   fixture corpus containing the concrete scenario in this criterion" and
   return the same generic `contract_violation`/exit 4 result. Fifty-five
   positive ACs say a "named fixture's positive scenario" executes. The prose
   does not enumerate fixture row IDs, inputs, exact expected bytes, or
   criterion-specific result tokens. At the same time, all 73 Validation
   Expectations claim their expected bytes are already fixed independently of
   the implementation, although 60 named owning-oracle paths do not exist in
   the reviewed tree. Representative evidence is Story 1.1
   (`epics.md:2168-2190`), Story 2.3 (`2460-2482`), Story 5.1 (`3071-3093`),
   Story 6.12 (`3554-3576`), and Story 7.15 (`3918-3940`). An implementer can
   author the missing corpus to match the implementation and satisfy these ACs,
   so R3-01's independent-oracle defect remains.

2. **R4-02 — Story 1.10's authorized path override is simultaneously its pass
   condition and a rejection condition.** The authority section says the
   planning-root replacement is user-directed, Story 1.10 owns the validator
   revision, and promotion requires canonical discovery plus archive quarantine
   (`epics.md:22-28`). Story 1.10's boundary likewise requires the
   "user-authorized planning-root discovery assertion" (`2390`). AC2 instead
   says that when "the user override is active" the capability fails closed
   (`2405-2406`). The live quarantine validator and aggregate both do exactly
   that today, exiting 1 at `planning-root tombstone does not fail closed`.
   Story 7.15 consumes the same aggregate while putting change of the override
   out of scope (`3930-3939`). No implementation can satisfy both acceptance
   branches without choosing which normative sentence to ignore.

3. **R4-03 — The artifact tries to close two higher-authority alternatives by
   silently reversing the canonical precedence chain.** The architecture says
   precedence is PRD, addendum, UX, then architecture, and a lower source may
   not replace a higher-source contract (`ARCHITECTURE-SPINE.md:59-63`). The PRD
   still permits persistent intent without Durable Ownership to be "rejected or
   retained as unmanaged" (`prd.md:227-234`) and still permits `safe` for an
   "exact excess instance" (`prd.md:446-452`). The epics document instead puts
   architecture and an undefined "user's seam-closure mission" before the PRD,
   then selects rejection and forbids excess-instance selection
   (`epics.md:30-36`). That lower artifact cannot make Stories 2.3, 4.3, and 4.6
   deterministic by declaring itself higher authority. R3-03 and R3-04 remain
   open until the higher sources are reconciled or a precise user decision is
   recorded in the canonical authority chain.

4. **R4-04 — Story 7.3 still has no closed per-verb release command matrix.** C-19
   allows `--transaction`, `--format`, and "verb-appropriate" `--artifact`, but
   never states which flags are required, optional, or forbidden for install,
   upgrade, validate, status, and rollback; it also says install and upgrade
   confirm without defining their confirmation grammar (`epics.md:433-443`).
   Story 7.3 delegates exact argv/result/exit/confirmation rows back to C-19 and
   to nonexistent `tests/fixtures/implementation/release-command-surface-v1`
   (`3630-3652`). Its AC2 closes only invalid arguments generally and rollback's
   token. The architecture owns the five verbs but supplies no missing argv
   matrix (`ARCHITECTURE-SPINE.md:1437-1445`). Two implementations can expose
   different legal install/upgrade/validate/status argv and confirmations while
   satisfying the written story. R3-11 is not closed.

5. **R4-05 — Story 7.9's normative owner-takeover authority still crosses both
   ownership boundaries that the story excludes.** Its boundary limits the
   story to installed-prior generic/pre-decision cuts and explicitly excludes
   KnownGood, ready admission, terminal commit, and FirstInstall
   (`epics.md:3774-3796`). The normative registry nevertheless assigns
   AD11-FUT-49 to Story 7.9 with
   `tests/fixtures/contracts/release-transaction-v1/owner-takeover.transitions.jsonl`
   (`1990-1996`). Direct parsing finds 35 rows: the first has intent `install`,
   `prior_release.kind=first-install-absent`, old generation 0, target generation
   1, and pending terminal; the last retains that FirstInstall authority and is
   `committed`. The new nonexistent Validation Expectations path does not
   supersede the normative AD-11 row. Story 7.9 still consumes Story 7.10's
   terminalization and Stories 7.11-7.12's FirstInstall ownership, so R3-08
   remains open and the semantic dependency graph is cyclic.

6. **R4-06 — Stories 7.8 and 7.10 still consume FirstInstall authorities before
   the stories that own FirstInstall.** Story 7.8 names an installed-prior
   Validation oracle and puts KnownGood publication out of scope
   (`epics.md:3750-3765`), but AC1 directly consumes `forward.transitions.jsonl`
   (`3767-3772`). Its 35 rows are entirely intent `install` with
   `prior_release.kind=first-install-absent`, old generation 0, and target
   generation 1; the final row is `committed`, beyond Story 7.8's stated
   `commit-decided` handoff. Story 7.10 excludes FirstInstall and names an
   installed-prior oracle (`3798-3813`), but AC1 and AD11-FUT-50 consume
   `known-good-publication-pending.manifest.json` (`1998-2004`, `3815-3820`),
   whose `prior_release.kind` is `first-install-absent`. Those authorities
   require FirstInstall planning/execution before Stories 7.11-7.12 provide it.
   R3-09 therefore remains open despite the narrowed story prose.

7. **R4-07 — Story 7.4 names a forbidden release authority as its user-owned
   artifact.** Contract C-21 says release authority consists only of ordered
   `ManagedConsumerUnitContractV1` rows, `BrownfieldConsumerPairsV1`, transaction
   consumers, and hashes, and explicitly forbids `ManagedConsumerManifestV1`
   (`epics.md:455-464`). Story 7.4 is nevertheless titled "Managed consumer
   manifest," asks for a "managed consumer manifest," and says "manifest
   readback" exists before preimages (`3654-3658`). Its Implementation Boundary
   correctly names the row/pair authorities (`3660`), leaving the story's value
   contract and implementation contract in disagreement. The renamed discovery
   oracle closes the old Story 7.4/7.6 path collision, but this wording still
   permits reintroduction of the forbidden aggregate type or makes the story's
   promised artifact impossible.

8. **R4-08 — Story 6.2 does not identify the interaction it owns.** Its boundary
   begins "Open a only for one exact Promise/Observation" (`epics.md:3320`). The
   missing noun is not cosmetic in an ownership-sensitive action story: it could
   mean Action Menu, modal, plan, or operation. The title suggests Action Menu,
   but AC1 says only that accelerators "enter the same plan path"
   (`3331-3336`). The boundary must explicitly name the Action Menu and its
   transition output so Story 6.2 cannot be implemented as plan creation owned
   by Story 6.3.

## Passing Evidence

- Digest, story inventory, required-section inventory, AC count, declared
  dependency grammar, dependency ordering, and acyclicity pass.
- The normative registry's counts, coverage inverse, AD-11 count, and AD-11
  owner reciprocity pass.
- R3-05 through R3-07, R3-10, and R3-12 through R3-13 are closed as detailed
  above.
- `tests/fixtures/contracts/validate.py`, the release oracle validator,
  `tests/compat/validate.sh` through the aggregate, and `tests/test_smoke.sh`
  pass. The aggregate then reaches the planning quarantine contradiction.

## Final Gate

**FAIL. Finding count: 8. PASS threshold: 0.**
