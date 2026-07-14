# Architecture Review — Technology, Versions, and Operations

**Artifact reviewed:** `ARCHITECTURE-SPINE.md`  
**Review date:** 2026-07-14  
**Verdict:** **CHANGES REQUIRED** before implementation starts

The overall technology choice and architectural fit are good for this utility: a single Rust binary, ratatui with its default Crossterm backend, hexagonal host adapters, typed commands, deterministic fixture tests, and a synchronous execution model are proportionate. The version matrix has one build-blocking contradiction, however, and the timeout/release/host-environment contracts are not yet strong enough to support the operational claims made by AD-10 and AD-12.

## Executive Findings

| Severity | Finding | Required disposition |
| --- | --- | --- |
| Blocker | `ratatui 0.30.2` requires Rust 1.88, but AD-12 and the stack fix MSRV/toolchain at Rust 1.85/1.85.1. | Raise MSRV to 1.88 and test it, or downgrade ratatui. Raising MSRV is recommended. |
| High | Scoped threads plus "cancellation by result abandonment" cannot guarantee the stated deadlines or prevent runaway child processes. | Make child termination/reaping part of `CommandRunner`; make collector concurrency bounded independently of scoped-thread abandonment. |
| High | Deployment/release is named but not designed: target ABI, install/upgrade path, artifact integrity, rollback, and timer migration are absent. | Add a compact release/install operations decision and acceptance checks. |
| Medium | Privilege and host capability behavior is abstracted but not specified per adapter. | Define non-interactive privilege rules, environment ownership, capability probes, and diagnostic mapping. |
| Medium | TUI backend/lifecycle and CI version policy are implicit. | Explicitly select ratatui's Crossterm feature, `ratatui::run`, and an MSRV plus current-stable CI matrix. |

## 1. Blocker — Ratatui and MSRV are incompatible

The spine simultaneously specifies:

- AD-12: MSRV 1.85 (line 115)
- stack: Rust toolchain 1.85.1 / MSRV 1.85 (line 134)
- stack: ratatui 0.30.2 (line 136)

The live crates.io sparse-index record for `ratatui 0.30.2` declares `rust_version = 1.88.0`. The same live index reports `clap 4.6.1` at Rust 1.85 and confirms the other named crate versions are current and compatible with lower Rust versions. The local `rustc` on `PATH` reports 1.85.1, so the proposed project cannot compile locally as written.

Evidence command used:

```bash
curl -A 'cargo/1.85.1' -fsSL https://index.crates.io/ra/ta/ratatui \
  | jq 'select(.vers == "0.30.2") | {vers, rust_version}'
# {"vers":"0.30.2","rust_version":"1.88.0"}
```

