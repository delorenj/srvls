---
review: story-quality-dependency-ordering
round: r9
artifactCommit: 849e1a5952b31f32a96eccbc2851909a30982542
verdict: FAIL
findingCount: 5
reviewer: independent-r9-story
---

# R9 Story Quality and Dependency-Ordering Review

## Verdict

**FAIL — 5 findings.** The 75 story blocks and all 150 acceptance rows are
present, ordered, and registry-bound, and the aggregate architecture gate
passes. The pre-assignment mechanism is nevertheless bypassable and, for
several stories, cannot bind the oracle declared by the story. These are
assignment-blocking defects rather than editorial observations.

## Review scope and method

The review inspected every Story 1.1 through 7.15 for user-value statement,
implementation boundary, mapped IDs, earlier-only dependency, validation
oracle, exclusions, and the positive/negative GWT pair. It also inspected all
150 rows in `story-acceptance-registry.json`, Contract C-23, the complete
`validate_story_fixture_approvals.py` implementation, and the create-story,
dev-story, and sprint-planning transition instructions. The following commands
were run from the review worktree at the pinned commit:

```text
python3 tests/validate_story_fixture_approvals.py
bash tests/validate_architecture_contracts.sh
rg -n '^### Story|^#### (Implementation Boundary|Acceptance Criteria|Requirement Mapping|Dependencies|Validation Expectations|Out of Scope)' _bmad-output/planning-artifacts/epics.md
rg -n 'validate_story_fixture_approvals|ready-for-dev|in-progress|HALT' _bmad/bmm/workflows/4-implementation tests/validate_story_fixture_approvals.py
```

Both no-argument validators pass, but neither exercises a real per-story
approval or completion chain. Findings below were confirmed against the
transition code paths themselves.

## Findings

### R9-SQ-01 — Critical — Oracle parsing crosses story boundaries and cannot represent declared multi-oracle stories

`declared_oracle()` searches with `re.DOTALL` but does not stop at the next
`### Story` heading. It recognizes only singular phrases (`The owning oracle
is` or the special journey wording), while Stories 6.7 and 7.12 explicitly say
`The owning oracles are ... and ...`. Consequently validation for Story 6.7
silently crosses into Story 6.8 and returns
`tests/fixtures/implementation/action-status-surface-v1`; Story 7.12 crosses
into Story 7.13 and returns
`tests/fixtures/implementation/rollback-plan-v1/revision-zero.json`. An
approval can therefore pass while binding the next story's oracle and none of
the reviewed story's declared evidence.

The same single-path model cannot faithfully bind Stories 1.1 and 1.2, whose
validation expectations name two artifacts/commands. For example Story 1.2 is
parsed as the literal nonexistent path
`tests/compat/manifest.json and tests/compat/SHA256SUMS`. Story 6.7 needs both
executor and privilege-environment corpora, but the approval schema exposes
only one `fixturePath` and one `expectedResultPath`.

**Required remediation:** parse only the selected story block; represent and
validate the complete ordered oracle set (or designate one real manifest that
cryptographically binds the set); add positive assignment tests for every
singular and plural declaration plus a negative test proving the parser cannot
cross a story heading.

### R9-SQ-02 — High — File-valued owning oracles collapse fixture input and expected result into the same file

For both `fixturePath` and `expectedResultPath`, the validator requires the
path to equal the parsed oracle or be beneath `oracle + "/"`. When the declared
oracle is a file—such as Story 1.3 `tests/compat/validate.sh`, Story 1.4
`tests/fixtures/contracts/validate.py`, Story 7.1
`stable-toolchain-evidence.json`, and multiple release JSON/JSONL stories—the
only satisfiable value for both fields is that same file. Thus the approval can
claim the executable validator (or one input JSON) is simultaneously the
fixture and expected result. This does not establish the independent exact
input/expected-byte pair promised by Contract C-23, and makes meaningful
approval impossible without lying about one field.

