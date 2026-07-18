---
reviewType: implementation-architecture-divergence
round: 15
targetCommit: 5532c1460eda02d0fefdabdf94f6923cc2da9113
targetArtifact: _bmad-output/planning-artifacts/epics.md
artifactSha256: 4a7c3f749d74d25a40d873945256248caabe65608138ede773a7c290e58aee26
verdict: FAIL
findingCount: 3
reviewedAt: 2026-07-17
---

# R15 Implementation / Architecture Divergence Review

## Verdict

**FAIL — 3 blocking findings.** The frozen compatibility, contract, release,
planning-quarantine, registry, mutation, and aggregate gates return zero. The
canonical backlog still covers AD-1 through AD-25 and ARCH-LIM-1 through
ARCH-LIM-24, and the Story 6.13 prose now refers only to existing Stories.
However, the new replay executes mutable working-tree bytes rather than the
bound implementation, the public mutation suite still leaves the required
trust-boundary attacks untested, and the promised canonical Story-reference
integrity check was not implemented.

## Frozen review basis

- Settled commit: `5532c1460eda02d0fefdabdf94f6923cc2da9113`
- Canonical artifact SHA-256:
  `4a7c3f749d74d25a40d873945256248caabe65608138ede773a7c290e58aee26`
- Acceptance-registry SHA-256:
  `aefb83471a6f951c2e39046c73a69b20460baa2c012c6b474a1802ca70e46c08`
- Architecture authority: final `ARCHITECTURE-SPINE.md`, AD-1 through AD-25,
  fixed contract corpora, limits, acceptance matrices, and release/FD3/FD4
  authorities.

This was an independent read-only audit. Only this report was written.

## Read-only validation record

| Check | Result |
|---|---|
| `git rev-parse HEAD` | PASS — exact settled commit |
| `bash tests/validate_architecture_contracts.sh` | PASS as implemented |
| `python3 tests/validate_planning_quarantine.py` | PASS — 2 exact globs, one canonical artifact, one byte-exact retired archive |
| `python3 tests/validate_story_fixture_approvals.py` | PASS — 75 Stories / 150 criterion-bound rows |
| `python3 tests/validate_story_approval_regressions.py` | PASS as implemented, but incomplete; R15-ARCH-02 |
| `bash tests/compat/validate.sh` | PASS — 90 inherited plus 4 approved deviations |
| Contract/release oracle replay | PASS as reported by the aggregate gate |
| AD inventory | PASS — AD-1..25 are represented |
| Limit inventory | PASS — ARCH-LIM-1..24 |
| Story-reference scan | PASS for current bytes — 943 simple references, zero unresolved; no gate enforces this |
| Bound implementation replay | FAIL — R15-ARCH-01 |

## Findings

### R15-ARCH-01 — Completion replay executes mutable checkout bytes, not the bound implementation

**Severity: blocking**

`validate_completion()` verifies the runner hash only by reading
`fixtureAuthorCommit`, then executes `(ROOT / result["runnerPath"]).resolve()`
in the reviewer's current checkout (`tests/validate_story_fixture_approvals.py:232-241`).
It never checks that the executable working-tree bytes equal
`runnerSha256`, never checks out `implementationCommit`, and never constrains
the executed tree or environment to that commit. A later tracked change or an
uncommitted replacement at the same path therefore controls the replay while
the validator reports that the fixture-author runner ran. The replay also
reads the fixture from the mutable checkout. Commit/tree identity, controlled
environment, and exact argv remain unattested. This does not close R14-ARCH-01
or C-23's claim that completion is bound to independently approved oracle
bytes.

**Required closure:** materialize a clean temporary worktree/archive at the
bound `implementationCommit`, verify the runner and fixture bytes there against
their approved hashes, execute there with an explicit controlled environment
and exact argv, and bind the produced exit/stdout to the completion object.
Reject dirty/current-tree substitution and prove both runner and fixture
substitution fail.

### R15-ARCH-02 — The public mutation gate still omits the required trust-boundary matrix

**Severity: blocking**

The R15 change adds only a nonzero `exitCode` mutation. The hermetic gate still
does not exercise runner path/hash/substitution/reordering, fixture mutation,
expected-result mutation, result hash/reordering/cardinality, copied
expectation without execution, symlink escape, dirty/untracked approval or
fixture state, unknown approval/completion keys, criterion order/hash
mutation, forged ancestry, or a predecessor completion on divergent history.
Its positive control uses runners whose output is constant and unrelated to
the fixture or implementation, so it does not demonstrate implementation
behavior. The aggregate can still print `story approval regression mutations:
PASS` without testing most of the security-relevant invariants explicitly
required by the prior accepted finding.

**Required closure:** add isolated, hermetic, public-command mutations for the
complete approval/completion/runner/result/cleanliness/identity/ancestry
matrix. Use a real two-oracle positive control whose result depends on both the
approved fixture and implementation, plus a divergent-predecessor negative
control. Each mutation must fail for its intended invariant, not incidentally
at an earlier unrelated check.

### R15-ARCH-03 — Story-reference integrity remains an unaudited prose invariant

**Severity: blocking**

Story 6.13 now correctly says Stories 2.1 through 2.6 and declares Story 2.6
plus Story 6.12 as predecessors. A read-only scan finds no unresolved simple
`Story N.N` reference in the current artifact. But neither
`canonical_rows()` nor the aggregate gate validates Story references outside
the parsed `Dependencies` line; `declared_dependencies()` merely extracts
whatever numbers are present. Thus the exact regression that produced
nonexistent Stories 2.7 and 2.8 can recur in implementation boundaries,
validation expectations, acceptance criteria, or dependencies while all gates
remain green. The required closure from R14-ARCH-03 was explicitly a registry
check, not a one-time prose correction.

**Required closure:** make the canonical gate parse every Story ID/range in
boundaries, dependencies, validation text, and acceptance criteria; require
each endpoint/reference to resolve exactly once to the 75-Story registry;
reject malformed or out-of-range references; and add an unresolved-reference
mutation to the public regression suite.

## Final status

The frozen target is not eligible for final/current promotion. Remediate all
three findings, settle a new digest, and rerun all three independent review
lanes.
