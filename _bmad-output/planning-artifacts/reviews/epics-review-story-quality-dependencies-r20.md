---
reviewType: story-quality-dependency-ordering
round: r20
subjectCommit: 36dea34febf8ccd644708a4bc8f82140238690d0
observedSha256: db1d24c8f4670d3fc72c54f3482a4cb644b57b33b086e128f66b2c2fdd21bcd2
verdict: FAIL
findingCount: 3
reviewer: independent-r20-story-lane
storyCount: 75
acceptanceCriterionCount: 150
declaredDependencyEdgeCount: 75
---

# R20 Story Quality and Dependency Review

## Verdict

**FAIL — 3 findings.** The settled artifact still has 75 well-formed stories,
150 criteria, and an ordered dependency graph. The R20 subject does not close
the exact-tree replay, branch-complete mutation, or atomic dual-surface status
findings. PASS requires zero findings.

## Frozen subject and method

- Pinned commit `36dea34febf8ccd644708a4bc8f82140238690d0` and observed the exact
  `epics.md` SHA-256
  `db1d24c8f4670d3fc72c54f3482a4cb644b57b33b086e128f66b2c2fdd21bcd2`.
- Parsed 75 unique Story sections and 150 GWT rows. Required story sections are
  present, all 75 declared dependency targets exist and precede their consumer,
  and no forward edge or cycle was found.
- Inspected the completion replay, regression mutations, atomic-status helper,
  and every workflow that writes Story or sprint status.
- Ran the aggregate architecture gate, Python compilation, and workflow XML
  parsing. They are green, but do not exercise the failures below.

## Findings

### R20-SQ-01 — Critical — Replay is not a pinned implementation environment and its trace can be forged

The validator now archives the complete implementation Git tree, which fixes
the earlier caller-selected file subset. It still mounts the review Host's
live `/usr`, `/bin`, `/lib`, and `/lib64` into the sandbox and supplies no
approved toolchain/dependency manifest (`tests/validate_story_fixture_approvals.py:285-301`).
The same implementation commit can therefore pass or fail as Host packages,
Rust toolchains, registries, or shared libraries change. `git archive` also
does not materialize gitlink contents, so this is not a sufficient build input
for a workspace with unbound external dependencies.

The consumption proof is only the presence of one pathname substring in an
`strace` text file (`306-308`). `/trace` is writable inside the runner sandbox
(`298`), so an approved runner can alter `/trace/access`; opening any one path
under `/work/implementation/` also does not prove the complete tree was the
build/test input. The only positive regression remains a root-level text file
read by a shell runner (`tests/validate_story_approval_regressions.py:99-143`),
not a representative multi-file Cargo workspace.

**Required closure:** bind an immutable toolchain and dependency set, make the
tracer output inaccessible to the runner, validate one canonical tree/toolchain
manifest shared by every oracle, and execute a real multi-file Cargo positive
replay plus substituted-toolchain/dependency negative cases.

### R20-SQ-02 — High — The mutation suite still does not test the claimed full-tree and transition controls

The checked-in mutations cover schema keys, row/hash/cardinality changes,
principal aliasing, result-path escape, nonzero attestation, and a zero-change
implementation (`tests/validate_story_approval_regressions.py:160-229`). They
do not exercise deletion, rename, executable-mode change, omitted or extra
tree members, divergent per-oracle trees, symlink/gitlink inputs, writable
trace forgery, substituted Host toolchain or dependencies, or a representative
Cargo replay. Nor does the suite execute a successful status transition or
mutate approval, completion, predecessor, HEAD, Story status, or sprint status
at any preflight/write boundary; it merely checks that workflow text mentions
the helper (`47-71`).

**Required closure:** add independently failing mutations for every full-tree,
role, sandbox, and immutable-environment invariant, and branch-complete
transition tests that inject each evidence/status/HEAD change between gate and
write and prove both authority files remain byte-identical.

### R20-SQ-03 — Critical — The advertised atomic CAS updates only sprint status and leaves TOCTOU windows

`transition_story_status.py` accepts only a sprint-status path and rewrites
only that file (`tests/transition_story_status.py:23-58`). It neither reads nor
CAS-updates the Story document. Create-story saves the Story first and invokes
the helper later (`create-story/instructions.xml:320-335`); dev-story likewise
sets the Story to review before the helper (`dev-story/instructions.xml:336-360`);
code-review saves the Story at lines 178-185 before invoking the helper at
202/209. Each workflow can therefore leave the two canonical status surfaces
split on a crash, failed CAS, or missing key; code-review and dev-story retain
explicit split-state output paths.

The helper's file lock protects only the sprint-status lock file. It runs Git
approval/completion gates at lines 34-41 and then writes at 42-55 without
pinning or rechecking HEAD/evidence, so another process can change approval,
completion, predecessor, or implementation truth after validation and before
the status write.

**Required closure:** one executable primitive must lock, validate a pinned
HEAD/evidence digest, CAS both the Story document and sprint-status source
states, and commit both replacements or neither. Remove all preceding direct
Story-status writes and split-success branches, then prove crash and concurrent
mutation behavior with executable tests.

## Live command results

```text
bash tests/validate_architecture_contracts.sh
  architecture contract gate: PASS

python3 tests/validate_story_approval_regressions.py
  story approval regression mutations: PASS

python3 -m py_compile tests/validate_story_fixture_approvals.py tests/validate_story_approval_regressions.py tests/transition_story_status.py
  PASS

xmllint --noout create-story/instructions.xml dev-story/instructions.xml code-review/instructions.xml
  PASS
```

These results establish internal consistency of the supplied gates, not the
missing immutable replay, mutation coverage, or atomic status behavior.

## Zero-finding acceptance condition

A later settled digest can pass only after a pinned representative Cargo
replay, a complete adversarial mutation matrix, and one executable atomic
dual-surface status transition are independently demonstrated with no new
story-quality or dependency findings.
