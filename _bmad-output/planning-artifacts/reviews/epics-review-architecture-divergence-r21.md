---
reviewType: implementation-architecture-divergence
round: 21
targetCommit: 80f1af3798db22cc678ce199be7deb8d034fff89
targetArtifact: _bmad-output/planning-artifacts/epics.md
observedSha256: db1d24c8f4670d3fc72c54f3482a4cb644b57b33b086e128f66b2c2fdd21bcd2
verdict: FAIL
findingCount: 4
reviewedAt: 2026-07-17
reviewer: independent-r21-architecture-lane
---

# R21 Implementation / Architecture Divergence Review

## Verdict

**FAIL — 4 findings.** The canonical requirement/AD inventories, aggregate
architecture gate, contract and release corpora, compatibility oracle, and
planning quarantine all pass at the settled digest. R21 also confirms that the
runner is now replayed as a static executable outside its own trace-evidence
principal and that approved runner paths are included in the implementation
immutability check. The remaining consumption predicate is nevertheless not a
result-reference proof, the corresponding boundaries still lack mutation
evidence, and the workflow/status changes continue to expose two authorities
and a non-rollback-safe failed transition. PASS requires zero findings.

## Frozen basis and read-only checks

- Commit: `80f1af3798db22cc678ce199be7deb8d034fff89`
- Canonical artifact SHA-256:
  `db1d24c8f4670d3fc72c54f3482a4cb644b57b33b086e128f66b2c2fdd21bcd2`
- Architecture basis: `ARCHITECTURE-SPINE.md`, AD-1 through AD-25, all 87
  AD-11 rows, AD-20 limits, and the final contract corpora.

| Command | Result |
|---|---|
| `git rev-parse HEAD` | PASS — exact settled commit |
| `bash tests/validate_architecture_contracts.sh` | PASS |
| `python3 tests/validate_planning_quarantine.py` | PASS |
| `python3 tests/validate_story_approval_regressions.py` | PASS |
| `git diff --check` | PASS |
| Compatibility and contract/release replay | PASS |
| Exact result-to-tree reference proof | FAIL — R21-ARCH-01 |
| Replay/immutability/status mutation evidence | FAIL — R21-ARCH-02 |
| Singular status authority | FAIL — R21-ARCH-03 |
| Rejected-transition atomicity | FAIL — R21-ARCH-04 |

## Findings

### R21-ARCH-01 — Critical — A path reference is still accepted as proof that the result derives from the exact tree

Moving `strace` outside the bubble prevents the runner from directly rewriting
the trace, but completion still accepts the first occurrence of the substring
`/work/implementation/` as sufficient consumption evidence
(`tests/validate_story_fixture_approvals.py:299-309`). The trace is neither
parsed as syscalls nor normalized and bound to declared Git objects. A static
runner can `stat` or open one irrelevant implementation path and then emit
constant approved bytes. That passes the current predicate without deriving
the observable result from the files relevant to its oracle. A single prefix
substring also does not demonstrate complete-tree, mode, link, rename, or
deletion consumption.

Contract C-23 requires the completion gate to replay the complete exact commit
and require its result. For AD-9/AD-11 and the codec, storage, reconciliation,
action, and release boundaries in AD-16, AD-18, AD-22, and AD-23, an irrelevant
lookup is not result-reference evidence.

**Required closure:** bind every runner to an independently approved,
machine-readable consumption manifest of exact normalized Git paths/object
IDs (including type and mode where material), validate the trace against that
manifest, and bind the result to those references; or use an equivalently
strong approved protocol. Prove both no-access constant output and
irrelevant-touch constant output fail.

### R21-ARCH-02 — High — The aggregate still has no mutations for the new trust boundaries

The regression suite's hermetic case is a one-file repository read by one
static C runner. Its mutations cover approval JSON fields and several older
completion fields, but none alters the approved runner after approval, changes
runner mode/type, deletes or renames it, substitutes a symlink, exercises a
multi-file Cargo tree, forges/omits/irrelevantly satisfies reference evidence,
or mutates archive modes/links/types. It also has no executable legal-edge,
stale-CAS, gate-failure, write/rename/fsync-failure, or two-authority status
mutation. Merely adding `runnerPath` to the final `git diff --quiet` loop and an
`EDGES` set is not mutation evidence that the aggregate fails when these
predicates are removed or inverted.

