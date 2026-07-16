---
title: "Technology Remediation Unanimous Closure Gate - srvls Architecture"
document_type: architecture_review
review_dimension: technology_remediation_unanimous_closure
status: final
verdict: "APPROVED"
blocking: false
reviewed_head: d4515067af8314cadf979da7b17921fbafc92d21
reviewed_spine_sha256: 754b956cc4fa345017415257ce2f3e295ad421d6ea6e9ff7d2b0d8555b42aee1
reviewed_state: frozen working-tree unanimous-closure candidate
review_date: 2026-07-16
reviewer: Professor Fiddlesticks
team: Team Argus
evidence_mode: complete-technology-linux-reality-unanimous-closure-gate
scope: technology, Linux spawn ownership, worker IPC, scheduling, diagnostics, SQLite, ABI, timers, and release recovery
finding_count: 0
blocking_findings: 0
high_findings: 0
---

<!-- markdownlint-disable MD013 MD025 -->

# Technology Remediation Unanimous Closure Gate

## Verdict

**APPROVED.** The exact 1,758-line architecture spine with SHA-256
`754b956cc4fa345017415257ce2f3e295ad421d6ea6e9ff7d2b0d8555b42aee1`
closes `REALITY-B01` without reopening any original technology-acceptance,
remediation, transport, scheduling, diagnostic, storage, release, ABI, or
managed-consumer finding. This final technology/Linux reality gate found zero
blocking, high, medium, or low defects.

The new `OwnedSpawnV1 -> SpawnedWorkerRootV1 | UnrootableSpawnV1` state
machine is constructible on Linux and fail-closed. A child PID is owned before
identity or group setup can fail. A complete root alone can suppress Host
truth. An unrootable child is either proved absent before any process Request
or causes that process scope to terminalize without Host-read. The barrier is
coordinator-wide across supersession, while later cleanup or reap evidence
cannot rewrite immutable collection truth.

The spine correctly remains `status: draft`. This approval clears the
technology/Linux reality gate; it does not finalize the architecture or claim
that product implementation artifacts already exist.

This review adds only this report. It does not amend the spine, `tasks.md`,
product source, canonical product or UX artifacts, or any existing report.

## Review Basis and Frozen Identity

Citation keys:

- `SPINE` -
  `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md`
- `TECH-CURRENCY` - `reviews/review-technology-currency-2026-07-16.md`
- `TECH-ACCEPT` - `reviews/review-technology-acceptance-2026-07-16.md`
- `TECH-GATE` - `reviews/review-technology-remediation-gate-2026-07-16.md`
- `TECH-RERUN` - `reviews/review-technology-remediation-rerun-2026-07-16.md`
- `TECH-FINAL` - `reviews/review-technology-remediation-final-2026-07-16.md`
- `TECH-CLOSURE` - `reviews/review-technology-remediation-closure-2026-07-16.md`
- `TECH-REALITY` - `reviews/review-technology-remediation-reality-closure-2026-07-16.md`
- `TWO-UNIT-REALITY` - `reviews/review-two-unit-remediation-reality-closure-2026-07-16.md`
- `RUBRIC-REALITY` - `reviews/review-rubric-remediation-reality-closure-2026-07-16.md`

The current SPINE was read completely from line 1 through line 1,758. The
complete technology finding history and the two independent `REALITY-B01`
reports were replayed against the current Rule text. The required spine hash
matched before semantic review and after report creation. The reviewed Git
head was `d4515067af8314cadf979da7b17921fbafc92d21`.

TECH-CURRENCY remains the same-day dependency and platform research basis.
This pass independently rechecked the Linux process, process-group, wait,
`/proc`, and Unix-socket assumptions. Repository reality still has no product
`Cargo.toml`, `Cargo.lock`, or final release artifact, so approval means the
architecture assigns complete executable proof; it is not implementation
acceptance.

The literal BMAD reviewer test was applied: independently written scheduler,
worker, process collector, reducer, storage adapter, and release coordinator
must choose the same transition, deadline, failure report, canonical bytes,
and public result. Named fixtures support the production Rule but do not repair
an unstated branch.

