---
title: "Technology Remediation Rerun - srvls Architecture"
document_type: architecture_review
review_dimension: technology_remediation_rerun
status: final
verdict: "CHANGES REQUIRED"
blocking: true
reviewed_head: d4515067af8314cadf979da7b17921fbafc92d21
reviewed_spine_sha256: 818bea5f4770b3f913fbba3e2e688da14d5f42cb150b2d284c2eb00bc3bae862
reviewed_state: frozen working-tree remediation
review_date: 2026-07-16
reviewer: Professor Fiddlesticks
team: Team Argus
evidence_mode: accepted-research-fresh-reality-rerun
scope: technology, worker IPC, collection scheduling, and release recovery closure
finding_count: 3
blocking_findings: 2
high_findings: 1
---

<!-- markdownlint-disable MD013 MD025 -->

# Technology Remediation Rerun

## Verdict

**CHANGES REQUIRED.** The exact 1,429-line spine with SHA-256
`818bea5f4770b3f913fbba3e2e688da14d5f42cb150b2d284c2eb00bc3bae862`
closes the immutable technology acceptance report's SQLite, ABI, and managed
systemd consumer findings. It also makes the bounded FD3 scope assignment,
diagnostic grammar, ordinary release admission, atomic release journal,
KnownGood commit decision, and public release-event projection substantially
implementable.

Three technology/reality seams remain:

1. AD-25's two oversized-frame terminal scope failures have no required
   mapping into AD-5's exhaustive CollectorReport shape or six Collector
   outcomes.
2. crash recovery reruns candidate validation under a new release process, but
   FD4 authenticates that process against the manifest's original
   release-owner PID/birth/executable identity and defines no recovery-owner
   rebind.
3. the direct-process worker-spawn barrier can stall one-shot replacement
   workers, but AD-10 admission simulates only the barrier-free LPT schedule.

The first two are blocking cross-unit contradictions. The third makes a valid
configuration capable of deterministic false timeouts. No broader technology
research or dependency change is required; all three are focused architecture
contract fixes. The spine correctly remains `status: draft`.

This review writes only this new report. It does not amend the spine, memlog,
canonical product or UX artifacts, product code, `tasks.md`, or any prior
review.

## Review Basis

Citation keys:

- `SPINE` —
  `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md`
- `MEMLOG` — the sibling `.memlog.md`
- `TECH-CURRENCY` — `reviews/review-technology-currency-2026-07-16.md`
- `TECH-ACCEPT` — `reviews/review-technology-acceptance-2026-07-16.md`
- `DIVERGENCE-ACCEPT` —
  `reviews/review-two-unit-divergence-acceptance-2026-07-16.md`
- `RUBRIC-ACCEPT` — `reviews/review-rubric-acceptance-2026-07-16.md`
- `PRD` — the canonical 2026-07-16 `prd.md` and `addendum.md`
- `DESIGN` and `EXPERIENCE` — the canonical 2026-07-16 UX spines

The current SPINE, complete MEMLOG, canonical PRD and addendum, DESIGN,
EXPERIENCE, all three immutable acceptance reports, the completed technology
currency record, and both independent remediation-gate reports were read
through EOF. The target was rehashed before and after the semantic pass. No
conclusion from the interrupted prior-hash review was carried forward.

This is a fresh semantic rerun against the frozen hash, not a new dependency
currency survey. Same-day completed probes and official-source conclusions in
TECH-CURRENCY remain the accepted research basis. Repository reality still has
no product `Cargo.toml`, `Cargo.lock`, or release artifact, so this report
judges whether the spine assigns executable proof rather than claiming that
implementation proof already exists.

The approval standard is literal: a story must be unable to choose a weaker
outcome, identity, ordering, cutoff, or recovery path while still conforming to
the Rule. Named fixtures do not repair a missing production contract.

## Required Technology and Reality Matrix

