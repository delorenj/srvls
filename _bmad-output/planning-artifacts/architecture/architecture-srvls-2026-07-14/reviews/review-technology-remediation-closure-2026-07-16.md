---
title: "Technology Remediation Closure Gate - srvls Architecture"
document_type: architecture_review
review_dimension: technology_remediation_closure
status: final
verdict: "CHANGES REQUIRED"
blocking: true
reviewed_head: d4515067af8314cadf979da7b17921fbafc92d21
reviewed_spine_sha256: 29c1078802abaa66abb391d4257f3cd952d6905fc9bf11d1bcd85f9b773fb76a
reviewed_state: frozen working-tree closure candidate
review_date: 2026-07-16
reviewer: Professor Fiddlesticks
team: Team Argus
evidence_mode: accepted-research-complete-closure-reality-gate
scope: technology, Linux worker IPC, collection scheduling, diagnostics, and release recovery closure
finding_count: 3
blocking_findings: 1
high_findings: 2
---

<!-- markdownlint-disable MD013 MD025 -->

# Technology Remediation Closure Gate

## Verdict

**CHANGES REQUIRED.** The exact 1,588-line spine with SHA-256
`29c1078802abaa66abb391d4257f3cd952d6905fc9bf11d1bcd85f9b773fb76a`
retains every original technology-acceptance closure and the prior
release-recovery fixes. The latest edits also close the two previously reported
same-time dispatch and overlapping transport-reason choices at the arithmetic
level.

The new batch transition is not yet implementable as written, however. AD-10
requires every worker to be authenticated before any batch request, while
AD-25 has no pre-request acknowledgement or other observable authentication
transition. Its only authenticated response follows the request. The batch
admission model also assigns zero time to spawn/authentication even though that
time precedes `dispatch_epoch_boot_ns` and counts against the generation
cutoff. Finally, the new diagnostic schema leaves conditional byte fields and
their evidence cut non-total, so conforming coordinators can still persist
different candidate bytes and DiagnosticIds.

These are focused architecture-contract defects, not a request for new broad
technology research or a dependency change. The spine correctly remains
`status: draft`.

This review writes only this new report. It does not amend the spine, memlog,
canonical product or UX artifacts, product code, `tasks.md`, source acceptance
reports, or any existing review report.

## Review Basis

Citation keys:

- `SPINE` —
  `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md`
- `TECH-CURRENCY` — `reviews/review-technology-currency-2026-07-16.md`
- `TECH-ACCEPT` — `reviews/review-technology-acceptance-2026-07-16.md`
- `TECH-GATE` — `reviews/review-technology-remediation-gate-2026-07-16.md`
- `TECH-RERUN` — `reviews/review-technology-remediation-rerun-2026-07-16.md`
- `TECH-FINAL` — `reviews/review-technology-remediation-final-2026-07-16.md`

The current SPINE was read completely from line 1 through line 1,588. The
complete technology currency, original technology acceptance, remediation
gate, remediation rerun, and final technology reports were also reread. The
target hash was required before semantic review and checked again after it.

This is a fresh closure gate against the newly frozen candidate, not a new
dependency-currency survey. The same-day completed probes and official-source
conclusions in TECH-CURRENCY remain the accepted research basis. Repository
reality still has no product `Cargo.toml`, `Cargo.lock`, or final release
artifact, so this verdict judges whether the architecture assigns executable
proof; it does not claim implementation evidence exists.

The acceptance standard remains literal. A production coordinator and worker
built separately must agree on every observable transition, deadline, failure
report, diagnostic byte, and durable result without inventing a second IPC
message or an unstated timing budget. A fixture cannot repair a missing Rule.

## Original Technology-Acceptance Replay

