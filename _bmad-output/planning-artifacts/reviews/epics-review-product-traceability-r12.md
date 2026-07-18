---
project: srvls
review_date: 2026-07-17
review_type: independent-product-traceability-r12
target_commit: 0e036d063dc34e5f615d3428326b76cc20b62a5b
target_path: _bmad-output/planning-artifacts/epics.md
actual_sha256: a486aefe99151fad1b031a04ee6ee5803cf9797f5ad09c6b0af069e2d7a1e6dd
digest_gate: PASS
verdict: FAIL
findingCount: 3
completionStatus: complete
---

# Epic Product Traceability Review R12

## Verdict

**FAIL — 3 findings. PASS requires zero.**

The settled backlog retains complete reciprocal inventory coverage for all 43
FR, 16 NFR, 6 UJ, 89 canonical UX IDs, and AD-1 through AD-25. Its 75 Stories
and 150 criterion-bound registry rows remain coherent, and the product journey
criteria preserve the PRD/UX consequences previously closed. The final C-23
and workflow seam is not implementation-ready: the dev-story instruction file
is not well-formed XML, the claimed reviewer/fixture-author identity rule is
weaker than its contract text, and the regression suite does not test that
identity attack.

The artifact is correctly still `remediated-draft`, `assignable: false`, and
`implementationAuthority: false`.

## Scope and method

This review pinned commit `0e036d063dc34e5f615d3428326b76cc20b62a5b`
and SHA-256 `a486aefe...e6dd`. It independently read the canonical PRD/addendum,
DESIGN and EXPERIENCE corpora, complete epic/story artifact, acceptance
registry, approval validator/regression suite, and create-story, dev-story,
and sprint-planning transition instructions. It replayed the aggregate checks,
parsed both XML workflows with Python's standard XML parser, and inspected the
Git-role comparisons and executable regression mutations directly.

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
| create-story XML | well formed | parsed successfully | PASS |
| dev-story XML | well formed | mismatched tag at line 335 | **FAIL** |
| C-23 role identity | stable, distinct identities | committer emails only | **FAIL** |
| Identity regression | same-principal metadata mutation | absent | **FAIL** |

The following repository commands passed at the pinned digest:

- `python3 tests/validate_story_fixture_approvals.py`
- `python3 tests/validate_story_approval_regressions.py`
- `python3 tests/validate_planning_quarantine.py`
- `bash tests/validate_architecture_contracts.sh`

Their success does not close the findings below because none parses dev-story
as XML and the identity regression suite never constructs the disputed commit
metadata.

## Findings

### F-R12-P01 — The authoritative dev-story workflow is malformed XML

`_bmad/bmm/workflows/4-implementation/dev-story/instructions.xml:335` embeds
the literal token `<story-id>` inside an `<action>` text node. A standard
`xml.etree.ElementTree.parse` fails with `mismatched tag: line 335, column 216`.
Thus the workflow carrying the mandatory completion-provenance gate cannot be
reliably loaded by an XML workflow engine. The aggregate architecture command
still passes because it performs substring checks and never parses the file.

Escape the token as `&lt;story-id&gt;` (or remove angle brackets), add both
implementation workflow files to a deterministic XML parse check, and include
that check in the architecture aggregate.

### F-R12-P02 — C-23 role commits do not prove stable Git identities

Contract C-23 says the approval must descend from distinct fixture-author and
reviewer Git identities. The R11 acceptance condition also required the two
role commits to have internally consistent identity metadata. The current
validator compares only `%ce` for `fixtureAuthorCommit` and `reviewerCommit`,
then compares the approval commit `%ce` to the reviewer `%ce`. It still never
requires `%ae == %ce` for either declared role commit.

Accordingly, a role commit may claim one author while being committed by a
different principal, and the approval object contains no stable principal or
signature binding that resolves which identity is authoritative. Require
author/committer agreement for both evidence commits (and the approval commit,
if author identity is part of the role claim), or define and validate a stronger
signed principal scheme. Keep fixture-author and reviewer principals distinct.

### F-R12-P03 — The regression suite does not exercise the identity attack

`tests/validate_story_approval_regressions.py` now creates a useful hermetic
approval/completion chain, but its `commit` helper always assigns identical
author and committer metadata. It tests a false completion mutation only. It
never constructs (a) identical committers with distinct author labels or (b)
an author/committer mismatch on either role commit, so the exact R11 identity
acceptance condition remains unproved while the aggregate reports PASS.

Add executable negative mutations for both cases and assert rejection by the
real validator. The aggregate must fail if either mutation is accepted.

## Acceptance condition

R12 cannot pass until all three findings are remediated and a fresh independent
review of one new settled digest reports zero findings. Preserve the current
nonassignable, non-authoritative frontmatter until that gate is satisfied.
