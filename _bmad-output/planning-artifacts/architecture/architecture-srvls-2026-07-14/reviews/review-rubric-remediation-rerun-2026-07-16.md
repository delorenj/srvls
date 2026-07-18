---
title: "srvls Architecture Remediation Good-Spine Gate Rerun"
document_type: architecture_review
review_dimension: good_spine_remediation_rerun
status: final
verdict: approved
blocking: false
review_date: 2026-07-16
reviewer: rubric-gate
reviewed_base_commit: d4515067af8314cadf979da7b17921fbafc92d21
reviewed_worktree_spine_sha256: 818bea5f4770b3f913fbba3e2e688da14d5f42cb150b2d284c2eb00bc3bae862
reviewed_worktree_patch_id: d881e20c6997e87662fa091e9b6a1505bf517118
reviewed_artifact: _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md
rerun_of: review-rubric-remediation-gate-2026-07-16.md
finding_count: 0
blocking_findings: 0
high_findings: 0
moderate_findings: 0
---

<!-- markdownlint-disable MD013 MD025 -->

# srvls Architecture Remediation Good-Spine Gate Rerun

## Verdict

**APPROVED.** The frozen revised `ARCHITECTURE-SPINE.md` at exact SHA-256
`818bea5f4770b3f913fbba3e2e688da14d5f42cb150b2d284c2eb00bc3bae862`
contains no blocker, high, or moderate architecture gap under the BMAD
good-spine rubric. GATE-B01, GATE-B02, GATE-H01, GATE-H02, and GATE-M01 from the
first remediation gate are literally closed. The direct-process worker barrier
has one implementable happens-before relation, and the previously accepted
compatibility, release, state, UX, operational-limit, Seed, Deferred, and trace
contracts remain intact.

The spine correctly remains a draft build substrate rather than claiming final
status (`SPINE:1-10`).

## Review Basis

Citation keys:

- `SPINE` —
  `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md`
- `MEMLOG` — the complete sibling `.memlog.md`
- `PRD` —
  `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md`
- `ADD` — the canonical PRD `addendum.md`
- `DESIGN` — the canonical UX `DESIGN.md`
- `EXPERIENCE` — the canonical UX `EXPERIENCE.md`
- `TECH-ACC` — `reviews/review-technology-acceptance-2026-07-16.md`
- `DVG-ACC` — `reviews/review-two-unit-divergence-acceptance-2026-07-16.md`
- `RUBRIC-ACC` — `reviews/review-rubric-acceptance-2026-07-16.md`
- `FIRST-GATE` — `reviews/review-rubric-remediation-gate-2026-07-16.md`

This rerun discarded the interrupted prior-hash analysis. It read the complete
1,429-line revised spine from the frozen hash, checked the complete memlog and
three immutable acceptance reports already used by the gate, and revalidated
the unchanged canonical PRD, addendum, DESIGN, and EXPERIENCE sources against
their prior complete reads and exact hashes. The PRD, addendum, DESIGN, and
EXPERIENCE hashes remain respectively `576186a6...`, `1848ab13...`,
`e68b22d5...`, and `815b95de...`. The review applies the complete
`bmad-architecture` headless good-spine and reviewer-gate instructions and
judges constructibility and cross-unit interoperability, not token presence.

## Good-Spine Rubric

