---
title: "srvls Architecture Clean Pass 3 Good-Spine Acceptance"
type: architecture-review
status: final
created: 2026-07-16
updated: 2026-07-17
reviewer: Bartholomew the Builder
review_mode: independent-good-spine-clean-pass3
reviewed_commit: db70e84c74a301d6e698cddf0c88fb47e78da851
reviewed_spine_sha256: 5907c2f7da67378c6da60de0ed6374b9393d30b7945d271e6e261467ebce9392
reviewed_spine_line_count: 2359
reviewed_memlog_sha256: ea143f28e2bb88b54835ecb2313c950812e02d8d45835cc86124e511226d915c
reviewed_memlog_line_count: 146
verdict: changes-required
finding_count: 1
blocking_findings: 1
high_findings: 0
moderate_findings: 0
low_findings: 0
---

<!-- markdownlint-disable MD025 -->

# Architecture Review: Clean Pass 3 Good-Spine Acceptance

## Verdict

**CHANGES REQUIRED. Finding count: 1 blocker.**

The zero-finding acceptance gate is not met at exact frozen commit
`db70e84c74a301d6e698cddf0c88fb47e78da851`.

Seven of the eight clean-pass2 corrections replay successfully. The correction
for `CLEAN2-B02` does not: AD-10 requires an already-expired reservation to be
terminalized before its request ID is allocated, while AD-25 requires the
resulting no-child `worker-timeout` diagnostic to contain `request_id` as a
non-optional tagged UUID. No conforming diagnostic can be constructed. The
same contradiction makes the binding admission-latency fixture impossible.

This is one root finding, `CP3-B01`. Its effects appear in several journey,
functional, non-functional, and UX acceptance rows below; those projections do
not increase the finding count.

Prior reports were attack inventories only. Their verdicts and claimed
closures were not accepted as proof.

## Frozen Target and Evidence Boundary

| Property | Frozen value |
| --- | --- |
| Branch | `feature-bartholomew-architecture-clean-pass3` |
| Reviewed commit | `db70e84c74a301d6e698cddf0c88fb47e78da851` |
| Reviewed parent | `74244150be23d5d297f4baa824d647df5bdeac5a` |
| Parent subject | `docs(architecture): close clean pass two findings` |
| Source remediation recorded by `tasks.md` | `96fc2c5` |
| Commit subject | `chore(tasks): complete clean architecture remediation` |
| Spine | `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md` |
| Spine evidence | 2,359 lines; SHA-256 `5907c2f7da67378c6da60de0ed6374b9393d30b7945d271e6e261467ebce9392` |
| Architecture memlog | 146 lines; SHA-256 `ea143f28e2bb88b54835ecb2313c950812e02d8d45835cc86124e511226d915c` |
| Worktree before review | Clean; `HEAD` exactly equaled the requested base |

The complete review basis was read through EOF:

- `AGENTS.md`, lowercase `tasks.md`, the complete local
  `bmad-architecture/SKILL.md`, and its complete `headless.md` and
  `reviewer-gate.md` references;
- the architecture spine and its complete append-only memlog;
- canonical `prd.md`, `addendum.md`, `DESIGN.md`, and `EXPERIENCE.md`;
- the complete Python `srvls` executable, `README.md`,
  `docs/architecture.md`, and `tests/test_smoke.sh` brownfield sources;
- all eleven historical good-spine rubric reports from the initial rubric
  through `review-rubric-clean-pass2-2026-07-16.md`; and
- the clean-pass2 technology and two-unit reports that originated the eight
  corrections replayed below.

No clean-pass3 peer report was opened or used. The architecture-skill
customization resolver found no `project-context.md`. Canonical precedence
remained PRD, addendum, DESIGN, EXPERIENCE, and then the current spine. The
legacy `epics.md` was not treated as a canonical source or accepted by this
architecture review; story implementability below means that independently
assigned future stories can implement the canonical spine without inventing
incompatible contracts.