| Prior claims | Closure result | Current binding evidence |
| --- | --- | --- |
| C01-C05, C20 — Rust edition, resolver, MSRV/stable lanes, target, bootstrap proof | **REMAINS CLOSED** | Rust 2024, resolver 3, MSRV 1.88, current-stable locked tests, `x86_64-unknown-linux-gnu`, committed lockfile, and bootstrap-before-Provider gates remain mandatory (`SPINE:457-467`). |
| C03, C07-C08, C10 — bundled SQLite graph | **REMAINS CLOSED** | The Stack retains exact `rusqlite = "=0.39.0"`, `libsqlite3-sys 0.37.0`, and bundled SQLite 3.51.3 targets; the SQLite adapter remains sole durable-state owner. |
| C06, C14 — glibc support choice and proof | **REMAINS CLOSED** | Release CI uses the exact final artifact, `readelf --version-info`, maximum `GLIBC_2.42`, and the same-artifact oldest-runtime smoke (`SPINE:457-466`). |
| C09 — TOML crate/spec separation | **REMAINS CLOSED** | The Stack retains `toml = "=1.1.3"` separately from TOML specification 1.1.0. |
| C11-C12 — ordered SQLite pragma verification | **REMAINS CLOSED** | Fresh and existing initialization sets WAL outside a transaction, requires returned and per-connection `wal`, reads FULL as numeric `2`, reads foreign keys as `1`, sets busy timeout, and only then permits `BEGIN IMMEDIATE` (`SPINE:653-665`). |
| C13 — one-binary release | **REMAINS CLOSED** | One versioned Rust binary, its SHA-256, locked release lanes, and release-asset smoke remain required (`SPINE:457-469`). |
| C15 — explicit systemd action limits | **REMAINS CLOSED** | ARCH-LIM-11 and ARCH-LIM-23 retain the explicit execution and total-decision bounds. |
| C16 — suspend-inclusive time | **REMAINS CLOSED** | Lease and cadence decisions still use Linux `CLOCK_BOOTTIME`; wall time remains provenance only. |
| C17-C19 — absolute consumers and timer success | **REMAINS CLOSED** | Every managed absolute `ExecStart`, expressly both named services, must target the canonical binary; loaded path, timer advancement, `Result=success`, and `ExecMainStatus=0` are read back, with whole-pair restoration on failure (`SPINE:470-482`). |

No original accepted technology choice moved into Deferred or became a
non-testable aspiration.

## Prior Remediation-Finding Replay

| Prior finding | Result on this hash | Assessment |
| --- | --- | --- |
| TRR-B01 — transport failure has no AD-5 terminal report | **CLOSED** | Every named setup, request, transport, parse, identity, typed-error, exit, and signal path produces one existing AD-5 report and outcome (`SPINE:1271-1318`). |
| TRR-B02 — resumed FD4 validates a dead original owner | **CLOSED** | Exclusive-lock publication makes one ReleaseRecoveryAttemptV1 active; FD4 binds peer, request, result, manifest revision, and capability to that attempt, including PID reuse and second-crash behavior (`SPINE:982-1034`, `SPINE:1064-1067`, `SPINE:1101-1117`). |
| TRR-H01 — process barrier absent from LPT admission | **CLOSED AT THE IDEALIZED EVENT MODEL** | Runtime and configuration now share one batch event transition. Independent event simulation reproduces the documented default 35 seconds and the 60-plus-seven-1-second result of 61 seconds (`SPINE:321-361`, `SPINE:843-850`). CLOSURE-B01 and CLOSURE-H01 below concern realizability and unmodeled startup, not the ideal arithmetic. |
| FINAL-M01 — overlapping transport reasons have no precedence | **CLOSED** | Deadline wins, then one explicit first-match order, with bare exit normalization and parent cleanup as secondary evidence (`SPINE:1282-1295`). |
| FINAL-M02 / FINAL-H01 — same-time slots may dispatch sequentially or as a batch | **CLOSED** | The Rule collects all slots free at the epoch, assigns one frozen LPT batch, and dispatches in worker-ID order only after batch setup (`SPINE:326-341`). |
| FINAL-B01 — synthesized diagnostic identity and bytes are not canonical | **PARTIAL** | Producer, scope, code, subject, schema token, key order, source encounter, and duplicate occurrence are fixed (`SPINE:1297-1313`). CLOSURE-H02 records the remaining conditional-value gap. |

## Blocking Finding

### CLOSURE-B01 — Pre-dispatch worker authentication has no protocol witness

AD-10 requires the coordinator to spawn, establish a process group, and
authenticate **every** one-shot worker in a batch before dispatching any batch
request. It then freezes roots only after all authentications and decides
whether the process gate closes from whether the process member authenticated
(`SPINE:326-349`).

AD-25 defines no transition by which the parent can observe that state. The
child locally validates FD3, `SO_PEERCRED`, and executable identity, then the
wire protocol contains exactly one parent request followed by one child result
and EOF. The result's capability echo is the first positive child response, but
it necessarily occurs after dispatch (`SPINE:1248-1263`, `SPINE:1320-1418`). A
child that has not yet run and a child that has successfully authenticated and
is waiting for the request are indistinguishable to the coordinator. An exit 77
proves failure, but absence of exit is not proof of completed authentication.

