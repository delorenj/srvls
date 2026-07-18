---
title: "srvls Architecture Two-Unit Divergence Final Pass"
type: architecture-review
status: final
created: 2026-07-16
updated: 2026-07-16
reviewer: Sir Fix-a-Lot
review_mode: independent-two-unit-divergence-final-pass
reviewed_commit: 8fd5d312fabe544163d9b57b6b933e56b5133414
reviewed_spine_sha256: 174a3637d185c63fe8118a01827332e8f712525681f42602efaedff6de6a2cbb
reviewed_spine_line_count: 1777
reviewed_artifact: _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md
verdict: changes-required
blocking_status: blocked
finding_count: 1
blocking_findings: 1
high_findings: 0
moderate_findings: 0
low_findings: 0
---

<!-- markdownlint-disable MD013 MD025 -->

# Architecture Review: Two-Unit Divergence Final Pass

## Verdict

**CHANGES REQUIRED. Blocking status: BLOCKED. Finding count: 1.**

The requested default four-worker trace does satisfy the stated 35-second
makespan even when its 30-second member remains silent through its deadline.
Ready shorter members dispatch and release their slots independently, the
process scope is the final LPT member, and no queued successor is trapped behind
its gate.

The general runtime/configuration contract does not converge, however. The
event-driven runtime must start the next scope whenever one slot becomes free,
and a ready process scope then closes the spawn gate. The configuration rule
simultaneously asserts that making every lane consume its full deadline is the
dominating bound. A valid trace in which one 20-second member finishes one
nanosecond early dispatches the process scope alone, strands three queued scopes
behind the gate, and exceeds the full-deadline trace by almost nine seconds.
One validator therefore accepts a 35-second cutoff while the conforming runtime
produces three generation-cutoff timeouts.

That changes Collector outcomes, strict exit, Snapshot and Diagnostic truth,
Brief completeness, and baseline eligibility. PASS is prohibited because the
finding count is nonzero.

This reviewer added only this report. The spine, memory log, task ledger,
product and UX sources, product code, and every existing review report remain
untouched.

## Frozen Target and Complete Source Basis

| Property | Frozen value |
| --- | --- |
| Branch | `feature-sir-fix-a-lot-architecture-final-pass` |
| Commit | `8fd5d312fabe544163d9b57b6b933e56b5133414` |
| Spine | 1,777 lines; SHA-256 `174a3637d185c63fe8118a01827332e8f712525681f42602efaedff6de6a2cbb` |
| Architecture memory log | 143 lines, read through EOF |
| Final PRD | 823 lines; SHA-256 `576186a6068c4a7c7cc087b16530b76269e62ab898a7b2c61db65e389ccdb6d7` |
| PRD addendum | 63 lines; SHA-256 `1848ab1351fe8e26edf127da34b0cda4dd3f63d4a17af03f96619f5d8671ae9d` |
| UX DESIGN | 329 lines; SHA-256 `e68b22d5fd232f50e580a9fd87b182b6f30938a1c5c789aa0045ed85f531d84c` |
| UX EXPERIENCE | 813 lines; SHA-256 `815b95de39607ce391dccd6fbaadbc37fcf8b7f73d4bfea1caeaaf910b610626` |
| 2026-07-16 acceptance reports | Rubric 286 lines, technology 193 lines, two-unit divergence 362 lines; all read through EOF |
| Committed remediation reports | 18 of 18 read through EOF: rubric, technology, and two-unit families at gate, rerun, final, closure, reality-closure, and unanimous-closure stages |

`AGENTS.md`, `tasks.md`, the complete configured BMAD architecture skill, and
its complete headless and reviewer-gate references were read before review. The
remediation reports supplied attack cases only; their verdicts were not treated
as proof. Canonical precedence remained PRD, addendum, DESIGN and EXPERIENCE,
then the architecture spine.

The gate used literal independent-unit interoperability: each seam must force
one admitted input, owner, byte representation, time cut, state transition,
durable result, and recovery outcome. A worked example or named fixture is not
closure when a second conforming construction remains observable.

## Independently Reconstructed Units

