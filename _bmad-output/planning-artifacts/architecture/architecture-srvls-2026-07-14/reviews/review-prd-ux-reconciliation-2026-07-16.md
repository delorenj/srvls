---
status: final
created: 2026-07-16
updated: 2026-07-16
verdict: reconciliation-required
---

<!-- markdownlint-disable MD013 -->

# Architecture Review: Canonical PRD and UX Reconciliation

## Verdict

**RECONCILIATION REQUIRED. The July 14 architecture is mechanically valid but
is not a safe source for downstream epic or story refresh until it is updated
against the finalized July 16 PRD, addendum, and UX contracts.**

The deterministic architecture linter reports zero findings, but the current
spine cites only pre-PRD sources and contains zero canonical `UJ-*`, `FR-*`,
`NFR-*`, `SM-*`, `UX-*`, or `SR-A11Y-*` references. Its source list predates
the canonical product and UX contracts (`SPINE:18-23`), while the UX precedence
ledger makes the final PRD/addendum authoritative, followed by the canonical UX
spines, then only non-conflicting architecture constraints (`RECON:19-31`).

The reconciliation inventory is complete:

| Inventory | Assessed | Preserve | Amend | Add | Defer | Conflict |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| User Journeys | 6/6 | 0 | 2 | 3 | 0 | 1 |
| Functional Requirements | 43/43 | 6 | 14 | 19 | 0 | 4 |
| Non-Functional Requirements | 16/16 | 2 | 11 | 2 | 0 | 1 |
| Success Measures | 9/9 | 1 | 2 | 5 | 0 | 1 |
| Canonical UX IDs | 89/89 | 3 | 39 | 38 | 0 | 9 |

`Add` means the current architecture does not own the required seam. `Amend`
retains a valid architectural core but must change or expand its binding.
`Conflict` means the existing rule would produce canonically wrong behavior.
No canonical MVP requirement is eligible for `Defer`; only explicitly
out-of-scope product candidates and already named architecture deferrals may
remain deferred.

## Citation Key and Review Method

All citations are repository-relative exact path and line references:

- `PRD` —
  `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md`
- `ADD` —
  `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/addendum.md`
- `DESIGN` —
  `_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/DESIGN.md`
- `UX` —
  `_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md`
- `RECON` —
  `_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/reconcile-source-inputs.md`
- `MEMLOG` —
  `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/.memlog.md`
- `SPINE` —
  `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md`

All seven requested inputs were read in full: 2,442 lines total. Identifier
counts were derived from canonical headings and de-duplicated references. The
existing spine passed:

```text
uv run .agents/skills/bmad-architecture/scripts/lint_spine.py \
  --workspace \
  _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14

ok: true
total_findings: 0
```

That result proves the spine's shape, not canonical semantic coverage.

## Highest-Risk Findings

### 1. Runtime Promise and Observation ownership is missing

The product owns two independent truth lanes: declared Runtime Promises and
fresh scoped Host Observations (`PRD:20-24`, `PRD:119-128`). Reconciliation
retains four orthogonal axes and evaluates them in a fixed order
(`PRD:147-173`). The current architecture instead defines one provider-neutral
`Entry` aggregate as the shared collector, grouping, inspection, export, and
action model (`SPINE:51-55`; `MEMLOG:15`).

That model is no longer sufficient. An `Observation` is collected evidence; it
cannot own a Promise lifecycle, Heartbeat history, Lease, closure reason,
Accepted Baseline, or declared intent. Conversely, a Runtime Promise may exist
without any Observation and must still support inspection and Start planning.

Required ownership after reconciliation:

| Truth or behavior | Required owner | Current owner | Disposition |
| --- | --- | --- | --- |
| Runtime Promise, Lease, Heartbeats, closure, declaration provenance | Domain aggregate plus durable Promise repository | No owner; durable application state is explicitly rejected in `MEMLOG:10` | **Conflict / Add** |
| Provider-neutral Observation and Provider detail | Collector adapters produce immutable Observation values | `Entry` aggregate in `SPINE:51-55` | **Amend** |
| Collection reports and scoped obligations | Collection application service and Collector-report reducer | Snapshot plus binary `Availability` in `SPINE:69-73` | **Conflict / Amend** |
| Correlation, evidence status, Promise outcome, labels, attention, safety | Pure deterministic reconciliation domain service | No owner | **Add** |
| Durable Snapshot, Accepted Baseline, Evidence Window, retention | Snapshot/baseline repository with atomic schema-versioned writes | Ephemeral inventory snapshot only; no durable owner | **Conflict / Add** |
| Action plan, operation identity, execution evidence, terminal outcome | Action application service plus durable operation/audit repository | In-memory command/OperationId flow in `SPINE:75-79`, `SPINE:99-103` | **Amend** |
| TUI, `--linear`, legacy, and machine representations | Presenter adapters over the same application projections | TUI plus legacy presenters only | **Amend / Add** |

The addendum already assigns record format/location, Agent contracts, Lease
time, correlation rules, and retention to downstream architecture
(`ADD:57-63`). Epics must not choose those independently.

### 2. Canonical states and outcomes conflict with current architecture

