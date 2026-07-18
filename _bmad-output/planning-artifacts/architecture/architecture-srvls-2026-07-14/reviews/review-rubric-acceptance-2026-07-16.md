---
name: "srvls Architecture Spine Final Good-Spine Acceptance Review"
status: final
reviewer: "Bartholomew the Builder"
review_date: 2026-07-16
reviewed_commit: b917bcc89b5e386789cd0d0e8dfd01ce0cd42d0f
reviewed_artifact: "_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md"
verdict: "CHANGES REQUIRED"
blocking: true
finding_count: 3
blocking_findings: 2
major_findings: 1
---

# srvls Architecture Spine Final Good-Spine Acceptance Review

## Verdict

**CHANGES REQUIRED. Blocking status: BLOCKED for downstream Provider,
reconciliation, Brief, or Snapshot implementation stories.**

Commit `b917bcc89b5e386789cd0d0e8dfd01ce0cd42d0f` materially closes every
previous B-1 through B-7, M-1 through M-6, and L-1 through L-3 finding. The
deterministic linter is clean; all 24 AD and 23 ARCH-LIM definitions and
references are valid; every canonical identifier is mechanically traced; and
release ownership, malformed legacy arity, cron read-only behavior, dependency
CI, correlation, suspend time, PlanId, Provider trust, state accounting, and
stable identity/policy contracts are now explicit.

Acceptance still fails on two newly introduced cross-unit seams. First,
AD-18's pure reconciliation use case is limited to AD-21's frozen
`CollectionPlanV1` and current eligible reports, but AD-21 freezes neither the
Accepted Baseline nor the retained resource-sample history required by FR-24,
FR-27, and FR-28. Second, AD-10 requires a supervised invocation of the same
binary for all potentially blocking Provider work, but AD-7 defines no internal
worker profile and no AD defines the parent/worker wire contract. These are
build-substrate holes, not implementation preferences.

No source fix is made by this review.

## Review basis

### Citation key

- `SPINE` — `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md`
- `RUBRIC` — `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/reviews/review-rubric-2026-07-16.md`
- `PRD` — `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md`
- `ADD` — `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/addendum.md`
- `UX` — `_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md`
- `DESIGN` — `_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/DESIGN.md`
- `SRC` — `srvls`

### Exact artifacts reviewed

| Artifact | Lines | SHA-256 |
| --- | ---: | --- |
| `SPINE` | 947 | `36091209e1db6abf2414d974fd2ab2fc59a6a88fd475862fbd887c9ba17f1c04` |
| `RUBRIC` | 255 | `ea7e5a5fe3d89a77bb68a42607db6f7d6e5e5ad761b00af704009702c07c4651` |
| `PRD` | 823 | `576186a6068c4a7c7cc087b16530b76269e62ab898a7b2c61db65e389ccdb6d7` |
| `ADD` | 63 | `1848ab1351fe8e26edf127da34b0cda4dd3f63d4a17af03f96619f5d8671ae9d` |
| `UX` | 813 | `815b95de39607ce391dccd6fbaadbc37fcf8b7f73d4bfea1caeaaf910b610626` |
| `DESIGN` | 329 | `e68b22d5fd232f50e580a9fd87b182b6f30938a1c5c789aa0045ed85f531d84c` |

Each artifact above was read completely. The dated technology-currency and
two-unit-divergence reviews were also read completely, then their claims were
retested against the current spine rather than carried forward as conclusions.

## Good-spine rubric