### Canonical source fingerprints

| Source | Lines | SHA-256 |
| --- | ---: | --- |
| `prd.md` | 823 | `576186a6068c4a7c7cc087b16530b76269e62ab898a7b2c61db65e389ccdb6d7` |
| `addendum.md` | 63 | `1848ab1351fe8e26edf127da34b0cda4dd3f63d4a17af03f96619f5d8671ae9d` |
| `DESIGN.md` | 329 | `e68b22d5fd232f50e580a9fd87b182b6f30938a1c5c789aa0045ed85f531d84c` |
| `EXPERIENCE.md` | 813 | `815b95de39607ce391dccd6fbaadbc37fcf8b7f73d4bfea1caeaaf910b610626` |

## Clean-Pass2 Correction Replay

| Correction | Independent replay | Result |
| --- | --- | --- |
| `TECH-CLEAN2-01` — admission lock survives owner death through children | The lease path is opened atomically with no-follow and `O_CLOEXEC`, `F_GETFD` must confirm `FD_CLOEXEC`, and every child closes the admission descriptor as its first file action before fallible setup. Fixtures keep exec'd children alive, terminate the owner, and require a new exclusive contender to acquire immediately (`SPINE:1242-1274,604-611`). | **PASS** |
| `CLEAN2-B01` — policy, manifest, and plan are not byte-total | AD-24 fixes complete PolicySnapshotV1 leaves, obligation-bearing binary ScopeManifestV1, exact CollectionPlanV1 top-level and nested schemas, row ordering, tagged absence, fingerprint preimages, and independent checked-in goldens (`SPINE:1626-1840,526-546`). | **PASS** |
| `CLEAN2-B02` — already-expired reservation can spawn or fail to terminate deterministically | AD-10 now forbids capability, socket, spawn, root, and reap state and orders expired reservations before live spawn. However, its request ID is allocated only after the strict-before check, while AD-25 requires an ID in the synthesized timeout diagnostic (`SPINE:354-376,2004-2035`). | **FAIL — `CP3-B01`** |
| `CLEAN2-B03` — Provider ObservationId schemas are incomplete | ObservationIdV1 fixes envelope version, Provider tag, field count, field tags, lengths, widths, normalization, hash domains/preimages, display, fingerprint, and five independent binary goldens (`SPINE:757-777,548-560`). | **PASS** |
| `CLEAN2-B04` — first-install KnownGood rollback is undefined | FirstInstallAbsentV1 is byte-total; automatic pre-decision recovery restores exact absence, while explicit rollback from the published sentinel returns stable `rollback-unavailable/no-prior-release` with no mutation (`SPINE:1492-1546,631-636`). | **PASS** |
| `CLEAN2-H01` — injected FD3 duplicates can become accepted | Every injected parent-end or child-end duplicate freezes `fd-peer-auth`, accepts no Hello/Ready/Request/Result, closes all owned copies, and proves failure-path EOF. Only the descriptor-clean control reaches Result and clean EOF (`SPINE:575-584,1874-1889`). | **PASS** |
| `CLEAN2-H02` — timer acceptance proves ordering, not causality | TimerCausalityProofV1 captures the Job ActivationDetails before JobRemoved and requires exact `trigger_unit=<timer>`, job unit/type/result, fresh invocation, and no manual or intervening activation. systemd 257 primary interface documentation confirms a present pair is a valid trigger and also confirms its best-effort limitation; absence therefore fails closed (`SPINE:1440-1472`). | **PASS** |
| `CLEAN2-H03` — release validation has no frozen deadline derivation | ARCH-LIM-24 is unique and contiguous. ReleaseValidationAttemptV1 persists owner, attempt, one CLOCK_BOOTTIME start, timeout, checked absolute cut, and requires timer, job, service, and FD4 evidence strictly before it. Recovery retains the old attempt and persists a new owner-bound cut (`SPINE:1093,1112-1115,1297-1314,625-628`). | **PASS** |

