---
title: "srvls Architecture Final Good-Spine Acceptance"
type: architecture-review
status: final
created: 2026-07-16
updated: 2026-07-16
reviewer: Bartholomew the Builder
review_mode: independent-good-spine-final-pass
reviewed_commit: 8fd5d312fabe544163d9b57b6b933e56b5133414
reviewed_spine_sha256: 174a3637d185c63fe8118a01827332e8f712525681f42602efaedff6de6a2cbb
verdict: changes-required
finding_count: 1
blocking_findings: 0
high_findings: 0
moderate_findings: 0
low_findings: 1
---

<!-- markdownlint-disable MD013 MD025 -->

# Architecture Review: Final Good-Spine Acceptance

## Verdict

**CHANGES REQUIRED. Finding count: 1.**

Commit `8fd5d312fabe544163d9b57b6b933e56b5133414` passes every
requested semantic safety probe. Its default four-worker schedule converges to
the exact 35-second makespan with five seconds of configured cutoff margin; its
frozen read cuts, worker IPC, diagnostic construction, process barriers,
SQLite transactions, release journal, recovery, ABI, and managed-timer
postconditions each select one implementable result.

Approval is nevertheless unavailable under the required zero-finding rule.
The Structural Seed lists the same concrete module path,
`src/adapters/worker.rs`, twice with different ownership descriptions. That
is a low-severity, locally remediable implementation-boundary defect, but it
allows independently assigned stories to claim the same module and means the
seed cannot be instantiated literally.

Prior verdicts were treated as an attack inventory and historical evidence,
never as authority. This verdict comes from a complete fresh read and
independent reconstruction of the frozen commit.

## Frozen Target

| Property | Observed value |
| --- | --- |
| Branch | `feature-bartholomew-architecture-final-pass` |
| Commit | `8fd5d312fabe544163d9b57b6b933e56b5133414` |
| Commit subject | `docs(architecture): integrate final acceptance remediation` |
| Spine | `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md` |
| Spine size | 1,777 lines |
| Spine SHA-256 | `174a3637d185c63fe8118a01827332e8f712525681f42602efaedff6de6a2cbb` |
| Worktree before review | Clean |

The repository contains lowercase `tasks.md`, not uppercase `TASKS.md`.
The complete lowercase task ledger was read as the project task source and was
not edited.

## Complete Review Basis

The reviewer read each of these inputs through EOF:

- `AGENTS.md`, `tasks.md`, the complete BMAD architecture skill, and its
  `headless.md` and `reviewer-gate.md` references;
- the 143-line architecture `.memlog.md` and the complete 1,777-line
  `ARCHITECTURE-SPINE.md`;
- the final 823-line PRD and 63-line addendum;
- the final 329-line UX `DESIGN.md` and 813-line `EXPERIENCE.md`;
- the three architecture acceptance reports dated 2026-07-16: rubric,
  technology, and two-unit divergence; and
- all 18 committed remediation reports: gate, rerun, final, closure,
  reality-closure, and unanimous-closure for each of the rubric, technology,
  and two-unit review families.

The current Rust stable channel and every crate lock target in the Stack table
were independently checked against the official Rust distribution channel and
Crates.io API. Rust stable was `1.97.1` dated 2026-07-14. Every named crate
target exists and is not yanked; the `toml =1.1.3` requirement resolves to
registry version `1.1.3+spec-1.1.0`. The deliberately locked
`rusqlite 0.39.0` and `libsqlite3-sys 0.37.0` remain valid non-yanked lock
targets even though newer compatible lines exist.

## Independent Four-Worker Schedule Reconstruction

### Frozen order and conditions

AD-20 supplies eight budgets:

`[Docker=30, PM2=20, systemd-user=15, systemd-system=15,
cron-user=10, cron-root=10, cron-system=10, process=10]`

AD-10 sorts descending by budget and then by canonical ScopeIdV1 bytes. AD-24
places the equal ten-second scopes in cron-user, cron-root, cron-system,
process order. Four slots are available. The adversarial member is the
30-second Docker lane: spawn/root construction succeeds, but its Hello/Ready
lane stays silent through its absolute deadline. Every shorter member becomes
Ready without consuming modeled time. This is the exact silent-Ready fixture,
not an unresolved spawn or unrootable-child case.

### Event trace

| Boot time | Worker 0 | Worker 1 | Worker 2 | Worker 3 | Gate/result |
| ---: | --- | --- | --- | --- | --- |
| 0 s | Docker 30: silent, no Request | PM2 20: Request immediately | systemd-user 15: Request immediately | systemd-system 15: Request immediately | Spawn gate open; the three Ready siblings do not wait for Docker |
| 15 s | Docker still silent | PM2 running | cron-user 10: new epoch and immediate Request | cron-root 10: new epoch and immediate Request | Both newly free slots dispatch without waiting for the earlier batch |
| 20 s | Docker still silent | cron-system 10: new epoch and immediate Request | cron-user running | cron-root running | The newly free slot dispatches independently |
| 25 s | Docker still silent | cron-system running | process 10: new epoch, root freeze, immediate Request | idle | Process is the final equal-budget scope; spawn gate closes with no queued successor |
| 30 s | Docker gets `worker-timeout`, never a Request | cron-system terminal | process running | idle | Freed slots remain idle behind the process gate; no work is queued |
| 35 s | idle | idle | process terminal | idle | Gate reopens; generation makespan is exactly 35 seconds |

