---
title: "srvls: Runtime Promise Reconciliation and Morning Handoff"
status: draft
created: 2026-07-16
updated: 2026-07-16
---

# PRD: srvls Runtime Promise Reconciliation and Morning Handoff

## 0. Document Purpose

This PRD is the canonical target-state product contract for `srvls`. It defines why the product exists, the operator and Agent outcomes it must deliver, and the stable Functional Requirement (`FR-*`) and Non-Functional Requirement (`NFR-*`) identifiers consumed by UX, architecture, epics, stories, and implementation-readiness assessment. Earlier requirement identifiers in `_bmad-output/planning-artifacts/epics.md` were planning candidates without a PRD source; their reconciliation is preserved in `addendum.md`.

The current product is the checked-in Python inventory CLI. Runtime Promises, direct-process discovery, reconciliation, the TUI, verified actions, and release automation described here are target behavior unless explicitly labeled as a current compatibility contract. Product-visible behavior and owner-approved brownfield constraints remain in this PRD; internal implementation mechanisms remain in `addendum.md` and the architecture artifact.

The PRD is grounded in the supplied runtime-promise thesis, the live Python behavior inventory, the current smoke suite, the owner-approved migration and interaction direction, and the 2026-07-15 readiness findings. The current smoke suite is integration evidence, not a sufficient migration oracle by itself; FR-16 defines the layered oracle that must exist before replacement.

## 1. Vision

`srvls` is the morning handoff and reconciliation layer for runtime promises created by humans and autonomous Agents on a Linux Host. It combines declared intent—what an Agent says should remain alive, why, for whom, and until when—with fresh scoped Host Observations—what the declared Collection Obligations actually found.

The product makes a machine stop feeling haunted. In one Brief, an Operator can see what Agents created overnight, what changed, what should be running, what is actually running, what is missing, what is unexplained, which Heartbeats were lost, and what is duplicated, stale, abandoned, unmanaged, or resource-hot. Each finding carries Project, Agent, purpose, Launch Mechanism, expected lifetime, evidence, and a conservative Safe-to-stop Assessment.

Plane remains the source for intended work, Git remains the source for code changes, and Telemetry remains the source for events and measurements. `srvls` owns a narrower question: what should be alive now, why, who owns it, and where is it actually running?

### 1.1 Why Now

Agentic development increases the rate at which short-lived servers, workers, tunnels, timers, containers, and process-manager entries are created. Existing supervisors report their own resources, but they do not preserve the Agent's cross-provider promise or reconcile that promise after the Agent exits. Ephemeral-by-default leases turn forgotten runtime intent into an explicit, reviewable state instead of permanent machine folklore.

## 2. Target User

The primary v1 user is a solo builder-operator who runs multiple projects and Agents on one Linux Host and needs a trustworthy handoff without reconstructing state from cron, systemd, Docker, PM2, process listings, logs, and Agent transcripts. Agents are secondary machine users: they declare, renew, inspect, and release Runtime Promises through deterministic non-interactive contracts.

### 2.1 Jobs To Be Done

- When beginning a work session, understand overnight runtime changes and attention items from one Brief.
- When an Agent starts something that must outlive its immediate command, preserve purpose, ownership, lifetime, and termination intent.
- When Host behavior is surprising, distinguish declared-but-missing work from unexplained, duplicate, stale, hot, unmanaged, or abandoned work.
- Before stopping anything, understand its Project, Agent, purpose, Launch Mechanism, current identity, dependencies, and Safe-to-stop Assessment.
- When a Provider is unavailable or evidence is incomplete, know exactly what `srvls` could not prove instead of receiving false confidence.
- When upgrading `srvls`, preserve existing automation and recover quickly if validation fails.

### 2.2 Non-Users in v1

- Multi-tenant enterprise fleets requiring centralized identity, policy, and remote orchestration.
- Teams seeking a replacement for systemd, cron, Docker, PM2, Plane, Git, or a Telemetry platform.
- Operators who want unattended policy-based deletion or broad stack-wide mutation.
- Non-Linux desktop and server operators.

### 2.3 Key User Journeys

#### UJ-1: Jarad receives the morning handoff

- **Persona + context:** Jarad is a solo builder-operator returning after several Agents worked overnight.
- **Entry state:** He opens `srvls` in an interactive terminal on the Host.
- **Path:** The Brief first summarizes changes and attention counts, then presents Project and Stack groups. Jarad expands a Project, filters to abandoned and broken findings, and inspects the evidence behind one item.
- **Climax:** Without opening five Provider tools, he can answer what changed, what should be alive, what is actually alive, and which findings need action.
- **Resolution:** He leaves healthy work alone and opens the exact Runtime Promise or Observation behind each attention item.
- **Edge case:** A Provider timed out; the Brief remains usable but labels the affected result incomplete and does not claim the Host is clean.

#### UJ-2: An Agent declares and renews an overnight runtime

- **Persona + context:** Ava is an autonomous coding Agent starting a Project development server that must survive until morning review.
- **Entry state:** Ava has the Project identity, purpose, Launch Mechanism, runtime locator, and expected lifetime.
- **Path:** Ava declares a Runtime Promise, receives its Promise ID and Lease expiry, launches the Runtime, sends Heartbeats while responsible, and records an opaque Plane or Git reference when useful.
- **Climax:** The Runtime appears as healthy once the Promise and Observation reconcile.
- **Resolution:** Ava either releases the Promise when done or leaves an explicit expiring Lease for morning review.
- **Edge case:** Ava exits without release; renewal stops, the Lease expires, and a surviving Observation becomes abandoned rather than silently persistent.

#### UJ-3: Jarad diagnoses a broken promise

- **Persona + context:** Jarad expects a Project worker to be alive, but its Runtime Promise has no matching Observation.
- **Entry state:** The Brief shows a broken finding and the last Heartbeat.
- **Path:** Jarad inspects the declared purpose, Launch Mechanism, expected lifetime, last renewal, collector completeness, and candidate near-matches.
- **Climax:** He can distinguish a true missing Runtime from a collector failure or identity mismatch.
- **Resolution:** He starts the exact supported resource through the contextual Action Menu or returns to the owning Project with evidence.

#### UJ-4: Jarad removes an abandoned runtime safely

