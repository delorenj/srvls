---
reviewType: story-quality-dependency-ordering
round: r21
subjectCommit: 80f1af3798db22cc678ce199be7deb8d034fff89
observedSha256: db1d24c8f4670d3fc72c54f3482a4cb644b57b33b086e128f66b2c2fdd21bcd2
verdict: FAIL
findingCount: 4
reviewer: independent-r21-story-lane
storyCount: 75
acceptanceCriterionCount: 150
declaredDependencyEdgeCount: 75
---

# R21 Story Quality and Dependency Review

## Verdict

**FAIL — 4 findings.** The settled artifact retains 75 complete Story sections,
150 canonical criteria, and an ordered, closed dependency graph. The revised
gate improves isolation and detects a changing `HEAD`, but it does not yet prove
hermetic full-tree consumption, exhaustively mutate those claims, or establish
one bound and singular atomic Story-status authority. PASS requires zero
findings.

## Frozen subject and method

- Reviewed pinned commit `80f1af3798db22cc678ce199be7deb8d034fff89` and
  observed `epics.md` SHA-256
  `db1d24c8f4670d3fc72c54f3482a4cb644b57b33b086e128f66b2c2fdd21bcd2`.
- Parsed 75 unique Story sections, 150 GWT criteria, and 75 declared
  dependency edges. Every target exists and precedes its consumer; no forward
  edge or cycle was found.
- Inspected the static completion replay, approval mutation suite, transition
  primitive, and all implementation workflows that describe Story status.
- Ran the full architecture-contract aggregate. It passes, but its Story
  regression suite does not exercise the failures below.

## Findings

### R21-SQ-01 — Critical — Static replay remains Host-observable and one access is not full-tree consumption

The runner is now required to be a static ELF and executes without mounted Host
libraries, which closes the live toolchain mount. The sandbox still mounts the
live Host's `/proc` and `/dev` (`tests/validate_story_fixture_approvals.py:299-304`)
and the validator neither rejects accesses outside the approved fixture and
implementation tree nor supplies deterministic substitutes. A static approved
runner can therefore derive its verdict from Host process state, devices,
randomness, or clock-like proc data, so identical Git evidence need not replay
identically on another Host.

The claimed exact-tree proof remains only a substring search for one access
under `/work/implementation/` (`308-310`). A runner can inspect one planted
file, ignore every other changed file, and pass; no canonical tree manifest or
per-member consumption/build-input binding is provided. Supplying a full
archive is not evidence that the oracle evaluated that full tree.

**Required closure:** expose only deterministic approved devices/proc data (or
reject all unapproved file accesses), bind a canonical implementation-tree
manifest, and prove that the runner's evaluated input is that manifest/tree
rather than a single convenient path.

### R21-SQ-02 — High — Regression mutations do not execute the new replay and transition invariants

The mutation suite's executable completion case proves one static runner reads
one root-level `implementation` file, but it has no negative cases for dynamic
ELF, `/proc` or `/dev` dependence, omitted/renamed/extra tree members, symlink
or gitlink inputs, executable-mode changes, ignored changed files, or runner
mutation. The status portion still only invokes the helper with missing
arguments (`tests/validate_story_approval_regressions.py:47-71`); it never runs
a successful transition and does not mutate edge, Story-ID/key binding,
approval/completion/predecessor evidence, working-tree bytes, `HEAD`, or source
status between preflight and replacement.

**Required closure:** add independently failing mutations for each replay
boundary and branch-complete executable transition tests, including concurrent
changes at every check/write boundary and byte-identical failure assertions.

### R21-SQ-03 — Critical — Story files remain a contradictory second status surface

The workflows say canonical status exists only in sprint status, but the
canonical create-story template still emits `Status: ready-for-dev`
(`create-story/template.md:1-5`). The dev checklist requires both Story Status
and Sprint Status to become `review` (`dev-story/checklist.md:58-62`), while the
dev workflow retains outputs claiming a Story-file-only `review` update when
sprint tracking is absent or split (`dev-story/instructions.xml:355-373`).
These instructions can produce two divergent authorities despite the newly
added prose forbidding a second Story-file status.

**Required closure:** remove Story status from the template, checklists, and
all fallback/split paths, or make one executable primitive atomically CAS every
declared authority. A prose assertion beside contradictory executable workflow
instructions is not singular authority.

### R21-SQ-04 — Critical — Atomic transition does not bind the approval Story to the mutated key and leaves evidence TOCTOU

`transition_story_status.py` validates `story_id` and independently regex-matches
`story_key`, but never proves they identify the same canonical Story
(`tests/transition_story_status.py:29-58`). A caller can validate approval for
one Story and use it to advance another Story's sprint key. It also accepts any
repository-local file as the status source rather than the configured canonical
sprint-status artifact.

The new `HEAD` comparison detects commits during the window, but all approval,
completion, predecessor, fixture, runner, and result checks include working-tree
state. Those files can change without changing `HEAD` after the subprocess
returns; the helper records no evidence digest and does not revalidate it before
`os.replace` (`42-65`). Thus the status can advance on evidence that is no
longer valid at the atomic write.

**Required closure:** derive the canonical key from the canonical backlog,
reject any ID/key/path mismatch, pin a complete evidence/tree digest, and
revalidate that digest under the same lock immediately before the CAS. Add
executable mismatch and concurrent-working-tree mutation tests.

## Live command results

```text
bash tests/validate_architecture_contracts.sh
  story acceptance registry: PASS (75 stories, 150 canonical-criterion-bound rows)
  story approval regression mutations: PASS
  architecture contract gate: PASS
```

These green results establish current internal consistency; they do not cover
the missing hermeticity, mutation branches, or singular bound status authority.

## Zero-finding acceptance condition

A later settled digest can pass only when replay is deterministic and bound to
the entire evaluated tree, mutation tests demonstrate every fail-closed branch,
and one executable transition owns a canonically bound Story status with no
second status surface or evidence TOCTOU window.