Linux does not make `SO_PEERCRED` a parent-side ready acknowledgement. Linux
[`unix(7)`](https://man7.org/linux/man-pages/man7/unix.7.html) specifies that
the returned credentials are those in effect when `socketpair(2)` was called.
Because the pair must exist before the endpoint can be inherited as FD3, a
local fork probe on this review Host produced:

```text
parent_view parent=1783400 child=1783404 peer_pid=1783400
child_view parent=1783400 self=1783404 peer_pid=1783400
```

That behavior correctly lets the child authenticate its parent. It does not
let the parent prove the child has executed the check. Parent-side `/proc`
inspection can prove PID, birth, executable, and process-group setup, but the
current Rule neither names that as the meaning of "authenticated" nor makes it
equivalent to the child-side FD3 check.

Two implementations must therefore diverge: add an unstated ready frame or
signal, optimistically treat a live spawned PID as authenticated, or block
without a positive completion event. The first changes the exact wire
protocol; the second violates AD-10's sequencing; the third has no terminal
bound. Root freeze, process-gate closure, dispatch epoch, and failed-member
reports all depend on that choice.

**Required closure:** either version FD3 with a bounded, authenticated
`WorkerReadyV1` response before the request, or replace the pre-dispatch claim
with a total parent-verifiable spawned-root state and move child authentication
to request handling. In either design, name the exact success/failure event,
timeout, report mapping, and process-root eligibility, then test a silent child,
exit 77 before readiness, readiness replay, and a batch with one failed member.

## High Findings

### CLOSURE-H01 — Spawn/authentication time is absent from the admitted makespan

AD-10 captures `dispatch_epoch_boot_ns` only after every batch member has been
spawned and authenticated. Scope deadlines start at that epoch. The same Rule
says the generation cutoff includes queue and worker-spawn-barrier time, while
configuration simulates only each scope's configured deadline and the process
barrier (`SPINE:326-361`). No startup/authentication deadline or worst-case
duration exists in AD-20.

The contracts cannot all hold at zero margin. For a configuration whose
idealized makespan exactly equals its generation cutoff, any positive batch
startup duration moves `dispatch_epoch_boot_ns` later while the generation
cutoff continues to age. A full scope budget then ends after the admitted
generation cutoff, and the atomic registry produces `timed-out` at equality
(`SPINE:351-361`, `SPINE:376-378`). The new statement that the admission worst
case assumes every member authenticates and consumes its full budget is
therefore false for that valid configuration. A slow or silent pre-request
child is worse: the model has no startup terminal event at all.

The configured scheduler margin cannot serve as an unstated hard startup
budget. Zero is valid, and even a positive margin is not assigned per batch or
connected to an authentication cutoff. The deterministic 35- and 61-second
event traces are correct only under a zero-cost spawn/auth assumption.

**Required closure:** introduce a bounded batch-start/authentication budget and
include it in the exact runtime/configuration event simulation for every batch,
or capture the dispatch epoch before startup and explicitly make startup part
of each scope budget. Tie silent and failed startup to an absolute monotonic
deadline, AD-25 report construction, gate reopening, and generation cutoff.
Add zero-margin and multi-batch nonzero-startup fixtures in addition to the
existing idealized 35/61 cases.

### CLOSURE-H02 — Diagnostic conditional bytes and evidence cut are not total

The new `WorkerTransportFailureV1` first-match primary reason is total. The
candidate identity is mostly byte-complete. Its parameter values are not yet a
total function of transport evidence, however (`SPINE:1282-1313`).

- `measured_bytes` and `allowed_bytes` are only said to be present "when
  measured." The Rule does not require their presence when a measurement
  exists, define whether a partial frame uses declared length or received byte
  count, or say whether zero-length, early-EOF, trailing-data, and ordinary
  schema failures retain the known frame length and cap.
- `exit_code` and `signal` retain wait evidence "observed under AD-10," but no
  immutable evidence cut says whether the coordinator canonicalizes the report
  before cleanup/reap or waits for that status. A parser failure followed by
  parent cleanup can therefore encode absent or the later wait status without
  changing the primary reason.
- `termination_origin=worker` is not defined as causal sender versus simply
  "not parent cleanup." Linux child wait status exposes the terminating signal,
  not a general sender identity; [`wait(2)`](https://man7.org/linux/man-pages/man2/waitpid.2.html)
  cannot by itself prove the stronger causal meaning.

Those fields participate in canonical DiagnosticParameterV1 bytes, candidate
sorting, and final DiagnosticId. The difference is therefore durable, not
cosmetic. The existing exact-boundary and combined fixtures can choose one
answer, but the production Rule does not require the same answer.

**Required closure:** define one per-primary-reason parameter matrix with exact
presence and value for all seven keys. Define `measured_bytes` as declared or
received length per framing state, bind `allowed_bytes` to the exact applicable
cap, define `termination_origin` semantically, and freeze a monotonic
failure-evidence cut before candidate canonicalization. Later reap evidence
must either be a separately typed retained diagnostic or be excluded from the
immutable transport candidate by Rule.

## Retained Technology and Release Gate

| Required seam | Result | Binding evidence |
| --- | --- | --- |
| Atomic CollectionPlan admission | **PASS** | One `BEGIN IMMEDIATE` operation freezes paired boot/wall time, repository revision, Promise/policy/scope/baseline/operation/history/current cuts, pins, canonical plan bytes, fingerprint, and latest-requested generation (`SPINE:862-927`). |
| Canonical policy and Scope bytes | **PASS** | CanonicalJsonV1, complete PolicySnapshotV1, CollectionPlanV1, ScopeIdV1, and ScopeManifestV1 fix order, types, path normalization, display, equality, and fingerprints (`SPINE:1156-1241`). |
| Process ownership and suppression | **PASS APART FROM BATCH READINESS** | Exact PID/birth roots, frozen process groups, Provider descendants, escaped-group emission, winner order, conflicts, and retained suppression diagnostics remain fixed (`SPINE:553-599`). |
| Crash-persistent release admission | **PASS** | Every ordinary stateful entry retains shared admission and refuses before SQLite unless ready; only release owns exclusive recovery (`SPINE:966-980`). |
| Recovery owner and FD4 | **PASS** | Atomic active-attempt publication, PID-reuse treatment, second-crash continuation, peer identity, one-use capability, and manifest-attempt binding remain explicit (`SPINE:982-1034`). |
| UpgradeTransaction journal | **PASS** | Checksummed no-follow replacement uses file fsync, atomic rename, directory fsync, pending-before-effect, complete-after-readback, and may-have-executed recovery (`SPINE:1036-1071`). |
| Managed consumers and whole-pair rollback | **PASS** | Both named services, loaded `ExecStart`, paired timer success, binary/state/unit/timer/daemon restoration, and readback remain mandatory (`SPINE:470-482`, `SPINE:1073-1083`). |
| KnownGood and explicit rollback | **PASS** | `commit-decided` is irreversible; KnownGood publication/readback precedes ready; exactly one record remains; rollback is a new transaction (`SPINE:1085-1117`). |
| Release events and crash results | **PASS** | Active attempt identity, complete internal-to-public mapping, projection states, durable emission boundaries, and four exhaustive machine results remain fixed (`SPINE:1119-1154`). |

## Mechanical and Reality Validation Record

| Validation | Command or method | Result |
| --- | --- | --- |
| Frozen target identity | `git rev-parse HEAD`; `sha256sum <SPINE>` before and after semantic review | **PASS** — head `d4515067af8314cadf979da7b17921fbafc92d21`; exact required SHA-256 retained. |
| Complete reads | Line-bounded reads through EOF for the 1,588-line SPINE and all five technology history reports | **PASS** — every original claim and later finding was reconstructed against current Rules. |
| Architecture linter | `uv run .agents/skills/bmad-architecture/scripts/lint_spine.py --workspace _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14` | **PASS** — `ok: true`; zero findings. |
| AD integrity | Ordered heading extraction | **PASS** — AD-1 through AD-25 exactly once; original AD-1 through AD-24 remain unrenumbered. |
| ARCH-LIM integrity | Ordered table-definition extraction | **PASS** — ARCH-LIM-1 through ARCH-LIM-23 exactly once. |
| Ideal event simulation | Independent batch/barrier trace for defaults and process-60 plus seven-1 | **PASS** — default makespan 35 seconds; pathological makespan 61 seconds. |
| Linux FD3 credential probe | Local `socketpair` plus `fork` and `getsockopt(SO_PEERCRED)` from both endpoints | **FAIL FOR PARENT READY PROOF** — both endpoints reported the socketpair creator PID; child-to-parent authentication works, parent-observed child readiness does not exist. |
| Required-term inspection | Exact `rg -n` sweep for dispatch epoch, transport reason/diagnostic, SQLite, ABI, named services, recovery attempts, journal, KnownGood, and events | **PASS FOR PRESENCE** — semantic defects are recorded above rather than hidden by token presence. |
| Product bootstrap reality | Repository `Cargo.toml` and `Cargo.lock` presence check | **PASS AS PLANNING STATE** — absent; implementation proof remains assigned to bootstrap. |
| Technology/reality closure | Batch authentication, timing, IPC, diagnostic, crash, SQLite, ABI, timer, and rollback interleavings | **FAIL** — CLOSURE-B01, CLOSURE-H01, and CLOSURE-H02. |

The deterministic linter proves the spine's mechanical structure. It cannot
prove that an IPC transition is observable or that a timing model includes all
of its own pre-dispatch work.

## Final Gate Status

**BLOCKED. Verdict: CHANGES REQUIRED.** Every original technology-acceptance
finding and the prior FD4/release findings remain closed. The idealized batch
arithmetic and transport primary-reason order now converge. Approval still
requires an observable, bounded pre-request worker state; admission accounting
for batch startup/authentication; and a total per-reason diagnostic parameter
matrix with one frozen evidence cut.
