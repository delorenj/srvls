---
reviewType: implementation-architecture-divergence
round: 20
targetCommit: 36dea34febf8ccd644708a4bc8f82140238690d0
targetArtifact: _bmad-output/planning-artifacts/epics.md
observedSha256: db1d24c8f4670d3fc72c54f3482a4cb644b57b33b086e128f66b2c2fdd21bcd2
verdict: FAIL
findingCount: 4
reviewedAt: 2026-07-17
reviewer: independent-r20-architecture-lane
---

# R20 Implementation / Architecture Divergence Review

## Verdict

**FAIL — 4 findings.** The architecture aggregate, all supplied contract and
release oracles, the 150-row acceptance registry, compatibility replay, and
planning quarantine pass at the settled digest. The R20 full-tree replay is a
material improvement over the synthetic per-file replay, but its reference
claim remains forgeable, it permits an implementation to replace an approved
runner, its new boundaries lack mutation evidence, and the status primitive is
not an atomic transition of the two authority surfaces used by the workflows.
PASS requires zero findings.

## Frozen basis and read-only checks

- Commit: `36dea34febf8ccd644708a4bc8f82140238690d0`
- Canonical artifact SHA-256:
  `db1d24c8f4670d3fc72c54f3482a4cb644b57b33b086e128f66b2c2fdd21bcd2`
- Architecture basis: `ARCHITECTURE-SPINE.md`, AD-1 through AD-25, the full
  AD-11 acceptance matrix, AD-20 limits, and final contract corpora.
- Enforcement basis: Contract C-23, assignment/completion validators, atomic
  status helper, workflow instructions, mutation suite, and aggregate gate.

| Command | Result |
|---|---|
| `git rev-parse HEAD` | PASS — exact settled commit |
| `bash tests/validate_architecture_contracts.sh` | PASS |
| `python3 tests/validate_planning_quarantine.py` | PASS |
| `python3 tests/validate_story_approval_regressions.py` | PASS |
| `git diff --check` | PASS |
| Compatibility replay/source pin/hash checks | PASS |
| Contract and release oracle replay/mutations | PASS |
| Exact Git-tree replay/reference trust boundary | FAIL — R20-ARCH-01 and R20-ARCH-02 |
| Replay/status mutation evidence | FAIL — R20-ARCH-03 |
| Atomic Story authority transition | FAIL — R20-ARCH-04 |

## Findings

### R20-ARCH-01 — Critical — Writable trace evidence does not prove consumption of the exact Git tree

The completion validator mounts the same-uid writable host directory at
`/trace`, asks `strace` to write `/trace/access`, and then accepts the test if
that text contains the substring `/work/implementation/`
(`tests/validate_story_fixture_approvals.py:291-308`). The approved runner and
its children can open, truncate, replace, or append that path while the trace
runs. Even without tampering, one metadata lookup or open of any path below the
tree satisfies the predicate; it does not establish that the observable result
was derived from the archived commit, nor that the files relevant to the
oracle were consumed. Pathname substring matching is also not an exact parsed
syscall/reference check.

Contract C-23 says the completion gate replays the complete exact commit and
requires its result. The current check proves only that some trace text contains
a prefix, so a runner that returns approved constant bytes after one irrelevant
`stat` can pass. That is not sufficient evidence for the exact compatibility,
codec, storage, action, and release boundaries owned by AD-9, AD-11, AD-16,
AD-18, AD-22, and AD-23.

**Required closure:** make reference evidence inaccessible to the runner
principal, parse exact normalized references, and bind the runner result to the
declared consumed Git objects; alternatively define an independently approved
runner protocol that emits a cryptographically verified consumption manifest.
Prove constant-output/irrelevant-touch and trace-forgery attempts fail.

### R20-ARCH-02 — Critical — Implementation may replace its independently approved runner

Assignment binds runner bytes at `fixtureAuthorCommit`, and replay correctly
executes those historical bytes. Completion immutability, however, compares
only `fixturePath` and `expectedResultPath` between approval and implementation
(`tests/validate_story_fixture_approvals.py:315-319`). It does not forbid a
change, deletion, mode change, or replacement of `runnerPath` in the
implementation commit. A story can therefore ship a weakened or malicious
checked-in oracle runner while completion passes by replaying the old runner
from the fixture-author commit.