| Check | Result | Binding evidence |
| --- | --- | --- |
| Real divergence points are fixed one level down | **PASS** | Plan admission, pure reduction, worker IPC, diagnostics, process ownership, release recovery, storage initialization, and deployed-consumer proof now have shared shapes and total rules (`SPINE:357-397`, `SPINE:432-538`, `SPINE:582-651`, `SPINE:786-857`, `SPINE:884-1243`). |
| Every AD Rule is enforceable and prevents its stated divergence | **PASS** | The five first-gate contradictions and ambiguities are closed in their owning ADs; no implementation must invent a missing cross-unit field or order. |
| Deferred cannot permit incompatible v1 stories | **PASS** | Every item preserves a concrete v1 choice and names a later trigger (`SPINE:1409-1429`). |
| Named technology is verified-current | **PASS** | The same-day technology record remains the governing accepted evidence, and the corrected lock graph and target stack are preserved (`SPINE:1273-1295`; `TECH-ACC:159-174`). |
| Brownfield behavior is ratified rather than contradicted | **PASS** | Raw profile routing, legacy verb arity, compatibility presenters, layered oracle, and direct-process exclusion from legacy surfaces remain explicit (`SPINE:240-310`). |
| Canonical PRD and UX capabilities land semantically | **PASS** | The frozen plan can now produce FR-27/FR-28 change truth, UJ-5 owns duplicate and historical hot evidence, and all capability families retain architecture owners (`SPINE:801-857`, `SPINE:1367-1407`; `PRD:456-480`; `EXPERIENCE:668-684`). |
| No AD weakens or contradicts another | **PASS** | AD-18's closed input is supplied by AD-21/AD-24; AD-10's subprocess boundary is supplied by AD-7/AD-25; AD-13 IDs and suppression are reducible from accepted reports (`SPINE:245-249`, `SPINE:674-709`, `SPINE:786-857`, `SPINE:1099-1243`). |
| Deployment and environment envelope is decided | **PASS** | Exact artifact ABI proof, oldest-runtime smoke, install ownership, consumer rewrites, release admission, recovery, and local Host scope remain binding (`SPINE:399-430`, `SPINE:884-1050`). |
| Provider and operational strategy is decided | **PASS** | Deterministic scheduling, typed scope assignments, authenticated same-binary workers, frame boundaries, subprocess outcomes, privilege, cutoff, cancellation, and no discovery are closed (`SPINE:312-355`, `SPINE:561-580`, `SPINE:741-857`, `SPINE:1139-1243`). |
| State integrity and recovery are decided | **PASS** | Ordered SQLite initialization, atomic plan admission, pinned inputs, release admission, checksummed write-ahead effects, KnownGood publication, and explicit rollback are total (`SPINE:582-651`, `SPINE:786-857`, `SPINE:884-1050`). |
| Security is decided at feature altitude | **PASS** | Absolute allowlisted executables, narrow environments and privilege, FD peer/executable authentication, one-time capabilities, no-symlink release paths, and pre-SQLite recovery gates are binding (`SPINE:561-580`, `SPINE:896-950`, `SPINE:1139-1243`). |
| Accessibility is decided | **PASS** | Text-primary meaning, no-animation v1, hostile-content handling, linear output, terminal ownership, and canonical UX authority remain closed (`SPINE:240-284`, `SPINE:540-559`, `SPINE:1257-1271`). |
| Structural Seed is minimal and code-owned | **PASS** | The Seed names one composition and boundary ownership shape without becoming a second requirements model (`SPINE:1297-1349`). |
| Status and finalization discipline are correct | **PASS** | Frontmatter remains `status: draft`, and no false finalization was added to the memlog (`SPINE:1-10`; `MEMLOG:125-142`). |

## First-Gate Finding Closure

| Gate | Result | Literal closure |
| --- | --- | --- |
| GATE-B01 — baseline comparison input absent | **CLOSED** | AcceptedBaselineCutV1 now embeds a complete versioned BaselineComparisonProjectionV1 containing the Evidence Window start/completeness and identity-sorted Promise, Observation, and Finding comparison rows. It is explicitly the entire FR-27 comparison input, not repository handles; the reducer performs zero post-admission baseline lookups (`SPINE:801-835`). CollectionPlan canonical bytes include the projection (`SPINE:1099-1112`), and cross-unit fixtures require immutable rows and zero later lookups (`SPINE:371-374`). |
| GATE-B02 — worker result cannot prove plan identity | **CLOSED** | CollectionPlanFingerprint is defined over every admitted plan field (`SPINE:824-827`, `SPINE:1099-1112`), included in each bounded scope request, recomputed into ScopeAssignmentFingerprint, echoed in WorkerResultV1, and byte-compared before evidence admission (`SPINE:840-851`, `SPINE:1168-1227`). Wrong-plan/same-generation and wrong-plan/same-scope fixtures are named (`SPINE:379-384`). |
| GATE-H01 — diagnostic sorting grammar incomplete | **CLOSED** | DiagnosticSubjectV1 has version/tag/length/payload bytes for every variant; DiagnosticParameterV1 uses declared-order CanonicalJsonV1 tagged values including absent, signed/unsigned integers, raw bytes, non-UTF-8 paths, lists, and objects. Encounter, duplicate occurrence, unsigned tuple order, local references, final merge, reference rewrite, rejection, and no-remap semantics are all total (`SPINE:444-490`). Property fixtures cover arbitrary valid values, duplicates, mixed producers, and post-evidence resolution (`SPINE:374-379`). |
| GATE-H02 — process-owner winner direction absent | **CLOSED** | The first item after an explicitly ascending strength/provider/unsigned-ScopeId sort wins; exact PID precedes cgroup, and equal-rule ties have one order. Suppression retains every accepted/rejected hint, completeness input, conflict, selected owner, applied rule, and diagnostic (`SPINE:514-538`). Exact-PID-versus-cgroup and multi-Provider tie fixtures are named (`SPINE:378-379`). |
| GATE-M01 — valid oversize request has no disposition | **CLOSED** | Workers receive a bounded per-scope projection rather than the complete plan (`SPINE:840-847`). The parent computes full length without truncation; an over-limit request is never sent and becomes terminal `worker-request-too-large`, while an over-limit result is never allocated or parsed and becomes terminal `worker-result-too-large`. Both remain typed scope failures under frozen obligation and strictness (`SPINE:1154-1166`). Exact-boundary, one-byte-over, and maximum-valid-assignment fixtures are mandatory (`SPINE:379-384`). |

