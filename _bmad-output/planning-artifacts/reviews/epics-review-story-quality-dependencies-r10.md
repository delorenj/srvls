---
review: story-quality-dependencies
round: r10
sourceCommit: 5b41e79d666bd667f4c444e835a30bfc9fb15fd2
reviewer: independent-read-only-story-review
verdict: FAIL
findingCount: 2
---

# R10 Story Quality and Dependency-Ordering Review

## Verdict

**FAIL — 2 findings.** The 75-story backlog and its 150-row acceptance registry are structurally complete, concrete, and linearly ordered, but two workflow paths still permit state or filesystem effects contrary to the fail-closed assignment contract. This report makes no changes outside this review file.

## Settled input and independence

- Reviewed immutable commit: `5b41e79d666bd667f4c444e835a30bfc9fb15fd2`.
- Scope: all 75 canonical Story sections in `epics.md`; all 150 rows in `story-acceptance-registry.json`; `tests/validate_story_fixture_approvals.py`; and the create-story, dev-story, and sprint-planning workflow instructions.
- Review was read-only with respect to the backlog, registry, validators, workflows, and product code.
- This is a fresh review; prior review conclusions were not accepted as evidence.

## Evidence and checks performed

1. Parsed exactly 75 `### Story E.S:` sections. Every Story contains a user-value statement, Implementation Boundary, Requirement Mapping, Dependencies, Validation Expectations, Out of Scope, and two Given/When/Then acceptance criteria.
2. Checked declared ordering across the entire sequence. Story 1.1 has no predecessor; each later Story declares its immediate canonical predecessor, yielding an acyclic dependency chain from 1.1 through 7.15 with no forward reference or missing Story ID.
3. Ran `python3 tests/validate_story_fixture_approvals.py`: PASS, reporting 75 stories and 150 canonical-criterion-bound rows.
4. Ran `python3 tests/validate_planning_quarantine.py`: PASS.
5. Ran `bash tests/validate_architecture_contracts.sh`: PASS, including compatibility, registry, release, machine-surface, and architecture aggregate checks.
6. Inspected assignment validation behavior: exact approval keys and schemas, canonical criterion hashes, tracked/clean fixture bytes, fixture/expected-result SHA-256 recomputation, oracle containment, distinct fixture-author/reviewer commits and Git identities, approval ancestry, predecessor completion provenance, implementation ancestry, and approved-fixture immutability.
7. Inspected all three transition workflows at the points that create a Story, derive `ready-for-dev`, enter `in-progress`, and enter `review`.

## Findings

### R10-SQ-01 — Create-story performs output writes before its fail-closed assignment gate

**Severity:** High  
**Evidence:** `_bmad/bmm/workflows/4-implementation/create-story/instructions.xml`, step 5. Multiple `<template-output file="{default_output_file}">` operations, including the final `story_completion_status`, occur before the command `python3 tests/validate_story_fixture_approvals.py {{story_id}}`. On a nonzero result the workflow says “Do not create … or save,” but the default output has already been incrementally written.

**Impact:** A missing/invalid approval or incomplete predecessor can leave a Story artifact on disk despite the contract that the Story must not be created or assigned until C-23 passes. Sprint-planning can subsequently discover that artifact, creating contradictory state and making failure non-atomic.

**Required remediation:** Move the C-23 command and its halt branch before the first output-producing `template-output` for the Story (after deterministic `story_id` derivation), or render exclusively to an explicitly disposable temporary artifact and prove deletion before halt. The nonzero path must leave no Story file and no sprint-status mutation. Add a workflow-level negative check that snapshots both paths/status before a forced gate failure and proves byte-identical state afterward.

### R10-SQ-02 — Dev-story explicitly continues implementation from an invalid status

**Severity:** High  
**Evidence:** `_bmad/bmm/workflows/4-implementation/dev-story/instructions.xml`, step 4. If current status is neither `ready-for-dev` nor `in-progress`, the workflow prints `Expected ready-for-dev or in-progress. Continuing anyway...` and does not halt. A caller can reach this through the explicitly supported user-provided story-file path, even when sprint status says `backlog`, `review`, or `done`.

**Impact:** Approval validity alone is not transition authorization. This path permits implementation to start outside the canonical dependency/status state machine, including reimplementation of a done Story or bypass of the ready-for-dev transition. It also leaves sprint status unchanged while work proceeds, so ordering is no longer machine-enforced.

**Required remediation:** Replace the “Continuing anyway” branch with a hard halt before implementation. Permit only `ready-for-dev` (transition to `in-progress`) or an explicit, already-`in-progress` resume. If review continuation is intended, define its exact source status and transition separately; it must not make arbitrary statuses eligible. Add negative workflow checks for `backlog`, `review`, `done`, unknown, and missing story-key states.

## Non-findings

- No missing Story section, required Story field, acceptance-polarity pair, or dependency declaration was found.
- No dependency cycle, forward dependency, or undeclared immediate predecessor was found.
- No horizontal epic without operator/Agent value was found; enabling work remains attached to the first value epic that consumes it.
- The central registry binds exactly the positive and negative criterion bytes for every Story, and the no-argument aggregate validates the complete row set.
- The approval validator fails closed for absent approvals and incomplete predecessor provenance; the defects are in workflow ordering/status authorization, not the validator's declared dependency traversal.
- Sprint-planning correctly derives a canonical Story ID and runs the C-23 gate before upgrading a discovered Story. Its prose precedence makes C-23 invalidity dominate preservation, despite the later general “never downgrade” shorthand.

## Acceptance condition for rerun

A subsequent settled digest may pass this lane only when both workflow defects are remediated, the workflow negative checks demonstrate no output/status mutation on failure, all 75 Story/150 registry checks still pass, and a fresh independent review reports zero findings.
