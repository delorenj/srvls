---
title: "Final Technology Acceptance Review - srvls Architecture"
document_type: architecture_review
review_dimension: technology_final_acceptance
status: final
verdict: "CHANGES REQUIRED"
blocking: true
reviewed_commit: 8fd5d312fabe544163d9b57b6b933e56b5133414
review_date: 2026-07-16
reviewer: WidgetWhisperer
team: Team Argus
evidence_mode: fresh_primary_source_acceptance
scope: technology, versions, deployment, state, IPC, scheduling, and release recovery
finding_count: 5
blocking_findings: 5
high_findings: 4
medium_findings: 0
low_findings: 1
---

<!-- markdownlint-disable MD013 MD025 -->

# Final Technology Acceptance Review

## Verdict

**CHANGES REQUIRED.** Commit
`8fd5d312fabe544163d9b57b6b933e56b5133414` does not meet the requested
zero-finding acceptance gate. This fresh pass found **five findings**: four
high-severity release or runtime contract gaps and one low-severity structural
assignment collision.

The architecture is otherwise unusually complete. Rust 2024, resolver 3, MSRV
1.88, the dependency graph, SQLite WAL and pragma readbacks, canonical framing
and transport diagnostics, exact-artifact ABI proof, crash-persistent release
admission, journal ordering, public event mapping, retained KnownGood rollback,
recovery ownership, ordinary-startup refusal, and the exact default collection
schedule all survive this pass. They cannot produce a PASS while any finding
remains.

| Severity | Count | Finding IDs |
| --- | ---: | --- |
| High | 4 | `TECH-FINAL-01` through `TECH-FINAL-04` |
| Medium | 0 | None |
| Low | 1 | `TECH-FINAL-05` |
| Total | 5 | **CHANGES REQUIRED** |

## Review Identity and Basis

The reviewed Git object is exactly
`8fd5d312fabe544163d9b57b6b933e56b5133414`, whose subject is
`docs(architecture): integrate final acceptance remediation`. The worktree was
clean before report creation. No product crate, `Cargo.toml`, `Cargo.lock`, or
release artifact exists at this planning commit, so this is architecture
acceptance of assigned executable proof, not implementation acceptance.

The following artifacts were read completely through EOF:

- repository `AGENTS.md` and the available lowercase `tasks.md` task ledger
  (`TASKS.md` is not present in the reviewed tree);
- `.agents/skills/bmad-architecture/SKILL.md`,
  `references/headless.md`, and `references/reviewer-gate.md`;
- the architecture workspace `.memlog.md` and `ARCHITECTURE-SPINE.md`;
- final `prd.md` and its addendum;
- UX `DESIGN.md` and `EXPERIENCE.md`;
- the three 2026-07-16 technology, two-unit, and rubric acceptance reports; and
- all eighteen committed remediation reports: each technology, two-unit, and
  rubric family member named `gate`, `rerun`, `final`, `closure`,
  `reality-closure`, and `unanimous-closure`.

Prior approvals were treated as evidence to replay, not as authority over a
fresh result. Current claims were checked only against the reviewed repository,
official upstream documentation and manifests, or locally installed primary
manuals and binaries.

## Acceptance Matrix

`SPINE` below means
`_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md`
at the reviewed commit.

