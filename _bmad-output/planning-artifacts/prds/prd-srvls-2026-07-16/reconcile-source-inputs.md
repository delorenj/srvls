---
title: "srvls PRD Source-Input Reconciliation"
project: "srvls"
artifact_type: "source-input-reconciliation"
date: "2026-07-16"
status: "analysis-only"
---

<!-- markdownlint-disable MD013 MD025 -->

# srvls PRD Source-Input Reconciliation

## Scope and method

This report reconciles the canonical `prd.md` and `addendum.md` against exactly
these inputs:

- `source-extract-live-evidence.md`;
- `research-current-landscape.md`; and
- the product-owner thesis supplied for this reconciliation.

It does not amend the PRD, addendum, UX, architecture, epics, tasks, code, or an
implementation-readiness artifact. A **phase-blocking** gap is an unresolved
product contract that would cause UX, architecture, or epic planning to invent
material behavior. A **non-blocking** gap can be resolved after those phases
begin, but has a named closure point before acceptance, migration, or release.

Artifact citations name the exact heading and, where available, the stable
requirement or journey identifier. Line numbers are intentionally secondary to
section names because the canonical artifacts are still drafts.

### Supplied thesis clause index

The supplied thesis is indexed here so later tables can cite it precisely:

- **T1 — Product role:** `srvls` is the morning handoff and reconciliation
  layer for Agent-created Runtime Promises.
- **T2 — Two-sided truth:** combine actual Host discovery with
  self-registration of intent, provenance, ownership, and renewable,
  ephemeral-by-default Leases.
- **T3 — Required handoff content:** surface what changed; declared versus
  running truth; lost Heartbeats; and healthy, broken, orphaned, duplicate,
  stale, hot, unmanaged, and abandoned findings.
- **T4 — Decision context:** identify Project, Agent, purpose, Launch
  Mechanism, expected lifetime, and conservative Safe-to-stop evidence.
- **T5 — System boundary:** Plane explains work, Git explains code, Telemetry
  explains events, and `srvls` explains what should be alive now.

## Executive verdict

The canonical PRD preserves the supplied thesis unusually well. T1 through T5
are directly represented in the Vision, the Runtime Promise lifecycle, Host
discovery, reconciliation vocabulary, Brief, inspection surfaces, safety
guardrails, and system boundaries. The strongest source-derived additions are
honest collection completeness, deterministic compatibility, exact-target
action safety, and bounded local history.

The reconciliation nevertheless does **not** support `prd.md` § 12, “Open
Questions,” which states that no phase-blocking product questions remain. Eight
phase-blocking gaps remain:

1. Provider and sub-source Collection Obligations are modeled but not assigned.
2. Incomplete evidence and lost Heartbeats do not have a complete,
   first-class reconciliation state model.
3. “Runtime Promise” is not explicitly bounded to runtime liveness versus a
   broader testable external outcome.
4. The morning Brief has no canonical evidence-window or accepted-baseline
   semantics.
5. A `safe` Safe-to-stop Assessment has no minimum positive evidence rule.
6. Lifecycle control and inherited TUI/Stack/release scope were promoted into
   MVP without explicit support in the supplied thesis and despite the live
   extract marking them as product decisions.
7. The current smoke test is called a migration oracle even though the live
   extract demonstrates that it is not yet sufficient for that role.
8. The addendum says legacy UX requirements are superseded by a dedicated UX
   contract, but no such artifact exists in the current planning-artifact set.

These gaps do not invalidate the thesis or the PRD's overall direction. They
identify where the canonical documents currently state more certainty than the
named inputs support.

## Coverage matrix

