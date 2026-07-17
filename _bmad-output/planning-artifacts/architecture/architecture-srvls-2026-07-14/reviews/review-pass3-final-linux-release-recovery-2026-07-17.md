---
reviewer: Sir Fix-a-Lot
session: sir-fix-a-lot-aegis-release-0717-r4
reviewed_digest: 04945fcb968eaba0d866f4c3bd9d0b5883a18fa8a28f1b82a8f70d7263981012
architecture_body_hash: 06df98f6d201abd47289d6c6771e15b83fb9d8a6c856a3a67e2e20e178a670aa
verdict: PASS
severity_counts:
  critical: 0
  high: 0
  medium: 0
  low: 0
total_findings: 0
---

# srvls Pass-3 Linux/systemd Release and Recovery Review

## Verdict

**PASS — zero findings.**

The frozen pass-3 architecture remediation, release corpus, validators, normative documentation, compatibility authorities, and current brownfield implementation are mutually consistent. The corpus goes beyond checksum self-consistency: it includes independent Linux lock and lease-handoff executions, fixed systemd/D-Bus semantic traces, captured brownfield consumer identity, exact negative mutation replay, and fail-closed future implementation gates.

The evidence does not claim that nonexistent Rust product code or release artifacts have passed. Those remain future acceptance obligations.

## Independence and frozen evidence

This was a fresh, independent, read-only review. I did not author or remediate the material and did not consult historical or peer reports under the architecture `reviews/` directory. Only the supplied prompt and `verify_digest.py` were accessed there.

The required verifier was executed exactly at both boundaries.

| Boundary | Substantive digest | Architecture body hash | Entries | Result |
| --- | --- | --- | ---: | --- |
| Start | `04945fcb968eaba0d866f4c3bd9d0b5883a18fa8a28f1b82a8f70d7263981012` | `06df98f6d201abd47289d6c6771e15b83fb9d8a6c856a3a67e2e20e178a670aa` | 226 | Match |
| End | `04945fcb968eaba0d866f4c3bd9d0b5883a18fa8a28f1b82a8f70d7263981012` | `06df98f6d201abd47289d6c6771e15b83fb9d8a6c856a3a67e2e20e178a670aa` | 226 | Match |

No evidence drift occurred during the review.

## Review basis and safety

Reviewed through EOF or as complete verifier-bound trees:

- `/home/delorenj/code/srvls/AGENTS.md`
- `.agents/skills/bmad-architecture/SKILL.md`
- `.agents/skills/bmad-architecture/customize.toml`
- `.agents/skills/bmad-architecture/references/headless.md`
- `.agents/skills/bmad-architecture/references/reviewer-gate.md`
- Complete `ARCHITECTURE-SPINE.md`
- Canonical PRD and addendum
- Canonical `DESIGN.md` and `EXPERIENCE.md`
- `README.md` and `docs/architecture.md`
- Current `srvls` Python implementation
- `mise.toml`
- Smoke, architecture-contract, planning-quarantine, compatibility, canonical-contract, and release validators
- Complete `tests/compat/` tree
- Complete top-level `tests/fixtures/contracts/` tree
- Every file in `tests/fixtures/contracts/release-transaction-v1/`
- Sprint-planning discovery instructions and workflow
- Canonical epics tombstone and byte-frozen retired artifact

Principal executed commands:

- Required digest verification at start and end
- Architecture spine lint, invoked directly with Python because `uv` could not create a cache temporary file in the read-only environment
- `tests/fixtures/contracts/release-transaction-v1/validate_oracles.py`
- `tests/fixtures/contracts/validate.py`
- `tests/validate_architecture_contracts.sh`
- `tests/test_smoke.sh`
- `tests/validate_planning_quarantine.py`
- Read-only `systemctl --user --version`, `show`, and `cat` observations
- Read-only `stat`, `wc`, `find`, `rg`, `jq`, `uname`, and tool-version observations

No repository byte was changed. No service, timer, process, package, database, unit file, manager configuration, or Host state was started, stopped, restarted, enabled, disabled, reloaded, installed, upgraded, rolled back, or otherwise mutated. The only active probes were the validators’ pre-authored private anonymous `memfd` tests.

## Live Linux/systemd observations

These observations are separate from normative contracts and future implementation obligations.