Primary references: [crates.io sparse index](https://index.crates.io/ra/ta/ratatui), [Cargo `rust-version` reference](https://doc.rust-lang.org/stable/cargo/reference/rust-version.html), [Ratatui installation](https://ratatui.rs/installation/).

**Recommendation:** keep ratatui 0.30.2 and raise `package.rust-version` and the tested MSRV to 1.88. Pin a build toolchain independently if desired; do not describe the development toolchain and MSRV as one field. Add `rust-toolchain.toml` only if this repository wants a reproducible contributor toolchain. CI should build/test once with 1.88 and once with current stable.

The lower-cost alternative is ratatui 0.29.0, whose registry metadata declares Rust 1.74, but that discards the 0.30 lifecycle API and modular release the design appears to want. A prerelease 0.30 build compatible with 1.85 is not an appropriate production pin.

Rust 2024 edition itself is correct: it stabilized with Rust 1.85. It does not make the ratatui 0.30.2 MSRV lower. [Rust Cargo reference](https://doc.rust-lang.org/cargo/?search=edition).

## 2. High — The timeout/cancellation model is not implementable as stated

AD-10 says scoped worker threads and channels provide per-operation deadlines with "cancellation by result abandonment" (line 103). That mechanism does not cancel scoped work:

- Every unjoined `std::thread::scope` worker is automatically joined before the scope returns. A stuck collector still holds up snapshot completion even if its receiver/result is abandoned. [Rust scoped threads](https://doc.rust-lang.org/std/thread/fn.scope.html).
- Dropping `std::process::Child` neither kills nor waits for the process. It may continue running, and an exited but unreaped child can remain a zombie. [Rust `Child`](https://doc.rust-lang.org/std/process/struct.Child.html).
- The standard library has `try_wait`, `kill`, and `wait`, but no single blocking `wait_timeout` primitive. Captured stdout/stderr must also be drained without deadlocking while respecting output caps.

This contradicts AD-10's stated prevention of runaway children and weakens refresh/quit behavior in the long-running TUI.

**Recommendation:** preserve the synchronous architecture, but strengthen `CommandRunner` to own the entire child lifecycle:

1. Spawn with piped output and a hard output cap.
2. Poll `try_wait` to the deadline, or use a small established wait-timeout implementation.
3. On timeout or cancellation, terminate the process (and process group where a provider can spawn descendants), then always `wait` to reap it.
4. Return a typed `TimedOut` diagnostic including provider and elapsed duration, never command secrets/output.
5. Limit in-flight collectors with a fixed-size worker set; dropping a result may suppress a stale UI update, but must not be described as cancellation.
6. Define quit/refresh semantics: a newer refresh supersedes presentation of an older snapshot, while its host children are still terminated/reaped by their own deadlines.

This can be implemented without Tokio. The important correction is that deadlines live at the subprocess boundary, not at the channel receiver.

## 3. High — Release and installation operations are underspecified

AD-12 promises "one locked Linux binary" and the capability map names a CI workflow, but the spine does not choose:

- release target (`x86_64-unknown-linux-gnu` versus musl) or minimum glibc baseline;
- whether the artifact is built in CI or on the target host;
- artifact naming, version reporting, checksums, and provenance;
- install location and atomic upgrade/rollback;
- how the existing `~/.local/bin/srvls` symlink moves from the repository Python file to the Rust binary;
- whether current systemd user timers keep resolving the same executable and receive a post-upgrade smoke test.

The current production recipe depends on the stable command name and redirects `--prom` and `--md` from systemd user services. An implementation can be correct while deployment silently continues executing the old Python file.

**Recommendation:** add a small deployment decision, not a packaging framework:

- Initial supported target: `x86_64-unknown-linux-gnu`, built on a declared glibc baseline matching big-chungus; add musl only if portability is actually needed.
- Release asset: `srvls-<version>-x86_64-unknown-linux-gnu.tar.gz` plus SHA-256 checksum.
- Binary exposes `srvls --version`; Cargo package version remains aligned with the existing git-tag version source.
- Install by copying to a versioned path under `~/.local/lib/srvls/<version>/srvls`, then atomically replacing `~/.local/bin/srvls`; retain the previous binary for rollback.
- Post-install validation runs `--version`, `--json`, `--prom`, and `--md`, verifies no ANSI on redirected output, then invokes the two existing timer services once before observing their next schedules.
- CI gates use `cargo fmt --check`, `cargo clippy --locked --all-targets -- -D warnings`, `cargo test --locked --all-targets`, an MSRV build, current-stable build, and release artifact smoke test.

Committing `Cargo.lock` is correct for an application binary. Build and CI commands should use `--locked` so the lock is enforced rather than merely present. [Cargo resolver and lock behavior](https://doc.rust-lang.org/cargo/reference/resolver.html#dependency-updates).

## 4. Medium — Host environment and privilege contracts need explicit policy

AD-3 correctly centralizes privilege behavior, and AD-5 correctly makes denied/unavailable collectors visible. The concrete operating policy is still missing, even though behavior differs materially by provider:

- root cron currently uses `sudo -n`; retaining `-n` is essential so a collector or TUI refresh never blocks on a password prompt;
- system-scope mutations currently use `sudo systemctl`; these should also be non-interactive by default, with denial represented explicitly;
- user systemd requires the invoking user's user-manager environment and should not be run after elevating the entire binary;
- Docker access inherits local socket/context policy and may be denied even when the CLI exists;
- PM2 inventory belongs to the invoking user's daemon/`PM2_HOME`;
- `systemctl --output=json` and provider output shapes vary by installed host-tool capability.

**Recommendation:** specify that the binary never elevates itself. Each adapter probes executable presence and required command capability, uses the invoking user's environment, and asks `CommandRunner` for only the narrow argv needed. Root/system actions use `sudo -n` unless an explicit interactive escalation mode is later designed. Map missing executable, unsupported output capability, daemon unavailable, permission denied, timeout, parse failure, and nonzero exit into distinct diagnostics. Record tool version/capability in provenance or debug logs, but do not log cron command bodies or secrets.

For the first release, test against the actual big-chungus versions of systemd, Docker CLI/daemon, PM2, cron, sudo, and glibc, and preserve scrubbed outputs as adapter fixtures. This is more durable than declaring broad minimum versions without evidence.

## 5. Medium — Make the Ratatui runtime and dependency policy explicit

Ratatui 0.30.2 enables its Crossterm backend by default, so a separate backend dependency is not inherently missing. The spine should nevertheless record the selected feature set because backend choice determines input events, terminal setup, and binary dependencies. [Ratatui installation](https://ratatui.rs/installation/).

Use `ratatui::run` as the application lifecycle boundary. In 0.30 it initializes the Crossterm terminal, installs terminal-restoring panic behavior, runs the closure, and restores the terminal on exit/panic. Any custom tracing/panic hook must be installed before it so restoration wraps the hook. [Ratatui terminal lifecycle](https://docs.rs/ratatui/0.30.2/ratatui/struct.Terminal.html).

Also distinguish requirements from resolutions:

- `Cargo.toml` should normally use compatible requirements for the selected major/minor lines.
- `Cargo.lock` records the exact reviewed resolution shown in the stack table.
- CI uses `--locked`.
- Dependency updates are deliberate and re-run MSRV plus golden/snapshot tests.

The currently named versions were checked against the live registry on 2026-07-14: clap 4.6.1, serde 1.0.228, serde_json 1.0.150, thiserror 2.0.18, tracing 0.1.44, tracing-subscriber 0.3.23, and insta 1.48.0 are current non-yanked releases. Ratatui 0.30.2 is also current; only its stated MSRV conflicts with the spine.

## Approval Conditions

The spine is ready for implementation when these four load-bearing changes are made:

1. Resolve ratatui/MSRV to **ratatui 0.30.2 + Rust 1.88 minimum** (recommended), and separate MSRV from development toolchain pinning.
2. Replace result-abandonment cancellation with an explicit child kill-and-reap deadline contract and bounded collector scheduling.
3. Add the minimal Linux target, artifact, atomic install/rollback, timer migration, and locked CI decisions.
4. State per-adapter non-interactive privilege/capability probing and diagnostic behavior.

No framework expansion, daemon, async runtime, dynamic plugins, or multi-crate workspace is needed to satisfy this review.
