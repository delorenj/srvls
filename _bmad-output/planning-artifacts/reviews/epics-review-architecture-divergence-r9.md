---
reviewType: implementation-architecture-divergence
round: 9
targetCommit: 849e1a5952b31f32a96eccbc2851909a30982542
targetArtifact: _bmad-output/planning-artifacts/epics.md
verdict: FAIL
findingCount: 2
reviewedAt: 2026-07-17
---

# R9 Implementation / Architecture Divergence Review

## Verdict

**FAIL — 2 findings.** The backlog and its checked-in current architecture
oracles pass their aggregate read-only gates, and the coverage registry contains
all 25 architecture decisions and 87 declared AD-11 rows. However, the C-23
assignment gate is not total for stories with multiple owning oracles, and its
dependency check does not validate the predecessor approval it calls fully
validated. Both defects permit or force implementation behavior that diverges
from the backlog's own architecture contract.

## Frozen review basis

- Commit: `849e1a5952b31f32a96eccbc2851909a30982542`
- Architecture: `ARCHITECTURE-SPINE.md`, AD-1 through AD-25, including the
  complete current/future AD-11 acceptance obligations and AD-20 limits.
- Planning authority: canonical `epics.md`, its coverage JSON, Contracts C-01
  through C-24, and the 150-row story acceptance registry.
- Enforcement surfaces: architecture aggregate gate, C-23 validator,
  create-story, dev-story, and sprint-planning workflows.

No product implementation code or planning artifact was modified during this
review.

## Read-only validation record

| Check | Result |
|---|---|
| `git rev-parse HEAD` | PASS — exact target commit |
| `bash tests/validate_architecture_contracts.sh` | PASS |
| `python3 tests/validate_story_fixture_approvals.py` | PASS — 75 stories / 150 rows |
| `python3 tests/validate_planning_quarantine.py` | PASS |
| AD heading extraction | PASS — AD-1 through AD-25 exactly once and ordered |
| Coverage JSON inventory | PASS — 25 AD IDs, 24 limit IDs, 87 AD-11 rows |
| Workflow gate presence | PASS — create-story, dev-story, and sprint-planning invoke C-23 before promotion |
| Per-story oracle parser replay | FAIL — Stories 6.7 and 7.12 bind to later stories' oracles |
| Declared predecessor completion replay | FAIL — predecessor approval contents and current criterion binding are not validated |

## Findings

### R9-ARCH-01 — Multiple-oracle stories are validated against a later story's oracle

**Severity: blocking**

Stories 6.7 and 7.12 intentionally declare two owning oracles using the phrase
`The owning oracles are`. `declared_oracle()` recognizes only singular
`The owning oracle is` or the journey-specific `are owned by` form. Worse, its
story regex is unbounded: the `.*?` may cross the next `### Story` heading.
Consequently the gate does not fail closed. Direct replay returns:

```text
6.7 -> tests/fixtures/implementation/action-status-surface-v1
7.12 -> tests/fixtures/implementation/rollback-plan-v1/revision-zero.json
```

Those are the declared oracles for Stories 6.8 and 7.13, respectively. A valid
Story 6.7 approval using either of its real AD-11 owners
(`action-executor-v1` or `provider-privilege-environment-v1`) is therefore
rejected, while a fixture under the unrelated Story 6.8 oracle can satisfy the
path check. The same defect affects Story 7.12's success and FirstInstall
recovery owners. This contradicts Contract C-23's named-oracle binding and the
AD-11 registry rows `AD11-FUT-40`, `AD11-FUT-51`, `AD11-FUT-68`, and
`AD11-FUT-71`.

**Required closure:** parse only within the exact story section; represent one
or more declared oracle roots explicitly; require fixture and expected-result
paths to bind the correct approved oracle set; and add negative tests proving
that neither cross-story bleed nor an unrelated sibling oracle is accepted.

### R9-ARCH-02 — Dependency completion accepts an unvalidated predecessor approval

**Severity: blocking**

Contract C-23 says every dependent story requires a *fully validated*
completion object. `validate_assignment()` calls `validate_completion()` for
each declared predecessor, but `validate_completion()` only obtains the last
commit touching `<dependency>-v1.json` and compares that commit to the
completion object's `approvalCommit`. It does not validate the predecessor
approval's schema, story ID, row IDs, current criterion hashes, fixture hashes,
declared oracle containment, reviewer/author separation, or ancestry. Its
`rows` argument is unused.

Thus a malformed or stale predecessor approval can be committed, followed by a
syntactically valid completion object and descendant implementation commit;
the dependent story's assignment gate accepts it. This bypasses the exact
criterion/fixture/reviewer evidence that C-23 requires before production and
allows implementation order to proceed on evidence that no longer corresponds
to the canonical backlog.

**Required closure:** factor approval validation into a nonrecursive routine
and invoke it for every predecessor before validating the completion object;
then validate the predecessor's completion and implementation ancestry. Add
mutation tests for stale criterion hashes, wrong story/row IDs, wrong oracle,
changed fixture bytes, and non-independent reviewer identity on a dependency.

## Architecture divergence matrix

| Area | Result | Evidence |
|---|---|---|
| AD-1..AD-10 | PASS | Owners and dependency sequence are present; current aggregate is green |
| AD-11 current corpus | PASS | compatibility, contracts, release, smoke, quarantine, and registry gates pass |
| AD-11 future obligations | FAIL | Four future rows are not correctly enforceable because of R9-ARCH-01 |
| AD-12..AD-25 semantic ownership | PASS with blocking gate exception | Story boundaries and acceptance rows cover toolchain, identity, terminal, privilege, storage, lifecycle, reconciliation, configuration, limits, cuts, actions, release, codecs, and FD3 |
| C-23 assignment/dependency enforcement | FAIL | R9-ARCH-01 and R9-ARCH-02 |
| Planning discovery/quarantine | PASS | one canonical artifact and byte-exact retired archive behavior |

## Final status

This batch is not eligible for final/current promotion. Remediate both findings
and run a fresh independent three-lane review against one new settled digest.