## DispatchScheduleV1 Adversarial Replay

An independent compiler implemented the normative AD-10 algorithm using
nanosecond integers: descending budget then unsigned ScopeId order, numbered
workers, frozen availability, process-gate reservation, checked makespan, and
`max(configured margin, 1 ns)`.

| Fixture | Replayed result | Result |
| --- | --- | --- |
| Default `[30,20,15,15,10,10,10,process=10]` | Epochs `0/15/20/25 s`; process gate `[25,35)`; makespan `35 s`; cutoff `40 s` | **PASS** |
| Near tie `[20,20,20,20,process=10,9,9,9]` | Epochs `0/20 s`; process gate `[20,30)`; makespan `30 s`; cutoff `35 s`; completion at `20 s - 1 ns` cannot advance process | **PASS** |
| Process-first `[process=60,1,1,1,1,1,1,1]`, margin zero | Epochs `0/60 s`; process gate `[0,60)`; makespan `61 s`; effective margin `1 ns`; cutoff `61 s + 1 ns` | **PASS** |

The fixed schedule itself is deterministic and internally consistent. The
finding occurs only when runtime begins processing a reservation at or after
its frozen cut and must materialize the required no-child diagnostic.

## Canonical Journey Trace

| Journey | Architecture landing | Result |
| --- | --- | --- |
| UJ-1 | AD-5/AD-7/AD-18/AD-20/AD-21/AD-24/AD-25 own scoped collection, partial truth, Brief, Evidence Window, and presentation. An admission-late required scope cannot produce its mandatory diagnostic. | **FAIL — `CP3-B01`** |
| UJ-2 | AD-13/AD-16/AD-17/AD-19/AD-20/AD-21/AD-24 own exact Promise identity, lifecycle events, leases, heartbeats, and deterministic Agent contracts. | **PASS** |
| UJ-3 | AD-5/AD-6/AD-13/AD-18/AD-20/AD-21/AD-22 own linked diagnosis, inspection, and Promise-origin Start. | **PASS** |
| UJ-4 | AD-6/AD-13 through AD-16/AD-18/AD-20 through AD-22/AD-24 own exact-target planning, revalidation, launch, and one terminal outcome. | **PASS** |
| UJ-5 | AD-4/AD-5/AD-16/AD-18/AD-20/AD-21/AD-25 own Stack inference, retained samples, multi-label findings, and exact action scope. | **PASS** |
| UJ-6 | AD-3/AD-7/AD-9/AD-11/AD-12/AD-16/AD-23/AD-24 own staged release, consumer validation, KnownGood recovery, and rollback. | **PASS** |

## Canonical Functional-Requirement Trace

All 43 canonical FR definitions were extracted exactly once. Range expansion
over the capability and trace tables covers FR-1 through FR-43 with no missing
or extra identifier.

