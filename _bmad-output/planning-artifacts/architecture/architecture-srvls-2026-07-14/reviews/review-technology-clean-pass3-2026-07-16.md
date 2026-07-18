---
title: Technology Clean-Pass3 Acceptance Review
document_type: architecture-review
review_dimension: technology
review_pass: clean-pass3
reviewer: WidgetWhisperer
review_date: 2026-07-16
evidence_completed_date: 2026-07-17
reviewed_commit: db70e84c74a301d6e698cddf0c88fb47e78da851
reviewed_spine_sha256: 5907c2f7da67378c6da60de0ed6374b9393d30b7945d271e6e261467ebce9392
reviewed_memlog_sha256: ea143f28e2bb88b54835ecb2313c950812e02d8d45835cc86124e511226d915c
verdict: PASS
finding_count: 0
blocking_finding_count: 0
---

<!-- markdownlint-disable MD013 MD025 -->

# Technology Clean-Pass3 Acceptance Review

## Verdict

**PASS.** Exact base commit
`db70e84c74a301d6e698cddf0c88fb47e78da851` has zero findings of any
severity. The remediated technology and deployment contracts are internally
complete, agree with current primary sources and the installed Linux/systemd
interfaces, and survived the independent adversarial probes below.

| Result | Count |
| --- | ---: |
| Critical findings | 0 |
| High findings | 0 |
| Medium findings | 0 |
| Low findings | 0 |
| Total findings | 0 |

PASS requires zero findings; that threshold is met.

## Review Basis and Independence

This review was performed only in the assigned
`widgetwhisperer-architecture-clean-pass3` worktree. Before evidence capture,
`git rev-parse HEAD` returned the exact required base above and the worktree was
clean. The normative artifact was `ARCHITECTURE-SPINE.md` through line 2359;
its append-only `.memlog.md` was read through line 146. Their SHA-256 digests
are frozen in the front matter.

The complete architecture skill, its required `headless.md` and
`reviewer-gate.md` references, project customization, `AGENTS.md`, and
`tasks.md` were read before review. All eleven historical technology/version
reports present through clean pass 2 were read for supersession history:

- version operations;
- technology currency and acceptance;
- remediation gate, rerun, final, closure, reality closure, and unanimous
  closure;
- final pass; and
- clean pass 2.

No clean-pass3 peer report was present or read. Historical findings were used
only as adversarial leads; current primary documentation, installed tools and
manager state, and fresh probes controlled the decision.

There is no product `Cargo.toml`, `Cargo.lock`, Rust source, or built `srvls`
release artifact at this architecture base. This is therefore acceptance of the
architecture's executable gates, not a claim that a future implementation
artifact has already passed release CI.

## Acceptance Matrix

