---
review: story-quality-dependencies
round: r11
sourceCommit: 01e535cdbbcccccc3019e9a5fc6a26780a64b4c2
reviewer: independent-read-only-story-review
verdict: FAIL
findingCount: 3
---

# R11 Story Quality and Dependency-Ordering Review

## Verdict

**FAIL — 3 findings.** The canonical backlog remains structurally complete and its declared Story dependency chain is sound, but two supported workflow paths still bypass the fail-closed assignment/status state machine. The new regression checker does not exercise those branches and therefore cannot supply the claimed non-mutation proof. This review changes only this report.

## Settled input and independence

- Reviewed immutable commit `01e535cdbbcccccc3019e9a5fc6a26780a64b4c2` in the dedicated R11 read-only review worktree.
- Scope included all 75 Story sections in `epics.md`, all 150 acceptance-registry rows, assignment and completion provenance validation, the regression checker, and create-story/dev-story/sprint-planning transition instructions.
- No prior verdict was accepted as evidence; commands and workflow control flow were inspected afresh.

## Evidence and checks performed

1. Parsed the canonical backlog and confirmed 75 Stories, each with a user-value statement, Implementation Boundary, Requirement Mapping, Dependencies, Validation Expectations, Out of Scope, and one positive plus one negative Given/When/Then criterion.
2. Checked the complete declared dependency order: Story 1.1 has no dependency and every subsequent Story names its immediate canonical predecessor. No forward edge, missing Story, or cycle was found.
3. Ran `python3 tests/validate_story_fixture_approvals.py`: PASS, 75 Stories and 150 criterion-bound rows.
4. Ran `python3 tests/validate_story_approval_regressions.py`: PASS as implemented, while separately auditing what its assertions actually cover.
5. Ran `python3 tests/validate_planning_quarantine.py`: PASS.
6. Ran `bash tests/validate_architecture_contracts.sh`: PASS, including the registry and regression checker.
7. Traced every create-story entry branch and dev-story status/sprint-status branch through their first filesystem or implementation effect.

## Findings

### R11-SQ-01 — Explicit create-story selection bypasses C-23 before writing

**Severity:** Critical  
**Evidence:** `_bmad/bmm/workflows/4-implementation/create-story/instructions.xml`, step 1. Both the initial user-provided story/path branch and the later prompt branches set identifiers and immediately `GOTO step 2a`. The C-23 command added at lines 91 and 150 exists only in the auto-discovery paths. Step 3 then emits the Story through multiple `template-output` operations.

**Impact:** Supplying a Story number or path—the workflow's documented supported interface—creates a `ready-for-dev` Story without an approval, without completed-predecessor evidence, and without the auto-discovery gate. This defeats the canonical pre-assignment contract and leaves the exact write-before-gate defect open on a different branch.

**Required remediation:** Centralize deterministic `story_id` derivation and the C-23 command in a single mandatory step reached by every selection mode, before step 2 analysis and before any output/status mutation. Reject a docs path that cannot resolve exactly one canonical Story ID. Add executable negative coverage for every explicit-selection branch and prove Story output and sprint status remain byte-identical after forced rejection.

### R11-SQ-02 — Dev-story permits implementation with no sprint status state machine

**Severity:** High  
**Evidence:** `_bmad/bmm/workflows/4-implementation/dev-story/instructions.xml`, step 4. When the sprint-status file does not exist, the workflow sets `current_sprint_status = "no-sprint-tracking"` and continues directly to step 5 implementation. No source status is established as `ready-for-dev` or `in-progress`; step 9 later explicitly supports moving the Story file to review without sprint tracking.

**Impact:** A caller-provided Story file can begin implementation and reach review without the canonical `backlog → ready-for-dev → in-progress → review` transition record. C-23 approval alone does not authorize that transition, so dependency/status ordering remains bypassable and concurrent consumers have no durable state to inspect.

**Required remediation:** For canonical srvls Stories, fail closed before implementation when sprint status is absent, the Story key is absent, or the status is unknown. Only `ready-for-dev` may enter `in-progress`, and only an already-`in-progress` Story may resume. Add executable negative cases for absent status file/key and for backlog, review, done, and unknown values.

### R11-SQ-03 — The regression checker is a string-presence check, not a workflow non-mutation proof

**Severity:** High  
**Evidence:** `tests/validate_story_approval_regressions.py`. Its create-story assertion compares only the first textual occurrence of `validate_story_fixture_approvals.py` with the first `template-output`; this passes while explicit-selection branches bypass that occurrence. Its workflow HALT assertion merely finds one `<action>HALT</action>` anywhere in each file. It neither drives selection/status branches nor snapshots Story and sprint-status bytes. It contains no assertions for absent sprint tracking, missing keys, backlog, review, done, unknown, or the `review_continuation` condition.

**Impact:** The architecture aggregate reports the regression suite PASS while the two bypasses above remain live. Subsequent instruction edits can also regress branch-local ordering without detection, so the checker is not evidence for fail-closed transition behavior.

**Required remediation:** Replace global substring checks with a deterministic workflow policy validator or executable harness that enumerates every supported selection/status branch. For every rejected branch, snapshot the Story path and sprint-status file before execution and assert absent/byte-identical state afterward. Include a positive case for `ready-for-dev` and an explicit resume case for `in-progress`; remove or precisely model `review_continuation` so it cannot make `review` eligible.

## Non-findings

- No missing required Story field, vague dependency declaration, forward dependency, cycle, or horizontal no-value epic was found.
- The 150-row registry is an exact inverse of the 75 Story acceptance pairs and binds criterion bytes by SHA-256.
- The approval validator itself checks declared oracles, tracked clean fixture bytes, recomputed hashes, distinct author/reviewer evidence, commit ancestry, predecessor completion, and approved-fixture immutability.
- Completion provenance is gated before the review-status update in dev-story; the remaining defects are earlier entry/status authorization paths.
- Sprint-planning's canonical discovery branch invokes C-23 before upgrading a discovered Story and gives invalidity precedence over status preservation.

## Acceptance condition for rerun

A later settled digest can pass this lane only after all Story-selection paths converge on one pre-effect C-23 gate, dev-story fails closed without a valid canonical sprint-status source state, and executable branch-complete regression evidence proves rejection causes no Story or sprint-status mutation. The full 75-Story/150-row and aggregate validations must continue to pass, followed by a fresh independent zero-finding review.