| Unit | Independent responsibility |
| --- | --- |
| P-A — Admission and Lifecycle Repository | Allocates generations, appends Promise events, captures paired clocks and repository cuts, and persists plans without consulting reducer behavior. |
| P-B — Reconciliation and Snapshot Reducer | Consumes only an admitted plan plus eligible reports and requests one atomic Snapshot, Findings, diagnostics, and current-pointer transaction. |
| C-A — Same-Binary Scope Worker | Authenticates FD3, proves Ready, validates one assignment, performs only supplied Host work, and emits one bounded result. |
| C-B — Collection Runtime Coordinator | Owns slot epochs, spawn identity, deadlines, per-member dispatch, process gates, transport failure synthesis, report admission, and eventual reaping. |
| S-A — Configuration Schedule Compiler | Computes the barrier-aware worst-case makespan and admits or rejects generation cutoff values without executing workers. |
| D-A — Diagnostic and Attribution Reducer | Allocates canonical diagnostic IDs, materializes self roots, applies process ownership hints, and retains conflicts and suppression evidence. |
| A-A — Action Coordinator | Consumes immutable ActionPlanV1, owns durable launch authorization and receipt, and alone applies terminal precedence and CAS. |
| K-A — Policy Compiler and Historical Reader | Produces canonical policy/scope bytes and renders old decisions without current-default reconstruction. |
| I-A — Release Coordinator | Owns quiescence, recovery-owner publication, FD4 validation, journal steps, KnownGood publication, events, rollback, and terminal result. |
| I-B — SQLite, Migration, and Consumer Adapter | Enforces pragma readbacks and transactions, performs backup/migrate/restore effects, checks ABI, and validates paired service/timer consumers. |

No construction was allowed a late baseline, policy, operation, history,
Promise, wall-clock, discovery, wait-status, or recovery-owner read not granted
by the frozen contract.

## Two-Construction Seam Matrix

Every requested critical seam was reconstructed twice. “A” and “B” below are
plausible independent implementations driven from the same frozen input.

