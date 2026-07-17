---
reviewType: story-quality-dependency-ordering
round: r17
subjectCommit: b7e8bc6c619b824c75d951fef8a3ebe104512c6e
verdict: FAIL
findingCount: 3
reviewer: independent-r17-story-lane
---

# R17 Story Quality and Dependency Review

## Verdict

**FAIL — 3 findings.** The 75-story inventory, 150 acceptance-row registry,
declared predecessor graph, transition workflows, and approval/completion
mutation suite were reviewed at the settled subject commit. All repository
gates pass, but the completion protocol is not capable of proving the ordinary
multi-file Rust implementations described by the backlog, and two transition
integrity gaps remain.

## Scope and evidence

- Audited all 75 Story sections for user value, boundary, mappings,
  dependencies, validation expectations, exclusions, and two ordered criteria.
- Parsed every declared predecessor and confirmed references resolve to earlier
  canonical Story IDs.
- Inspected create-story, dev-story, code-review, sprint-planning, and
  sprint-status mutation paths.
- Inspected the C-23 assignment/completion validator and its hermetic mutation
  tests.
- Executed `python3 tests/validate_story_fixture_approvals.py` and
  `bash tests/validate_architecture_contracts.sh`; both passed at the subject
  commit. Passing those checks does not exercise a representative Rust Story
  completion.

## Findings

### R17-SQ-01 — Critical — The completion sandbox cannot validate the multi-file Rust Stories it gates

Contract C-23 says each oracle receives one changed `implementationPath` and
the validator copies only that single Git blob to `/work/implementation`, marks
it executable, and invokes the runner with only that file and one fixture
(`epics.md:503-527`; `tests/validate_story_fixture_approvals.py:251-277`). It
does not materialize the implementation commit's source tree, Cargo workspace,
lockfile, dependencies, sibling modules, migrations, or test support. Story 1.1
already requires a Rust workspace plus `cargo test --locked`, and nearly every
subsequent implementation Story necessarily changes/uses multiple project
files (`epics.md:3243-3264`). A normal checked-in Rust source file is not a
standalone executable; a built target is normally not a tracked implementation
artifact. Consequently `--complete` can only pass for an artificial
single-file executable/proxy, not for the implementation boundary the Story
claims to validate. The existing regression test hides this mismatch by using
a one-file shell-readable `implementation` fixture.

**Required remediation:** replay each approved oracle against a read-only
materialization of the exact implementation commit (with a separately writable
scratch/home), bind the complete declared change set or an immutable build
manifest, and pass a stable repository/workspace entry point to the runner.
Add a mutation/integration test that completes a representative multi-file
Rust/Cargo Story and proves omitted or substituted sibling files fail.

### R17-SQ-02 — High — C-23 permits tautological oracle bindings instead of independent fixture, runner, and expectation evidence

`within_oracle()` accepts a binding path equal to `oraclePath`, and
`validate_approval()` never requires `fixturePath`, `runnerPath`, and
`expectedResultPath` to be distinct (`tests/validate_story_fixture_approvals.py:146-148,175-190`).
This is especially material for Stories whose declared oracle is itself a file
(for example Story 1.1 names `tests/architecture_boundaries.rs`, Story 1.2 names
manifest/SHA files, and Stories 7.1/7.2 name JSON evidence files). The same
tracked bytes can therefore be bound as the oracle, runner, fixture, and/or
expected result where hashes happen to agree, defeating the stated independent
input/runner/expected-output separation. The mutation suite checks a path
outside an oracle but has no aliasing mutation.

**Required remediation:** define the binding model for file-valued versus
directory-valued owning oracles, require disjoint typed roles (executable
runner, immutable input fixture, immutable expected result), reject path/byte
aliasing where independence is required, and add mutations for every prohibited
alias. Update Story validation expectations that currently name data files as
the oracle so each identifies an actual executable runner and its separate
inputs/expectations.

### R17-SQ-03 — High — create-story has a check/use race before ready-for-dev mutation

Every selection branch runs C-23 in Step 1, but the workflow then performs the
entire context-generation sequence and writes the Story before setting its
document and sprint states to `ready-for-dev` in Steps 5/6
(`create-story/instructions.xml:20-100,276-334`). There is no second approval
and predecessor check immediately before either authority mutation. During a
long generation, the approval, canonical criteria, owning oracle, predecessor
completion, or branch head can change after the successful preflight. The
workflow would still publish `ready-for-dev` from stale evidence. The regression
suite only asserts that one validator string occurs before the first
`template-output`; it does not test invalidation between preflight and status
write.

**Required remediation:** rerun the exact assignment validator immediately
before the first Story status write and again atomically with sprint-status
mutation (or pin and verify one immutable head/digest across the workflow).
Add a workflow regression that changes approval/predecessor/criterion state
after initial selection and proves neither output becomes `ready-for-dev`.

## Zero-finding acceptance condition

Rerun this independent lane only after all three findings are remediated and a
new settled digest is published. PASS requires a representative multi-file
completion proof, aliasing mutations, transition-race mutation coverage, and no
new Story/dependency findings.
