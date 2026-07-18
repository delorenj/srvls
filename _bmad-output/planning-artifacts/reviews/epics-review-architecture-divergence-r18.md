---
reviewType: implementation-architecture-divergence
round: 18
targetCommit: 4eefc21ff6f56b04aae9463a98b79cefca58938f
targetArtifact: _bmad-output/planning-artifacts/epics.md
artifactSha256: dbd4b4e95a1bc0f272d959ef9587078d2220d7e19134c7b183fa8acf8f6c7059
verdict: FAIL
findingCount: 3
reviewedAt: 2026-07-17
---

# R18 Implementation / Architecture Divergence Review

## Verdict

**FAIL — 3 blocking findings.** The aggregate architecture, compatibility,
release, quarantine, registry, approval, and mutation commands return zero, and
the canonical backlog continues to inventory AD-1 through AD-25,
ARCH-LIM-1 through ARCH-LIM-24, and 87 AD-11 rows. The R18 change improves the
completion replay from one file to a bounded multi-file directory and adds a
partial plural-reference check. Neither change closes its R17 trust boundary:
the mutation suite remains materially unchanged, non-participating changes can
still authorize completion, and Story-reference parsing remains match-only.

## Frozen review basis

- Settled commit: `4eefc21ff6f56b04aae9463a98b79cefca58938f`
- Canonical artifact SHA-256:
  `dbd4b4e95a1bc0f272d959ef9587078d2220d7e19134c7b183fa8acf8f6c7059`
- Acceptance-registry SHA-256:
  `aefb83471a6f951c2e39046c73a69b20460baa2c012c6b474a1802ca70e46c08`
- Approval validator SHA-256:
  `d8fa346938a165f94b8e650e9a4b59147b2b845112021bfa2b38e20f8bb4ced6`
- Mutation validator SHA-256:
  `9f530a1c9628316e4328f44d860c4d8b8b92e060d0410689aa9c6ac8ee918957`
- Architecture authority: final `ARCHITECTURE-SPINE.md`, AD-1 through AD-25,
  fixed contract corpora, limits, acceptance matrices, release/FD3/FD4
  authorities, and C-23's fail-closed transition boundary.

This was an independent read-only audit. Only this report was written.

## Read-only validation record

| Check | Result |
|---|---|
| `git rev-parse HEAD` | PASS — exact settled commit |
| `bash tests/validate_architecture_contracts.sh` | PASS as implemented |
| `python3 tests/validate_planning_quarantine.py` | PASS — 2 exact globs, one canonical artifact, one byte-exact retired archive |
| `python3 tests/validate_story_fixture_approvals.py` | PASS — 75 Stories / 150 criterion-bound rows |
| `python3 tests/validate_story_approval_regressions.py` | PASS as implemented, but incomplete; R18-ARCH-01 through R18-ARCH-03 |
| Frozen compatibility replay | PASS — 90 inherited plus 4 approved deviations |
| Release oracle validation | PASS — complete reported crash/rollback/FD4/toolchain mutation inventory |
| Multi-file sandbox replay | PASS for its single positive control; vulnerable to non-participating manifest changes |
| AD inventory | PASS — AD-1..25 represented |
| Limit inventory | PASS — ARCH-LIM-1..24 represented |
| Story-reference integrity | FAIL — accepted prefixes and ignored malformed singular forms remain |

## Findings

### R18-ARCH-01 — The required isolated mutation matrix is still absent

**Severity: blocking**

`validate_story_approval_regressions.py` was adapted mechanically to the new
`implementationFiles` shape, but it still exercises the same small set of
mutations and ends with the unqualified text `story approval regression
mutations: PASS`. It does not print a mutation count or names. It still lacks
isolated cases for runner path/order, fixture and expectation path/bytes/hash,
result hash/order/cardinality, symlink and dirty/untracked evidence, unknown
keys at every schema level, row/criterion order and hashes, forged ancestry,
divergent predecessor history, or the malformed/unresolved reference classes.
The implemented test therefore cannot substantiate the security and reference
matrix claimed by the aggregate PASS.

**Required closure:** create a named table-driven inventory from a valid
hermetic chain; change exactly one invariant per case; invoke the public CLI or
aggregate entry point; assert the specific rejection; and print the executed
count and complete names. The inventory must include every C-23 trust-boundary
class and every accepted Story-reference grammar rejection class.

### R18-ARCH-02 — Multi-file replay still permits changed-but-nonparticipating completion

**Severity: blocking**

`validate_completion()` sets one aggregate `changed` flag when *any* manifest
file differs between approval and implementation commits. The runner receives
the entire reconstructed manifest directory, but the validator neither records
nor proves which files the runner consumed. A completion can therefore retain
the previously approved behavior-bearing file unchanged, add or alter an
unrelated manifest file, obtain the already-approved expected output, and pass
the `changed` gate. The new positive control has one file and the regression
suite only corrupts its claimed hash, so this bypass is not tested.

This is exactly the changed-but-nonparticipating implementation substitution
called out in R17. Replacing one file with a directory changes transport, not
the proof that implementation behavior participated in the result.

**Required closure:** bind the approved runner contract to an exact declared
input manifest and prove a behavior-bearing change participates in replay (or
use a comparison oracle that distinguishes approved from implemented trees).
Add a negative control with an unchanged behavior file plus a changed unrelated
file and otherwise unchanged oracle evidence; the public completion CLI must
reject it.

### R18-ARCH-03 — Story-reference validation still accepts prefixes and ignores unsupported syntax

**Severity: blocking**

The new plural check uses `re.match(r"Stories ... through ...", mention)`
rather than complete consumption. Thus `Stories 5.1 through 5.9 and 99.99`, or
any other trailing text, is accepted by the grammar check while the range loop
validates only its prefix. Singular discovery remains
`re.findall(r"Story (\d+\.\d+)", epics)`, so malformed singular tokens that do
not match that pattern are ignored rather than rejected. The implementation
also does not enforce exactly-once resolution of every reference token against
the ordered Story-heading registry, and no reference mutation cases were
added.

**Required closure:** tokenize every `Story`/`Stories` occurrence outside the
normative registry, fully consume one documented grammar, expand accepted
lists/ranges, and resolve every token exactly once against the ordered 75-Story
registry. Reject trailing text, malformed singular/plural forms, unsupported
lists, cross-Epic and descending ranges, duplicates, and out-of-range IDs.
Prove each class with an isolated public-gate mutation.

## Final status

The frozen target is not eligible for final/current promotion. Remediate all
three findings, settle a new digest, and rerun all three independent review
lanes.