| Critical seam | Construction A | Construction B | Result and exact evidence |
| --- | --- | --- | --- |
| Baseline and paired wall cuts | P-A embeds the accepted baseline projection and one boot/UTC ClockSample while holding admission. | P-B receives only those immutable values and refuses every later repository or wall read. | **CONVERGED.** Later acceptance and wall changes belong to the next generation (`SPINE:943-988`, `1001-1007`). |
| Atomic plan admission | P-A allocates GenerationId, cuts, plan, pins, fingerprint, and latest pointer, then commits. | A failure-injected repository rolls the transaction back at every boundary. | **CONVERGED.** The observable state is all fields or none (`SPINE:943-982`). |
| Operation and resource-history updates | One writer commits an operation phase or sample immediately before admission. | The same writer commits immediately after admission. | **CONVERGED.** Before is in OperationCutV1/ResourceHistoryCutV1; after affects only the next plan (`SPINE:970-985`). |
| Snapshot/current transaction | P-B supplies reports, diagnostics, Observations, Findings, decision version, and expected current revision. | The repository races a newer requested generation against that CAS. | **CONVERGED.** Only latest requested truth can move current; the losing candidate remains non-current evidence (`SPINE:749-753`, `1001-1010`). |
| FD3 Hello and Ready | C-A authenticates parent SO_PEERCRED, validates Hello, and sends one Ready whose first byte carries SCM_CREDENTIALS. | C-B validates the owned PID/birth/executable/group and every echoed field before accepting Ready. | **CONVERGED.** Direction, credentials, identity, deadlines, and replay behavior are byte-total (`SPINE:1332-1378`). |
| Silent and failed workers | C-A stays silent, exits 77, sends malformed Ready, or fails after Request. | C-B applies the deadline-first cause table and synthesizes exactly one AD-5 report for only that scope. | **CONVERGED.** Equality times out; earlier causal failures are canonical invalid output (`SPINE:1403-1497`). |
| Per-member request dispatch and schedule bound | C-B dispatches a ready non-process member immediately and opens a new epoch whenever its slot frees. | S-A treats all lanes at their full configured deadlines as the dominating schedule. | **DIVERGED.** The default trace converges, but FINALPASS-B01 proves a valid early-completion/process-gate trace exceeds the admitted full-deadline bound (`SPINE:326-360`, `380-394`). |
| Process spawn-root barrier | C-B freezes each complete worker root even when its worker is silent or failed. | D-A suppresses only an exact frozen PID/birth or group member and emits unrelated same-inode processes. | **CONVERGED.** The process assignment and report echo the same complete self set (`SPINE:609-619`, `641-668`, `1509-1513`, `1557-1559`). |
| Unrootable-child absence | C-B turns any post-PID setup failure into UnrootableSpawnV1 and blocks every same/later process Host read. | A cleanup implementation proves exact-child reap and, for a known group, zero exact-PGID members. | **CONVERGED.** A missed half-open cut yields process `worker-timeout` with no Request or Host read (`SPINE:621-639`, `1394-1401`). |
| Failure and report evidence cuts | One event loop observes frame classification before wait status. | Another observes wait readiness first but defers classification as required and excludes later cleanup evidence. | **CONVERGED.** Both freeze the same causal cut and candidate bytes; direct report admission additionally requires Result, EOF, and exit zero (`SPINE:1414-1441`, `1480-1492`, `1564-1569`). |
| Canonical policy and Scope bytes | K-A serializes complete PolicySnapshotV1/ScopeIdV1 from typed fields. | An independent verifier parses and re-encodes before comparing fingerprints and LPT order. | **CONVERGED.** JSON grammar, policy preimage, Provider tags, path rules, manifest order, and domains are complete (`SPINE:1252-1284`, `1302-1320`). |
| Diagnostic allocation and process deduplication | C-A creates post-evidence local candidate references and D-A performs the final per-scope merge. | A second reducer receives duplicate worker/coordinator candidates and competing exact/cgroup hints in another arrival order. | **CONVERGED.** Canonical tuple order removes arrival order; exact self/Provider strength, Scope bytes, conflicts, and rejected hints determine one result (`SPINE:548-594`, `656-680`, `1443-1492`). |
| SQLite transactions and pragma readbacks | I-B opens a fresh database and sets WAL/FULL/foreign keys in the required order. | I-B opens an existing database or a second connection with a wrong or differently typed readback. | **CONVERGED.** Every connection either proves `wal`, numeric `2`, and `1` before BEGIN IMMEDIATE or fails closed before a transaction (`SPINE:733-753`). |
| Release journal crash edges | I-A crashes before pending, after pending/effect, and after complete/readback. | I-B restarts from the last rename-complete checked envelope and re-verifies every may-have-executed effect. | **CONVERGED.** Atomic replacement and pending-before-effect/complete-after-readback force one recovery direction (`SPINE:1119-1154`). |
| Recovery-owner races and FD4 | Two replacement owners race after the live lock drops, including PID reuse and a second owner crash. | The candidate validator receives stale and fresh attempt-bound requests. | **CONVERGED.** Exclusive-lock capability, predecessor checksum, gap-free attempt, exact peer identity, and one-use FD4 material admit only the published owner (`SPINE:1065-1117`). |
| KnownGood and rollback | I-A crashes immediately before durable complete `commit-decided`. | I-A crashes immediately after it but before KnownGood or ready admission. | **CONVERGED.** The first restores the prior pair; the second must finish publication, ready, and commit. Explicit rollback is a new transaction (`SPINE:1168-1200`). |
| Exact-artifact ABI validation | CI parses imported `GLIBC_*` versions from the final binary and rejects a maximum above 2.42. | The oldest-runtime lane smokes the byte-identical final artifact rather than a rebuild. | **CONVERGED.** Both gates bind the same artifact (`SPINE:508-518`). |
| Paired timer verification | One installer invokes a service directly after rewriting ExecStart. | The conforming installer activates through each paired timer, observes its trigger advance, and checks service result/status. | **CONVERGED.** Direct service success alone is insufficient; failure restores and proves the complete binary/state/unit/timer pair (`SPINE:524-532`, `1156-1166`). |

## Required Default Four-Worker Reconstruction

The frozen default order is
`[Docker=30, PM2=20, systemd=15, systemd=15, cron=10, cron=10,
cron=10, process=10]`. ScopeIdV1 tags place process after all three cron scopes
at the equal 10-second deadline (`SPINE:923-926`, `1302-1320`).

Assume Docker returns a complete SpawnedWorkerRootV1 but never sends Ready and
the other members become Ready without consuming modeled Provider time beyond
their full lane budgets.