| Gate | Normative anchors | Result | Independent evidence |
| --- | --- | --- | --- |
| Rust stable identity and stale-cache refusal | AD-12:644-695; Stack:2199-2223 | PASS | Fresh official stable metadata identifies Rust 1.97.1 at full commit `8bab26f4f68e0e26f0bb7960be334d5b520ea452`. The host's cached stable 1.97.0 and active 1.95.0 override both differ, so AD-12's pre-build exact identity comparison correctly rejects them. |
| Rust 1.88 MSRV dependency graph | AD-12:644-670; Stack:2207-2223 | PASS | An isolated exact-version probe built and tested with official 1.88.0 and 1.97.1. The resolved critical graph is ratatui 0.30.2 to Crossterm 0.29 and rusqlite 0.39.0 to libsqlite3-sys 0.37.0 to bundled SQLite 3.51.3. |
| SQLite initialization, backup, and ABI gates | AD-12:660-669; AD-16:898-967; AD-23:1393-1396 | PASS | Fresh/reopened WAL, FULL, foreign-key, timeout, and `BEGIN IMMEDIATE` probes matched the specified readbacks. A live-WAL SQLite backup/restore retained schema, rows, and integrity. The final-artifact `readelf` plus oldest-runtime gate is sound and does not infer success before an artifact exists. |
| Release journal, recovery owner, and decision cut | AD-23:1277-1315, 1354-1429, 1490-1538 | PASS | Same-directory mode-0600 O_EXCL/fsync/rename/directory-fsync replay kept the prior authority across an orphan torn temp, accepted the next complete envelope atomically, and rejected truncated/checksum-invalid bytes. All pending/effect/complete crash cuts have one explicit readback path, and `commit-decided` is unambiguously forward-only. |
| FirstInstallAbsentV1 and explicit rollback | AD-23:1487-1551 | PASS | Exact owned link/hash recovery removed only the transaction-owned pair; a hash mismatch preserved the foreign replacement. Repeated sentinel rollback produced identical `rollback-unavailable/no-prior-release` results with zero manifest, event, admission, unit, state, or filesystem mutation; recovering admission wins before the sentinel. |
| Admission `flock`, atomic CLOEXEC, and every child path | AD-23:1238-1275, 1320-1325 | PASS | Shared and exclusive inherited leases reproduced the clean-pass2 liveness failure. Atomic CLOEXEC made the contender succeed while the exec child remained alive, and explicit close-first made it succeed while a pre-exec child deliberately stalled. The catch-all whitelist covers FD3, FD4, Provider, systemctl, timer-control, smoke, checksum, and every other child. |
| Loaded service/timer and enablement parity | AD-12:674-694; AD-23:1398-1430 | PASS | Installed systemd 257 exposed every named service/timer field. Four loaded unit fragments and hashes matched `systemctl cat`; `NeedDaemonReload=no`; each service is static, each timer enabled by a separate one-unit query; target, monotonic/calendar schedules, accuracy, random delay, persistence, wake, remain, and reactivation values were exact. |
| Timer causality and attempt-bound deadline | AD-20:1093; AD-23:1297-1315, 1431-1477 | PASS | Installed D-Bus reports Job and Unit `ActivationDetails` as `a(ss)`. Live evidence contained `trigger_unit=srvls-metrics.timer`. The contract captures the exact Job before removal, requires the documented causal pair, rejects absent/competing evidence, and binds all unit, timer, terminal, and FD4 observations to one persisted strict-before CLOCK_BOOTTIME cut. |
| FD3 ownership, descriptor closure, and EOF | AD-25:1847-2058 | PASS | SOCK_CLOEXEC marked both original endpoints; an injected raw duplicate cleared CLOEXEC and suppressed EOF after the original closed; EOF appeared only after the duplicate closed. AD-25 rejects any such duplicate before Hello, restores FD3 CLOEXEC before Provider launch, and accepts Result only on the clean ownership lane. |
| Schedules, admitted cuts, and canonical structure | AD-10:316-456; AD-11:458-517; AD-20:1057-1114; AD-24:1589-1845 | PASS | Independent LPT replay matched all three named schedules, equality expired without child state, and multi-epoch catch-up terminalized all expired reservations before any live spawn. Architecture lint is clean; 25 ADs, 24 ARCH-LIMs, and 55 expanded Structural Seed paths are contiguous and unique. |

## Current Technology Evidence

### Rust Identity, MSRV, and Dependency Graph

Fresh official `channel-rust-stable.toml` evidence was compared with verbose
compiler identity before compilation:

| Evidence | Result |
| --- | --- |
| Official stable manifest | date `2026-07-16`; release `1.97.1 (8bab26f4f 2026-07-14)`; full commit `8bab26f4f68e0e26f0bb7960be334d5b520ea452` |
| Isolated official MSRV | rustc 1.88.0; full commit `6b00bc3880198600130e1cf62b8f8a93494488cc`; commit date `2025-06-23` |
| Isolated refreshed stable | rustc 1.97.1; exact official full commit and commit date `2026-07-14` |
| Host cached `stable` | rustc 1.97.0, stale relative to the official manifest |
| Host active override | rustc/cargo 1.95.0, not the release stable identity |

An isolated crate outside the repository used edition 2024, resolver 3,
`rust-version = "1.88"`, and the exact reviewed direct versions. Both
toolchains passed locked all-target tests and locked release builds. Cargo
metadata and tree inspection confirmed:

- ratatui 0.30.2 resolves the default Crossterm 0.29 line;
- rusqlite 0.39.0 with `bundled` resolves libsqlite3-sys 0.37.0 and its bundled
  header declares SQLite 3.51.3;
- `toml = "=1.1.3"` resolves registry version
  `1.1.3+spec-1.1.0`, consistent with Cargo's SemVer build-metadata handling;
- ratatui 0.30.2 and time 0.3.53 both declare Rust 1.88 support; and
- every exact Stack version was present and non-yanked in current official
  registry metadata.

This directly exercises the MSRV graph while preserving AD-12's separate
requirement that the eventual committed lockfile and exact final artifact pass
all release gates.

### SQLite and Final-Artifact ABI Boundary