| Requirement | Architecture landing | Result |
| --- | --- | --- |
| FR-1 | RuntimePromise aggregate, application lifecycle service, UUIDv7 ID, and transactional projection in AD-1/AD-2/AD-13/AD-16/AD-17. | **PASS** |
| FR-2 | Append-only lifecycle events, declaration provenance, revisions, and exact folds in AD-2/AD-16/AD-17/AD-24. | **PASS** |
| FR-3 | Finite Lease is the default omitted-intent behavior in AD-17/AD-20. | **PASS** |
| FR-4 | Heartbeat renewal, idempotency, boot-aware time, and actor ownership are fixed in AD-13/AD-16/AD-17. | **PASS** |
| FR-5 | Release, completion, and revocation are typed lifecycle events with immutable closure reason in AD-16/AD-17. | **PASS** |
| FR-6 | Persistent intent requires durable ownership plus an inspectable Launch Mechanism in AD-6/AD-17/AD-19. | **PASS** |
| FR-7 | Versioned Agent commands and deterministic machine envelopes are fixed by AD-7/AD-9/AD-17/AD-24. | **PASS** |
| FR-8 | Cron scopes, obligations, typed inputs, privilege, reports, and compatibility fixtures are owned by AD-3/AD-5/AD-9 through AD-11/AD-15/AD-24/AD-25. | **PASS** |
| FR-9 | Separate system and user systemd scopes use the same bounded authenticated report contract. | **PASS** |
| FR-10 | Docker endpoint/context scope and immutable container identity are exact and bounded. | **PASS** |
| FR-11 | PM2_HOME, process ID, birth evidence, and executable/name fingerprint are exact and bounded. | **PASS** |
| FR-12 | Direct Host process identity, self roots, exact suppression, and weak-evidence emission are fixed by AD-5/AD-10/AD-13/AD-18/AD-25. | **PASS** |
| FR-13 | One Provider-neutral Observation aggregate retains typed Provider facets and exact identity. | **PASS** |
| FR-14 | Obligation and outcome ownership is explicit, but the required no-child timeout diagnostic is unconstructible for an already-expired reservation. | **FAIL — `CP3-B01`** |
| FR-15 | Bounded Provider detail, sanitizer ownership, byte/line caps, and truncation disclosure are fixed. | **PASS** |
| FR-16 | Frozen Python corpus, output compatibility, smoke coverage, consumer checks, and compatibility ledger are binding. | **PASS** |
| FR-17 | Strict policy is defined, but an already-expired required scope cannot yield the exact report/diagnostic input from which strict exit is selected. | **FAIL — `CP3-B01`** |
| FR-18 | Pure deterministic correlation retains anchors, evidence weights, conflicts, ties, and stable assignment. | **PASS** |
| FR-19 | Healthy intent requires sufficient, non-conflicting evidence under the canonical axis order. | **PASS** |
| FR-20 | Broken intent uses only the frozen eligible scope reports and preserves unresolved absence. | **PASS** |
| FR-21 | Unmatched exact Observations remain separate, retained, and explainable. | **PASS** |
| FR-22 | Strict-max Promise assignment and intended-instance duplicate classification are deterministic. | **PASS** |
| FR-23 | Stale requires positive architecture-owned evidence and a visible policy source. | **PASS** |
| FR-24 | Hot uses timestamped retained samples and refuses insufficient sample history. | **PASS** |
| FR-25 | Unmanaged and abandoned labels remain compatible, explicit, and non-mutating. | **PASS** |
| FR-26 | Findings retain supporting, contradicting, and missing evidence plus Safe-to-stop truth. | **PASS** |
| FR-27 | Baseline acceptance, compatibility, immutable pins, bounded comparison, and no post-admission reads are fixed. | **PASS** |
| FR-28 | Brief materialization names all eight morning answers, completeness, baseline, window, timezone, and drill-down IDs. | **PASS** |
| FR-29 | Evidence tiers, deterministic residual claiming, StackGroupId, collision handling, and Ungrouped are fixed. | **PASS** |
| FR-30 | TTY/TERM routing, raw profiles, format precedence, fzf compatibility, and linear fallback are explicit. | **PASS** |
| FR-31 | EXPERIENCE owns keys, focus, search, facets, refresh, and responsive behavior; Elm Update owns model state. | **PASS** |
| FR-32 | Promise and Observation identities remain separate while evidence links them in bounded detail. | **PASS** |
| FR-33 | Text carries all meaning; color/Unicode are optional and hostile controls are sanitized. | **PASS** |
| FR-34 | Loading, stale, partial, empty, operation, replacement, and terminal states have one model owner. | **PASS** |
| FR-35 | The Action Menu resolves only exact supported capabilities, including Promise-origin Start. | **PASS** |
| FR-36 | Immutable plans contain exact identity, typed argv, capability, risk, and cron/direct-process restrictions. | **PASS** |
| FR-37 | Generation, identity, policy, boot, and lifetime are revalidated immediately before mutation. | **PASS** |
| FR-38 | Required confirmation, disabled unsafe actions, and stronger unknown acknowledgement are binding. | **PASS** |
| FR-39 | PlanId/OperationId, nonterminal target uniqueness, separate action pool, and verification generation isolate operations. | **PASS** |
| FR-40 | OperationCoordinator owns launch receipts, fresh verification, outcome precedence, and terminal CAS. | **PASS** |
| FR-41 | Groups are read-only and privilege remains exact Provider/principal scoped. | **PASS** |
| FR-42 | Locked artifact, checksum, isolated smoke, ABI proof, staged activation, and release transaction are fixed. | **PASS** |
| FR-43 | Binary, SQLite, consumers, enablement, daemon state, KnownGood, rollback, and crash recovery form one transaction. | **PASS** |