The three Ready members of epoch zero receive their requests per member at
Ready, rather than at the silent member's deadline. Later open-gate dispatch
epochs occur at 15, 20, and 25 seconds. The silent Docker root is representable
in the process freeze, so its absent Ready does not create an unrootable-child
barrier. The process lane ends at 35 seconds and has no queued successor for
its closed-gate interval.

The default cutoff is 40 seconds:

`40 s cutoff - 35 s exact makespan = 5 s scheduler margin`

This matches AD-10's runtime/configuration event model, the explicit AD-11
fixture, and ARCH-LIM-3 at `SPINE:321-394`, `SPINE:442-457`, and
`SPINE:899-901,923-931`.

## Requested Safety-Cut Results

| Probe | Result | Fresh acceptance evidence |
| --- | --- | --- |
| Immutable baseline cut | **PASS** | AcceptedBaselineCutV1 embeds the complete versioned comparison projection and canonical rows; the reducer performs no later baseline lookup (`SPINE:943-969,977-988`). |
| Operation, history, prior-current, and wall cuts | **PASS** | OperationCutV1, ResourceHistoryCutV1, prior-current ID/revision, and one paired boot/UTC ClockSampleV1 are captured in admission; later repository and wall reads are forbidden inputs to reconciliation (`SPINE:943-975,990-1007`). |
| Atomic plan admission | **PASS** | One `BEGIN IMMEDIATE` allocates GenerationId, captures every cut, inserts canonical plan/fingerprint and pins, and updates latest-requested, or commits none (`SPINE:943-988`). |
| IPC authentication | **PASS** | Same-binary FD3 uses a reserved route, Unix stream, SO_PASSCRED, child SO_PEERCRED, executable device/inode equality, one-use 256-bit capability, and exact Hello/Ready SCM credentials before Host work (`SPINE:1327-1388`). |
| IPC byte and terminal contracts | **PASS** | Four length-prefixed CanonicalJsonV1 frames, exact caps, replay/mismatch rules, total failure precedence, bounded synthetic reports, exact request/result schemas, EOF/exit rules, and no child discovery leave one wire result (`SPINE:1345-1588`). |
| Policy grammar | **PASS** | CanonicalJsonV1 fixes normalization, escaping, key/array order, integer grammar, typed absence, binary/path representation, and the complete PolicySnapshotV1 fingerprint preimage (`SPINE:1252-1284`). |
| Scope grammar | **PASS** | ScopeIdV1 assigns fixed Provider tags and fields, raw-path normalization, equality/order/display rules, ScopeManifest framing, and one fingerprint preimage (`SPINE:1302-1320`). |
| Diagnostic allocation | **PASS** | Candidates are created after evidence, sorted by one complete byte tuple, referenced locally, merged after the cut, assigned per-scope gap-free ordinals, and atomically rewritten (`SPINE:548-594`). |
| Diagnostic deduplication | **PASS** | Exact identity, hint strength, Provider/Scope tie order, selected owner, conflicts, rejected hints, and retained suppression evidence make duplicate-process reduction total (`SPINE:648-683`). |
| Process roots | **PASS** | Every returned PID becomes OwnedSpawnV1, refines to a complete root, or becomes an unrootable record; complete groups remain frozen until proven empty (`SPINE:609-624`). |
| Unrootable-child barrier | **PASS** | Exact child reap and, where applicable, zero group membership are required before current or later process Host-read; a missed cut times out without Request and later reap cannot rewrite truth (`SPINE:621-647,1394-1401`). |
| Journal phase ordering | **PASS** | Checksummed no-follow O_EXCL replacement is file-fsynced, atomically renamed, and directory-fsynced; every effect records pending before execution and complete only after required readback (`SPINE:1119-1154`). |
| Release recovery ownership | **PASS** | Durable ReleaseAdmissionV1 precedes SQLite, recovery attempts are gap-free and lock-capability bound, and FD4 validation is attempt-, peer-, capability-, generation-, and candidate-bound (`SPINE:1037-1117`). |
| KnownGood and rollback | **PASS** | Completed `commit-decided` is the irreversible boundary; publication, ready admission, and commit follow in order; pre-decision recovery restores the whole pair, and explicit rollback is a new transaction (`SPINE:1168-1200`). |
| SQLite readbacks | **PASS** | Initialization requires returned WAL, WAL on every connection, synchronous numeric 2, foreign keys numeric 1, and busy timeout before any transaction; writers then use `BEGIN IMMEDIATE` (`SPINE:733-745`). |
| ABI gate | **PASS** | Release CI checks the exact final artifact with `readelf --version-info`, rejects imports above GLIBC_2.42, and smokes that same artifact in the oldest supported runtime (`SPINE:503-517`). |
| Managed timer postconditions | **PASS** | Every managed absolute ExecStart is rewritten and read back after daemon-reload; each timer must advance and its triggered service must report `Result=success` and `ExecMainStatus=0`; failure restores and revalidates the whole pair (`SPINE:518-532,1156-1166`). |