| Rubric check | Result | Acceptance evidence |
| --- | --- | --- |
| Real divergence points are fixed one level down and none are missed | **FAIL — BLOCKING** | NEW-B-1 leaves the baseline/history read cut open; NEW-B-2 leaves the mandatory worker process boundary open. |
| Every AD Rule is enforceable and prevents its stated divergence | **FAIL — BLOCKING** | AD-5 requires retained history, AD-18 permits only plan plus reports, and AD-21's plan omits that history (`SPINE:168-181`, `553-582`, `659-680`). AD-10 requires a child route that AD-7 does not define (`SPINE:241-262`, `304-346`). |
| Deferred contains no decision that permits incompatible stories | **PASS** | Every deferral is post-MVP, preserves the v1 choice, and has a revisit condition (`SPINE:927-947`; `PRD:666-676`). |
| Named technology is current and reality-grounded | **PASS** | Rust 1.97.0 was the current stable release on 2026-07-16. Every queried exact crate version exists and is non-yanked; the corrected rusqlite/TOML pins and glibc build policy remain in `SPINE:369-393`, `792-815`. |
| Brownfield behavior is ratified or ledgered | **PASS** | AD-7 selects legacy verbs before bad-arity validation, matching `SRC:338-345`; AD-9 preserves the layered oracle and exact output/action corpus (`SPINE:236-302`). |
| Every canonical product and UX capability lands semantically | **FAIL — BLOCKING** | Mechanical coverage is complete, but NEW-B-1 leaves UJ-1, UJ-5, FR-24, FR-27, FR-28, SM-1, SM-2, and their baseline/hot UX projections without one frozen input contract. NFR-3 remains non-enforceable across NEW-B-2. |
| No rule weakens or contradicts another | **FAIL — BLOCKING** | The AD-5 history read and AD-18 input closure cannot both be implemented from AD-21's enumerated plan. AD-7's exhaustive pre-side-effect routing has no profile for AD-10's required same-binary worker. |
| Deployment and environment decisions are closed | **PASS** | One binary, Host ABI, install path, release namespace, staged activation, consumer ownership, state migration, and crash recovery are explicit (`SPINE:369-393`, `707-737`). |
| Provider strategy and operations are closed | **FAIL — BLOCKING** | Executable, environment, cwd, privilege, scheduling, cutoff, and typed result policy are closed; the mandatory parent/worker process route and transport are not (NEW-B-2). |
| State integrity and recovery are closed | **FAIL — BLOCKING** | SQLite, action recovery, release rollback, and capacity posture are explicit, but the baseline/history revision participating in a generated Snapshot and Brief is not frozen (NEW-B-1). |
| Security is closed at feature altitude | **PASS** | Canonical adapters use absolute allowlisted executables, `/`, a minimal environment allowlist, argv-only execution, narrow privilege, and bounded/redacted evidence (`SPINE:185-234`, `440-459`). |
| Accessibility is closed | **PASS** | Canonical UX contracts govern all text, focus, linear, responsive, hostile-content, restoration, and acceptance behavior (`SPINE:264-276`, `419-438`, `764-774`, `917-925`). |
| Operational limits are closed | **PASS WITH BLOCKING CONSUMER GAP** | ARCH-LIM-1 through ARCH-LIM-23 are complete and arithmetically consistent. NEW-B-1 concerns the frozen inputs that consume ARCH-LIM-10, not the limit definition itself. |

## Prior finding closure matrix

All prior findings are closed on their original terms. A closure does not
waive a distinct new finding created by the remediation mechanism.

