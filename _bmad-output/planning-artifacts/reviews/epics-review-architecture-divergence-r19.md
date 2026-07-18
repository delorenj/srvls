---
reviewType: implementation-architecture-divergence
round: 19
targetCommit: 0df6e9aa8a4b63668944065852ef3cc3f693f0d3
targetArtifact: _bmad-output/planning-artifacts/epics.md
verdict: FAIL
findingCount: 3
reviewedAt: 2026-07-17
---

# R19 Implementation / Architecture Divergence Review

## Verdict

**FAIL — 3 findings.** The canonical architecture, coverage inventory, current
contract oracles, quarantine behavior, and approval regression suite all pass.
The new completion replay nevertheless does not replay the committed
implementation faithfully, does not recognize a normal executable as consumed,
and lacks mutation proofs for the new trust boundaries. Those defects make
Contract C-23 unsatisfiable for ordinary compiled execution and leave its
claimed exact implementation reference open to regressions.

## Frozen review basis

- Commit: `0df6e9aa8a4b63668944065852ef3cc3f693f0d3`
- Architecture: `ARCHITECTURE-SPINE.md`, AD-1 through AD-25, all AD-11
  acceptance obligations, and AD-20 limits.
- Planning authority: canonical `epics.md`, Contracts C-01 through C-24, the
  machine-checkable coverage registry, and the 150-row acceptance registry.
- Enforcement surfaces: architecture aggregate, compatibility/contracts/release
  oracles, C-23 assignment and completion validators, mutation suite, and the
  create/dev/review/sprint workflow transitions.

No product code or planning authority was modified during this review.

## Read-only validation record

| Check | Result |
|---|---|
| `git rev-parse HEAD` | PASS — exact settled commit |
| `bash tests/validate_architecture_contracts.sh` | PASS |
| `python3 tests/validate_story_fixture_approvals.py` | PASS — 75 stories / 150 rows |
| `python3 tests/validate_story_approval_regressions.py` | PASS |
| `python3 tests/validate_planning_quarantine.py` | PASS |
| Compatibility replay/source pins/hashes | PASS |
| Contract and release oracle replay/mutations | PASS |
| AD-1..AD-25 and AD-11 coverage inventory | PASS — exercised by aggregate gate |
| Exact implementation replay fidelity | FAIL — R19-ARCH-01 |
| Executable/reference-consumption proof | FAIL — R19-ARCH-02 |
| New replay-boundary mutation coverage | FAIL — R19-ARCH-03 |

## Findings

### R19-ARCH-01 — Replay changes the committed implementation's Git object semantics

**Severity: blocking**

`validate_completion()` copies every manifest entry's blob bytes into a fresh
regular file and unconditionally applies mode `0500`. The completion manifest
contains only `path`, `relativePath`, and `sha256`; it does not bind the Git
object type or mode. A committed regular data file, executable, and symbolic
link are therefore all replayed as a different executable regular file. A
symlink is especially unsafe: `git show <commit>:<path>` supplies its target
text, so replay validates a regular file containing that text rather than the
committed link and its resolution behavior.

This contradicts C-23's exact implementation artifact/manifest claim and can
both accept behavior the commit does not have and reject behavior it does have.
It also weakens AD-9/AD-11 compatibility evidence wherever executable mode,
link identity, or path resolution is part of the consumer boundary.

**Required closure:** bind Git object type and mode for every implementation
entry; either reconstruct those semantics exactly in the sandbox or explicitly
reject unsupported object types before completion. Add positive replay for
regular data and executable files plus negative mutations for mode/type/link
changes.

### R19-ARCH-02 — `openat` is not a complete implementation-consumption proof

**Severity: blocking**

The validator requires each manifest path to appear in an `strace -e
trace=openat` log. Normal execution of a compiled implementation is observed as
`execve`, not an `openat` of that executable by the approved runner. Likewise,
interpreters and loaders may consume references through `execve`, `open`,
`openat2`, `stat`/`readlink`, or memory mapping paths that this filter does not
observe. Consequently a legitimate runner that directly executes the built
srvls artifact fails the gate even when its exit and stdout exactly match the
independently approved expectation. Conversely, substring presence in an
`openat` trace proves only that a path was opened, not that the replayed result
was derived from that file.

This makes the post-implementation C-23 gate incompatible with the Rust binary
and release artifacts required by AD-9, AD-11, AD-12, AD-18, and AD-22, blocking
their stories from reaching a valid completed state.

**Required closure:** define the supported reference/consumption operations and
trace them without substring matching (at minimum exact normalized `execve` and
file-open references), or replace syscall inference with an approved runner
protocol that emits a cryptographically bound list of consumed manifest
objects. Prove direct binary execution and multi-file consumption positively,
and prove an unconsumed manifest entry is rejected.

### R19-ARCH-03 — Mutation coverage does not exercise the newly asserted replay boundaries

**Severity: blocking**

The R19 mutation additions cover approval unknown keys, criterion hash, oracle
cardinality, fixture/runner/expected hashes, and verdict. Existing completion
mutations cover a result-path escape, nonzero attestation, one implementation
hash, and a zero-change commit. They do not mutate the newly introduced exact
diff equality, role-distinct bytes, per-file access/reference requirement,
result-versus-approved expectation, implementation object mode/type, duplicate
repository path, or extra/missing manifest entry. Thus the suite can remain
green if any of those new controls is removed or inverted.

Because these controls are the executable proof behind C-23's exact-manifest,
sandboxed-replay, and independent-expectation requirements, a green regression
suite is not evidence that the architecture boundary fails closed.

**Required closure:** add hermetic negative mutations for every new predicate,
including undeclared added/removed/renamed diff entries, duplicate repository
paths, unconsumed entries, mismatched expected result, role aliasing, and Git
mode/type/link changes; add positive reference cases for direct executable and
multi-file replay.

## Architecture divergence matrix

| Area | Result | Evidence |
|---|---|---|
| AD-1..AD-8 | PASS | Ownership, storage, lifecycle, collection, and ordering remain mapped and aggregate-clean |
| AD-9 / AD-11 | FAIL | Exact compatibility and acceptance evidence cannot be faithfully replayed for executable/type-sensitive artifacts |
| AD-12 / AD-18 / AD-22 | FAIL | Rust bootstrap, installed binary, and codec/release executables encounter the `openat`-only completion barrier |
| AD-13..AD-17, AD-19..AD-21, AD-23..AD-25 | PASS at backlog level | Owners, limits, cuts, and oracle rows are present; no separate semantic divergence found |
| C-23 assignment/dependency gates | PASS | Approval identity, oracle cardinality, criteria, dependencies, and workflow transitions validate |
| C-23 completion replay/reference gate | FAIL | R19-ARCH-01 and R19-ARCH-02 |
| Replay mutation evidence | FAIL | R19-ARCH-03 |
| Planning discovery/quarantine | PASS | One canonical artifact and byte-exact retired-history quarantine |

## Final status

The backlog is not eligible for final/current promotion at this digest.
Remediate all three findings and run a fresh independent three-lane review on a
single new settled commit.