The canonical names are data contracts, filters, serialization values, fixture
values, and UI copy. They are not presentation synonyms.

| Contract | Canonical values | Current architecture | Disposition |
| --- | --- | --- | --- |
| Promise Lifecycle | `lease-active`, `heartbeat-late`, `lease-expired`, `persistent-active`, `closed`; closure reason is exactly `released`, `completed`, or `revoked` (`PRD:151-156`) | Absent | **Add** |
| Evidence Status | `sufficient`, `incomplete`, `stale`, `out-of-scope` (`PRD:151-156`; `UX:25-34`) | Absent | **Add** |
| Promise Outcome | `healthy`, `broken`, `unresolved`, `inactive` (`PRD:151-156`) | Generic normalized status/health in `SPINE:51-55`, `SPINE:141-143` | **Conflict / Add** |
| Observation labels | `orphaned`, `duplicate`, `stale`, `hot`, `unmanaged`, `abandoned`; labels coexist (`PRD:134-145`) | Absent | **Add** |
| Safe-to-stop Assessment | `safe`, `unsafe`, `unknown`, with reasons and no authorization effect (`PRD:446-454`) | Absent | **Add** |
| Collection Obligation | `required`, `optional`, `not-applicable`, with scope promotion (`PRD:303-328`) | `Availability { Required \| Optional }` in `SPINE:69-73` | **Conflict / Amend** |
| Collector outcome | `complete`, `partial`, `unavailable`, `denied`, `timed-out`, `invalid-output` (`PRD:303-311`) | `Success`, `Partial`, `Failed`, `TimedOut`, `Denied`, `Unavailable` in `SPINE:69-73` | **Conflict** |
| Action Outcome | `verified`, `executed-unverified`, `refused`, `timed-out`, `failed`, exactly one (`PRD:585-605`) | `ExecutedUnverified`, `Stale`, and `Failed` rules in `SPINE:75-79` | **Conflict** |

The phrase “unknown evidence” in `PRD:382-389` must not become a fifth Evidence
Status. The canonical table and UX explicitly require `unresolved` Promise
Outcome with `incomplete`, `stale`, or `out-of-scope` Evidence Status
(`PRD:151-156`; `UX:25-34`). Pre-execution identity drift is `refused` with
reason `stale-identity`; post-execution replacement is `executed-unverified`
with a replacement reason (`PRD:595-605`; `UX:211-216`).

### 3. Durable state and time semantics directly contradict the PRD

The memlog constrains the utility to “no ... durable application state”
(`MEMLOG:10`) and assumes flags/environment only until grouping or theme needs
justify more (`MEMLOG:28`). The PRD requires atomic, crash-safe,
schema-versioned Runtime Promise, lifecycle event, Snapshot, and compatibility
metadata (`PRD:734-736`) plus local durable Promise, event, policy, Snapshot,
and compatibility state (`PRD:789-795`).

The no-durable-state constraint must be explicitly superseded in the memlog; it
cannot merely disappear from a redistilled spine. Architecture must then bind:

- record schemas and locations;
- atomic write/rename, locking, fsync/durability, corruption detection, and
  recovery behavior;
- schema versioning and migration/compatibility policy;
- bounded retention and deletion without deleting active reconciliation truth;
- stable Promise IDs and operation IDs distinct from Observation identities;
- wall time for display/audit, monotonic duration accounting, Host boot identity,
  suspend/clock-discontinuity behavior, and Lease revalidation.

The current time convention is only “UTC `SystemTime`/duration internally”
(`SPINE:135-146`), while the canonical contract requires wall-clock rollback,
restart, suspend, and discontinuity behavior to be explicit (`PRD:738-740`).

### 4. Operational numeric limits are a readiness blocker

The PRD states that architecture owns Collector deadlines, output caps,
retention, Heartbeat grace, and action-verification limits, and that these must
be closed before implementation readiness can report `READY` (`PRD:814-819`).
UX repeats that ownership and requires effective values and provenance to be
visible (`UX:552-577`; `RECON:114-116`).

The spine currently says only “fixed,” “bounded,” “deadline,” and “caps”
(`SPINE:99-103`) and gives no operational values, valid ranges, units, or
configuration provenance. Architecture must close at least this twelve-family
minimum set; the review intentionally does not invent the numbers.

| Architecture-owned family | Current state | Required closure |
| --- | --- | --- |
| Default ephemeral Lease duration | Absent | Default, min/max, units, source precedence, restart/suspend behavior |
| Heartbeat grace | Absent | Default/range and relationship to declared renewal cadence |
| Stale policy | Absent | Evidence source, window/range, and no-Telemetry behavior |
| Hot policy | Absent | Metric, sample/trend window, threshold range, and provenance |
| Promise/event/Snapshot/audit retention | Absent | Per-record bounds, active-truth exception, deletion and recovery behavior |
| Collector deadlines | Qualitative only | Per-scope default/range, hard termination, diagnostic mapping |
| Subprocess and detail output bounds | Qualitative only | stdout/stderr bytes, detail bytes/lines, truncation/redaction disclosure |
| Action verification limit | Qualitative only | Default/range, polling/correlation rule, `executed-unverified` boundary |
| Collector worker concurrency | “fixed worker set” only | Count/default/range and canonical-host acceptance behavior |
| Provider execution hard deadline | Qualitative only | Per-operation bound and distinction from verification timeout |
| Signal shutdown and child-reaping grace | Absent | First/repeated signal bounds and durable-outcome write boundary |
| Action-plan validity | Absent | Expiry/generation rule and confirmation behavior after expiry |