| Prior ID | Disposition | Current binding evidence |
| --- | --- | --- |
| B-1 — correlation and confidence | **CLOSED** | AD-18 fixes the lexicographic vector, anchor strength, conflicts, name threshold, categorical confidence, candidate eligibility, strict maxima, ties, and retained evidence (`SPINE:547-582`). |
| B-2 — suspend time | **CLOSED** | Same-boot Lease and Heartbeat decisions use suspend-inclusive Linux `CLOCK_BOOTTIME`; suspend consumes both durations (`SPINE:526-545`, `782`). |
| B-3 — release invocation and owner | **CLOSED** | AD-7 routes `srvls release`; AD-12 makes it the sole process owner; AD-23 assigns `application::release` and `StateMigrationCoordinator` (`SPINE:258-262`, `369-393`, `707-737`). |
| B-4 — durable Plan identity | **CLOSED** | `PlanId` is UUIDv7, `ActionPlanRepository` is a port, SQLite has an ActionPlan family, and AD-22 fixes the immutable plan and consumption CAS (`SPINE:100-113`, `395-417`, `461-524`, `682-705`). |
| B-5 — legacy bad arity | **CLOSED** | AD-7 selects a legacy verb before its exact-three-argument check (`SPINE:241-246`), matching `SRC:338-345`. |
| B-6 — Provider trust | **CLOSED** | AD-15 binds absolute allowlisted executable resolution, cwd `/`, minimal per-Provider environment allowlists, and a frozen legacy-only exception (`SPINE:440-459`). |
| B-7 — dependency-boundary enforcement | **CLOSED** | AD-1 names a checked-in dependency manifest and `cargo test --locked --test architecture_boundaries` in bootstrap and every all-target lane (`SPINE:71-83`, `862-865`). |
| M-1 — cron read-only | **CLOSED** | AD-6 says cron has no canonical mutation capability and refuses it before argv construction (`SPINE:185-204`). |
| M-2 — trace ownership | **CLOSED AS WRITTEN** | Capability rows now include Snapshot, action, identity, privilege, release, and compatibility owners (`SPINE:885-925`). NEW-M-1 identifies a different UJ-5-specific omission. |
| M-3 — Stack evidence priority | **CLOSED** | Exact matched Project evidence is `400`, Provider-native `300`, source `200`, semantic `100`, with non-summing and non-transitive rules (`SPINE:115-137`). |
| M-4 — hot evidence owner | **CLOSED AS TO OWNERSHIP** | AD-5 assigns timestamped samples to immutable Snapshot history; AD-16 persists retained samples; ARCH-LIM-10 defines the query window (`SPINE:139-183`, `477-480`, `625-650`). NEW-B-1 concerns freezing that owned history into reconciliation input. |
| M-5 — Host and policy identity | **CLOSED** | AD-24 fixes stable machine-based HostIdentityV1, distinguishes BootIdentity, canonicalizes PolicySnapshotV1, and domain-separates fingerprints (`SPINE:739-762`). |
| M-6 — finalization versus D-state | **CLOSED** | AD-14 preserves the last truthful phase when storage cannot complete; ARCH-LIM-22/23 are bounded attempts and a decision budget, not universal durable-write, reap, or exit guarantees (`SPINE:419-438`, `648-657`). |
| L-1 — public identity encoding | **CLOSED** | AD-24 requires UTF-8 NFC, RFC 3986 unreserved literals, uppercase percent-hex, and rejection of malformed/noncanonical input (`SPINE:739-762`). |
| L-2 — CollectionAttempt schema | **CLOSED** | AD-16 explicitly includes `CollectionPlans and CollectionAttempts` in the versioned schema families (`SPINE:512-524`). |
| L-3 — state-byte accounting | **CLOSED** | AD-16 defines the no-symlink `st_blocks * 512` sum over database, WAL, SHM, backups, and upgrade manifests plus deterministic capacity behavior (`SPINE:493-524`; ARCH-LIM-19 at `645`). |

## Tier 1 findings — blocking

### NEW-B-1 — The frozen truth cut omits baseline and historical sample inputs

AD-5 requires hot classification to query timestamped samples in immutable
Snapshot history and makes the Accepted Baseline define the Evidence Window
(`SPINE:168-183`). AD-18 then says one pure use case consumes **only** an AD-21
frozen `CollectionPlan` and its eligible reports before producing all labels and
the Brief (`SPINE:553-582`). AD-21 enumerates the plan fields—generation start,
boot and Host identity, Promise revisions/event sequences, policy, and frozen
scope manifest—but includes no Accepted Baseline identity/revision, compatible
baseline projection, current-Snapshot revision, retained sample IDs, or bounded
sample slice (`SPINE:659-680`).

The missing values are required inputs, not optional enrichment:

- FR-24 requires metric, sample time, threshold, and source for hot findings
  (`PRD:418-425`).