- **Persona + context:** A development server survived after its ephemeral Runtime Promise expired.
- **Entry state:** The finding is abandoned with an Observation, expired Lease, prior Owner, and Safe-to-stop Assessment.
- **Path:** Jarad inspects the evidence, opens the contextual Action Menu, reviews the resolved Provider-native operation, confirms the exact identity, and executes the action.
- **Climax:** `srvls` revalidates identity, performs the scoped action, refreshes truth, and reports verified success or an explicit non-success outcome.
- **Resolution:** The Observation disappears and the audit history records what happened without deleting unrelated Promise history.
- **Edge case:** Identity changed between inspection and execution; `srvls` refuses the stale action.

#### UJ-5: Jarad triages duplicate and hot runtime findings

- **Persona + context:** Two Observations match a single Runtime Promise and one exceeds a configured resource threshold.
- **Entry state:** The Brief displays duplicate and hot findings together rather than collapsing them into one ambiguous status.
- **Path:** Jarad compares stable identities, start times, resource evidence, Agent provenance, and the expected instance count.
- **Climax:** He can identify the intended instance and understand why the other is a duplicate candidate.
- **Resolution:** He acts on one exact Observation or defers when the Safe-to-stop Assessment is unknown; group-wide mutation is unavailable.

#### UJ-6: Jarad upgrades and recovers

- **Persona + context:** Jarad installs a new `srvls` binary while existing timers consume its machine-readable output.
- **Entry state:** A previous version is installed and known-good.
- **Path:** The installer stages the new version, verifies its checksum, runs the compatibility smoke, atomically activates it, and validates scheduled consumers.
- **Climax:** The upgrade either proves compatible or automatically preserves a clear rollback path.
- **Resolution:** Jarad runs the new version or restores the previous target without reconstructing the installation manually.

## 3. Glossary

- **Action Menu** — Contextual TUI surface listing only lifecycle actions supported for the selected Observation. Opened with `a`.
- **Action Outcome** — Canonical terminal result of one lifecycle operation: `verified`, `executed-unverified`, `refused`, `timed-out`, or `failed`. Diagnostics and reason codes are retained metadata, not additional terminal outcomes.
- **Agent** — Human-operated or autonomous actor that declares and owns a Runtime Promise. An Agent has a stable supplied identifier and display label.
- **Accepted Baseline** — Snapshot an Operator explicitly accepted as the start of the next Evidence Window. Ordinary refreshes do not advance it.
- **Brief** — Point-in-time morning handoff containing an Evidence Window, change summary, reconciliation findings, completeness, and drill-down paths.
- **Collector** — Provider-specific read adapter that emits Observations and explicit collection diagnostics.
- **Collection Obligation** — Per-Provider or per-source policy of `required`, `optional`, or `not-applicable` used to decide whether missing evidence makes a Brief incomplete.
- **Durable Ownership** — An Owner and Launch Mechanism expected to remain valid beyond the creating Agent's session, such as a managed systemd unit with an accountable Project.
- **Evidence Status** — Orthogonal conclusion about whether evidence for a Runtime Promise is `sufficient`, `incomplete`, `stale`, or `out-of-scope`.
- **Evidence Window** — Closed comparison interval from an Accepted Baseline to the current Snapshot, with timestamps and configured timezone.
- **Heartbeat** — Renewal evidence from an Agent that it still owns an active Runtime Promise.
- **Host** — The single Linux machine observed and controlled by v1.
- **Launch Mechanism** — Provider and invocation context responsible for starting and controlling a Runtime, such as systemd, Docker, PM2, cron, or a direct process.
- **Lease** — Time-bounded validity of an ephemeral Runtime Promise. It expires unless renewed.
- **Observation** — Provider-neutral evidence that a scheduled or running Runtime exists on the Host, with a stable Provider identity and provenance.
- **Operator** — Human using the Brief, CLI, TUI, inspection, and lifecycle controls.
- **Owner** — Accountable Agent or human identity responsible for a Runtime Promise.
- **Promise Lifecycle** — Orthogonal state of a Runtime Promise: `lease-active`, `heartbeat-late`, `lease-expired`, `persistent-active`, or `closed`. Every `closed` state retains exactly one reason: `released`, `completed`, or `revoked`.
- **Project** — Stable supplied identity and display label for the body of work a Runtime supports. External work or code references are optional opaque metadata.
- **Promise ID** — Stable identifier returned when a Runtime Promise is declared.
- **Provider** — Runtime or scheduler surface observed or controlled by `srvls`: cron, systemd, Docker, PM2, or direct Host processes in v1.
- **Reconciliation Finding** — One or more evidence-backed classifications produced by comparing Runtime Promises, Heartbeats, Leases, and Observations. Findings may coexist.
- **Runtime** — Scheduled or running Host resource created for a purpose.
- **Runtime Promise** — Declaration that an Agent, working on a Project, started or expects a Runtime for a purpose and expects its scheduled or running presence to remain true until a termination condition. It includes ownership, lifetime, Launch Mechanism, and provenance. It does not assert arbitrary business or tool outcomes in v1.
- **Safe-to-stop Assessment** — Conservative `safe`, `unsafe`, or `unknown` conclusion with reasons. It is decision support, never a guarantee.
- **Snapshot** — Durable, bounded point-in-time record used to compare Briefs and audit reconciliations.
- **Stack** — Deterministic read-only grouping of related Observations based on Provider-native, Project, source-location, and conservative name evidence.
- **Telemetry** — External event and measurement systems. `srvls` may retain opaque references but does not replace them.

### 3.1 Reconciliation Finding Vocabulary

- **healthy** — An active Runtime Promise has the intended number of matching running Observations and no contradictory evidence.
- **broken** — An active Runtime Promise expects a running Runtime but has no matching running Observation under complete-enough collection.
- **orphaned** — A running Observation has no matching Runtime Promise.
- **duplicate** — More matching Observations exist than the Runtime Promise's intended instance count.
- **stale** — A running Observation lacks recent use evidence under configured policy while not being proven abandoned.
- **hot** — A Runtime exceeds a configured resource threshold or trend rule.
- **unmanaged** — An Agent-created Runtime lacks Durable Ownership or a reliable Launch Mechanism.
- **abandoned** — A running Observation remains after its Runtime Promise Lease expired, ownership Heartbeats were lost beyond grace, or intent was explicitly closed as released, completed, or revoked.