The installed host is glibc 2.42 with SQLite CLI 3.50.6; the probe intentionally
used the reviewed bundled dependency rather than treating the host CLI as the
application library.

Fresh and reopened database checks returned:

| Check | Observed |
| --- | --- |
| `PRAGMA journal_mode=WAL` setter/readback | `wal` / `wal` |
| `PRAGMA synchronous=FULL` numeric readback | `2` |
| Fresh connection `foreign_keys` before enablement | `0` |
| Per-connection `foreign_keys=ON` readback | `1` |
| Busy timeout | `5000` ms |
| First writer transaction | `BEGIN IMMEDIATE` succeeded after all readbacks |

The live-WAL backup probe observed a WAL sidecar, used SQLite's backup API,
then reopened the backup read-only. `integrity_check=ok`, user schema version 7,
and all rows survived. With source and destination handles closed, a restored
copy was file- and directory-fsynced and again passed integrity and row checks.

A representative GNU release-mode Rust probe was an x86-64 GNU PIE and imported
no GLIBC symbol newer than 2.34. That is only a mechanism probe. AD-12 correctly
requires running GNU `readelf --version-info` on the future exact final `srvls`
artifact, rejecting any import above 2.42, and smoking that same artifact in the
pinned oldest-supported glibc 2.42 runtime.

### Release Journal and Crash Recovery

The fresh filesystem probe reproduced the normative journal primitive:

```text
journal: mode0600=True orphan_not_promoted=True atomic_authority_v2=True torn_rejected=True
sqlite_backup: wal_seen=True backup_integrity=True schema=True rows=True restored_pair=True
```

The recovery state model then enumerated every effect cut without inferring
completion from a public phase:

| Crash cut | Sole admissible recovery action |
| --- | --- |
| Before pending publication | retain the prior authoritative manifest |
| Pending, before effect | read back, then run the idempotent effect |
| Effect partially applied | exact readback; complete or atomically replace |
| Effect done, before complete | exact readback, then persist complete |
| Complete persisted | advance to the next ordered step |

The irreversible branch is equally total: pre-decision restores and validates
the entire prior pair; after `commit-decided`, recovery finishes KnownGood
publication, target-generation ready admission, and terminal commit without
rolling back. A new recovery owner must publish and read back its gap-free
owner attempt before effect truth or a fresh validation attempt can run.

For FirstInstallAbsentV1, the adversarial filesystem cases returned:

```text
exact-owned pair: restored-absent; link and versioned binary absent
foreign binary hash: hash-mismatch; foreign link and bytes preserved
sentinel rollback x2: rollback-unavailable/no-prior-release; tree digest unchanged
```

This matches the byte-total absence recovery, reserved generation zero, skipped
absent-binary stages, required absence validator, and deterministic no-mutation
explicit rollback contract.

### Admission Lock and Child Descriptor Whitelist

The lock probe used real Linux `flock` open-file-description semantics and an
exec child. The contender always requested a nonblocking exclusive lease.

| Owner lease / child behavior | CLOEXEC | Contender while child alive | Contender after exit |
| --- | ---: | ---: | ---: |
| Exclusive / inherited through exec | no | blocked | acquired |
| Shared / inherited through exec | no | blocked | acquired |
| Exclusive / atomic CLOEXEC | yes | acquired | acquired |
| Shared / atomic CLOEXEC | yes | acquired | acquired |
| Exclusive / explicit first child close, then child stalls | deliberately inheritable before fork | acquired | acquired |

The first two rows reproduce TECH-CLEAN2-01. The remaining rows verify both
layers of its closure: atomic `O_CLOEXEC` with immediate `F_GETFD` proof and an
explicit close action before any fallible or blocking child setup. AD-23 names
all known child categories and adds the exhaustive "every other child path"
rule, so no spawn path is left to infer the policy.

### Loaded systemd Service/Timer Parity

The live user manager is systemd 257.9. Four exact fragment hashes were
captured:

| Unit | Fragment SHA-256 | Loaded/enablement | Normalized contract evidence |
| --- | --- | --- | --- |
| `srvls-metrics.service` | `b232dab9a3561cbb520263cafc00a26763894b70b618aa36ef22357ca980a4fa` | loaded, static | oneshot; complete shell argv; `RemainAfterExit=no` |
| `srvls-metrics.timer` | `4d6b8d0b90bf32d20c68456662ef8460deb98ba2fdb9e95bf7a8c174e12eb043` | loaded, enabled | target metrics service; OnBoot 2 min; OnUnitActive 5 min; accuracy 1 min; random delay 20 s; not persistent; no wake; remain yes; no defer |
| `srvls-snapshot.service` | `e6b3a3593a4fd0f67d112293fa5678b3cfb8909a9babef85909317bae4aa75dc` | loaded, static | oneshot; complete ExecStart and ExecStartPost argv; `RemainAfterExit=no` |
| `srvls-snapshot.timer` | `6cb2a2a6cf5961ba1027af8894a2b653de61e5a0b9f397efa21a1dd3087f2967` | loaded, enabled | target snapshot service; calendar `*-*-* 04:10:00`; accuracy 1 min; random delay 0; persistent; no wake; remain yes; no defer |

All four report `NeedDaemonReload=no`, empty SourcePath/DropInPaths as expected,
and byte-identical fragments through `systemctl cat`. Enablement was queried
one unit per invocation: both services returned `static`, both timers
`enabled`. This specifically avoids `systemctl is-enabled`'s aggregate
any-enabled exit behavior.

The current brownfield metrics service remains failed with status 126 because
its loaded ExecStart still names
`/home/delorenj/code/infra/bin/srvls`, a mode-0664, non-executable forwarding
file. This is deployment evidence, not an architecture finding: AD-12/AD-23
explicitly inventory and replace that managed absolute consumer, require the
new loaded path and complete timer contract, and refuse or restore the whole
pair unless a fresh timer-originated candidate exits successfully.

### ActivationDetails and the CLOCK_BOOTTIME Attempt Cut

Installed `org.freedesktop.systemd1` documentation and introspection expose
`ActivationDetails` on both Unit and Job as `a(ss)` and document
`trigger_unit` as a valid trigger that caused the activation job. The live
metrics unit supplied concrete kernel/manager evidence:

```text
a(ss) 3 "trigger_unit" "srvls-metrics.timer"
          "trigger_timer_realtime_usec" "1784255304243951"
          "trigger_timer_monotonic_usec" "35072644551"
```

The unit-level value can outlive a later invocation; AD-23 correctly does not
use it as sufficient acceptance. It subscribes before the trigger, captures
the exact Job object's complete list before JobRemoved, requires that job's
Unit and type, the exact timer pair, result `done`, an advancing timer trigger,
a new InvocationID and start, successful terminal fields, and no intervening
manual or unrelated activation. Because systemd supplies the detail only best
effort, absence fails rather than becoming inferred causality.

The attempt-cut probe used actual `CLOCK_BOOTTIME` and checked the boundary:

| Observation | Result |
| --- | --- |
| One nanosecond before persisted cut | eligible |
| Equal to persisted cut | expired |
| One nanosecond after persisted cut | expired |
| New recovery owner | old attempt retained; next effect-attempt persisted with fresh start/cut |
| Same-owner retry | requires another durable effect attempt; no silent deadline refresh |

The clock was available and nondecreasing on this kernel. The single cut is
persisted and read back before loaded-unit sampling, timer work, child creation,
or FD4 creation, so timer and validator evidence cannot receive independent or
extended subsystem timeouts.

### FD3 Ownership and EOF

The fresh socketpair probe observed:

```text
reader_cloexec=True writer_cloexec=True raw_dup_cloexec=False
after_original_close=no-eof
after_duplicate_close=b''
```

This is the adversarial condition AD-25 must reject. Its ownership table,
original/opposite/duplicate closure cuts, injected-duplicate failure before
Hello, child whitelist, FD3 CLOEXEC restoration before Provider spawn, and
worker write shutdown/close plus parent EOF/close together provide both
ownership proof and terminal framing. No successful lane relies on EOF alone
to discover an undetected duplicate.

### Deterministic Schedules and Structural Uniqueness

An independent implementation of the AD-10 compiler reproduced the named
fixtures exactly:

| Fixture | Epochs | Process gate | Makespan | Generation cutoff |
| --- | --- | --- | ---: | ---: |
| Default `[30,20,15,15,10,10,10,process=10]` | `0,15,20,25` s | `[25,35)` s | 35 s | 40 s |
| Near tie `[20,20,20,20,process=10,9,9,9]` | `0,20` s | `[20,30)` s | 30 s | 35 s |
| Process 60 s plus seven 1 s, zero configured margin | `0,60` s | `[0,60)` s | 61 s | `61,000,000,001` ns |

At a default-schedule admission sample exactly 25 seconds late, equality first
terminalized PM2, both systemd members, and both epoch-15 cron members in
ascending epoch/worker order. Only after every no-child timeout existed did it
start the still-live Docker, epoch-20 cron, and epoch-25 process reservations;
none received a moved deadline or cleanup state.