- FR-27 fixes the Evidence Window from an explicitly Accepted Baseline to the
  current Snapshot and says refresh keeps its start fixed until explicit
  acceptance (`PRD:456-466`).
- FR-28 requires the Brief to name the Accepted Baseline, current Snapshot,
  timezone, and incomplete-window conditions (`PRD:472-480`).
- UX-CP-1, UX-CP-12, UX-ST-16, UX-IP-6, and the UJ-5 flow require those exact
  values and retained hot evidence (`UX:176-187`, `214-215`, `341-352`,
  `668-684`).

Two lower units can therefore choose incompatibly. One planner can freeze the
baseline pointer and bounded sample history at generation start. Another can
implement only the enumerated plan and load the current baseline/history during
reduction or Brief composition. A concurrent `b` acceptance, retained Snapshot,
or retention transaction then changes the Evidence Window or hot label for the
same GenerationId. Omitting the late read instead makes FR-24/27/28 impossible;
performing it contradicts AD-18's closed input set.

**Blocking status: YES.** Amend AD-21 with one versioned historical input cut:
the Accepted Baseline pointer and revision, compatible baseline projection,
current repository revision, and the bounded retained resource-sample set or
immutable IDs plus a pinned repository snapshot. Define baseline-acceptance and
retention behavior while a generation holds that cut. AD-18 must consume that
shape without a later repository read. Add concurrent baseline-acceptance,
retention, and three-sample hot fixtures to AD-11.

### NEW-B-2 — The mandatory same-binary worker has no route or wire contract

AD-10 requires all potentially blocking Provider file, `/proc`, and command
work to run in a supervised invocation of the same binary so the parent can cut
a scope without stranding a worker thread (`SPINE:304-346`). AD-7 requires raw
argv to choose one profile before any side effect and enumerates canonical,
canonical-inspect, legacy-action, TUI, legacy-inventory, and bare profiles; it
defines no internal worker profile (`SPINE:236-262`). AD-21 says what workers
receive and echo at the domain level, but does not define how a child is
selected or how the values cross the process boundary (`SPINE:659-680`).

The CLI unit can reasonably reserve a hidden argv namespace and line-delimited
JSON on stdio. The collection unit can reasonably use a canonical namespace,
an environment selector, length-prefixed JSON, or another versioned envelope.
Each can preserve inward ports and typed domain values, yet the units cannot
start or decode one another. An environment selector also conflicts with
AD-7's raw-argv-first profile rule, while an unknown hidden flag falls into the
ledgered nonzero-unknown behavior. Exit status, diagnostics, malformed input,
stdout/stderr ownership, config inheritance, cancellation, and protocol-version
mismatch are likewise unowned.

**Blocking status: YES.** Reserve one explicit internal profile before public
and legacy routing, name its trust/availability rule, and define one versioned
request/result envelope carrying CollectionPlan/ScopeId identity, deadline,
capture reservation, typed report, and diagnostics. Bind stdin/stdout/stderr,
exit, timeout, signal, and mismatch behavior and add a cross-process fixture.
Provider stories cannot safely begin until the bootstrap CLI and collection
coordinator share this contract.

## Tier 2 finding — major

### NEW-M-1 — The UJ-5 trace row omits hot-history owners

The range-expanded identifier audit is complete, but semantic trace authority
still has one derivative defect. UJ-5 covers duplicate and hot triage, yet its
row lists only AD-4, AD-18, and AD-20 (`SPINE:904`). Hot evidence is owned by
AD-5, persisted by AD-16, and must enter the frozen generation through AD-21.
The FR-18 through FR-27 row correctly lists those decisions (`SPINE:891`), so
the two trace views disagree.

**Blocking status: NO independently.** After NEW-B-1 defines the missing cut,
add AD-5, AD-16, and AD-21 to UJ-5 and name retained sample history in its
landing. This row cannot remain authoritative as written.

## Identifier and semantic coverage audit

### Definition and reference integrity