| Input concept | Canonical coverage | Reconciliation judgment |
| --- | --- | --- |
| Morning handoff and reconciliation layer (T1) | `prd.md` § 1, “Vision”; § 2.3, UJ-1 “Jarad receives the morning handoff”; § 4.4, FR-28 “Produce the Brief” | **Covered.** The Vision also preserves the qualitative goal that the Host should stop feeling “haunted.” |
| Agent self-registration of intent and ownership (T2) | `prd.md` § 4.1, FR-1 “Declare a Runtime Promise,” FR-2 “Preserve declaration provenance,” FR-4 “Renew ownership with Heartbeats,” and FR-7 “Expose deterministic Agent contracts” | **Covered.** The machine-facing lifecycle is explicit and retry-aware. Authorization and durable identity mechanics correctly remain downstream concerns, subject to the local trust-domain constraint. |
| Ephemeral-by-default, renewable Leases (T2) | `prd.md` § 3, “Glossary” entries for Heartbeat, Lease, and Runtime Promise; § 4.1, FR-3, FR-4, and FR-6; § 8, NFR-10 and NFR-16 | **Covered with a state-model gap.** The policy exists, but the operator-visible transitions among active, grace, expired, closed, lost-Heartbeat, and abandoned are not complete. |
| Actual Host discovery (T2) | `prd.md` § 4.2, FR-8 through FR-17; § 6.1, “In Scope” | **Substantially covered.** Cron, systemd, Docker, PM2, and direct processes are named. “Actual Host truth” overstates what can be concluded until provider instances, users, daemons, contexts, permissions, and obligations are bounded. |
| Declared versus running truth (T3) | `prd.md` § 3, definitions of Runtime Promise and Observation; § 4.3, FR-18 “Correlate Runtime Promises and Observations”; § 4.4, FR-32 “Inspect intent and truth together” | **Covered.** This is the canonical product model's clearest through-line. |
| What changed (T3) | `prd.md` § 4.3, FR-27 “Detect change through bounded Snapshots”; § 4.4, FR-28; § 6.1 | **Covered in capability, incomplete in semantics.** New, resolved, changed, and persisting items are required, but “since the prior successful Brief” is not enough to define a morning handoff baseline. |
| Lost Heartbeats (T3) | `prd.md` § 2.3, UJ-2; § 4.1, FR-4; § 4.3, FR-25; § 4.4, FR-28 | **Named but only partially modeled.** A surviving runtime after grace can become abandoned, but the canonical outcome for a Promise with a lost Heartbeat during grace, after expiry without an Observation, or under incomplete collection is undefined. |
| Healthy, broken, orphaned, duplicate, stale, hot, unmanaged, and abandoned (T3) | `prd.md` § 3.1, “Reconciliation Finding Vocabulary”; § 4.3, FR-19 through FR-25; § 7, SM-2 | **All eight covered.** The labels are explicitly multi-label. An orthogonal `unresolved` or `out-of-scope` evidence outcome is still missing. |
| Project, Agent, purpose, Launch Mechanism, and expected lifetime (T4) | `prd.md` § 3, “Glossary”; § 4.1, FR-1 and FR-2; § 4.3, FR-26; § 4.4, FR-32 | **Covered.** These fields survive declaration, reconciliation, inspection, and explanation. |
| Conservative Safe-to-stop evidence (T4) | `prd.md` § 3, “Safe-to-stop Assessment”; § 4.3, FR-26; § 4.5, FR-37 and FR-38; § 9.1, “Safety” | **Covered in posture, incomplete in rule.** `unknown` is correctly preferred over unsupported safety, but the minimum evidence needed to emit `safe` is not defined. |
| Plane, Git, Telemetry, and `srvls` boundaries (T5) | `prd.md` § 1, “Vision”; § 4.4, FR-32; § 5, “Non-Goals”; § 10, “Integrations and Dependencies” | **Covered exactly.** External references stay opaque and cannot determine Runtime health. |
| Fragmented control-plane inventory | `source-extract-live-evidence.md` § “Evidence-backed problem framing” → “Fragmented host truth”; `prd.md` § 2.1, “Jobs To Be Done”; § 4.2 | **Covered.** The PRD preserves the current one-view value while expanding discovery to direct Host processes. |
| Honest absence and partial truth | `source-extract-live-evidence.md` § “Visibility is useful only when absence is trustworthy”; `prd.md` § 4.2, FR-14 and FR-17; § 8, NFR-2 and NFR-3 | **Strongly covered at the policy level.** Concrete scope obligations and default automation outcomes remain open. |
| Inventory as an automation surface | `source-extract-live-evidence.md` § “Inventory is both an incident surface and an automation surface”; `prd.md` § 4.2, FR-16 and FR-17; § 8, NFR-7 and NFR-14 | **Covered.** Compatibility is treated as a product contract, though the current verification oracle is overstated. |
| Safe diagnosis-to-action chain | `source-extract-live-evidence.md` § “Acting from the same view raises the safety bar”; `prd.md` § 4.5, FR-36 through FR-41 | **Thoroughly specified, but scope provenance is weak.** Safety behavior is strong if mutation remains MVP; the source extract explicitly left that launch-scope choice unresolved. |
| Promise-to-observation whitespace | `research-current-landscape.md` § “Executive synthesis”; § “Capability and whitespace matrix”; § “Evidence-backed differentiation opportunities” → “Promise-to-observation reconciliation”; `prd.md` § 1 and § 4.3 | **Covered and central.** The PRD avoids positioning `srvls` as a replacement manager or agent control plane. |
| Coverage honesty across authority boundaries | `research-current-landscape.md` § “Coverage honesty as a feature”; `prd.md` § 4.2, FR-14; § 8, NFR-2 | **Conceptually covered, operationally incomplete.** The research names multiple PM2 homes, Docker contexts, rootless scopes, endpoints, and instrumentation boundaries that the PRD does not disposition. |
| Morning delta over another live dashboard | `research-current-landscape.md` § “Morning delta rather than another live dashboard”; `prd.md` § 4.3, FR-27; § 4.4, FR-28 and FR-29 | **Mostly covered.** Attention precedes Stack detail, but the handoff window and operator acceptance point are unspecified. |
| Evidence drill-down without control-plane pretense | `research-current-landscape.md` § “Evidence drill-down without control-plane pretense”; `prd.md` § 4.2, FR-15; § 4.3, FR-26; § 4.4, FR-32; § 9.1 | **Covered.** Reconciliation is read-only and mutation is separately planned and authorized. |
| Stable product vocabulary above provider schemas | `research-current-landscape.md` § “A stable product vocabulary above unstable schemas”; `prd.md` § 3 and § 3.1; § 4.2, FR-13 | **Partially covered.** The vocabulary is stable, but evidence state and anomaly type are not yet cleanly separated. |

