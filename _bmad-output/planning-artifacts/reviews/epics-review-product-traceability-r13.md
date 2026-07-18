---
project: srvls
review_date: 2026-07-17
review_type: independent-product-traceability-r13
target_commit: a7f6e55918b036adf7db6f33191b4f7d2f6333f4
target_path: _bmad-output/planning-artifacts/epics.md
actual_sha256: 872e3542d20c413344f9fb9acde74a8f1cac3cdff73ef32aa3762692b5bdf64f
digest_gate: PASS
verdict: FAIL
findingCount: 1
completionStatus: complete
---

# Epic Product Traceability Review R13

## Verdict

**FAIL — 1 finding. PASS requires zero.**

The settled backlog retains complete reciprocal coverage for all 43 FR, 16
NFR, 6 UJ, 89 canonical UX IDs, and AD-1 through AD-25. The 75 Stories and 150
criterion-bound acceptance rows remain coherent. The PRD journeys and UX
consequences remain represented in executable Story criteria, and the R12 XML
and author/committer-consistency defects are corrected. One required C-23
identity regression remains absent, so the aggregate evidence does not yet
prove the complete identity policy it claims.

The artifact correctly remains `remediated-draft`, `assignable: false`, and
`implementationAuthority: false`.

## Scope and method

This review pinned commit `a7f6e55918b036adf7db6f33191b4f7d2f6333f4`
and SHA-256 `872e3542...bdf64f`. It independently inspected the canonical PRD,
DESIGN and EXPERIENCE corpora, complete epic/story artifact, acceptance
registry, approval/completion validator, executable regression suite, and all
three implementation workflow surfaces. It replayed the aggregate validators
and parsed both XML instruction files with Python's standard XML parser.

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
| create-story / dev-story XML | well formed | both parsed | PASS |
| C-23 role validation | distinct consistent principals | enforced | PASS |
| C-23 identity regressions | both known attacks rejected | one of two exercised | **FAIL** |

The following repository commands passed at the pinned digest:

- `python3 tests/validate_story_fixture_approvals.py`
- `python3 tests/validate_story_approval_regressions.py`
- `python3 tests/validate_planning_quarantine.py`
- `bash tests/validate_architecture_contracts.sh`

## Finding

### F-R13-P01 — The same-principal identity attack still has no executable regression

R12 required two distinct identity mutations: an author/committer mismatch on
a role commit, and identical committers hidden behind distinct author labels.
`tests/validate_story_approval_regressions.py:134-148` adds only the first. It
constructs one commit whose author is `spoof@example.test` and committer is
`fixture@example.test`, then calls `principal_email()` directly. It never
constructs fixture-author and reviewer commits with different author labels
but the same committer principal and never drives that pair through the public
approval validator.

The production check in `validate_story_fixture_approvals.py` appears to reject
the omitted case, but C-23 makes this security boundary executable acceptance
evidence, not an inspection-only claim. A later refactor could remove or weaken
the distinct-principal set check while the aggregate regression continued to
report PASS.

Add a hermetic negative approval whose fixture-author and reviewer commits
have distinct, internally consistent displayed identities only if the chosen
principal model permits that construction, or more directly two role commits
that resolve to the same validated principal. Invoke the public assignment
validation path and assert rejection. Retain the existing author/committer
mismatch mutation and the positive distinct-principal chain.

## Acceptance condition

R13 cannot pass until the same-principal role attack is covered by an
executable negative regression through the real assignment validator and a
fresh independent review of one new settled digest reports zero findings.
Preserve nonassignable, non-authoritative frontmatter until that gate passes.