These labels are not mutually exclusive. A Reconciliation Finding retains every applicable label and the evidence for each; presentation may assign an attention rank without discarding labels.

### 3.2 Orthogonal Reconciliation Model

Each active or historically relevant Runtime Promise is evaluated on four axes. Presentation can summarize them, but storage, filters, exports, and acceptance fixtures retain every axis.

| Axis | Canonical values | Rule |
| --- | --- | --- |
| Promise Lifecycle | `lease-active`, `heartbeat-late`, `lease-expired`, `persistent-active`, `closed` | `heartbeat-late` begins when the declared renewal cadence plus grace is missed while the Lease remains valid. A Host boot-ID change expires an ephemeral Lease unless a valid renewal re-establishes ownership. `closed` requires a retained `released`, `completed`, or `revoked` reason. |
| Evidence Status | `sufficient`, `incomplete`, `stale`, `out-of-scope` | Required Collection Obligations must be complete and fresh for `sufficient`. Unsupported or intentionally excluded scope is `out-of-scope`, never apparent absence. |
| Promise Outcome | `healthy`, `broken`, `unresolved`, `inactive` | `healthy` and `broken` require sufficient evidence for active intent. `unresolved` covers active intent whose presence or absence evidence is incomplete, stale, or out-of-scope. Expired or closed intent is `inactive`; a surviving Observation is represented independently by an `abandoned` label. |
| Observation labels | `orphaned`, `duplicate`, `stale`, `hot`, `unmanaged`, `abandoned` | Zero or more labels attach to exact Observations. `healthy` and `broken` remain Promise outcomes while all eight thesis-required terms remain visible in the combined Reconciliation Finding vocabulary. |

Evaluation order is deterministic:

1. Resolve Promise Lifecycle from declaration, renewal cadence, grace, Lease, closure event, boot identity, and time evidence.
2. Resolve Evidence Status from Collection Obligations, Collector outcomes, freshness, and supported scope.
3. Correlate identities only within supported evidence and derive Promise Outcome.
4. Derive every applicable Observation label without using a label as mutation authorization.
5. Calculate attention rank and Safe-to-stop Assessment from the retained axes and evidence.

Expiry, Heartbeat, and closure transitions are explicit:

- A late Heartbeat under a still-valid Lease yields `heartbeat-late`; a matching Observation is not yet abandoned.
- A Lease-expired Runtime Promise has `inactive` Promise Outcome; each fresh matched surviving Observation receives `abandoned` with reason `lease-expired`.
- A Runtime Promise closed as `released`, `completed`, or `revoked` has `inactive` Promise Outcome; each fresh matched surviving Observation receives `abandoned` with that closure reason.
- An inactive Promise with no matched survivor remains inactive history. That absence is asserted only when the relevant Collection Obligations are sufficient.
- An active-intent conclusion that depends on incomplete, stale, or out-of-scope evidence yields `unresolved` rather than healthy or broken. Closed or expired intent remains `inactive`, but incomplete evidence cannot prove that no survivor exists; an `abandoned` label still requires a fresh positive identity match.
- Closure or expiry never constitutes mutation authorization.

## 4. Features and Functional Requirements

### 4.1 Runtime Promise Lifecycle

Agents and Operators can declare intended Runtime state before or immediately after launch, keep ownership current, and close the intent explicitly. This feature realizes UJ-2 and supplies the declared side of every reconciliation.

#### FR-1: Declare a Runtime Promise

An Agent or Operator can declare a Runtime Promise containing Agent, Project, Runtime locator, purpose, Launch Mechanism, expected lifetime or termination condition, Owner, intended instance count, persistence choice, and optional opaque Plane, Git, or Telemetry references.

**Consequences:**

- Missing required identity, purpose, lifetime, or ownership fields produce deterministic field-level errors and no partial record.
- A successful declaration returns a Promise ID and current Lease state in human- and machine-readable forms.

#### FR-2: Preserve declaration provenance

`srvls` records the declaration source, creation time, supplied Agent and Project identities, and subsequent lifecycle events without silently rewriting history.

**Consequences:**

- Corrections create auditable revisions or events associated with the same Promise ID.
- Secrets and unrestricted command output are not required Promise metadata.

#### FR-3: Make Runtime Promises ephemeral by default

A newly declared Runtime Promise receives a finite Lease unless the caller explicitly requests persistent intent.

**Consequences:**

- Omitted persistence never creates an indefinite Runtime Promise.
- The response makes expiry and renewal expectations explicit.

#### FR-4: Renew ownership with Heartbeats

An owning Agent can renew an active Lease and provide a Heartbeat associated with the Promise ID.

**Consequences:**

- Renewal is idempotent for a caller-supplied operation identity.
- Late, unauthorized, malformed, released, or unknown renewals return distinct deterministic outcomes.

#### FR-5: Release, complete, or revoke intent

An authorized Agent or Operator can mark a Runtime Promise released, completed, or revoked with reason and time.

**Consequences:**

- Closing intent does not itself stop a Runtime.
- The closure event retains exactly one reason: released, completed, or revoked.
- On the next refresh, closed intent has inactive Promise Outcome and any fresh matched surviving Observation is abandoned with the closure reason.

#### FR-6: Declare explicit persistent intent

An Agent or Operator can opt a Runtime Promise into persistence only while supplying Durable Ownership and a Launch Mechanism that can be inspected later.

**Consequences:**

- Persistent intent without Durable Ownership is rejected or retained as unmanaged, never treated as healthy by assertion alone.
- Persistent Runtime Promises remain auditable and can be revoked explicitly.

#### FR-7: Expose deterministic Agent contracts

All declaration, query, renewal, release, and validation operations are available non-interactively with deterministic machine-readable responses and exit behavior.

**Consequences:**

- Agents can safely retry idempotent operations and distinguish accepted, refused, stale, conflict, and unavailable outcomes.
- Human-readable diagnostics do not corrupt machine-readable stdout.

### 4.2 Actual Host State Discovery

Collectors discover fresh scoped Host Observations independently of declared intent. A failed Collector reduces evidence sufficiency but never erases successful evidence from other Providers. This feature realizes UJ-1, UJ-3, and UJ-5.

#### FR-8: Collect cron work