| Identifier family | Definitions | Duplicates | Gaps | Undefined references | Result |
| --- | ---: | ---: | ---: | ---: | --- |
| AD-1 through AD-24 | 24 | 0 | 0 | 0 | **PASS** |
| ARCH-LIM-1 through ARCH-LIM-23 | 23 | 0 | 0 | 0 | **PASS** |

Every AD has exactly one `Binds`, `Prevents`, and enforceable-intent `Rule`
shape. The deterministic linter reports zero findings. The failures above are
semantic incompatibilities the mechanical linter cannot detect.

### Canonical source-to-trace coverage

| Family | Canonical source IDs | Range-expanded trace IDs | Mechanical result | Semantic result |
| --- | ---: | ---: | --- | --- |
| UJ | 6 | 6 | **PASS** | **FAIL** — UJ-1 and UJ-5 depend on NEW-B-1; UJ-5 also has NEW-M-1. |
| FR | 43 | 43 | **PASS** | **FAIL** — FR-24, FR-27, and FR-28 depend on NEW-B-1. |
| NFR | 16 | 16 | **PASS** | **FAIL** — NFR-1/NFR-12 depend on the common history cut; NFR-3 depends on NEW-B-2. |
| SM/SM-C | 9 | 9 | **PASS** | **FAIL** — SM-1 and SM-2 cannot be deterministic until NEW-B-1 closes. |
| Canonical UX | 89 | 89 | **PASS** | **FAIL** — all IDs have owners, but baseline/hot and collection-state projections inherit NEW-B-1/NEW-B-2. |

The 89 canonical UX IDs were expanded and checked individually as these exact
families: UX-FND 6, UX-IA 12, UX-VT 4, UX-CP 16, UX-ST 20, UX-IP 12,
UX-A11Y 5, SR-A11Y 1, UX-RP 6, and UX-BUD 7. Routing, voice, focus,
confirmation, action outcome, accessibility, responsive, and budget semantics
all have compatible owners. The failed subset is not a missing UX token: it is
the architecture input needed by baseline, hot, Brief, collection-state, and
linear projections.

## Requested seam verification

| Required seam | Result | Top evidence |
| --- | --- | --- |
| Release command ownership | **PASS** | `srvls release` owns install, upgrade, validate, status, and rollback; `application::release` and typed StateMigrationCoordinator own the effects (`SPINE:258-259`, `381-390`, `713-737`). |
| Legacy bad-arity routing | **PASS** | Legacy verb selects before exact-three-argument validation (`SPINE:241-246`), matching `SRC:338-345`. |
| Cron read-only behavior | **PASS** | Canonical cron mutation is absent and refused before argv construction (`SPINE:190-193`). |
| Dependency-boundary CI | **PASS** | Checked-in manifest plus locked `architecture_boundaries` test in bootstrap and all-target lanes (`SPINE:76-83`, `862-865`). |
| Correlation and confidence | **PASS** | Ordered non-summing vector, conflict rules, threshold, confidence categories, strict maximum, tie/ambiguity, and retained evidence (`SPINE:553-582`). |
| Suspend time | **PASS** | `CLOCK_BOOTTIME`; suspend consumes Lease and Heartbeat time (`SPINE:539-545`, `782`). |
| PlanId and durable plan handoff | **PASS** | UUIDv7 PlanId, repository/schema family, immutable ActionPlanV1, CAS consumption, launch and verification receipts (`SPINE:401-417`, `475-489`, `682-705`). |
| Provider trust | **PASS** | Absolute allowlist, cwd `/`, minimal environment allowlist, no caller PATH/hooks/credentials, legacy exception only (`SPINE:449-459`). |
| Hot evidence ownership | **PASS owner; FAIL cut** | Snapshot history and persisted samples are owned (`SPINE:168-170`, `477-480`, `636`), but NEW-B-1 blocks deterministic consumption. |
| Stable Host, policy, and public encodings | **PASS** | Machine-id HostIdentityV1, separate BootIdentity, NFC/percent encoding, canonical PolicySnapshotV1 and domain-separated hashes (`SPINE:739-762`). |
| State accounting | **PASS** | Exact `st_blocks * 512` artifact set, pruning, pinned truth, capacity mode, watermarks (`SPINE:493-524`; `ARCH-LIM-19`). |
| Trace rows | **PASS mechanical; FAIL semantic** | Every source ID is present; NEW-M-1 identifies the remaining owner omission. |