| Area | Live observation | Conclusion |
| --- | --- | --- |
| Kernel | Linux `6.17.0-40-generic`, x86-64 | Supports the exercised process-associated record-lock and `memfd` behavior |
| systemd | systemd `257.9` | Matches the v257 D-Bus semantic basis used by the corpus |
| User manager | This reviewer process lacked `DBUS_SESSION_BUS_ADDRESS` and `XDG_RUNTIME_DIR` | No fresh user-manager `show/cat` readback was available from this isolated session; no claim is made otherwise |
| Record locks | Both anonymous-`memfd` `F_RDLCK` and `F_WRLCK` owner-death tests passed | Child descriptor retention did not retain the parent’s process-associated lock |
| ActionExecutor lease handoff | Both negative late-acquisition and positive acknowledged-overlap tests passed | Admission generation and shared/exclusive lease behavior are reality-backed |
| Current product | Executable single-file Python implementation; smoke suite passed | Brownfield product is still Python/shell-oriented, not Rust |
| Rust toolchain | Host `rustc 1.95.0`; corpus independently freezes stable `1.97.1` evidence | Host compiler is not falsely treated as release evidence |
| Other tools | Python `3.14.4`, Bash `5.2.37` | Current implementation and validators executed successfully |

The absence of a user bus in this isolated reviewer environment does not convert the frozen brownfield capture into a live observation. The architecture correctly treats manager readback and restored-pair validation as implementation/release obligations, while the corpus supplies exact captured identities and D-Bus ordering authorities.

## Release-corpus inventory

| Evidence class | Required | Observed | Result |
| --- | ---: | ---: | --- |
| Substantive digest entries | 226 | 226 | Pass |
| Named crash-cut manifests | 11 | 11 | Pass |
| Complete transition chains | 7 | 7 | Pass |
| JSONL envelopes | 247 | 247 | Pass |
| Standalone authorities | 15 | 15 | Pass |
| Trace fixtures | 4 | 4 | Pass |
| Standalone result | 1 | 1 | Pass |
| Top-level checksum inventory | 1 | 1 | Pass |
| Release checksum inventory | 1 | 1 | Pass |

Both checksum inventories passed, including the closed-file-set requirement. Standalone canonical JSON objects have exactly one repository newline; JSONL histories have one canonical envelope per line and one final newline.

### Seven chains

| Chain | Envelopes | Contract covered |
| --- | ---: | --- |
| `forward.transitions.jsonl` | 35 | FirstInstall forward commit |
| `owner-takeover.transitions.jsonl` | 35 | FirstInstall replacement-owner completion |
| `first-install-recovery.transitions.jsonl` | 43 | Pre-decision FirstInstall recovery and absence restoration |
| `explicit-rollback.transitions.jsonl` | 25 | Explicit installed rollback |
| `upgrade.transitions.jsonl` | 35 | Installed generation 7 → 8 forward upgrade |
| `upgrade-owner-takeover.transitions.jsonl` | 35 | Installed upgrade replacement-owner completion |
| `upgrade-recovery.transitions.jsonl` | 39 | Failed upgrade, whole-pair generation 8 → 7 restoration |
| **Total** | **247** | Complete |

Each nonzero revision binds its immediate predecessor checksum and appends exactly one event. Cursor, final step record, effect attempt, manifest revision, event sequence, recovery-attempt linkage, terminal state, and generation cascades were recomputed and validated. The eleven named crash cuts byte-match their chain positions.

### Crash-cut coverage

The cuts cover:

- Initial transaction creation with absent cursor
- First-install consumer removal pending
- Commit decision complete
- KnownGood publication pending
- KnownGood publication complete
- Ready admission pending
- FirstInstall owner takeover pending validation
- Explicit rollback with restored ready admission pending
- Installed-upgrade ready admission pending
- Installed-upgrade owner takeover pending validation
- Installed-upgrade recovery pending restored-pair validation

This closes first install, same-generation/recovery behavior, installed upgrade, pre-decision recovery, post-decision completion, explicit rollback, and rollback-unavailable behavior.

## Directional hashes and negative replay

The explicit rollback direction is correct and unambiguous:

| Step/evidence | Generation role | Contract hash |
| --- | --- | --- |
| `restore-consumers` pre-effect | Displaced generation 8 source | `b7a215225c7f466b9c7ebb0cebe6fa2a889c1161581de5420d05dca5be2a7dad` |
| `restore-consumers` post-effect | Restored generation 7 target | `f3a3f80eeaa0cd7ccc202471635a8eccee49fdd6ad7d41204517d676639a8821` |
| Rollback daemon reload | Generation 7 restored target | `f3a3f80e…` |
| Restored-pair validation | Generation 7 restored target | `f3a3f80e…` |

Forward installed upgrade is generation 7 → 8. Failed-upgrade recovery reverses the consumer effect from generation 8 to generation 7 while reload, timer proof, and FD4 validation remain bound to restored generation 7.

The release validator passed all adversarial suites:

- 5 explicit rollback-direction mutations
- 12 FD4 scalar/binding mutations
- 22 checksum-resealed release semantic mutations
- 7 brownfield-pair mutations
- 3 toolchain mutations
- 25 CanonicalJsonV1 mutations
- 1 key-order mutation
- 11 percent/path mutations
- Positive two-pair FirstInstall expansion

