---
title: Technology Currency Review - srvls Architecture
document_type: architecture_review
review_dimension: technology_currency
status: final
verdict: CHANGES REQUIRED
reviewed_commit: 799fc092f5d35149e082cce7efab2f6f2a189c99
review_date: 2026-07-16
reviewer: WidgetWhisperer
team: Team Argus
evidence_mode: independent evidence transcription
scope: architecture technology choices, compatibility, and deployment migration
---

## Verdict

**CHANGES REQUIRED.** Rust 2024, MSRV 1.88, the selected terminal and
serialization ecosystem, bundled SQLite, and a one-binary release are viable
architectural directions. The reviewed dependency set is not currently
compatible with the declared MSRV, however, and the live absolute-path systemd
consumers make an in-place binary migration unsafe unless the installer owns
their discovery, rewrite, validation, and rollback.

The two Tier 0 findings are release blockers. The architecture must pin
`rusqlite = "=0.39.0"` while retaining MSRV 1.88, and it must explicitly define
the migration of absolute-path consumers. Tier 1 findings close correctness
ambiguities. Tier 2 findings require bootstrap and release proof before the
architecture can be considered implementation-ready.

## Review Scope and Evidence Semantics

This review records already-completed independent evidence for reviewed commit
`799fc092f5d35149e082cce7efab2f6f2a189c99`. It does not claim that a Rust
product, lockfile, CI lane, or release artifact currently exists.

Labels used below:

- **Confirmed fact**: directly established by the completed evidence.
- **Architecture choice**: a support or behavior decision the architecture must
  make and enforce.
- **Inference**: a conclusion supported by the evidence but not itself a live
  product guarantee.
- **Unsupported claim**: not proven by an existing repository artifact or by
  the completed validation record.

## Claim-by-Claim Matrix

| ID | Claim | Classification | Assessment | Required disposition |
| --- | --- | --- | --- | --- |
| C01 | Rust 2024 is usable for the product. | Confirmed fact | Valid with Cargo resolver 3. | Retain and declare explicitly. |
| C02 | MSRV 1.88 is a valid baseline. | Architecture choice | Valid only after dependency remediation. | Retain; test it as a locked lane. |
| C03 | The current exact graph supports MSRV 1.88. | Unsupported claim | False for `libsqlite3-sys 0.38.1`. | Pin `rusqlite = "=0.39.0"`. |
| C04 | Stable toolchains 1.95 and 1.97 pass the representative graph. | Confirmed fact | Passed all-target and release probes. | Record as evidence, not MSRV proof. |
| C05 | `x86_64-unknown-linux-gnu` is supported. | Confirmed fact | Supported Rust target. | Retain as the named release target. |
| C06 | Host glibc is 2.42. | Confirmed fact | Host observation only. | Do not convert it into a support floor. |
| C07 | All requested crate pins exist and are non-yanked. | Confirmed fact | Verified with requested features. | Retain, subject to C03 and C09. |
| C08 | `rusqlite 0.40.1` supports Rust 1.88. | Unsupported claim | Transitive build script requires 1.95. | Replace only this pin with 0.39.0. |
| C09 | TOML can be required as `=1.1.3+spec-1.1.0`. | Unsupported claim | Cargo ignores SemVer build metadata. | Use `toml = "=1.1.3"`; document spec separately. |
| C10 | Bundled rusqlite uses Host SQLite. | Unsupported claim | Bundled mode selects embedded SQLite. | State embedded-version ownership explicitly. |
| C11 | WAL, FULL, foreign keys, and immediate transactions are compatible. | Confirmed fact | Compatible deliberate settings. | Specify ordering and verification. |
| C12 | `synchronous=FULL` means value 2. | Confirmed fact | Correct SQLite pragma value. | Verify value after configuration. |
| C13 | A single GNU PIE binary is feasible. | Inference | Representative release supports feasibility. | Require reproducible release proof. |
| C14 | Building on glibc 2.42 makes 2.42 the binary floor. | Unsupported claim | Observed imports were no newer than 2.34. | Choose and enforce a target baseline. |
| C15 | systemd automatically gives actions the architecture's limits. | Unsupported claim | Manager defaults are 90 seconds. | Encode action-specific policy explicitly. |
| C16 | Rust `Instant` defines suspend-inclusive lease time. | Unsupported claim | Suspend behavior is unspecified. | Name Linux `CLOCK_BOOTTIME`. |
| C17 | Existing `srvls` consumers all follow shell resolution. | Unsupported claim | User units bypass it with absolute paths. | Inventory and migrate every bypass consumer. |
| C18 | The current user-unit target is executable. | Confirmed fact | It is a 31-byte non-executable regular file. | Treat as failed live consumer state. |
| C19 | Active timers demonstrate successful execution. | Unsupported claim | Metrics latest result is exit 126. | Validate timer-triggered execution. |
| C20 | Product bootstrap artifacts already prove the architecture. | Unsupported claim | No manifest, lockfile, source, CI, or release exists. | Bootstrap before Provider work. |

## Dependency Currency Record