`srvls` collects user, root, `/etc/crontab`, and `/etc/cron.d` entries with schedule, command identity, source location, user context, and provenance.

**Consequences:**

- Unavailable or denied sources produce explicit Collector diagnostics.
- Hostile names and command text cannot inject terminal or shell behavior.

#### FR-9: Collect systemd work

`srvls` collects system and user services and timers with full unit identity, enablement, runtime state, health, schedule, and provenance.

**Consequences:**

- System and user scopes remain distinguishable.
- Partial authorization or manager unavailability is represented explicitly.

#### FR-10: Collect Docker work

`srvls` collects containers with immutable identity, runtime state, health, restart policy, image, Compose Project, labels, and working-directory evidence when available.

**Consequences:**

- Container names are display data, not the sole action identity.
- Docker daemon failure does not suppress other Provider results.

#### FR-11: Collect PM2 work

`srvls` collects PM2 processes with stable observed identity, runtime state, restart count, namespace, script, working directory, and start-time evidence.

**Consequences:**

- Reused numeric PM2 identifiers cannot silently target a different process.
- Invalid or unexpected PM2 JSON produces bounded diagnostics rather than a crash.

#### FR-12: Collect direct Host processes

`srvls` collects direct Host process Observations needed to reconcile Agent-created Runtimes that are not owned by cron, systemd, Docker, or PM2.

**Consequences:**

- Observations include PID plus start-time or equivalent birth evidence, executable or command fingerprint, parent evidence, user, and working directory when permitted.
- Kernel threads, `srvls` itself, and Provider-owned child processes are deduplicated or clearly attributed rather than double-counted.

#### FR-13: Normalize Observations

Every Collector emits a Provider-neutral Observation composed from identity, lifecycle, schedule, health, provenance, ownership hints, resource signals, and Provider-specific detail references.

**Consequences:**

- Provider-specific behavior remains available through typed detail without inheritance in the domain model.
- Normalization retains encounter provenance required for deterministic compatibility output.

#### FR-14: Report collection completeness

Each refresh returns Observations together with explicit per-Collector completeness, duration, and diagnostic outcomes.

**Consequences:**

- `complete`, `partial`, `unavailable`, `denied`, `timed-out`, and `invalid-output` remain distinguishable.
- Every Provider scope exposes its Collection Obligation and why it applies; an active Runtime Promise referencing that scope makes it required for reconciliation.
- Reconciliation rules that require absence evidence do not claim certainty when the relevant Collector is incomplete.

##### v1 Collection Obligation policy

| Provider scope | Default obligation | Promotion and failure rules |
| --- | --- | --- |
| Invoking user's crontab | `required` | Missing command, denial, timeout, or invalid parse makes the Brief incomplete. An absent crontab under a successful query is complete empty evidence. |
| `/etc/crontab` and `/etc/cron.d` | `required` | Successful `/etc/cron.d` enumeration is required. Enumeration denial or failure, an unreadable discovered file, or parse failure makes the Brief incomplete. |
| Root crontab | `optional` | Becomes `required` when configured as required or referenced by an active Runtime Promise. Denial is always visible. |
| System systemd manager | `required` | Manager unavailability, denial, or invalid output makes the Brief incomplete. |
| Invoking user's systemd manager | `required` | No running user manager is a visible complete-empty or unavailable outcome according to the manager response, never silently omitted. |
| Other users' systemd managers | `not-applicable` | Unsupported in v1 unless an explicitly configured local scope is added; a Runtime Promise referencing an unsupported scope yields `out-of-scope`. |
| Active local Docker context | `optional` when no CLI, endpoint, containers, or Runtime Promise is detected; otherwise `required` | Detection or an active Runtime Promise promotes the scope to `required`. Additional contexts are excluded unless explicitly configured. |
| Invoking user's default PM2 home | `optional` when neither PM2 nor a PM2 Runtime Promise is detected; otherwise `required` | A discovered PM2 daemon, home, or active Promise promotes the scope. |
| Other users and additional PM2 homes | `not-applicable` | Unsupported in v1 unless explicitly configured; referenced unsupported homes yield `out-of-scope`. |
| Direct processes visible to the local principal | `required` | Process-table failure makes the Brief incomplete. Per-field permission redaction is explicit but does not erase an otherwise stable Observation. |

An active Runtime Promise can promote a supported `optional` scope to `required`; it cannot make an unsupported `not-applicable` scope appear observed. The Brief lists included and excluded users, managers, daemons, contexts, homes, and permission boundaries.

#### FR-15: Inspect bounded Provider detail

An Operator can inspect an Observation's Provider-appropriate status, schedule, provenance, identity, and bounded log or output detail.

**Consequences:**

- Detail is byte- and line-bounded and unsafe terminal controls are sanitized.
- Inspection failures remain local to the selected Observation.

#### FR-16: Preserve compatibility surfaces

The replacement implementation preserves the established Python CLI's flat JSON, Prometheus, Markdown, table, inspection, executable-name, ordering, escaping, arguments, exit behavior, and explicit CLI-action behavior through a layered compatibility oracle unless a deliberate deviation is recorded and tested.

**Consequences:**

- The checked-in Python source and tests are inventoried into explicit behavioral contracts; source text alone is not an executable oracle.
- A frozen deterministic fixture corpus covering every supported Provider, output, argument, ordering and escaping rule, partial-failure policy, and action-safety path must exist before replacement.
- The current live-Host smoke suite validates integration behavior but cannot substitute for the fixture corpus; named deployed consumers receive separate end-to-end checks.
- Every intentional deviation has a compatibility-ledger entry with rationale, version impact, replacement assertion, and affected-consumer disposition.
- New Promise and reconciliation fields use additive or explicitly versioned contracts rather than silently changing legacy consumers.

#### FR-17: Support strict collection policy

`srvls` exposes visible partial-failure diagnostics and a strict mode with deterministic Collector-outcome-to-exit behavior.

**Consequences:**

- Default mode returns usable partial truth with diagnostics.
- Strict mode fails according to documented completeness policy while preserving machine-readable error structure.

### 4.3 Reconciliation and Explainability

`srvls` correlates declared intent with fresh scoped Host Observations and keeps uncertainty visible. Classification is explainable, multi-axis, and conservative. This feature realizes UJ-1, UJ-3, UJ-4, and UJ-5.