## Conflicts and stale-source dispositions

### Resolved or expected staleness

1. `source-extract-live-evidence.md` § “Purpose and boundary” calls itself input
   for a future PRD, and § “Readiness gaps” → “Source-confirmed gate failures”
   says no canonical PRD exists. The current `prd.md` resolves that historical
   absence. Those statements remain valid evidence of the earlier gate; they
   are not current blockers.

2. `source-extract-live-evidence.md` § “Conflicts and staleness” says the legacy
   `FR1` through `FR18` identifiers were non-canonical. `addendum.md` § “Legacy
   Requirement Reconciliation” now maps every legacy FR to canonical `FR-*`
   identifiers. This conflict is resolved for the requirements named in that
   table.

3. `source-extract-live-evidence.md` § “Conflicts and staleness” distinguishes
   today's Python table and `--fzf` behavior from the proposed ratatui default.
   `prd.md` § 4.4, FR-30 makes the change explicit, while § 4.2, FR-16 requires
   an intentional compatibility-ledger disposition. This is a deliberate
   product change, not silent parity, once the ledger entry exists.

### Unresolved conflicts

1. **Current smoke test versus “compatibility oracle.”**
   `source-extract-live-evidence.md` § “Current compatibility contracts” says
   the current smoke suite is useful but is not yet a migration oracle because
   it is Host-dependent, samples only the first JSON item, lacks injected
   Collector failures and mutation coverage, and contains a clean-Host Markdown
   inconsistency. `prd.md` § 0 calls the live Python CLI and smoke test a
   compatibility oracle; § 4.2, FR-16 and § 8, NFR-14 repeat the oracle claim;
   `addendum.md` § “Approved Technical Direction” does the same. The canonical
   set must distinguish the Python behavior oracle, today's partial smoke, and
   the future frozen compatibility corpus.