AD-11 requires positive and negative executable evidence for each acceptance
obligation. The current aggregate can remain green across regressions in the
new replay, approval-asset immutability, and status controls.

**Required closure:** add independently failing mutations for every listed
boundary, including a representative multi-file Cargo workspace, and require
the complete suite from `validate_architecture_contracts.sh`.

### R21-ARCH-03 — Critical — The workflows still publish a Story-file status before the claimed canonical status CAS

The create-story template unconditionally contains `Status: ready-for-dev`
(`create-story/template.md:3`). The workflow renders and saves that document
before invoking the sprint-status transition
(`create-story/instructions.xml:316-335`). Thus a failed approval recheck,
stale sprint CAS, process termination, or filesystem error can leave a
discoverable Story claiming `ready-for-dev` while the declared canonical entry
remains `backlog`. Dev-story still searches Story files for `ready-for-dev`
when sprint status is absent (`dev-story/instructions.xml:80-111`) and its
failure branches explicitly claim that the Story file was updated to `review`
(`dev-story/instructions.xml:365-372`). Code-review likewise saves the Story
file before its sprint transition and retains no-sprint and missing-key
success/fallback branches (`code-review/instructions.xml:185-220`).

The prose saying there is no second Story-file status does not remove the
second authority. These paths recreate the split-brain assignment and review
state that C-23 is intended to prevent.

**Required closure:** remove status from Story documents and every file-based
discovery/fallback path, or update both surfaces in one rollback-safe CAS
transaction. No workflow may save or report an advanced state before the
canonical transition succeeds.

### R21-ARCH-04 — High — A failed status helper can still leave the canonical file changed

`transition_story_status.py` writes and fsyncs a temporary file, calls
`os.replace`, and only then fsyncs the parent directory
(`tests/transition_story_status.py:61-69`). If directory open/fsync fails, the
command exits nonzero after the target has already changed; there is no saved
old inode, rollback, or recovery journal. Process death after replace has the
same ambiguous outcome. The workflow contract treats nonzero as rejection and
promises no write on failure, so this is a false rejection with durable or
potentially durable mutation. The regression suite exercises only missing
arguments and does not inject these cuts.

**Required closure:** implement a recoverable transition protocol (or define a
single append-only authority) whose reported failure leaves byte-identical
state or whose restart recovery deterministically completes/rolls back before
discovery. Add stale-evidence, gate-failure, pre-rename, post-rename, directory
fsync, and crash-cut tests.

## Architecture divergence matrix

| Area | Result | Evidence |
|---|---|---|
| AD-1..AD-8 | PASS at backlog level | Lifecycle, ownership, storage, and collection mappings remain present |
| AD-9 / AD-11 | FAIL | Exact result reference and required negative evidence remain incomplete |
| AD-12..AD-15 | PASS at backlog level | Owners and acceptance rows remain mapped |
| AD-16 / AD-18 / AD-22 / AD-23 | FAIL at executable evidence boundary | Their completion results inherit the deficient C-23 reference proof |
| AD-17, AD-19..AD-21, AD-24..AD-25 | PASS at backlog level | Contracts, limits, and owners remain mapped |
| C-23 approval/dependency ancestry | PASS | Criterion, oracle, identity, ancestry, and predecessor checks remain enforced |
| C-23 runner immutability predicate | PASS in implementation, unproven by mutation | Fixture, runner, and expected paths are now compared |
| C-23 replay/reference | FAIL | R21-ARCH-01 |
| Architecture mutation evidence | FAIL | R21-ARCH-02 |
| Workflow status authority and transition | FAIL | R21-ARCH-03 and R21-ARCH-04 |
| Planning discovery/quarantine | PASS | Exact discovery and retired-artifact quarantine validate |

## Final status

The backlog is not eligible for final/current promotion at this digest. Close
all four findings and rerun all three independent review lanes on one new
settled commit.