## Technology reality record

- The official Rust release record identifies Rust 1.97.0 as stable on
  2026-07-09; the spine accurately calls it current-stable at review.
- Official crates.io version endpoints confirmed all exact Stack entries
  queried by this review are present and non-yanked. This includes
  `ratatui 0.30.2`, `ratatui-crossterm 0.1.2`, `clap 4.6.2`,
  `serde 1.0.228`, `serde_json 1.0.150`, `rusqlite 0.39.0`,
  `libsqlite3-sys 0.37.0`, `toml 1.1.3+spec-1.1.0`, `uuid 1.24.0`,
  `time 0.3.53`, `thiserror 2.0.18`, `tracing 0.1.44`,
  `tracing-subscriber 0.3.23`, `signal-hook 0.4.4`, `libc 0.2.186`,
  `strsim 0.11.1`, `insta 1.48.0`, and `crossterm 0.29.0`.
- The manifest form `toml = "=1.1.3"` and separate TOML 1.1.0 spec notation
  remain correct because Cargo ignores SemVer build metadata. The spine does
  not repeat the earlier invalid requirement.
- No Rust product manifest or lockfile exists at this documentation gate. AD-12
  and AD-11 correctly assign locked MSRV/current-stable proof to bootstrap CI
  rather than claiming implementation evidence already exists.

## Validation record

| Validation | Command or method | Result |
| --- | --- | --- |
| Commit and isolation | `git rev-parse HEAD`; `git status --short --branch` | **PASS** — exact reviewed commit before report creation; clean isolated branch. |
| Required complete reads | Line-bounded reads through EOF for SPINE, RUBRIC, PRD, ADD, UX, and DESIGN | **PASS** — 3,230 controlling Markdown lines plus six lint-profile lines. |
| Architecture linter | `uv run .agents/skills/bmad-architecture/scripts/lint_spine.py --workspace _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14` | **PASS** — `ok: true`; zero findings. |
| AD/ARCH-LIM integrity | Range-expanding definition/reference audit | **PASS** — AD 24/24; ARCH-LIM 23/23; zero duplicates, gaps, or undefined references. |
| Canonical ID integrity | Range-expanded PRD/UX-to-capability/trace comparison | **PASS** — UJ 6/6; FR 43/43; NFR 16/16; SM/SM-C 9/9; UX 89/89. |
| Semantic coverage | Individual source contract and governing-rule review | **FAIL** — NEW-B-1, NEW-B-2, and NEW-M-1. |
| Live legacy router | Line-numbered `SRC:338-345` comparison to AD-7 | **PASS** — verb-first, then bad-arity check. |
| Technology currency | Official Rust release record and crates.io exact-version JSON endpoints | **PASS** — current stable verified; queried versions present and non-yanked. |
| Markdown lint | `markdownlint-cli2 --config _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/.markdownlint-cli2.jsonc <this-report>` | **PASS** — zero errors. |
| Whitespace/error check | `git diff --check`; `git diff --cached --check` | **PASS** — no output. |
| Changed-file scope | `git status --short`; cached-name inspection | **PASS** — only this acceptance report. |

## Final blocking status

**BLOCKED. Verdict: CHANGES REQUIRED.** The prior remediation is accepted, but
the spine is not yet approved as the sole downstream build substrate. Close
NEW-B-1 and NEW-B-2, repair NEW-M-1, rerun the deterministic and semantic gate,
and only then move the spine from draft to final or regenerate dependent
implementation stories.
