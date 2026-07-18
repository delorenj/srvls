---
project: srvls
review_date: 2026-07-17
review_type: independent-product-traceability-r11
target_commit: 01e535cdbbcccccc3019e9a5fc6a26780a64b4c2
target_path: _bmad-output/planning-artifacts/epics.md
actual_sha256: a486aefe99151fad1b031a04ee6ee5803cf9797f5ad09c6b0af069e2d7a1e6dd
digest_gate: PASS
verdict: FAIL
findingCount: 1
completionStatus: complete
---

# Epic Product Traceability Review R11

## Verdict

**FAIL — 1 finding. PASS requires zero.**

The settled backlog retains complete reciprocal inventory coverage for all 43
FR, 16 NFR, 6 UJ, 89 canonical UX IDs, and AD-1 through AD-25. The story
acceptance registry binds all 150 numbered criteria, the seven user-value epics
and 75 dependency-ordered stories remain discoverable only at the canonical
path, and the approval gate now correctly checks the approval commit's
committer rather than only its author. One independently exploitable identity
gap remains: the same committer can still author the fixtures and commit their
approval while supplying different author metadata on the two declared
evidence commits.

The artifact is correctly still `remediated-draft`, `assignable: false`, and
`implementationAuthority: false`.

## Scope and method

This review pinned commit `01e535cdbbcccccc3019e9a5fc6a26780a64b4c2`
and SHA-256 `a486aefe...e6dd`. It read the canonical PRD and addendum, DESIGN and
EXPERIENCE corpora, the complete epic/story artifact, normative acceptance
registry, approval validator and regression suite, and the create-story,
dev-story, and sprint-planning transition instructions. It replayed the R10
identity finding against both Git author and committer metadata and checked
that the prior journey, UX, source-inventory, dependency, immutable-fixture,
and fail-closed workflow remediations remain intact.

## Coverage and executable evidence

| Surface | Expected | Observed | Result |
| --- | ---: | ---: | --- |
| Epics / stories | 7 / 75 | 7 / 75 | PASS |
| Acceptance rows | 150 | 150 exact IDs and criterion hashes | PASS |
| Functional requirements | 43 | 43 reciprocal IDs | PASS |
| Non-functional requirements | 16 | 16 reciprocal IDs | PASS |
| User journeys | 6 | 6 reciprocal IDs | PASS |
| Canonical UX IDs | 89 | 89 reciprocal IDs | PASS |
| Architecture decisions | AD-1..AD-25 | complete | PASS |
| AD-11 acceptance rows | 87 | 87 unique owning rows | PASS |
| Approval committer is declared reviewer | required | approval/reviewer committer emails compared | PASS |
| Reviewer is not fixture author | required | author labels only; committers may be identical | **FAIL** |

The following commands passed at the pinned digest:

- `python3 tests/validate_planning_quarantine.py`
- `python3 tests/validate_story_fixture_approvals.py`
- `bash tests/validate_architecture_contracts.sh`

The aggregate approval command intentionally validates registry structure, not
a future per-story approval object, so its success does not exercise or close
the identity finding below.

## Finding

### F-R11-P01 — One committer can still be both fixture author and reviewer

Contract C-23 requires the approval reviewer not to be the fixture author and
requires the approval to descend from distinct fixture-author and reviewer Git
identities (`epics.md:503-520`). The validator establishes distinctness only by
comparing `%ae`, the author emails of `reviewerCommit` and
`fixtureAuthorCommit` (`validate_story_fixture_approvals.py:165-166`). It then
checks that the approval commit's `%ce` equals the reviewer commit's `%ce`
(`validate_story_fixture_approvals.py:167-168`), but never checks the committer
of `fixtureAuthorCommit`.

Consequently one principal can commit the fixture bytes with author metadata
`fixture-author@example`, create `reviewerCommit` with author metadata
`reviewer@example`, and commit the approval; all three commits can carry the
same committer email. The author-email distinctness and approval-committer
comparison both pass even though the person who committed the fixtures also
committed their approval. The current regression suite checks command wiring
and missing artifacts but has no mutation for this same-committer/different-
author case (`validate_story_approval_regressions.py:32-50`).

Require the fixture-author evidence commit to have a stable, internally
consistent identity and require its committer identity to differ from the
approval/reviewer committer identity. At minimum, compare `%ce` for
`fixtureAuthorCommit` against `%ce` for both `reviewerCommit` and the derived
approval commit, and reject author/committer identity disagreement for the two
role commits. Add an executable Git-history mutation proving that identical
committers with distinct `%ae` labels fail closed.

## Acceptance condition

R11 cannot pass until F-R11-P01 is remediated and a fresh independent review of
one new settled digest reports zero findings. Keep the artifact nonassignable
and non-authoritative until that review passes.