2. **Mechanism-neutral research versus solution-specific PRD requirements.**
   `source-extract-live-evidence.md` § “Runtime-promise thesis” → “Why this
   thesis matters” classifies Rust, ratatui, grouping, icons, and concurrency as
   implementation or experience choices. `research-current-landscape.md` §
   “Implementation mechanisms explicitly not selected” likewise declines to
   choose language, TUI library, architecture, storage, collection protocol, or
   correlation algorithm. Yet `prd.md` § 4.2, FR-16; § 4.4, FR-29 through
   FR-35; § 4.6, FR-42 and FR-43; § 6.1; and § 8, NFR-15 embed Rust, ratatui,
   exact keybindings, an initial target triple, and release mechanics. Those may
   be valid approved constraints from `addendum.md` § “Approved Technical
   Direction,” but they overreach the named product inputs and contradict
   `prd.md` § 0's claim that implementation mechanisms remain in the addendum
   and architecture.

3. **General expected outcome versus runtime-liveness intent.**
   `research-current-landscape.md` § “What the adjacent products do not
   explain” and § “Candidate product requirements” describe a Promise as a
   testable expected outcome with an evidence condition, or as explicitly
   untestable. `prd.md` § 3 defines a Runtime Promise more narrowly as an
   expectation that a Runtime remain alive until a termination condition. The
   supplied thesis T5 supports the narrower “what should be alive now” meaning.
   The narrowing is defensible, but it is not explicitly recorded as a product
   boundary or non-goal, leaving downstream teams free to implement incompatible
   interpretations.

4. **Research outcome vocabulary versus PRD anomaly vocabulary.**
   `research-current-landscape.md` § “Recommended reconciliation outcomes” uses
   supported, contradicted, unresolved, stale, and out of scope. `prd.md` § 3.1
   instead uses the thesis-required eight labels. The labels are not direct
   substitutes: `duplicate`, `hot`, and `unmanaged` are anomaly dimensions,
   while `unresolved` and `out of scope` describe evidence sufficiency. The PRD
   uses “unknown evidence” in § 4.3, FR-20 and partial states in § 4.4, FR-34,
   but never defines a first-class per-Promise outcome for those cases.

5. **Dedicated UX contract claimed but absent.**
   `source-extract-live-evidence.md` § “Readiness gaps” → “Source-confirmed gate
   failures” records the missing dedicated UX artifact. `addendum.md` § “Legacy
   Requirement Reconciliation” says `UX-DR1` through `UX-DR8` are superseded by
   “the dedicated UX contract.” The current `_bmad-output/planning-artifacts`
   inventory contains no UX artifact. This report does not perform or modify UX
   work; it records that the addendum's present-tense claim is not yet true.

6. **“Actual Host truth” versus bounded authority scopes.**
   `research-current-landscape.md` § “The operator questions and today's nearest
   answers,” § “Coverage honesty as a feature,” and § “Terminology risks” show
   that inventory is always scoped by manager, user, daemon, context, endpoint,
   credentials, and instrumentation. `prd.md` § 1 and the title of § 4.2 use
   “actual Host truth” while § 4.2, FR-14 only defines the obligation mechanism,
   not the v1 obligation assignments. The absolute wording is not earned until
   scope is explicit.

## Qualitative gains and losses

### Qualitative intent retained

- **The Host should stop feeling haunted.** `prd.md` § 1 retains the emotional
  operator outcome and immediately grounds it in an inspectable Brief.
- **Honesty beats apparent completeness.** `prd.md` § 2.1, § 4.2, FR-14 and
  FR-17, and § 8, NFR-2 preserve the strongest qualitative lesson from
  `source-extract-live-evidence.md` § “Visibility is useful only when absence is
  trustworthy.”
- **Provenance must survive summary.** `prd.md` § 4.1, FR-2; § 4.3, FR-18 and
  FR-26; and § 4.4, FR-32 preserve source, identity, conflicts, and drill-down.
- **Reconciliation is not orchestration.** `prd.md` § 5 and § 9.1 preserve the
  distinction emphasized by `research-current-landscape.md` § “Process-supervisor
  conclusion” and § “Evidence drill-down without control-plane pretense.”
- **Plane, Git, and Telemetry remain themselves.** `prd.md` § 1 and § 10 retain
  T5 without attempting to ingest those systems as a new source of runtime
  truth.

### Qualitative intent weakened or lost