## Direct-Process Worker-Barrier Proof

The revised contract supplies one deterministic sequence:

1. The coordinator authenticates every live AD-25 worker and includes its exact
   PID, birth, executable device, and inode with the coordinator identity in
   SelfProcessSetV1 (`SPINE:505-509`).
2. Immediately before releasing the direct-process worker to its Host read, the
   coordinator freezes that set and acquires the worker-spawn barrier
   (`SPINE:508-510`).
3. The barrier remains held through the half-open direct-process evidence cut,
   so every earlier live worker is in the frozen set and no later worker can
   appear in the report (`SPINE:509-512`). The process assignment and report
   echo that complete set; the scope-assignment fingerprint also commits to it
   (`SPINE:512-514`, `SPINE:1177-1179`, `SPINE:1204-1208`).
4. The reducer suppresses self only on exact PID/birth/device/inode membership;
   an unrelated concurrent `srvls` process sharing the binary inode is not
   suppressed (`SPINE:512-514`, `SPINE:522-535`).

This closes the worker appearance race without broad inode suppression or a
second discovery path.

## Complete Acceptance-Remediation Audit

| Requested remediation | Result | Binding evidence |
| --- | --- | --- |
| Accepted Baseline, nonterminal operation, resource history, repository revision, and prior current frozen in CollectionPlanV1 | **PASS** | All cuts and revisions are created by one admission read and persisted in the complete plan (`SPINE:792-835`). |
| Paired boot and UTC wall cut | **PASS** | One ClockSampleV1 pairs boot nanoseconds, UTC wall nanoseconds, and BootIdentity; its wall sample alone stamps Snapshot, Evidence Window end, samples, and Brief (`SPINE:794-796`, `SPINE:851-854`). |
| One atomic plan admission | **PASS** | One repository operation under `BEGIN IMMEDIATE` allocates generation, captures all cuts, inserts canonical plan and pins, and moves latest-requested, or commits none (`SPINE:792-833`). |
| Reserved and authenticated internal worker routing | **PASS** | Raw argv reserves `__srvls-worker-v1` before clap or side effects; FD3 Unix peer UID/PID and executable device/inode checks plus one-time capability authenticate the same binary (`SPINE:245-249`, `SPINE:1139-1152`). |
| Versioned framing, request/result, stdio, exit, timeout, signal, mismatch, and no-discovery behavior | **PASS** | AD-25 fixes all frame, schema, identity, stdio, exit, deadline, cancellation, signal, and discovery rules (`SPINE:1154-1243`). |
| Byte-complete PolicySnapshot JSON and ScopeIdV1 grammar | **PASS** | CanonicalJsonV1 fixes encoding and schema rules; PolicySnapshotV1 fixes full typed field inclusion/order and fingerprints; ScopeIdV1 fixes tags, fields, path/string normalization, display, manifest order, and hash preimage (`SPINE:1052-1137`). |
| Post-evidence diagnostics | **PASS** | Candidates exist only after evidence and final IDs are assigned after the cutoff with atomic reference rewrite (`SPINE:444-490`). |
| Deterministic process ownership, suppression, conflict, self suppression, and retained diagnostics | **PASS** | Exact hint evidence, total winner order, self set, conflict behavior, retained rejected evidence, and incomplete-evidence behavior are explicit (`SPINE:505-538`). |
| Crash-persistent release admission before SQLite | **PASS** | Every stateful entry holds shared admission and refuses before SQLite unless ready and terminal; only release may recover under exclusive ownership (`SPINE:896-910`). |
| Checksummed atomic UpgradeTransaction replacement and write-ahead/write-after effects | **PASS** | Every manifest replacement is checksummed, O_EXCL/no-follow, file-fsynced, renamed, and directory-fsynced; every forward and rollback effect has durable pending before effect and complete only after readback (`SPINE:939-971`). |
| Exactly one KnownGoodReleaseV1 and rollback as a new transaction | **PASS** | Publication follows durable commit decision, retains exactly one pinned prior pair, and explicit rollback runs the complete protocol as a new UpgradeTransactionV1 (`SPINE:985-1015`). |
| Durable phase-to-public-event and crash-result mapping | **PASS** | Every internal step maps to one public phase/UX label, event durability controls projection, recovery emits resumed plus the eventual result, and final result has four exhaustive values (`SPINE:1017-1050`). |
| Ordered SQLite WAL/FULL/foreign-key readbacks on fresh and existing databases | **PASS** | Initialization requires `wal`, numeric `2`, and `1` in order before any transaction on every connection (`SPINE:588-600`); fresh/existing fixtures are named (`SPINE:384-390`). |
| Exact-artifact ABI gate and oldest-runtime smoke | **PASS** | `readelf --version-info` fails imported versions above `GLIBC_2.42`, then smokes the same artifact in the oldest supported 2.42 runtime (`SPINE:399-414`). |
| Every managed absolute ExecStart and paired timer validation with whole-pair rollback | **PASS** | Both named services and every managed absolute consumer are rewritten; loaded paths, timer advancement, Result, and ExecMainStatus are read back, and any failure restores and proves the complete pair (`SPINE:417-428`, `SPINE:973-983`). |
| UJ-5 and related traces | **PASS** | UJ-5 lands in exact duplicate evidence plus retained timestamped history owners; FR/SM/UX collection traces include AD-25 where the worker boundary applies (`SPINE:1367-1407`). |
| Named property, concurrency, crash, IPC, timer, and rollback fixtures | **PASS** | AD-11 enumerates baseline/history races, diagnostic/process properties, frame boundaries and mismatches, fresh/existing storage, every release crash edge, consumer/timer proof, whole-pair rollback, and explicit KnownGood rollback (`SPINE:357-397`). |

