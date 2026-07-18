---
title: Technology Clean-Pass2 Acceptance Review
document_type: architecture-review
review_dimension: technology
review_pass: clean-pass2
reviewer: WidgetWhisperer
review_date: 2026-07-16
reviewed_commit: 300ad193f88ab4fa7f5429c560d8f14794dd45a0
reviewed_spine_sha256: 401ebc30e64a41623d629a407b4260c0d21c7a3b7c3ae9ebc058cba0aad56206
reviewed_memlog_sha256: dc2244ff89973ac1261caaa33fb47c7d7154ec3fd8117d3c1b8ca91b6828fba9
verdict: CHANGES REQUIRED
finding_count: 1
blocking_finding_count: 1
---

<!-- markdownlint-disable MD013 MD025 -->

# Technology Clean-Pass2 Acceptance Review

## Verdict

**CHANGES REQUIRED.** Exact base commit
`300ad193f88ab4fa7f5429c560d8f14794dd45a0` has one High, release-blocking
technology finding. The admission lock is not normatively close-on-exec, so a
child inherited from a crashed lock owner can keep the `flock` alive and prevent
the recovery owner that AD-23 promises from ever acquiring the exclusive lease.

The remediated Rust-stable identity, SQLite PRAGMAs, ABI gates, durable journal
ordering, KnownGood decision boundary, loaded systemd service/timer parity,
fresh timer invocation correlation, FD3 ownership and EOF, deterministic
schedule, identifier uniqueness, and Structural Seed uniqueness otherwise pass
this independent review.

| Result | Count |
| --- | ---: |
| High blocking findings | 1 |
| Medium findings | 0 |
| Low findings | 0 |
| Total findings | 1 |

PASS requires zero findings. This report therefore cannot accept the
architecture as written.

## Review Basis and Independence

This review was performed only in the assigned worktree against the exact base
commit above. The reviewed normative artifact was
`ARCHITECTURE-SPINE.md` through line 2011; its append-only `.memlog.md` was read
through line 145. All ten historical technology reports present at the base
commit were read for supersession history. No other new clean-pass2 report was
opened or used.

The prior reports were treated as leads, not proof. Every named technology claim
below was replayed against current primary official material, installed primary
manuals or tools, and small deterministic local probes. The current spine and
current official metadata control wherever history disagrees.

## Acceptance Matrix