1. **“Morning” becomes a generic previous-run delta.** The landscape's bounded
   handoff window, unresolved questions, and operator decision queue in
   `research-current-landscape.md` § “Morning delta rather than another live
   dashboard” are reduced to “since the prior successful Brief” in `prd.md` §
   4.3, FR-27. Repeated automated or exploratory refreshes could erase the
   human morning boundary.

2. **Outcome-first framing is diluted by solution scope.** The live extract's
   runtime trust loop in `source-extract-live-evidence.md` § “Runtime-promise
   thesis” is surrounded in the PRD by Rust migration, ratatui interaction,
   keybindings, lifecycle mutation, installation, and rollback requirements.
   These may be needed, but their volume makes the morning reconciliation wedge
   less dominant than it is in T1 and in `research-current-landscape.md` §
   “Positioning implications.”

3. **Coverage honesty lacks a concrete scope narrative.** The PRD names
   Collector outcomes but does not tell the Operator which users, manager
   instances, daemons, contexts, or endpoints count as the Host. That loses the
   research's repeated warning that absence is always scoped.

4. **Safe-to-stop is conservative in tone but thin in substance.** The PRD
   correctly refuses to guarantee safety, yet it does not preserve the
   landscape's question from `research-current-landscape.md` § “What the
   adjacent products do not explain”: what adjacent manager can recreate,
   restart, or still depend on the target?

5. **The operator-impact measure is absent.** `source-extract-live-evidence.md`
   § “Executive evidence finding” says no source establishes incident
   frequency, time saved, acceptable refresh latency, or adoption. `prd.md` § 7
   converts requirements into fixture pass conditions, but it does not define
   whether the morning handoff materially reduces reconstruction effort or
   unsafe action.

6. **Current and target product states remain easy to conflate.**
   `source-extract-live-evidence.md` § “Conflicts and staleness” requires an
   explicit today/target split. `prd.md` is a target contract, but present-tense
   statements such as “`srvls` collects” can be misread as live capability when
   Runtime Promises, direct-process discovery, ratatui, and safe action
   verification do not exist in the current Python implementation.

## Missing and overreaching requirements

### Missing requirements or decisions

1. **Concrete coverage policy.** No canonical table assigns `required`,
   `optional`, or `not-applicable` to the v1 cron sources, system/user systemd
   managers, Docker daemon or context, PM2 user and `PM2_HOME`, and direct
   process scopes. The mechanism exists in `prd.md` § 3 and § 4.2, FR-14, but
   the decision requested by `source-extract-live-evidence.md` § “PRD decision
   queue,” item 6, remains open.

2. **Complete reconciliation state model.** The PRD needs an orthogonal result
   for insufficient, stale, or out-of-scope evidence and visible Lease/
   Heartbeat lifecycle states. Without it, an active Promise that is neither
   provably healthy nor provably broken has no canonical result. Evidence:
   `prd.md` § 3.1; § 4.3, FR-19, FR-20, and FR-25; and
   `research-current-landscape.md` § “Recommended reconciliation outcomes.”

3. **Runtime Promise semantic boundary.** The canonical set must say whether a
   Promise asserts only runtime presence/liveness or can carry an arbitrary
   semantic postcondition. T5 and `prd.md` § 3 favor liveness; the broader model
   appears in `research-current-landscape.md` § “Candidate product
   requirements,” item 2.

4. **Morning evidence window and baseline acceptance.** `prd.md` § 4.3, FR-27
   needs product semantics for window start/end, timezone, first run, incomplete
   runs, manual versus scheduled refresh, and which baseline an Operator has
   accepted. This follows `research-current-landscape.md` § “Morning delta
   rather than another live dashboard” and § “Candidate product requirements,”
   item 1.

5. **Minimum Safe-to-stop rule.** `prd.md` § 4.3, FR-26 needs to require the
   minimum positive evidence for `safe`, including active or historical intent,
   Lease and Heartbeat state, identity freshness, Durable Ownership, Launch
   Mechanism restart or recreation behavior, dependency evidence, resource
   activity, and relevant Collector completeness. Otherwise different
   implementations can all claim conformance while producing materially
   different safety decisions.