| Required audit | Result | Fresh acceptance evidence |
| --- | --- | --- |
| Rust 2024, resolver 3, MSRV lane | **ACCEPTED** | AD-12 binds edition 2024, explicit resolver 3, MSRV 1.88, locked MSRV tests, and a separate stable lane (`SPINE:508-517`). Ratatui 0.30.2 declares Rust 1.88. |
| Current-stable Rust lane | **FINDING** | The dated lock-target table says 1.97.0, while the official stable channel became 1.97.1 on the same review date (`TECH-FINAL-01`). |
| SQLite WAL and pragma readback | **ACCEPTED** | Initialization is outside a transaction, requires the WAL setter result, then per-connection `wal`, numeric synchronous `2`, foreign keys `1`, and busy timeout before any transaction (`SPINE:727-745`). |
| Unix FD3 stream and peer credentials | **PARTIAL** | `AF_UNIX SOCK_STREAM`, child-side `SO_PEERCRED`, parent-side `SO_PASSCRED` plus Ready `SCM_CREDENTIALS`, PID/birth/executable/group checks, and pre-Host refusal are explicit (`SPINE:1327-1375`). Duplicate endpoint ownership is not (`TECH-FINAL-04`). |
| Canonical framing and transport diagnostics | **ACCEPTED** | Direction, size caps, canonical payloads, EOF, total primary-reason order, failure cut, seven diagnostic parameters, and cleanup/reap non-rewrite are binding (`SPINE:1345-1577`). |
| Exact-artifact ELF ABI proof | **ACCEPTED** | The exact final artifact is checked with `readelf --version-info` against `GLIBC_2.42` and then run in the pinned oldest-supported glibc 2.42 image (`SPINE:508-517`). |
| systemd user service and timer pair | **FINDING** | Loaded timer configuration and enablement are not positively read back (`TECH-FINAL-02`), and trigger/status evidence does not prove a fresh candidate invocation (`TECH-FINAL-03`). |
| Crash-persistent release admission | **ACCEPTED** | A mode-checked, locked, atomically replaced admission record refuses every ordinary stateful entry before SQLite while recovery is pending (`SPINE:1049-1063`). |
| Release journal phase order | **ACCEPTED** | Each effect is preceded by fsynced `pending` evidence and followed by `complete` only after readback; pending is recovered as may-have-executed (`SPINE:1119-1154`). |
| Release event mapping | **ACCEPTED** | Every durable step maps to one public phase and canonical label; event projection and emission cuts are total (`SPINE:1202-1237`). |
| Retained KnownGood rollback | **ACCEPTED** | Commit decision precedes KnownGood publication, one verified prior pair remains pinned, and rollback is a new transaction through the same protocol (`SPINE:1168-1200`). |
| Recovery ownership | **ACCEPTED** | Exclusive lock capability plus gap-free attempt records, PID/birth/executable identity, predecessor checksum, and durable owner publication prevent competing recovery (`SPINE:1065-1084`). |
| Ordinary startup during pending upgrade | **ACCEPTED** | Every ordinary stateful path retains a shared lease and returns `upgrade-recovery-required` before SQLite or Host effects unless admission is ready and no transaction is nonterminal (`SPINE:1053-1063`). |
| Silent-30 versus ready siblings | **ACCEPTED** | Independent Ready lanes keep dispatching while one 30-second member remains silent; the deterministic trace is exactly 35 seconds (`SPINE:321-394`, `SPINE:448-457`, and the replay below). |
| Structural implementation seed | **FINDING** | The same `adapters/worker.rs` path is declared twice with competing responsibility descriptions (`TECH-FINAL-05`). |

## Findings

### TECH-FINAL-01 — The dated current-stable Rust target is stale

**Severity:** High

**Exact evidence.** The Stack says its versions are the reviewed 2026-07-16
lock targets, then records `Rust current-stable lane | 1.97.0 at review`
(`SPINE:1620-1626`). AD-12 separately requires a current-stable CI lane
(`SPINE:508-517`).

**Counterexample.** The official stable-channel manifest is dated 2026-07-16
and records `[pkg.rust] version = "1.97.1 (8bab26f4f 2026-07-14)"`. The Rust
Release Team's same-day announcement says 1.97.1 fixes an LLVM optimization
miscompilation and that a 1.97.0 IR change increased its likelihood. A cached
1.97.0 toolchain can therefore satisfy the literal table while failing the
architecture's current-stable claim.

