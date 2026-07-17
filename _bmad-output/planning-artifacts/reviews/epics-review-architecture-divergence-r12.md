---
reviewType: implementation-architecture-divergence
round: 12
targetCommit: 0e036d063dc34e5f615d3428326b76cc20b62a5b
targetArtifact: _bmad-output/planning-artifacts/epics.md
artifactSha256: a486aefe99151fad1b031a04ee6ee5803cf9797f5ad09c6b0af069e2d7a1e6dd
verdict: FAIL
findingCount: 3
reviewedAt: 2026-07-17
---

# R12 Implementation / Architecture Divergence Review

## Verdict

**FAIL — 3 findings.** The architecture corpus, limits, AD-1 through AD-25,
all 87 AD-11 rows, compatibility/release oracles, canonical registry, and
workflow entry gates are represented and the aggregate validator is green.
R11's equal-commit completion defect is rejected. The completion proof still
does not bind execution of the Story's owning oracles, predecessor ancestry is
not enforced against the dependent Story's approval, and the promised
hermetic mutation suite exercises only one oracle and one security mutation.

## Frozen review basis

- Commit: `0e036d063dc34e5f615d3428326b76cc20b62a5b`
- Canonical artifact digest:
  `a486aefe99151fad1b031a04ee6ee5803cf9797f5ad09c6b0af069e2d7a1e6dd`
- Acceptance-registry digest:
  `aefb83471a6f951c2e39046c73a69b20460baa2c012c6b474a1802ca70e46c08`
- Architecture authority: `ARCHITECTURE-SPINE.md`, AD-1 through AD-25 and
  its final corpora, limits, and acceptance matrices.
- Enforcement surfaces: Contracts C-01 through C-24, the 150-row registry,
  aggregate gate, approval/completion validators, mutation regression suite,
  and create-story/dev-story/sprint-planning workflows.

This was an independent read-only review of the settled target. Only this
review report was written.

## Read-only validation record

| Check | Result |
|---|---|
| `git rev-parse HEAD` | PASS — exact settled target |
| `bash tests/validate_architecture_contracts.sh` | PASS |
| `python3 tests/validate_planning_quarantine.py` | PASS — exact canonical discovery and retired quarantine |
| `python3 tests/validate_story_approval_regressions.py` | PASS as implemented, but incomplete; see R12-ARCH-03 |
| Compatibility replay | PASS — 90 inherited cases plus 4 approved deviations |
| Release oracle replay | PASS — reported crash cuts, chains, authorities, FD3/FD4 modes, FirstInstall, rollback, recovery, canonical encodings, and mutation classes |
| Acceptance registry | PASS — 75 Stories / 150 criterion-bound rows |
| AD and limit extraction | PASS — AD-1..AD-25 and ARCH-LIM-1..24 represented |
| AD-11 inventory | PASS — 87 current/future rows with owners, fixtures, assertions, and aggregate command |
| Multi-oracle approval cardinality | PASS — declared owners require exact ordered bindings |
| Strict distinct completion commits | PASS — approval, implementation, and completion commits must differ and be ordered |
| Completion oracle-result proof | FAIL — no result binding or execution evidence |
| Dependency temporal ancestry | FAIL — predecessor implementation is not compared with dependent approval |
| Hermetic security mutation coverage | FAIL — one-oracle positive path and one completion mutation only |

## Architecture decision and seam matrix

