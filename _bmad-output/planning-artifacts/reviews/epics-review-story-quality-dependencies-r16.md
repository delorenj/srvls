---
review: story-quality-dependencies
round: 16
settledCommit: 630498ad05e566a4c858c17f1a643e71575930d5
verdict: FAIL
findingCount: 4
reviewer: independent-r16-story
---

# Round 16 Story Quality and Dependency Review

## Verdict

**FAIL — 4 findings.** The 75-story backlog, 150-row registry, and dependency
DAG remain structurally sound. R16 binds runner path and bytes before
implementation and replays those immutable bytes in a temporary directory with
a ten-second timeout. The assignment gate does not actually validate those new
runner fields, the replay remains host-capable rather than isolated, and the
mutation and workflow checks do not prove the newly claimed controls. PASS
requires zero findings.

## Frozen artifact and scope

| Check | Observed value |
| --- | --- |
| Settled commit | `630498ad05e566a4c858c17f1a643e71575930d5` |
| Commit subject | `docs: isolate and bound oracle replay` |
| `epics.md` SHA-256 | `8b9d3f4b731fca03f2ac8cbaa13d95fe00c4609aef9424ff2747aec66a8ffb17` |
| `epics.md` Git blob | `0410d729526afc84d75ece7d4b6c833a86b80d51` |
| Story / AC inventory | 75 Stories; 150 canonical registry rows |
| Dependency graph | 75 earlier-only edges; no unknown target, forward edge, or cycle |

I audited all 75 story sections, dependency declarations, the acceptance
registry and both validators, all five status-changing workflows, and the R16
delta from R15. I ran the supplied registry, mutation, aggregate architecture,
quarantine, syntax, XML, and independent story/DAG checks.

## Prior-finding reconciliation

| R15 finding | R16 disposition |
| --- | --- |
| R15-SQ-01 | Partially closed: runner path/hash moved into pre-implementation approval, and replay materializes historical bytes. The assignment validator omits validation of those fields and no mode/invocation contract exists. |
| R15-SQ-02 | Partially closed: replay has a minimal environment, temporary working directory, immutable inputs, and timeout. It retains host filesystem, process, and network authority and ignores stderr/side effects. |
| R15-SQ-03 | Open: only the happy runner changed to consume its fixture; the requested adversarial replay and structural workflow mutations were not added. |

## Findings

### R16-SQ-01 — A story can be assigned with an invalid or absent approved runner

**Severity: Critical**

`validate_approval` requires the runner keys syntactically, but its two loops
validate only `fixturePath`/`fixtureSha256` and
`expectedResultPath`/`expectedResultSha256`
(`tests/validate_story_fixture_approvals.py:171-201`). It does not type-check the
runner path/hash, require the path to remain inside its oracle, require a
tracked file, validate current or fixture-author bytes, or bind executable
mode and invocation. Runner validation first occurs after implementation in
`validate_completion` (`:242-245`). Thus a missing, malformed, escaping, or
fabricated runner approval passes every `ready-for-dev`/`in-progress`
assignment route, contradicting C-23's pre-assignment independent oracle.

**Required closure:** validate runner path, SHA-256, Git-tree type/mode, bytes,
oracle containment, and exact invocation/fixture-argument contract inside
`validate_approval`; make the approval schema bind them. Add assignment-time
mutations for missing runner, malformed hash, path escape, wrong bytes,
symlink/non-regular tree entry, non-executable mode, and argument substitution.

### R16-SQ-02 — Temporary-directory replay is bounded but not isolated

**Severity: Critical**

The runner receives a reduced environment and disposable cwd, but it still
runs as the reviewing user with `/usr/bin:/bin`, inherited filesystem and
process authority, and unrestricted network access
(`tests/validate_story_fixture_approvals.py:250-262`). It can read `/etc`, the
repository by absolute path, query the network, signal processes, or write
outside the temporary directory. CPU/memory/process/output are unbounded until
the wall timeout. stderr and filesystem side effects are captured or discarded
without policy; only exit and stdout hash are judged (`:263-268`). This is not
the isolated, read-only, disabled-network replay required by the prior finding
or implied by the completion evidence.

**Required closure:** use a fail-closed sandbox mechanism that provides a
read-only/hidden host filesystem, disabled network, bounded CPU/memory/process
and output, exact executable/interpreter policy, explicit stderr policy, and
only approved read-only inputs plus a controlled output location. Prove the
repository and other host paths cannot be read or changed.

### R16-SQ-03 — The mutation suite does not exercise the R16 trust boundary

**Severity: High**

The only R16 regression change replaces `printf expected` with a `sed` runner
and moves runner metadata from completion to approval
(`tests/validate_story_approval_regressions.py:97-138`). No rejection case
mutates runner path/hash/mode, dirty or alternate bytes, fixture argument,
stdout, stderr, timeout, environment, host-state/network access, side effects,
or resource exhaustion. The existing false-exit mutation still fails before
replay. Consequently the green mutation result does not test the controls
added to close R15-SQ-01/02.

**Required closure:** add executable, independently failing mutations for each
approval and replay property, including a copied-expected/fixture-ignoring
runner, hang, stdout/stderr mismatch, path escape, host read/write, repository
mutation, network attempt, and output/resource exhaustion. Require all from the
aggregate gate.

### R16-SQ-04 — Workflow dominance remains asserted by substring counts

**Severity: High**

The regression harness checks string order/count and the presence of generic
`HALT` text (`tests/validate_story_approval_regressions.py:47-66`). It does not
associate a HALT with a particular failed command, traverse branches, or prove
that every write to `ready-for-dev`, `in-progress`, `review`, and `done` is
dominated by the appropriate assignment/completion gate. A workflow can add an
unguarded state write or move a write before its gate while these assertions
remain green.

**Required closure:** parse workflow structure and enumerate every advanced
status mutation with its control-flow predecessors, or route all mutations
through one executable transition program. Add mutations that insert or move
an unguarded write in each workflow and demonstrate aggregate-gate rejection.

## Additional specification inconsistency

C-23 says the completion object binds a runner path/SHA-256
(`epics.md:522-526`), while the R16 completion schema explicitly removes those
keys and moves them to approval. Align the prose with the enforced schema while
closing R16-SQ-01.

## Commands executed

```text
git rev-parse HEAD
git log --oneline -8
git diff 5532c146..630498a --stat
git diff 5532c146..630498a -- tests/validate_story_fixture_approvals.py tests/validate_story_approval_regressions.py _bmad-output/planning-artifacts/epics.md
sha256sum _bmad-output/planning-artifacts/epics.md
git hash-object _bmad-output/planning-artifacts/epics.md
python3 tests/validate_story_fixture_approvals.py
python3 tests/validate_story_approval_regressions.py
bash tests/validate_architecture_contracts.sh
python3 tests/validate_planning_quarantine.py
python3 -m py_compile tests/validate_story_fixture_approvals.py tests/validate_story_approval_regressions.py
xmllint --noout _bmad/bmm/workflows/4-implementation/{create-story,dev-story,code-review}/instructions.xml
python3 <read-only 75-story and dependency-DAG audit>
rg -n 'validate_story_fixture_approvals|ready-for-dev|in-progress|review|done' _bmad/bmm/workflows/4-implementation
```

All supplied gates returned PASS. Those results do not close the four findings
above.