| Gate | Normative anchors | Result | Independent evidence |
| --- | --- | --- | --- |
| Rust stable 1.97.1 identity and stale-cache refusal | AD-12:568-580 | PASS | The official stable manifest reports date `2026-07-16`, release `1.97.1 (8bab26f4f 2026-07-14)`, and full commit `8bab26f4f68e0e26f0bb7960be334d5b520ea452`; installed cached `stable` is 1.97.0 at a different commit, which the required exact comparison rejects before compilation. |
| SQLite WAL, FULL, and foreign-key readbacks | AD-16:809-821 | PASS | Fresh and reopened database probes returned `wal`, numeric synchronous value `2`, and foreign-keys value `1` after connection-local enablement; all configuration occurs outside a transaction before `BEGIN IMMEDIATE`. |
| Exact-artifact GLIBC ABI gate and oldest-runtime smoke | AD-12:563-587 | PASS | GNU `readelf --version-info` exposes imported GLIBC versions; the rule gates the exact final artifact at `GLIBC_2.42` and then runs that same artifact in the pinned oldest-supported 2.42 runtime. This is a sound release contract; no unbuilt `srvls` release artifact was inferred to have passed it. |
| Crash-persistent admission, journal recovery, and KnownGood rollback | AD-23:1143-1351 | **FAIL** | Pending/complete effects, atomic readback, the irreversible `commit-decided` cut, KnownGood publication, and forward-only recovery are coherent, but the admission lock descriptor can survive an owner crash in an exec'd child and block takeover. See TECH-CLEAN2-01. |
| Loaded service/timer property and enablement parity, forward and rollback | AD-12:591-606; AD-23:1257-1288, 1308-1317 | PASS | Installed systemd 257 interfaces expose every named normalized property; exact one-unit enablement readback avoids `is-enabled` any-enabled semantics, and rollback uses the same validator against the prior contract. |
| Fresh timer trigger, InvocationID, start, and result correlation | AD-23:1290-1306 | PASS | Installed systemd exposes `LastTriggerUSecMonotonic`, `InvocationID`, `ExecMainStartTimestampMonotonic`, `Result`, `ExecMainCode`, and `ExecMainStatus`; the strict baseline, identity, temporal, and terminal checks reject stale success. |
| FD3 CLOEXEC ownership, duplicate endpoints, and EOF | AD-25:1511-1541, 1800-1815 | PASS | `SOCK_CLOEXEC` marks the original pair, raw `dup` clears CLOEXEC on the duplicate, and a retained duplicate suppressed EOF until its last close. The ownership cuts and duplicate-parent/child fixtures require exactly the closures needed for clean EOF. |
| Deterministic schedule and remediation fixtures | AD-10:321-407; AD-11:462-494 | PASS | Independent LPT replay produced the exact default, near-tie, and pathological epochs, gates, makespans, and cutoffs. Early completion does not alter reservation bytes. |
| Identifier and Structural Seed uniqueness | AD-1 through AD-25; ARCH-LIM-1 through ARCH-LIM-23; Structural Seed:1877-1931 | PASS | Parsed 25 unique contiguous AD identifiers, 23 unique contiguous ARCH-LIM declarations, and 55 unique expanded Structural Seed paths; `src/adapters/worker.rs` and `src/adapters/release.rs` each occur exactly once. |

## Blocking Finding

### TECH-CLEAN2-01 — The Admission Lock Can Survive Owner Death in an Exec'd Child

- **Severity:** High
- **Disposition:** release-blocking
- **Affected qualities:** crash recovery, release liveness, single-owner
  correctness, operational safety
- **Primary anchors:** AD-23:1143-1157, AD-23:1180-1206,
  AD-25:1511-1535

#### Evidence

AD-23:1143-1146 requires `admission.lock` to be a no-follow regular file held
with `flock`, but it does not require the lock descriptor to be created with
`O_CLOEXEC`, to have `FD_CLOEXEC` verified, or to be closed in every child spawn
file action. AD-23:1159-1178 then assumes a replacement owner can acquire the
exclusive lock after a crashed release owner.

The candidate-validator rule at AD-23:1180-1206 closes other copies of the FD4
socket endpoint; it does not close unrelated inherited descriptors such as the
admission lease. Likewise, the exact FD3 table at AD-25:1527-1535 accounts for
the socketpair descriptors only. The architecture also launches providers and
systemd commands while ordinary stateful entries retain shared leases. No
global spawn whitelist closes the admission lock in those children.

Linux `flock(2)` makes the resulting failure mechanical:

- locks are attached to an open file description;
- descriptors duplicated by `fork` refer to the same lock;
- the lock is released only by explicit unlock or after every descriptor that
  references that open file description closes; and
- the lock is preserved across `execve`.

Linux `open(2)` also states that a new descriptor remains open across `execve`
by default unless `O_CLOEXEC` or `FD_CLOEXEC` is used, and specifically
recommends atomic `O_CLOEXEC` to avoid the fork/exec race in multithreaded
programs.

A local kernel-level reproduction cleared CLOEXEC on an exclusively flocked
temporary descriptor, forked and exec'd `/usr/bin/sleep`, and closed the owner
copy to model owner death. A separately opened contender produced:

```text
inherited_lock_blocks_recovery=true
lock_acquirable_after_inheriting_child_exit=true
```