The mutations reject same, swapped, unknown, duplicated, malformed, stale, cross-bound, wrong-generation, wrong-schema, wrong-artifact, wrong-owner, wrong-deadline, wrong-path-role, and wrong-terminal evidence even after affected checksums are resealed. This demonstrates semantic validation rather than mere hash consistency.

## Technical conclusions

### Filesystem and atomicity

The architecture distinguishes canonical link, versioned binary, database, transaction manifest, KnownGood, backup, fragment, drop-in, enablement-link, and directory roles. Regular files, symlinks, absent-prior paths, and pre-existing directories have closed evidence shapes.

Temporary creation, file synchronization, directory synchronization, rename/atomic replacement, symlink replacement, SQLite backup, integrity verification, and recovery boundaries are ordered and durable. First-install removal requires byte-equal file/link/directory evidence before unlink or permitted directory pruning.

### Locks, ownership, and admission

The architecture deliberately uses traditional process-associated `F_SETLK`/`F_SETLKW` byte-range locks, not `flock`, `lockf`, or OFD locks. That choice supplies close-on-owner-death semantics even when a stopped child retains the descriptor. The live proof covers both shared and exclusive modes and verifies owner/type through `F_GETLK`.

Atomic `CLOEXEC`, close-first child behavior, owner identity, admission generation, recovery takeover, submitter/ActionExecutor lease transfer, and refusal before mutation on stale admission are explicit. The lock and handoff probes passed.

### FD3/FD4 and recovery

FD3/FD4 ownership, closure, EOF, request/result direction, close-first child setup, process/job recovery, evidence identity, and terminal handling are bound. FD4 requests are cross-bound to transaction checksum, recovery attempt, manifest revision, generation, binary, schema, backup, owner, and absolute deadline.

### Timers and D-Bus

Deadlines use `CLOCK_BOOTTIME`; equality is terminal rather than granting an extra attempt. Timer acceptance binds service/timer pairing, baseline, trigger causality, job identity, `JobRemoved`, invocation identity, start time, terminal result, and the same validation attempt.

Fresh recovery connections must install matches, bind the manager owner, call `Manager.Subscribe`, recheck ownership, drain discontinuity markers, and only then consume `ListJobs` or `JobRemoved`. The corpus rejects stale owners, gaps, overflow, disconnects, and subscription failures.

### systemd consumer identity

The corpus freezes exact fragments, drop-ins, normalized manager properties, service/timer pairing, enablement mutation/readback, daemon-reload, loaded readback, timer causality, and restored-pair evidence. Two brownfield pairs are present:

| Pair | Source contract | Candidate contract |
| --- | --- | --- |
| metrics | `4ce9b13e7c5ecabf9bc450fef57c4878d7cf8494df7bb1260b0bf201eb3ab8f1` | `874c43cdc78dc59e0af187783abc01bbee11ef42d57a0f3eb45abfac27201caa` |
| snapshot | `0ba59ba2ac1a6e007e16bf72e2b637ca2de610f58434e1f66fa2e3a89071d565` | `198218c35598b1e10a49abd737dd0937bdafa46f5a0699d322fa52e25d4a699b` |

Only the two canonical executable-path occurrences may change when deriving a candidate. Rehashed behavioral changes such as adding `|| true` are rejected.

### KnownGood, backup, and recovery

StateBackup plans and completed manifests bind schemas, source and backup paths, database/WAL/SHM dispositions, file hashes, integrity, connection exclusion, and both file and directory fsync.

KnownGood candidate, commit decision, expected publication checksum, publication evidence, installed bundle, retained adjacent release, and ready admission form a closed cascade. Recovery correctly separates:

- Pre-decision rollback/recovery
- Post-decision forward completion
- First-install absence restoration
- Installed failed-upgrade restoration
- Explicit rollback
- Rollback unavailable without embedding a fictitious transaction

### Toolchain and current implementation honesty

The stable toolchain fixture proves official Rust `1.97.1` manifest/archive identity and compiler execution. It does not claim product compilation, ABI compatibility, candidate `readelf`, or oldest-runtime smoke.

The architecture gate conditionally requires Rust boundary tests and runs Cargo only after a `Cargo.toml` exists. The current repository contains a Python implementation and shell/Python validation. `README.md`, `docs/architecture.md`, the release README, and `PROVENANCE.md` all preserve that distinction.

## Validator results

- Architecture spine lint: 0 findings
- Compatibility replay: PASS
- Source pin and immutable hashes: PASS
- AD-9 coverage: 90 inherited plus 4 approved deviations
- Planning quarantine: PASS
- Canonical contract oracles: PASS
- Release oracle validation: PASS
- Smoke suite: PASS
- Aggregate architecture contract gate: PASS
- Start/end frozen digest: PASS

## No findings

No critical, high, medium, or low issue was identified.

FINDINGS: 0
VERDICT: PASS