This violates C-23's separation rule that implementation may not recapture or
update approved rows in the same change and creates divergent repository and
completion authorities for every AD-11 owning oracle.

**Required closure:** require runner path, bytes, Git object type, and mode to
remain identical from approval through implementation (or prohibit the
implementation diff from touching all approval-bound oracle assets). Add
delete, rename, mode, symlink, and byte-replacement mutations.

### R20-ARCH-03 — High — Green mutation tests do not exercise the new full-tree and status controls

The R20 remediation removed the implementation-manifest hash mutation and did
not replace it with full-tree archive mutations. The hermetic positive remains
a shell runner reading one root text file. There are no negative executions for
Git mode/symlink/type preservation, runner mutation, archive/path extraction,
writable-trace forgery, irrelevant tree access, no-access constant output,
result derivation, status CAS mismatch after a successful gate, illegal status
edges, or filesystem failure before rename. The status helper is tested only
with missing arguments.

The aggregate can consequently remain green if any new archive, trace, or CAS
predicate is removed or inverted. That is inadequate for Contract C-23 and the
AD-11 requirement that every acceptance obligation have executable positive
and negative evidence.

**Required closure:** add hermetic positive and independently failing mutation
cases for every new full-tree, reference, approval-asset immutability, and
status-transition predicate, including a representative multi-file Cargo
workspace replay. Require the complete suite from the aggregate architecture
gate.

### R20-ARCH-04 — Critical — The status helper is atomic for one YAML file, not for Story authority

`transition_story_status.py` locks, CAS-checks, fsyncs, and replaces only
`sprint-status.yaml`. The workflows continue to mutate the Story document
status separately: create-story sets `ready-for-dev` before invoking the YAML
transition, and dev-story sets Story status to `review` before invoking it
(`create-story/instructions.xml:320,335`;
`dev-story/instructions.xml:336-360`). A failed approval/completion gate, stale
YAML CAS, process crash, or filesystem error therefore leaves the Story file
and sprint status split. The helper also accepts every pair in the status set,
including unsupported skips and regressions, because it has no legal transition
matrix (`tests/transition_story_status.py:16,23-47`).

This does not close the R19 atomic-authority finding and lets assignment,
implementation, review, or done discovery observe contradictory state.

**Required closure:** designate one canonical status authority or atomically
CAS both Story and sprint surfaces under one pinned-evidence transaction, with
rollback/no-write behavior on every failure. Enforce the legal transition
graph and add executable crash/stale-evidence/gate-failure mutations asserting
both files remain byte-identical on rejection.

## Architecture divergence matrix

| Area | Result | Evidence |
|---|---|---|
| AD-1..AD-8 | PASS at backlog level | Ownership, lifecycle, storage, and collection mappings remain intact |
| AD-9 / AD-11 | FAIL | Approved runner can diverge from shipped runner; exact-tree result reference is not proven |
| AD-12..AD-15 | PASS at backlog level | Owners and acceptance rows are present; no additional semantic divergence found |
| AD-16 / AD-18 / AD-22 / AD-23 | FAIL at executable evidence boundary | Storage, reconciliation, codec, and release results rely on the deficient C-23 replay proof |
| AD-17, AD-19..AD-21, AD-24..AD-25 | PASS at backlog level | Contracts, limits, and story owners remain mapped |
| C-23 approval/dependency ancestry | PASS | Identity, criteria, oracle cardinality, and predecessor completion checks remain present |
| C-23 exact replay/reference | FAIL | R20-ARCH-01 and R20-ARCH-02 |
| Mutation evidence | FAIL | R20-ARCH-03 |
| Workflow status authority | FAIL | R20-ARCH-04 |
| Planning discovery/quarantine | PASS | Exact discovery and retired-artifact quarantine validate |

## Final status

The backlog is not eligible for final/current promotion at this digest. Close
all four findings and rerun all three independent review lanes on one new
settled commit.
