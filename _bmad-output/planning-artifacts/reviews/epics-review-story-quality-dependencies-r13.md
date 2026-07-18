---
review: story-quality-dependencies
round: 13
settledCommit: a7f6e55918b036adf7db6f33191b4f7d2f6333f4
verdict: FAIL
findingCount: 4
reviewer: independent-r13-story
---

# Round 13 Story Quality and Dependency Review

## Verdict

**FAIL — 4 findings.** The canonical backlog itself is structurally complete and
ordered, but the implementation-state enforcement remains bypassable and the
completion proof accepts an unscoped result path. This is not a zero-finding
report and must not be used as promotion evidence.

## Scope and settled digest

This review used only commit
`a7f6e55918b036adf7db6f33191b4f7d2f6333f4`. It audited all 75 Story sections,
all 150 exact acceptance-registry rows, the complete 74-edge dependency graph,
the assignment and completion validator, its hermetic mutation suite, and every
implementation workflow route that writes a Story status.

## Findings

### R13-SQ-01 — code-review can mark a Story `done` without completion validation

**Severity:** Critical

`_bmad/bmm/workflows/4-implementation/code-review/instructions.xml:171-205`
sets the Story and sprint tracker directly to `done` when review findings are
fixed. It never runs
`python3 tests/validate_story_fixture_approvals.py --complete <story-id>`.
Consequently a caller can enter code-review with a hand-authored `review`
Story, omit the C-23 completion object entirely, and still reach `done`. This
contradicts Contract C-23 and bypasses the otherwise fail-closed preservation
logic in sprint-planning.

**Required closure:** derive the canonical Story ID in code-review and require a
successful `--complete` check immediately before every `done` write; HALT and
leave the prior state unchanged on non-zero exit. Add a regression assertion
that the gate text precedes both the Story-file and sprint-status `done` writes.

### R13-SQ-02 — code-review can restore `in-progress` without assignment validation

**Severity:** High

The alternate branch at
`_bmad/bmm/workflows/4-implementation/code-review/instructions.xml:177-205`
writes `in-progress` when findings remain, again without running the assignment
form of the C-23 validator. Thus code-review is a second entry route to active
implementation that bypasses fixture approval and completed-predecessor
ordering.

**Required closure:** run
`python3 tests/validate_story_fixture_approvals.py <story-id>` before either
`in-progress` write, HALT on failure, and cover this ordering in the workflow
regression suite.

### R13-SQ-03 — sprint-status correction is an unrestricted state-transition bypass

**Severity:** High

`_bmad/bmm/workflows/4-implementation/sprint-status/instructions.md:55-78`
allows any unrecognized Story status to be corrected directly to any listed
valid status, including `ready-for-dev`, `in-progress`, `review`, or `done`, and
writes the correction without either assignment or completion validation. A
single malformed status therefore opens an explicit interactive route around
all C-23 gates.

**Required closure:** before applying a correction, validate assignment for
`ready-for-dev`/`in-progress` and completion for `review`/`done`; on failure
permit only `backlog` (or leave the malformed value untouched while reporting
the error). Add this workflow to the hermetic/static route assertions.

### R13-SQ-04 — completion accepts a matching result from outside its owning oracle

**Severity:** High

`tests/validate_story_fixture_approvals.py:214-224` checks the result's declared
`oraclePath` and SHA-256, but never applies `within_oracle(resultPath,
oraclePath)`. A completion can therefore point every oracle result at one
unrelated repository file containing the approved expected bytes. The object
then proves byte equality, not that each declared owning oracle emitted its own
executed result. The hermetic suite at
`tests/validate_story_approval_regressions.py:115-148` tests a valid completion,
one zero-change mutation, and identity mismatch, but has no result-path escape
mutation.

**Required closure:** require each `resultPath` to be contained by its paired
owning oracle (using a result-specific containment rule if output suffixes are
needed), require one distinct result binding per oracle, and add hermetic
negative cases for cross-oracle and unrelated-path substitution.

## Confirmed properties

- The artifact contains exactly 75 uniquely identified Stories and exactly two
  canonical criteria per Story.
- The registry contains exactly 150 rows, and the no-argument validator binds
  every row ID, Story ID, kind, criterion bytes, and SHA-256 to `epics.md`.
- Every Story has an implementation boundary, requirement and architecture
  mapping, explicit dependencies, validation expectations, and out-of-scope
  statement.
- The dependency graph contains 74 declared edges, no unknown targets, no
  forward edges, and no cycles. It is a strict implementation sequence from
  Story 1.1 through Story 7.15.
- create-story and dev-story contain assignment gates; dev-story contains a
  completion gate before `review`; sprint-planning revalidates preserved
  advanced states.
- The aggregate architecture contract gate passed at the settled commit.

## Commands executed

```text
git rev-parse HEAD
python3 tests/validate_story_fixture_approvals.py
python3 tests/validate_story_approval_regressions.py
bash tests/validate_architecture_contracts.sh
python3 <read-only 75-story structure and dependency DAG audit>
rg -n 'validate_story_fixture|validate_story_completion|ready-for-dev|in-progress|approval' _bmad/bmm/workflows/4-implementation _bmad/bmm/workflows/4-implementation/sprint-planning tests
rg -n 'Set .*done|= "done"|→ done|Status to: "done"' _bmad/bmm/workflows/4-implementation --glob '*.xml' --glob '*.md'
```

Observed baseline checks: registry PASS (75 Stories / 150 rows), hermetic
regression script PASS, architecture contract gate PASS. Those green checks do
not exercise or close the four bypasses above.
