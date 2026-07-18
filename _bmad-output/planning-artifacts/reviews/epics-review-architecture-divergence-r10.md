---
reviewType: implementation-architecture-divergence
round: 10
targetCommit: 5b41e79d666bd667f4c444e835a30bfc9fb15fd2
targetArtifact: _bmad-output/planning-artifacts/epics.md
artifactSha256: 6fc43377b3ba19fc6ee656fa6e4e00e3366f41a4ee244ee86ab0125e195a4f53
verdict: FAIL
findingCount: 2
reviewedAt: 2026-07-17
---

# R10 Implementation / Architecture Divergence Review

## Verdict

**FAIL — 2 findings.** The architecture aggregate, compatibility corpus,
release oracles, planning quarantine, and 150-row acceptance registry all pass.
The R9 cross-story parser and predecessor-validation defects are repaired.
However, C-23 still cannot bind all declared owning oracles for a multi-oracle
Story, and CI does not execute the approval/completion code paths whose
correctness controls assignment and dependency order.

## Frozen review basis

- Commit: `5b41e79d666bd667f4c444e835a30bfc9fb15fd2`
- Canonical artifact digest:
  `6fc43377b3ba19fc6ee656fa6e4e00e3366f41a4ee244ee86ab0125e195a4f53`
- Acceptance-registry digest:
  `aefb83471a6f951c2e39046c73a69b20460baa2c012c6b474a1802ca70e46c08`
- Architecture authority: `ARCHITECTURE-SPINE.md`, AD-1 through AD-25,
  including AD-11's current/future acceptance corpus and AD-20 limits.
- Enforcement surfaces: Contracts C-01 through C-24, the 150-row registry,
  `validate_architecture_contracts.sh`, the C-23 validator, and create-story,
  dev-story, and sprint-planning gates.

This was a read-only review of the settled target. No product code or planning
authority was changed.

## Read-only validation record

| Check | Result |
|---|---|
| `git rev-parse HEAD` | PASS — exact target commit |
| `bash tests/validate_architecture_contracts.sh` | PASS |
| `python3 tests/validate_story_fixture_approvals.py` | PASS — 75 Stories / 150 canonical rows |
| Compatibility replay | PASS — 90 inherited cases plus 4 approved deviations |
| Release oracle replay | PASS — all reported chains, cuts, bindings, and mutation classes |
| Planning discovery/quarantine | PASS — one canonical artifact and byte-exact retired archive |
| AD extraction and registry inspection | PASS — AD-1 through AD-25, 24 limits, and 87 AD-11 rows are represented |
| Workflow inspection | PASS — all three workflow surfaces call C-23 before status promotion; dev-story also calls completion validation before review |
| R9 cross-story parser replay | PASS — Story sections are bounded and Stories 6.7 / 7.12 return their own two oracle roots |
| R9 predecessor-validation replay | PASS — predecessor completion now invokes full predecessor approval validation and checks implementation/completion ancestry |
| Multi-oracle approval cardinality | FAIL — one approval path pair may satisfy any one declared oracle while leaving the other unbound |
| Approval/completion mutation coverage in aggregate CI | FAIL — aggregate invokes only the registry-only no-argument branch |

## Architecture decision and seam matrix