**Required remediation:** give every story an explicit fixture root/manifest
and independently addressable expected result, or revise the schema to bind
typed input and expected-output sets. Reject identical input/output paths where
the criterion does not explicitly define an identity transform. Exercise these
rules with real approval fixtures in CI.

### R9-SQ-03 — Critical — A dependent story does not validate its predecessor's C-23 approval

`validate_assignment()` loops over declared predecessors but calls only
`validate_completion(dependency, rows)`. `validate_completion()` never parses
or validates the predecessor approval JSON: it does not check its schema,
row IDs, current criterion hashes, verdict, oracle paths/hashes, author/reviewer
identities, or ancestry evidence. It merely obtains the last commit touching
that path and accepts a completion JSON naming it. A malformed, rejected, or
stale predecessor approval plus a syntactically valid completion file therefore
unlocks the next story. This defeats both dependency ordering and the stated
rule that every dependent Story requires a “fully validated completion
object.”

**Required remediation:** validation of a predecessor completion must first
run the full approval validation for that predecessor, without recursively
requiring its assignment-time dependencies twice, then validate completion
provenance and implementation ancestry. Add mutations for stale criterion
hash, rejected verdict, wrong oracle, same reviewer/author, and malformed
approval on a completed predecessor.

### R9-SQ-04 — High — Reviewer independence is asserted by an unrelated historical commit, not review evidence

The approval's `reviewerCommit` is accepted when it is any commit object with a
different author email from `fixtureAuthorCommit` and is an ancestor of the
approval commit. No reviewed artifact, approval payload, criterion hashes,
fixture hashes, or verdict must exist in that commit. Any old repository commit
from another email can be supplied as `reviewerCommit`, allowing the fixture
author to write and commit the approval alone while passing the “independent
reviewer” gate. Distinct email strings are also not proof of distinct
principals.

**Required remediation:** require independently authored review evidence that
binds the story ID, current criterion hashes, fixture/expected hashes, and
approved verdict, and require the final approval to incorporate that exact
evidence. Add a negative test using an unrelated historical commit and another
using two emails controlled by the same approval author under the chosen
identity policy.

### R9-SQ-05 — Critical — Workflow failure branches do not halt, and sprint planning preserves invalid advanced states

The create-story and dev-story C-23 failure checks print `STOP` and say not to
change status, but contain no `<action>HALT</action>`/HALT condition. Execution
then continues to unconditional status-writing actions: create-story Step 6
“Save story document unconditionally” and sets `ready-for-dev`; dev-story
continues into the status checks and permits `in-progress`. Other workflow
branches use explicit `HALT`, demonstrating that output text alone is not the
workflow stop primitive.

Sprint planning adds a second bypass: detection says a failing C-23 command
retains `backlog`, but the immediately following preservation rule says an
existing more advanced status is never downgraded. An invalid or removed
approval therefore leaves an existing `ready-for-dev`, `in-progress`,
`review`, or `done` state discoverable and assignable.

**Required remediation:** add explicit HALT actions before every subsequent
save/status transition on a nonzero C-23 exit; make C-23 validity a dominant
invariant over status preservation; and add executable transition tests proving
failure cannot create or preserve assignable states in all three workflows.

## Story-set quality and ordering observations

Apart from the blocking gate defects above, all 75 stories have the required
seven structural fields, exactly two canonical acceptance rows, and explicit
earlier-only dependencies. The sequence closes the Rust/bootstrap,
Promise/Lease/Heartbeat, five-provider discovery including direct processes,
reconciliation/baseline/Brief, TUI start/navigation, separated action
planning/execution/verification, and release/FirstInstall/rollback seams. No
additional story-content or forward-dependency finding is reported in this
round.

## Acceptance condition for rerun

A rerun may PASS only when the five defects are remediated, real per-story
fixtures prove the singular/multi-oracle and file-oracle cases, dependency
mutation tests prove predecessor approvals are revalidated, reviewer evidence
is content-bound, and workflow transition tests prove a failed C-23 gate cannot
produce or preserve an assignable state.