Mechanical structure results were:

```text
architecture lint: ok=true, total_findings=0
AD: count=25, contiguous 1..25, duplicates=[]
ARCH-LIM: count=24, contiguous 1..24, duplicates=[]
Structural Seed: expanded=55, unique=55, duplicates=[]
```

Brace expansion confirmed the five distinct host adapter paths and exactly one
`src/adapters/worker.rs` and one `src/adapters/release.rs` ownership path.

## Findings

None. No Critical, High, Medium, Low, or informational architecture defect was
identified. The live broken legacy metrics consumer is recorded above as
brownfield migration evidence and is covered by a fail-closed release
postcondition; it is not presented as a healthy current deployment.

## Primary Sources

- Rust official
  [stable manifest](https://static.rust-lang.org/dist/channel-rust-stable.toml),
  [Rust 1.97.1 announcement](https://blog.rust-lang.org/2026/07/16/Rust-1.97.1/),
  and
  [Cargo `rust-version`](https://doc.rust-lang.org/stable/cargo/reference/rust-version.html)
  documentation; exact package records were cross-checked through the official
  crates.io API.
- Ratatui official
  [0.30.2 tagged manifest](https://raw.githubusercontent.com/ratatui/ratatui/ratatui-v0.30.2/Cargo.toml).
- SQLite official
  [PRAGMA](https://www.sqlite.org/pragma.html),
  [WAL](https://www.sqlite.org/wal.html),
  [backup API](https://www.sqlite.org/backup.html), and
  [transaction](https://www.sqlite.org/lang_transaction.html) documentation.
- GNU Binutils official
  [`readelf`](https://sourceware.org/binutils/docs/binutils/readelf.html)
  documentation.
- systemd 257 official
  [`systemctl`](https://www.freedesktop.org/software/systemd/man/257/systemctl.html),
  [`systemd.timer`](https://www.freedesktop.org/software/systemd/man/257/systemd.timer.html),
  and
  [`org.freedesktop.systemd1`](https://www.freedesktop.org/software/systemd/man/257/org.freedesktop.systemd1.html)
  documentation, cross-checked against the installed systemd 257.9 manuals,
  D-Bus API, and live user manager.
- Linux man-pages project copies for
  [`flock(2)`](https://man7.org/linux/man-pages/man2/flock.2.html),
  [`open(2)`](https://man7.org/linux/man-pages/man2/open.2.html),
  [`fcntl(2)`](https://man7.org/linux/man-pages/man2/fcntl.2.html),
  [`execve(2)`](https://man7.org/linux/man-pages/man2/execve.2.html),
  [`dup(2)`](https://man7.org/linux/man-pages/man2/dup.2.html),
  [`socketpair(2)`](https://man7.org/linux/man-pages/man2/socketpair.2.html),
  [`unix(7)`](https://man7.org/linux/man-pages/man7/unix.7.html),
  [`clock_gettime(2)`](https://man7.org/linux/man-pages/man2/clock_gettime.2.html),
  [`rename(2)`](https://man7.org/linux/man-pages/man2/rename.2.html), and
  [`fsync(2)`](https://man7.org/linux/man-pages/man2/fsync.2.html).

## Required Checks

All acceptance checks pass on the exact reviewed base plus only this report:

- architecture lint: `ok=true`, `total_findings=0`;
- canonical Markdown lint with the project profile: pass;
- `git diff --check`: pass;
- exact-base ancestry and restricted-change check: pass;
- identifier uniqueness: 25 AD identifiers and 24 ARCH-LIM declarations,
  with no duplicate or sequence gap;
- Structural Seed uniqueness: 55 expanded paths, no duplicate;
- exact-version MSRV/stable builds and tests: pass;
- SQLite initialization, live-WAL backup, integrity, and restore probes: pass;
- shared/exclusive lock inheritance and close-first adversarial probes: pass;
- loaded unit/timer and separate one-unit enablement inspection: pass;
- ActivationDetails API/type and live timer-trigger evidence: pass;
- attempt deadline equality and recovery-attempt rebinding: pass;
- FD3 duplicate/EOF adversarial probe: pass; and
- default, near-tie, pathological, and late-admission schedule replays: pass.

## Acceptance Gate

The final technology acceptance verdict for exact base
`db70e84c74a301d6e698cddf0c88fb47e78da851` is **PASS** with zero findings of
any severity.