| Time | Slot transition | Gate consequence |
| ---: | --- | --- |
| 0 | Docker silent 0–30; PM2 0–20; two systemd members 0–15 | Ready PM2/systemd requests dispatch without waiting for silent Docker. |
| 15 | The two free systemd slots take two cron members, each 15–25. | Spawn gate remains open. |
| 20 | The PM2 slot takes the third cron member, 20–30. | Spawn gate remains open. |
| 25 | The first free cron slot takes process, 25–35. | All parent-side spawn outcomes are resolved; Docker's complete root is frozen even though it has no Ready. Process closes the gate with no queued successor. |
| 30 | Docker becomes `worker-timeout`; the third cron reaches its lane bound. | Docker affects only its own report. Its frozen root/reap lifecycle cannot add queued work. |
| 35 | Process reaches its bound and the gate reopens. | Every scope is terminal; the modeled makespan is 35 seconds. |

This proves, rather than refutes, the requested 35-second bound. The five-second
margin makes the default 40-second generation cutoff valid. Earlier Ready,
failure, or ordinary completion can move the final process dispatch earlier,
but because process is the final queued scope in this fixture, its gate cannot
strand a successor. The explicit silent-member fixture at `SPINE:448-457` is
therefore internally consistent.

## Blocking Finding

### FINALPASS-B01 — Full-deadline LPT is not a dominating bound after per-slot process dispatch

- **Severity:** Tier 0 / blocking
- **Affected units:** C-B runtime coordinator and S-A configuration compiler
- **Exact evidence:** `SPINE:326-360`, `380-394`, `448-457`, `899-901`,
  `923-931`

AD-10 requires a newly free slot to start the next epoch immediately while the
gate is open. A ready process member closes that gate after parent-side spawn
outcomes are classified; slots which become free during the process cut remain
idle. Configuration is required to consume those exact transitions, but its
claimed worst case makes every lane consume its full deadline and says Ready or
failure patterns cannot exceed that trace. The claim is false when a process
scope is next in LPT order immediately before a would-be free-slot tie.

Use four workers, the valid five-second margin, and these valid configured
deadlines:

| LPT position | Scope | Budget |
| ---: | --- | ---: |
| 1 | systemd user | 20 s |
| 2 | systemd system | 20 s |
| 3 | Docker | 20 s |
| 4 | PM2 | 20 s |
| 5 | process | 10 s |
| 6 | cron user | 9 s |
| 7 | cron root | 9 s |
| 8 | cron system | 9 s |

All values are within ARCH-LIM-2, and the differing deadlines make this exact
LPT order independent of tie interpretation after the first four scopes.

#### Construction A — Full-deadline configuration compiler

1. At 0, S-A assigns the four 20-second scopes.
2. At 20 seconds all four slots free together.
3. One epoch selects process plus the three cron scopes before process closes
   the gate.
4. Cron members reach 29 seconds and process reaches 30 seconds.
5. The computed makespan is 30 seconds, so ARCH-LIM-3 accepts a 35-second
   cutoff after the configured five-second margin.

This follows the literal full-deadline dominating construction at
`SPINE:380-394`.

#### Construction B — Event-driven conforming runtime

1. At 0, C-B assigns the same four 20-second scopes.
2. Systemd user validly terminalizes at `20 s - 1 ns`; the other three remain
   live until exactly 20 seconds.
3. The gate is open and one slot is free, so AD-10 immediately creates a
   one-member epoch for the next LPT scope: process. With a zero-cost successful
   setup it becomes Ready and closes the gate at `20 s - 1 ns`.
4. One nanosecond later the other three original scopes terminalize. Their slots
   remain idle because process owns the closed gate.
5. Process reaches its absolute lane bound at `30 s - 1 ns`; the gate reopens
   and the three queued cron scopes dispatch.
6. Without a generation cutoff their lane bounds are `39 s - 1 ns`. Under the
   35-second cutoff accepted by Construction A, all three instead receive
   generation-cutoff `worker-timeout` reports at 35 seconds.

This follows the immediate-free-slot and process-gate transitions at
`SPINE:326-360`. The 20-second-minus-one-nanosecond completion is legal: a scope
may complete at any strict-before point inside its budget, and zero-cost process
setup is explicitly part of the schedule model (`SPINE:373-390`).

#### Observable divergence

Construction A accepts the configuration and predicts that all three cron lanes
reach their own 29-second bounds without generation-cutoff truncation.
Construction B runs that accepted configuration and produces three premature
generation-cutoff `timed-out` CollectorReportV1 values. A compiler that instead
maximizes over every legal event ordering rejects the same cutoff. The
disagreement changes:

- required and optional strict exit;
- Snapshot scope outcomes and diagnostic bytes;
- current Evidence Status and allowed absence claims;
- Brief completeness and reconciliation Findings; and
- baseline eligibility and later comparison input.

The existing default fixture does not expose the bug because process is last.
The 60-second process fixture does not expose it because process is in the
initial four-slot epoch. Naming “process in every LPT position” and comparing a
trace does not choose the missing near-tie transition or make the false
dominance claim true (`SPINE:442-457`).

#### Required rule

Define one normative `WorstReachableMakespanV1` shared by runtime and
configuration. For fixed ScopeManifest order and worker count, it must maximize
terminal time over every legal integer-boot-nanosecond Ready, terminal failure,
and successful Provider completion point from dispatch through each member's
absolute deadline, applying the exact per-slot epoch, process-gate, unrootable
absence, and generation-cutoff transitions. A process dispatch one nanosecond
before a sibling free-slot tie must be included. Configuration must reject a
cutoff below that maximum plus `max(scheduler_margin, 1 ns)`.

If the intended bound remains the single full-deadline trace instead, AD-10 must
replace immediate per-slot process dispatch with an exact runtime reservation
rule that provably makes that trace dominating. Intent or fixture arithmetic is
not sufficient. Add the 20/20/20/20, process-10, 9/9/9 near-tie fixture and
assert both the full-budget and one-nanosecond-early traces, including admitted
cutoff, request times, gate interval, terminal reports, strict exit, Snapshot,
and Brief.

## Regression Result for All Other Requested Seams

The finding is isolated to runtime/configuration schedule admission. No second
divergence survived the adversarial replay:

- baseline, paired clock, Promise, operation, history, prior-current, and policy
  cuts remain one atomic CollectionPlanV1 input;
- FD3 Hello/Ready, per-scope failure synthesis, causal evidence cuts, canonical
  diagnostics, and report admission remain byte-total;
- every internal child is either a complete frozen root or absent before a
  direct-process Host read;
- diagnostic allocation, ownership winner selection, conflict retention, and
  self suppression are independent of arrival order;
- fresh and existing SQLite connections fail closed before transactions unless
  all pragma readbacks match;
- release admission, journal effects, recovery-owner attempts, FD4 validation,
  KnownGood commit direction, and rollback yield one result at every exercised
  crash edge; and
- exact-artifact ABI and paired timer checks bind the activated binary/state/
  consumer pair and restore that whole pair on failure.

## Mechanical Validation Record

| Validation | Command or method | Result |
| --- | --- | --- |
| Frozen target | `git rev-parse HEAD`; `sha256sum .../ARCHITECTURE-SPINE.md`; `wc -l` | **PASS** — commit `8fd5d31`, SHA-256 `174a3637...bb`, 1,777 lines |
| Complete source basis | Line-bounded reads through EOF plus committed remediation inventory | **PASS** — all mandated architecture, product, UX, acceptance, and 18 remediation reports read |
| Independent schedule arithmetic | Full-budget and one-nanosecond-early event traces | **PASS** — default 35 s; counterexample 30 s compiler trace versus `39 s - 1 ns` unconstrained runtime trace and three 35 s cutoffs |
| BMAD architecture linter | `uv run .agents/skills/bmad-architecture/scripts/lint_spine.py --workspace .../architecture-srvls-2026-07-14` | **PASS** — `ok: true`, zero structural findings |
| AD and ARCH-LIM integrity | Ordered heading/table ID extraction | **PASS** — AD-1 through AD-25 and ARCH-LIM-1 through ARCH-LIM-23 exactly once |
| Markdown lint | `markdownlint-cli2` with canonical UX configuration | **PASS** — one file, zero errors |
| Whitespace/error check | `git diff --check`; `git diff --cached --check` | **PASS** — no whitespace errors |
| Changed-file scope | `git status --short`; report-path comparison | **PASS** — this report is the sole changed path |

## Final Status

**BLOCKED. Verdict: CHANGES REQUIRED. Finding count: 1.** The requested default
silent-member trace proves 35 seconds, but the exact frozen architecture does
not define one safe general cutoff result for the event-driven process gate.