| Required seam | Result | Frozen-spine evidence and reality assessment |
| --- | --- | --- |
| Fresh and existing SQLite initialization | **PASS** | AD-16 requires `journal_mode=WAL` outside a transaction with returned `wal`, then per-connection WAL readback, `synchronous=FULL` numeric `2`, `foreign_keys=ON` numeric `1`, and busy timeout before any transaction; writers then use `BEGIN IMMEDIATE` (`SPINE:588-600`). Fresh/existing fixtures are mandatory (`SPINE:384-386`). |
| Exact release ABI floor | **PASS** | Release CI runs `readelf --version-info` on the final artifact, fails above `GLIBC_2.42`, and smokes that same artifact in the pinned oldest-supported glibc 2.42 runtime (`SPINE:404-413`). `readelf` is present on the review Host; artifact proof remains correctly assigned to release CI. |
| Managed absolute `ExecStart` migration | **PASS** | Every managed absolute consumer, expressly `srvls-metrics.service` and `srvls-snapshot.service`, is rewritten to the canonical activated binary; loaded `ExecStart`, timer trigger advancement, `Result=success`, and `ExecMainStatus=0` are read back, and any failure restores and reproves the whole binary/state/unit/timer/daemon pair (`SPINE:417-429`, `SPINE:973-983`). |
| Atomic CollectionPlan admission and frozen cuts | **PASS** | One `BEGIN IMMEDIATE` operation allocates GenerationId, captures paired boot/wall time and repository revision, freezes Promise/policy/scope/baseline/operation/history/current cuts, inserts canonical plan plus fingerprint and pins, and updates latest-requested or commits none (`SPINE:792-835`). Workers receive only bounded scope projection (`SPINE:837-857`). |
| Canonical policy and Scope identity bytes | **PASS** | CanonicalJsonV1 fixes scalar, escape, key, order, integer, binary, optional, and rejection rules; CollectionPlan includes every admitted field (`SPINE:1058-1112`). Scope tags, framing, path/string normalization, display, manifest order, and fingerprint are byte-complete (`SPINE:1114-1132`). |
| FD3 route, peer checks, framing, request/result, streams, exits, timeout, signal, mismatch, and no discovery | **PASS EXCEPT OVERSIZE TERMINALIZATION** | The reserved raw route, Unix stream, `SO_PEERCRED`, same-executable check, one-use capability, length caps, byte-total request/result, plan and assignment fingerprints, `/dev/null` stdio, exit meanings, process-group cutoff, and no-discovery child behavior are explicit (`SPINE:1139-1243`). TRR-B01 is the remaining outcome-shape contradiction. |
| Diagnostic construction after evidence | **PASS** | AD-13 fixes per-scope ordinal partition, real-scope coordinator diagnostics, tagged byte-complete subject and parameter grammars, duplicate occurrence, producer-local reference, post-cut merge/sort, atomic rewrite, and invalid-reference rejection (`SPINE:444-490`). |
| Process ownership and self suppression | **PASS EXCEPT BARRIER SCHEDULING** | Self membership is exact PID/birth/device/inode, unrelated same-inode processes are excluded, ownership evidence and winner direction are total, and suppression retains conflicts and diagnostics (`SPINE:505-538`). TRR-H01 concerns the barrier's interaction with the separate scheduling contract, not the suppression decision table. |
| Crash-persistent ordinary release admission | **PASS** | Every stateful entry retains a shared lease and refuses before SQLite unless admission is `ready` with no nonterminal transaction; only release may acquire exclusive recovery ownership (`SPINE:896-910`). |
| FD4 candidate validation bypass | **PASS FOR THE INITIAL OWNER; FAIL AFTER OWNER CRASH** | The initial exchange is a bounded, single-use, read-only, no-forwarding, fail-closed FD4 protocol (`SPINE:912-937`). TRR-B02 shows that its manifest-owner comparison cannot be satisfied by a later recovery owner. |
| Atomic UpgradeTransaction effects | **PASS** | Checksummed canonical envelopes use unique no-follow temporary files, file fsync, atomic rename, and directory fsync; every effect records durable pending before execution and complete only after readback, with `pending` treated as may-have-executed (`SPINE:939-971`). |
| KnownGood commit decision and explicit rollback | **PASS** | The prior pair is staged, `commit-decided` is the irreversible durable boundary, KnownGood publication and readback precede ready admission, post-decision recovery must finish forward, exactly one record remains, and rollback creates a new transaction (`SPINE:985-1015`). |
| Durable release events and crash results | **PASS** | Every internal step maps to one public phase and canonical UX label; event results map to pending/running/passed/failed/skipped-with-reason, durable emission boundaries are fixed, and final machine results are exhaustive (`SPINE:1017-1050`). |
| Named property, concurrency, crash, IPC, timer, and rollback fixtures | **PARTIAL** | AD-11 contains the prior requested families (`SPINE:371-397`). The two missing cross-unit mappings and the barrier-aware schedule counterexample below are not currently named and cannot be inferred from those fixtures. |