## Canonical Non-Functional-Requirement Trace

All 16 NFR definitions were extracted exactly once and the architecture trace
expands across NFR-1 through NFR-16 without a cardinality gap.

| Requirement | Architecture landing | Result |
| --- | --- | --- |
| NFR-1 | Most domain outcomes are canonical, but the already-expired no-child outcome has no complete legal diagnostic value. | **FAIL — `CP3-B01`** |
| NFR-2 | Scoped obligations, explicit non-complete results, stale-last-good truth, and withheld absence remain honest. | **PASS** |
| NFR-3 | Schedule, deadlines, capture, cancellation, and reaping are bounded, but the required pre-spawn expiry terminalization is not implementable as encoded. | **FAIL — `CP3-B01`** |
| NFR-4 | Typed argv-only execution, safe option handling, executable/environment/cwd policy, and no shell construction are fixed. | **PASS** |
| NFR-5 | No whole-process elevation; non-interactive and Provider-scoped privilege are explicit. | **PASS** |
| NFR-6 | One TerminalSession and phase-specific signal/shutdown owner restore terminal state. | **PASS** |
| NFR-7 | Routing and presenter ownership keep machine stdout deterministic and terminal-control free. | **PASS** |
| NFR-8 | Text, ASCII, no-color, keyboard, linear, hostile-text, responsive, and restoration contracts are retained. | **PASS** |
| NFR-9 | SQLite pragmas, immediate transactions, CAS, manifest fsync ordering, and fail-closed migration are fixed. | **PASS** |
| NFR-10 | CLOCK_BOOTTIME, boot identity, UTC provenance, and no wall-clock extension are defensible. | **PASS** |
| NFR-11 | Local permissions, retention, redaction, bounded capture, and capacity refusal minimize data. | **PASS** |
| NFR-12 | Generation, operation, release, and worker concurrency rules are otherwise exact; the expiry/diagnostic contract gives two units incompatible required states. | **FAIL — `CP3-B01`** |
| NFR-13 | Fake ports, property suites, goldens, virtual clocks, and crash/IPC fixtures are extensive, but the binding expired-reservation fixture is unsatisfiable. | **FAIL — `CP3-B01`** |
| NFR-14 | The Python compatibility corpus, live smoke, and named consumer assertions remain authoritative. | **PASS** |
| NFR-15 | Target, lock graph, MSRV/stable lanes, checksum, ABI gate, reversible installation, and runtime smoke are bound. | **PASS** |
| NFR-16 | Typed precedence, provenance, complete PolicySnapshotV1, limits, validation, and no hidden defaults are fixed. | **PASS** |

## Canonical UX Trace

The canonical experience inventory contains exactly 89 unique IDs. Mechanical
range expansion over the architecture trace covers exactly those same 89 IDs,
with no omission or extra identifier. The 16 DESIGN component names equal the
16 EXPERIENCE component bindings in the same order.