#### FR-18: Correlate Runtime Promises and Observations

`srvls` correlates Runtime Promises to Observations using Provider-native stable identities, declared locators, Project and Launch Mechanism evidence, and bounded secondary evidence.

**Consequences:**

- Every match records contributing evidence, conflicts, and confidence.
- Weak name similarity alone cannot establish an action identity or a healthy finding.

#### FR-19: Identify healthy intent

An active Runtime Promise with the intended number of compatible running Observations and sufficient Collector completeness receives a healthy Reconciliation Finding.

**Consequences:**

- Health is not asserted when required Collectors are incomplete or identities conflict.
- Additional hot or stale evidence remains visible alongside health only when logically compatible with policy.

#### FR-20: Identify broken intent

An active Runtime Promise expecting a running Runtime with no matching running Observation receives a broken Reconciliation Finding when absence evidence is complete enough.

**Consequences:**

- Incomplete collection yields `unknown` evidence rather than a false broken conclusion.
- The finding retains last Heartbeat, Lease, Launch Mechanism, and candidate near-match evidence.

#### FR-21: Identify orphaned Observations

A running Observation with no matching Runtime Promise receives an orphaned Reconciliation Finding.

**Consequences:**

- Provider-managed preexisting resources may remain orphaned without being mislabeled Agent-created.
- The Operator can see why no declaration matched and whether collection was complete.

#### FR-22: Identify duplicate Observations

When matching running Observations exceed a Runtime Promise's intended instance count, `srvls` emits duplicate Reconciliation Findings for the excess set without choosing a destructive target silently.

**Consequences:**

- Stable identities, start times, and matching evidence remain visible for comparison.
- Duplicate classification never authorizes group-wide mutation.

#### FR-23: Identify stale Runtimes

`srvls` can classify a running Runtime stale using configured, explainable evidence of non-use or obsolescence.

**Consequences:**

- Missing Telemetry is not automatically proof of staleness.
- The applied policy window and evidence source are part of the finding.

#### FR-24: Identify hot Runtimes

`srvls` can classify a Runtime hot when collected resource evidence crosses configured threshold or trend policy.

**Consequences:**

- The metric, sample time, threshold, and source are displayed.
- A hot label does not imply the Runtime is safe to stop.

#### FR-25: Identify unmanaged and abandoned Runtimes

`srvls` emits unmanaged when an Agent-created Runtime lacks Durable Ownership or a reliable Launch Mechanism, and abandoned when a surviving Observation outlives an ephemeral Lease, lost-Heartbeat grace, or intent explicitly closed as released, completed, or revoked.

**Consequences:**

- Persistent declarations without Durable Ownership remain unmanaged.
- Abandoned findings retain the expiry or closure reason and the historical Promise match.
- Lease expiry alone never stops the Runtime automatically.

#### FR-26: Explain findings and Safe-to-stop Assessment

Every attention-worthy Reconciliation Finding exposes classification rules, identity evidence, contradictory or missing evidence, confidence, ownership, purpose, expected lifetime, Launch Mechanism, and a Safe-to-stop Assessment with reasons.

**Consequences:**

- Insufficient evidence produces `unknown`, not `safe`.
- The assessment is recalculated after refresh and before mutation.

The v1 decision contract is conservative and deterministic:

| Assessment | Required decision rule |
| --- | --- |
| `safe` | The exact Observation identity is fresh; every relevant required Collector is sufficient; no active or persistent Runtime Promise, known dependency, or other declared instance requires it; ownership, purpose, expected lifetime, and Launch Mechanism behavior are known; no Provider restart policy or manager will immediately recreate it; no conflicting operation is in flight; and the target is either released, completed, revoked, or expired, or is the exact excess instance of a duplicate set. |
| `unsafe` | Fresh evidence proves an active or persistent Promise, known dependency, required instance, conflicting operation, or Provider recreation policy makes stopping contrary to declared intent or ineffective. |
| `unknown` | Identity, ownership, purpose, lifetime, dependency, recreation behavior, Collector completeness, or freshness is missing, stale, ambiguous, or contradictory. |

`safe` is scoped to the known runtime-liveness and manager-dependency evidence available to `srvls`; it is not a claim about arbitrary business side effects. Execution still requires FR-37 revalidation and the confirmation policy in FR-38.

#### FR-27: Detect change through bounded Snapshots

`srvls` stores bounded local Snapshots sufficient to report new, resolved, changed, and persisting Runtime Promises, Observations, and Reconciliation Findings within an Evidence Window from an explicitly Accepted Baseline to the current Snapshot.

**Consequences:**

- The Operator can explicitly accept a compatible current Snapshot as the next baseline through the TUI or a deterministic non-interactive command; ordinary refreshes and scheduled candidate Snapshots never advance it.
- The Evidence Window retains the Accepted Baseline timestamp, current Snapshot timestamp, and configured timezone. TUI refreshes keep the start fixed until explicit acceptance.
- A first run states that no baseline exists and does not invent a change set. An incompatible baseline is rejected and requires explicit acceptance of a replacement.
- An incomplete Snapshot is ineligible for baseline acceptance by default. An explicit override records the missing scope, principal, timestamp, and reason in local audit history.
- Retention and deletion are deterministic, configurable, and do not remove the active truth required for reconciliation.

### 4.4 Morning Brief, CLI, and TUI

The Brief is the primary human handoff. It presents attention before detail, keeps the approved Stack-first exploration model, and exposes the same truth through deterministic non-interactive surfaces. This feature realizes UJ-1, UJ-3, UJ-4, and UJ-5.

#### FR-28: Produce the Brief

`srvls` produces a Brief answering what Agents created, what changed, what should be running, what is actually running, what is missing, what is unexplained, which Heartbeats were lost, and what is duplicate, stale, abandoned, unmanaged, or hot.

**Consequences:**

- The summary includes collection completeness and counts without hiding multi-label findings.
- The summary names the Accepted Baseline, current Snapshot, configured timezone, and any baseline-unavailable or incomplete-window condition.
- Every summary item drills down to Runtime Promise, Observation, and evidence detail.

#### FR-29: Organize attention and Stack context

The default TUI presents a concise attention summary followed by deterministic Stack groups, with Project, Agent, Provider, and Reconciliation Finding filters and an explicit Ungrouped section.

