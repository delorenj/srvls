---
reviewType: implementation-architecture-divergence
round: 13
targetCommit: a7f6e55918b036adf7db6f33191b4f7d2f6333f4
targetArtifact: _bmad-output/planning-artifacts/epics.md
artifactSha256: 872e3542d20c413344f9fb9acde74a8f1cac3cdff73ef32aa3762692b5bdf64f
verdict: FAIL
findingCount: 2
reviewedAt: 2026-07-17
---

# R13 Implementation / Architecture Divergence Review

## Verdict

**FAIL — 2 blocking findings.** AD-1 through AD-25, ARCH-LIM-1 through
ARCH-LIM-24, all 87 AD-11 rows, the final contract corpora, and the principal
story dependency order are represented. The aggregate, compatibility,
planning-quarantine, contract, release, acceptance-registry, and approval
regression commands return zero. R12's predecessor-ancestry defect is closed.
The new completion envelope, however, still does not prove that an oracle ran,
and its regression suite still does not exercise the fail-closed surface it is
supposed to protect.

## Frozen review basis

- Settled commit: `a7f6e55918b036adf7db6f33191b4f7d2f6333f4`
- Canonical artifact SHA-256:
  `872e3542d20c413344f9fb9acde74a8f1cac3cdff73ef32aa3762692b5bdf64f`
- Acceptance-registry SHA-256:
  `aefb83471a6f951c2e39046c73a69b20460baa2c012c6b474a1802ca70e46c08`
- Architecture authority: the final `ARCHITECTURE-SPINE.md`, AD-1 through
  AD-25, its limits, acceptance matrices, fixed corpora, and release/FD3/FD4
  authorities.

This was an independent read-only audit of the settled target. Only this
review report was written.

## Read-only validation record

| Check | Result |
|---|---|
| `git rev-parse HEAD` | PASS — exact settled commit |
| `bash tests/validate_architecture_contracts.sh` | PASS |
| `python3 tests/validate_story_approval_regressions.py` | PASS as implemented, but materially incomplete; see R13-ARCH-02 |
| `python3 tests/validate_planning_quarantine.py` | PASS — exact discovery/quarantine |
| Compatibility replay | PASS — 90 inherited plus 4 approved deviations |
| Contract and release oracle replay | PASS — fixed encodings, FD3/FD4, recovery, crash cuts, two-pair and mutation corpora reported green |
| Acceptance registry | PASS — 75 stories / 150 criterion-bound rows |
| AD and limit inventory | PASS — AD-1..25 and ARCH-LIM-1..24 |
| AD-11 inventory | PASS — 87 unique rows, 14 current and 73 future; unique fixture/assertion pairs and valid story owners |
| Multi-oracle approval cardinality | PASS — every declared oracle requires one ordered binding |
| Dependency ancestry | PASS — predecessor completion commit must precede the dependent approval, transitively binding predecessor implementation |
| Executed-oracle evidence | FAIL — result paths can be the approved expected files themselves |
| Security mutation coverage | FAIL — the public regression exercises only a small fraction of the validator's trust boundary |

## Architecture seam matrix

| Area | Result | Evidence |
|---|---|---|
| AD-1..AD-10 | PASS | Dependency direction, intent/observation split, ports, snapshot authority, exact mutation, presentation, compatibility, and bounded collection/action ownership are sequenced |
| AD-11 current corpus | PASS | Every currently checked-in aggregate component returns zero |
| AD-11 future acceptance | FAIL | Completion can be synthesized without executing an owning oracle; regression evidence does not cover its own acceptance boundary |
| AD-12..AD-17 | PASS | Toolchain/ABI, typed identity, terminal owner, privilege/environment, SQLite, and Runtime Promise semantics have explicit owners |
| AD-18..AD-22 | PASS | Reconciliation, provenance, limits, frozen cuts, FD3, action planning, handoff, and finalization remain separated |
| AD-23..AD-25 | PASS | Release recovery, two consumer pairs, KnownGood, FirstInstall, FD4, canonical bytes, and authenticated FD3 are explicitly owned |
| CommandRunner budgets | PASS | Per-child, per-scope, generation, total-budget, and completion-driven concurrency obligations are explicit |
| Dependency enforcement | PASS | Direct predecessor completion precedes dependent approval; transitive Git ancestry follows |
| Multi-oracle execution evidence | FAIL | Exact cardinality is enforced, but no command, exit status, runner identity, or independently produced output is bound |

## Findings

### R13-ARCH-01 — Completion provenance accepts copied expectations as “executed” results

**Severity: blocking**

`validate_completion()` requires one `oracleResults` entry per approved
binding, but an entry contains only `oraclePath`, `resultPath`, and
`resultSha256`. It checks that `resultSha256` equals the already approved
`expectedResultSha256` and that those bytes exist at `implementationCommit`.
It never executes `oraclePath`, binds a command/runner and exit status, or even
requires `resultPath` to differ from `expectedResultPath`. The hermetic positive
control demonstrates the bypass directly: every `resultPath` is set to
`tests/fixtures/story-v*/expected`. Thus an unrelated implementation commit can
copy/reference approved expected bytes and obtain a valid completion without
running either owning oracle. This contradicts C-23's “executed result” claim
and AD-11's deterministic implementation acceptance obligation.

**Required closure:** make `--complete` run every ordered declared oracle in a
clean checkout of the bound implementation commit and bind command/runner
identity, exit status, criterion hashes, and independently generated result
bytes, or define an equivalently tamper-evident execution-attestation format.
Reject a result path that aliases an approved input/expectation and reject
missing, extra, reordered, stale, nonzero, or unexecuted evidence. Include a
valid two-oracle execution and alias/copied-expectation negatives.

### R13-ARCH-02 — The approval regression gate does not cover its security boundary

**Severity: blocking**

`hermetic_git_gate()` now has a useful two-oracle positive chain and dependent
Story, but it performs only two runtime negative checks: making
`implementationCommit == approvalCommit` and supplying mismatched
author/committer identity. Static cardinality/path helper assertions are not
public-validator mutation tests. There are no independent mutations for exact
approval/completion keys, row order and criterion hashes, oracle
cardinality/order, traversal or symlink containment, fixture/expected byte
hashes, untracked/dirty state, declared author/reviewer ancestry, forged
approval commit, result cardinality/order/path/hash/exit truth, approved-byte
immutability, completion ancestry, or divergent predecessor ancestry. The
aggregate therefore prints `story approval regression mutations: PASS` without
regression evidence for most of the machine-enforced boundary, including the
new completion/result and dependency code.

**Required closure:** turn each security-relevant approval, completion,
oracle-result, identity, cleanliness, immutability, and temporal edge into an
isolated hermetic mutation invoked through the public validator command. Keep
the two-oracle dependent positive control, prove every mutation fails for the
intended invariant, and include the execution-evidence mutations required by
R13-ARCH-01.

## Final status

The settled target is not eligible for final/current promotion. Close both
findings, settle a new digest, and rerun all three independent review lanes.