6. **Explicit MVP scope disposition.** The owner must confirm whether
   Stack-first ratatui exploration, start/stop/restart/disable-or-delete,
   compatibility-led Rust replacement, and atomic release/rollback are all part
   of the first product slice or are inherited roadmap constraints. The live
   extract leaves grouping, mutation, interaction, and release scope in
   `source-extract-live-evidence.md` § “Candidate requirement concepts” and §
   “PRD decision queue”; the supplied thesis T1 through T5 does not select those
   mechanisms.

7. **Compatibility-oracle construction.** `prd.md` § 4.2, FR-16 should not
   allow today's smoke pass alone to satisfy migration compatibility. The
   requirement must distinguish a source behavior inventory, a deterministic
   fixture corpus, live-Host smoke, injected partial-failure cases, mutation
   safety cases, and named deployed consumers, consistent with
   `source-extract-live-evidence.md` § “Current compatibility contracts.”

8. **Additional Provider disposition.** Supervisor, Process Compose, Podman,
   CRI, multiple Docker contexts, multiple PM2 homes, and other user scopes are
   documented boundaries in `research-current-landscape.md` §§ 2 and 3. They do
   not need to enter MVP, but `prd.md` § 5 or § 6.2 should explicitly classify
   them as unsupported or deferred so “Host truth” cannot imply coverage.

### Requirements that overreach the named inputs

1. **Solution technology inside the product contract.** Rust, ratatui, exact
   TUI keys, `--fzf` migration, target triple, checksum/staging mechanics, and
   atomic activation are solution constraints in `prd.md` § 4.2, FR-16; § 4.4,
   FR-30, FR-31, and FR-35; § 4.6; § 6.1; and § 8, NFR-15. They are supported by
   `addendum.md` § “Approved Technical Direction,” but not by T1 through T5 or
   the mechanism-neutral landscape research. Their presence also conflicts with
   `prd.md` § 0's stated document boundary.

2. **Lifecycle control as a core launch feature.** `prd.md` § 4.5, FR-36 through
   FR-41 and § 6.1 make mutation part of MVP. The live evidence strongly supports
   the safety chain if mutation exists, but `source-extract-live-evidence.md` §
   “Product-evidence gaps not to fill by invention” and § “PRD decision queue”
   explicitly say launch scope was unconfirmed. T4 requires conservative
   Safe-to-stop evidence, not in-product mutation.

3. **Stack-first presentation as a product invariant.** `prd.md` § 4.4, FR-29
   makes automatic Stack grouping the default after attention. The research
   supports layer-aware correlation as an opportunity, while
   `source-extract-live-evidence.md` § “Candidate requirement concepts” says its
   launch essentiality and operator correction model still require validation.

4. **“All Host truth” implications from a fixed Provider set.** `prd.md` § 4.2
   and § 6.1 add direct processes but omit the other manager and scope
   boundaries identified by the landscape. The fixed set is a reasonable MVP;
   the overreach is the absolute truth wording, not the act of scoping.

## Terminology drift