No counterexample survived these semantic probes. In particular, malformed
and oversized worker exchanges cannot create a seventh Collector outcome;
process cleanup cannot leak an internal child into Host truth; a crash cannot
move release recovery across the durable commit decision; and a successful
service start without a timer-originated activation does not satisfy release
validation.

## Good-Spine Rubric

| Rubric dimension | Result | Assessment |
| --- | --- | --- |
| Real lower-level divergence points | **PASS except FINAL-LOW-01** | AD-1 through AD-25 cover the domain, state, worker, action, configuration, UI, release, and operational seams. The duplicate module path is the one remaining implementation-boundary divergence. |
| Enforceable AD Rules | **PASS** | Each AD has Binds, Prevents, and a normative Rule; named fixtures and boundary tests make the critical contracts observable. |
| Deferred discipline | **PASS** | Deferred items have explicit revisit conditions and do not reopen v1 safety, identity, persistence, release, or output invariants (`SPINE:1757-1777`). |
| Current named technology | **PASS** | Official live registry/channel checks confirmed the toolchain and every locked crate target exists and is non-yanked. |
| Brownfield ratification | **PASS** | The legacy Python compatibility behavior and smoke/golden lanes remain explicit migration oracles; the Rust seed does not silently redefine the frozen compatibility surface. |
| PRD/addendum coverage | **PASS** | Functional, nonfunctional, safety, compatibility, release, history, and lifecycle capabilities are bound by ADs and trace rows; no required product capability is omitted. |
| UX coverage | **PASS** | TUI ownership, terminal lifecycle, linear/machine surfaces, accessibility, responsive behavior, and release-progress truth retain the final DESIGN/EXPERIENCE contracts. |
| Parent-spine compatibility | **N/A** | No inherited parent architecture spine is declared for this feature-level workspace. |
| Operational/environmental envelope | **PASS** | Local Host, Linux/glibc target, privileges, filesystem/state, subprocess limits, service/timer deployment, recovery, observability, and CI/release gates are decided. |
| Structural Seed | **FAIL** | The same concrete adapter path appears twice with different responsibility descriptions. |

## Finding

### FINAL-LOW-01 — Structural Seed assigns one module path twice

- **Severity:** Low
- **Acceptance effect:** Blocking under the required zero-finding rule
- **Evidence:** `ARCHITECTURE-SPINE.md:1679` lists
  `worker.rs # authenticated FD3 parent/child protocol` under
  `src/adapters/`. `ARCHITECTURE-SPINE.md:1682` lists the same
  `src/adapters/worker.rs` path again as
  `worker.rs # FD3/FD4 authentication, framing, child entry`.

**Counterexample:** Story A follows line 1679 and implements
`adapters::worker` as the FD3 collection-worker boundary, leaving FD4
release-validator mechanics in adjacent `adapters::release`. Story B follows
line 1682 and independently makes that same `adapters::worker` module own
both FD3 and FD4 authentication, framing, and child entry. Both stories follow
a literal seed entry, but integration cannot preserve both module ownership
maps: they edit the same file, choose different public interfaces, and place
the FD4 dependency boundary in different modules.

**Impact:** The normative AD-23 and AD-25 protocols remain semantically
complete, so this does not weaken runtime safety. It does make the cold-start
tree impossible to instantiate as written, creates an avoidable parallel-story
merge and ownership collision, and prevents
`tests/architecture_boundaries.rs` from deriving one unambiguous expected
adapter layout.

**Required remediation:** Give every Structural Seed module one unique path.
Either collapse both rows into a single `adapters/worker.rs` entry whose
comment explicitly owns both FD3 and FD4, or retain the FD3
`adapters/worker.rs` row and rename the FD4 boundary to a distinct path such
as `adapters/release_validator.rs`, with `adapters/release.rs` ownership
clarified accordingly. Remove the duplicate row and add a boundary fixture if
the split affects dependency enforcement.

No spine edit is made by this reviewer.

## Mechanical Validation

| Check | Result |
| --- | --- |
| Frozen commit and SHA-256 before review | **PASS** |
| Complete required-source reads | **PASS** |
| BMAD `lint_spine.py` | **PASS** — `ok: true`, zero mechanical findings |
| AD sequence | **PASS** — AD-1 through AD-25 exactly once and in order |
| ARCH-LIM sequence | **PASS** — ARCH-LIM-1 through ARCH-LIM-23 exactly once |
| Official Rust/Crates.io target verification | **PASS** |
| Markdown lint on this report | **PASS** — zero errors |
| `git diff --check` | **PASS** — no whitespace errors |
| Changed-file scope | **PASS** — only this new report |

## Final Status

**CHANGES REQUIRED. One low-severity finding exists.** All requested safety
contracts pass, but approval would violate the explicit zero-findings
acceptance rule until FINAL-LOW-01 is remediated.