For every policy, the configuration contract must expose effective value,
units, built-in default, valid range, winning source, overridden-source chain,
and a deterministic validation error (`UX:114-136`, `UX:450-457`). The current
“CLI and environment only” convention (`SPINE:135-146`) may be retained only if
it is promoted from assumption to a complete source-class and precedence
decision. The architecture must either bind a deterministic precedence such as
built-in, environment, then CLI override, or explicitly add another source; an
epic must not decide this.

The seven UX-visible budgets are already canonical and must be inherited, not
renumbered or replaced: input/filter, refresh acknowledgement, slow-refresh
disclosure, action acknowledgement, pending update, terminal outcome render,
and resize response (`UX:563-577`). Architecture still needs to publish the
canonical Host used by their p95 fixture (`UX:558-561`).

## User Journey Coverage — 6/6

| Journey | Architecture assessment | Disposition | Evidence |
| --- | --- | --- | --- |
| UJ-1 morning handoff | Inventory/TUI exists, but there is no Brief, Evidence Window, attention summary, Promise truth, or baseline | **Add** | `PRD:52-59`; `SPINE:216-225` |
| UJ-2 Agent declares and renews | Promise, Lease, Heartbeat, durable provenance, and Agent command contracts are absent; durable state is rejected | **Conflict** | `PRD:61-68`; `MEMLOG:10`; `SPINE:165-201` |
| UJ-3 diagnose broken Promise | Collector truth and inspection are reusable, but no Promise correlation, absence gate, or Promise-origin Start exists | **Add** | `PRD:70-76`; `SPINE:69-79` |
| UJ-4 remove abandoned Runtime | Exact-target plan/revalidate/verify is strong, but abandoned/safety semantics and canonical outcomes are absent or wrong | **Amend** | `PRD:78-85`; `SPINE:75-79`, `SPINE:117-133` |
| UJ-5 duplicate and hot triage | Stack grouping is not duplicate reconciliation; hot policy, multi-label findings, intended count, and safety are absent | **Add** | `PRD:87-93`; `SPINE:63-67` |
| UJ-6 upgrade and recover | Atomic symlink/checksum/rollback is present; staged compatibility and post-activation consumer validation are incomplete in the spine | **Amend** | `PRD:95-101`; `SPINE:111-115`; `MEMLOG:45`, `MEMLOG:61` |

## Functional Requirement Coverage — 43/43

### Runtime Promise lifecycle — FR-1 through FR-7

| ID | Primary disposition | Required architecture landing | Evidence |
| --- | --- | --- | --- |
| FR-1 | **Add** | Runtime Promise aggregate, validation, durable repository, stable Promise ID, human/machine result | `PRD:181-188`; `SPINE:165-201` |
| FR-2 | **Add** | Append-only declaration/lifecycle provenance and auditable revision semantics | `PRD:190-197`; `MEMLOG:10` |
| FR-3 | **Conflict** | Finite Lease by default, never implicit persistence; supersede no-durable-state constraint | `PRD:199-206`; `MEMLOG:10` |
| FR-4 | **Add** | Idempotent Heartbeat/renewal command, caller-operation identity, authorization, Lease clock | `PRD:208-215` |
| FR-5 | **Add** | Closed lifecycle plus exactly one retained closure reason; no mutation side effect | `PRD:217-225` |
| FR-6 | **Add** | Persistent intent invariant requiring Durable Ownership and inspectable Launch Mechanism | `PRD:227-234` |
| FR-7 | **Add** | Deterministic Agent command schemas, retry correlation, stdout/stderr and exit contracts | `PRD:236-243`; `UX:385-390` |

### Host discovery — FR-8 through FR-17

| ID | Primary disposition | Required architecture landing | Evidence |
| --- | --- | --- | --- |
| FR-8 | **Preserve** | Keep cron adapter/typed diagnostics; reconcile scope obligations | `PRD:249-256`; `SPINE:34-38`, `SPINE:181-191` |
| FR-9 | **Preserve** | Keep system/user systemd adapter and explicit scope | `PRD:258-265`; `SPINE:34-38`, `SPINE:181-191` |
| FR-10 | **Preserve** | Keep immutable Docker identity and failure-local collection | `PRD:267-274`; `SPINE:117-121` |
| FR-11 | **Preserve** | Keep PM2 birth-discriminated identity and bounded parse diagnostics | `PRD:276-283`; `SPINE:117-121`; `MEMLOG:49` |
| FR-12 | **Add** | Direct Host-process Collector, PID plus birth/fingerprint identity, provider-child/self deduplication | `PRD:285-292`; `SPINE:181-191` |
| FR-13 | **Amend** | Rename/refactor collected `Entry` into canonical Observation plus typed Provider detail/provenance | `PRD:294-301`; `SPINE:51-55` |
| FR-14 | **Conflict** | Replace `Availability` and old reducer vocabulary with scoped Collection Obligation and canonical outcomes | `PRD:303-328`; `SPINE:69-73` |
| FR-15 | **Amend** | Retain bounded inspection; bind numeric byte/line limits and the canonical sanitizer | `PRD:330-337`; `SPINE:87-91`, `SPINE:99-103` |
| FR-16 | **Amend** | Expand from one test authority to layered inventory, frozen corpus, live smoke, deployed-consumer checks, and ledger | `PRD:339-349`; `SPINE:93-97`, `SPINE:105-109` |
| FR-17 | **Amend** | Define canonical Collector-outcome-to-exit mapping using effective obligations and stable error envelopes | `PRD:351-358`; `SPINE:69-73` |