| Family | Expected / found / traced | Semantic acceptance |
| --- | ---: | --- |
| UX-FND-1 through UX-FND-6 | 6 / 6 / 6 | **FAIL only UX-FND-4** — the expired-scope failure cannot become a complete partial-truth diagnostic (`CP3-B01`) |
| UX-IA-1 through UX-IA-12 | 12 / 12 / 12 | **PASS** |
| UX-VT-1 through UX-VT-4 | 4 / 4 / 4 | **PASS** |
| UX-CP-1 through UX-CP-16 | 16 / 16 / 16 | **FAIL only UX-CP-2** — completeness-banner requires each scope's diagnostic (`CP3-B01`) |
| UX-ST-1 through UX-ST-20 | 20 / 20 / 20 | **FAIL only UX-ST-4 and UX-ST-5** — incomplete/unavailable scope rendering requires the missing diagnostic (`CP3-B01`) |
| UX-IP-1 through UX-IP-12 | 12 / 12 / 12 | **PASS** |
| UX-A11Y-1 through UX-A11Y-5 | 5 / 5 / 5 | **PASS** |
| SR-A11Y-1 | 1 / 1 / 1 | **PASS** |
| UX-RP-1 through UX-RP-6 | 6 / 6 / 6 | **PASS** |
| UX-BUD-1 through UX-BUD-7 | 7 / 7 / 7 | **PASS** |

All visual, interaction, responsive, accessibility, and budget contracts retain
their higher-source ownership. Architecture supplies the state and operational
substrate without replacing UX decisions. The semantic failures above are all
projections of the one invalid collection diagnostic, not UX omissions.

## Decision, Limit, and Structural Integrity

| Check | Result |
| --- | --- |
| AD definitions | **PASS** — AD-1 through AD-25 appear exactly once, contiguous and ordered |
| AD references | **PASS** — no undefined AD reference |
| Decision completeness | **PASS** — every AD contains Binds, Prevents, and Rule |
| Operational limits | **PASS** — ARCH-LIM-1 through ARCH-LIM-24 appear exactly once, contiguous and ordered; no undefined limit reference |
| Structural Seed | **PASS** — 44 expanded concrete files, 44 unique; zero duplicate file path |
| FD ownership | **PASS** — `adapters/worker.rs` solely owns FD3 transport and `adapters/release.rs` solely owns release/FD4 transport |
| Deferred discipline | **PASS** — nine items retain a closed v1 choice and a later requirement or safety trigger |
| Placeholders | **PASS** — no TODO, TBD, or FIXME marker in the spine |
| Stale normative claims | **PASS** — superseded memlog claims are not present as current spine rules |

## Good-Spine Rubric

| Rubric dimension | Result | Assessment |
| --- | --- | --- |
| Real lower-level divergence points | **FAIL** | Collection admission and worker-diagnostic implementation disagree on whether an expired reservation has a request ID. |
| Enforceable Rules | **FAIL** | AD-10 and AD-25 are individually precise but cannot both be enforced for the no-child timeout row. |
| Decision completeness | **PASS** | All 25 decisions have ownership, prevented divergence, and normative rules; every other tested boundary selects one result. |
| Internal consistency | **FAIL** | `CP3-B01` is a direct cross-section contradiction. |
| Story implementability | **FAIL** | An admission/catch-up story following AD-10 and a diagnostic/IPC story following AD-25 cannot integrate without inventing an unapproved absent ID, placeholder ID, or earlier allocation rule. |
| Testability | **FAIL** | AD-11 requires byte-identical no-child timeout diagnostics, but their required request-ID value has no source. |
| Deferred discipline | **PASS** | No current implementation choice needed for v1 is deferred. |
| Named technology currency and fit | **PASS** | Rust and crate targets, ratatui MSRV, SQLite bundle, Linux/glibc target, and systemd causal premise were independently verified. |
| Brownfield ratification | **PASS** | Existing CLI behavior, compatibility corpus, smoke suite, and deployed-consumer constraints remain authorities. |
| PRD/addendum coverage | **FAIL only through `CP3-B01`** | All IDs and owners exist; FR-14/FR-17 and NFR-1/NFR-3/NFR-12/NFR-13 cannot be fully realized on the expired-reservation path. |
| UX coverage | **FAIL only through `CP3-B01`** | All 89 IDs and 16 components trace; four partial-truth/completeness IDs lack realizable input on the affected path. |
| Operational/environmental envelope | **PASS** | Host, clocks, identity, privilege, state, release, ABI, consumers, recovery, and CI are closed. |
| Structural Seed | **PASS** | Concrete ownership is unique after brace expansion. |
| Parent-spine compatibility | **N/A** | No inherited parent architecture spine is declared for this feature workspace. |