**Primary source.** Rust's
[stable-channel manifest](https://static.rust-lang.org/dist/channel-rust-stable.toml)
and the Rust Release Team's
[Rust 1.97.1 announcement](https://blog.rust-lang.org/2026/07/16/Rust-1.97.1/).

**Impact.** The exact reviewed version claim is false at acceptance time. More
importantly, the superseding point release is compiler-correctness remediation;
accepting 1.97.0 as current stable weakens reproducibility and can admit an
artifact built with the known-higher-risk compiler.

**Required remediation.** Change the reviewed current-stable evidence to
1.97.1. Keep the symbolic stable lane, but require bootstrap/release CI to
refresh channel metadata and persist `rustc --version --verbose` plus the
stable manifest date before compiling. A cached 1.97.0 installation must fail
the dated current-stable evidence check.

### TECH-FINAL-02 — Loaded timer definition and enablement are not postconditions

**Severity:** High

**Exact evidence.** AD-12 stages the paired timer definition and enablement,
then validates only loaded service `ExecStart`, timer trigger advancement,
service `Result=success`, and `ExecMainStatus=0` (`SPINE:524-531`). AD-23 repeats
that consumer-validation proof set (`SPINE:1159-1165`). Neither rule requires a
comparison of the loaded timer target, schedule, delay/persistence settings, or
unit-file enablement with the transaction manifest.

**Counterexample.** Install a timer with the correct service but a one-second
cadence instead of five minutes, or leave the exact timer disabled while it is
still active in the current user-manager session. One activation can advance
`LastTriggerUSecMonotonic` and the service can return success. Every named
postcondition passes, but future cadence is wrong or the timer disappears after
the next login/reboot. A wrong `Unit=` can also combine with stale service
status from `TECH-FINAL-03` and pass without exercising the managed service.

**Primary source.** The installed systemd 257 `systemctl(1)` manual states that
`daemon-reload` reloads unit files and rebuilds the dependency tree; it does not
assert their intended values. It defines `is-enabled` as the unit-file
enablement readback. The installed `org.freedesktop.systemd1(5)` interface
exposes timer `Unit`, `TimersMonotonic`, `TimersCalendar`, `AccuracyUSec`,
`RandomizedDelayUSec`, `Persistent`, and related loaded properties. Equivalent
official references are the systemd 257
[systemctl manual](https://www.freedesktop.org/software/systemd/man/257/systemctl.html)
and
[D-Bus API](https://www.freedesktop.org/software/systemd/man/257/org.freedesktop.systemd1.html).

**Impact.** A release can commit and publish KnownGood while scheduled
automation is disabled, targets the wrong unit, or runs at the wrong cadence.
The rollback validator has the same blind spot, so a claimed whole-pair restore
can also leave automation broken.

**Required remediation.** After `systemctl --user daemon-reload`, compare a
normalized loaded service/timer property set to the manifest, including the
timer `Unit`, monotonic/calendar schedules, accuracy/random delay,
persistence/wake/reactivation properties as applicable, fragment identity, and
the exact expected `UnitFileState`/`is-enabled` result. Perform this before the
fresh activation proof. Add wrong-target, wrong-schedule, wrong-delay,
wrong-persistence, and disabled-but-active forward and rollback fixtures.

### TECH-FINAL-03 — Timer success is not correlated to a fresh candidate invocation

**Severity:** High

**Exact evidence.** The release rule observes timer trigger advancement and
then reads `Result=success` and `ExecMainStatus=0` (`SPINE:527-530`,
`SPINE:1159-1162`). It does not require the target service to be inactive before
the trigger, nor does it compare an invocation identity or main-process start
timestamp before and after the trigger.

**Counterexample.** Leave the target service active when its timer elapses.
systemd advances the timer, but does not restart an already-active target. The
service's `Result` and `ExecMainStatus` may still describe its current or last
successful run. Loaded `ExecStart` can point at the new candidate while all
three named observations pass without ever executing that candidate.

**Primary source.** The installed systemd 257 `systemd.timer(5)` manual says an
already-active target is not restarted when a timer elapses. The installed
`org.freedesktop.systemd1(5)` manual says `ExecMainStartTimestampMonotonic`,
`ExecMainCode`, and `ExecMainStatus` can describe the current or last run and
that service `Result` describes the last run. It also exposes `InvocationID`.
Equivalent official references are the systemd 257
[timer manual](https://www.freedesktop.org/software/systemd/man/257/systemd.timer.html)
and
[D-Bus API](https://www.freedesktop.org/software/systemd/man/257/org.freedesktop.systemd1.html).

**Impact.** A broken or non-executable candidate can be committed and replace
the KnownGood record even though no timer-originated candidate process ran.
This defeats the managed-consumer acceptance gate and FR-43 release safety.

**Required remediation.** Either prove the service inactive before triggering,
or record baseline `InvocationID` and `ExecMainStartTimestampMonotonic` and
require a new invocation/start strictly after the observed timer trigger.
Require the correlated invocation to terminate with `Result=success`,
`ExecMainCode=CLD_EXITED`, and `ExecMainStatus=0`. Add active-service,
`RemainAfterExit=yes`, and stale-success regression fixtures for both forward
validation and rollback revalidation.

### TECH-FINAL-04 — FD3 duplicate endpoint closure is unspecified

**Severity:** High

**Exact evidence.** AD-25 creates a stream socketpair and maps the child
endpoint to inherited FD3, but does not require the parent to close every copy
of the child endpoint or the child to close every copy of the parent endpoint
(`SPINE:1332-1347`). The FD4 validator rule explicitly closes every other copy
with close-on-exec (`SPINE:1086-1090`). FD3 result acceptance nevertheless
requires the complete Result payload to be followed by clean EOF
(`SPINE:1561-1569`).

**Counterexample.** A local socketpair replay duplicated the child endpoint,
sent a complete `done` payload, and closed the original child socket. The parent
received the payload but nonblocking read returned `NO_EOF`; only closing the
retained duplicate produced `b''` EOF:

```text
payload b'done'
before_duplicate_close NO_EOF
after_duplicate_close b''
```

That implementation still creates the required socketpair and maps the child
endpoint to FD3, but a syntactically valid result cannot cross the architecture's
EOF trust cut and eventually becomes `worker-timeout`.

**Primary source.** The installed Linux man-pages `dup(2)` states that a
duplicate refers to the same open file description; `close(2)` frees the
underlying resources only when the last referring descriptor closes; and
`socketpair(2)` defines the connected pair. Online primary copies are
[dup(2)](https://man7.org/linux/man-pages/man2/dup.2.html),
[close(2)](https://man7.org/linux/man-pages/man2/close.2.html), and
[socketpair(2)](https://man7.org/linux/man-pages/man2/socketpair.2.html).

**Impact.** A conforming-looking spawn implementation can turn every otherwise
valid worker result into a timeout. The failure is batch-sensitive, difficult
to diagnose from the child, and directly breaks collection completeness and
the 35-second scheduling contract.

**Required remediation.** Give FD3 an explicit post-spawn descriptor ownership
table. Require close-on-exec at creation; retain exactly the parent endpoint in
the coordinator and exactly FD3 in the worker; close every original and
duplicate opposite endpoint in both processes before Hello; close or
write-shutdown FD3 after the one Result; and close the parent endpoint after the
EOF cut. Add injected duplicate-parent-end and duplicate-child-end fixtures
that prove clean EOF cannot be suppressed.

### TECH-FINAL-05 — The structural seed assigns one adapter path twice

**Severity:** Low

**Exact evidence.** The Structural Seed lists
`adapters/worker.rs # authenticated FD3 parent/child protocol` at
`SPINE:1679`, then lists the same `adapters/worker.rs` path again as
`FD3/FD4 authentication, framing, child entry` at `SPINE:1682`.

**Counterexample.** One implementation story can reasonably assign the first
entry as an FD3-only transport adapter while a release story assigns the second
entry as a separate FD4 validator adapter. Git can contain only one file at
that path, so the two stories collide or one silently drops responsibility.

**Primary source.** The reviewed commit's own `ARCHITECTURE-SPINE.md` structural
seed is the authoritative implementation mapping for this finding.

**Impact.** This does not itself create a runtime defect, but it makes module
ownership and story boundaries non-unique precisely where FD3 and FD4 have
different authentication and lifecycle rules.

**Required remediation.** Either consolidate the two comments into one unique
`adapters/worker.rs` entry with explicit FD3 and FD4 responsibilities, or split
them into uniquely named modules such as `worker_transport.rs` and
`release_validator_transport.rs`. Update story ownership and tests to match the
chosen unique paths.

## Exact Default-Schedule Replay

The deterministic LPT simulation sorted the frozen defaults
`[30,20,15,15,10,10,10,process=10]` by descending deadline and ScopeId, then
replayed four worker slots with independent Ready lanes.

| Time | Worker 0 | Worker 1 | Worker 2 | Worker 3 |
| --- | --- | --- | --- | --- |
| `t=0` | 30-second member, silent | 20-second ready member | 15-second ready member | 15-second ready member |
| `t=15` | still silent | still running | first 10-second member to `t=25` | second 10-second member to `t=25` |
| `t=20` | still silent | third 10-second member to `t=30` | running | running |
| `t=25` | still silent | running | process 10-second member to `t=35`; process spawn gate closes with no queued successor | idle under barrier |
| `t=30` | silent member times out | 10-second member completes | process running | idle |
| `t=35` | free | free | process completes | free |

The maximum completion is exactly **35 seconds**. The five-second margin gives
the configured 40-second cutoff. The silent 30-second lane neither delays the
ready siblings nor changes the final process dispatch. The separate
60-second-process plus seven one-second scopes counterexample also resolves to
61 seconds; a 61-second cutoff fails the mandatory half-open one-nanosecond
headroom, while 61 seconds plus one nanosecond is admissible.

## Accepted Technology and Recovery Proofs

### Rust, dependency graph, and ABI

- Edition 2024, resolver 3, and the declared MSRV are mutually compatible.
  Ratatui 0.30.2 is non-yanked and declares Rust 1.88; its tagged manifest uses
  Crossterm 0.29. The reviewed dependency pins exist, and `time` 0.3.53 also
  keeps the effective floor at 1.88.
- `rusqlite = "=0.39.0"` selects `libsqlite3-sys` 0.37 and its bundled SQLite
  3.51.3 source. The TOML package's published build metadata does not invalidate
  the documented `=1.1.3` Cargo requirement.
- The ABI gate is correctly applied to the exact final release artifact, not a
  nearby build. GNU `readelf --version-info` exposes ELF version sections; the
  threshold check plus smoke in the oldest supported glibc 2.42 image is an
  adequate proof for the chosen lane.

### SQLite state

SQLite documents that setting `journal_mode` returns the resulting mode and
that an unsuccessful WAL transition returns the prior mode. It also documents
numeric synchronous value `2` as FULL and that changing `foreign_keys` inside a
transaction is a no-op. AD-16's ordered, outside-transaction setter/readback
sequence therefore fails closed at the correct boundary. `BEGIN IMMEDIATE`
then provides the intended early writer reservation.

### IPC framing and diagnostics

Apart from `TECH-FINAL-04`, the FD3 contract is acceptance-ready. Linux
`SO_PEERCRED` authenticates the socketpair peer at connection creation, while
receiver-side `SO_PASSCRED` supplies kernel `SCM_CREDENTIALS` for the Ready
message. The same-executable and owned-spawn checks close the remaining process
identity gap. CanonicalJsonV1, declared field order, exact four-frame direction,
payload limits, strict deadlines, EOF, wait-status precedence, and the complete
diagnostic matrix make transport results deterministic and byte-comparable.

### Release state and recovery

The release protocol has one recovery owner, one durable admission gate, and
one ordered effect journal. A crash cannot make ordinary stateful startup open
SQLite while an upgrade is pending. Pre-decision recovery restores the prior
whole pair; post-decision recovery must finish KnownGood publication, ready
admission, and terminal commit in order. KnownGood is retained rather than
repointed, and explicit rollback is itself a newly admitted, validated,
journaled transaction. The public event mapping covers every internal step and
does not infer completion from phase names.

## Primary Sources and Local Proof Record

Primary official or locally installed references used in this pass:

- Rust
  [stable manifest](https://static.rust-lang.org/dist/channel-rust-stable.toml),
  [1.97.1 announcement](https://blog.rust-lang.org/2026/07/16/Rust-1.97.1/),
  [2024 resolver guidance](https://doc.rust-lang.org/stable/edition-guide/rust-2024/cargo-resolver.html),
  and Cargo's
  [`rust-version` contract](https://doc.rust-lang.org/stable/cargo/reference/rust-version.html);
- Ratatui's
  [0.30.2 tagged manifest](https://raw.githubusercontent.com/ratatui/ratatui/ratatui-v0.30.2/Cargo.toml)
  and official crates.io version metadata;
- SQLite
  [PRAGMA](https://www.sqlite.org/pragma.html),
  [WAL](https://sqlite.org/wal.html), and
  [transaction](https://www.sqlite.org/lang_transaction.html) documentation;
- GNU Binutils
  [`readelf` manual](https://sourceware.org/binutils/docs/binutils/readelf.html);
- installed Linux man-pages 6.9.1 for `unix(7)`, `socketpair(2)`, `dup(2)`,
  `close(2)`, `clock_gettime(3)`, `flock(2)`, `rename(2)`, and `fsync(2)`;
- installed systemd 257 manuals for `systemd.timer(5)`, `systemctl(1)`, and
  `org.freedesktop.systemd1(5)`, cross-linked above to the official systemd 257
  copies; and
- the freedesktop.org
  [XDG Base Directory specification](https://specifications.freedesktop.org/basedir-spec/latest/).

Observed local primary-tool versions were Rust/Cargo 1.95.0 for the active
directory override, SQLite CLI 3.50.6, GNU readelf 2.45, glibc 2.42, and systemd
257. Local version skew was used only to identify executable proof boundaries;
it was never substituted for official current-stable or bundled-library
metadata.

Deterministic proof commands completed as follows:

- architecture spine lint: `ok=true`, `total_findings=0`;
- independent schedule replay: `makespan 35`;
- retained-FD socketpair replay: `NO_EOF` before last duplicate close and EOF
  immediately after it;
- Markdown lint of this report: pass; and
- `git diff --check`: pass.

## Closure Gate

PASS requires all five findings to be remediated in the normative spine and
replayed against the same official or installed-primary evidence. The rerun
must show:

1. current stable is refreshed to 1.97.1 or the then-current official channel;
2. loaded service and timer definitions plus enablement match the manifest;
3. timer success is correlated to a fresh candidate invocation;
4. FD3 endpoint-copy ownership makes the required EOF inevitable; and
5. every Structural Seed path is unique.

Until then, the final technology acceptance verdict remains **CHANGES
REQUIRED**.