| Term | Drift across inputs | Required disposition |
| --- | --- | --- |
| Runtime Promise | T1/T2/T5 and `prd.md` § 3 mean a renewable declaration that a Runtime should be alive. `research-current-landscape.md` § “Terminology risks” and § “Candidate product requirements” use a broader testable expected outcome. | Canonically choose liveness-only or general outcome evidence. If liveness-only, state that boundary and keep business/tool outcomes out of v1. |
| Host truth | `prd.md` §§ 1 and 4.2 use “actual Host truth.” The landscape repeatedly shows manager-, user-, daemon-, context-, endpoint-, permission-, and instrumentation-bounded evidence. | Prefer “fresh Host observations within declared coverage” in downstream language; never let unscanned scope appear absent. |
| Reconciliation | The landscape warns that Kubernetes usage implies an active controller. The PRD combines read-only comparison with separately invoked lifecycle controls. | Preserve `prd.md` § 9.1's separation in UX and APIs; a finding must never imply automatic remediation. |
| Healthy | T3 requires the label. `research-current-landscape.md` § “Terminology risks” warns that healthy can mean liveness, readiness, resource state, or business success. The PRD also collects Provider-native health. | Qualify it as Runtime-Promise reconciliation health and retain Provider health as separate evidence. |
| Broken | T3 requires the label, while the research prefers “contradicted” for an evidence outcome. | Define broken as an active liveness Promise contradicted by complete-enough evidence, not a claim that the Project or external outcome failed. |
| Unknown / unresolved / out of scope | `prd.md` § 4.3, FR-20 uses unknown evidence; § 4.4, FR-34 uses partial and unavailable UI states. The research makes unresolved and out of scope first-class outcomes. | Add a canonical evidence-status axis so missing coverage cannot leave a Promise unclassified. |
| Orphaned / unmanaged / abandoned | `prd.md` § 3.1 defines three potentially coexisting conditions based on missing Promise, missing Durable Ownership, and expired ownership. The landscape does not use this taxonomy. | Specify evaluation order and evidence prerequisites while preserving multi-label output. In particular, define how Agent origin is established for an unmanaged Observation with no active Promise. |
| Agent / Owner / Durable Ownership | The landscape's “Agent” can be an SDK object, service, worker, persona, or human; the PRD uses a supplied actor identity and separately defines Owner. | Keep stable actor identity, display label, authority, and durable owner distinct in machine contracts. Do not equate a self-supplied label with authorization. |
| Verified | The landscape prefers “supported by fresh evidence” because verified can sound absolute. The PRD uses verified primarily for post-action outcomes. | Keep verified scoped to a named postcondition, source, time, and Snapshot generation; do not reuse it for general semantic success. |
| Brief / handoff | The research defines a bounded operator briefing. The PRD defines a point-in-time Brief but deltas from a prior successful Brief. | Define the accepted handoff baseline and evidence window so scheduled refreshes do not redefine “morning.” |
| Stack | The PRD makes Stack a deterministic grouping with confidence and evidence. The sources treat grouping as a candidate correlation mechanism. | Keep Stack read-only and evidence-bearing; explicitly defer or define operator correction and persistent override behavior. |

## Phase-blocking gaps

| ID | Gap | Why it blocks the next planning phases | Closure evidence required |
| --- | --- | --- | --- |
| PB-1 | Provider/sub-source coverage obligations are unassigned | UX cannot truthfully render absence, architecture cannot implement completeness reduction, and epics cannot test healthy/broken/orphaned behavior without knowing which scopes count. | A canonical v1 scope-and-obligation table covering provider instances, users, daemons/contexts, permissions, unavailable tooling, and Promise-referenced scopes. |
| PB-2 | Reconciliation and Lease/Heartbeat states are incomplete | An active Promise under partial evidence or lost-Heartbeat grace can be neither healthy nor broken and has no defined first-class outcome. Domain, Brief, filtering, and acceptance fixtures would diverge. | An orthogonal model for Promise lifecycle, evidence sufficiency, reconciliation outcome, and multi-label anomalies, including lost-Heartbeat transitions and retention. |
| PB-3 | Runtime Promise semantic boundary is implicit | A liveness declaration and an arbitrary external-outcome check require different schemas, collectors, UX, and success criteria. T5 favors one, while the research proposes the other. | An explicit canonical statement selecting liveness-only or general testable outcomes, with the rejected interpretation made a non-goal or deferred scope. |
| PB-4 | Morning window and accepted baseline are undefined | Snapshot storage, delta computation, scheduled collection, refresh behavior, and the primary UX narrative depend on what “overnight” and “since last handoff” mean. | Rules for window, timezone, baseline acceptance, first run, incompatible baseline, incomplete run, scheduled run, and manual refresh. |
| PB-5 | Positive Safe-to-stop evidence is undefined | The user thesis makes conservative stop evidence central. Without minimum evidence, UX can show incompatible safety judgments and action epics cannot have stable acceptance criteria. | A product-level decision table or invariant list that makes `safe`, `unsafe`, and `unknown` reproducible and includes manager recreation/dependency and collection-completeness evidence. |
| PB-6 | MVP includes unconfirmed inherited solution and mutation scope | UX, architecture, and epics would spend substantial effort on Stack inference, ratatui control, mutation, and release mechanics that T1–T5 do not require and the live extract left open. | Explicit owner disposition for each: core MVP, compatibility constraint, later phase, or non-goal. Safety requirements remain mandatory for any retained mutation. |
| PB-7 | Compatibility oracle is internally contradictory | Epics cannot define replacement acceptance when the canonical documents call a demonstrably incomplete smoke suite sufficient evidence. | A layered compatibility plan naming the present behavior inventory, frozen deterministic corpus, live smoke role, intentional-deviation ledger, and deployed-consumer checks. |
| PB-8 | Addendum references a nonexistent dedicated UX contract | The addendum retires prior UX identifiers in favor of an artifact that is not present, so downstream consumers have no valid UX source. | A dedicated UX contract that traces to the canonical PRD, or corrected addendum wording that leaves the UX source explicitly pending. This report does neither. |

