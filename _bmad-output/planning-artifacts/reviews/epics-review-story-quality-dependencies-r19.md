---
reviewType: story-quality-dependency-ordering
round: r19
subjectCommit: 0df6e9aa8a4b63668944065852ef3cc3f693f0d3
observedSha256: dbd4b4e95a1bc0f272d959ef9587078d2220d7e19134c7b183fa8acf8f6c7059
verdict: FAIL
findingCount: 3
reviewer: independent-r19-story-lane
storyCount: 75
acceptanceCriterionCount: 150
declaredDependencyEdgeCount: 75
---

# R19 Story Quality and Dependency Review

## Verdict

**FAIL — 3 findings.** The canonical story inventory, required-section
grammar, acceptance-row registry, and declared dependency graph are complete
and structurally valid. The R18 remediation does not, however, supply an
implementation-complete replay, a mutation matrix for the controls it now
claims, or atomic authority transitions across the Story and sprint-status
surfaces. PASS requires zero findings.

## Frozen subject and method

- Pinned the review to commit
  `0df6e9aa8a4b63668944065852ef3cc3f693f0d3` and observed exact `epics.md`
  SHA-256
  `dbd4b4e95a1bc0f272d959ef9587078d2220d7e19134c7b183fa8acf8f6c7059`.
- Parsed all 75 unique Story sections and confirmed each has its user-value
  statement, implementation boundary, requirement mapping, dependency,
  validation expectation, out-of-scope statement, and two GWT rows.
- Parsed 75 declared dependency edges. Every target exists and precedes its
  consumer; the graph has no forward edge or cycle.
- Inspected assignment and completion validation plus create-story,
  dev-story, code-review, sprint-planning, and sprint-status mutation paths.
- Executed the registry validator, approval regression suite, aggregate
  architecture gate, Python compilation, and XML parsing. All supplied gates
  pass, but the green regression suite does not exercise the failures below.

## Findings

### R19-SQ-01 — Critical — Completion replay still cannot represent or execute the exact implementation commit

The new complete-diff comparison uses only `git diff --name-only` and then
requires every named path to exist at the implementation commit
(`tests/validate_story_fixture_approvals.py:280-290`). It therefore cannot
represent a deletion, does not bind a mode change or rename semantics, and
does not bind one canonical manifest object shared by every oracle. Replay
then constructs a synthetic tree containing only caller-selected changed file
bytes, forces every materialized file to mode `0500`, and mounts no unchanged
workspace files, lockfile, vendored dependencies, or pinned Rust toolchain
(`293-315`). An ordinary multi-file Cargo story necessarily consumes unchanged
workspace and dependency inputs and cannot be replayed by this sandbox.

The `openat` trace requirement does not repair that gap: opening each selected
path is not proof that the exact repository tree was built or tested, and the
approved runner receives a writable `/trace` mount while the validator trusts
the resulting pathname text (`305-323`). The positive regression remains a
single root-level text file consumed by a shell script
(`tests/validate_story_approval_regressions.py:94-139`), not a representative
Rust workspace.

**Required closure:** derive and bind one mode-aware, rename/deletion-aware
manifest from the complete approval-to-implementation commit diff; require the
identical manifest for every oracle; materialize the exact read-only Git tree
with immutable toolchain/dependency inputs and separate writable scratch; and
prove a real multi-file Cargo completion end to end.

### R19-SQ-02 — High — The regression matrix does not test the R18 controls

The validator now rejects three equal role hashes and compares changed path
names, but the regression suite has no path-alias or byte-alias case, no
omitted or extra changed sibling, no divergent per-oracle manifest, no
deletion, rename, mode mutation, Cargo replay, trace forgery, substituted
workspace input, or missing toolchain/dependency case
(`tests/validate_story_approval_regressions.py:94-225`). Its newly factored
mutations cover schema/hash/cardinality/verdict variations that predate the R18
findings; they do not execute the new role-separation or complete-change-set
branches. Consequently `story approval regression mutations: PASS` is not
evidence for either claimed remediation.

**Required closure:** add independently failing mutations for every prohibited
role alias and complete-tree divergence, plus one successful representative
multi-file Cargo replay. Require those cases from the aggregate gate.

### R19-SQ-03 — Critical — Story and sprint-status authority writes remain non-atomic and stale-evidence windows remain

Create-story revalidates before setting the Story document to
`ready-for-dev`, then saves that document and later writes sprint status with
no second gate or immutable-head check
(`create-story/instructions.xml:318-336`). Dev-story validates completion,
writes the Story to `review`, performs intervening definition-of-done work, and
then writes sprint status without revalidation
(`dev-story/instructions.xml:332-361`). Code-review does revalidate before its
second write, but the first Story write is already saved; a failure or evidence
change at the second gate therefore leaves the two authority surfaces split
(`code-review/instructions.xml:171-210`). Sprint-status prose likewise cannot
make a multi-file mutation atomic merely by re-running commands immediately
before its write.

The regression suite only checks instruction-string presence and ordering
(`tests/validate_story_approval_regressions.py:43-63`). It performs no
transition execution and no mutation of approval, criterion, predecessor,
completion, source status, or HEAD between preflight and either authority
write.

**Required closure:** route every status transition through one executable,
atomic transition primitive (or one pinned immutable evidence/head transaction)
that updates both canonical surfaces or neither. Add branch-complete executable
mutations at every preflight/write boundary and assert both files remain
byte-identical on rejection.

## Live command results

```text
python3 tests/validate_story_fixture_approvals.py
  story acceptance registry: PASS (75 stories, 150 canonical-criterion-bound rows)

python3 tests/validate_story_approval_regressions.py
  Story 1.2 fixture approval: PASS (...)
  story approval regression mutations: PASS

bash tests/validate_architecture_contracts.sh
  architecture contract gate: PASS

python3 -m py_compile tests/validate_story_fixture_approvals.py tests/validate_story_approval_regressions.py
  PASS

xmllint --noout create-story/instructions.xml dev-story/instructions.xml code-review/instructions.xml
  PASS
```

These results establish that the checked-in gates are internally green, not
that the missing replay and transition cases are safe.

## Zero-finding acceptance condition

A later settled digest can pass this lane only after exact full-tree Cargo
replay, a complete role/diff/sandbox mutation matrix, and atomic dual-surface
workflow transitions are implemented and independently rerun with no new
story-quality or dependency findings.