### Reconciliation — FR-18 through FR-27

| ID | Primary disposition | Required architecture landing | Evidence |
| --- | --- | --- | --- |
| FR-18 | **Add** | Pure correlation service with evidence/conflicts/confidence and supported-scope gates | `PRD:364-371` |
| FR-19 | **Add** | Canonical healthy Promise Outcome rule under sufficient evidence | `PRD:373-380` |
| FR-20 | **Add** | Broken versus unresolved rule using sufficient absence evidence | `PRD:382-389` |
| FR-21 | **Add** | Orphaned Observation rule independent of Agent-created provenance | `PRD:391-398` |
| FR-22 | **Add** | Duplicate excess-set rule; never infer destructive target | `PRD:400-407` |
| FR-23 | **Add** | Configured explainable stale policy and evidence provenance | `PRD:409-416` |
| FR-24 | **Add** | Configured hot threshold/trend policy and sample provenance | `PRD:418-425` |
| FR-25 | **Add** | Unmanaged/abandoned rules across ownership, Lease, Heartbeat, and closure | `PRD:427-435` |
| FR-26 | **Add** | Evidence explanation plus deterministic conservative Safe-to-stop service | `PRD:437-454` |
| FR-27 | **Conflict** | Durable candidate Snapshots, explicit Accepted Baseline pointer, eligibility/override audit, retention | `PRD:456-466`; `MEMLOG:10`; `SPINE:69-73` |

### Brief, CLI, and TUI — FR-28 through FR-35

| ID | Primary disposition | Required architecture landing | Evidence |
| --- | --- | --- | --- |
| FR-28 | **Add** | Brief projection answering all eight questions with baseline, timezone, completeness, and drill-down IDs | `PRD:472-480` |
| FR-29 | **Amend** | Preserve deterministic Stack inference but place attention first and expose Ungrouped/evidence | `PRD:482-489`; `SPINE:63-67` |
| FR-30 | **Amend** | Preserve TTY routing; add exact `TERM=dumb`, `--linear`, Agent, and ledger-gated fzf behavior | `PRD:491-498`; `SPINE:81-85` |
| FR-31 | **Amend** | Bind canonical keys, filter algebra, focus recovery, responsive modes, nonblocking refresh | `PRD:500-507`; `SPINE:135-147` |
| FR-32 | **Add** | Linked Promise/Observation/Heartbeat/Lease/evidence detail and opaque references | `PRD:509-516` |
| FR-33 | **Preserve** | Keep text, `NO_COLOR`, ASCII, and sanitation invariant; adopt UX's stronger sanitizer | `PRD:518-525`; `SPINE:87-91` |
| FR-34 | **Amend** | Add every canonical application, collection, baseline, config, and action state without aliases | `PRD:527-534`; `UX:193-250` |
| FR-35 | **Add** | Canonical `a` Action Menu and Promise-origin Start; direct keys are conditional accelerators | `PRD:536-543`; `SPINE:135-147` |

### Lifecycle safety and recovery — FR-36 through FR-43

| ID | Primary disposition | Required architecture landing | Evidence |
| --- | --- | --- | --- |
| FR-36 | **Amend** | Retain typed plans; add Promise-origin Start, direct-process signal limits, and explicit cron read-only rule | `PRD:549-556`; `SPINE:75-79` |
| FR-37 | **Amend** | Preserve exact Observation revalidation; add Promise/absence/start-target revalidation | `PRD:558-565`; `SPINE:117-121` |
| FR-38 | **Amend** | Default Cancel, restart confirmation, typed unknown acknowledgement, exact operation and privilege | `PRD:567-574`; `UX:319-339` |
| FR-39 | **Amend** | Preserve separate OperationId/generation; persist operation state and define exit/cancellation races | `PRD:576-583`; `SPINE:99-103`; `UX:392-410` |
| FR-40 | **Conflict** | Replace old outcome vocabulary and implement canonical precedence and reason-code split | `PRD:585-605`; `SPINE:75-79` |
| FR-41 | **Preserve** | Keep individual targets, read-only groups, and narrow noninteractive raw-mode privilege | `PRD:607-614`; `SPINE:129-133` |
| FR-42 | **Amend** | Keep locked artifact/checksum/atomic path; add staged compatibility checks and deterministic compatibility/version report | `PRD:620-627`; `SPINE:111-115` |
| FR-43 | **Amend** | Keep prior target through post-activation timer/consumer validation; auto-restore and revalidate on failure | `PRD:629-636`; `SPINE:111-115`; `MEMLOG:45`, `MEMLOG:61` |