## Preserved Contracts and Discipline

- AD-1 through AD-24 retain their original numbers; the new worker boundary is
  AD-25. There is exactly one definition of every AD-1 through AD-25 and no
  undefined AD reference.
- ARCH-LIM-1 through ARCH-LIM-23 remain contiguous, unique, referenced, and
  arithmetically unchanged (`SPINE:741-784`).
- The one-binary hexagonal core and Elm-style TUI shell remain the accepted
  paradigm (`SPINE:46-71`).
- Brownfield table, flat JSON, Prometheus, Markdown, inspection, action, raw
  routing, and deployed-consumer contracts remain separate from canonical
  Promise/Brief surfaces (`SPINE:240-310`).
- The Structural Seed remains implementation-shaped and minimal; it adds only
  the contract and worker/release ownership modules demanded by the decisions
  (`SPINE:1297-1349`).
- Seed and Deferred do not move an MVP invariant out of the ADs. Deferred keeps
  grouping overrides, themes, plugins, grouped legacy output, broader
  portability, multi-resource actions, interactive TUI elevation, remote and
  multi-user operation, and external content fetching behind explicit future
  triggers (`SPINE:1409-1429`).
- Prior acceptance reports, product code, memlog, and `tasks.md` were not edited
  by this review. This file is a new independent rerun report and leaves the
  historical first-gate verdict intact.

## Validation Record

| Validation | Command or method | Result |
| --- | --- | --- |
| Frozen identity | `sha256sum .../ARCHITECTURE-SPINE.md` | **PASS** — exact required SHA-256 `818bea5f...862` before review and before report creation. |
| Base and spine patch | `git rev-parse HEAD`; spine-only stable patch ID | **PASS** — base `d4515067...`; patch `d881e20c...`. |
| Complete revised-spine read | Line-bounded reads through EOF | **PASS** — 1,429/1,429 lines from the frozen artifact. |
| Canonical source control | Exact source hashes plus targeted semantic rereads after prior complete reads | **PASS** — PRD, addendum, DESIGN, and EXPERIENCE are unchanged. |
| Acceptance and first-gate closure | Complete immutable reports plus literal current-rule comparison | **PASS** — every requested finding is closed above. |
| Current diff requested-term inspection | Spine-only diff sweep for every requested collection, IPC, diagnostic, release, SQLite, ABI, consumer, fixture, and UJ-5 term | **PASS** — every term lands in an owning Rule or trace. |
| Architecture linter | `uv run .agents/skills/bmad-architecture/scripts/lint_spine.py --workspace _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14` | **PASS** — `ok: true`; zero findings. |
| AD integrity | Definition and reference inventory | **PASS** — AD-1 through AD-25 exactly once; no out-of-range reference. |
| ARCH-LIM integrity | Definition and reference inventory | **PASS** — ARCH-LIM-1 through ARCH-LIM-23 exactly once; no out-of-range reference. |
| Draft status | Frontmatter inspection | **PASS** — `status: draft`. |
| Whitespace/error check | `git diff --check` before report creation | **PASS** — no output. |

## Final Gate

There is no blocker, high, or moderate finding. The frozen revised spine is
approved as the architecture build substrate. This review does not mark the
spine final; finalization remains with the parent BMAD workflow.