## REALITY-B01 Closure

**CLOSED.** The current Rule selects the required second remediation strategy:
an after-PID failure that cannot become a complete self root must be proved
absent before process Host-read, otherwise the process scope terminalizes.

### Total Spawn-Ownership State Machine

| Linux-observable transition | Required architecture state | Safe consequence |
| --- | --- | --- |
| Spawn returns no child PID | No owned or self-root record | Existing `worker-spawn`/no-child mapping; no cleanup target is invented. |
| Spawn returns a child PID | `OwnedSpawnV1(request_id, pid, unreaped_owned_child_handle)` before any subsequent setup read | The parent has one exact wait/cleanup identity before birth, executable, or group setup can fail (`SPINE:597-607`). |
| Birth, executable, and dedicated group all succeed | Refine to complete `SpawnedWorkerRootV1` | The exact PID/birth/executable/PGID root may enter SelfProcessSetV1 and remains until the group is proved empty. |
| Group setup is `not-attempted` or `failed` after PID return | Refine to `UnrootableSpawnV1`; target only the exact unreaped child PID | The inherited coordinator group is never signaled or encoded as self (`SPINE:609-622`). |
| Group setup succeeds but birth or executable proof fails | Refine to `UnrootableSpawnV1` with `succeeded(pgid)` | Cleanup targets only the known dedicated group; admission additionally requires exact-child reap and zero `/proc` members with that PGID. |
| Unrootable absence proves strictly before both process cuts | Drop the barrier only after exact reap and, when applicable, group-empty proof | Complete roots freeze and the authenticated process Request may proceed. |
| Absence is pending at equality, after either cut, or in D-state | Keep operational reap evidence; synthesize the process `worker-timeout` unless an earlier process failure already owns its report | No process Request, no Host-read, no internal Observation, and the spawn gate reopens (`SPINE:623-634`, `SPINE:1378-1385`). |

`UnrootableSpawnV1` contains request ID, PID, the exact owned child handle,
tagged group-setup result, and WorkerReapEvidenceV1. It is coordinator-wide,
survives generation supersession, is never serialized as a partial root, and
never suppresses a Host process (`SPINE:609-627`). This is the missing state
from the prior counterexample.

Before any process-scope Request in the current or a later generation, the
coordinator closes the worker-spawn gate and resolves every current or
superseded unrootable record. The exact owned child must have exited and been
reaped. A successful group setup additionally requires zero current `/proc`
members with the exact PGID. Only then are complete roots frozen. The gate
remains closed through the half-open process Host-read cut, so no later worker
can appear outside the assignment (`SPINE:337-367`, `SPINE:629-640`).

This also covers an unrootable process worker itself. It cannot become Ready
because Hello requires the complete expected identity, so its own normal
`worker-spawn` report terminalizes it without Host-read. The unrootable record
persists for the next process scope. A Ready process sibling in the same or a
later generation blocks at the coordinator barrier until exact absence or its
own timeout.

### Linux Constructibility and Reuse Safety