The requested pins exist, are non-yanked, and expose the requested features:

- [`ratatui 0.30.2`](https://crates.io/crates/ratatui), through
  [`ratatui-crossterm 0.1.2`](https://crates.io/crates/ratatui-crossterm) and
  [`crossterm 0.29`](https://crates.io/crates/crossterm);
- [`clap 4.6.2`](https://crates.io/crates/clap);
- [`serde 1.0.228`](https://crates.io/crates/serde) and
  [`serde_json 1.0.150`](https://crates.io/crates/serde_json);
- [`rusqlite 0.40.1`](https://crates.io/crates/rusqlite), with the compatibility
  exception described below;
- [`toml 1.1.3+spec-1.1.0`](https://crates.io/crates/toml), manifested as
  version `=1.1.3`;
- [`uuid 1.24.0`](https://crates.io/crates/uuid) with UUID v7 and Serde features;
- [`time 0.3.53`](https://crates.io/crates/time);
- [`thiserror 2.0.18`](https://crates.io/crates/thiserror);
- [`tracing 0.1.44`](https://crates.io/crates/tracing) and
  [`tracing-subscriber 0.3.23`](https://crates.io/crates/tracing-subscriber);
- [`signal-hook 0.4.4`](https://crates.io/crates/signal-hook);
- [`strsim 0.11.1`](https://crates.io/crates/strsim); and
- [`insta 1.48.0`](https://crates.io/crates/insta).

Crate existence and published versions are directly represented by the
[crates.io crate pages](https://crates.io/crates).

## Tier 0 - Release Blockers

### T0.1 - `rusqlite 0.40.1` Breaks the Declared MSRV

The representative exact dependency graph passes on Rust 1.95 and installed
stable Rust 1.97. It fails on Rust 1.88 only in `libsqlite3-sys 0.38.1`, selected
by `rusqlite 0.40.1`. Its build script uses `cfg_select`, which is stable only
since Rust 1.95. Cargo accepted the graph because that dependency omits its true
`rust-version`; dependency resolution therefore did not protect the declared
MSRV. See Cargo's [`rust-version` reference](https://doc.rust-lang.org/cargo/reference/rust-version.html)
and the standard library [`cfg_select` macro](https://doc.rust-lang.org/std/macro.cfg_select.html).

Exact remediation:

1. Retain package `edition = "2024"` and `rust-version = "1.88"`.
2. Set the direct manifest requirement to `rusqlite = "=0.39.0"` with the
   architecture's required features, including `bundled`.
3. Generate and commit `Cargo.lock`; confirm it selects
   `libsqlite3-sys 0.37.0`.
4. Run locked all-target tests and a locked release build on Rust 1.88.
5. Run the same locked checks on the current stable lane.
6. Reject dependency updates unless both lanes remain green.

Changing only rusqlite to 0.39.0 selects `libsqlite3-sys 0.37.0` and passes the
same Rust 1.88 all-target tests and release probe. Its bundled SQLite is 3.51.3,
whose official [3.51.3 release log](https://sqlite.org/releaselog/3_51_3.html)
includes the WAL-reset corruption fix. This is the required remediation while
retaining MSRV 1.88.

### T0.2 - Absolute-Path Consumers Make Installation Unsafe

Live shell resolution is `~/.local/bin/srvls` to
`/home/delorenj/code/srvls/srvls`. The user units `srvls-metrics.service` and
`srvls-snapshot.service` instead call `/home/delorenj/code/infra/bin/srvls`.
That target is a 31-byte non-executable regular file. Both timers are active,
and the metrics unit's latest result is exit 126.

Exact remediation for the installer and rollback design:

1. Inventory shell-resolved entry points, symlinks, service definitions,
   timers, and every absolute path that bypasses shell lookup.
2. Classify each consumer as managed, migrated, intentionally retained, or
   blocked; require an explicit disposition for every discovered consumer.
3. Snapshot the binary, symlink, unit files, timer files, enablement state, and
   application state needed for rollback.
4. Install the versioned binary atomically and update the managed shell entry
   point.
5. Rewrite both managed user services to the canonical installed binary path.
6. Run `systemctl --user daemon-reload`, then verify loaded unit definitions,
   executability, service invocation, timer invocation, and exit status.
7. On failure, restore consumer definitions, binary, symlink, enablement state,
   and application state as one rollback operation; daemon-reload and recheck.

Active timers are not success evidence. Completion requires a successful
timer-triggered run from each rewritten unit, not merely successful installation
or manual execution.

## Tier 1 - Correctness Requirements

### T1.1 - Correct TOML Manifest Syntax

Cargo ignores SemVer build metadata in dependency requirements. The manifest
must use `toml = "=1.1.3"`. The architecture may separately state that this
release implements TOML specification 1.1.0; `+spec-1.1.0` must not be treated
as a version-selection constraint.

### T1.2 - Name `CLOCK_BOOTTIME` for Lease Semantics

Rust documents [`std::time::Instant`](https://doc.rust-lang.org/std/time/struct.Instant.html)
without specifying consistent suspend behavior across platforms. Linux
[`clock_gettime(2)`](https://man7.org/linux/man-pages/man2/clock_gettime.2.html)
defines `CLOCK_BOOTTIME` as including time while the system is suspended.

Exact remediation: define lease age and expiry on Linux using
`CLOCK_BOOTTIME`; wrap the clock behind an injectable interface; use the same
clock domain for acquisition, renewal, comparison, and tests; document Linux as
the behavioral target. Do not describe plain Rust `Instant` as guaranteeing
suspend-inclusive behavior.

### T1.3 - Specify SQLite Pragma Ordering and Verification

Bundled rusqlite chooses its embedded SQLite rather than Host SQLite; see the
[rusqlite bundled-feature documentation](https://docs.rs/rusqlite/latest/rusqlite/#optional-features).
WAL, `synchronous=FULL`, foreign keys, and `BEGIN IMMEDIATE` are compatible,
deliberate settings. SQLite documents
[WAL](https://sqlite.org/wal.html),
[`foreign_keys`](https://sqlite.org/pragma.html#pragma_foreign_keys), and
[transaction modes](https://sqlite.org/lang_transaction.html).

Exact remediation for every opened connection:

1. Set and verify `journal_mode=WAL` during controlled initialization.
2. Set `synchronous=FULL` and verify the returned numeric value is `2`.
3. Set `foreign_keys=ON` before every transaction begins.
4. Read back `foreign_keys` and fail closed unless it is `1`.
5. Begin write-critical sections with `BEGIN IMMEDIATE` only after pragma
   configuration and verification.
6. Integration-test the ordering on fresh and existing databases.

## Tier 2 - Proof and Support-Baseline Gaps

### T2.1 - Bootstrap Proof Does Not Yet Exist

No `Cargo.toml`, `Cargo.lock`, Rust product source, CI workflow, or release
artifact exists yet. Consequently, repository-current claims about locked MSRV
compatibility, current-stable compatibility, release shape, or dependency
reproducibility are unsupported.

The bootstrap story must precede Provider work and must create those artifacts.
Its acceptance evidence is a committed lockfile plus locked all-target tests and
locked release builds on Rust 1.88 and current stable. Rust 2024 should use
[resolver version 3](https://doc.rust-lang.org/edition-guide/rust-2024/cargo-resolver.html)
and declare the MSRV through Cargo's `rust-version` field.

### T2.2 - glibc Support Floor Is an Architecture Choice

The host uses glibc 2.42. A representative release built there was an x86-64
GNU PIE and imported no symbol newer than `GLIBC_2.34`. That demonstrates
feasibility for the sampled graph; it does not establish a durable deployment
baseline.

Exact remediation: choose the oldest supported glibc baseline; build in a
pinned image matching that baseline; retain `x86_64-unknown-linux-gnu` as the
named target; inspect the final binary with `readelf`; fail CI if imported GLIBC
symbol versions exceed the chosen floor; smoke-test on the oldest supported
runtime. Installed stable Rust 1.97 and the current shell override Rust 1.95 are
toolchain observations, not deployment-baseline decisions.

## systemd Timeout Policy

The compiled and effective systemd manager defaults are 90 seconds. The
architecture's action limits are its own policy and are not inherited
automatically. The implementation must encode explicit per-unit or per-action
timeouts and test their failure behavior. Relevant primary references are the
[systemd source defaults](https://github.com/systemd/systemd/blob/main/src/core/system.conf.in)
and [`systemd-system.conf`](https://www.freedesktop.org/software/systemd/man/latest/systemd-system.conf.html).

## Validation Record

| Validation | Result | Meaning |
| --- | --- | --- |
| Rust 2024 with MSRV 1.88 | Valid choice | Requires the remediated locked graph. |
| Installed stable toolchain | Rust 1.97 | Representative graph passed. |
| Current shell override | Rust 1.95 | Representative graph passed. |
| Original exact graph on 1.88 | Failed | Only `libsqlite3-sys 0.38.1` failed. |
| `rusqlite 0.39.0` graph on 1.88 | Passed | All-target tests and release probe passed. |
| Target | Supported | `x86_64-unknown-linux-gnu`. |
| Host libc | glibc 2.42 | Observation, not chosen support floor. |
| Representative release format | Passed | x86-64 GNU PIE. |
| Representative GLIBC imports | Passed sample | No imported symbol newer than 2.34. |
| systemd manager defaults | Confirmed | Compiled and effective values are 90 seconds. |
| Live shell command path | Confirmed | Resolves through `~/.local/bin/srvls`. |
| Absolute user-unit target | Failed | Non-executable 31-byte regular file. |
| Timer state | Active but unhealthy | Metrics latest result is exit 126. |
| Product bootstrap artifacts | Absent | No manifest, lockfile, source, CI, or release. |

## Approval Gate

Re-review may return **APPROVED** only when both Tier 0 remediations are present
in the architecture, all Tier 1 semantics are explicit, and the Tier 2
bootstrap and support-baseline proof is assigned to acceptance-testable work.
Until then, the technology direction is feasible but the architecture is not
safe to implement as written.