**Consequences:**

- Stack labels, membership, confidence, and evidence are inspectable.
- Ambiguous items remain visible in Ungrouped rather than being forced into a Stack.

#### FR-30: Select interactive or non-interactive presentation

`srvls` opens the TUI by default only when both input and output are interactive terminals, while redirected execution retains non-interactive table behavior.

**Consequences:**

- Explicit output flags always select the requested non-interactive format.
- `--fzf` remains a deprecated alias to the TUI while the undocumented `--fzf-lines` surface is removed through the compatibility ledger.

#### FR-31: Navigate and refine the TUI

An Operator can navigate, expand or collapse Stacks, filter, search, refresh, inspect, open help, and return or quit entirely by keyboard.

**Consequences:**

- Focus and selection remain predictable as filters and refreshes change visible rows.
- Refresh does not block navigation and visibly distinguishes fresh, refreshing, and stale content.

#### FR-32: Inspect intent and truth together

The TUI and CLI inspection surfaces show linked Runtime Promise, Heartbeat, Lease, Observation, Project, Agent, Launch Mechanism, reconciliation evidence, and bounded Provider detail.

**Consequences:**

- Unmatched declarations and unmatched Observations remain inspectable independently.
- Opaque Plane, Git, and Telemetry references are displayed as references, not fetched or interpreted as truth.

#### FR-33: Communicate without color or Unicode dependence

Rows and summaries communicate Provider, identity, running state, health, freshness, pending work, and Reconciliation Findings using text plus optional semantic color and icons.

**Consequences:**

- `NO_COLOR`, monochrome, and deterministic ASCII fallbacks preserve meaning.
- Unsafe control characters in untrusted Host data are sanitized before rendering.

#### FR-34: Represent application and terminal states explicitly

Loading, refreshing, stale, partial-failure, unavailable-Provider, empty, filtered-empty, pending-action, verified, executed-unverified, refused, timed-out, failed, and baseline-unavailable states each receive explicit visible treatment, including responsive behavior on small terminals.

**Consequences:**

- Small layouts collapse secondary detail before the primary list or essential status.
- No state is represented only by animation, color, or disappearing content.

#### FR-35: Provide a discoverable Action Menu

Pressing `a` on an actionable Runtime Promise or Observation opens the Action Menu with supported start, stop, restart, and disable or delete operations; direct `s`, `R`, and `x` shortcuts remain where unambiguous, and `?` documents all bindings.

**Consequences:**

- Start has an explicit TUI path from a Runtime Promise even when no running Observation exists.
- Unsupported or unsafe actions are absent or disabled with an explanation.

### 4.5 Safe Runtime Lifecycle Control

Lifecycle control remains exact-target, Provider-scoped, identity-revalidated, and verified. `srvls` assists an Operator; it does not auto-remediate. This feature realizes UJ-3, UJ-4, and UJ-5.

#### FR-36: Plan supported lifecycle actions

`srvls` can plan start from an active Runtime Promise whose Launch Mechanism resolves to a supported Provider target. It can plan stop, restart, and disable or delete for individual systemd, Docker, PM2, and direct-process Observations according to Provider capability. Cron Observations remain read-only in v1.

**Consequences:**

- A plan names the exact target, Provider-native operation, required privilege, expected effect, and unsupported limitations before execution.
- Direct-process support is limited to identity-safe signals and cannot invent a start or restart path without a declared Launch Mechanism.

#### FR-37: Revalidate identity before mutation

Immediately before execution, `srvls` re-collects or verifies the selected Observation's canonical Provider identity, or revalidates the Runtime Promise, absence evidence, and Provider-native start target when no Observation exists.

**Consequences:**

- Stale, reused, missing, or ambiguous identities are refused without mutation.
- Display names, Stack membership, and row position are never action identities.

#### FR-38: Confirm destructive and uncertain actions

The TUI requires confirmation for stop and disable or delete, names the exact Runtime and operation, and includes the current Safe-to-stop Assessment and uncertainty.

**Consequences:**

- PM2 deletion and persistent-scheduler disablement are visibly destructive.
- Unknown safety does not prevent an explicit informed Operator choice, but it cannot be presented as safe.

#### FR-39: Isolate asynchronous operations

Each lifecycle operation has a unique operation identity, captures its source generation, suppresses duplicate submissions, and remains distinct from concurrent refreshes.

**Consequences:**

- An older refresh cannot overwrite newer action-verification truth.
- UI cancellation or navigation does not silently duplicate or misattribute an in-flight operation.

#### FR-40: Verify and report action outcomes

After a lifecycle operation begins, `srvls` refreshes relevant truth and reports exactly one canonical Action Outcome: `verified`, `executed-unverified`, `refused`, `timed-out`, or `failed`.

**Consequences:**

- Command exit alone is not treated as verified state change.
- Machine-readable and TUI outcomes identify the operation, target, evidence, and next safe step.
- Diagnostics and reason codes attach to any outcome without creating aliases such as `completed-with-diagnostic` or `stale`.

The terminal decision order is deterministic:

| Precedence | Action Outcome | Decision rule |
| --- | --- | --- |
| 1 | `verified` | Fresh post-action evidence proves the planned postcondition for the exact target, regardless of command diagnostics. |
| 2 | `refused` | No Provider operation was launched because confirmation, capability, authorization, duplicate-operation, or immediate identity revalidation failed. Pre-execution identity drift uses reason `stale-identity`. |
| 3 | `timed-out` | Provider execution exceeded its hard deadline, termination and reaping were attempted, and the postcondition was not verified within the bounded operation. |
| 4 | `failed` | The Provider invocation could not start, or fresh post-action evidence disproves the planned postcondition. |
| 5 | `executed-unverified` | A Provider operation was launched but the postcondition can be neither proved nor disproved because verification is incomplete, ambiguous, expired, or observes a replacement identity. |

Successful execution with diagnostics remains `verified` when the postcondition is proved. Post-execution replacement uses `executed-unverified` with a replacement reason; it is never reported as pre-execution `stale-identity`.

#### FR-41: Keep groups read-only and privilege scoped

Stack, Project, Agent, and Reconciliation Finding groups remain read-only in v1, and any required privilege is limited to the selected Provider operation.

