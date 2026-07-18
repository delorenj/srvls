---
reviewType: implementation-architecture-divergence
round: 11
targetCommit: 01e535cdbbcccccc3019e9a5fc6a26780a64b4c2
targetArtifact: _bmad-output/planning-artifacts/epics.md
artifactSha256: a486aefe99151fad1b031a04ee6ee5803cf9797f5ad09c6b0af069e2d7a1e6dd
verdict: FAIL
findingCount: 2
reviewedAt: 2026-07-17
---

# R11 Implementation / Architecture Divergence Review

## Verdict

**FAIL — 2 findings.** AD-1 through AD-25, the 87-row AD-11 inventory, the
current compatibility and release corpora, all 24 limits, and the aggregate
architecture command are represented and green. R10's multi-oracle
cardinality defect is repaired: approvals now require one ordered binding per
declared oracle. Completion provenance still admits a zero-change
"implementation," however, and the new regression gate does not execute a
valid approval or completion path or mutate their security-critical fields.

## Frozen review basis

- Commit: `01e535cdbbcccccc3019e9a5fc6a26780a64b4c2`
- Canonical artifact digest:
  `a486aefe99151fad1b031a04ee6ee5803cf9797f5ad09c6b0af069e2d7a1e6dd`
- Acceptance-registry digest:
  `aefb83471a6f951c2e39046c73a69b20460baa2c012c6b474a1802ca70e46c08`
- Architecture authority: `ARCHITECTURE-SPINE.md`, AD-1 through AD-25,
  including the final contract corpora, limits, and AD-11 matrices.
- Enforcement surfaces: Contracts C-01 through C-24, the 150-row acceptance
  registry, aggregate architecture gate, approval/completion validator,
  mutation regression script, and the three implementation workflows.

This was an independent read-only review of the settled target. Only this
review report was written.

## Read-only validation record

| Check | Result |
|---|---|
| `git rev-parse HEAD` | PASS — exact settled target |
| `bash tests/validate_architecture_contracts.sh` | PASS |
| Compatibility replay | PASS — 90 inherited cases plus 4 approved deviations |
| Contract fixtures | PASS |
| Release oracle replay | PASS — reported crash cuts, chains, authorities, traces, live FD3/FD4 modes, FirstInstall, rollback, CanonicalJsonV1, and mutation classes |
| Planning discovery/quarantine | PASS — one canonical artifact and byte-exact retired archive |
| Acceptance registry | PASS — 75 Stories / 150 criterion-bound rows |
| AD extraction | PASS — AD-1 through AD-25, 24 ARCH-LIM rows, and 87 AD-11 rows represented |
| Multi-oracle parser/cardinality | PASS — Stories 6.7 and 7.12 expose two ordered owners and `oracleBindings` requires exact owner order |
| Workflow entry gates | PASS — create-story, dev-story, and sprint-planning invoke C-23 before promotion; dev-story invokes `--complete` before review |
| Strict post-approval implementation proof | FAIL — approval and implementation commits may be identical |
| Approval/completion mutation regression | FAIL — no hermetic valid path and no security-field mutations |

## Architecture decision and seam matrix

| Area | Result | Evidence |
|---|---|---|
| AD-1..AD-10 | PASS | Dependency direction, declared/observed separation, ports, inference, snapshot, command, presentation, compatibility, and bounded-concurrency owners are ordered |
| AD-11 current corpus | PASS | Compatibility, contract, release, smoke, planning, registry, and regression commands all return zero |
| AD-11 future corpus | FAIL | C-23 completion truth and its regression proof remain non-strict; see R11-ARCH-01/02 |
| AD-12..AD-17 | PASS | Toolchain/release identity, exact identities, terminal owner, privilege boundary, SQLite truth, and Promise lifecycle are explicit |
| AD-18..AD-22 | PASS | Reconciliation, provenance, limits, frozen collection cut, FD3, and durable action handoff are independently assignable and dependency ordered |
| AD-23..AD-25 | PASS | Release transaction, canonical encodings, consumer pairs, KnownGood, FirstInstall, FD4, recovery, and authenticated FD3 obligations are owned |
| CommandRunner vs concurrent collection | PASS | Total process budget and completion-driven reservation scheduling are separate dependent Stories |
| SQLite durability and recovery | PASS | Initialization, schema/migration, CAS, backup, integrity, retention, crash recovery, and invariants have explicit owners |
| Action lifecycle | PASS | One enum feeds discovery/planning/confirmation; admission, execution, shutdown, verification, and outcome are separated |
| Release/consumer migration | PASS | Both consumer pairs, ABI/toolchain evidence, rollback direction, multi-pair recovery, FD3, and FD4 are represented |
| Multi-oracle approval | PASS | Exact ordered `oracleBindings` cardinality closes R10-ARCH-01 |
| Completion/CI enforcement | FAIL | Strict temporal implementation proof and executable mutation coverage remain open |

## Findings

### R11-ARCH-01 — Completion accepts the approval commit as the implementation commit

**Severity: blocking**

`validate_completion()` uses `git merge-base --is-ancestor` for both edges but
never requires distinct commits. Git treats a commit as its own ancestor.
Therefore a completion object with
`implementationCommit == approvalCommit` passes the first edge, and a later
completion commit passes the second. The approved fixture diff is naturally
empty. This records `completed` without any post-approval implementation
commit and contradicts C-23's ordered rule that production work is forbidden
until approval and that completion subsequently binds an implementation
commit. It also weakens the dependency-order gate because a dependent Story
can accept this zero-change completion as its predecessor evidence.

**Required closure:** require three strictly ordered, distinct commits:
`approvalCommit != implementationCommit != completionCommit`, approval is a
proper ancestor of implementation, and implementation is a proper ancestor of
completion. Add a regression mutation that substitutes the approval commit as
the implementation commit and proves rejection.

### R11-ARCH-02 — The regression gate does not exercise approval or completion semantics

**Severity: blocking**

`tests/validate_story_approval_regressions.py` statically checks registry
cardinality, two parser results, one `within_oracle()` false case, and workflow
text ordering. Its three subprocess negatives are only an invalid Story ID, a
missing approval, and a missing completion. It never constructs or validates
one successful multi-oracle approval or one successful completion. It never
mutates schema keys, row hashes/order, oracle cardinality/order, fixture and
expected hashes, dirty/untracked paths, reviewer/author identity, commit
ancestry, approved-fixture immutability, completion bindings, or predecessor
completion. Consequently the aggregate's printed `story approval regression
mutations: PASS` does not prove the enforcement paths whose regressions would
permit unauthorized assignment or false completion. R11-ARCH-01 is one such
escaping mutation.

**Required closure:** add a hermetic Git-history fixture with at least one
valid two-oracle approval, valid implementation, valid completion, and
dependent assignment. Starting from that positive control, mutate every
security-relevant schema, hash, identity, cardinality, ancestry,
immutability, and dependency edge and assert fail-closed behavior. Keep the
suite in `validate_architecture_contracts.sh`.

## Final status

The settled target is not eligible for final/current promotion. Repair both
completion enforcement gaps, settle a new digest, and rerun all three
independent review lanes.
