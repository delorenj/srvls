---
project: srvls
review_date: 2026-07-17
review_type: independent-product-traceability-r9
target_commit: 849e1a5952b31f32a96eccbc2851909a30982542
target_path: _bmad-output/planning-artifacts/epics.md
actual_sha256: 6fc43377b3ba19fc6ee656fa6e4e00e3366f41a4ee244ee86ab0125e195a4f53
digest_gate: PASS
verdict: FAIL
findingCount: 6
completionStatus: complete
---

# Epic Product Traceability Review R9

## Verdict

**FAIL — 6 findings. PASS requires zero.**

The canonical inventory and reciprocal traceability remain mechanically
complete: 43 FR, 16 NFR, 6 UJ, all 89 canonical UX IDs, AD-1 through AD-25,
75 stories, 150 acceptance rows, and 87 AD-11 rows are present. The settled
artifact also closes the previously missing UJ-2 action-path edge. All
repository aggregate validators pass.

The remaining defects are in the executable C-23 assignment contract. Four
stories cannot produce an approval that satisfies the validator, reviewer
authorship is not bound to the approval commit, predecessor completion is only
shallowly checked, predecessor implementation ordering is not enforced, the
no-recapture rule is not proved, and sprint-status regeneration preserves
advanced states after C-23 failure. These are product traceability defects
because C-23 is the mechanism that turns future story fixtures into independent
acceptance evidence.

## Scope and method

This review pinned commit `849e1a5952b31f32a96eccbc2851909a30982542` and
SHA-256 `6fc43377...f53`, read the canonical PRD/addendum, both canonical UX
documents, the complete epic/story artifact, C-23, its registry and validator,
and the create-story, dev-story, and sprint-planning workflows. It replayed the
source inventories through the normative registry and story mappings, inspected
the complete action journey added for UJ-2, and adversarially followed approval,
completion, dependency, and status-transition paths.

## Mechanical and executable evidence

| Surface | Expected | Observed | Result |
| --- | ---: | ---: | --- |
| Epics / stories | 7 / 75 | 7 / 75 | PASS |
| Numbered acceptance rows | 150 | 150 exact IDs and hashes | PASS |
| FR / NFR / UJ | 43 / 16 / 6 | complete reciprocal inventories | PASS |
| Canonical UX IDs | 89 | 83 core + 5 A11Y + SR-A11Y-1 | PASS |
| Architecture decisions | AD-1..AD-25 | complete | PASS |
| AD-11 rows | 87 | 87 unique rows | PASS |
| Story approval/assignment behavior | fail closed | 6 defects | **FAIL** |

The following commands passed at the pinned digest:

- `python3 tests/validate_story_fixture_approvals.py` — 75 stories and 150
  registry rows (discovery mode only).
- `bash tests/validate_architecture_contracts.sh` — compatibility, contract,
  release, Host-smoke, and approval-registry aggregates.
- `python3 tests/validate_planning_quarantine.py` — exact canonical discovery
  and retired-artifact quarantine.

## Findings

### F-R9-P01 — Four declared oracle strings are impossible approval paths

`declared_oracle()` captures every character through the next semicolon and
then requires both approval paths to equal or be descendants of that captured
string (`tests/validate_story_fixture_approvals.py:101-110,132-140`). Story 1.1
therefore requires a filesystem path beginning
`tests/architecture_boundaries.rs and cargo test ...`; Story 1.2 requires one
beginning `tests/compat/manifest.json and tests/compat/SHA256SUMS`; Stories 4.10
and 6.12 include `with assertion ...` in the required path
(`epics.md:3247,3270,4086,4597`). No regular file can simultaneously be the
declared conjunction or directory-plus-assertion, so these four stories can
never pass C-23 and can never be assigned. Give every story one unambiguous
oracle root/path, or encode an explicit ordered list/assertion field that the
validator understands.

### F-R9-P02 — The reviewer is not proved to be the approval committer

C-23 says a reviewer distinct from the fixture author must commit the approval
(`epics.md:508-517`). The validator compares the authors of `reviewerCommit`
and `fixtureAuthorCommit`, and proves both are ancestors of `approval_commit`,
but never compares the author/committer of `approval_commit` with the reviewer
identity (`tests/validate_story_fixture_approvals.py:145-157`). The fixture
author can commit the approval while naming any unrelated ancestor authored by
a second email as `reviewerCommit`. Bind the actual approval commit identity to
the reviewer evidence (or use a verifiable signed-review object).

### F-R9-P03 — A dependent story does not fully validate predecessor approval

C-23 requires every dependent story to consume a **fully validated** completion
object (`epics.md:518-521`). `validate_assignment()` instead calls only
`validate_completion()` for each dependency (`tests/validate_story_fixture_approvals.py:158-159`).
That function does not validate the predecessor approval schema, story/row IDs,
criterion hashes, fixture/result hashes, oracle containment, author/reviewer
separation, or fixture-author bytes (`tests/validate_story_fixture_approvals.py:163-178`).
A malformed predecessor approval plus a structurally valid completion object
can therefore authorize its successor. Reuse the complete predecessor approval
validation before accepting its completion proof.

### F-R9-P04 — Predecessor implementation is not ordered before successor assignment

`validate_completion()` returns the predecessor `implementationCommit`, but
the caller discards it (`tests/validate_story_fixture_approvals.py:158-160,178`).
There is no ancestry check from that implementation commit to the successor's
approval/assignment point. Consequently a predecessor implementation can
exist on an unrelated branch and still unlock the successor, contradicting
C-23's `ancestor implementation` requirement and the backlog's dependency
ordering. Require each predecessor implementation commit to be an ancestor of
the successor approval commit (and of the implementation start point).

### F-R9-P05 — The implementation may modify approved fixture bytes and later hide it

C-23 forbids recapturing or updating approved rows in the implementation change
(`epics.md:521-522`). Assignment validates only the current worktree bytes and
the fixture-author commit bytes (`tests/validate_story_fixture_approvals.py:137-157`),
while completion proves only approval-to-implementation ancestry
(`tests/validate_story_fixture_approvals.py:171-177`). It never compares the
approved fixture/result paths at the implementation commit, nor inspects the
approval-to-implementation diff. An implementation commit can alter/bless both
files and a later commit can restore them before a dependent is assigned.
Completion validation must prove the approved paths are byte-identical at the
implementation commit and absent from the implementation diff.

### F-R9-P06 — Sprint regeneration preserves advanced status after C-23 failure

Sprint planning says a failing approval check retains `backlog`
(`sprint-planning/instructions.md:82-87`), then immediately says an existing
more-advanced status is preserved and never downgraded (`:89-92`). Thus a
missing, invalidated, or tampered approval for an existing `ready-for-dev` or
`in-progress` story remains assignable/active after regeneration. This
contradicts the workflow's own fail-closed C-23 rule. On C-23 failure, quarantine
the story in a nonassignable status or halt with the invalid advanced state
unchanged but explicitly unusable; the generic no-downgrade rule cannot win.

## Acceptance condition

R9 cannot pass until all six findings are remediated and a fresh independent
review at one new settled digest reports zero findings. The artifact should
remain nonassignable and non-authoritative in the meantime.