Thus the durable admission file can correctly remain `recovering` while the
next release process is indefinitely unable to publish a recovery owner. The
same defect on a shared lease can indefinitely delay an otherwise valid
exclusive release admission. This contradicts AD-23:1155-1157's statement that
the crashed release's live lock is dropped and breaks the stated recovery
contract even though the journal itself is durable.

#### Required Correction

Amend AD-23 at the admission-lock definition and every spawn boundary to require
all of the following:

1. open every admission shared or exclusive lease atomically with `O_CLOEXEC`
   and fail closed unless `F_GETFD` confirms `FD_CLOEXEC` before the lease is
   treated as acquired;
2. define a process-wide child descriptor whitelist: only standard descriptors
   and the explicitly mapped transient FD3 or FD4 may cross their corresponding
   same-binary exec; validator, worker, Provider, `systemctl`, timer, and other
   child paths must close the admission-lock descriptor in spawn file actions;
3. extend the descriptor ownership proof to include the admission lease and
   require zero admission-lock descriptors in every child after exec; and
4. add deterministic shared- and exclusive-lease fixtures that leave an exec'd
   child alive, terminate the lease owner, and prove a new exclusive contender
   acquires immediately and can publish the next recovery owner. Cover the FD3,
   FD4, Provider, and systemd-command launch paths, plus an injected pre-exec
   setup stall or failure.

The correction must remain normative in the spine. A comment or implementation
assumption that Rust commonly opens files close-on-exec is insufficient for an
architecture whose release safety depends on that property.

## Independent Technology Verification

### Rust Stable Identity and Dependency Currency

The official stable channel manifest fetched during this review contained:

```text
date = "2026-07-16"
version = "1.97.1 (8bab26f4f 2026-07-14)"
git_commit_hash = "8bab26f4f68e0e26f0bb7960be334d5b520ea452"
```

The official Rust announcement is dated 2026-07-16 and identifies 1.97.1 as a
point release. In contrast, `rustup run stable rustc --version --verbose` on the
review host reported cached Rust 1.97.0 and commit
`2d8144b7880597b6e6d3dfd63a9a9efae3f533d3`. AD-12 requires both release and
full commit to equal the fresh manifest before any compile, so this exact stale
cache is refused. The active directory override was Rust/Cargo 1.95.0 and was
not substituted for stable-channel evidence.

Exact crates.io metadata checks also found every version named as a reviewed
lock target in the current Stack table to exist and be non-yanked. Ratatui 0.30.2 and
ratatui-crossterm 0.1.2 declare Rust 1.88; the tagged Ratatui manifest uses
edition 2024 and crossterm 0.29. The `libsqlite3-sys` 0.37.0 bundled header
identifies SQLite 3.51.3. These observations are consistent with the spine's
MSRV, edition, and bundled-database claims.

### SQLite Initialization

The official PRAGMA documentation confirms that setting `journal_mode` returns
the resulting mode, WAL persists for the database, `synchronous` queries return
numeric values with FULL equal to `2`, and `foreign_keys` is a no-op when changed
inside a transaction. The transaction documentation confirms that
`BEGIN IMMEDIATE` starts the write transaction immediately.

An installed SQLite 3.50.6 probe over a fresh temporary database and a reopened
connection produced:

```text
setter_journal_mode=wal
fresh_journal_mode=wal
fresh_synchronous=2
fresh_foreign_keys=1
reopen_journal_mode=wal
reopen_foreign_keys_before_set=0
reopen_synchronous=2
reopen_foreign_keys_after_set=1
begin_immediate=ok
```

That proves why AD-16 correctly reasserts and reads back the connection-local
foreign-key property on every connection rather than relying on WAL's persistent
database property.

### GLIBC ABI and Oldest Runtime

GNU Binutils documents `readelf --version-info` as displaying the version
sections needed to inspect imported symbols. Installed GNU readelf 2.45 showed
the imported GLIBC requirements of `/usr/bin/true`, including a maximum of
`GLIBC_2.34`, which independently exercises the proposed gate on this glibc 2.42
host. AD-12 binds both the static version gate and the oldest-runtime smoke to
the exact final release artifact. That closes the common gap where a different
binary is inspected or smoked.