## Non-Functional Requirement Coverage — 16/16

| ID | Primary disposition | Architecture result | Evidence |
| --- | --- | --- | --- |
| NFR-1 | **Amend** | Extend deterministic grouping/order into lifecycle, correlation, safety, serialization, and attention | `PRD:702-704`; `SPINE:63-67`, `SPINE:93-103` |
| NFR-2 | **Amend** | Preserve partial truth, but adopt canonical obligations/outcomes and storage/action failure scope | `PRD:706-708`; `SPINE:69-73` |
| NFR-3 | **Amend** | Preserve worker/deadline/reaping design; publish numeric concurrency, deadline, and capture bounds | `PRD:710-712`; `SPINE:99-103` |
| NFR-4 | **Preserve** | Typed argv-only runner, no shell, end-of-options handling already bind the seam | `PRD:714-716`; `SPINE:75-79`, `SPINE:99-103` |
| NFR-5 | **Preserve** | Narrow Provider operation privilege and no raw-mode prompt already bind the seam | `PRD:718-720`; `SPINE:129-133` |
| NFR-6 | **Amend** | Preserve RAII terminal owner; add phase-specific signal, cancellation, reaping, and durable outcome rules | `PRD:722-724`; `SPINE:123-127`; `UX:392-410` |
| NFR-7 | **Amend** | Preserve clean legacy stdout; extend to Promise, action, config, JSON, and `--linear` contracts | `PRD:726-728`; `SPINE:81-97` |
| NFR-8 | **Amend** | Preserve text/color/ASCII floor; add screen-reader path, exact geometry, focus, motion, and sanitizer rules | `PRD:730-732`; `UX:459-519` |
| NFR-9 | **Conflict** | Supersede no-durable-state constraint with atomic schema-versioned Promise/Snapshot/audit storage | `PRD:734-736`; `MEMLOG:10` |
| NFR-10 | **Add** | Bind monotonic duration, wall time, boot ID, restart, suspend, and clock-discontinuity semantics | `PRD:738-740`; `SPINE:141-142` |
| NFR-11 | **Add** | Bind local permissions, field minimization, redaction, retention, and deletion for new durable stores | `PRD:742-744` |
| NFR-12 | **Amend** | Preserve generation/OperationId lanes; add durable writer coordination and late Heartbeat/Lease races | `PRD:746-748`; `SPINE:99-103` |
| NFR-13 | **Amend** | Preserve fixtures/fakes/goldens; add Promise, Lease/time, reconciliation, config, linear, and signal fixtures | `PRD:750-752`; `SPINE:105-109` |
| NFR-14 | **Amend** | Preserve compatibility corpus; add behavior inventory, live smoke, named consumers, exact metrics, and ledger completeness | `PRD:754-756`; `SPINE:93-109` |
| NFR-15 | **Amend** | Preserve locked x86_64 GNU/Linux release; close full staged validation and recovery contract | `PRD:758-760`; `SPINE:111-115` |
| NFR-16 | **Amend** | Promote configuration from assumption to schema, defaults, bounds, source precedence, provenance, validate/explain | `PRD:762-764`; `MEMLOG:28`; `SPINE:145` |

## Success Measure Coverage — 9/9

| ID | Primary disposition | Architecture gate | Evidence |
| --- | --- | --- | --- |
| SM-1 | **Add** | Canonical Brief fixtures prove all eight answers and honest incompleteness | `PRD:680-684` |
| SM-2 | **Add** | Multi-axis reconciliation fixtures prove all eight labels without false certainty | `PRD:682-684` |
| SM-3 | **Conflict** | Replace action results and test exactly one canonical outcome by precedence | `PRD:684`; `SPINE:75-79` |
| SM-4 | **Amend** | Layer frozen corpus, live smoke, named consumers, and approved ledger deviations | `PRD:686-690`; `SPINE:93-109` |
| SM-5 | **Add** | Agent lifecycle fixtures cover declare/retry/renew/query/release/expiry | `PRD:688-690` |
| SM-6 | **Add** | Brief-to-evidence-to-exact-target fixtures cover TUI and human-linear paths | `PRD:690`; `UX:412-448` |
| SM-C1 | **Add** | Precision fixtures prohibit unsupported anomaly labels and destructive ranking shortcuts | `PRD:692-696` |
| SM-C2 | **Amend** | Preserve partial truth and test that deadline pressure never becomes absence | `PRD:694-696`; `SPINE:69-73` |
| SM-C3 | **Preserve** | Read-only groups and no automatic cleanup already prevent cleanup-volume optimization | `PRD:696`; `SPINE:75-79`, `SPINE:227-235` |

## Canonical UX Contract Family Coverage — 89/89

The 89 canonical IDs comprise 6 FND, 12 IA, 4 VT, 16 CP, 20 ST, 12 IP,
5 A11Y, 6 RP, 7 BUD, and 1 SR-A11Y contract. Every ID in every family is
accounted for below.

