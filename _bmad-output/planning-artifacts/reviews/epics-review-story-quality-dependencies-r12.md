---
review: story-quality-dependencies
round: r12
sourceCommit: 0e036d063dc34e5f615d3428326b76cc20b62a5b
reviewer: independent-read-only-story-review
verdict: FAIL
findingCount: 4
---

# R12 Story Quality and Dependency-Ordering Review

## Verdict

**FAIL — 4 findings.** The 75 Story definitions, 150-row acceptance registry, declared dependency chain, and approval/completion provenance validator are internally sound. The supported workflow control flow is not: explicit Story creation still writes without a valid canonical source-state transition, review continuation mutates an invalid state before rejecting it, sprint regeneration can preserve completion states without completion provenance, and the regression suite does not exercise any of those workflow branches. This review changes only this report.

## Settled input and independence

- Reviewed immutable commit `0e036d063dc34e5f615d3428326b76cc20b62a5b` in the dedicated R12 review worktree.
- Inspected all 75 Story sections, all 150 registry rows, dependency declarations, approval and completion validation, create-story/dev-story/sprint-planning branches, and the regression checker's actual executed assertions.
- Re-ran the canonical registry, regression, quarantine, architecture-contract, release, and compatibility gates. They all report PASS as implemented; the findings below identify behavior those gates do not cover.

## Checks and non-findings

1. `python3 tests/validate_story_fixture_approvals.py` passed with exactly 75 Stories and 150 criterion-bound rows.
2. `python3 tests/validate_story_approval_regressions.py` passed, including its hermetic Git approval/completion/dependency chain.
3. `python3 tests/validate_planning_quarantine.py` and `bash tests/validate_architecture_contracts.sh` passed.
4. Every Story has the required value statement, implementation boundary, mappings, explicit dependency, validation expectation, out-of-scope declaration, and positive/negative Given/When/Then rows.
5. Story 1.1 is the sole root; every later Story declares its immediate canonical predecessor. No missing target, forward edge, or dependency cycle was found.
6. The registry is an exact inverse of the Story acceptance pairs and binds their criterion bytes by SHA-256. The approval validator checks declared oracles, tracked clean fixture bytes, hashes, reviewer separation, commit ancestry, predecessor completion, and post-approval fixture immutability.

## Findings

### R12-SQ-01 — Explicit create-story selection writes before proving a legal backlog transition

**Severity:** Critical  
**Evidence:** `_bmad/bmm/workflows/4-implementation/create-story/instructions.xml`, steps 1, 5, and 6. A caller-provided Story number/path runs C-23 and jumps directly to artifact generation. Step 5 sets and emits `ready-for-dev`; step 6 saves the Story **unconditionally**, then merely says to verify the sprint entry is `backlog` before updating it. There is no pre-write requirement that a sprint-status file and exact Story key exist, no check/HALT for a missing key or non-backlog status, and the no-sprint-status prompt explicitly supports creating a Story anyway.

**Impact:** A valid approval for an already `in-progress`, `review`, or `done` Story—or for a Story absent from canonical sprint tracking—allows the Story artifact to be overwritten and marked `ready-for-dev` before the workflow discovers any invalid source state. This bypasses the canonical state machine and cannot provide rejection non-mutation.

**Required remediation:** Before any template output or Story save, converge every explicit and automatic selection mode on one gate that requires the canonical sprint-status file, the exact canonical key, and source status `backlog`, then runs C-23. Any missing/ambiguous key, absent status authority, or other source status must HALT with Story and sprint-status bytes unchanged. Re-check the same source state atomically at the update boundary.

### R12-SQ-02 — Review continuation mutates `review` to `in-progress` and then rejects it

**Severity:** Critical  
**Evidence:** `_bmad/bmm/workflows/4-implementation/dev-story/instructions.xml`, step 4. The first branch updates status when `current status == 'ready-for-dev' OR review_continuation == true`. Therefore a code-review continuation whose current status is `review` is written to `in-progress`. The later branch tests the original/current status and HALTs because it is neither `ready-for-dev` nor `in-progress`.

**Impact:** The rejected `review` branch mutates sprint status before HALT. It also conflicts directly with the documented rule that only `ready-for-dev` may start and only `in-progress` may resume. Depending on variable refresh semantics it either rejects after mutation or improperly authorizes review re-entry; neither is fail closed.

**Required remediation:** Remove `review_continuation` from transition authorization. Evaluate exactly one source-state decision before mutation: `ready-for-dev` may transition, `in-progress` may resume without mutation, and every other/missing state must HALT byte-identically. If review remediation is supported, define a separate explicit `review → in-progress` contract and provenance gate rather than smuggling it through the start transition.

### R12-SQ-03 — Sprint regeneration preserves `review`/`done` without completion provenance

**Severity:** High  
**Evidence:** `_bmad/bmm/workflows/4-implementation/sprint-planning/instructions.md`, step 3 preservation rule. For every existing Story file it runs only assignment-mode `validate_story_fixture_approvals.py <story_id>`. If that passes, it preserves any more advanced existing state, including `review` and `done`. It never runs `--complete <story_id>` before preserving a completion-bearing state.

**Impact:** A stale or manually edited sprint-status file can retain `review` or `done` based solely on pre-assignment approval and predecessor completion. The implementation commit, approval-to-implementation ancestry, completion commit, and approved-fixture immutability required by the durable completion gate are never proved.

**Required remediation:** During preservation, require assignment validation for `ready-for-dev`/`in-progress` and completion validation for `review`/`done`; force invalid advanced states to the last provable state or fail regeneration without mutation. Add explicit tests for absent, malformed, stale, and valid completion provenance.

### R12-SQ-04 — Regression evidence does not execute or model workflow branches

**Severity:** High  
**Evidence:** `tests/validate_story_approval_regressions.py`. The new hermetic test executes validator functions, not create-story, dev-story, or sprint-planning transition policy. Workflow assertions remain global substring/order checks: first approval-command occurrence before first template output, one HALT token in each file, and a preservation-rule phrase. There are no branch cases for explicit number/path, absent sprint authority, missing key, non-backlog create states, `review_continuation`, or completion-blind advanced preservation; no Story/sprint byte snapshots are compared.

**Impact:** The aggregate gate reports PASS while R12-SQ-01 through R12-SQ-03 remain present. Text can satisfy the checker even when another supported control-flow branch writes first or preserves an unauthorized state.

**Required remediation:** Extract a deterministic transition-policy helper used by the workflows or build an executable workflow-policy harness. Enumerate every selection and source-state branch. For each rejection, snapshot Story and sprint-status paths and assert absent/byte-identical results. Include positive `backlog → ready-for-dev`, `ready-for-dev → in-progress`, no-op `in-progress` resume, completion-proven `in-progress → review`/advanced preservation, and negative absent/missing/backlog-review-done-unknown cases.

## Acceptance condition for rerun

A later settled digest can pass this lane only when every create/start/resume/preserve/completion branch uses one fail-closed state policy before effects, rejection is proven byte-non-mutating, and branch-complete executable regression evidence covers all supported inputs. The full 75-Story/150-row, dependency, quarantine, and architecture aggregates must remain green, followed by a fresh independent zero-finding review.