**Consequences:**

- No group interaction silently widens an action target.
- `srvls` never elevates the entire process or permits an interactive authorization prompt while terminal raw mode is active.

### 4.6 Installation, Automation, and Recovery

The product must replace the Python executable without breaking existing consumers and must leave a reversible path. This feature realizes UJ-6.

#### FR-42: Build and install a verifiable release

`srvls` can be built, versioned, checksum-verified, staged, smoke-tested, and installed as a standalone release artifact for the supported Host target.

**Consequences:**

- Activation occurs only after the staged binary passes required checks.
- The installed binary reports version and compatibility information deterministically.

#### FR-43: Upgrade, validate automation, and roll back

An Operator can atomically upgrade `srvls`, validate existing metrics and Snapshot timer consumers, and roll back to the prior known-good target.

**Consequences:**

- The previous target remains identifiable until the new version and consumers validate.
- Failed validation does not leave a partially replaced executable or an undocumented recovery procedure.

## 5. Non-Goals

- `srvls` is not a scheduler, process supervisor, container runtime, service manager, or remote execution platform.
- `srvls` does not replace Plane, Git, or Telemetry and does not infer runtime truth from those systems.
- v1 does not perform unattended cleanup, policy-based auto-remediation, or lease-expiry termination.
- v1 does not mutate entire Stacks, Projects, Agent groups, or Reconciliation Finding groups.
- v1 does not provide a hosted control plane, web UI, multi-user authorization system, or distributed fleet view.
- v1 does not retain unrestricted logs, command output, secrets, or full-fidelity Telemetry.
- v1 does not guarantee that any Runtime is safe to stop; it provides a conservative evidence-backed assessment.
- The approved replacement does not intentionally redesign established machine-readable contracts without a compatibility-ledger decision.

## 6. MVP Scope

### 6.1 Owner-Approved Inherited Constraints

The Stack-first TUI, safe individual mutation, compatibility-led replacement of the Python CLI with one Rust binary, and supported install, validation, and rollback path are explicit owner-approved brownfield MVP constraints. They are not inferred from the runtime-promise thesis. Product-visible behavior remains specified here; internal mechanisms and library choices remain in `addendum.md` and the architecture artifact.

### 6.2 In Scope

- One Linux Host and one local Operator trust domain.
- Runtime Promise declaration, Lease, Heartbeat, persistence, release, query, and local audit history.
- Discovery across cron, systemd, Docker, PM2, and direct Host processes.
- Explainable reconciliation with all eight required finding labels and lost-Heartbeat evidence.
- Bounded Snapshots and change-since-prior-Brief reporting.
- Interactive terminal Brief following the approved TUI direction plus deterministic table, JSON, Markdown, and Prometheus-compatible legacy outputs.
- Exact-target, confirmed, identity-safe, verified lifecycle actions supported by each Provider.
- Compatibility-led Rust migration, supported release artifact, atomic install or upgrade, automation validation, and rollback.

### 6.3 Out of Scope for MVP

- Remote Hosts or fleet-wide reconciliation; revisit after one-Host coverage and identity contracts are proven.
- Automatic termination after Lease expiry; revisit only with field evidence that conservative review is insufficient.
- Multi-Operator RBAC and remote Agent authentication; revisit with a networked control plane.
- Deep Plane, Git, or Telemetry ingestion; v1 stores optional opaque references only.
- Browser, desktop GUI, and mobile surfaces.
- Windows and macOS Providers.
- Guaranteed discovery of Supervisor, Process Compose, Podman, Kubernetes or CRI, additional Docker contexts, other users' systemd managers, or additional PM2 homes. A deliberately configured scope is supported only when an existing v1 Collector can observe it and reports its obligation honestly.
- Durable manual Stack membership corrections or persistent Operator overrides of inferred Stack membership; v1 exposes evidence, confidence, and Ungrouped items instead.
- Stack-wide or Project-wide lifecycle actions.

## 7. Success Metrics

### Primary

- **SM-1: Complete morning answer set.** In the canonical acceptance scenarios, one Brief answers all eight questions in FR-28 and exposes any incomplete evidence. Validates FR-14 and FR-18 through FR-29.
- **SM-2: Reconciliation correctness.** Every canonical fixture for healthy, broken, orphaned, duplicate, stale, hot, unmanaged, and abandoned produces the specified labels and evidence with no silent false certainty. Validates FR-18 through FR-26.
- **SM-3: Safe action truthfulness.** Every mutation acceptance case ends in exactly one of verified, executed-unverified, refused, timed-out, or failed according to FR-40 precedence; none reports verified success without fresh post-action evidence. Validates FR-36 through FR-41.

### Secondary

- **SM-4: Compatibility closure.** The frozen deterministic compatibility corpus, current live-Host smoke suite, and named deployed-consumer checks pass completely, or each intentional deviation has an approved ledger entry and replacement assertion. Validates FR-16, FR-17, FR-42, and FR-43.
- **SM-5: Agent lifecycle closure.** Canonical Agent scenarios can declare, retry, renew, query, release, and observe Lease expiry deterministically without human parsing. Validates FR-1 through FR-7.
- **SM-6: Explainable operator decisions.** In each core journey fixture, the Operator can reach the evidence and exact target from the Brief without issuing native Provider discovery commands. Provider-native commands are needed only after leaving `srvls` for remediation outside supported capabilities. Validates FR-26, FR-28 through FR-35, and FR-37.

### Counter-Metrics

- **SM-C1: Do not optimize anomaly count.** More findings are not better; false positive or unsupported labels are defects. Counterbalances SM-1 and SM-2.
- **SM-C2: Do not optimize speed by hiding incompleteness.** Faster refreshes cannot convert timed-out or denied Collectors into apparent absence. Counterbalances SM-1.
- **SM-C3: Do not optimize cleanup volume.** Fewer running Runtimes is not a success measure, and broad automatic stopping is prohibited. Counterbalances SM-3.

## 8. Cross-Cutting Non-Functional Requirements

#### NFR-1: Deterministic domain outcomes

Identical normalized inputs, policy, and baseline produce identical ordering, correlation, findings, attention rank, Safe-to-stop Assessment, and machine-readable serialization.

#### NFR-2: Honest partial truth