| Family | IDs | Primary disposition counts | Architecture reconciliation | Evidence |
| --- | --- | --- | --- | --- |
| Foundation | UX-FND-1..6 | 1 preserve, 4 amend, 1 conflict | Preserve local one-tool and no-auto-cleanup boundaries; add orthogonal truth and Agent/linear surfaces; fix old outcomes | `UX:13-57` |
| Information Architecture | UX-IA-1..12 | 7 amend, 5 add | Add Brief, Action Menu, baseline, deterministic refinement, config surfaces; amend existing detail/help/install/machine paths | `UX:59-136` |
| Voice and Tone | UX-VT-1..4 | 1 preserve, 2 amend, 1 add | UX owns copy; architecture must expose exact vocabulary, provenance, reason codes, retry correlation, and bounded diagnostics | `UX:138-168` |
| Components | UX-CP-1..16 | 1 preserve, 8 amend, 7 add | Group row is structurally supported; every other component needs amended or new projection/state support | `UX:170-191`; `DESIGN:198-314` |
| State Patterns | UX-ST-1..20 | 8 amend, 5 add, 7 conflict | Add empty/baseline/config/focus states; amend refresh/action controls; replace all old outcome and stale-identity aliases | `UX:193-250` |
| Interaction Primitives | UX-IP-1..12 | 5 amend, 6 add, 1 conflict | Amend routing/keys/confirmation/install/signals; add filter, action menu, baseline, Agent, linear, config; replace action lifecycle vocabulary | `UX:252-457` |
| Accessibility | UX-A11Y-1..5 | 4 amend, 1 add | Amend semantics/focus/sanitizer/no-motion/restoration; add full human-linear alternative | `UX:459-500` |
| Responsive/Platform | UX-RP-1..6 | 1 amend, 5 add | Add 120x30, 80x24, 60x20, below-minimum, and resize behavior; amend redirected/TERM routing | `UX:502-519` |
| UX Budgets | UX-BUD-1..7 | 7 add | Inherit exact defaults/ranges unchanged and add architecture scheduling plus canonical-host acceptance support | `UX:552-577` |
| Screen-reader acceptance | SR-A11Y-1 | 1 add | Add complete `--linear` implementation and fixture path with all action outcomes | `UX:443-448` |

The paired visual spine adds no hidden palette or icon vocabulary. Its contract
families are also reconciled:

| Visual family | Disposition | Architecture consequence | Evidence |
| --- | --- | --- | --- |
| Forensic-calm brand and authority boundary | **Preserve** | Inherit; do not restate or invent branding | `DESIGN:101-120` |
| Color, glyph, typography, time | **Amend** | Text is primary; color/glyphs are orthogonal supplements; terminal theme/font remain in control | `DESIGN:122-166`; `MEMLOG:22` |
| Layout, reading order, collapse | **Add / Amend** | Attention precedes Stack; add exact collapse order and responsive geometry | `DESIGN:168-196`; `SPINE:63-67` |
| Sixteen named components | **Add / Amend** | Names match UX-CP-1..16 exactly; presenters may not invent substitutes | `DESIGN:198-314` |
| Do/don't invariants | **Preserve / Amend** | Retain partial truth, exact identity, read-only groups; replace optimistic or blended state semantics | `DESIGN:316-329` |

### Human-linear and TUI closure

The current spine contains only the legacy presenters and ratatui tree
(`SPINE:165-201`) and keys that predate the canonical Action Menu and baseline
dialog (`SPINE:135-147`). The following are architecture-visible, not optional
UX polish:

- `--linear` is an additive first-class human surface with the exact six-step
  command path in `UX:412-448`; it is neither the legacy table nor JSON.
- `srvls config validate --linear|--json` and
  `srvls config explain --linear` validate before collection, state writes,
  mutation, raw mode, or alternate-screen entry (`UX:114-136`, `UX:450-457`).
- Bare invocation and `TERM=dumb` routing preserve legacy table behavior;
  explicit formats win, `NO_COLOR` affects color only, and `--ascii` affects
  glyphs only (`UX:254-278`).
- `a` is the canonical action entry, `b` opens baseline acceptance, and direct
  `s`/`R`/`x` keys are conditional exact-Observation accelerators. Start has no
  direct key and originates from a Promise (`UX:303-339`).
- `q` cannot exit while submitted work is active; `Esc` navigates/cancels only
  before submit. Signal disposition is phase-specific and persists one truthful
  terminal outcome before restoration (`UX:392-410`).
- Focus is recovered by exact identity, never row index, and the responsive
  floor is exactly 60 by 20 (`UX:218-233`, `UX:502-519`).

### Configuration provenance closure

UX does not require architecture to invent a file format, but it does require a
real schema and visible provenance. Architecture must decide:

1. source classes and deterministic precedence;
2. canonical field order and names;
3. types, defaults, valid ranges, units, and redaction policy;
4. environment and CLI spelling, including repeatability/conflicts;
5. unknown-field and invalid-value policy with no silent clamp/fallback;
6. the machine error envelope and stable reason codes;
7. which policy values are captured into Snapshots, findings, plans, and audit
   records so later explanation uses the value that actually governed work.

Without that decision, stories would invent incompatible defaults and could
recompute old findings using new policy.

## Existing Architecture Decision Disposition

