---
reviewType: implementation-architecture-divergence
round: 17
targetCommit: b7e8bc6c619b824c75d951fef8a3ebe104512c6e
targetArtifact: _bmad-output/planning-artifacts/epics.md
artifactSha256: 27fac8a71121812a95de3a5746c2696b3a3ed625488d8ad0b589f783d838d5a9
verdict: FAIL
findingCount: 2
reviewedAt: 2026-07-17
---

# R17 Implementation / Architecture Divergence Review

## Verdict

**FAIL — 2 blocking findings.** The frozen compatibility, contract, release,
planning-quarantine, registry, mutation, and aggregate commands return zero.
The canonical backlog retains AD-1 through AD-25, ARCH-LIM-1 through
ARCH-LIM-24, and the 87 AD-11 rows. The R17 change now materializes the exact
implementation artifact, executes it through the approved runner with fixed
argv inside a bounded `bwrap` sandbox, and rejects duplicate Story headings.
However, the public mutation suite does not prove most of the security matrix
claimed by C-23, and the Story-reference gate still accepts unparsed malformed
or unsupported reference syntax.

## Frozen review basis

- Settled commit: `b7e8bc6c619b824c75d951fef8a3ebe104512c6e`
- Canonical artifact SHA-256:
  `27fac8a71121812a95de3a5746c2696b3a3ed625488d8ad0b589f783d838d5a9`
- Acceptance-registry SHA-256:
  `aefb83471a6f951c2e39046c73a69b20460baa2c012c6b474a1802ca70e46c08`
- Approval validator SHA-256:
  `fa87f543accb577d9ae825b6889eeb6c3466af78f9b17bc90b263c04e744c5f8`
- Mutation validator SHA-256:
  `fe187096675cc23f5cd4489b2aff5b1ef629c3043c1624c2bfa64442b465d7a9`
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
| `python3 tests/validate_story_approval_regressions.py` | PASS as implemented, but incomplete; R17-ARCH-01 and R17-ARCH-02 |
| Frozen compatibility replay | PASS — 90 inherited plus 4 approved deviations |
| Release oracle validation | PASS — reported complete crash/rollback/FD4/toolchain mutation inventory |
| Bound implementation replay | PASS — exact implementation-commit bytes are supplied as argv 1 in the bounded sandbox |
| AD inventory | PASS — AD-1..25 represented |
| Limit inventory | PASS — ARCH-LIM-1..24 represented |
| Story-reference integrity | FAIL — unsupported/malformed plural references are ignored |

## Findings

### R17-ARCH-01 — The public mutation suite still does not prove its required trust-boundary matrix

**Severity: blocking**

The R17 mutation change adds only a runner-hash mutation and an
implementation-hash mutation. The hermetic suite otherwise exercises the
existing same-principal, result-path escape, false exit, zero-change, and
author/committer mismatch cases. It still has no isolated mutations for runner
path substitution or ordering; fixture path/bytes/hash substitution; expected
path/bytes/hash substitution; result hash, ordering, or cardinality; copied
expectation with changed-but-nonparticipating implementation behavior; symlink
escape; dirty/untracked approval or bound files; unknown approval/completion/
binding/result keys; criterion ordering or criterion hash; forged ancestry; or
a predecessor completion on divergent history. The aggregate therefore prints
`story approval regression mutations: PASS` without exercising most of the
fail-closed invariants on which C-23 assignment and completion authority rests.

The new positive control does demonstrate that one implementation value
(`done`) participates in replay, but it does not mutate that value while
retaining fixture, runner, expected, and claimed result evidence. It therefore
does not directly prove that an implementation-behavior substitution is
rejected by the public CLI.

**Required closure:** implement a table-driven isolated mutation inventory in
which every case begins from a valid hermetic approval/completion/dependency
chain, changes exactly one named invariant, invokes the public CLI or aggregate
entry point, and asserts the specific rejection. Include an implementation
behavior mutation with otherwise unchanged oracle evidence and a divergent-
predecessor-history mutation. Print the executed mutation count and names so
the aggregate result is auditable.

### R17-ARCH-02 — Story-reference integrity remains match-only rather than grammar-complete

**Severity: blocking**

`canonical_rows()` validates singular references with `Story (\d+\.\d+)` and
exact plural ranges with `Stories (\d+\.\d+) through (\d+\.\d+)`. It never
enumerates every `Story`/`Stories` token and requires that the complete token be
consumed by an allowed grammar. Consequently a typo such as `Stories 5.1
thrugh 5.9`, a plural list, a mixed list/range, trailing unresolved text, or a
cross-epic form outside the exact regex is silently ignored rather than
rejected. The mutation suite contains no malformed, unresolved-simple,
descending, cross-epic, out-of-range, or unsupported-list reference cases.

The two ranges currently present in the artifact happen to match and resolve;
that is not a fail-closed integrity gate for future mutations in boundaries,
dependencies, validation text, or acceptance criteria.

**Required closure:** define one explicit Story-reference grammar, scan every
`Story` and `Stories` occurrence outside the normative JSON registry, require
complete consumption, expand all accepted lists/ranges, and require every
resolved ID exactly once in the ordered 75-Story heading registry. Reject
malformed, cross-epic, descending, duplicate, and out-of-range forms. Add
isolated mutations for each rejection class, including an unresolved singular
reference and a malformed plural range.

## Final status

The frozen target is not eligible for final/current promotion. Remediate both
findings, settle a new digest, and rerun all three independent review lanes.
