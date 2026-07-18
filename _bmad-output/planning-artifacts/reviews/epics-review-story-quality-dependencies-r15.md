---
review: story-quality-dependencies
round: 15
settledCommit: 5532c1460eda02d0fefdabdf94f6923cc2da9113
verdict: FAIL
findingCount: 3
reviewer: independent-r15-story
---

# Round 15 Story Quality and Dependency Review

## Verdict

**FAIL — 3 findings.** The 75 stories and dependency DAG are structurally
sound, and the native Git-object-ID defect from R14 is closed. The mandatory
completion gate still does not replay an independently approved immutable
runner, its execution is not hermetic, and the mutation suite does not test
those claimed properties. PASS requires zero findings.

## Frozen artifact and scope

| Check | Observed value |
| --- | --- |
| Settled commit | `5532c1460eda02d0fefdabdf94f6923cc2da9113` |
| Commit subject | `docs: replay completion oracles and fix journey dependency` |
| `epics.md` SHA-256 | `4a7c3f749d74d25a40d873945256248caabe65608138ede773a7c290e58aee26` |
| `epics.md` Git blob | `585f33c6082fdce630c5ad37ea972042d9658276` |
| Artifact size | 4,981 lines; 220,257 bytes |
| Story / AC inventory | 75 Stories; 150 canonical rows |
| Dependency graph | 75 earlier-only edges; one root; no unknown target, forward edge, or cycle |

I audited every story section and dependency declaration, the full acceptance
registry, assignment and completion validators, the mutation harness, and all
status-changing routes in create-story, dev-story, code-review,
sprint-planning, and sprint-status. I ran the registry, mutation, aggregate
architecture, planning-quarantine, Python syntax, XML, and independent
story/DAG inventory checks.

## Exhaustive story accounting

| Epic | Stories | AC rows | Structure | Ordering |
| --- | ---: | ---: | --- | --- |
| 1 | 10 | 20 | Pass | Pass |
| 2 | 6 | 12 | Pass | Pass |
| 3 | 11 | 22 | Pass | Pass |
| 4 | 10 | 20 | Pass | Pass |
| 5 | 10 | 20 | Pass | Pass |
| 6 | 13 | 26 | Pass | Pass |
| 7 | 15 | 30 | Pass | Pass |
| **Total** | **75** | **150** | **Pass** | **Pass** |

Every story has a user-value statement, bounded implementation scope,
requirement mapping, dependency declaration, validation expectation,
out-of-scope boundary, and positive and negative GWT rows. The registry binds
exactly one P01 and N01 row per story. Story 6.13 now correctly declares both
Story 2.6 and Story 6.12, closing the R14 journey dependency defect.

## Prior-finding reconciliation

| R14 finding | R15 disposition | Evidence |
| --- | --- | --- |
| R14-SQ-01 | Closed | Commit fields accept native SHA-1 or SHA-256 OIDs, resolve as commit objects, and the hermetic repository now uses the host Git default (SHA-1 here). |
| R14-SQ-02 | Partially remediated; remains open as R15-SQ-01 and R15-SQ-02 | The validator now invokes a runner, but neither runner selection nor the executed bytes are approval-bound, and execution is not hermetic. |
| R14-SQ-03 | Partially remediated; remains open as R15-SQ-03 | The harness reads all five workflows and adds one false-exit mutation, but does not exercise the new runner/replay trust boundary or structurally verify all writes. |

## Findings

### R15-SQ-01 — Replay executes mutable working-tree bytes selected after approval

**Severity: Critical**

`validate_completion` proves that `runnerPath` bytes existed in
`fixtureAuthorCommit`, but `runnerPath` and `runnerSha256` occur only in the
post-implementation completion object. The pre-implementation approval object
does not bind either value. More importantly, the validator executes
`ROOT / result["runnerPath"]` from the current working tree without comparing
those bytes or executable mode to the fixture-author commit and without
requiring the runner to be tracked and clean
(`tests/validate_story_fixture_approvals.py:229-244`). A dirty replacement at
the same path can therefore emit the approved bytes and pass while the
supposedly approved runner is never executed. The implementation also chooses
which historical file to call a runner after approval. This does not satisfy
Contract C-23's independent pre-assignment oracle binding.

**Required closure:** put runner path, SHA-256, executable mode, invocation,
and fixture argument binding in each pre-implementation `oracleBinding`.
Materialize or execute the exact runner blob from the approved commit (or first
require current tracked/clean bytes and mode to equal it), and reject any
completion-side substitution. Add dirty-runner, alternate-historical-runner,
mode-change, untracked-runner, and runner-path-substitution mutations.

### R15-SQ-02 — The claimed hermetic replay is unbounded and can mutate or depend on the repository

**Severity: Critical**

The replay is a plain `subprocess.run([runner, fixture], cwd=ROOT,
capture_output=True)` with the caller's full environment, repository working
directory, network and filesystem access, and no timeout. It can hang the
mandatory gate, read unrelated host state, modify tracked planning or product
files, invoke arbitrary programs, or simply ignore the fixture and print the
known expected bytes. Only stdout and exit status are checked; stderr,
side-effects, fixture consumption, and repository cleanliness after execution
are not. Calling this execution “hermetic” and treating it as durable oracle
evidence is materially stronger than what the validator establishes.

**Required closure:** run immutable approved bytes in a bounded isolated
sandbox with a minimal deterministic environment, read-only inputs, disabled
network, explicit timeout/resource limits, captured stdout/stderr, and a clean
temporary working directory; verify the input binding and reject side effects.
At minimum snapshot and recheck repository state around execution and fail
closed on timeout. Add hanging, environment-dependent, network/host-state,
fixture-ignoring, stderr, and repository-mutation cases.

### R15-SQ-03 — Green mutations still do not protect the replay or workflow ordering claims

**Severity: High**

The R15 mutation addition changes only declared `exitCode` from zero to one;
that fails before the runner is invoked. It therefore does not test replay at
all. There is no mutation for dirty or substituted runner bytes, executable
mode, wrong/ignored fixture, copied expected output, timeout, side effects,
stdout mismatch, or stale execution. Workflow checks are likewise substring
checks: for code-review and sprint-status they establish only that a command
phrase exists somewhere, not that every advanced-state write is dominated by
the correct gate. The aggregate gate can remain green after precisely the
regressions it claims to prevent.

**Required closure:** add executable end-to-end mutations for every replay
property above. Parse each workflow into ordered actions/branches (or provide a
single status-transition program used by every workflow) and assert that each
`ready-for-dev`, `in-progress`, `review`, and `done` mutation is dominated by
assignment/completion validation as appropriate. Require those tests from the
aggregate gate.

## Commands executed

```text
git rev-parse HEAD
git log --oneline 761b9e2..HEAD
git diff --stat 761b9e2..HEAD
sha256sum _bmad-output/planning-artifacts/epics.md
git hash-object _bmad-output/planning-artifacts/epics.md
python3 tests/validate_story_fixture_approvals.py
python3 tests/validate_story_approval_regressions.py
bash tests/validate_architecture_contracts.sh
python3 tests/validate_planning_quarantine.py
python3 -m py_compile tests/validate_story_fixture_approvals.py tests/validate_story_approval_regressions.py
xmllint --noout _bmad/bmm/workflows/4-implementation/{create-story,dev-story,code-review}/instructions.xml
python3 <read-only 75-story, 150-row, and dependency-DAG audit>
rg -n 'validate_story_fixture_approvals|ready-for-dev|in-progress|review|done' _bmad/bmm/workflows/4-implementation
```

All supplied gates returned PASS. Those green results do not close the three
findings above.
