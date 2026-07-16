---
title: "Technology Remediation Reality Closure Gate - srvls Architecture"
document_type: architecture_review
review_dimension: technology_remediation_reality_closure
status: final
verdict: "APPROVED"
blocking: false
reviewed_head: d4515067af8314cadf979da7b17921fbafc92d21
reviewed_spine_sha256: 03b539cc80e98b7dac436360b324cb6e6f925a95e775571343b84b9cf2756a55
reviewed_state: frozen working-tree reality-closure candidate
review_date: 2026-07-16
reviewer: Professor Fiddlesticks
team: Team Argus
evidence_mode: accepted-research-complete-linux-reality-closure-gate
scope: technology, Linux worker authentication, collection timing, transport diagnostics, and retained release architecture
finding_count: 0
blocking_findings: 0
high_findings: 0
---

<!-- markdownlint-disable MD013 MD025 -->

# Technology Remediation Reality Closure Gate

## Verdict

**APPROVED.** The exact 1,710-line architecture spine with SHA-256
`03b539cc80e98b7dac436360b324cb6e6f925a95e775571343b84b9cf2756a55`
closes `CLOSURE-B01`, `CLOSURE-H01`, and `CLOSURE-H02` without reopening any
original technology-acceptance or prior remediation finding. The gate found
zero blocking, high, medium, or low technology/reality defects.

The worker handshake is now positively observable on Linux before request
dispatch; worker setup consumes the same pre-spawn absolute scope and
generation budgets modeled by configuration; and every transport failure maps
to one byte-complete diagnostic at one immutable evidence cut. Later cleanup
and reap evidence cannot perturb the persisted report or DiagnosticId.

The spine correctly remains `status: draft`. This approval clears the
technology/reality closure gate; it does not finalize the architecture and
does not claim product implementation evidence exists.

This review adds only this report. It does not amend the spine, `tasks.md`,
product source, canonical product or UX artifacts, or any existing review.

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

The current SPINE was read completely from line 1 through line 1,710. All six
technology-history reports listed above were read completely and their
acceptance claims and findings were replayed against the current text. The
required spine hash matched before semantic review and after report creation;
the reviewed Git head was
`d4515067af8314cadf979da7b17921fbafc92d21`.

The same-day completed dependency and platform research in TECH-CURRENCY and
TECH-ACCEPT remains the accepted currency basis. This pass independently
retested the Linux-specific FD3 assumptions. Repository reality still has no
product `Cargo.toml`, `Cargo.lock`, or release artifact, so approval means the
architecture assigns complete executable proof. It does not substitute design
text for a future implementation gate.

The literal test was whether independently implemented coordinator, worker,
configuration validator, reducer, and repository adapters must select the same
transition, deadline, failure code, diagnostic bytes, and durable result. A
fixture was accepted only where the production Rule itself was total.

## Targeted Closure Replay

| Finding | Result | Binding closure |
| --- | --- | --- |
| `CLOSURE-B01` - pre-dispatch worker authentication lacked a protocol witness | **CLOSED** | AD-25 now defines Hello and authenticated Ready before Request, with kernel credentials plus parent-owned child identity proof; AD-10 waits for every member to become Ready or terminal before dispatch (`SPINE:316-365`, `SPINE:1277-1337`). |
| `CLOSURE-H01` - spawn/authentication time was absent from admitted makespan | **CLOSED** | The dispatch epoch is sampled before spawn; setup, authentication, transfer, work, and failure consume the same absolute scope budget; configuration simulates that same complete lane and requires at least 1 ns headroom (`SPINE:321-377`, `SPINE:847-881`). |
| `CLOSURE-H02` - conditional diagnostic bytes and evidence cut were non-total | **CLOSED** | AD-25 fixes the first decisive evidence cut, wait/EOF precedence, all seven parameter values for every cause, exact size rows, termination origin, and exclusion of later reap status (`SPINE:1339-1428`). |

## CLOSURE-B01 - Linux-Observable Ready Authentication

**CLOSED.** The production Rule now exposes a positive, bounded transition
before Host work or request dispatch.

The parent creates one `AF_UNIX SOCK_STREAM` socketpair, enables `SO_PASSCRED`
on its receiving endpoint before spawn, allocates the request identity and
one-time capability, maps only the child endpoint to FD 3, and makes the child
the leader of a dedicated generation-owned process group. The child first
authenticates its parent with child-side `SO_PEERCRED`, exact `getppid()`, and
the `/proc/self/exe` versus `/proc/<parent>/exe` device/inode comparison. It
then marks FD 3 close-on-exec before Provider launch (`SPINE:1277-1291`).

