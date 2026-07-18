---
reviewType: implementation-architecture-divergence
round: 16
targetCommit: 630498ad05e566a4c858c17f1a643e71575930d5
targetArtifact: _bmad-output/planning-artifacts/epics.md
artifactSha256: 8b9d3f4b731fca03f2ac8cbaa13d95fe00c4609aef9424ff2747aec66a8ffb17
verdict: FAIL
findingCount: 3
reviewedAt: 2026-07-17
---

# R16 Implementation / Architecture Divergence Review

## Verdict

**FAIL — 3 blocking findings.** The frozen compatibility, contract, release,
planning-quarantine, registry, mutation, and aggregate commands return zero,
and the canonical backlog retains AD-1 through AD-25 and ARCH-LIM-1 through
ARCH-LIM-24 coverage. The new code improves isolation of fixture-author bytes,
but it still does not execute the implementation bound by the completion, the
public mutation suite remains far short of its required trust-boundary matrix,
and Story-range references remain outside the integrity gate.

## Frozen review basis

- Settled commit: `630498ad05e566a4c858c17f1a643e71575930d5`
- Canonical artifact SHA-256:
  `8b9d3f4b731fca03f2ac8cbaa13d95fe00c4609aef9424ff2747aec66a8ffb17`
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
| `python3 tests/validate_story_approval_regressions.py` | PASS as implemented, but incomplete; R16-ARCH-02 |
| `bash tests/compat/validate.sh` | PASS — 90 inherited plus 4 approved deviations |
| Contract/release oracle replay | PASS as reported by the aggregate gate |
| AD inventory | PASS — AD-1..25 represented |
| Limit inventory | PASS — ARCH-LIM-1..24 represented |
| Bound implementation oracle execution | FAIL — R16-ARCH-01 |
| Story-reference integrity | FAIL — range syntax is not parsed; R16-ARCH-03 |

## Findings

### R16-ARCH-01 — Replay is isolated but never executes the bound implementation

**Severity: blocking**

`validate_completion()` now copies the runner and fixture from
`fixtureAuthorCommit` into a temporary directory, applies a ten-second timeout,
and supplies a small environment. It does not materialize any bytes from
`implementationCommit` and does not pass an implementation artifact to the
runner (`tests/validate_story_fixture_approvals.py:250-263`). The only use of
`implementationCommit` after ancestry checks is to prove that a precomputed
`resultPath` blob with the expected hash exists in that commit. Consequently an
implementation can commit the approved expected bytes without its behavior
ever being invoked. The regression positive control demonstrates the flaw: its
fixture-author runner converts `input` to `expected`, while the implementation
is merely a file containing `done`; the gate passes although the implementation
does not produce or participate in the result.

This does not satisfy C-23's completion claim or the prior required closure to
execute in a clean tree bound to `implementationCommit` with exact argv.

**Required closure:** materialize an immutable clean archive/worktree for the
exact `implementationCommit`; bind and pass a declared implementation entry
point/artifact to every approved runner using an exact versioned argv contract;
execute only those commit bytes under the bounded environment; and attest the
fresh output. The positive control must fail when implementation behavior is
changed while fixture, runner, expected bytes, and claimed result are retained.

### R16-ARCH-02 — The public mutation gate still omits the required security matrix

**Severity: blocking**

`tests/validate_story_approval_regressions.py` exercises a valid chain plus
same-principal, result-path escape, nonzero claimed exit, zero-change
implementation, and author/committer mismatch cases. It still has no explicit
mutations for runner path/hash/substitution/reordering, fixture or expected
bytes/hash substitution, result hash/reordering/cardinality, copied
expectation without implementation execution, symlink escape, dirty/untracked
approval or bound files, unknown approval/completion keys, criterion
order/hash changes, forged ancestry, or a predecessor completion on divergent
history. Several parser-only checks run against the real repository rather than
isolated mutations. The aggregate can therefore print `story approval
regression mutations: PASS` without proving most of the previously required
fail-closed invariants.

**Required closure:** implement the complete isolated mutation table. Each
case must begin from a valid hermetic chain, mutate exactly one invariant, run
the public CLI/aggregate path, and assert rejection for that invariant. Include
a two-oracle control whose result depends on the exact implementation bytes and
a divergent-predecessor history case.

### R16-ARCH-03 — Story-range references still bypass canonical integrity validation

**Severity: blocking**

The new dangling-reference check uses only `re.findall(r"Story
(\d+\.\d+)", epics)`. It neither recognizes plural `Stories` nor expands range
syntax. The canonical artifact currently contains `Stories 3.11 through 5.9`
and `Stories 2.1 through 2.6 and 6.1 through 6.12`; none of those endpoints or
intermediate references is validated by this check. It also accepts duplicate
Story headings because the registry test compares sets. Thus the R15-required
gate for every Story ID/range in boundaries, dependencies, validation text,
and acceptance criteria remains incomplete, and no unresolved-range mutation
exists in the regression suite.

**Required closure:** parse singular and plural Story references plus every
allowed list/range grammar, expand ranges within their epic, require each
reference and endpoint to resolve exactly once to the ordered 75-Story
registry, reject malformed/cross-epic/descending/out-of-range syntax, reject
duplicate headings, and add isolated mutations for unresolved simple and range
references.

## Final status

The frozen target is not eligible for final/current promotion. Remediate all
three findings, settle a new digest, and rerun all three independent review
lanes.