Linux [`wait(2)`](https://man7.org/linux/man-pages/man2/waitpid.2.html) defines
an exited, unwaited child as a zombie and retains its PID and termination
status until the parent reaps it. That makes the spine's unreaped owned-child
handle a stable exact-child cleanup identity: while running or waitable, the
child PID cannot be recycled into another process. A compliant implementation
does not signal that numeric PID after its owned wait/reap transition.

Linux [`setpgid(2)`](https://man7.org/linux/man-pages/man2/getpgrp.2.html)
confirms both sides of the split. A child inherits the parent's process group;
successful `setpgid(child, child)` creates the dedicated group with PGID equal
to the child PID, while a parent attempt after child `execve` can fail with
`EACCES`. The `failed` branch therefore must not signal the inherited group,
and the current Rule expressly targets the exact owned child instead.
[`kill(2)`](https://man7.org/linux/man-pages/man2/kill.2.html) distinguishes a
positive exact PID from a negative process-group target, matching the two
tagged cleanup branches.

For `succeeded(pgid)`, the exact unreaped child anchors the group identity
through termination. Cleanup targets that known group, then the owned child is
reaped and `/proc` is checked for zero exact-PGID members. If the numeric PGID
is reused after reap but before the scan, the nonzero proof fails closed and
the process scope performs no Host-read. If reuse occurs after a successful
zero-member cut, the later group is unrelated and is correctly not in the
frozen self set. The fixture expressly forbids signaling or suppressing an
unrelated group (`SPINE:452-459`).

The no-group branch needs no descendant search because the exact current
worker may not fork, clone, or launch a Provider/helper before one accepted
Request (`SPINE:1320-1330`). Reaping that one owned child is therefore a total
absence proof. Once a complete group exists, Provider descendants remain in
that group after Request and use the established complete-root path.

Linux [`proc_pid_stat(5)`](https://man7.org/linux/man-pages/man5/proc_pid_stat.5.html)
exposes both process state and process-group identity and identifies `D` as
uninterruptible sleep. A D-state child may not become waitable within either
cut. The architecture does not promise an impossible reap bound: it emits the
existing process timeout without Host-read, reopens the gate, retains the
unrootable barrier across supersession, and retries absence proof before every
later process Request. Other provider collection remains bounded; the internal
child can never leak into direct-process truth.

A local Linux fork/exec probe exercised both cleanup branches:

```text
known-group {'owned_pid': 2226661, 'recorded_pgrp': 2226661, 'birth': 6780684, 'exe': (66306, 45092925), 'waited_pid': 2226661, 'group_members_after_reap': [], 'parent_alive': 2226659}
unrootable {'owned_pid': 2226662, 'group_setup': 'EACCES', 'inherited_pgrp': 2226659, 'coordinator_pgrp': 2226659, 'waited_pid': 2226662, 'parent_alive': 2226659}
```

The successful branch established, signaled, reaped, and proved an empty
dedicated group. The post-exec failure branch demonstrated the dangerous
inherited coordinator PGID; exact-PID cleanup reaped only the child and left
the coordinator alive. The architecture requires exactly that distinction.

### Barrier, Deadline, and D-State Interleavings

| Interleaving | Required result |
| --- | --- |
| Cleanup completes at boot time 4 with process deadline 10 | Freeze complete roots at 4; process Request and Host-read may begin with only the remaining budget. |
| Cleanup completes at exactly 10 | Equality is timeout; no Request or Host-read; gate reopens at 10. |
| Cleanup remains D-state/pending | Same timeout/no-read/reopen result; WorkerReapEvidenceV1 stays operational and immutable-report bytes do not change. |
| Generation 1 is superseded while cleanup is pending | UnrootableSpawnV1 remains in the coordinator barrier; Generation 2 cannot issue a process Request until absence proves against Generation 2's cuts. |
| Process worker already failed before barrier | Its existing AD-25 report remains sole; no second timeout is invented, no Host-read occurs, and the gate reopens. |
| Complete failed-worker root exists | The group stays in SelfProcessSetV1 until proven empty; no unrootable variant or partial identity is substituted. |

An independent virtual trace reproduced the decisive cuts:

```text
cleanup-before-cut {'failed_scope_cut': 0.2, 'process_request': 4.0, 'process_host_read': True, 'gate_reopen': 10.0, 'process_result': 'deadline-bounded'}
cleanup-at-cut {'failed_scope_cut': 0.2, 'process_request': None, 'process_host_read': False, 'gate_reopen': 10.0, 'process_result': 'worker-timeout'}
d-state-pending {'failed_scope_cut': 0.2, 'process_request': None, 'process_host_read': False, 'gate_reopen': 10.0, 'process_result': 'worker-timeout'}
```

The barrier consumes the process scope's existing absolute budget; it does not
create a new timing allowance. All setup and cleanup time remains inside the
pre-spawn scope deadline and the absolute generation cutoff. A process timeout
reopens spawn at the same event boundary the configuration model already uses
for a full-budget process lane, so the 35-second default, 61-second pathological
case, and mandatory one-nanosecond half-open headroom remain valid
(`SPINE:369-386`, `SPINE:873-923`).

AD-11 now owns the exact cross-unit fixture: an after-PID group/identity setup
failure with pending cleanup and a Ready process sibling in the same and a
later generation. It requires no process Request before absence, timeout when
either cut is missed, no leaked Observation, no unrelated-group signal or
suppression, and no later reap rewrite (`SPINE:452-472`).

## Linux Hello/Ready Reality Recheck

**PASS.** The four-frame FD3 protocol remains parent Hello, child Ready, parent
Request, child Result, then EOF. The parent enables `SO_PASSCRED` before spawn;
the child authenticates the creator parent through `SO_PEERCRED`; and the first
Ready byte received with `recvmsg` carries one matching `SCM_CREDENTIALS`
record plus echoed PID/birth/executable/PGID identity (`SPINE:1314-1376`).

Linux [`unix(7)`](https://man7.org/linux/man-pages/man7/unix.7.html) confirms
that `SCM_CREDENTIALS` represents the sender, is kernel checked, requires
receiver `SO_PASSCRED`, and needs at least one real byte on a Unix stream. A
fresh local probe returned:

```text
{'first_byte': b'R', 'credentials': [(2229401, 1000, 1000)], 'rest': b'EADY', 'creator': 2229399, 'spawned_child': 2229401, 'parent_so_peercred': (2229399, 1000, 1000), 'waited': 2229401, 'child_exit': 0, 'ctrunc': False}
```

The credential PID matched the spawned child; `SO_PEERCRED` correctly remained
the socketpair creator parent. Missing credentials, wrong identity or fields,
replay, exit 77, silence, and pre/post-Ready I/O retain their exact mappings.

## Original and Remediation Finding Replay

| Finding family | Result on this hash | Current binding evidence |
| --- | --- | --- |
| C01-C05 and C20 - edition, resolver, MSRV/stable lanes, target, bootstrap | **REMAINS CLOSED** | Rust 2024, resolver 3, MSRV 1.88, reviewed current-stable, locked all-target CI, `x86_64-unknown-linux-gnu`, one binary, and bootstrap-before-Provider proof remain mandatory (`SPINE:491-523`, `SPINE:1602-1624`). |
| C03, C07-C10 - bundled SQLite graph and TOML syntax | **REMAINS CLOSED** | Exact `rusqlite = "=0.39.0"`, libsqlite3-sys 0.37.0, bundled SQLite 3.51.3, `toml = "=1.1.3"`, and TOML specification 1.1.0 remain distinct lock targets (`SPINE:1602-1624`). |
| C06 and C14 - glibc support choice and proof | **REMAINS CLOSED** | CI runs `readelf --version-info` on the exact final artifact, fails above `GLIBC_2.42`, then smokes that artifact in the oldest supported glibc 2.42 runtime (`SPINE:496-505`). |
| C11-C12 - SQLite ordering and readbacks | **REMAINS CLOSED** | Fresh and existing databases set WAL outside a transaction, require returned and per-connection `wal`, read FULL as `2`, read foreign keys as `1`, set busy timeout, then permit transactions (`SPINE:714-740`). |
| C13 and C17-C19 - one binary, absolute consumers, and timers | **REMAINS CLOSED** | Every managed absolute `ExecStart`, expressly both named services, is rewritten and read back; timer advancement, `Result=success`, `ExecMainStatus=0`, and whole-pair rollback remain mandatory (`SPINE:506-521`). |
| C15-C16 - explicit bounds and suspend-inclusive time | **REMAINS CLOSED** | ARCH-LIM-11/23 remain exact and same-boot duration decisions use `CLOCK_BOOTTIME`; wall time is provenance. |
| TRR-B01 - transport failure lacked one AD-5 report | **REMAINS CLOSED** | Every setup, authentication, transport, parse, mismatch, typed error, exit, signal, and timeout path creates one existing six-outcome CollectorReport (`SPINE:1387-1481`). |
| TRR-B02 - resumed FD4 authenticated a dead owner | **REMAINS CLOSED** | One active ReleaseRecoveryAttemptV1 is published/read back under exclusive admission; PID reuse, second recovery crash, fresh capability, and FD4 attempt binding remain total (`SPINE:1052-1104`). |
| TRR-H01, FINAL-H01, FINAL-M02 - process barrier and same-time batch ambiguity | **REMAINS CLOSED** | One ordered dispatch-epoch transition owns batch selection, readiness, root freeze, process gate, slot release, and queue resumption (`SPINE:321-399`). |
| FINAL-M01 - overlapping transport reasons | **REMAINS CLOSED** | Deadline-first first-match primary selection, frame-before-wait, and direct-exit normalization remain total (`SPINE:1398-1425`). |
| FINAL-B01 - diagnostic identity and bytes | **REMAINS CLOSED** | Post-evidence candidates, canonical per-scope merge, exact seven-field matrix, and later-reap exclusion yield one DiagnosticId (`SPINE:536-582`, `SPINE:1427-1476`). |
| CLOSURE-B01 - no pre-Request authentication witness | **REMAINS CLOSED** | Hello/Ready and credentials provide a positive bounded witness before any Request. |
| CLOSURE-H01 - setup absent from timing model | **REMAINS CLOSED** | Dispatch epoch is sampled before spawn; setup, Ready, Request, work, Result, cleanup decision, and the new absence barrier consume existing absolute cuts. |
| CLOSURE-H02 - diagnostic parameters/evidence cut non-total | **REMAINS CLOSED** | Zero-byte EOF joins wait status, partial EOF fails immediately, all seven values are fixed, and WorkerReapEvidence cannot mutate the candidate. |
| REALITY-B01 - live post-spawn failure absent from self truth | **CLOSED** | OwnedSpawnV1 captures exact ownership before setup; complete roots alone suppress; UnrootableSpawnV1 blocks process Host-read until exact absence or timeout (`SPINE:597-640`, `SPINE:1378-1385`). |

## Retained Storage, Release, and Contract Gate

| Required seam | Result | Binding evidence |
| --- | --- | --- |
| Atomic CollectionPlanV1 admission | **PASS** | One repository operation performs paired boot/UTC sampling, absolute generation cut, current revision, Promise/policy/scope, accepted baseline, nonterminal operation, resource history, prior-current, plan insert, pins, and latest request under one `BEGIN IMMEDIATE` or commits none (`SPINE:924-997`). |
| Canonical policy, plan, Scope, and diagnostics | **PASS** | CanonicalJsonV1, complete PolicySnapshotV1, ordered CollectionPlanV1, tagged ScopeIdV1, post-evidence candidates, and atomic reference rewrite remain byte-total (`SPINE:524-582`, `SPINE:1226-1312`). |
| Deterministic ownership and suppression | **PASS** | Complete roots, exact PID/birth/group membership, Provider hints, winner order, conflicts, rejected hints, and retained ProcessSuppressionV1 evidence remain deterministic; unrootable children never become weak self evidence (`SPINE:597-670`). |
| Crash-persistent ReleaseAdmissionV1 | **PASS** | Every stateful entry holds shared admission and fails before SQLite unless ready with no nonterminal transaction; release alone owns exclusive recovery (`SPINE:1036-1050`). |
| Checksummed UpgradeTransaction ordering | **PASS** | Same-directory no-follow O_EXCL write, file fsync, atomic rename, directory fsync, checksum readback, pending-before effect, and complete-after effect readback cover every forward and rollback effect (`SPINE:1106-1154`). |
| KnownGood and explicit rollback | **PASS** | Commit decision is irreversible; publication/readback retains exactly one KnownGoodReleaseV1; post-decision recovery finishes forward; rollback is a new full transaction (`SPINE:1156-1187`). |
| Public release phases and crash results | **PASS** | Every durable step maps to one public phase and UX label; attempt identity, event states, resumed recovery, and the four final machine results remain exhaustive (`SPINE:1189-1224`). |
| ABI and managed timers | **PASS** | Exact-artifact GLIBC gate, oldest-runtime smoke, both named services, loaded ExecStart readback, paired timer-triggered success, and whole-pair restore remain literal (`SPINE:491-521`, `SPINE:1143-1154`). |
| UJ-5 and named fixtures | **PASS** | UJ-5 retains exact duplicate evidence and timestamped resource history; property, concurrency, crash, IPC, timer, PID-reuse, second-crash, and rollback families remain assigned (`SPINE:420-489`, `SPINE:1707-1736`). |

No accepted contract moved into Structural Seed or Deferred. The seed remains
implementation-owned structure, and Deferred retains only explicitly
out-of-scope future choices (`SPINE:1626-1694`, `SPINE:1738-1758`).

## Validation Record

| Validation | Command or method | Result |
| --- | --- | --- |
| Frozen target identity | `git rev-parse HEAD`; `sha256sum <SPINE>` before and after review | **PASS** - head `d4515067af8314cadf979da7b17921fbafc92d21`; required SHA-256 unchanged. |
| Complete semantic read | Line-bounded reads through EOF for the 1,758-line current SPINE plus all original/remediation finding registers | **PASS** - every finding family replayed. |
| Linux owned-spawn reality | Official wait, setpgid, kill, and proc semantics plus local known-group and post-exec-EACCES cleanup probes | **PASS** - exact owned-child and known-group branches are constructible and do not target the coordinator group. |
| Linux ancillary reality | Official `unix(7)` plus a fresh AF_UNIX SOCK_STREAM/fork/sendmsg/recvmsg probe | **PASS** - first Ready byte carried one child credential record without truncation; child authenticated creator parent. |
| Barrier and timing traces | Cleanup-before-cut, equality, D-state, supersession, default, pathological, zero-margin, and nonzero-startup event replay | **PASS** - process Host-read occurs only after exact absence; all other paths remain inside existing absolute cuts. |
| Diagnostic matrix walk | Every primary/cut row, all seven values, zero-byte EOF, partial EOF, cleanup, and later-reap mutation | **PASS** - one immutable report and DiagnosticId per path. |
| Architecture linter | `uv run .agents/skills/bmad-architecture/scripts/lint_spine.py --workspace _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14` | **PASS** - `ok: true`; zero findings. |
| AD integrity | Ordered exact heading extraction | **PASS** - AD-1 through AD-25 occur exactly once; AD-1 through AD-24 remain unrenumbered. |
| ARCH-LIM integrity | Ordered exact table-definition extraction | **PASS** - ARCH-LIM-1 through ARCH-LIM-23 occur exactly once. |
| Required-term inspection | Exact term sweep over ownership, setup state, group proof, supersession, no-fork, process timeout, credentials, budgets, diagnostics, SQLite, ABI, services, admission, journal, KnownGood, rollback, and release events | **PASS** - every required term lands in an enforceable Rule and was inspected in context. |
| Markdown lint | `markdownlint-cli2 --config _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/.markdownlint-cli2.jsonc <this-report>` | **PASS** - one file; zero errors. |
| Whitespace/error check | `git diff --check`; untracked-report no-index check | **PASS** - no whitespace errors. |
| Changed-file scope | `git status --short`; target-path comparison | **PASS** - this reviewer added only this unanimous-closure report; shared remediation artifacts were already present. |

## Final Gate Status

**APPROVED. Blocking status: CLEAR for technology and Linux reality.**
`REALITY-B01` and every prior finding are closed with zero findings on the exact
required spine hash. Any later semantic change to AD-5, AD-10 through AD-13,
AD-16, AD-20 through AD-25, the Stack, or Deferred requires a new
technology/Linux reality gate.
