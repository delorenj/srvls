---
review: story-quality-dependencies
round: 14
settledCommit: 761b9e2385e0c0b967cda93a132d126c32c716d1
verdict: FAIL
findingCount: 3
reviewer: independent-r14-story
---

# Round 14 Story Quality and Dependency Review

## Verdict

**FAIL — 3 findings.** The 75-story backlog and its dependency graph are
structurally implementation-ready, and the R13 workflow bypasses are closed at
their edited surfaces. The C-23 gate is nevertheless unusable in this
repository, and its new completion object still records an assertion of
execution rather than independently proving execution. PASS requires zero
findings.

## Frozen artifact and scope

| Check | Observed value |
| --- | --- |
| Settled commit | `761b9e2385e0c0b967cda93a132d126c32c716d1` |
| Commit subject | `docs: attest executed oracle completion` |
| `epics.md` SHA-256 | `13eb5926f0b2356bbe6730cfe4050b2dfc2b2addd95a83402db926834a67796f` |
| `epics.md` Git blob | `5b5a210ccb911e6e5d44f5c6b3f7214cde8a226d` |
| Artifact size | 4,980 lines; 220,101 bytes |
| Story / AC inventory | 75 Stories; 150 canonical rows |
| Dependency graph | 74 earlier-only edges; one root; no unknown target, forward edge, or cycle |

I audited every Story section, the complete acceptance registry, every
dependency declaration, the assignment and completion implementations, the
hermetic mutation suite, and all status-changing routes in create-story,
dev-story, code-review, sprint-planning, and sprint-status. I also ran the
registry, mutation, aggregate architecture, XML, and Python syntax gates.

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

All 75 Stories have a user-value statement, scoped implementation boundary,
requirement mapping, explicit dependency, validation expectation, out-of-scope
boundary, and two GWT criteria. The registry contains exactly one unique P01
and N01 row for each Story and binds their exact criterion bytes. No Story
quality or semantic forward-dependency defect was found in the backlog text.

## Prior-finding reconciliation

| R13 finding | R14 disposition | Evidence |
| --- | --- | --- |
| R13-SQ-01 | Closed at workflow surface | code-review derives the Story ID and runs `--complete` before either `done` write. |
| R13-SQ-02 | Closed at workflow surface | code-review runs assignment validation before either Story or sprint-status mutation and requires `review` as the source of the return to `in-progress`. |
| R13-SQ-03 | Closed at workflow surface | sprint-status validates every correction above `backlog`, and additionally requires completion for `review` or `done`, before applying the batch. |
| R13-SQ-04 | Closed at validator surface | completion now applies `within_oracle` to `resultPath`; the hermetic suite includes an unrelated-path rejection. |

## Findings

### R14-SQ-01 — C-23 rejects every real commit in the canonical repository

**Severity: Critical**

The repository uses SHA-1 Git object IDs: `git rev-parse --show-object-format`
returns `sha1`, and HEAD is a 40-hex object ID. The validator uses one
SHA-256-only regular expression (`tests/validate_story_fixture_approvals.py:19`)
not just for byte digests, but also for `reviewerCommit`,
`fixtureAuthorCommit`, and `implementationCommit` (`:176`, `:212`). Therefore
no approval or completion object containing an actual commit from this
repository can pass. The mutation suite hides the incompatibility by creating
its temporary repository with `git init --object-format=sha256`
(`tests/validate_story_approval_regressions.py:73`). A backlog whose mandatory
pre-assignment gate cannot accept its own repository is not assignable.

**Required closure:** distinguish 64-hex content SHA-256 values from Git object
IDs. Validate commit fields by resolving the repository's native object IDs
(or accepting Git-supported algorithms and then requiring `cat-file` commit
resolution), and run the primary hermetic success path under the same object
format as the canonical repository. Add explicit positive SHA-1 and negative
non-commit/unresolved-object cases.

### R14-SQ-02 — Completion provenance does not prove that an oracle executed

**Severity: Critical**

Contract C-23 now calls the result “fresh executed”, but
`validate_completion` never executes `runnerPath` and never consumes the
approved fixture. It only proves that an arbitrary path under the oracle
existed in `fixtureAuthorCommit`, trusts a declarative `exitCode: 0`, and
checks that an implementation-committed result file contains the already-known
expected bytes (`tests/validate_story_fixture_approvals.py:225-240`). An
implementer can select any pre-existing file as the runner, copy the approved
expected bytes to a new in-oracle path, write zero into the JSON, and satisfy
every check without running a test. File executability, command/arguments,
fixture consumption, stdout/stderr or result production, and runner-result
causality are not established. The change therefore attests a claim made by
the implementation change; it is not independent executed-oracle evidence.

**Required closure:** bind the runner path, bytes, executable mode, invocation,
fixture, and expected output before implementation, then have the validator
execute that immutable runner hermetically against the approved fixture (or
verify a CI-signed execution attestation whose trust root and payload are
independent of the implementation commit). Compare freshly captured exit code
and result bytes directly. Add mutations for a non-executable/arbitrary runner,
an unexecuted copied expected result, false zero exit, wrong fixture, and stale
or replayed execution evidence.

### R14-SQ-03 — The regression suite does not protect the workflow fixes or the new execution fields

**Severity: High**

The regression script still reads only create-story, dev-story, and
sprint-planning (`tests/validate_story_approval_regressions.py:39-41`). It does
not load or assert ordering in code-review or sprint-status, even though those
two files are the sole R13 remediation for three status-transition bypasses.
It also adds only a result-path escape mutation for the new completion schema;
there are no mutations for runner substitution/hash, nonzero/forged exit,
pre-existing result freshness, result-to-oracle uniqueness, or the native Git
object format. The green `story approval regression mutations: PASS` therefore
does not regression-test the newly claimed workflow or executed-evidence
properties.

**Required closure:** statically parse every status-changing workflow and prove
the relevant gate precedes each advanced-state write, including both Story and
sprint-status writes. Extend the hermetic suite with the execution and Git-ID
mutations listed above, and require the suite from the aggregate gate.

## Commands executed

```text
git rev-parse HEAD
git rev-parse --show-object-format
sha256sum _bmad-output/planning-artifacts/epics.md
python3 tests/validate_story_fixture_approvals.py
python3 tests/validate_story_approval_regressions.py
bash tests/validate_architecture_contracts.sh
python3 -m py_compile tests/validate_story_fixture_approvals.py tests/validate_story_approval_regressions.py
xmllint --noout _bmad/bmm/workflows/4-implementation/{create-story,dev-story,code-review}/instructions.xml
python3 <read-only 75-story, 150-row, and dependency-DAG audit>
rg -n 'validate_story_fixture_approvals|ready-for-dev|in-progress|review|done' _bmad/bmm/workflows/4-implementation tests
```

The no-argument registry gate, current SHA-256-only hermetic suite, aggregate
architecture gate, Python compilation, and XML parsing all returned PASS. The
green results do not close the three findings above.
