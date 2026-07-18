---
reviewType: story-quality-dependency-ordering
round: r18
subjectCommit: 4eefc21ff6f56b04aae9463a98b79cefca58938f
verdict: FAIL
findingCount: 3
reviewer: independent-r18-story-lane
---

# R18 Story Quality and Dependency Review

## Verdict

**FAIL — 3 findings.** All 75 stories, the canonical-reference grammar, the
declared dependency graph, every implementation status mutation, and the C-23
multi-file completion sandbox were audited at the settled subject commit. The
repository gates pass, but the completion proof still does not bind or execute
a complete ordinary Rust workspace, role-aliasing remains accepted, and the
workflow mutations remain vulnerable to stale validation.

## Scope and evidence

- Audited the 75 canonical Story sections and their 150 acceptance rows.
- Checked every declared predecessor reference and the validator's singular,
  plural, and same-Epic range grammar.
- Inspected create-story, dev-story, code-review, sprint-planning, and
  sprint-status transition instructions.
- Inspected C-23 approval/completion replay and its hermetic regression suite.
- Ran `python3 tests/validate_story_fixture_approvals.py`,
  `python3 tests/validate_story_approval_regressions.py`, and
  `bash tests/validate_architecture_contracts.sh`; all pass at the subject
  commit. These checks do not exercise the missing cases below.

## Findings

### R18-SQ-01 — Critical — Multi-file completion is still a caller-selected partial tree, not the implementation commit

The completion object supplies an arbitrary nonempty `implementationFiles`
list independently for each oracle. Validation checks that at least one listed
file changed, but never compares the manifest with the complete Git diff from
approval to implementation, never requires every oracle to receive the same
manifest, and never materializes the implementation commit's full repository
tree (`tests/validate_story_fixture_approvals.py:268-293`). Thus a completion
may omit a changed sibling, manifest, migration, build script, lockfile, or
test-support file and replay a favorable subset. The sandbox also exposes only
that subset plus `/usr`, `/bin`, and libraries; it does not provide the exact
Cargo workspace or an immutable dependency/toolchain input capable of running
the ordinary multi-file Rust stories. The regression's purported positive
case remains one root-level file named `implementation` read by a shell script
(`tests/validate_story_approval_regressions.py:102-139`), and it has no
multi-file Cargo build, omitted-sibling, extra-changed-file, or per-oracle
manifest-divergence mutation.

**Required remediation:** derive one canonical manifest from the complete
approval-to-implementation Git change set (including additions, modifications,
deletions, and modes), require it identically for every oracle, and replay from
a read-only materialization of the exact implementation commit with separately
writable scratch/home and immutable toolchain/dependency inputs. Add a genuine
multi-file Cargo workspace completion plus mutations for omitted/substituted
siblings, undeclared changed files, deletions/modes, and divergent per-oracle
manifests.

### R18-SQ-02 — High — Distinct path strings do not provide independent oracle roles

The R17 remediation only requires the fixture, runner, and expected-result
paths to differ. It does not reject byte aliases, hard-link-equivalent Git
blobs, a runner whose approved bytes equal an input/expectation, or otherwise
prove typed role independence (`tests/validate_story_fixture_approvals.py:174-190`).
The regression suite still contains no fixture/runner/expectation path-alias or
byte-alias mutation. Consequently three differently named paths can bind the
same approved evidence and satisfy C-23's nominal separation.

**Required remediation:** define and enforce typed, non-aliasing roles for
file-valued and directory-valued oracles; at minimum require runner bytes/blob
identity to differ from fixture and expectation and reject prohibited input /
expectation aliases. Add one fail-closed mutation for each prohibited path and
byte alias.

### R18-SQ-03 — High — Authority mutations are still separated from their validation by check/use windows

Create-story revalidates before writing the Story status, but later updates
`sprint-status.yaml` without another validation or an immutable-head check
(`create-story/instructions.xml:318-336`). Dev-story similarly runs
`--complete`, writes the Story to `review`, performs more work, then mutates the
sprint status (`dev-story/instructions.xml:331-360`). Code-review validates,
writes the Story status, saves it, then separately mutates sprint status
(`code-review/instructions.xml:171-209`); sprint-status validates a correction
batch before applying it. Approval, criterion, predecessor completion, branch
head, or completion evidence may change between each check and its second
authority write, leaving the two canonical status surfaces inconsistent or
authorized by stale evidence. The regression suite checks instruction-string
presence and order only; it has no mutation between preflight and either write.

**Required remediation:** pin and verify one immutable repository head and
evidence digest across each complete transition, or revalidate immediately at
each write under one atomic transition mechanism. Add executable regressions
that mutate approval, criterion, predecessor/completion evidence, and HEAD
after preflight and prove neither the Story document nor sprint status advances.

## Zero-finding acceptance condition

Rerun this independent lane after all three findings are remediated at a new
settled digest. PASS requires a representative full multi-file Cargo replay,
complete-change-set and role-alias mutations, atomic/pinned dual-surface status
transitions, and no new story-quality or dependency findings.