| Area | Result | Evidence |
|---|---|---|
| AD-1..AD-10 | PASS | Bootstrap, boundaries, compatibility, reconciliation, CLI/TUI, action planning, and provider admission have ordered Story owners and green current gates |
| AD-11 current corpus | PASS | Compatibility, contract, release, smoke, registry, and quarantine commands all pass |
| AD-11 future corpus | FAIL | The four multi-oracle obligations attached to Stories 6.7 and 7.12 are not all approval-bound; see R10-ARCH-01 |
| AD-12..AD-17 | PASS | Stable toolchain, canonical identity, terminal ownership, privilege boundaries, SQLite, and Lease semantics are explicitly owned |
| AD-18..AD-22 | PASS | Reconciliation, configuration, exact limits, collection cuts/FD3, and action persistence/execution are dependency ordered |
| AD-23..AD-25 | PASS | Release authority, canonical codecs, FD3/FD4 precedence, FirstInstall, KnownGood, rollback, and recovery semantics are represented and their current oracles pass |
| CommandRunner / concurrent collection | PASS | Read-only runner budget and separate collection reservation/deadline ownership are split before provider work |
| SQLite durability / crash recovery | PASS | Schema, migration, backup, integrity, repositories, retention, CAS, and recovery boundaries are separately assignable |
| Action discovery through outcome | PASS | One enum feeds discovery/planning/confirmation; durable admission/execution/shutdown/verification/outcome are separate dependent Stories |
| Release consumer migration | PASS | Both managed pairs, FirstInstall, FD3/FD4, ABI/toolchain evidence, KnownGood, rollback, and multi-pair recovery are explicit |
| C-23 assignment/dependency gate | FAIL | Cardinality and CI-path defects below prevent a total fail-closed proof |

## Findings

### R10-ARCH-01 — Multi-oracle Stories require all owners but C-23 binds only one

**Severity: blocking**

Stories 6.7 and 7.12 each declare two owning oracles. The R9 remediation now
parses both correctly, but `srvls-fixture-approval-v1` still contains only one
`fixturePath` and one `expectedResultPath`. `validate_approval()` accepts each
path when it is within **any** declared oracle:

```python
if not any(within_oracle(data["fixturePath"], oracle) for oracle in oracles):
    fail(...)
```

There is no coverage or cardinality check requiring every declared oracle to be
bound. Therefore a Story 6.7 approval can bind only `action-executor-v1` and
omit `provider-privilege-environment-v1`; a Story 7.12 approval can bind only
`first-install-success-v1` and omit the architecture-native recovery trace (or
vice versa). Both ordered row hashes may still be present and the approval will
pass. This leaves AD-11 rows `AD11-FUT-40`, `AD11-FUT-51`, `AD11-FUT-68`, and
`AD11-FUT-71` without a total pre-assignment evidence binding.

**Required closure:** make the approval schema cardinality match the declared
oracle set (for example, an ordered exact `oracleBindings` array with fixture
and expected-result hashes per owner), or give each Story one declared bundle
oracle that contains and hashes all required evidence. Fail on missing, extra,
duplicate, or cross-owner bindings, and keep criterion-row order explicit.

### R10-ARCH-02 — Aggregate CI never exercises approval or completion validation

**Severity: blocking**

`tests/validate_architecture_contracts.sh` invokes
`python3 tests/validate_story_fixture_approvals.py` with no Story argument. That
branch validates only the canonical 150-row registry and returns before
`validate_approval()`, `validate_assignment()`, or `validate_completion()`.
No other checked-in test invokes the validator with a Story or `--complete`.
Consequently CI cannot detect regressions in schema exactness, oracle
containment, file hashes, Git identity/ancestry, approved-fixture immutability,
completion provenance, or predecessor enforcement. The R9 fixes themselves
have no executable regression proof in the aggregate architecture gate.

This diverges from the backlog's claim that architecture-boundary CI and the
C-23 workflow gates fail closed before implementation. A workflow command is
not sufficient evidence when the command's enforcement paths are never tested.

**Required closure:** add hermetic positive and negative tests for assignment
and completion using a temporary Git repository or committed immutable test
history. Cover wrong/extra keys, stale row hashes, every multi-oracle
cardinality mutation, changed/untracked fixture bytes, wrong author/reviewer,
non-ancestor commits, altered approved fixtures, stale predecessor approval,
and missing/non-ancestor completion. Invoke that suite from
`validate_architecture_contracts.sh`.

## Final status

The target is not eligible for final/current promotion. Remediate both
findings, settle a new digest, and rerun all three independent review lanes.