| Existing decision | Primary disposition | Reconciliation |
| --- | --- | --- |
| AD-1 Dependency direction | **Amend** | Preserve inward dependencies; add Promise, reconciliation, config, storage, clock, and operation ports |
| AD-2 Composed base Entry | **Conflict** | Replace “one aggregate owns all” with separate Runtime Promise and Observation aggregates plus reconciliation projections |
| AD-3 Host integration ports | **Amend** | Preserve Collector/Inspector/ActionExecutor/CommandRunner; add stores, clock/boot, config, audit, and direct-process ports |
| AD-4 Stack inference | **Preserve** | Keep deterministic algorithm as a read-only Observation projection; attention precedes it |
| AD-5 Snapshot collection truth | **Conflict** | Retain failure-local truth but replace availability/outcome vocabulary and add obligations, durable candidates, and baseline semantics |
| AD-6 Commands own mutations | **Conflict** | Preserve typed planning and revalidation; replace confirmation scope, Promise Start, persistence, signals, and Action Outcomes |
| AD-7 Terminal-aware mode | **Amend** | Add linear/Agent/config surfaces, exact mode precedence, and ledger-gated fzf-lines removal |
| AD-8 Visual fallbacks | **Amend** | Make text primary, separate color/glyph controls, adopt full sanitizer and responsive/accessibility rules |
| AD-9 Presenter compatibility | **Amend** | Replace “sole authority” with layered oracle and named consumer validation; add versioned Promise/reconciliation schemas |
| AD-10 Bounded concurrency | **Amend** | Preserve generation/OperationId lanes and total runner; bind numeric limits and durable writer/cancellation semantics |
| AD-11 Deterministic verification | **Amend** | Add all Promise, Lease/time, reconciliation, config, human-linear, lifecycle, signal, and recovery fixtures |
| AD-12 Locked Linux binary | **Amend** | Preserve MSRV/lock/ABI/checksum/atomic link; add staged compatibility, consumer validation, and automatic recovery proof |
| AD-13 Typed identity | **Amend** | Retain Provider-native Observation identity; add direct-process birth identity and separate stable Promise/plan/operation IDs |
| AD-14 Terminal-session owner | **Amend** | Preserve RAII/Update ownership; add phase-specific bounded cancellation, reaping, durable outcome, and quit policy |
| AD-15 Narrow privilege | **Preserve** | Retain selected-Provider scope and no raw-mode prompt; expose privilege in plans and machine results |

Primary count for the fifteen existing ADs: 2 preserve, 10 amend, 3 conflict.
In addition, `MEMLOG:10` must be superseded as a direct authority conflict.

### New architecture decisions required

| New decision family | Disposition | Must bind |
| --- | --- | --- |
| Declared-intent domain and durable Promise repository | **Add** | FR-1..7, NFR-9..11 |
| Orthogonal reconciliation and Safe-to-stop policy | **Add** | FR-18..26, NFR-1..2 |
| Durable Snapshots, Accepted Baseline, Evidence Window, audit, retention | **Add** | FR-27..28, NFR-9, baseline UX |
| Lease/time/boot/suspend/clock semantics | **Add** | FR-3..5, NFR-10 |
| Configuration schema, precedence, validation, provenance, numeric policy | **Add** | NFR-16, UX-IA-12, UX-IP-12, UX-BUD-1..7 |
| Direct Host-process observation and identity | **Add** | FR-12, FR-36..37 |
| Brief, human-linear, Agent, and machine projection contracts | **Add** | FR-7, FR-28..35, UX-IP-9..12, SR-A11Y-1 |
| Durable operation/audit and phase-specific shutdown | **Add** | FR-39..40, NFR-6, UX-IP-10 |

### Deferrals that remain valid

The existing Deferred section may remain only with its current revisit
conditions: persistent grouping overrides, user theme files, dynamic
collectors, grouped legacy machine output, broader portability, group actions,
and terminal-safe interactive privilege (`SPINE:227-235`). These align with the
PRD's explicit exclusions for remote fleet control, automatic cleanup, RBAC,
deep external-system ingestion, non-Linux Providers, unsupported scopes,
persistent Stack overrides, and group actions (`PRD:666-676`).

Deferral must not be used for direct processes, Promise state, reconciliation,
human-linear access, canonical configuration, operational bounds, or
install/recovery; all are canonical MVP obligations.

## Compatibility Reconciliation

The architecture's presenter boundary, encounter-order rule, frozen fixtures,
goldens, lockfile, and compatibility ledger are valuable and should be
preserved (`SPINE:93-115`). Four amendments are mandatory:

1. **Layer the oracle.** The checked-in Python behavior inventory, frozen
   deterministic fixture/golden corpus, live-Host smoke, and named deployed
   consumers are jointly required; `tests/compat` cannot be called the sole
   authority (`PRD:339-349`, `PRD:754-756`).
2. **Ledger every target safety deviation.** Current immediate name/row-based
   actions are explicitly contradicted by the PRD and replaced by plan,
   identity, confirmation, revalidation, verification, and canonical outcomes
   (`RECON:68-78`).
3. **Do not remove `--fzf-lines` by assertion.** The current spine removes it
   directly (`SPINE:81-85`); canonical sources permit removal only through the
   compatibility ledger (`PRD:491-498`; `ADD:50-53`; `UX:254-278`).