## Independent Two-Unit and Contradiction Audit

| Seam | Result |
| --- | --- |
| Domain versus adapters/presentation | **PASS** — AD-1 and the boundary test select one inward dependency graph. |
| Promise versus Observation truth | **PASS** — aggregates, events, projection, reconciliation, and historical rendering remain orthogonal. |
| Configuration versus admission versus runtime | **PASS** — canonical policy, manifest, schedule, plan, fingerprints, cuts, and byte comparisons are complete. |
| Admission/catch-up versus diagnostic encoder | **FAIL — `CP3-B01`** — no request ID exists at the required no-child terminal cut, but the encoder requires one. |
| Live worker versus coordinator | **PASS** — FD ownership, credentials, framing, identity, deadlines, cause precedence, EOF, and reap evidence agree after a live reservation passes the strict-before check. |
| Provider process versus direct-process reducer | **PASS** — exact roots and absence proofs select one suppression result and preserve weak/conflicting evidence. |
| Action adapter versus verifier/TUI | **PASS** — plan, receipt, operation phase, fresh evidence, outcome precedence, and terminal CAS have one owner. |
| Configuration versus historical state | **PASS** — complete canonical policy bytes govern behavior while provenance and prior materialized findings remain inspectable. |
| SQLite versus release coordinator | **PASS** — admission, manifest, migration, validation, KnownGood, consumer/timer state, rollback, and terminal result fail closed. |
| UX versus architecture | **PASS apart from the missing diagnostic input** — UX retains behavioral ownership and architecture otherwise supplies one exact state source. |

## Technology and Brownfield Replay

- The official stable-channel manifest fetched during this review is dated
  2026-07-16 and identifies Rust 1.97.1 with full commit
  `8bab26f4f68e0e26f0bb7960be334d5b520ea452`. The local symbolic stable toolchain
  remained stale at 1.97.0, which AD-12 correctly requires bootstrap/release CI
  to reject before compilation.
- Official crates.io metadata confirmed every Stack-table lock target exists and
  is non-yanked. Ratatui 0.30.2 declares Rust 1.88.0 and uses the Crossterm 0.29
  line. The `libsqlite3-sys` 0.37.0 bundled header reports SQLite 3.51.3.
- The systemd v257 primary D-Bus interface source confirms Job
  `ActivationDetails`, `trigger_unit`, valid-trigger semantics, and best-effort
  presence exactly as AD-23 depends on.
- The live host reports systemd 257, x86_64 Linux 6.17, glibc 2.42, 32 logical
  CPUs on an AMD Ryzen 9 9950X, and approximately 128 GiB RAM, matching the
  architecture's target and reference-host claims.
- The complete brownfield smoke suite passed against 293 live inventory items:
  JSON schema, Prometheus families, Markdown, table, cron inspection, and
  hostile-name non-injection all passed.

