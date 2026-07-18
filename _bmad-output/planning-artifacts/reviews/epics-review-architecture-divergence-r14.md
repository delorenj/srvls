---
reviewType: implementation-architecture-divergence
round: 14
targetCommit: 761b9e2385e0c0b967cda93a132d126c32c716d1
targetArtifact: _bmad-output/planning-artifacts/epics.md
artifactSha256: 13eb5926f0b2356bbe6730cfe4050b2dfc2b2addd95a83402db926834a67796f
verdict: FAIL
findingCount: 3
reviewedAt: 2026-07-17
---

# R14 Implementation / Architecture Divergence Review

## Verdict

**FAIL — 3 blocking findings.** The compatibility, contract, release,
planning-quarantine, acceptance-registry, approval-regression, and aggregate
commands all return zero at the frozen target. AD-1 through AD-25,
ARCH-LIM-1 through ARCH-LIM-24, and all 87 enumerated AD-11 rows remain present.
The completion envelope still accepts invented oracle output without executing
an oracle, its mutation gate treats that invented output as the positive
control and leaves most of the trust boundary untested, and Story 6.13 names
two nonexistent predecessor Stories.

## Frozen review basis

- Settled commit: `761b9e2385e0c0b967cda93a132d126c32c716d1`
- Canonical artifact SHA-256:
  `13eb5926f0b2356bbe6730cfe4050b2dfc2b2addd95a83402db926834a67796f`
- Acceptance-registry SHA-256:
  `aefb83471a6f951c2e39046c73a69b20460baa2c012c6b474a1802ca70e46c08`
- Architecture authority: final `ARCHITECTURE-SPINE.md`, AD-1 through AD-25,
  its fixed contract corpora, limits, acceptance matrices, and release/FD3/FD4
  authorities.

This was an independent read-only audit. Only this report was written.

## Read-only validation record

| Check | Result |
|---|---|
| `git rev-parse HEAD` | PASS — exact settled commit |
| `bash tests/validate_architecture_contracts.sh` | PASS as implemented |
| `python3 tests/validate_planning_quarantine.py` | PASS — exact canonical discovery and retired quarantine |
| `python3 tests/validate_story_fixture_approvals.py` | PASS — 75 stories / 150 criterion-bound rows |
| `python3 tests/validate_story_approval_regressions.py` | PASS as implemented, but incomplete; R14-ARCH-02 |
| `bash tests/compat/validate.sh` | PASS — 90 inherited plus 4 approved deviations |
| Contract/release oracle replay | PASS — fixed contract and release corpora report green |
| AD/limit inventory | PASS — AD-1..25 and ARCH-LIM-1..24 |
| AD-11 inventory | PASS — 87 unique rows, 14 current and 73 future |
| Executed-oracle attestation | FAIL — no oracle is executed or externally attested |
| Dependency integrity | FAIL — Story 6.13 consumes nonexistent Stories 2.7 and 2.8 |

## Findings

### R14-ARCH-01 — Fresh result files are still not executed-oracle evidence

**Severity: blocking**

`validate_completion()` checks a declared runner's bytes, a claimed zero exit
code, and a fresh result file whose bytes equal the approved expectation
(`tests/validate_story_fixture_approvals.py:225-239`). It never invokes that
runner, checks out and runs the implementation commit, or verifies a signed CI
attestation that binds command, environment, start/end identity, exit status,
and output. The hermetic “valid” chain demonstrates the bypass: it writes
`actual` files containing `expected`, records `exitCode: 0`, and passes without
ever executing either file named `runner`
(`tests/validate_story_approval_regressions.py:115-129`). A fabricated fresh
copy now avoids the prior alias check but remains indistinguishable from an
executed oracle. Consequently AD-11 future rows and C-23 completion can be
declared complete without implementation acceptance having run.

**Required closure:** execute every ordered approved runner in a clean checkout
of the bound implementation commit, or validate an equivalently tamper-evident
external execution attestation. Bind the exact commit/tree, runner and argv,
controlled environment, criterion/fixture hashes, exit status, and separately
generated result bytes. Prove copied expectations and claimed-but-unexecuted
zero exits fail.

### R14-ARCH-02 — The mutation gate still omits most completion and ancestry attacks

**Severity: blocking**

The hermetic gate exercises only same-principal approval, an escaped result
path, `implementationCommit == approvalCommit`, and author/committer mismatch
(`tests/validate_story_approval_regressions.py:133-177`). It has no public-gate
mutations for nonzero/fabricated exit truth, runner path/hash/reordering,
result hash/reordering/cardinality, copied expectation bytes, symlink escape,
dirty/untracked fixture or approval state, approval/completion unknown keys,
criterion order/hash, fixture/expected mutation, forged commit ancestry, or a
predecessor completion on a divergent history. Several static helper checks do
not exercise the serialized public validator. The aggregate therefore reports
“story approval regression mutations: PASS” while its positive control itself
is the unexecuted-output bypass in R14-ARCH-01.

**Required closure:** add isolated hermetic public-command mutations for every
security-relevant approval, completion, runner/result, cleanliness,
immutability, identity, and ancestry invariant. Include a real two-oracle
execution positive control and divergent-predecessor negative control.

### R14-ARCH-03 — Story 6.13 consumes nonexistent Stories 2.7 and 2.8

**Severity: blocking**

Epic 2 ends at Story 2.6, but Story 6.13's implementation boundary says it
integrates “Stories 2.1 through 2.8” (`epics.md:4618`). Its dependency field
lists only Story 6.12 (`epics.md:4622`), so the dependency parser and assignment
gate cannot detect or enforce the two invalid references. This is not an
independently implementable dependency boundary and permits the UJ-2 lifecycle
journey to be assigned without a machine-enforced completion edge to its real
Agent predecessors.

**Required closure:** replace the invalid range with the exact existing Story
IDs and declare every direct cross-epic predecessor in `Dependencies` so C-23's
completion-before-dependent-approval rule enforces them. Add a registry check
that every Story reference in boundaries, validation text, and dependencies
resolves to exactly one canonical Story.

## Final status

The frozen target is not eligible for final/current promotion. Remediate all
three findings, settle a new digest, and rerun all three independent review
lanes.