The smoke itself remains a required release-CI proof and cannot be executed in
an architecture-only worktree with no final release artifact. This review
accepts the completeness of the contract, not a nonexistent release result.

### Release Journal, Recovery, and KnownGood

Apart from TECH-CLEAN2-01, AD-23's write ordering matches the primary filesystem
semantics: unique same-directory temporary file, file fsync, atomic rename,
parent-directory fsync, and readback. Every external effect has pending and
complete journal cuts. Recovery republishes an owner before repeating an effect.

The irreversible `commit-decided` record is fsynced before KnownGood
publication. Before that decision recovery restores and validates the whole
prior binary/state/unit pair; after it, recovery can only finish KnownGood,
ready admission, and terminal commit. Explicit rollback is a new fully admitted
transaction rather than an unjournaled pointer swap. Those decisions are sound
once the admission lock is guaranteed to die with its actual owner.

### Managed systemd Units and Fresh Timer Proof

Installed systemd 257 primary manuals and D-Bus introspection expose the exact
properties named by AD-23:

- unit identity and load state: `FragmentPath`, `SourcePath`, `DropInPaths`,
  `UnitFileState`, and `NeedDaemonReload`;
- service definition and result: `ExecStart`, `RemainAfterExit`, `InvocationID`,
  `ExecMainStartTimestampMonotonic`, `Result`, `ExecMainCode`, and
  `ExecMainStatus`; and
- timer definition and trigger: `Unit`, `TimersMonotonic`, `TimersCalendar`,
  `LastTriggerUSecMonotonic`, `AccuracyUSec`, `RandomizedDelayUSec`,
  `FixedRandomDelay`, `Persistent`, `WakeSystem`, `RemainAfterElapse`, and
  `DeferReactivation`.

The installed `systemctl(1)` documentation confirms that `show` presents
normalized manager properties, `daemon-reload` reloads units and rebuilds the
dependency tree, and multi-unit `is-enabled` succeeds when any named unit is
enabled. AD-23 correctly requires one-unit calls with exact token and exit status
or exact D-Bus `UnitFileState`, never ActiveState or an any-enabled aggregate.

A read-only live-manager probe also demonstrated the hazard being controlled: an
enabled and active timer coexisted with stale failed service result fields and a
prior nonzero InvocationID. The contract's strict trigger advance, new nonzero
InvocationID, later start timestamp, identical terminal invocation, and explicit
success tuple are therefore all necessary. The symmetric forward and rollback
validators cover both generations.

### FD3 Ownership and EOF

Linux socket and descriptor documentation confirms that `SOCK_CLOEXEC` applies
close-on-exec to the initially returned descriptors, `dup` refers to the same
open file description but clears CLOEXEC on the new descriptor, and an open
duplicate can retain the endpoint until its final close. `SO_PEERCRED` and
`SO_PASSCRED` provide the peer and message credentials used by AD-25.

The independent socketpair probe observed CLOEXEC on both originals and not on a
raw duplicate. After the peer sent its payload and closed its original endpoint,
the receiver saw `NO_EOF` while the duplicate remained open and clean EOF
immediately after the last duplicate closed. AD-25's lifecycle table, post-spawn
audit, write shutdown, explicit close, and both injected-duplicate fixtures are
therefore sufficient for the FD3 channel itself.

### Schedule and Structural Uniqueness

An independent implementation of AD-10's descending-budget/ScopeId LPT compiler
replayed all named fixtures:

| Fixture | Epochs (s) | Process gate | Makespan | Cutoff |
| --- | --- | --- | ---: | ---: |
| default | `0,15,20,25` | `[25,35)` | 35 s | 40 s |
| near tie | `0,20` | `[20,30)` | 30 s | 35 s |
| process 60 s plus seven 1 s, configured margin 0 | `0,60` | `[0,60)` | 61 s | 61 s + 1 ns |