4. **Version additive target schemas.** Promise, Observation, reconciliation,
   config, action, and `--linear` surfaces are new contracts. They must not
   silently alter flat legacy JSON, Prometheus, Markdown, table, inspection, or
   exit behavior (`PRD:339-349`; `UX:52-57`).

## Lifecycle Safety Reconciliation

Preserve these strong existing invariants:

- individual exact targets and read-only groups (`SPINE:75-79`);
- Provider-native identity and immediate pre-mutation revalidation
  (`SPINE:117-121`);
- typed argv-only execution, hard termination, and child reaping
  (`SPINE:99-103`);
- separate refresh generation and OperationId lanes (`SPINE:99-103`);
- narrow privilege and no raw-mode authorization prompt (`SPINE:129-133`).

Amend them so lifecycle behavior cannot diverge:

- Start plans from an active Promise and supported Launch Mechanism even with no
  Observation; absence and start target are revalidated (`PRD:536-565`).
- Cron remains read-only. Direct-process actions are identity-safe signals only
  and cannot invent Start/Restart without a Launch Mechanism (`PRD:549-556`).
- Safe-to-stop is a recalculated advisory, never authorization. `unsafe` is
  unavailable; `unknown` requires typed acknowledgement in the TUI
  (`PRD:446-454`; `UX:235-250`).
- Provider execution timeout is `timed-out`; verification inability after an
  invoked operation is `executed-unverified`. Do not collapse the two
  (`PRD:595-605`).
- Every submitted operation and exactly one terminal outcome are durable before
  controlled exit. Repeated signals do not create a second outcome
  (`UX:392-410`).

## Install and Recovery Reconciliation

Preserve the current one-binary, locked MSRV 1.88, x86_64 GNU/Linux, checksum,
version-directory, atomic symlink, prior-target, and rollback design
(`SPINE:111-115`). Amend its transaction boundary:

1. Stage and checksum the candidate.
2. Run the frozen compatibility smoke before link mutation.
3. Atomically activate the candidate while retaining the known-good target.
4. Validate version, `srvls-metrics`, `srvls-snapshot`, exact machine outputs,
   and every named deployed consumer.
5. Release the old target only after all required validation passes.
6. On post-activation failure, atomically restore the prior target, rerun
   consumer validation, and emit one failed final result with recovery evidence.

The PRD and UX require that order (`PRD:95-101`, `PRD:620-636`;
`UX:376-383`, `UX:686-702`). The memlog contains some consumer-smoke intent
(`MEMLOG:45`), but the final AD-12 dropped it; it must return to the spine as an
enforceable rule.

## Downstream Invention Stop-List

Until the architecture is updated, downstream epics and stories must not invent
any of the following:

- Promise, event, Snapshot, baseline, operation, audit, or compatibility record
  formats, paths, schemas, locking, migration, or recovery;
- Promise/Observation aggregate ownership or a blended replacement status;
- any canonical lifecycle, evidence, Promise outcome, Observation label,
  Collector outcome, or Action Outcome alias;
- Lease clock, boot, suspend, rollback, grace, expiry, or retention behavior;
- correlation weights, identity-confidence rules, absence gates, or safety
  authorization shortcuts;
- config source classes, precedence, defaults, ranges, silent fallback, or
  provenance capture;
- numeric Collector, capture, concurrency, retention, verification, execution,
  plan-expiry, or shutdown/reaping limits;
- direct-process identity, provider-child deduplication, or signal capability;
- baseline eligibility/override side effects or automatic baseline advancement;
- TUI keys, focus, responsive geometry, `--linear` commands, machine envelopes,
  or outcome copy outside the canonical UX IDs;
- compatibility-corpus authority, `--fzf-lines` removal, consumer disposition,
  install activation, or rollback transaction boundaries.

Stories may cite canonical contracts and create acceptance fixtures, but they
must wait for architecture to own the seams above before choosing implementation
mechanisms or values.

## Required Reconciliation Order

1. Append explicit memlog entries superseding the no-durable-state constraint,
   the single-Entry ownership model, old Collector vocabulary, old Action
   Outcomes, color-primary wording, and unconditional `--fzf-lines` removal.
2. Add the final PRD, addendum, DESIGN, EXPERIENCE, and source-reconciliation
   ledger to the spine source list and expand scope/binds to Promise lifecycle,
   reconciliation, durable state, config, direct processes, Brief/linear/Agent
   surfaces, and recovery.
3. Add the eight new decision families above and publish all architecture-owned
   numeric defaults, ranges, provenance, and acceptance checks.
4. Amend AD-1 through AD-15 without renumbering them; preserve the two decisions
   and valid deferrals identified here.
5. Re-run deterministic spine lint, independent semantic reviewers, all
   UJ/FR/NFR/SM/UX trace counts, then regenerate epics/stories and rerun
   implementation readiness.

The architecture should not be used as the sole build substrate until this
sequence closes with 6/6 UJs, 43/43 FRs, 16/16 NFRs, 9/9 success measures, and
89/89 canonical UX IDs explicitly traced to preserved, amended, or added
architecture decisions.