## Tier 0 - Blocking Findings

### TRR-B01 - Oversized worker failures cannot produce the required terminal Collector report

AD-5 makes the collection shape exhaustive. Every Collector returns generation,
scope, obligation, Observations, duration, diagnostics, and exactly one of six
outcomes; every frozen scope has one terminal report (`SPINE:149-161`). Strict
policy differs by outcome: every non-complete required scope fails, while
`partial`, `denied`, `timed-out`, and `invalid-output` also fail regardless of
obligation (`SPINE:155-157`).

AD-25 instead defines `worker-request-too-large` and
`worker-result-too-large` as terminal scope failures and says they participate
in obligation and strictness, but it does not synthesize a CollectorReport or
map either code to one of AD-5's six outcomes (`SPINE:1154-1166`). The request
case has no worker report at all; the result case explicitly refuses allocation
and parsing. `WorkerResultV1` cannot close the gap because its tagged variants
exist only after a valid result frame (`SPINE:1210-1227`).

Two conforming reducers can therefore choose `invalid-output`, `unavailable`, a
failed CollectionAttempt with no scope report, or an extra seventh outcome.
Those choices change strict-mode success, completeness, Snapshot eligibility,
and machine output. Saying the codes “participate” does not choose one.

**Required closure:** define one coordinator-synthesized
`CollectorReportV1` for each pre-request, framing, authentication, abnormal
worker-exit, and oversized-result failure. Fix its duration, empty evidence,
diagnostic ownership, and one existing AD-5 outcome, or version AD-5 with an
explicit exhaustive transport-failure outcome and all strictness projections.
Add request-at-limit, request-one-over, result-at-limit, result-one-over, and
required/optional strict-mode fixtures that assert the complete persisted
report and public result.

### TRR-B02 - Crash-resumed FD4 validation authenticates against a dead release owner

`UpgradeTransactionV1` stores one release-owner PID, birth, and executable
identity (`SPINE:939-944`). FD4 then requires the candidate's peer parent to
match that manifest release-owner identity before admission or SQLite
(`SPINE:912-925`). This is sound for the process that created the manifest.

It is not sound for the required recovery interleaving:

1. release process A persists candidate-validation `pending` with A as the
   manifest owner;
2. A crashes and the kernel releases its exclusive `flock`;
3. release process B acquires exclusive recovery ownership and persists the
   resumed attempt; and
4. B launches the staged candidate to rerun validation, as pending-effect
   recovery requires (`SPINE:966-971`).

The candidate observes B through `SO_PEERCRED` and `getppid()`, but the manifest
still names A. The mandatory comparison fails closed as
`upgrade-recovery-required`. No Rule atomically rebinds the active release owner
or distinguishes immutable original owner from the authenticated recovery
attempt. Inferring such a rebind would create a second transaction and security
contract not present in the spine.

**Required closure:** retain the original owner as history, but add a versioned
`ReleaseRecoveryAttemptV1` or active-owner field that only the exclusive-lock
holder may atomically publish after proving the prior owner is gone. Bind the
FD4 request, peer PID/birth/executable check, capability, and result to that
specific recovery attempt. Define PID-reuse and failed-takeover behavior. Add a
crash at candidate-validation pending followed by a different PID/birth, plus
old-PID reuse, forged rebind, and second-crash fixtures.

## Tier 1 - High Finding

### TRR-H01 - The process spawn barrier is absent from the accepted LPT cutoff model

AD-10 says a fixed pool runs the exact LPT schedule and configuration accepts a
generation cutoff when it is at least that simulated makespan plus scheduler
margin (`SPINE:317-323`). ARCH-LIM-1 permits one to eight workers;
ARCH-LIM-2 permits every scope deadline from 1 to 60 seconds; and ARCH-LIM-3
permits zero scheduler margin (`SPINE:752-756`). AD-25 workers are one-shot:
one request, one result, then EOF (`SPINE:1154-1157`).

The new self-suppression rule globally blocks worker spawn from immediately
before the process worker is released until its Host-read cut closes
(`SPINE:505-512`). That delay is absent from the LPT simulation. A valid
counterexample uses four workers, a 60-second process deadline, seven 1-second
scope deadlines, zero margin, and a 60-second cutoff. Barrier-free LPT has a
60-second makespan and passes configuration. At dispatch, the process worker
and three short workers consume the pool. When the short one-shot workers exit,
their queued successors cannot be spawned while the process cut remains open.
If that cut closes near its valid deadline, remaining scopes cannot dispatch
before the admitted generation cutoff and become false timeouts.