The near-tie schedule bytes and reservations remain identical when worker zero
terminalizes one nanosecond early. The compiler's persisted origin and absolute
deadlines therefore make the remediation event-independent as claimed.

The uniqueness parser expanded the brace path
`host/{cron,systemd,docker,pm2,process}.rs`, reconstructed full paths from the
tree indentation, and found 55 paths with zero duplicates. It also confirmed
exactly one `src/adapters/worker.rs`, exactly one `src/adapters/release.rs`, 25
unique ordered AD headings, and 23 unique ordered ARCH-LIM declarations.

## Primary Sources

- Rust official
  [stable manifest](https://static.rust-lang.org/dist/channel-rust-stable.toml),
  [Rust 1.97.1 announcement](https://blog.rust-lang.org/2026/07/16/Rust-1.97.1/),
  [Cargo `rust-version`](https://doc.rust-lang.org/stable/cargo/reference/rust-version.html),
  and official crates.io version metadata.
- Ratatui official
  [0.30.2 tagged manifest](https://raw.githubusercontent.com/ratatui/ratatui/ratatui-v0.30.2/Cargo.toml).
- SQLite official
  [PRAGMA](https://www.sqlite.org/pragma.html),
  [WAL](https://www.sqlite.org/wal.html), and
  [transaction](https://www.sqlite.org/lang_transaction.html) documentation.
- GNU Binutils official
  [`readelf`](https://sourceware.org/binutils/docs/binutils/readelf.html)
  documentation.
- systemd 257 official
  [`systemctl`](https://www.freedesktop.org/software/systemd/man/257/systemctl.html),
  [`systemd.timer`](https://www.freedesktop.org/software/systemd/man/257/systemd.timer.html),
  and
  [`org.freedesktop.systemd1`](https://www.freedesktop.org/software/systemd/man/257/org.freedesktop.systemd1.html)
  documentation, cross-checked with the installed systemd 257 manuals and
  manager.
- Linux man-pages official project copies for
  [`flock(2)`](https://man7.org/linux/man-pages/man2/flock.2.html),
  [`open(2)`](https://man7.org/linux/man-pages/man2/open.2.html),
  [`execve(2)`](https://man7.org/linux/man-pages/man2/execve.2.html),
  [`dup(2)`](https://man7.org/linux/man-pages/man2/dup.2.html),
  [`close(2)`](https://man7.org/linux/man-pages/man2/close.2.html),
  [`socketpair(2)`](https://man7.org/linux/man-pages/man2/socketpair.2.html),
  [`unix(7)`](https://man7.org/linux/man-pages/man7/unix.7.html),
  [`rename(2)`](https://man7.org/linux/man-pages/man2/rename.2.html), and
  [`fsync(2)`](https://man7.org/linux/man-pages/man2/fsync.2.html).

## Required Checks

All mandated mechanical checks pass on the reviewed base plus this report:

- architecture lint:
  `ok=true`, `total_findings=0`;
- canonical Markdown lint using the project profile: pass;
- `git diff --check`: pass;
- identifier uniqueness: 25 AD identifiers and 23 ARCH-LIM declarations,
  zero duplicates and no sequence gaps;
- Structural Seed uniqueness: 55 expanded full paths, zero duplicates;
- schedule replay: all three named fixtures and early-completion invariance
  pass; and
- restricted-change check: this review report is the only path changed from
  `300ad19`.

## Acceptance Gate

The next independent technology acceptance pass may return PASS only after
TECH-CLEAN2-01 is corrected normatively, the new descriptor-inheritance fixtures
pass, architecture lint remains clean, and no new finding is introduced.

Until then, the final technology acceptance verdict is **CHANGES REQUIRED**.