Primary network evidence was the official Rust stable manifest and
[Rust 1.97.1 announcement](https://blog.rust-lang.org/2026/07/16/Rust-1.97.1/),
official crates.io registry metadata/source archives, and the official systemd
v257 `org.freedesktop.systemd1` interface source.

## Mechanical Validation

| Check | Result |
| --- | --- |
| Exact base | **PASS** — pre-edit `HEAD` equaled full `db70e84c74a301d6e698cddf0c88fb47e78da851` |
| BMAD architecture lint | **PASS** — `ok: true`, zero linter findings |
| Canonical PRD inventory | **PASS** — UJ `6/6`, FR `43/43`, NFR `16/16`; no missing or extra ID |
| Canonical UX inventory | **PASS mechanically** — `89/89` source IDs and `89/89` architecture trace IDs |
| UX component parity | **PASS** — 16 DESIGN names equal 16 EXPERIENCE bindings in order |
| AD integrity | **PASS** — `25/25`, contiguous, no undefined reference, complete decision sections |
| Limit integrity | **PASS** — `24/24`, contiguous, no undefined reference |
| Structural Seed uniqueness | **PASS** — 44 expanded concrete files, zero duplicate |
| Schedule replay | **PASS** — default `35/40 s`, near-tie `30/35 s`, process-first `61 s + 1 ns` |
| Eight-correction replay | **FAIL** — seven pass; `CLEAN2-B02` fails as `CP3-B01` |
| Official technology evidence | **PASS** — exact Rust identity, exact non-yanked crate targets, SQLite 3.51.3, systemd 257 causality semantics |
| Brownfield live smoke | **PASS** — all smoke assertions passed |
| Canonical Markdown lint | **PASS** — `markdownlint-cli2` with the canonical UX configuration reports zero errors |
| Whitespace validation | **PASS** — `git diff --check` reports no errors |
| Changed-file scope | **PASS** — this report is the only changed path and will be the only committed path |

## Finding

### CP3-B01 — Already-expired reservations cannot construct their required diagnostic

- **Severity:** Blocker
- **Correction replay:** `CLEAN2-B02` remains open
- **Affected contracts:** UJ-1; FR-14, FR-17; NFR-1, NFR-3, NFR-12,
  NFR-13; UX-FND-4, UX-CP-2, UX-ST-4, UX-ST-5

AD-10 defines this exact sequence:

1. Before capability allocation, socket creation, or spawn, sample
   `CLOCK_BOOTTIME` and compare the reservation's scope and generation cuts.
2. At equality or after either cut, create no capability, socket, OwnedSpawn,
   child, or process-group state and synthesize the no-child `worker-timeout`
   (`SPINE:354-360`).
3. Allocate the member's request ID and capability only **after** the mandatory
   strict-before check (`SPINE:376-382`).

AD-25 then requires every report to own exactly one byte-complete
WorkerTransportDiagnosticV1 whose exact parameter object includes
`request_id` as tagged `id`, not `absent | id` (`SPINE:2004-2015`). Its
exhaustive matrix requires a `deadline with no child` timeout row
(`SPINE:2034`). AD-11 additionally requires equal/late admission fixtures to
produce byte-identical instances of that diagnostic (`SPINE:502-509`).

There is no alternate request-ID source in CollectionPlanV1,
DispatchScheduleV1, the reservation member schema, or any other request-ID
allocation rule. The contradiction is therefore constructive, not editorial:

- following AD-10 yields no RequestId value at the terminal cut;
- inventing a UUID, sentinel, or placeholder violates the only allocation rule
  and the exact diagnostic schema;
- omitting the key or tagging it absent violates AD-25; and
- allocating it before the check violates AD-10 step 2 as written.

Two independently assigned stories can neither integrate nor satisfy the
binding fixture without making a new architecture decision.

**Required closure:** choose and bind one representation. The smallest
zero-side-effect correction is to make `request_id` exactly `absent | id`,
require `absent` only for the no-child expired-reservation row, retain `id` for
every path that passed the strict-before check, and update the exhaustive
matrix/goldens. Alternatively, freeze a RequestId before the expiry check and
define its persisted/deterministic ownership. In either case, replay the
one-nanosecond-before/equal/after and multi-missed-epoch fixtures and prove
canonical diagnostic bytes.

## Final Status

**CHANGES REQUIRED. One blocker.** The architecture is otherwise unusually
complete and mechanically clean, but the explicit zero-finding gate forbids a
PASS while `CP3-B01` remains.