Pre-spawning all eight one-shot children would exceed the configured four-worker
pool. Reusing four children would contradict the single-request/single-result
FD3 contract. Delaying the process scope can contradict descending-deadline LPT.
The current Rules choose none of those behaviors.

**Required closure:** make the barrier part of the exact admission-time schedule
and cutoff simulation, or define a pool-compatible process-scan ordering or
authenticated persistent-worker protocol that preserves the accepted model.
Specify whether provider grandchildren are also inside the barrier's process
evidence treatment. Add the 60/1-second, zero-margin counterexample, process
scope in every LPT position, and near-deadline Host-read fixtures.

## Contracts That Remain Closed

No additional finding remains for:

- Rust 2024, resolver 3, MSRV 1.88 and current-stable locked lanes;
- the `rusqlite = "=0.39.0"` / `libsqlite3-sys 0.37.0` / bundled SQLite
  3.51.3 graph and `toml = "=1.1.3"` manifest form;
- Linux `CLOCK_BOOTTIME`, one-binary delivery, bootstrap-before-Provider
  sequencing, and explicit Provider/action bounds;
- baseline, operation, history, repository, and paired-clock CollectionPlan
  cuts and atomic admission;
- byte-complete PolicySnapshot, Scope, diagnostic, and bounded scope-assignment
  contracts;
- deterministic ownership hints, conflicts, self membership, suppression, and
  retained diagnostics, apart from the scheduling interaction in TRR-H01;
- ordinary crash-persistent release admission, atomic/checksummed manifest
  replacement, write-ahead/write-after effect ordering, KnownGood retention,
  explicit rollback, and public release-event mapping; and
- exact-artifact ABI proof and managed timer-consumer migration.

## Validation Record

| Validation | Command or method | Result |
| --- | --- | --- |
| Frozen target identity | `git rev-parse HEAD`; `sha256sum <SPINE>` before and after review | **PASS** - head `d4515067af8314cadf979da7b17921fbafc92d21`; exact required SHA-256 retained. |
| Required complete reads | Line-bounded reads through EOF for SPINE, MEMLOG, PRD, addendum, DESIGN, EXPERIENCE, acceptance reports, technology currency, and remediation gates | **PASS** - no prior-hash conclusion reused. |
| Accepted reality evidence | TECH-CURRENCY and TECH-ACCEPT claim-by-claim comparison | **PASS** - completed research retained; absent product artifacts are not presented as proof. |
| Architecture linter | `uv run .agents/skills/bmad-architecture/scripts/lint_spine.py --workspace _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14` | **PASS** - `ok: true`; zero findings. |
| AD integrity | Ordered heading extraction | **PASS** - AD-1 through AD-25 exactly once; original AD-1 through AD-24 remain unrenumbered. |
| ARCH-LIM integrity | Ordered table-definition extraction | **PASS** - ARCH-LIM-1 through ARCH-LIM-23 exactly once. |
| Required-term inspection | Exact `rg -n` sweep for SQLite, ABI, managed services, SelfProcessSet, oversize results, FD4 bypass, commit decision, KnownGood, and release events | **PASS** - every requested term lands in an enforceable Rule; semantic contradictions are reported rather than hidden by token presence. |
| Technology/reality semantic gate | Required-seam matrix plus crash, IPC, and scheduling interleavings | **FAIL** - TRR-B01, TRR-B02, and TRR-H01. |
| Markdown lint | `markdownlint-cli2` with the canonical UX lint profile against this report | **PASS** - one file; zero errors. |
| Whitespace/error check | `git diff --check` | **PASS** - no output. |
| Changed-file scope | Target-path presence and `git status --short` | **PASS** - this reviewer added only this new rerun report; shared remediation artifacts were already present. |

The deterministic linter proves mechanical spine structure. It cannot detect
the three cross-rule interleavings above.

## Final Gate Status

**BLOCKED. Verdict: CHANGES REQUIRED.** SQLite, ABI, managed consumer,
canonical encoding, diagnostic, initial FD3/FD4, release journal, KnownGood,
rollback, and release-event technology contracts are accepted. Remap every
worker transport failure into the exhaustive collection result, make FD4
recovery authenticate the current exclusive recovery attempt, and reconcile
the direct-process spawn barrier with the admitted schedule before this exact
spine can receive technology approval.