| Area | Result | Evidence |
|---|---|---|
| AD-1..AD-10 | PASS | Layer direction, declared/observed truth, ports, inference, snapshot, exact mutation, presentation, compatibility, and bounded concurrency are dependency ordered |
| AD-11 current corpus | PASS | Compatibility, contract, release, smoke, planning, registry, and regression commands return zero |
| AD-11 future corpus | FAIL | Story completion is not machine-bound to its declared oracle results and the security regression proof is incomplete |
| AD-12..AD-17 | PASS | Release identity, typed identity, terminal owner, privilege, SQLite truth, and Promise lifecycle are explicit |
| AD-18..AD-22 | PASS | Reconciliation, provenance, limits, frozen truth cut, FD3, and durable action handoff have assignable owners |
| AD-23..AD-25 | PASS | Quiesced release, canonical encodings, paired consumers, KnownGood, FirstInstall, FD4 recovery, and authenticated FD3 are covered |
| CommandRunner budget | PASS | Total budget and completion-driven concurrent scheduling are separate dependent Stories |
| SQLite durability | PASS | Schema, migration, backup, integrity, crash restart, CAS, retention, and invariants are explicit |
| Action lifecycle | PASS | Discovery/planning/confirmation and durable execution/shutdown/verification/outcome remain separated around one enum |
| Release/consumer migration | PASS | Two consumer pairs, ABI/toolchain evidence, rollback direction, recovery, FD3, and FD4 are represented |
| Approval/completion gate | FAIL | Approval cardinality is strict; completion result and dependency ancestry are not |

## Findings

### R12-ARCH-01 — Completion provenance does not bind owning-oracle execution or results

**Severity: blocking**

`srvls-story-completion-v1` contains only `storyId`, `approvalCommit`,
`implementationCommit`, and `verdict`. `validate_completion()` verifies commit
ordering and that approved fixture/expected bytes did not change, but it does
not execute any Story-declared owning oracle and the completion object contains
no per-oracle command/result/evidence hash. A distinct implementation commit
that changes an unrelated file can therefore be marked `completed`. The
dev-story prose says to run the full regression suite, but that unbound action
is not deterministic completion evidence and cannot prove the two canonical
P01/N01 rows or every multi-oracle owner passed against the implementation
commit. This diverges from AD-11 deterministic verification and C-23's claim
that dependents consume a “fully validated completion object.”

**Required closure:** extend completion provenance with an exact ordered result
binding for every declared oracle (command/runner identity, implementation
commit, result artifact hash, exit/result value, and criterion-row hashes), or
run those exact oracles hermetically in `--complete` at the bound implementation
tree. Reject missing, extra, reordered, stale, or failing results and cover a
valid multi-oracle completion plus each mutation.

### R12-ARCH-02 — A predecessor implementation need not be an ancestor of the dependent approval

**Severity: blocking**

`validate_assignment()` obtains the dependent Story's `approval_commit`, calls
`validate_completion()` for each declared dependency, and discards the returned
predecessor `implementationCommit`. It never requires that predecessor
implementation (or its completion commit) be an ancestor of the dependent
Story approval. A completion object brought in from a divergent history can be
present and internally ordered while the dependent fixtures were authored and
approved without that predecessor. This does not enforce C-23's “ancestor
implementation” rule and permits dependency-order divergence.

**Required closure:** for every direct dependency, require its implementation
and committed completion provenance to be ancestors of the dependent approval
commit (proper ancestry where identities differ). Add a divergent-branch or
cherry-picked completion mutation that must fail while the linear positive
chain continues to pass.

### R12-ARCH-03 — The hermetic regression suite does not meet its multi-oracle or mutation claim

**Severity: blocking**

`hermetic_git_gate()` builds one oracle binding, despite R11 requiring a valid
two-oracle approval/completion chain. It performs only one security mutation:
substituting `approvalCommit` for `implementationCommit`. It does not mutate
approval/completion schemas, criterion order/hashes, oracle cardinality/order,
fixture and expected hashes, path containment, dirty/untracked state,
reviewer/author identity, approval ancestry, result truth, approved-fixture
immutability, or predecessor ancestry. Static checks that Stories 6.7 and 7.12
parse to two owners do not execute multi-oracle validation. The aggregate's
`story approval regression mutations: PASS` therefore overstates the security
surface actually tested.

**Required closure:** make the hermetic positive control use at least two
ordered owning oracles and a dependent Story, then independently mutate every
security-relevant field and temporal edge in approval, completion, oracle
result, immutability, identity, and dependency enforcement. Each mutation must
be observed to fail closed through the public validator command.

## Final status

The settled target is not eligible for final/current promotion. Close all
three findings, settle a new digest, and rerun the three independent review
lanes.