The blocker count is high enough that `prd.md` § 12 should not be treated as a
reliable phase-gate statement. This is a source-input reconciliation finding,
not a replacement implementation-readiness result.

## Non-blocking gaps

| ID | Gap | Why it does not block UX/architecture/epic planning now | Required closure point |
| --- | --- | --- | --- |
| NB-1 | No measured operator outcome | The product contract can be designed from the supplied owner thesis and canonical journeys, but `prd.md` § 7 currently measures fixture conformance rather than reduced reconstruction time, unsafe actions, or morning effort. | Before beta success evaluation, define at least one operator-impact measure without copying current timeout or Host-count observations. |
| NB-2 | No user-facing refresh or action latency target | `prd.md` § 8, NFR-3 requires bounded execution and preserves honest partial truth, so architecture can proceed with budgets. | Before implementation acceptance, set stakes-appropriate refresh, inspection, and action-verification budgets or explicitly approve qualitative bounds. |
| NB-3 | Exact supported Linux baseline is unnamed | One Host and `x86_64-unknown-linux-gnu` are enough to constrain initial architecture. | Before release stories are accepted, record the verified distribution, kernel/glibc assumptions, and supported installation channel. |
| NB-4 | Named compatibility-consumer inventory is incomplete | `prd.md` § 10 names `srvls-metrics`, `srvls-snapshot`, and legacy output formats, which is enough for planning seams. | Before migration cutover, inventory actual timer units, scripts, dashboards, Snapshot destinations, symlink ownership, and rollback location. |
| NB-5 | Automatic Stack correction is not dispositioned | Read-only, inspectable confidence and Ungrouped behavior prevent forced false grouping in v1. | Before final UX acceptance, either define a correction/challenge flow or explicitly defer persistent/manual overrides. |
| NB-6 | Current-versus-target wording is implicit | `prd.md` § 0 establishes that the PRD is a product contract and FR-16 establishes migration, so downstream readers can infer target state. | Before publishing the PRD outside the planning set, add a visible current/target legend or equivalent language. |
| NB-7 | Agent identity and authorization mechanics remain downstream | `prd.md` § 6.1 limits v1 to one local Operator trust domain, avoiding a networked multi-user security model. | Architecture must still distinguish supplied identity, authenticated local principal, Owner authority, and idempotency identity before Agent APIs are implemented. |

## Final reconciliation judgment

The supplied thesis is not the weak part of the canonical PRD. Its essential
spine is present and traceable: Agent-declared, ephemeral Runtime Promises;
renewable ownership; independent Host discovery; declared-versus-observed
reconciliation; the required finding vocabulary; a change-focused morning
Brief; conservative Safe-to-stop evidence; and crisp Plane/Git/Telemetry
boundaries.

The remaining risk comes from three kinds of drift:

1. **certainty drift** — scoped evidence is called Host truth before scope and
   incomplete-evidence outcomes are fully defined;
2. **scope drift** — prior Rust/ratatui/Stack/control/release plans became MVP
   product requirements without explicit support from the supplied thesis; and
3. **artifact drift** — the smoke suite and dedicated UX contract are described
   as stronger or more complete than current evidence supports.

Resolve PB-1 through PB-8 before treating the PRD as safe input to downstream
phase work. Preserve the current thesis spine while doing so; the reconciliation
does not support weakening the morning handoff, Agent provenance, ephemeral
Lease, evidence honesty, or conservative safety commitments.