Collector, storage, inspection, and mutation failures remain explicit and scoped; the product never substitutes missing evidence with success, absence, or safety.

#### NFR-3: Bounded refresh behavior

Collectors run with bounded concurrency, hard subprocess deadlines, bounded output, termination, and unconditional child reaping so one unavailable Provider cannot impose sequential latency or hang the Brief.

#### NFR-4: Host command safety

All Host commands use typed arguments and argv-only execution with safe end-of-options behavior. Provider data is never interpolated into a shell command.

#### NFR-5: Least privilege

Collection and mutation use the least privilege needed for the selected Provider and scope. Whole-process elevation and interactive authorization while terminal raw mode is active are prohibited.

#### NFR-6: Terminal restoration

Raw mode, alternate screen, cursor, input state, and signal handling are restored on normal return, error, panic unwind, Ctrl-C, SIGINT, and SIGTERM paths.

#### NFR-7: Clean machine interfaces

Machine-readable stdout contains no ANSI, icons, progress, logs, or human diagnostics. Ordering, exit policy, encoding, and escaping are deterministic.

#### NFR-8: Accessible terminal communication

Status and focus are understandable without color, Unicode, animation, or a large terminal. Untrusted control characters are sanitized before display.

#### NFR-9: Atomic and durable local state

Runtime Promise, lifecycle event, Snapshot, and compatibility metadata writes are atomic, crash-safe, schema-versioned, and recoverable without accepting a partially written record as truth.

#### NFR-10: Defensible Lease time semantics

Lease duration calculations resist wall-clock rollback; displayed events retain wall time. Host restart, suspend, and clock discontinuity produce explicit revalidation or expiry behavior rather than extending ownership silently.

#### NFR-11: Local data minimization

State is local by default, permission-restricted, bounded by retention policy, and limited to fields needed for ownership, identity, reconciliation, audit, and compatibility. Secrets and unrestricted logs are excluded or redacted.

#### NFR-12: Concurrency correctness

Refresh generations and operation identities prevent stale refresh, late Collector, duplicate action, or concurrent state write from replacing newer truth or misattributing an outcome.

#### NFR-13: Testability without Host mutation

Domain rules, Collectors, correlation, presentations, actions, Lease behavior, and TUI states are verifiable with deterministic fixtures, fakes, goldens, and terminal backends; live-Host tests are opt-in.

#### NFR-14: Brownfield compatibility

The migration oracle is layered: an explicit inventory of established Python behavior, a frozen deterministic fixture and golden corpus, the current live-Host smoke suite, and end-to-end checks for named deployed consumers, including the exact project-owned Prometheus families. Intentional deviations require an explicit ledger entry, version impact, replacement assertion, and consumer disposition.

#### NFR-15: Supported release baseline

The initial release supports `x86_64-unknown-linux-gnu` on the verified Host baseline, a committed dependency lock, reproducible validation, checksum verification, and reversible installation.

#### NFR-16: Configurable policy without hidden defaults

Lease duration, Heartbeat grace, stale policy, hot thresholds, retention, Collector deadlines, and output bounds have documented defaults, validation, and provenance in findings; invalid configuration fails visibly.

## 9. Constraints and Guardrails

### 9.1 Safety

- Reconciliation is read-only; lifecycle actions are separately planned and authorized.
- Lease expiry, orphaned status, abandoned status, and `safe` assessment never trigger automatic mutation in v1.
- Mutation targets exactly one revalidated Observation.
- Unknown evidence remains unknown through the UI, exports, and action flow.

### 9.2 Privacy and Data Governance

- Runtime Promise metadata should identify purpose without requiring source code, prompts, secrets, or full command output.
- Optional Plane, Git, and Telemetry references remain opaque identifiers or links.
- Local history uses bounded retention and explicit deletion behavior.
- Provider output and process command lines are treated as untrusted and potentially sensitive.

### 9.3 Compatibility

- Legacy consumers keep working during the Rust migration.
- New reconciliation schemas are versioned and additive where practical.
- The executable name remains `srvls`.
- Provider identity and output ordering rules are public contracts once released.

## 10. Integrations and Dependencies

- **Linux process and scheduler surfaces:** cron files and commands, system and user systemd managers, Docker daemon CLI or API surface, PM2, and the Host process table.
- **Agent callers:** local deterministic CLI contracts for Runtime Promise lifecycle operations. A network service is not required in v1.
- **Local durable state:** Runtime Promises, lifecycle events, policy/configuration, bounded Snapshots, and compatibility metadata.
- **Existing automation:** `srvls-metrics` and `srvls-snapshot` systemd timer consumers and the established table, JSON, Markdown, and Prometheus outputs.
- **Plane, Git, and Telemetry:** optional opaque references only. Their availability cannot determine Runtime health.

## 11. Risks and Mitigations

| Risk | Product impact | Required mitigation |
| --- | --- | --- |
| Weak correlation creates false confidence | Wrong healthy, orphaned, or safe conclusion | Evidence-weighted matching, explicit confidence, completeness gates, and `unknown` safety |
| Process identity is reused | Mutation targets a different Runtime | Provider-native identity plus birth evidence and immediate revalidation |
| Agents stop renewing unexpectedly | Healthy work appears abandoned | Explicit grace policy, visible last Heartbeat, no automatic stop |
| Provider failure looks like absence | False broken or clean Brief | Per-Collector completeness and absence rules that require sufficient evidence |
| Local state corrupts or drifts | Intent and history become untrustworthy | Atomic schema-versioned writes, validation, recovery, and bounded Snapshots |
| TUI hides uncertainty | Operator acts on misleading presentation | Textual state vocabulary, linked evidence, accessible fallbacks, explicit partial states |
| Migration breaks automation | Existing metrics or snapshots fail | Compatibility corpus, staged smoke, consumer validation, atomic activation, rollback |
| Product expands into orchestration | Safety and scope explode | Non-goals, read-only groups, one-Host MVP, no auto-remediation |

## 12. Open Questions

No phase-blocking product questions remain for UX, architecture, or epic planning. Post-MVP candidates are bounded in Section 6.3 and require new evidence before scope expansion.

## 13. Assumptions Index

No unresolved inline assumptions remain. Fast-path defaults and their rationale are recorded in `.memlog.md`; downstream implementation decisions are isolated in `addendum.md`.