The versioned wire sequence is exactly four length-prefixed CanonicalJsonV1
data frames and EOF:

1. parent `WorkerHelloV1`;
2. child `WorkerReadyV1`;
3. parent `WorkerRequestV1`;
4. child `WorkerResultV1`; then clean EOF.

Hello carries the request ID, capability, pre-spawn dispatch epoch, absolute
scope deadline, absolute generation cutoff, and the expected child PID,
boot-start ticks, executable device/inode, and process-group ID. Ready echoes
the identity fields and is sent with `sendmsg`. The first Ready byte must be
received with exactly one kernel-validated `SCM_CREDENTIALS` record matching
the spawned PID and expected UID/GID. Before accepting Ready, the parent also
matches the echo to its still-owned unreaped child, current `/proc/<pid>` birth
and executable identity, and dedicated process group (`SPINE:1293-1323`).

This split is sound on Linux. [`unix(7)`](https://man7.org/linux/man-pages/man7/unix.7.html)
defines `SO_PEERCRED` from socket creation time, so it authenticates the
creator parent to the inherited child endpoint. With `SO_PASSCRED` enabled,
`recvmsg` exposes sender credentials as `SCM_CREDENTIALS`; the credentials are
kernel checked, and stream ancillary data requires an accompanying data byte.
The Ready frame supplies that byte and the parent combines its kernel sender
PID with owned PID/birth/executable/process-group evidence. Parent and child
therefore prove the two different directions without treating the creator
credential as child readiness.

A local Linux stream-socket probe reproduced the required behavior:

```text
ready-first-byte b'R' [(2012029, 1000, 1000)]
ready-rest b'EADY' [(2012029, 1000, 1000)]
result b'RESULT' [(2012029, 1000, 1000)]
creator 2012027 child 2012029 SO_PEERCRED (2012027, 1000, 1000)
```

An owned-process probe also matched credential PID to current Linux identity:

```text
byte b'R' cred_pid 2049999 owned_pid 2049999 birth_ticks 6662227 exe_dev_ino 66306 45092925 pgrp 2049999 expected_pgrp 2049999 ctrunc False
```

Credentials may accompany later stream reads while `SO_PASSCRED` remains
enabled; that does not add a protocol data frame or weaken the specifically
required first-Ready-byte proof. The Rule authenticates Ready exactly once and
continues to validate the framed data sequence independently.

AD-10 makes this observable state operational: every member of one frozen LPT
batch becomes authenticated-ready or terminal before any member receives a
Request; failed spawned roots remain self-owned until their process groups are
proven empty; and only a still-live Ready process member can close the process
Host-read spawn gate (`SPINE:326-358`). A silent child, failed proof, exit 77,
malformed or replayed Ready, or setup failure is bounded by the earlier scope
or generation deadline and synthesizes one terminal report.

### Complete Handshake Failure Mapping

| Observable failure | Required primary result |
| --- | --- |
| Spawn fails before a child exists | `worker-spawn`; no process cleanup origin |
| Process-group or owned-identity setup fails after spawn | `worker-spawn`; parent cleanup |
| Parent cannot encode Hello or Request canonically | `request-encode` |
| Request canonical payload exceeds 32 MiB | `worker-request-too-large`; Request is not sent |
| Pre-Ready FD3 I/O, malformed/oversized/credential-less Ready, wrong kind or fields, replay, or peer proof failure | `fd-peer-auth` |
| Bare child exit 77 before Ready and without earlier cause | `fd-peer-auth` with direct worker exit evidence |
| Silence or any equality/late event | `worker-timeout` |
| Post-Ready FD3 I/O, zero/partial/trailing/repeated/wrong-direction/malformed frame | `frame-invalid` |
| Result declared above its effective cap | `worker-result-too-large`; payload is not allocated |
| Valid frame with schema, protocol version, worker identity, capability, or assignment defect | Exact named mismatch code |
| Trusted `protocol-error` or `worker-error` result | `worker-protocol-error` or `worker-internal-error` with exact stable subcode |
| Bare exit 0 or 64 without earlier cause | `frame-invalid` |
| Bare exit 70 without earlier cause | `worker-internal-error` |
| Other direct nonzero exit or signal | `worker-exit` or `worker-signal` |

The worker has no secondary discovery route: no ordinary clap routing,
configuration, XDG, SQLite, current-state, PATH, wall-clock, or scope
recomputation is allowed. It consumes only the authenticated request, absolute
monotonic cuts, Provider environment, and scoped Host reads
(`SPINE:1435-1524`).

## CLOSURE-H01 - One Pre-Spawn Absolute Timing Model

**CLOSED.** Runtime and configuration now model the same event sequence.

Before any batch spawn, the coordinator samples one
`dispatch_epoch_boot_ns`, allocates each member's request identity and
capability, and sets each absolute scope deadline to epoch plus that scope's
configured budget. Spawn, process-group setup, Hello/Ready authentication,
Request transfer, Provider work, Result transfer, and failure decision all
consume that same budget. Setup subtracts from Provider time and cannot extend
the completion cut (`SPINE:326-365`).

The generation cutoff is absolute from AD-21 admission and includes queue plus
the complete setup-and-work lane. Configuration replays the same batch
assignment, Ready/failure outcome, root freeze, process barrier, and completion
bound. Half-open admission requires the barrier-aware makespan plus
`max(scheduler_margin, 1 ns)`, so a configured zero margin is not equality
(`SPINE:367-377`, `SPINE:847-881`, `SPINE:893-902`).

Independent virtual-clock replay confirmed both required edge classes:

```text
default-nonzero-setup cutoff 40
 epoch 0 resolved 0.7 deadlines [30,20,15,15]
 epoch 15 resolved 16 deadlines [25,25]
 epoch 20 resolved 20.3 deadline 30
 epoch 25 resolved 25.8 deadline 35 gate (25.8,35)
 makespan 35 strictly_before_cutoff True

60-plus-seven-1-zero-margin cutoff 61.000000001
 epoch 0 resolved 1 deadlines [60,1,1,1] gate (1,60)
 epoch 60 resolved 60.9 deadlines [61,61,61,61]
 makespan 61 strictly_before_cutoff True
```

The first case proves nonzero setup remains inside each pre-spawn deadline.
The second proves a multi-batch process barrier and nonzero startup cannot
consume the mandatory one-nanosecond half-open headroom. AD-11 names both the
zero-margin lane and multi-batch nonzero spawn/Hello/Ready fixtures and
requires runtime/configuration trace equality (`SPINE:425-436`).

## CLOSURE-H02 - Byte-Complete Failure Evidence

**CLOSED.** Primary selection is deadline-first, first-match, and total. The
coordinator freezes `failure_evidence_cut_boot_ns` when the failure first
becomes decidable, before result admission closes and parent cleanup begins.
The expected frame is classified completely before wait status is consulted.
Zero-byte EOF is not itself a cause: the parent joins the owned child until the
earlier absolute deadline, then applies direct exit/signal or timeout. Partial
EOF is immediately `frame-invalid`. A valid report needs exact framing, clean
EOF, and exit 0 before both deadlines; a trusted protocol/worker-error result
selects its cause at EOF without waiting for later status
(`SPINE:1350-1377`).

`WorkerTransportDiagnosticV1` fixes producer, ScopeId, primary code,
parameter-schema token, byte-complete subject, source encounter, and duplicate
occurrence. Its parameter object always has exactly seven declared-order tagged
keys: request ID, worker subcode, exit code, signal, termination origin,
measured bytes, and allowed bytes. The exhaustive matrix fixes every active and
absent value for spawn, setup, encoding, both size cases, Ready/authentication,
every framing/mismatch/trusted-error case, direct exits/signals, and timeout
with or without a child (`SPINE:1379-1410`).

Only the Request-too-large and Result-too-large rows carry sizes, and they use
the exact payload length excluding the four-byte frame header. Known zero,
partial EOF, trailing data, Ready oversize, and ordinary schema defects keep
both size fields tagged absent. `termination_origin` means no process,
coordinator-required cleanup, or direct worker wait status; it never claims a
Linux signal sender. Exit and signal values appear only when direct wait status
selected the cause (`SPINE:1412-1420`).

Any cleanup or reap status observed after the cut is retained solely in
bounded `WorkerReapEvidenceV1`, including cleanup-invoked, pending/exit/signal,
observation boot time, and group-empty proof. It cannot rewrite the
CollectorReport, diagnostic candidate, DiagnosticId, Snapshot, or Brief
(`SPINE:1420-1428`). AD-11 requires a table-driven fixture for every primary
and causal variant, all seven parameter values, the evidence cut, canonical
candidate bytes, final ID, current-pointer result, Brief completeness, and
strict/non-strict behavior (`SPINE:443-458`).

## Original Acceptance and Prior-Finding Replay

| Prior gate | Result on this hash | Current binding evidence |
| --- | --- | --- |
| C01-C05 and C20 - Rust edition, resolver, lanes, target, bootstrap | **REMAINS CLOSED** | Rust 2024, resolver 3, MSRV 1.88, reviewed current-stable lane, locked CI, one `x86_64-unknown-linux-gnu` binary, and bootstrap-before-Provider proof remain mandatory (`SPINE:477-507`, `SPINE:1554-1576`). |
| C03, C07-C10 - bundled SQLite and TOML targets | **REMAINS CLOSED** | Exact `rusqlite = "=0.39.0"`, `libsqlite3-sys 0.37.0`, bundled SQLite 3.51.3, `toml = "=1.1.3"`, and TOML spec 1.1.0 remain distinct lock targets (`SPINE:1554-1576`). |
| C06 and C14 - glibc support and proof | **REMAINS CLOSED** | CI inspects the exact final artifact with `readelf --version-info`, fails above `GLIBC_2.42`, then smokes that same artifact on the oldest supported glibc 2.42 runtime (`SPINE:482-491`). |
| C11-C12 - ordered SQLite readbacks | **REMAINS CLOSED** | Fresh and existing databases set WAL outside a transaction and require returned `wal`; each connection reads WAL, sets and reads FULL as `2`, enables and reads foreign keys as `1`, then applies busy timeout before any transaction (`SPINE:677-703`). |
| C13 and C17-C19 - one binary and managed consumers | **REMAINS CLOSED** | Every managed absolute `ExecStart`, expressly both named services, receives loaded readback, timer-trigger advancement, successful service result, and whole-pair restoration on failure (`SPINE:492-507`). |
| C15-C16 - bounded actions and suspend-inclusive time | **REMAINS CLOSED** | ARCH-LIM-11/23 remain explicit and all same-boot duration decisions use `CLOCK_BOOTTIME`; UTC wall time is paired provenance. |
| TRR-B01 - transport failure lacked an AD-5 terminal report | **REMAINS CLOSED** | Every worker lifecycle failure synthesizes exactly one existing CollectorReport and never a seventh outcome or missing scope (`SPINE:1339-1433`). |
| TRR-B02 - resumed FD4 validation named a dead owner | **REMAINS CLOSED** | Exclusive publication creates one active ReleaseRecoveryAttemptV1, including PID-reuse and repeated-recovery-crash behavior, and FD4 binds to that attempt (`SPINE:1015-1067`). |
| TRR-H01, FINAL-H01, and FINAL-M02 - process barrier and same-time batch ambiguity | **REMAINS CLOSED** | One explicit dispatch-epoch algorithm governs batch assignment, root freeze, process gate, slot release, and queue resumption (`SPINE:321-390`). |
| FINAL-M01 - overlapping transport reasons lacked precedence | **REMAINS CLOSED** | Deadline-first and ordered primary selection plus direct-wait normalization remain total (`SPINE:1350-1377`). |
| FINAL-B01 - synthesized diagnostic identity was not canonical | **REMAINS CLOSED** | AD-13 candidate construction and post-evidence ordinal assignment plus AD-25's exact transport matrix fix one canonical result (`SPINE:522-568`, `SPINE:1379-1428`). |

## Retained Architecture Contracts

| Required seam | Result | Binding evidence |
| --- | --- | --- |
| Atomic CollectionPlanV1 admission | **PASS** | One repository `admit_collection` operation performs every cut under one `BEGIN IMMEDIATE`: gap-free generation, paired boot/UTC clock, absolute generation cut, current repository revision, Promise/policy/scope cuts, baseline projection, nonterminal operations, resource history, and prior-current pointer; partial visibility is impossible (`SPINE:887-960`). |
| Byte-complete canonical plan and identity | **PASS** | AD-24 fixes CanonicalJsonV1 scalar and union grammar, every PolicySnapshot field, ordered CollectionPlan fields, and tagged ScopeIdV1 provider grammar; no omission, `null`, untyped map, or alternate byte encoding remains (`SPINE:1198-1270`). |
| Constructible diagnostics after evidence | **PASS** | Candidates exist only after evidence, contain fixed tagged subject/parameters, sort by canonical bytes, and receive final per-scope ordinals after the evidence cut with atomic reference rewrite (`SPINE:516-568`). |
| Deterministic process ownership and suppression | **PASS** | Exact coordinator/worker PID, birth, executable, process-group roots, materialized group membership, Provider ownership hints, tie/conflict behavior, escaped-group emission, self suppression, and retained conflicts are fixed rather than inferred from ancestry alone (`SPINE:583-626`). |
| Crash-persistent stateful-entry gate | **PASS** | `ReleaseAdmissionV1` makes every stateful entry acquire and retain shared admission and fail before SQLite unless state is ready with no nonterminal transaction; only release recovery owns exclusive mutation (`SPINE:999-1013`). |
| Checksummed atomic upgrade journal | **PASS** | UpgradeTransaction effects use write-ahead pending, no-follow temporary write, file fsync, atomic replacement, directory fsync, readback, effect, effect readback, then write-after complete; every may-have-executed crash edge is recoverable (`SPINE:1069-1128`). |
| Exactly one KnownGood and explicit rollback | **PASS** | Successful validation stages the candidate, makes an irreversible commit decision, publishes and reads back exactly one KnownGoodReleaseV1, then returns ready; rollback is a new full UpgradeTransaction, never direct repointing (`SPINE:1119-1150`). |
| Durable phases and crash results | **PASS** | Every internal step maps to a public release phase and canonical UX label; event status and crash recovery projections are complete and retain the active recovery attempt (`SPINE:1152-1206`). |
| Named fixtures and traceability | **PASS** | AD-11 names property, concurrency, crash, IPC, timer, rollback, PID-reuse, second-crash, and exact-artifact fixtures; UJ-5 now lands on retained timestamped resource history and related trace rows remain bound (`SPINE:411-475`, `SPINE:1659-1688`). |

No accepted contract was weakened into Structural Seed or Deferred. The seed
remains structural only, and Deferred retains only explicitly out-of-scope
future choices (`SPINE:1578-1646`, `SPINE:1690-1710`).

## Validation Record

| Validation | Command or method | Result |
| --- | --- | --- |
| Frozen target identity | `git rev-parse HEAD`; `sha256sum <SPINE>` before and after review | **PASS** - head `d4515067af8314cadf979da7b17921fbafc92d21`; required SHA-256 unchanged. |
| Complete semantic reads | Line-bounded reads through EOF for the 1,710-line SPINE and complete technology history | **PASS** - every targeted and retained finding replayed. |
| Linux ancillary reality | Official `unix(7)` semantics plus local stream `SO_PEERCRED`, `SO_PASSCRED`, `recvmsg`, owned PID/birth/executable/process-group probes | **PASS** - parent and child authentication directions are constructible exactly as specified. |
| Timing reality | Independent nonzero-setup default and 60-plus-seven one-second multi-batch virtual-clock traces | **PASS** - scope completions stay inside pre-spawn cuts and the 1 ns half-open headroom is enforced. |
| Architecture linter | `uv run .agents/skills/bmad-architecture/scripts/lint_spine.py --workspace _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14` | **PASS** - `ok: true`; zero findings. |
| AD integrity | Ordered exact heading extraction | **PASS** - AD-1 through AD-25 occur exactly once; AD-1 through AD-24 remain unrenumbered. |
| ARCH-LIM integrity | Ordered exact table-definition extraction | **PASS** - ARCH-LIM-1 through ARCH-LIM-23 occur exactly once. |
| Required-term inspection | Exact `rg -n` sweep for dispatch epoch, Hello/Ready, credentials, owned identity, timing, failure cut, diagnostic matrix, EOF/wait precedence, reaping, SQLite, ABI, services, plan, release admission, journal, KnownGood, rollback, and release events | **PASS** - every required term lands in an enforceable Rule and was inspected in context. |
| Markdown lint | `markdownlint-cli2 --config _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/.markdownlint-cli2.jsonc <this-report>` | **PASS** - one file; zero errors. |
| Whitespace/error check | `git diff --check` | **PASS** - no output. |
| Changed-file scope | `git status --short`; target-path comparison | **PASS** - this reviewer added only this reality-closure report; shared remediation artifacts were already present. |

## Final Gate Status

**APPROVED. Blocking status: CLEAR for technology and Linux reality.**
`CLOSURE-B01`, `CLOSURE-H01`, and `CLOSURE-H02` are closed with zero findings
on the exact required spine hash. Any later semantic change to AD-5, AD-10,
AD-11, AD-13, AD-16, AD-20 through AD-25, the Stack, or Deferred requires a
new technology/reality gate.
