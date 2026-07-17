---
title: "srvls Canonical Epics and Stories"
type: canonical-epics
status: draft
assignable: false
implementationAuthority: false
stepsCompleted:
  - step-01-validate-prerequisites
  - step-02-design-epics
inputDocuments:
  - _bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md
  - _bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/addendum.md
  - _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/DESIGN.md
  - _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md
  - _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md
retiredArtifact:
  path: _bmad-output/retired-artifacts/epics-pre-canonical-prd-2026-07-15.md
  sha256: 9a256682785733c23fbf017c138115b067ec894fe8b697da75da134905d7effd
  implementationAuthority: false
---

# srvls - Canonical Epic Breakdown

## Authority and Quarantine

This document is the only assignable epic and story decomposition for srvls
once its status and implementationAuthority fields are promoted at workflow
completion. Authority descends in this order: final PRD, final PRD addendum,
final UX DESIGN and EXPERIENCE spines, final architecture spine, then this
decomposition. A story may refine delivery order but may not weaken or rename a
source contract.

The pre-canonical backlog remains byte-preserved at the retiredArtifact path
and digest above, outside the planning-artifact discovery root. It is historical
evidence only. It must not be copied into this document, assigned, used as an
acceptance oracle, or moved back under planning-artifacts.

## Requirements Inventory

### User Journeys

- UJ-1 — Morning handoff: an Operator receives one honest Brief, explores
  attention and Stack context, and drills into evidence even when a Provider is
  incomplete.
- UJ-2 — Agent-owned overnight runtime: an Agent declares, renews, queries, and
  closes finite runtime intent through deterministic machine contracts.
- UJ-3 — Broken-promise diagnosis: an Operator distinguishes true absence from
  Collector failure or identity mismatch and can start an exact supported
  target.
- UJ-4 — Safe abandoned-runtime removal: an Operator inspects evidence,
  confirms one exact target, survives identity races, and receives a verified
  or explicit non-success outcome.
- UJ-5 — Duplicate and hot triage: an Operator retains coexisting findings,
  compares exact instances, and never receives an implicit destructive target.
- UJ-6 — Upgrade and recovery: an Operator stages, validates, activates, and,
  when necessary, restores one known-good binary/state/consumer pair.

### Functional Requirements

- FR-1 — Declare a Runtime Promise with required Agent, Project, locator,
  purpose, Launch Mechanism, lifetime, Owner, count, persistence, and optional
  opaque references; return deterministic field errors or Promise ID and Lease.
- FR-2 — Preserve declaration source, time, supplied identities, revisions, and
  lifecycle history without silently rewriting or collecting unrestricted
  secrets and output.
- FR-3 — Make every new Runtime Promise finite by default and expose expiry and
  renewal expectations.
- FR-4 — Renew ownership with idempotent Heartbeats and distinguish late,
  unauthorized, malformed, closed, and unknown outcomes.
- FR-5 — Release, complete, or revoke intent with exactly one retained reason;
  closing intent never stops a Runtime.
- FR-6 — Permit persistent intent only with Durable Ownership and an
  inspectable Launch Mechanism; otherwise reject it or retain it as unmanaged.
- FR-7 — Expose deterministic non-interactive declare, query, renew, close, and
  validation contracts with clean stdout and retry-safe outcomes.
- FR-8 — Collect user, root, system, and drop-in cron work with schedule,
  command identity, source, principal, provenance, and explicit failures.
- FR-9 — Collect system and user systemd services and timers with full identity,
  enablement, runtime, health, schedule, scope, and provenance.
- FR-10 — Collect Docker containers with immutable identity, runtime, health,
  restart, image, Compose, label, and working-directory evidence.
- FR-11 — Collect PM2 processes with birth-safe identity, state, restarts,
  namespace, script, working directory, and start evidence.
- FR-12 — Collect direct Host processes with PID plus birth evidence,
  executable or command fingerprint, parent, user, and permitted working
  directory while excluding or attributing internal and Provider-owned work.
- FR-13 — Normalize every Provider result into one provider-neutral Observation
  with typed Provider detail and deterministic encounter provenance.
- FR-14 — Report per-scope obligation, completeness, duration, and diagnostics;
  incomplete evidence may not prove absence.
- FR-15 — Inspect bounded, sanitized Provider detail with failures scoped to the
  selected Observation.
- FR-16 — Preserve inherited Python table, flat JSON, Prometheus, Markdown,
  inspection, executable, ordering, escaping, argv, exits, and explicit-action
  behavior through a layered oracle and explicit deviation ledger.
- FR-17 — Support usable partial truth by default and deterministic strict-mode
  exits with machine-readable diagnostics.
- FR-18 — Correlate Runtime Promises and Observations using exact Provider
  identity and bounded supporting evidence while retaining confidence and
  conflicts.
- FR-19 — Identify healthy active intent only with the intended matching
  instance count and sufficient evidence.
- FR-20 — Identify broken active intent only with sufficient absence evidence;
  otherwise retain unresolved truth and near-match evidence.
- FR-21 — Identify orphaned running Observations without claiming that
  preexisting Provider resources are Agent-created.
- FR-22 — Identify every exact excess duplicate Observation without silently
  choosing a destructive target.
- FR-23 — Identify stale Runtimes only from configured, positive, explainable
  non-use or obsolescence evidence.
- FR-24 — Identify hot Runtimes from configured resource samples, thresholds,
  time, and source without implying safety.
- FR-25 — Identify unmanaged and abandoned Runtimes from Durable Ownership,
  Launch Mechanism, Lease, Heartbeat, and explicit closure evidence without
  auto-stopping them.
- FR-26 — Explain classifications, identity, contradictions, missing evidence,
  confidence, ownership, purpose, lifetime, Launch Mechanism, and conservative
  safe, unsafe, or unknown Safe-to-stop Assessment.
- FR-27 — Persist bounded Snapshots and an explicitly Accepted Baseline so new,
  resolved, changed, and persisting truth has one closed Evidence Window;
  refresh never advances the baseline.
- FR-28 — Produce a Brief answering all eight morning questions with
  completeness, baseline, current Snapshot, timezone, multi-label counts, and
  drill-down identities.
- FR-29 — Put attention before deterministic Stack groups, expose Project,
  Agent, Provider, and finding filters, and retain ambiguous items as
  inspectable Ungrouped truth.
- FR-30 — Enter the TUI only for eligible interactive input/output; preserve
  redirected table and explicit formats, deprecate fzf into the TUI, and retire
  fzf-lines only through the ledger.
- FR-31 — Support keyboard navigation, group expansion, filtering, search,
  refresh, inspection, help, return, and quit with stable focus and
  nonblocking refresh.
- FR-32 — Inspect Promise, Heartbeat, Lease, Observation, Project, Agent,
  Launch Mechanism, reconciliation evidence, and bounded Provider detail
  together without treating opaque references as truth.
- FR-33 — Communicate every meaning through text with optional color and glyphs,
  deterministic NO_COLOR and ASCII behavior, and sanitized untrusted content.
- FR-34 — Give explicit treatment to every canonical application, collection,
  baseline, action, and terminal state, including small-terminal behavior.
- FR-35 — Provide a discoverable Action Menu with an explicit Promise-origin
  Start path, documented accelerators, and explained unsupported or disabled
  actions.
- FR-36 — Plan exact supported start, stop, restart, disable, delete, and
  direct-process signal actions; keep cron read-only and never invent a direct
  start path.
- FR-37 — Revalidate exact Provider identity or Promise-origin start evidence
  immediately before mutation and refuse stale, reused, missing, or ambiguous
  targets.
- FR-38 — Confirm stop and destructive operations with exact target, risk, and
  Safe-to-stop evidence; unknown safety requires an informed explicit choice.
- FR-39 — Isolate every operation by ID and source generation, suppress
  duplicate submissions, and prevent refresh races or navigation from
  misattributing it.
- FR-40 — Verify fresh post-action truth and return exactly one canonical
  verified, executed-unverified, refused, timed-out, or failed outcome under the
  specified precedence.
- FR-41 — Keep Stack, Project, Agent, and finding groups read-only and scope
  privilege to one selected Provider operation without raw-mode authorization.
- FR-42 — Build, version, checksum, stage, smoke, install, and identify a
  standalone supported release artifact before activation.
- FR-43 — Atomically upgrade, validate metrics and Snapshot consumers, preserve
  the previous known-good pair, and roll back without partial replacement.

### Non-Functional Requirements

- NFR-1 — Identical normalized input, policy, and baseline produce identical
  domain outcomes, ordering, ranking, safety, and serialization.
- NFR-2 — Every collection, storage, inspection, and mutation failure remains
  explicit and scoped; missing evidence never becomes success, absence, or
  safety.
- NFR-3 — Refresh uses bounded concurrency, deadlines, captures, termination,
  and reaping so one Provider cannot hang or sequentialize the Brief.
- NFR-4 — Host commands use typed argv-only execution, end-of-options safety,
  and no shell interpolation.
- NFR-5 — Collection and mutation use least privilege; whole-process elevation
  and interactive authorization in raw mode are prohibited.
- NFR-6 — Terminal state restores on normal, error, panic, Ctrl-C, SIGINT, and
  SIGTERM paths.
- NFR-7 — Machine stdout is deterministic and contains no ANSI, icons,
  progress, logs, or human diagnostics.
- NFR-8 — Terminal meaning remains accessible without color, Unicode,
  animation, a large terminal, cursor motion, or trusted Host text.
- NFR-9 — Local Promise, event, Snapshot, operation, and compatibility state is
  atomic, crash-safe, schema-versioned, and recoverable.
- NFR-10 — Lease time resists wall-clock rollback and makes restart, suspend,
  and clock discontinuity explicit.
- NFR-11 — Local state is permission-restricted, bounded, minimized, and
  excludes or redacts secrets and unrestricted logs.
- NFR-12 — Generations and operation identities prevent stale refresh, late
  Collector, duplicate action, or concurrent write from replacing newer truth.
- NFR-13 — Domain, adapters, presentation, Lease, actions, and TUI are
  deterministically testable without Host mutation; live tests are opt-in.
- NFR-14 — Brownfield migration uses the explicit inventory, frozen fixture and
  golden corpus, live smoke, deployed-consumer checks, and deviation ledger.
- NFR-15 — The supported release baseline is locked, reproducibly validated,
  checksum verified, ABI bounded, and reversibly installed.
- NFR-16 — Every configurable duration, threshold, retention, deadline, and
  bound has documented default, valid range, provenance, and visible failure.

### Supplemental Success and Counter-Metrics

- SM-1 — One canonical Brief answers all eight morning questions and exposes
  incomplete evidence.
- SM-2 — Canonical fixtures classify all eight required finding terms with no
  unsupported certainty.
- SM-3 — Every mutation fixture ends in exactly one FR-40 Action Outcome and
  never claims verified without fresh evidence.
- SM-4 — Compatibility corpus, live smoke, and named consumer checks close or
  carry an approved deviation.
- SM-5 — Agents deterministically declare, retry, renew, query, close, and
  observe expiry.
- SM-6 — Operators reach exact evidence and action targets without native
  Provider discovery commands.
- SM-C1 — Finding volume is never optimized at the cost of precision.
- SM-C2 — Refresh speed never hides incomplete evidence.
- SM-C3 — Cleanup volume is never a success measure and no broad automatic
  stopping is introduced.

### Architecture Requirements

- AD-1 through AD-3 — Enforce inward dependency direction, distinct domain
  aggregates, inward-owned ports, and one owner for every side effect.
- AD-4 through AD-6 — Make Stack inference evidence-based, Snapshot truth
  scoped, and every mutation a durable exact-target Command.
- AD-7 through AD-9 — Route profiles before side effects, keep meaning
  decoration-independent, and separate frozen compatibility from versioned new
  contracts.
- AD-10 — Compile one bounded deterministic DispatchSchedule with immutable
  epochs, half-open cuts, latest-wins generations, bounded capture, and a
  separate action pool.
- AD-11 — Wire every deterministic fixture family and required future
  implementation matrix into one aggregate architecture-contract gate before
  its owning story can pass.
- AD-12 — Ship one Rust 2024 binary with MSRV 1.88, symbolic stable evidence,
  locked dependencies, glibc 2.42 ABI proof, checksum, and reversible paired
  state/consumer delivery.
- AD-13 through AD-15 — Use byte-total typed identities and diagnostics,
  generation-bound self-process suppression, one terminal/shutdown owner, and
  narrow explicit privilege.
- AD-16 through AD-19 — Make SQLite the sole durable truth owner, use explicit
  Promise events and defensible time, run one pure reconciliation engine, and
  retain typed configuration provenance.
- AD-20 — Implement ARCH-LIM-1 through ARCH-LIM-24 exactly, including derived
  bounds and visible provenance.
- AD-21 — Admit one atomic CollectionPlan that freezes Promise, policy, scope,
  schedule, baseline, operation, resource-history, and prior-current cuts and
  performs no later truth lookup.
- AD-22 — Persist immutable ActionPlan and launch/verification handoffs so one
  OperationCoordinator owns FR-40 terminal truth.
- AD-23 — Quiesce all stateful work behind process-associated POSIX admission
  locks and execute release, validation, owner takeover, KnownGood publication,
  FirstInstall recovery, and explicit rollback as one crash-recoverable
  transaction.
- AD-24 — Use the closed canonical JSON, binary identity, policy, plan,
  Snapshot, baseline, release, and fingerprint grammars for current and
  historical authority.
- AD-25 — Run each Collector through the authenticated same-binary FD3 protocol
  with exact descriptor ownership, peer proof, framing, size, identity,
  diagnostic, EOF, cleanup, and report rules.
- ARCH-LIM-1 through ARCH-LIM-24 — Preserve every published default, inclusive
  valid range, derived formula, cutoff, capacity mode, and action/release bound
  as a typed, visible, tested policy contract.
- ARCH-HOST-1 — Run UX budgets on the constrained four-vCPU, 8-GiB,
  x86_64 GNU/Linux glibc-2.42 deterministic profile for 30 post-warm-up
  iterations and record all named environment and fixture evidence.
- Structural seed — The first Rust commit supplies the prescribed crate/module
  layout, private-by-default boundaries, Cargo.lock, architecture-boundary
  test, and aggregate gate; Provider implementation cannot precede it.

### UX Design Requirements

#### Foundation and Voice

- UX-FND-1 through UX-FND-6 — One terminal product, orthogonal truth, exact
  identity, honest partial evidence, no automatic cleanup, and explicit
  compatibility ownership.
- UX-VT-1 through UX-VT-4 — Calm exact language, canonical vocabulary, explicit
  time/provenance, and one safe recovery instruction for every non-success.

#### Information Architecture

- UX-IA-1 through UX-IA-10 — Brief, Explorer, runtime detail, Provider/evidence
  detail, filter, Action Menu, baseline, help, release/recovery, and
  Agent/machine surfaces with explicit entry and exit paths.
- UX-IA-11 — Deterministic query/facet composition, visible constraints,
  filtered-empty recovery, and refresh persistence.
- UX-IA-12 — Pre-side-effect configuration errors and valid policy detail show
  field, value/redaction, source, type, range, precedence, default, and repair.

#### Components

- UX-CP-1 through UX-CP-16 — Implement the exact brief-summary,
  completeness-banner, attention-row, group-row, runtime-detail,
  evidence-table, provider-detail, filter-bar, action-menu,
  confirmation-dialog, operation-status, baseline-dialog, help-overlay,
  finding-marker, machine-result, and install-phase contracts shared with
  DESIGN.md.

#### States and Interaction

- UX-ST-1 through UX-ST-18 — Render every loading, refreshing, stale, partial,
  unavailable, empty, filtered-empty, action, outcome, identity-race, baseline,
  bounded-detail, and invalid-config state explicitly.
- UX-ST-19 — Preserve focus by exact identity with deterministic fallback.
- UX-ST-20 — Keep controls conservative for unsupported, unsafe, unknown,
  stale, incomplete, pending, destructive, and safe targets.
- UX-IP-1 through UX-IP-3 — Route output deterministically and implement the
  complete keyboard, navigation, search, and filter contract.
- UX-IP-4 through UX-IP-7 — Use one discoverable action path, cancel-first
  confirmation, explicit baseline acceptance, and plan-to-outcome phases.
- UX-IP-8 through UX-IP-12 — Implement release progress, Agent results,
  in-flight exit/signal disposition, complete human-linear operation, and
  configuration recovery.

#### Accessibility, Responsiveness, and Budgets

- UX-A11Y-1 through UX-A11Y-5 — Text-first semantics, persistent keyboard
  focus, the complete human-linear alternative, hostile-text safety, and
  motion-free progress with terminal restoration.
- SR-A11Y-1 — Prove the complete linear morning handoff and exact action path
  under TERM=dumb and NO_COLOR for complete, incomplete, confirmation, and all
  Action Outcomes.
- UX-RP-1 through UX-RP-6 — Preserve the full, compact, narrow,
  below-minimum, live-resize, and redirected contracts without losing identity,
  state, completeness, focus, or action safety.
- UX-BUD-1 through UX-BUD-7 — Meet the exact local feedback, refresh,
  slow-refresh, submit, pending-update, outcome, and resize response budgets
  with their defaults, ranges, fixture, and p95 method.
- DESIGN visual contract — Inherit terminal typography and theme; use
  cell-native spacing, text-first markers, optional accessible style, stable
  reading order, exact component anatomy, deterministic narrow collapse, and
  no product palette, icon-only meaning, spinner, or unsafe raw control text.

## Coverage Maps

### FR-to-Epic Coverage

| Requirement | Primary Epic | Delivery outcome |
| --- | --- | --- |
| FR-1 | Epic 2 | Declare complete Runtime Promise intent |
| FR-2 | Epic 2 | Retain declaration provenance and revisions |
| FR-3 | Epic 2 | Default every Promise to a finite Lease |
| FR-4 | Epic 2 | Renew ownership through idempotent Heartbeats |
| FR-5 | Epic 2 | Close intent with one durable reason |
| FR-6 | Epic 2 | Require Durable Ownership for persistence |
| FR-7 | Epic 2 | Give Agents deterministic lifecycle contracts |
| FR-8 | Epic 3 | Discover cron work |
| FR-9 | Epic 3 | Discover systemd work |
| FR-10 | Epic 3 | Discover Docker work |
| FR-11 | Epic 3 | Discover PM2 work |
| FR-12 | Epic 3 | Discover direct Host processes |
| FR-13 | Epic 3 | Normalize all Provider Observations |
| FR-14 | Epic 3 | Publish scoped collection completeness |
| FR-15 | Epic 3 | Inspect bounded Provider detail |
| FR-16 | Epic 1 | Freeze and enforce brownfield compatibility |
| FR-17 | Epic 3 | Apply deterministic strict collection policy |
| FR-18 | Epic 4 | Correlate declared intent and observed truth |
| FR-19 | Epic 4 | Identify healthy intent |
| FR-20 | Epic 4 | Identify broken intent conservatively |
| FR-21 | Epic 4 | Identify orphaned Observations |
| FR-22 | Epic 4 | Identify exact duplicate Observations |
| FR-23 | Epic 4 | Identify stale Runtimes from positive evidence |
| FR-24 | Epic 4 | Identify hot Runtimes from sampled evidence |
| FR-25 | Epic 4 | Identify unmanaged and abandoned Runtimes |
| FR-26 | Epic 4 | Explain findings and Safe-to-stop Assessment |
| FR-27 | Epic 4 | Maintain bounded Snapshots and Accepted Baseline |
| FR-28 | Epic 4 | Produce the eight-answer morning Brief |
| FR-29 | Epic 4 | Organize attention, Stacks, and Ungrouped truth |
| FR-30 | Epic 5 | Route interactive and non-interactive presentation |
| FR-31 | Epic 5 | Navigate and refine the TUI |
| FR-32 | Epic 5 | Inspect intent and Host truth together |
| FR-33 | Epic 5 | Preserve meaning without color or Unicode |
| FR-34 | Epic 5 | Render every application and terminal state |
| FR-35 | Epic 6 | Expose a discoverable exact-target Action Menu |
| FR-36 | Epic 6 | Plan only supported lifecycle actions |
| FR-37 | Epic 6 | Revalidate identity before mutation |
| FR-38 | Epic 6 | Confirm destructive and uncertain actions |
| FR-39 | Epic 6 | Isolate asynchronous operations |
| FR-40 | Epic 6 | Verify and report one canonical Action Outcome |
| FR-41 | Epic 6 | Keep groups read-only and privilege narrow |
| FR-42 | Epic 7 | Build and install a verifiable release |
| FR-43 | Epic 7 | Upgrade, validate consumers, and roll back |

## Epics and Stories

## Epic 1: Trustworthy Rust and Durable Storage Foundation

Operators and downstream implementers gain a compatibility-locked Rust
substrate whose boundaries, configuration, typed contracts, local state, and
verification gates fail closed before Host discovery or mutation is added.

**Primary FR coverage:** FR-16.

**Enables:** Every later epic consumes the locked crate structure, canonical
encodings, deterministic policy, bounded execution port, SQLite repositories,
and aggregate acceptance gate. It requires no later epic to validate its own
foundation outcomes.

### Story 1.1: Bootstrap the Locked Rust Crate and Dependency Boundaries

As a srvls maintainer,
I want the prescribed Rust 2024 crate structure and inward-only dependency
boundaries established first,
So that every later capability has one testable architectural home.

**Implementation Boundary:** Create the single-binary crate skeleton, private
modules, inward-owned ports, dependency-boundary test, locked toolchain and
Cargo.lock, aggregate contract-gate entry point, and no Provider behavior.

**Requirement Mapping:** FR: FR-16; NFR: NFR-1, NFR-13, NFR-14, NFR-15; UJ:
UJ-6; UX: UX-FND-1, UX-FND-6; AD: AD-1, AD-3, AD-11, AD-12, AD-18.

**Dependencies:** None; this is the mandatory structural seed.

**Validation Expectations:** Compile on the locked MSRV and stable toolchain;
assert forbidden dependency edges fail; prove the one-binary/module inventory
and locked build in the aggregate gate.

**Out of Scope:** Provider adapters, SQLite schema, presentation, actions,
release activation, and any shell-out implementation.

**Acceptance Criteria:**

1. **Given** a clean supported checkout **When** the locked build and unit
   suite run **Then** one Rust 2024 binary compiles at MSRV 1.88 with the
   prescribed module tree **And** Cargo.lock is required.
2. **Given** a module attempts an outward dependency forbidden by AD-1
   **When** the boundary test evaluates it **Then** the gate fails with the
   exact edge **And** domain code remains free of adapter/presentation types.
3. **Given** no Provider implementation exists **When** the aggregate
   architecture gate runs **Then** the structural, toolchain, and test lanes
   pass independently **And** later-story matrices are registered but cannot
   claim acceptance before wiring.

### Story 1.2: Freeze and Enforce the Layered Compatibility Oracle

As an existing srvls user,
I want inherited Python behavior frozen before replacement,
So that the Rust migration preserves relied-on outputs or records an approved
deviation.

**Implementation Boundary:** Check in the table, flat JSON, Prometheus,
Markdown, inspect, executable-resolution, ordering, escaping, argv, exit, and
explicit-action corpus; implement byte, semantic, and live-smoke lanes plus a
deviation ledger with owner, rationale, replacement contract, and consumer
evidence.

**Requirement Mapping:** FR: FR-16; NFR: NFR-1, NFR-7, NFR-13, NFR-14; UJ:
UJ-1, UJ-2, UJ-6; UX: UX-FND-6, UX-IA-10, UX-CP-15; AD: AD-7, AD-9, AD-11,
AD-14, AD-18.

**Dependencies:** Story 1.1.

**Validation Expectations:** Reproduce the frozen corpus byte-for-byte where
owned, compare normalized semantics where nondeterminism is documented, run
named live smokes, and fail on an unapproved or unexpired deviation.

**Out of Scope:** New TUI contracts, changing inherited behavior merely for
style, fetching Plane/Git/Telemetry, and treating the retired backlog as an
oracle.

**Acceptance Criteria:**

1. **Given** every frozen Python fixture **When** the Rust compatibility lane
   executes **Then** owned bytes, exits, ordering, escaping, executable choice,
   and argv match **And** semantic-only fields use an explicit normalizer.
2. **Given** a deliberate incompatibility **When** the gate encounters it
   **Then** it fails unless a ledger entry names the exact fixture, owner,
   rationale, replacement, consumer proof, and expiry **And** approval is
   machine-checkable.
3. **Given** a deployed consumer fixture and supported Host smoke **When** the
   live lane runs **Then** invocation, stdout/stderr, exit, and executable path
   are recorded **And** a golden-only pass cannot close live compatibility.

### Story 1.3: Define Canonical Encodings and Typed Identities

As an Operator,
I want every persisted and displayed identity to be byte-total and canonical,
So that evidence remains exact across processes, refreshes, upgrades, and
hostile Host text.

**Implementation Boundary:** Implement closed canonical JSON and binary
grammars, typed IDs, raw-byte path/text wrappers, stable ordering, domain
diagnostics, fingerprints, redaction/truncation metadata, and version tags for
current and historical authority.

**Requirement Mapping:** FR: FR-2, FR-13, FR-15, FR-16; NFR: NFR-1, NFR-2,
NFR-7, NFR-8, NFR-11; UJ: UJ-1, UJ-3, UJ-4; UX: UX-FND-3, UX-VT-2,
UX-CP-5, UX-CP-7, UX-A11Y-4; AD: AD-8, AD-13, AD-21, AD-24, AD-25.

**Dependencies:** Stories 1.1 and 1.2.

**Validation Expectations:** Golden and property tests cover every ID family,
non-UTF-8 bytes, control sequences, map/order stability, unknown versions,
round trips, collision resistance, redaction, truncation, and one-newline JSON.

**Out of Scope:** Provider correlation policy, UI layout, storage repositories,
and assigning identity from friendly names.

**Acceptance Criteria:**

1. **Given** canonical domain values in arbitrary insertion order **When**
   encoded and fingerprinted **Then** bytes and digest are identical **And**
   decoding reconstructs the typed values without lossy text conversion.
2. **Given** non-UTF-8 paths, ANSI/OSC controls, bidi markers, newlines, or
   over-bound text **When** values cross a boundary **Then** identity bytes are
   preserved while display text is sanitized and bounded **And** metadata says
   what changed.
3. **Given** an unknown grammar version, malformed ID, duplicate key, or
   noncanonical number **When** decoded **Then** the value is rejected with a
   stable typed diagnostic **And** no partial authority is admitted.

### Story 1.4: Compile Typed Configuration and Operational Policy

As an Operator,
I want every duration, threshold, retention, deadline, and bound compiled with
visible provenance,
So that invalid policy fails before collection, storage, or mutation.

**Implementation Boundary:** Implement defaults, inclusive ranges,
configuration precedence, source/redaction, duration and size parsing,
cross-field/derived ARCH-LIM-1..24 formulas, deterministic PolicySnapshotV1
encoding, invalid-config diagnostics, and policy display.

**Requirement Mapping:** FR: FR-16, FR-17; NFR: NFR-1, NFR-2, NFR-11,
NFR-16; UJ: UJ-1, UJ-2, UJ-6; UX: UX-IA-12, UX-VT-3, UX-IP-12,
UX-ST-18; AD: AD-11, AD-19, AD-20, AD-21, AD-24.

**Dependencies:** Story 1.3.

**Validation Expectations:** Table/property tests enumerate all defaults,
minimum/maximum/just-outside values, precedence layers, redacted inputs,
derived overflow/capacity relationships, stable policy bytes, and pre-side-
effect rejection.

**Out of Scope:** Dynamic remote configuration, implicit unit guessing,
Provider discovery, and silently clamping invalid values.

**Acceptance Criteria:**

1. **Given** defaults and each precedence source **When** policy compiles
   **Then** the effective typed value, units, source, default, range, and
   overridden source are deterministic **And** secrets remain redacted.
2. **Given** every inclusive ARCH-LIM boundary and one value immediately
   outside it **When** validation runs **Then** boundaries pass and outside
   values fail with field/type/range/repair **And** no side effect has begun.
3. **Given** derived capture, retention, queue, history, or capacity arithmetic
   that overflows or violates a cross-field rule **When** compiled **Then**
   policy is rejected rather than clamped **And** the exact formula operands
   are inspectable.

### Story 1.5: Open SQLite as Fail-Closed Durable Truth

As an Operator,
I want local state opened, migrated, and permission-checked transactionally,
So that srvls never runs from split or weakly protected truth.

**Implementation Boundary:** Implement the sole SQLite state owner, canonical
location, restrictive directory/file modes, connection pragmas, schema/meta
versioning, ordered transactional migrations, compatibility checks, integrity
probe, backup precondition hooks, corruption/unsupported-version diagnostics,
and no alternate durable store.

**Requirement Mapping:** FR: FR-2, FR-16, FR-27; NFR: NFR-2, NFR-9, NFR-11,
NFR-12, NFR-14; UJ: UJ-2, UJ-6; UX: UX-ST-18, UX-VT-4, UX-IA-9; AD: AD-11,
AD-16, AD-17, AD-20, AD-23, AD-24.

**Dependencies:** Stories 1.3 and 1.4.

**Validation Expectations:** Temporary-database tests cover first create,
every migration edge, crash before/during/after commit, unsupported future
schema, corrupt bytes, busy timeout, mode repair/refusal, integrity failure,
and byte-identical reopen.

**Out of Scope:** Promise-specific repositories, release activation, cloud
replication, and attempting to repair unknown corruption automatically.

**Acceptance Criteria:**

1. **Given** no state exists at the canonical path **When** storage opens
   **Then** one permission-restricted database and schema metadata are created
   atomically **And** success is returned only after integrity and pragma
   checks.
2. **Given** a supported older schema **When** migration is interrupted at any
   injected cut **Then** reopen yields either the complete prior or complete
   next schema **And** never a partially authoritative mix.
3. **Given** weak permissions, incompatible future schema, corruption, or
   failed integrity **When** open is attempted **Then** startup fails closed
   with one recovery instruction **And** no collection, baseline, or action
   side effect starts.

### Story 1.6: Persist Atomic State, Events, and Compare-and-Swap Revisions

As an Agent or Operator,
I want durable domain changes and audit evidence committed once,
So that retries and concurrent writers cannot create conflicting truth.

**Implementation Boundary:** Implement inward-owned repository ports and
SQLite adapters for aggregate rows, append-only events, idempotency keys,
compare-and-swap revisions, transaction outbox/audit records, immutable
Snapshot inputs, stable query ordering, and typed conflicts.

**Requirement Mapping:** FR: FR-2, FR-4, FR-5, FR-27, FR-39; NFR: NFR-1,
NFR-9, NFR-12, NFR-13; UJ: UJ-2, UJ-4, UJ-6; UX: UX-CP-15, UX-ST-12,
UX-VT-3; AD: AD-1, AD-3, AD-5, AD-6, AD-16, AD-17, AD-22.

**Dependencies:** Story 1.5.

**Validation Expectations:** Repository contract suites run against fake and
SQLite implementations; race tests cover duplicate keys, stale revisions,
rollback, read ordering, event/state atomicity, late writers, and crash reopen.

**Out of Scope:** Domain lifecycle decisions, Collector execution, action
effects, and release lock ownership.

**Acceptance Criteria:**

1. **Given** a valid state transition and event **When** the transaction
   commits **Then** aggregate revision, event, idempotency result, and audit
   evidence are visible together **And** an injected failure exposes none.
2. **Given** two writers using one prior revision **When** both attempt an
   update **Then** exactly one commits and the other receives a typed conflict
   **And** retry cannot overwrite newer state.
3. **Given** the same idempotency key and canonical request **When** replayed
   after success or crash recovery **Then** the stored result is returned
   byte-for-byte **And** a different request under that key is refused.

### Story 1.7: Enforce Bounded Retention, Capacity, and Recovery

As an Operator,
I want state growth bounded without deleting evidence still needed for truth
or recovery,
So that long-running use stays predictable and auditable.

**Implementation Boundary:** Implement ARCH-LIM retention/capacity modes,
eligible-row ordering, baseline/operation/release pins, archive/delete
transactions, low-disk and hard-cap behavior, recovery of interrupted
maintenance, vacuum policy, visible counters/provenance, and never-evict rules.

**Requirement Mapping:** FR: FR-2, FR-27, FR-39, FR-43; NFR: NFR-2, NFR-9,
NFR-11, NFR-12, NFR-16; UJ: UJ-1, UJ-4, UJ-6; UX: UX-ST-5, UX-ST-12,
UX-ST-16, UX-VT-3; AD: AD-5, AD-11, AD-16, AD-20, AD-22, AD-23.

**Dependencies:** Story 1.6.

**Validation Expectations:** Boundary/model tests cover every retention class,
age/count/byte ties, all pin types, concurrent baseline/action/release,
low-disk modes, hard-cap refusal, crash cuts, deterministic victim order, and
no dangling references.

**Out of Scope:** Remote archival, deleting current/baseline/in-flight/
KnownGood evidence, unbounded logs, and silent best-effort eviction.

**Acceptance Criteria:**

1. **Given** rows over age, count, or byte limits **When** retention runs
   **Then** only eligible unpinned rows are removed in canonical order **And**
   current, baseline, in-flight, audit-minimum, and release recovery evidence
   survive.
2. **Given** capacity cannot be restored without evicting protected evidence
   **When** a new write is admitted **Then** policy enters the specified
   visible degraded or refusal mode **And** does not delete a pin or claim
   success.
3. **Given** interruption at each retention transaction cut **When** storage
   reopens **Then** referential integrity and exact counters recover
   deterministically **And** the Operator receives bounded recovery evidence.

### Story 1.8: Provide Typed Bounded Host Execution and the Foundation Gate

As a later capability implementer,
I want one safe command port and one aggregate verification gate,
So that discovery and actions cannot bypass argv, capture, deadline, privilege,
or architecture contracts.

**Implementation Boundary:** Implement typed argv-only CommandRunner and
fake/TestBackend, end-of-options construction, explicit environment/cwd,
bounded stdout/stderr capture with truncation metadata, deadlines,
TERM/KILL/reaping, process groups, descriptor policy, privilege request type,
and aggregate AD-11 orchestration including ARCH-HOST-1 evidence.

**Requirement Mapping:** FR: FR-15, FR-16, FR-17, FR-37, FR-42; NFR: NFR-2,
NFR-3, NFR-4, NFR-5, NFR-13, NFR-15, NFR-16; UJ: UJ-1, UJ-3, UJ-4, UJ-6;
UX: UX-ST-5, UX-ST-10, UX-BUD-1, UX-BUD-2, UX-BUD-3; AD: AD-3, AD-7,
AD-10, AD-11, AD-14, AD-15, AD-20, AD-25.

**Dependencies:** Stories 1.1 through 1.7.

**Validation Expectations:** Fake-port, property, and live opt-in tests cover
argv injection, leading hyphens, timeout boundaries, capture caps, TERM/KILL,
descendant reaping, environment/descriptor leaks, privilege refusal, stable
diagnostics, constrained-host 30-iteration p95 evidence, and aggregate lane
ownership.

**Out of Scope:** Provider parsing, concurrent collection scheduling, action
outcome policy, interactive authorization, and implementing future gate
matrices before their owning stories.

**Acceptance Criteria:**

1. **Given** hostile args, leading hyphens, shell metacharacters, large output,
   a hung child, and descendants **When** CommandRunner executes **Then** no
   shell is invoked, end-of-options is explicit where supported, capture is
   bounded, deadline escalates TERM then KILL, and every child is reaped
   **And** diagnostics preserve exit/signal/truncation.
2. **Given** a command requests ambient elevation, interactive authorization,
   undeclared environment, cwd, or descriptor inheritance **When** admitted
   **Then** the request is refused before spawn **And** one typed narrow
   privilege contract is required.
3. **Given** all Epic 1 fixtures and the ARCH-HOST-1 profile **When** the
   aggregate gate runs **Then** structure, compatibility, encoding, policy,
   storage, repository, retention, execution, and budget lanes are named and
   machine-readable **And** a missing/unwired lane fails rather than being
   inferred as passed.

## Epic 2: Runtime Promise Lifecycle

Agents and Operators can declare why a Runtime should exist, keep finite
ownership current, inspect it deterministically, opt into accountable
persistence, and close intent without implicitly mutating Host truth.

**Primary FR coverage:** FR-1 through FR-7.

**Depends on:** Epic 1 durable state, typed time, configuration, and machine
result contracts. It is complete without discovered Observations.

### Story 2.1: Declare and Revise Complete Runtime Intent

As an Agent,
I want to declare and deliberately revise why one Runtime should exist,
So that srvls can preserve accountable intent before any Host evidence exists.

**Implementation Boundary:** Implement RuntimePromise declaration and revision
commands/use cases with required Agent, Project, Provider locator, purpose,
Launch Mechanism, lifetime, Owner, intended count, persistence, optional opaque
references, canonical validation, revision compare-and-swap, provenance, and
idempotency.

**Requirement Mapping:** FR: FR-1, FR-2, FR-6, FR-7; NFR: NFR-1, NFR-2,
NFR-7, NFR-9, NFR-11, NFR-12, NFR-13; UJ: UJ-2; UX: UX-FND-2, UX-FND-3,
UX-IA-10, UX-CP-15, UX-IP-9; AD: AD-2, AD-8, AD-9, AD-11, AD-13, AD-17,
AD-21, AD-24.

**Dependencies:** Epic 1, especially Stories 1.3, 1.4, and 1.6.

**Validation Expectations:** Domain and machine golden tests cover every
required/malformed field, byte-total identities, opaque references, default
values, retries, conflicting revisions, persistent/unmanaged branches, stable
error order, and no Host side effects.

**Out of Scope:** Discovering a Runtime, verifying that intent is healthy,
starting it, fetching opaque references, and silently rewriting supplied
identity.

**Acceptance Criteria:**

1. **Given** all required canonical fields and an idempotency key **When** an
   Agent declares intent **Then** one Promise ID, revision, finite Lease, and
   effective policy are returned deterministically **And** declaration source,
   time, supplied identities, and event are committed atomically.
2. **Given** missing, malformed, out-of-range, conflicting, or over-bound
   fields **When** declaration is attempted **Then** stable field diagnostics
   and repair hints are returned **And** no Promise, Lease, event, or Host
   effect is created.
3. **Given** an existing Promise and expected revision **When** a semantic
   revision is submitted **Then** changed fields and provenance become one new
   revision **And** a stale revision conflicts without overwriting newer
   intent.

### Story 2.2: Enforce Finite Leases and Accountable Persistence

As an Operator,
I want Agent intent finite by default and persistence tied to durable
ownership,
So that forgotten declarations cannot masquerade indefinitely as current
requirements.

**Implementation Boundary:** Implement Lease creation/evaluation with wall and
monotonic anchors, boot identity and discontinuity evidence, defaults/ranges,
finite expiry, persistent-intent validation against Durable Ownership and
inspectable Launch Mechanism, invalid-persistent unmanaged retention policy,
and lifecycle queries.

**Requirement Mapping:** FR: FR-3, FR-6, FR-7; NFR: NFR-1, NFR-2, NFR-9,
NFR-10, NFR-13, NFR-16; UJ: UJ-2, UJ-4; UX: UX-VT-3, UX-CP-5, UX-ST-4,
UX-ST-20; AD: AD-2, AD-11, AD-17, AD-19, AD-20, AD-21, AD-24.

**Dependencies:** Story 2.1.

**Validation Expectations:** Use fake clocks and boot IDs to test default,
minimum, maximum, exact expiry, one-nanosecond boundaries, rollback, forward
jump, suspend, reboot, overflow, persistent ownership/mechanism combinations,
and restart reconstruction.

**Out of Scope:** Automatically stopping expired work, assuming persistence
from a long Lease, Host discovery, and interpreting opaque references.

**Acceptance Criteria:**

1. **Given** no explicit lifetime **When** a Promise is declared **Then** the
   documented finite default and renewal expectation are stored and returned
   **And** expiry is computed without unbounded wall-clock trust.
2. **Given** persistent intent with and without Durable Ownership and an
   inspectable Launch Mechanism **When** validation runs **Then** only the
   complete accountable pair becomes persistent **And** policy either rejects
   or explicitly retains the invalid request as unmanaged.
3. **Given** wall rollback, suspend, boot change, or monotonic discontinuity
   **When** lifecycle is reconstructed **Then** the specified conservative
   state and evidence are deterministic **And** discontinuity never silently
   extends ownership.

### Story 2.3: Renew Ownership with Idempotent Heartbeats

As an Agent,
I want retry-safe Heartbeats to renew only the Promise I own,
So that transient delivery failures do not duplicate or steal lifecycle
authority.

**Implementation Boundary:** Implement authenticated Heartbeat submission,
owner/Promise/revision checks, idempotency key, sequence and observed-at
validation, Lease renewal, late-within-Lease status, expiry boundary, durable
event/result, and unauthorized/malformed/closed/unknown outcomes.

**Requirement Mapping:** FR: FR-4, FR-7; NFR: NFR-1, NFR-2, NFR-7, NFR-9,
NFR-10, NFR-12, NFR-13, NFR-16; UJ: UJ-2; UX: UX-FND-2, UX-CP-5,
UX-CP-15, UX-IP-9, UX-ST-4; AD: AD-2, AD-11, AD-17, AD-20, AD-21, AD-24.

**Dependencies:** Stories 2.1 and 2.2.

**Validation Expectations:** State-machine/property tests cover first,
duplicate, reordered, malformed, wrong-owner, wrong-revision, late,
exact-expiry, expired, closed, unknown, crash replay, clock/boot change, and
concurrent Heartbeats.

**Out of Scope:** Liveness probing, Runtime telemetry, recreating expired
intent, and extending ownership on an unauthorized request.

**Acceptance Criteria:**

1. **Given** the current Owner, revision, valid sequence, and idempotency key
   within the Lease **When** a Heartbeat arrives **Then** exactly one event and
   renewed finite Lease commit **And** a replay returns identical bytes.
2. **Given** a Heartbeat after the preferred cadence but before Lease expiry
   **When** evaluated **Then** it is accepted as late with timing evidence
   **And** late is distinguishable from expired and abandoned.
3. **Given** malformed, unauthorized, stale-revision, reordered, closed,
   unknown, or expired input **When** submitted **Then** one canonical
   non-success result is returned **And** Lease and Promise state do not
   change.

### Story 2.4: Release, Complete, Revoke, and Inspect Lifecycle History

As an Agent or Operator,
I want to close intent with one explicit reason and inspect its full history,
So that accountability ends cleanly without implying the Runtime was stopped.

**Implementation Boundary:** Implement release, complete, and authorized
revoke transitions; one retained reason; idempotency and revision checks;
terminal lifecycle history; current and historical query; closed Heartbeat
behavior; and explicit no-Host-mutation semantics.

**Requirement Mapping:** FR: FR-2, FR-5, FR-7; NFR: NFR-1, NFR-2, NFR-7,
NFR-9, NFR-12, NFR-13; UJ: UJ-2, UJ-4; UX: UX-FND-5, UX-VT-2, UX-VT-4,
UX-CP-5, UX-CP-15, UX-IP-9; AD: AD-2, AD-5, AD-11, AD-17, AD-21, AD-24.

**Dependencies:** Stories 2.1 through 2.3.

**Validation Expectations:** Transition tables cover each close reason,
authorization, empty/over-bound reason, duplicate and conflicting closes,
Heartbeat-after-close, query ordering, crash replay, and assertions that no
CommandRunner/Provider action port is invoked.

**Out of Scope:** Stopping or disabling a Runtime, deleting history, inferring
completion from collection, and reopening a terminal Promise in place.

**Acceptance Criteria:**

1. **Given** active intent and an authorized principal **When** release,
   complete, or revoke is requested with one valid reason **Then** one terminal
   event and revision commit **And** the result states that Host truth was not
   mutated.
2. **Given** a duplicate identical close **When** retried **Then** the original
   terminal result is returned **And** a different close reason or stale
   revision conflicts without rewriting history.
3. **Given** a terminal Promise **When** queried or Heartbeated **Then** its
   declaration, revisions, Lease/Heartbeats, close principal/time/reason, and
   closed result remain inspectable **And** no renewal or implicit reopen
   occurs.

### Story 2.5: Deliver Deterministic Agent Lifecycle Results

As an automation Agent,
I want declare, query, renew, revise, and close to share one stable machine
contract,
So that retries and recovery never require parsing human prose.

**Implementation Boundary:** Implement versioned JSON request/result envelopes,
stdin/argv routing, stable schema and exit matrix, clean stdout/stderr,
idempotency guidance, current/list/history queries, bounded pagination,
deterministic ordering, redaction, explicit recovery instructions, and human-
linear lifecycle equivalents.

**Requirement Mapping:** FR: FR-1 through FR-7; NFR: NFR-1, NFR-2, NFR-7,
NFR-8, NFR-11, NFR-12, NFR-13; UJ: UJ-2; UX: UX-IA-10, UX-CP-15,
UX-IP-9, UX-IP-11, UX-A11Y-3, UX-VT-4; AD: AD-7, AD-8, AD-9, AD-11,
AD-13, AD-17, AD-24.

**Dependencies:** Stories 2.1 through 2.4.

**Validation Expectations:** Golden command matrices cover all operations and
outcomes, stdin/argv equivalence, duplicate retry, pagination, hostile text,
NO_COLOR/TERM=dumb, stdout/stderr separation, one trailing newline, exit
stability, and SM-5 end-to-end lifecycle.

**Out of Scope:** TUI, collection, reconciliation, action execution, Provider-
specific output, and compatibility with undocumented prose parsing.

**Acceptance Criteria:**

1. **Given** any valid lifecycle request through argv or canonical stdin
   **When** executed **Then** the same versioned envelope, typed result,
   effective policy, retry guidance, and stable exit are emitted **And** stdout
   contains only one JSON document and trailing newline.
2. **Given** validation, authorization, conflict, closed, unknown, expiry, or
   storage failure **When** returned **Then** the machine result names exact
   reason and safe recovery instruction **And** logs/human diagnostics remain
   on stderr without ANSI or icons.
3. **Given** the canonical UJ-2 fixture with lost response, retry, late
   Heartbeat, query, close, and post-close retry **When** run end-to-end
   **Then** one coherent event history and deterministic results prove SM-5
   **And** no Host command or Provider adapter is invoked.

## Epic 3: Five-Provider Discovery Including Direct Processes

Operators receive fresh, bounded, scoped Host Observations from cron, systemd,
Docker, PM2, and direct processes, with exact identities, honest completeness,
strict policy, and failure-local inspection.

**Primary FR coverage:** FR-8 through FR-15 and FR-17.

**Depends on:** Epic 1 execution, identity, storage, and verification
foundation; consumes Epic 2 Promises only to promote supported Collection
Obligations. Discovery still returns useful truth when no Promise exists.

### Story 3.1: Admit One Frozen Collection Plan and Dispatch Schedule

As an Operator,
I want every refresh admitted as one immutable bounded plan,
So that concurrent Host changes cannot move the meaning of a generation.

**Implementation Boundary:** Implement CollectionPlanV1 admission transaction
freezing PromiseCut, PolicySnapshot, ScopeSet and obligations, compiled
DispatchSchedule, AcceptedBaselineCut, OperationCut, ResourceHistoryCut,
PriorCurrentCut, generation/latest-requested markers, policy fingerprints,
half-open epochs, deterministic LPT admission/setup dispatch, and zero post-
admission truth lookup.

**Requirement Mapping:** FR: FR-14, FR-17; NFR: NFR-1, NFR-2, NFR-3, NFR-9,
NFR-12, NFR-13, NFR-16; UJ: UJ-1, UJ-3; UX: UX-ST-1, UX-ST-2, UX-ST-3,
UX-ST-5, UX-BUD-2, UX-BUD-3; AD: AD-5, AD-10, AD-11, AD-20, AD-21, AD-24.

**Dependencies:** Epic 1 and promoted Collection Obligations from Epic 2.

**Validation Expectations:** Golden traces cover the default and near-tie
schedules, exact boundary/catch-up admission, zero-margin process LPT,
setup-delay realization, max concurrency, latest-wins, cancellation, policy/
Promise/baseline/history races, overflow, and zero post-admission lookup.

**Out of Scope:** Executing Collectors, parsing Provider output, action-pool
work, reconciliation, and consulting newly arrived truth mid-generation.

**Acceptance Criteria:**

1. **Given** frozen supported policy, scope, Promise, baseline, operation,
   history, and prior-current rows **When** refresh admission commits **Then**
   one canonical CollectionPlanV1 and generation fingerprint contain every cut
   **And** no later lookup may alter that generation.
2. **Given** default, near-tie, and zero-margin cost vectors **When** the
   schedule compiler runs **Then** exact lane assignment/start/finish traces
   follow AD-10 LPT, setup delay, half-open boundaries, and canonical ties
   **And** realized dispatch never exceeds the frozen concurrency bound.
3. **Given** overlapping refresh requests and late prior workers **When**
   generations complete **Then** only the latest requested eligible generation
   may advance current truth **And** every superseded/late result remains
   bounded diagnostic evidence.

### Story 3.2: Authenticate and Bound Same-Binary FD3 Collector Workers

As an Operator,
I want each Collector isolated behind the authenticated same-binary protocol,
So that a Provider hang or malformed child cannot corrupt the coordinator.

**Implementation Boundary:** Implement parent/worker same-executable spawn,
FD3 socketpair ownership and close-on-exec rules, peer executable/inode/start
proof, nonce/plan/Provider/scope handshake, length-delimited canonical frames,
size/time limits, exactly one terminal report, EOF semantics, child cleanup,
descriptor allowlist, and failure-local diagnostics.

**Requirement Mapping:** FR: FR-13, FR-14, FR-17; NFR: NFR-2, NFR-3, NFR-4,
NFR-5, NFR-11, NFR-12, NFR-13, NFR-16; UJ: UJ-1, UJ-3; UX: UX-ST-5,
UX-VT-3, UX-VT-4; AD: AD-10, AD-11, AD-13, AD-14, AD-15, AD-20, AD-24,
AD-25.

**Dependencies:** Stories 1.3, 1.8, and 3.1.

**Validation Expectations:** The full FD3 matrix covers descriptor
number/ownership, peer mismatch, exec/inode/start races, nonce replay,
wrong plan/provider/scope, malformed/oversize/truncated/extra frames,
timeout/signals/EOF, duplicate terminal report, inherited descriptors, child
exit, cleanup, and canonical diagnostics.

**Out of Scope:** A long-lived daemon, unauthenticated plugin protocol,
Provider parsing, action execution, and accepting stdout as Collector truth.

**Acceptance Criteria:**

1. **Given** an admitted plan and verified same-binary child **When** FD3
   handshake completes **Then** nonce, plan, Provider, scope, peer executable,
   inode, and start evidence match before payload acceptance **And** only
   declared descriptors remain open.
2. **Given** malformed, oversized, replayed, mismatched, duplicate, truncated,
   or post-terminal frames **When** the parent reads FD3 **Then** the scope
   fails with one typed bounded diagnostic **And** no partial payload becomes
   accepted truth.
3. **Given** timeout, EOF, signal, worker panic, or descendant leak **When**
   cleanup runs **Then** the process group is terminated/reaped and exactly one
   terminal report or synthesized failure exists **And** sibling scopes
   continue under schedule policy.

### Story 3.3: Collect Cron Work with Exact Source Identity

As an Operator,
I want user, root, system, and drop-in cron represented with source provenance,
So that scheduled work is visible even when one scope is unreadable.

**Implementation Boundary:** Implement cron scope enumeration and parser for
user crontabs, root crontab, system crontab, and drop-ins; schedule and command
identity; principal; environment/source/line provenance; comments/continuation/
special schedule handling; permission diagnostics; bounded raw detail; and
read-only Provider capabilities.

**Requirement Mapping:** FR: FR-8, FR-13, FR-14, FR-15, FR-17; NFR: NFR-1,
NFR-2, NFR-3, NFR-4, NFR-5, NFR-11, NFR-13; UJ: UJ-1, UJ-3; UX: UX-CP-6,
UX-CP-7, UX-ST-5, UX-ST-20; AD: AD-2, AD-11, AD-13, AD-15, AD-18, AD-25.

**Dependencies:** Stories 3.1 and 3.2.

**Validation Expectations:** Frozen parser and live opt-in fixtures cover every
scope, standard/special schedules, environment lines, comments, whitespace,
continuations, system principal field, malformed/large/non-UTF-8 lines,
duplicate sources, permission denial, timeout, and deterministic provenance.

**Out of Scope:** Editing/installing crontabs, starting/stopping cron entries,
shell-evaluating commands, and treating inaccessible root scope as empty.

**Acceptance Criteria:**

1. **Given** valid entries across all four cron scope families **When**
   collected **Then** schedule, command identity, source bytes, line, principal,
   scope, and encounter provenance are exact and deterministic **And**
   environment text remains bounded evidence.
2. **Given** malformed, hostile, over-bound, or non-UTF-8 content **When**
   parsed **Then** unaffected entries survive, diagnostics name source/line and
   truncation **And** no command text is executed or trusted for display.
3. **Given** root or drop-in permission failure **When** collection completes
   **Then** that obligation is incomplete with the exact failure **And** user/
   system successes remain usable without proving absence in the failed scope.

### Story 3.4: Collect System and User systemd Work

As an Operator,
I want system and user services and timers correlated with full unit identity,
So that enablement, runtime health, and schedules remain distinct.

**Implementation Boundary:** Implement system/user scope enumeration, service
and timer identity, load/active/sub states, enablement, result, main PID/birth
evidence, unit paths/drop-ins, timer calendar/monotonic next/last trigger,
triggered unit, provenance, typed detail, scope diagnostics, and bounded typed
argv.

**Requirement Mapping:** FR: FR-9, FR-13, FR-14, FR-15, FR-17; NFR: NFR-1,
NFR-2, NFR-3, NFR-4, NFR-5, NFR-11, NFR-13; UJ: UJ-1, UJ-3; UX: UX-CP-5,
UX-CP-6, UX-CP-7, UX-ST-5; AD: AD-2, AD-11, AD-13, AD-15, AD-18, AD-25.

**Dependencies:** Stories 3.1 and 3.2.

**Validation Expectations:** Provider golden/live fixtures cover system and
user managers, inactive/failed/activating services, masked/static/enabled
states, service/timer pairing, calendar and monotonic timers, missing user bus,
permission denial, vanished units, non-UTF-8 paths, version variants, and
deterministic argv/parse.

**Out of Scope:** Mutating units, inferring a service is enabled from active,
requiring a user bus for system truth, and following journal output.

**Acceptance Criteria:**

1. **Given** services and timers in both managers **When** collected **Then**
   full unit name plus manager scope anchors identity and enablement, runtime,
   health, schedule, source, and trigger relationship remain separate **And**
   birth evidence accompanies any process identity.
2. **Given** a missing user manager, vanished unit, permission denial, command
   failure, or partial property set **When** a scope completes **Then** exact
   diagnostics and completeness are retained **And** successful system or
   sibling-unit truth is not discarded.
3. **Given** hostile properties, paths, or version-specific unknown fields
   **When** normalized **Then** known bounded typed detail is preserved,
   untrusted text is sanitized at presentation boundaries, and unsupported
   fields do not reorder identity **And** no shell is invoked.

### Story 3.5: Collect Immutable Docker Container Truth

As an Operator,
I want Docker containers anchored by immutable identity,
So that recreated names cannot be confused with the instance I inspected.

**Implementation Boundary:** Implement daemon scope collection for full
container ID, name, created/start evidence, state/health, restart count/policy,
image ID/reference, Compose project/service/working directory, permitted
labels, mounts/network summaries within bounds, provenance, and daemon/scope
diagnostics.

**Requirement Mapping:** FR: FR-10, FR-13, FR-14, FR-15, FR-17; NFR: NFR-1,
NFR-2, NFR-3, NFR-4, NFR-5, NFR-11, NFR-13; UJ: UJ-1, UJ-4, UJ-5; UX:
UX-FND-3, UX-CP-5, UX-CP-7, UX-ST-10; AD: AD-2, AD-11, AD-13, AD-15,
AD-18, AD-25.

**Dependencies:** Stories 3.1 and 3.2.

**Validation Expectations:** Golden/live fixtures cover running/exited/
restarting/unhealthy, same-name replacement, abbreviated-ID rejection,
Compose present/absent/conflicting labels, restart policy, daemon unavailable,
permission denial, inspect race, large/secret labels, bounded detail, and
stable ordering.

**Out of Scope:** Image pulls, log collection, arbitrary environment exposure,
Docker mutation, and using mutable name as exact identity.

**Acceptance Criteria:**

1. **Given** containers with mutable names and Compose metadata **When**
   collected **Then** full immutable container ID and creation/start evidence
   anchor identity while name, image, health, restart, Compose, labels, and cwd
   remain evidence **And** secrets/unpermitted labels are excluded or redacted.
2. **Given** a container vanishes or is replaced between list and inspect
   **When** collection completes **Then** the race is explicit and no mixed
   identity Observation is emitted **And** unaffected containers remain
   usable.
3. **Given** daemon unavailable, permission denied, timeout, or truncated
   detail **When** reported **Then** scope completeness and bounds are visible
   **And** absence and Safe-to-stop are not inferred.

### Story 3.6: Collect Birth-Safe PM2 Process Truth

As an Operator,
I want PM2-managed processes identified beyond reusable PM2 and OS IDs,
So that restarts and ecosystem changes do not misattribute an instance.

**Implementation Boundary:** Implement PM2 home/scope discovery, PM2 ID plus
daemon/process birth evidence, name, namespace, status, restarts, pid, script,
interpreter, working directory, start time, ecosystem/source evidence,
provenance, bounded typed JSON parsing, and scope diagnostics.

**Requirement Mapping:** FR: FR-11, FR-13, FR-14, FR-15, FR-17; NFR: NFR-1,
NFR-2, NFR-3, NFR-4, NFR-5, NFR-11, NFR-13; UJ: UJ-1, UJ-4, UJ-5; UX:
UX-FND-3, UX-CP-5, UX-CP-7, UX-ST-10; AD: AD-2, AD-11, AD-13, AD-15,
AD-18, AD-25.

**Dependencies:** Stories 3.1 and 3.2.

**Validation Expectations:** Fixtures cover online/stopped/errored/launching,
cluster instances, PM2 ID and PID reuse, restart races, multiple homes/
namespaces, missing cwd/script/start evidence, daemon down, malformed/large
JSON, permission denial, and canonical ordering.

**Out of Scope:** PM2 log/env capture, assuming namespace is identity,
modifying ecosystem files, and lifecycle mutation.

**Acceptance Criteria:**

1. **Given** PM2 processes including clusters and restarts **When** collected
   **Then** daemon scope, PM2 ID, OS PID, and birth/start evidence form a
   birth-safe identity **And** namespace, name, script, cwd, state, and restart
   count remain non-authoritative evidence.
2. **Given** an ID/PID reuse or restart during collection **When** list and
   detail disagree **Then** the item is marked raced/incomplete rather than
   merged **And** no stale instance can become an exact action target.
3. **Given** malformed output, missing daemon, permission failure, or bounded
   truncation **When** the report completes **Then** diagnostics are local to
   PM2 scope **And** other Providers and parseable PM2 items remain usable.

### Story 3.7: Collect Direct Processes Without Reporting srvls Itself

As an Operator,
I want unmanaged direct Host processes represented with birth-safe identity,
So that real work outside managers is visible without counting srvls or
Provider-owned children twice.

**Implementation Boundary:** Implement process-table collection using PID plus
boot/process start ticks, executable/argv fingerprint, parent, uid/user,
permitted cwd, state and bounded resource sample; generation-bound
self-process/descendant suppression; attribution of systemd/Docker/PM2-owned
processes; kernel-thread and permission policy; provenance and diagnostics.

**Requirement Mapping:** FR: FR-12, FR-13, FR-14, FR-15, FR-17; NFR: NFR-1,
NFR-2, NFR-3, NFR-5, NFR-11, NFR-12, NFR-13; UJ: UJ-1, UJ-4, UJ-5; UX:
UX-FND-3, UX-CP-5, UX-CP-7, UX-ST-10; AD: AD-2, AD-11, AD-13, AD-14,
AD-18, AD-21, AD-25.

**Dependencies:** Stories 3.1 and 3.2.

**Validation Expectations:** Procfs/fake fixtures cover PID reuse, boot change,
exec between reads, vanished/zombie/kernel thread, permission denial, non-UTF-8
exe/cwd/argv, cycles, self/worker/grandchild suppression, Provider ownership,
resource samples, caps, and iteration-order invariance.

**Out of Scope:** Arbitrary environment/memory/file inspection, inventing a
direct-process Start path, signals, and duplicating a process already owned by
another Provider.

**Acceptance Criteria:**

1. **Given** stable direct processes **When** proc evidence is collected
   **Then** PID plus boot/start ticks and executable or command fingerprint
   anchor identity with parent, principal, permitted cwd, state, and sample
   provenance **And** inaccessible optional fields remain explicit.
2. **Given** srvls coordinator, FD3 workers, descendants, or processes exactly
   owned by systemd/Docker/PM2 **When** suppression/attribution runs **Then**
   current-generation self work is excluded and managed work is attributed
   rather than duplicated **And** ambiguous ownership remains visible.
3. **Given** PID reuse, exec/read race, vanish, permission denial, or cap
   exhaustion **When** the scope completes **Then** no mixed birth identity is
   emitted and completeness/diagnostics are exact **And** unaffected process
   truth remains usable.

### Story 3.8: Normalize and Atomically Commit Honest Collection Truth

As an Operator,
I want all five Providers projected into one neutral Observation model,
So that completeness and partial success mean the same thing everywhere.

**Implementation Boundary:** Implement adapter-to-domain normalization,
typed Provider detail, Observation/provenance IDs, obligation outcomes,
complete/incomplete/out-of-scope states, deterministic encounter and final
ordering, strict/partial policy, latest-generation compare-and-swap, immutable
accepted reports/diagnostics/samples, and Snapshot candidate transaction.

**Requirement Mapping:** FR: FR-13, FR-14, FR-17; NFR: NFR-1, NFR-2, NFR-3,
NFR-9, NFR-12, NFR-13, NFR-16; UJ: UJ-1, UJ-3, UJ-5; UX: UX-FND-2,
UX-FND-4, UX-CP-2, UX-ST-3, UX-ST-5, UX-VT-3; AD: AD-2, AD-5, AD-10,
AD-11, AD-13, AD-16, AD-18, AD-21, AD-24, AD-25.

**Dependencies:** Stories 3.1 through 3.7.

**Validation Expectations:** Cross-Provider contract and property tests cover
all outcome states, duplicate identity, encounter ordering, partial/strict
exit matrix, cancelled/superseded/late generations, atomic commit cuts,
diagnostic bounds, sample lineage, and identical normalized bytes.

**Out of Scope:** Promise correlation, finding classification, baseline
acceptance, display ranking, and converting diagnostics into Observations.

**Acceptance Criteria:**

1. **Given** successful reports from all five Providers **When** normalized
   **Then** every item has one neutral Observation identity, typed detail,
   source/scope/encounter provenance, and stable canonical order **And**
   Provider-specific fields do not leak into domain identity rules.
2. **Given** any mix of success, unavailable, timeout, parse failure,
   permission denial, cancelled, and out-of-scope obligations **When** policy
   evaluates **Then** partial mode commits usable truth with explicit withheld
   scope and strict mode returns its deterministic diagnostic exit **And**
   neither mode converts missing evidence to absence.
3. **Given** a newer requested generation, late child, duplicate identity, or
   injected transaction crash **When** a candidate commits **Then** stale truth
   cannot replace current and either the entire accepted candidate plus
   diagnostics/samples commits or none does **And** attempt evidence remains
   bounded.

### Story 3.9: Inspect Bounded Failure-Local Provider Evidence

As an Operator,
I want to inspect one Observation or failed obligation without dumping the
Host,
So that I can diagnose exact Provider truth safely.

**Implementation Boundary:** Implement Provider-neutral inspect projection and
linear/machine commands for exact Observation or obligation ID, typed Provider
detail, source/provenance, bounds, sanitization, redaction, truncation, capture
metadata, diagnostics, ambiguous/not-found results, and no re-collection.

**Requirement Mapping:** FR: FR-15, FR-17; NFR: NFR-1, NFR-2, NFR-7, NFR-8,
NFR-11, NFR-13; UJ: UJ-1, UJ-3, UJ-5; UX: UX-IA-4, UX-CP-6, UX-CP-7,
UX-ST-5, UX-ST-17, UX-A11Y-3, UX-A11Y-4; AD: AD-7, AD-8, AD-9, AD-11,
AD-13, AD-18, AD-20, AD-24.

**Dependencies:** Story 3.8.

**Validation Expectations:** Golden and hostile-text fixtures cover every
Provider detail variant and failure, exact/not-found/ambiguous IDs, redaction,
truncation, non-UTF-8/control input, bounds/provenance, NO_COLOR/TERM=dumb,
stable JSON/exits, and proof that inspection invokes no Collector.

**Out of Scope:** Unbounded logs, interactive search widgets, correlation
evidence, Plane/Git/Telemetry fetching, and lifecycle mutation.

**Acceptance Criteria:**

1. **Given** an exact Observation ID from any Provider **When** inspected
   **Then** neutral identity, source, scope, encounter, typed detail,
   freshness, bounds, redaction, and truncation are shown deterministically
   **And** no current Host lookup changes the stored evidence.
2. **Given** an unavailable or incomplete obligation **When** inspected
   **Then** command, scope, timing, exit/signal, bounded captures, and one safe
   recovery instruction are exposed **And** sibling success remains separate.
3. **Given** hostile text, unknown ID, or ambiguous friendly query **When**
   rendered in linear or JSON form **Then** output is sanitized, bounded, and
   machine-stable with an explicit result **And** no cursor control, secret, or
   arbitrary Provider output reaches the terminal.

## Epic 4: Reconciliation, Baseline, and Morning Brief

Operators can compare declared intent with actual Host truth, see every
coexisting finding and uncertainty, accept an explicit comparison boundary,
and receive one explainable morning Brief with attention, Stack, and Ungrouped
context.

**Primary FR coverage:** FR-18 through FR-29.

**Depends on:** Epic 2 declared intent and Epic 3 scoped Observations. It
produces complete deterministic CLI, linear, and machine Brief value before an
interactive TUI or mutation exists.

### Story 4.1: Correlate Promises and Observations with Explainable Evidence

As an Operator,
I want intent correlated to Host truth by exact and bounded evidence,
So that friendly-name resemblance cannot create health or an action identity.

**Implementation Boundary:** Implement the pure reconciliation use case,
Provider/locator anchor, canonical lexicographic evidence vector, exact
Project/mechanism/source/process and bounded name evidence, conflicts,
candidates, strict maxima, ambiguity, confidence, supports/contradicts/missing,
deterministic order, and decision-contract version.

**Requirement Mapping:** FR: FR-18, FR-26; NFR: NFR-1, NFR-2, NFR-12,
NFR-13; UJ: UJ-1, UJ-3, UJ-5; UX: UX-FND-2, UX-FND-3, UX-FND-4,
UX-CP-5, UX-CP-6; AD: AD-2, AD-11, AD-13, AD-18, AD-21, AD-24.

**Dependencies:** Epic 2 and Epic 3.

**Validation Expectations:** Table/property suites cover every evidence
dimension and conflict, bounded Jaro-Winkler threshold, no-anchor candidates,
equal maxima, multi-instance matching, permutation invariance, stable
fingerprints, and zero post-admission lookup.

**Out of Scope:** Finding labels, safety decisions, baseline movement, Stack
groups, presentation, and mutation.

**Acceptance Criteria:**

1. **Given** exact Provider identity and immutable locator evidence plus
   Project, Launch Mechanism, source, process ownership, and name evidence
   **When** candidate edges are evaluated **Then** the canonical
   lexicographic vector records match/absent/conflict without summing **And**
   anchor conflict rejects the edge.
2. **Given** no anchor, bounded name values at/below the fixed threshold, and
   equal best edges **When** matching runs **Then** no-anchor evidence remains
   candidate-only, below-threshold is absent, and equal maxima are ambiguous
   **And** typed IDs never break an evidence tie.
3. **Given** identical admitted plan/report bytes in different encounter order
   **When** reconciled repeatedly **Then** edges, evidence, confidence, order,
   and fingerprint are identical **And** historical materialized results retain
   their original decision version.

### Story 4.2: Resolve Lifecycle, Evidence, Healthy, Broken, and Unresolved Axes

As an Operator,
I want lifecycle and evidence sufficiency evaluated before health,
So that Collector failure cannot make a Runtime look missing or correct.

**Implementation Boundary:** Implement orthogonal Promise Lifecycle, Evidence
Status, and Promise Outcome axes; active/persistent/expired/closed reasons;
Heartbeat-late and Lease evidence; sufficient/incomplete/stale/out-of-scope;
healthy/broken/unresolved/inactive; intended count; and absence gating.

**Requirement Mapping:** FR: FR-19, FR-20, FR-25; NFR: NFR-1, NFR-2, NFR-10,
NFR-13, NFR-16; UJ: UJ-2, UJ-3; UX: UX-FND-2, UX-FND-4, UX-CP-3,
UX-CP-5, UX-ST-4, UX-ST-5; AD: AD-2, AD-5, AD-17, AD-18, AD-20, AD-21.

**Dependencies:** Story 4.1.

**Validation Expectations:** Cover the complete axis cross-product, exact
Lease/Heartbeat boundaries, reboot/discontinuity, closure reasons, intended
counts, near matches, incomplete absence, conflicts, and deterministic
serialization.

**Out of Scope:** Observation finding labels beyond required inputs,
Safe-to-stop, action planning, and UI severity.

**Acceptance Criteria:**

1. **Given** active finite, active persistent, late-within-Lease, expired, and
   each explicitly closed Promise **When** lifecycle resolves **Then** exactly
   one lifecycle and its timing/reason evidence are retained **And** expiry or
   closure never authorizes Host mutation.
2. **Given** complete, incomplete, stale, or out-of-scope relevant obligations
   **When** active intent is evaluated **Then** healthy/broken require
   sufficient evidence and all other cases are unresolved **And** incomplete
   collection cannot prove no survivor.
3. **Given** intended count with zero, exact, excess, conflicting, and
   candidate-only matches **When** outcome derives **Then** healthy requires
   exact compatible running count and broken requires sufficient zero-running
   evidence **And** near-match/conflict evidence remains inspectable.

### Story 4.3: Identify Orphaned and Exact Duplicate Observations

As an Operator,
I want unmatched and excess exact Observations kept distinct,
So that unexplained work is visible without srvls choosing what to kill.

**Implementation Boundary:** Implement orphaned label with preexisting
Provider-resource context, exact duplicate excess sets relative to intended
count, retained match/ambiguity/completeness evidence, multi-label coexistence,
stable member ordering, and no target recommendation.

**Requirement Mapping:** FR: FR-21, FR-22, FR-26; NFR: NFR-1, NFR-2,
NFR-12, NFR-13; UJ: UJ-1, UJ-5; UX: UX-FND-2, UX-FND-5, UX-CP-3,
UX-CP-5, UX-CP-14, UX-ST-20; AD: AD-2, AD-5, AD-13, AD-18, AD-21, AD-24.

**Dependencies:** Stories 4.1 and 4.2.

**Validation Expectations:** Cover unmatched preexisting/Agent cases, exact
and excess counts, equal ties, incomplete evidence, identity reuse, coexistence
with all other labels, stable ordering, and permutation invariance.

**Out of Scope:** Choosing a duplicate loser, group actions, automatic cleanup,
and durable manual correlation overrides.

**Acceptance Criteria:**

1. **Given** a fresh running Observation with no eligible Promise edge **When**
   labels derive **Then** it is orphaned with no-match and completeness evidence
   **And** Provider management context does not invent an Agent origin.
2. **Given** one Promise with corroborated exact running matches beyond its
   intended count **When** duplicate logic runs **Then** every exact excess
   identity, birth/start evidence, and comparison is retained **And** no member
   is silently recommended for mutation.
3. **Given** ambiguous equal matches, incomplete collection, or conflicting
   identity **When** orphan/duplicate logic evaluates **Then** uncertainty
   remains explicit and safety stays unknown where required **And** assignment
   is not forced to simplify counts.

### Story 4.4: Classify Stale and Hot from Frozen Positive Evidence

As an Operator,
I want stale and hot labels backed by visible policy and sampled evidence,
So that missing telemetry or one transient sample cannot become false certainty.

**Implementation Boundary:** Implement stale positive-evidence policy and hot
resource-history policy over frozen ResourceHistoryCutV1, exact thresholds,
windows/sample counts, immutable samples, metric/source provenance,
three-sample race handling, multi-label coexistence, and insufficient-evidence
behavior.

**Requirement Mapping:** FR: FR-23, FR-24, FR-26; NFR: NFR-1, NFR-2, NFR-9,
NFR-11, NFR-12, NFR-13, NFR-16; UJ: UJ-1, UJ-5; UX: UX-FND-2, UX-VT-3,
UX-CP-5, UX-CP-14, UX-ST-17; AD: AD-5, AD-11, AD-16, AD-18, AD-20, AD-21,
AD-24.

**Dependencies:** Stories 4.1 through 4.3.

**Validation Expectations:** Boundary/property suites cover absent positive
evidence, all stale/hot threshold-window-sample edges, missing telemetry,
resource sample races, concurrent retention, frozen row fingerprints,
multi-label combinations, and ARCH-LIM-9/10 policy variants.

**Out of Scope:** Continuous telemetry ingestion, arbitrary trend analysis,
resource control, and treating stale/hot as authorization.

**Acceptance Criteria:**

1. **Given** positive non-use/obsolescence evidence, absent evidence, and
   values around the configured stale window **When** stale evaluates **Then**
   only supported positive evidence meeting policy creates stale **And**
   source, sample time, value, units, threshold, and provenance remain visible.
2. **Given** CPU/memory samples at, below, and above thresholds with
   sufficient and insufficient counts/windows **When** hot evaluates **Then**
   only the configured rule creates hot **And** the label neither changes
   safety nor erases another finding.
3. **Given** newer samples, retention, baseline acceptance, or a later
   Snapshot after plan admission **When** this generation reconciles **Then**
   only frozen ResourceHistoryCutV1 rows are consumed **And** no later lookup
   changes the result.

### Story 4.5: Identify Unmanaged and Abandoned Runtimes

As an Operator,
I want ownership loss and intent closure represented against surviving exact
Runtimes,
So that forgotten Agent work is visible without automatic termination.

**Implementation Boundary:** Implement unmanaged and abandoned labels from
Durable Ownership, Launch Mechanism, Heartbeat/Lease, exact surviving
Observation, and released/completed/revoked history; retain reasons and
multi-axis truth; prohibit label-driven mutation.

**Requirement Mapping:** FR: FR-25, FR-26; NFR: NFR-1, NFR-2, NFR-10,
NFR-13; UJ: UJ-2, UJ-4; UX: UX-FND-2, UX-FND-5, UX-CP-5, UX-CP-14,
UX-ST-20; AD: AD-2, AD-5, AD-6, AD-17, AD-18, AD-21.

**Dependencies:** Stories 4.1 through 4.4.

**Validation Expectations:** Cover persistence/ownership combinations, late
Heartbeat versus expiry, all close reasons, fresh survivor/no survivor,
incomplete evidence, multiple labels, and no-mutation assertions.

**Out of Scope:** Lease-expiry cleanup, policy remediation, inferred Durable
Ownership, and deletion of Promise history.

**Acceptance Criteria:**

1. **Given** Agent-created observed work without Durable Ownership or reliable
   Launch Mechanism **When** labels derive **Then** the exact Observation is
   unmanaged with missing/conflicting ownership evidence **And** declaration
   alone cannot make it healthy or safe.
2. **Given** a fresh exact Observation surviving Lease expiry or explicit
   release, completion, or revocation **When** reconciliation runs **Then** it
   is abandoned with exact reason and historical Promise reference **And**
   inactive intent with no survivor stays history.
3. **Given** incomplete/stale relevant collection and no positive survivor
   **When** closed or expired intent evaluates **Then** no abandoned absence
   claim is made **And** no label invokes a Host action.

### Story 4.6: Explain Findings and Calculate Safe-to-stop Conservatively

As an Operator,
I want every finding and safety assessment to expose its reasoning,
So that I can decide from evidence instead of a blended status guess.

**Implementation Boundary:** Implement explanation projection and
safe/unsafe/unknown rules over exact fresh identity, collection completeness,
active/persistent intent, instance count, dependencies, ownership, purpose,
lifetime, Launch Mechanism recreation, operation conflicts, expiry/closure,
and exact duplicate excess; retain confidence, policy provenance, missing/
contradictory evidence, and scope limits.

**Requirement Mapping:** FR: FR-18, FR-26, FR-36, FR-38; NFR: NFR-1, NFR-2,
NFR-12, NFR-13, NFR-16; UJ: UJ-1, UJ-3, UJ-4, UJ-5; UX: UX-VT-1,
UX-VT-3, UX-VT-4, UX-CP-5, UX-CP-6, UX-CP-14, UX-ST-20; AD: AD-2, AD-5,
AD-6, AD-11, AD-18, AD-20, AD-21, AD-22.

**Dependencies:** Stories 4.1 through 4.5.

**Validation Expectations:** Decision-table tests cover every required safe
predicate, each independent unsafe predicate, each missing/stale/ambiguous/
contradictory unknown predicate, Provider recreation, dependencies,
operations, duplicate excess, completeness, and deterministic reason order.

**Out of Scope:** Claiming arbitrary business safety, elevating safe to
authorization, planning/executing an action, and auto-remediation.

**Acceptance Criteria:**

1. **Given** fresh exact identity, sufficient collection, known ownership/
   purpose/lifetime/mechanism/dependencies, no active requirement or operation,
   and an allowed closure/expiry/excess reason **When** safety evaluates
   **Then** it is safe with every satisfied predicate and scope limit **And**
   remains advisory.
2. **Given** active/persistent intent, required instance, dependency,
   recreation policy, or conflicting operation **When** safety evaluates
   **Then** it is unsafe with all deterministic reasons **And** unrelated
   positive evidence cannot override it.
3. **Given** missing, stale, ambiguous, or contradictory identity, ownership,
   purpose, lifetime, dependency, recreation, completeness, freshness, or
   correlation **When** no unsafe predicate is proven **Then** safety is
   unknown with exact reasons **And** no finding label converts it to safe.

### Story 4.7: Persist Snapshots and Accept an Explicit Baseline

As an Operator,
I want to choose the exact complete Snapshot starting my next Evidence Window,
So that refresh never silently changes what changed means.

**Implementation Boundary:** Implement SnapshotV1 atomic materialization of
reports, diagnostics, Observations, samples, findings, baseline projection and
fingerprints; latest-current CAS; AcceptedBaselineCut compatibility;
eligibility; deterministic baseline command; TUI-independent acceptance/audit;
explicit incomplete override; pins; retention; and first-run/incompatible
states.

**Requirement Mapping:** FR: FR-27; NFR: NFR-1, NFR-2, NFR-9, NFR-11,
NFR-12, NFR-13, NFR-16; UJ: UJ-1; UX: UX-IA-7, UX-CP-12, UX-ST-16,
UX-IP-6; AD: AD-5, AD-11, AD-16, AD-20, AD-21, AD-24.

**Dependencies:** Stories 4.1 through 4.6 and Story 3.8.

**Validation Expectations:** Fixed-byte/cross-unit fixtures cover atomic
Snapshot/finding commit, latest generation CAS, baseline preimages/fingerprints,
concurrent acceptance, compatibility, zero post-admission lookup, first-run,
incomplete override, pins/retention, crash cuts, and superseded candidates.

**Out of Scope:** Automatic baseline movement, normal acceptance of incomplete
truth, reserializing Provider detail at acceptance, and reevaluating history
under current policy.

**Acceptance Criteria:**

1. **Given** the latest eligible completed generation **When** Snapshot
   transaction commits **Then** reports, diagnostics, Observations, samples,
   materialized findings, baseline projection/fingerprints, plan/policy/
   Promise revisions, and current pointer commit together **And** superseded
   candidates cannot become current.
2. **Given** a compatible complete current Snapshot **When** an Operator
   accepts its exact ID **Then** one transaction moves only the Accepted
   Baseline pointer, records principal/time/timezone/audit, and pins exact bytes
   **And** refresh, schedule, exit, or action cannot accept it.
3. **Given** no/incompatible baseline or an incomplete candidate **When**
   comparison/acceptance is requested **Then** the reason is explicit and no
   change set is invented **And** override succeeds only with nonempty reason,
   acknowledgement, missing scopes, principal, and time.

### Story 4.8: Produce the Complete Change-Aware Morning Brief

As an Operator returning to the Host,
I want one deterministic Brief answering all morning questions,
So that I do not reconstruct state across five Provider tools.

**Implementation Boundary:** Implement new/resolved/changed/persisting
comparison for Promises/Observations/Findings; all eight FR-28 answers;
Evidence Window/timezone; completeness and withheld conclusions; multi-label
counts; deterministic attention rank; exact drill-down IDs; facets/query;
versioned JSON; brief/inspect linear surfaces; and first-run/incompatible
treatment.

**Requirement Mapping:** FR: FR-27, FR-28, FR-32; NFR: NFR-1, NFR-2, NFR-7,
NFR-8, NFR-13; UJ: UJ-1, UJ-3, UJ-5; UX: UX-IA-1, UX-IA-3, UX-IA-10,
UX-CP-1, UX-CP-2, UX-CP-3, UX-CP-5, UX-CP-6, UX-CP-14, UX-CP-15,
UX-IP-11, UX-A11Y-1, UX-A11Y-3, SR-A11Y-1; AD: AD-5, AD-7, AD-8, AD-9,
AD-11, AD-18, AD-21, AD-24.

**Dependencies:** Story 4.7.

**Validation Expectations:** Golden Brief fixtures cover every answer and
change class, multi-label counts, all completeness states, first run,
incompatible baseline, timezone, withheld conclusions, rank/order,
drill-down integrity, facets/query, TERM=dumb/NO_COLOR linear traversal, JSON,
and SM-1/SM-2/SM-6.

**Out of Scope:** Advancing the baseline, hiding labels behind one count,
asserting clean with incomplete evidence, alternate-screen layout, mutation,
and fetching opaque references.

**Acceptance Criteria:**

1. **Given** one frozen current Snapshot and none or one compatible Accepted
   Baseline **When** the Brief composes **Then** it names window, timezone,
   baseline/current, freshness, completeness, all change classes, and all eight
   answers **And** coexisting labels retain separate counts and IDs.
2. **Given** current truth containing Agent work, expected/actual Runtimes,
   missing/unexplained items, lost Heartbeats, diagnostics, and all finding
   labels **When** attention renders **Then** each answer has exact counts and
   drill-down identities in deterministic order **And** no row authorizes
   action.
3. **Given** first run, incompatible baseline, or incomplete required scope
   under TERM=dumb/NO_COLOR **When** linear/machine Brief renders **Then**
   affected obligations and withheld conclusions are explicit and a screen-
   reader user can inspect exact evidence without cursor motion **And** no clean
   or zero-change claim is invented.

### Story 4.9: Group Stack Context Conservatively and Gate Operator Impact

As an Operator,
I want related Runtimes grouped by inspectable evidence after attention,
So that Projects and services are easier to scan without forcing ambiguity.

**Implementation Boundary:** Implement AD-4 absolute grouping tiers, lexical
raw-path normalization, exact Project/native/source/semantic evidence,
residual-member thresholds, deterministic candidate ordering/greedy claim,
nontransitive membership, StackGroupId/labels/collision disambiguation,
confidence/evidence, explicit Ungrouped, Project/Agent/Provider/finding facets,
and the Product Owner beta impact decision record.

**Requirement Mapping:** FR: FR-29; NFR: NFR-1, NFR-2, NFR-8, NFR-13; UJ:
UJ-1, UJ-5; UX: UX-FND-5, UX-IA-2, UX-IA-5, UX-IA-11, UX-CP-3, UX-CP-4,
UX-CP-8, UX-CP-14; AD: AD-4, AD-8, AD-11, AD-13, AD-18, AD-24.

**Dependencies:** Stories 4.1 through 4.8.

**Validation Expectations:** Property/table suites cover each tier, conflicts/
ties, Docker/PM2 precedence, path bytes/parent traversal, semantic tokens,
minimum residuals, specificity/order, collision, no transitive merge,
Ungrouped, facet composition, and a checked beta-impact decision record.

**Out of Scope:** Durable manual group overrides, filesystem
canonicalization, name-only Promise correlation, group mutation, theme, and
using inventory/finding count as operator impact.

**Acceptance Criteria:**

1. **Given** Project, Provider-native, source, and semantic evidence **When**
   grouping candidates form **Then** absolute tiers 400/300/200/100 apply
   without summing/transitive merge and sort by tier, residual count,
   specificity, canonical key **And** native/Project/source need two residual
   members and semantic needs three with a nongeneric prefix.
2. **Given** repeated/dot/parent/non-UTF-8/case-sensitive paths, conflicts,
   name-only evidence, and label collisions **When** grouping runs **Then**
   permitted lexical bytes normalize without filesystem access, invalid/
   ambiguous items remain Ungrouped, and labels disambiguate visibly **And**
   group rows stay read-only.
3. **Given** beta evaluation preparation **When** the Product Owner impact gate
   is reviewed **Then** an approved current Provider-by-Provider baseline,
   canonical-Brief target, window, and privacy-safe method exist **And**
   inventory or finding counts are rejected as user-impact proxies.

## Epic 5: Interactive TUI

Operators can explore the same Brief and evidence through a responsive,
keyboard-complete, accessible terminal interface that preserves focus, stale
truth, partial evidence, and every canonical state without relying on
decoration.

**Primary FR coverage:** FR-30 through FR-34.

**Depends on:** Epic 4 Brief and inspection projections. It remains a complete
read-only experience and does not require lifecycle mutation.

### Story 5.1: Route Presentation and Own the Terminal Lifecycle

As an Operator,
I want srvls to enter an interactive terminal only when eligible,
So that scripts keep stable output and my terminal always restores.

**Implementation Boundary:** Implement pre-side-effect PresentationProfile
routing for explicit formats, redirected streams, interactive eligibility,
legacy table/JSON/Prometheus/Markdown, deprecated fzf migration/ledger, and a
single TerminalSession/Shutdown owner for raw mode, alternate screen, cursor,
mouse/paste policy, panic hook, Ctrl-C, SIGINT, SIGTERM, and idempotent restore.

**Requirement Mapping:** FR: FR-30, FR-33, FR-34; NFR: NFR-1, NFR-6, NFR-7,
NFR-8, NFR-13, NFR-14; UJ: UJ-1, UJ-3; UX: UX-FND-1, UX-FND-6, UX-IA-1,
UX-IP-1, UX-A11Y-5, UX-RP-6; AD: AD-7, AD-8, AD-9, AD-11, AD-14.

**Dependencies:** Epic 4 and compatibility Story 1.2.

**Validation Expectations:** Pseudoterminal and golden matrix covers every
stdin/stdout/stderr TTY combination, explicit format precedence, TERM=dumb,
NO_COLOR, unsupported terminal, fzf flags, normal/error/panic/Ctrl-C/SIGINT/
SIGTERM exits, nested restore calls, and byte-stable redirected output.

**Out of Scope:** TUI layout, action signal disposition, changing frozen
legacy formats without a ledger entry, and using terminal entry to authorize.

**Acceptance Criteria:**

1. **Given** explicit format, redirected stdout, noninteractive stdin, TERM=dumb,
   and eligible TTY combinations **When** routing occurs **Then** exactly one
   profile is selected before Host/state side effects **And** only eligible
   input/output enters the TUI.
2. **Given** fzf/fzf-lines compatibility invocations **When** routed **Then**
   documented fzf behavior points into the TUI and fzf-lines retires only
   through an approved deviation **And** inherited explicit formats stay byte-
   compatible.
3. **Given** normal quit, error, panic, Ctrl-C, SIGINT, or SIGTERM at every
   terminal phase **When** shutdown runs **Then** raw mode, screen, cursor, and
   input modes restore exactly once **And** the original exit/signal outcome is
   preserved.

### Story 5.2: Render the Brief-First Explorer Across Terminal Sizes

As an Operator,
I want a Brief-first Explorer that collapses predictably,
So that attention, completeness, identity, and state survive on any supported
terminal.

**Implementation Boundary:** Implement app shell, brief-summary,
completeness-banner, attention rows, Stack/Ungrouped group rows, list/detail
panes, status/context lines, DESIGN cell spacing/typography, full/compact/
narrow/below-minimum layouts, deterministic live resize, scroll indicators,
stable reading order, and read-only group affordances.

**Requirement Mapping:** FR: FR-28, FR-29, FR-31, FR-33, FR-34; NFR: NFR-1,
NFR-2, NFR-8, NFR-13; UJ: UJ-1, UJ-5; UX: UX-FND-1, UX-FND-2, UX-IA-1,
UX-IA-2, UX-CP-1, UX-CP-2, UX-CP-3, UX-CP-4, UX-RP-1, UX-RP-2, UX-RP-3,
UX-RP-4, UX-RP-5; AD: AD-5, AD-8, AD-11, AD-14, AD-18.

**Dependencies:** Story 5.1 and Stories 4.8–4.9.

**Validation Expectations:** Ratatui/TestBackend goldens at every breakpoint
and live-resize sequence cover complete/incomplete Briefs, long/raw-byte text,
multi-label rows, Stack/Ungrouped, no/large inventories, scroll, focus
visibility, below-minimum recovery, and deterministic cell bounds.

**Out of Scope:** Action Menu behavior, terminal theme invention, hidden hover
content, group mutation, and dropping completeness to fit.

**Acceptance Criteria:**

1. **Given** full, compact, and narrow supported widths **When** the same Brief
   renders **Then** reading order, attention before groups, completeness,
   exact identity/state/labels, and selected context persist while optional
   columns collapse in the specified order **And** no semantic relies on color.
2. **Given** a terminal below minimum size **When** rendered/resized **Then**
   one explicit required/current-size message and quit/help path replace the
   main layout **And** returning to a supported size restores the same selected
   identity and scroll context.
3. **Given** hostile or overlong rows and multiple labels **When** laid out
   **Then** cell bounds are never exceeded, truncation is marked, details
   remain reachable, and labels are not collapsed into one severity **And**
   Stack/Project/Agent/finding rows expose no action affordance.

### Story 5.3: Navigate, Search, Filter, and Preserve Stable Focus

As a keyboard Operator,
I want complete navigation and visible query constraints,
So that refresh and filtering never make me act on a different item.

**Implementation Boundary:** Implement canonical keymap for movement,
page/home/end, expand/collapse, pane focus, inspect/back, help, refresh, search,
facet filter, clear, quit; query grammar/matching shared with linear surface;
visible filter bar; filtered-empty recovery; focus by exact identity and
deterministic fallback; scroll preservation; disabled-key explanations.

**Requirement Mapping:** FR: FR-29, FR-31, FR-34; NFR: NFR-1, NFR-8,
NFR-12, NFR-13; UJ: UJ-1, UJ-5; UX: UX-IA-2, UX-IA-5, UX-IA-8, UX-IA-11,
UX-CP-8, UX-CP-13, UX-IP-2, UX-IP-3, UX-ST-7, UX-ST-19, UX-A11Y-2;
AD: AD-8, AD-11, AD-13, AD-14, AD-18.

**Dependencies:** Story 5.2.

**Validation Expectations:** Model/property and PTY tests cover every key and
focus target, composed facets/query, Unicode/raw-byte matching policy,
filtered-empty, selected removal, group collapse, reorder, refresh,
small-terminal transition, help return, rapid input, and identity-safe action
handoff absence.

**Out of Scope:** Mouse-only interaction, fuzzy matching that differs from
linear mode, durable saved searches, and action initiation.

**Acceptance Criteria:**

1. **Given** any Brief/Explorer/detail/help focus **When** documented keys run
   **Then** movement, expansion, pane change, inspect, return, refresh, help,
   and quit have deterministic results **And** unsupported keys do not mutate
   state.
2. **Given** combined Project, Agent, Provider, finding facets and a text query
   **When** constraints apply **Then** the filter bar restates every constraint,
   canonical matching/order match the linear surface, and a filtered-empty
   recovery clears/narrows constraints **And** refresh preserves them.
3. **Given** selected identity disappears, moves, is filtered, or its group
   collapses **When** the model updates **Then** focus follows the exact
   identity if present, otherwise the specified nearest/parent/fallback order
   **And** row position alone never transfers selection.

### Story 5.4: Inspect Runtime, Evidence, and Provider Detail Together

As an Operator,
I want one detail flow joining intent, actual truth, and bounded evidence,
So that diagnosis does not require switching Provider tools.

**Implementation Boundary:** Implement runtime-detail, evidence-table, and
provider-detail components for Promise, Heartbeat, Lease, Observation,
Project, Agent, Launch Mechanism, lifecycle/evidence/outcome/labels/safety,
supports/contradicts/missing, source/provenance, opaque references, bounds,
redaction/truncation, tabs/sections, exact IDs, and return path.

**Requirement Mapping:** FR: FR-15, FR-26, FR-32, FR-33, FR-34; NFR: NFR-1,
NFR-2, NFR-8, NFR-11, NFR-13; UJ: UJ-1, UJ-3, UJ-4, UJ-5; UX: UX-IA-3,
UX-IA-4, UX-CP-5, UX-CP-6, UX-CP-7, UX-CP-14, UX-ST-17, UX-A11Y-1,
UX-A11Y-4; AD: AD-2, AD-8, AD-11, AD-13, AD-18, AD-20.

**Dependencies:** Stories 5.2 and 5.3.

**Validation Expectations:** Golden/detail-model tests cover every axis/label/
Provider variant, Promise-only and Observation-only cases, ambiguity,
complete/incomplete evidence, opaque references, raw bytes/control text,
redaction, truncation, narrow layout, scroll/focus return, and no Host lookup.

**Out of Scope:** Fetching Plane/Git/Telemetry references, unbounded logs,
editing intent, action confirmation, and presenting opaque references as truth.

**Acceptance Criteria:**

1. **Given** a correlated, Promise-only, Observation-only, or ambiguous item
   **When** detail opens **Then** exact IDs, intent, Host truth, all orthogonal
   axes/labels/safety, ownership, purpose, lifetime, mechanism, and timestamps
   are shown without invented fields **And** back returns to the prior identity.
2. **Given** supports, contradictions, missing evidence, Provider detail, or a
   collection failure **When** evidence is selected **Then** source, scope,
   command provenance, bounds, redaction, truncation, policy, and recovery are
   inspectable **And** no re-collection or opaque-reference fetch occurs.
3. **Given** hostile/non-UTF-8/long text in any detail **When** rendered at all
   breakpoints **Then** control sequences are neutralized, identity remains
   byte-exact, truncation is explicit, and content remains keyboard reachable
   **And** terminal state cannot be altered by Host text.

### Story 5.5: Keep Stale Truth Visible During Nonblocking Refresh

As an Operator,
I want refresh to preserve the last trustworthy view and disclose progress,
So that slow or partial collection never blanks or mislabels my screen.

**Implementation Boundary:** Implement async app event loop, explicit loading/
refreshing/stale/partial/unavailable/empty/filtered-empty model, current vs
candidate generation, per-obligation progress/deadline, stale-while-refreshing,
latest-wins application, pending update notices, refresh cancellation, baseline
state integration, input/render isolation, and no action state.

**Requirement Mapping:** FR: FR-17, FR-31, FR-34; NFR: NFR-2, NFR-3, NFR-6,
NFR-12, NFR-13, NFR-16; UJ: UJ-1, UJ-3; UX: UX-CP-2, UX-CP-11,
UX-ST-1, UX-ST-2, UX-ST-3, UX-ST-4, UX-ST-5, UX-ST-6, UX-ST-7, UX-ST-16,
UX-BUD-1, UX-BUD-2, UX-BUD-3, UX-BUD-5; AD: AD-5, AD-10, AD-11, AD-14,
AD-21.

**Dependencies:** Stories 5.1 through 5.4 and Epic 3 generation contracts.

**Validation Expectations:** Deterministic event-loop tests and constrained-
Host measurements cover initial load, fast/slow/failed/partial/overlapping
refresh, input bursts, resize, cancel, superseded/late results, pending update,
baseline changes, stable focus, stale badges/times, 30-run p95 budgets, and
terminal restoration.

**Out of Scope:** Mutating during refresh, making stale evidence fresh by
display, clearing old truth before candidate commit, and hiding slow scopes.

**Acceptance Criteria:**

1. **Given** a current Snapshot **When** refresh starts or exceeds the slow
   threshold **Then** current rows remain visible with stale/refreshing text,
   candidate generation and obligation progress/deadline are named, and input
   remains responsive **And** no spinner/animation carries sole meaning.
2. **Given** partial, unavailable, cancelled, superseded, late, or successful
   generation results **When** delivered **Then** only latest eligible success
   replaces current, every failure/withheld scope remains visible, and focus is
   reconciled by exact identity **And** blank/clean truth is never invented.
3. **Given** ARCH-HOST-1 fixtures over 30 post-warm-up iterations **When**
   budgets are measured **Then** local feedback, fast/slow refresh disclosure,
   and pending-update p95 meet UX-BUD defaults/ranges **And** environment,
   fixtures, commands, and raw samples are recorded.

### Story 5.6: Preserve Text-First Meaning, Accessibility, and Hostile-Text Safety

As an Operator using colorless, ASCII, or assistive output,
I want every state and control communicated in stable text,
So that decoration, motion, Unicode, or trusted Host strings are never required.

**Implementation Boundary:** Implement theme inheritance and optional
accessible styles, text-first markers and labels, ASCII/NO_COLOR modes,
contrast-safe optional color roles, no icon-only meaning, motion-free progress,
focus cues, sanitizer at all terminal boundaries, stable reading order, and
parity links to the complete human-linear surface.

**Requirement Mapping:** FR: FR-33, FR-34; NFR: NFR-6, NFR-7, NFR-8,
NFR-11, NFR-13; UJ: UJ-1, UJ-3, UJ-4; UX: UX-FND-1, UX-VT-1, UX-VT-2,
UX-A11Y-1, UX-A11Y-2, UX-A11Y-3, UX-A11Y-4, UX-A11Y-5, UX-RP-3,
UX-RP-4, UX-RP-6, SR-A11Y-1; AD: AD-7, AD-8, AD-11, AD-13, AD-14.

**Dependencies:** Stories 5.1 through 5.5 and Story 4.8.

**Validation Expectations:** Cell/golden/PTY tests under default, NO_COLOR,
ASCII, TERM=dumb, hostile text, screen-reader linear fixtures, every focus/state
marker, contrast lint where color exists, no animation requirement, redirected
cleanliness, and injected panic/signal restoration.

**Out of Scope:** Shipping a product palette/font, requiring emoji/Nerd Fonts,
screen-reader cursor interception in alternate screen, and replacing the linear
alternative with documentation.

**Acceptance Criteria:**

1. **Given** color, Unicode, glyphs, and animation disabled **When** every
   canonical read-only state renders **Then** text identifies meaning, focus,
   selection, completeness, freshness, labels, safety, and controls **And**
   information/order matches decorated mode.
2. **Given** ANSI/OSC/DCS controls, bidi/zero-width characters, tabs/newlines,
   non-UTF-8 bytes, and overlong Host text **When** rendered **Then** terminal
   controls cannot execute, substitutions/truncation are explicit, and exact
   raw identity remains inspectable safely **And** layout bounds hold.
3. **Given** TERM=dumb and NO_COLOR **When** the complete morning fixture runs
   through the linear surface **Then** all eight answers, incomplete evidence,
   exact drill-down, and recovery are available without cursor motion **And**
   the TUI advertises the same canonical command path.

### Story 5.7: Complete Help, Configuration Recovery, State, and UX Budget Gates

As an Operator,
I want in-context help and every read-only state proven under the UX budgets,
So that the TUI is learnable and predictable before actions are added.

**Implementation Boundary:** Implement help overlay with context keymap/
vocabulary/recovery, invalid-config pre-TUI and valid-policy detail, canonical
read-only state/component matrix, small-terminal help/quit, resize coalescing,
render/input instrumentation, ARCH-HOST-1 runner, golden ownership/update
workflow, and aggregate TUI/linear accessibility gate.

**Requirement Mapping:** FR: FR-30 through FR-34; NFR: NFR-1, NFR-2, NFR-6,
NFR-8, NFR-13, NFR-16; UJ: UJ-1, UJ-3, UJ-5; UX: UX-IA-8, UX-IA-12,
UX-CP-13, UX-IP-12, UX-ST-1 through UX-ST-7, UX-ST-16 through UX-ST-20,
UX-RP-1 through UX-RP-6, UX-BUD-1, UX-BUD-2, UX-BUD-3, UX-BUD-5,
UX-BUD-7; AD: AD-7, AD-8, AD-11, AD-14, AD-19, AD-20.

**Dependencies:** Stories 5.1 through 5.6.

**Validation Expectations:** The aggregate matrix enumerates every mapped
state/component/profile/breakpoint, every key and recovery path, invalid and
valid configuration detail, resize bursts, stable focus, visual goldens,
TERM=dumb/NO_COLOR, terminal restoration, and 30-run p95 UX-BUD evidence with
default/range/provenance.

**Out of Scope:** Action states UX-ST-8 through UX-ST-15, release phases,
telemetry about the user, accepting unreviewed golden changes, and beta release.

**Acceptance Criteria:**

1. **Given** any read-only context, filtered/empty/partial state, invalid
   configuration, or below-minimum terminal **When** help or recovery is
   requested **Then** keys, vocabulary, current constraints, effective policy,
   exact error/source/range, and one safe next step are available **And**
   closing help restores prior exact focus.
2. **Given** every read-only canonical state, component, presentation profile,
   and responsive breakpoint **When** the aggregate matrix runs **Then** a
   checked fixture/golden and deterministic assertion exist for each row
   **And** missing/unwired rows fail the AD-11 gate.
3. **Given** local input/render/resize and refresh fixtures on ARCH-HOST-1
   **When** 30 post-warm-up iterations are measured **Then** applicable
   UX-BUD-1/2/3/5/7 p95 values meet effective policy **And** raw evidence,
   environment, toolchain, and fixture fingerprints are retained.

## Epic 6: Safe Exact-Target Actions

Operators can discover, plan, confirm, execute, and verify one supported
Provider-native lifecycle operation against one revalidated identity, including
Promise-origin Start, while groups stay read-only and every race or uncertainty
ends truthfully.

**Primary FR coverage:** FR-35 through FR-41.

**Depends on:** Epic 3 exact Provider identities, Epic 4 safety evidence, and
Epic 5 interaction shell. The same plan and operation contracts also work
non-interactively.

### Story 6.1: Discover Supported Actions Including Promise-Origin Start

As an Operator,
I want one discoverable Action Menu explaining availability,
So that I can find the exact supported path without guessing a shortcut.

**Implementation Boundary:** Implement ProviderCapability planning and
read-only Action Menu for exact Observation targets plus an explicit broken/
unresolved Promise-origin Start entry; start/stop/restart/disable/delete/signal
capabilities; documented accelerators; disabled/unsupported/stale/incomplete/
unsafe/unknown explanations; group-row prohibition; cron read-only; and no
side effect.

**Requirement Mapping:** FR: FR-35, FR-36, FR-41; NFR: NFR-1, NFR-2, NFR-5,
NFR-8, NFR-13; UJ: UJ-3, UJ-4, UJ-5; UX: UX-IA-6, UX-CP-9, UX-IP-4,
UX-ST-8, UX-ST-20, UX-A11Y-1; AD: AD-3, AD-6, AD-8, AD-11, AD-15, AD-18,
AD-22.

**Dependencies:** Epic 5, Story 4.6 safety, and Epic 3 Provider identities.

**Validation Expectations:** Capability/menu matrix covers every Provider,
action, lifecycle/evidence/safety/freshness state, Promise-only start,
ambiguous/duplicate/group targets, cron, direct process, keyboard/linear entry,
and proof that opening/closing the menu invokes no action port.

**Out of Scope:** Confirmation, durable ActionPlan, mutation, raw-mode
authorization, group actions, cron mutation, and direct-process start.

**Acceptance Criteria:**

1. **Given** one exact selected Observation **When** the Action Menu opens
   **Then** only Provider-declared start/stop/restart/disable/delete/signal
   capabilities appear with accelerator, risk, requirement, and enabled/
   disabled reason **And** opening/selecting for preview has no side effect.
2. **Given** a broken or unresolved Promise with an inspectable supported
   Launch Mechanism and no Observation **When** the menu opens from Promise
   detail **Then** an explicit Start path targets that frozen Promise revision
   and mechanism evidence **And** no direct-process or inferred command start
   is invented.
3. **Given** cron, a Stack/Project/Agent/finding group, ambiguous identity,
   stale/incomplete evidence, or unsupported operation **When** actions are
   requested **Then** mutation is disabled with exact explanation and recovery
   **And** navigation never turns a group into a hidden bulk target.

### Story 6.2: Freeze the ActionPlan and Require Cancel-First Confirmation

As an Operator,
I want the exact proposed effect frozen and restated before commitment,
So that later refresh or selection movement cannot change what I approve.

**Implementation Boundary:** Implement immutable canonical ActionPlanV1 with
OperationId/idempotency key, source generation/Snapshot, exact target identity
or Promise revision, Provider capability/op, effect/risk, safety evidence,
preconditions, expected postcondition, privilege request, deadlines/bounds,
fingerprint/expiry; confirmation dialog; cancel-first focus; destructive and
unknown-safety acknowledgements; and plan/confirm audit.

**Requirement Mapping:** FR: FR-36, FR-38, FR-39, FR-41; NFR: NFR-1, NFR-2,
NFR-5, NFR-9, NFR-12, NFR-13, NFR-16; UJ: UJ-3, UJ-4, UJ-5; UX: UX-CP-10,
UX-IP-5, UX-IP-7, UX-ST-8, UX-ST-9, UX-ST-20, UX-A11Y-1; AD: AD-6, AD-11,
AD-15, AD-20, AD-21, AD-22, AD-24.

**Dependencies:** Story 6.1.

**Validation Expectations:** Golden/model tests cover all action types,
safe/unsafe/unknown, destructive acknowledgements, cancel/escape/default focus,
resize, source refresh/selection movement, plan expiry, canonical bytes/
fingerprint, identical/different retries, and no effect before durable
confirmation.

**Out of Scope:** Identity revalidation, command execution, outcome
verification, broad sudo, and treating Safe-to-stop as authorization.

**Acceptance Criteria:**

1. **Given** an enabled capability **When** planning runs **Then** immutable
   plan bytes freeze exact target/revision, source generation, operation,
   effect, risk, safety evidence, privilege, bounds, expiry, and expected
   postcondition **And** fingerprint is stable under identical input.
2. **Given** stop, disable, delete, signal, or unknown-safety action **When**
   confirmation renders **Then** exact identity, Provider, effect, risk,
   supports/missing evidence, source age, and acknowledgement are visible with
   Cancel focused **And** Enter cannot imply consent from row selection.
3. **Given** cancel, escape, resize, refresh, navigation, expired plan, or
   changed plan fingerprint **When** confirmation resolves **Then** no
   operation is submitted and a fresh plan is required where applicable
   **And** the reason is deterministic and audited.

### Story 6.3: Revalidate Exact Identity and Scope Privilege Before Mutation

As an Operator,
I want the target and required privilege rechecked immediately before effect,
So that PID, container, PM2, unit, or Promise reuse cannot redirect my action.

**Implementation Boundary:** Implement Provider-specific fresh identity probes
for Docker full ID/creation, PM2 daemon/ID/PID/birth, systemd unit/scope and
process birth, direct PID/boot/start/exe fingerprint, and Promise revision/
Launch Mechanism; compare every frozen precondition; classify changed,
vanished, ambiguous, unsupported, or permission failure; and construct one
narrow explicit privilege request outside raw-mode authorization.

**Requirement Mapping:** FR: FR-37, FR-38, FR-41; NFR: NFR-1, NFR-2, NFR-4,
NFR-5, NFR-12, NFR-13; UJ: UJ-3, UJ-4; UX: UX-FND-3, UX-CP-10, UX-ST-10,
UX-ST-20, UX-VT-4; AD: AD-6, AD-11, AD-13, AD-15, AD-20, AD-22.

**Dependencies:** Story 6.2 and exact Provider identities from Epic 3.

**Validation Expectations:** Race matrix covers every identity field and
Provider, vanish/recreate/reuse, same friendly name/new birth, Promise revision
or mechanism change, permission denial, probe timeout, end-of-options, narrow
privilege allow/deny, and assertion that refusal invokes no mutation command.

**Out of Scope:** Executing the operation, retrying changed targets
automatically, whole-process elevation, interactive privilege prompts in raw
mode, and friendly-name fallback.

**Acceptance Criteria:**

1. **Given** a confirmed plan whose fresh immutable identity and preconditions
   still match **When** preflight runs **Then** one signed/typed launch
   authorization names the exact Provider operation and narrow privilege
   **And** it is bound to plan fingerprint and OperationId.
2. **Given** target vanished, was recreated/reused, changed birth/revision/
   mechanism, became ambiguous, or no longer supports the operation **When**
   preflight runs **Then** mutation is refused as identity changed with old/new
   evidence **And** no action command is spawned.
3. **Given** privilege is required **When** authorization is acquired **Then**
   only the selected Provider operation/target/argv is eligible through the
   non-raw helper contract **And** denial/cancellation stays explicit without
   elevating the TUI process.

### Story 6.4: Admit One Operation Atomically and Own Its Handoffs

As an Operator,
I want a confirmed action admitted exactly once before execution,
So that crashes and duplicate input cannot produce an untracked Host effect.

**Implementation Boundary:** Implement atomic Operation admission from
confirmed plan/preflight; OperationId/idempotency uniqueness; source-generation
and plan pins; durable planned/confirmed/admitted state and audit; action-pool
slot reservation; launch-record handoff before spawn; verification-request/
result handoffs; OperationCoordinator sole terminal owner; stale takeover; and
release-admission interaction.

**Requirement Mapping:** FR: FR-39, FR-40; NFR: NFR-1, NFR-2, NFR-9,
NFR-12, NFR-13, NFR-16; UJ: UJ-3, UJ-4; UX: UX-CP-11, UX-IP-7, UX-ST-11,
UX-ST-12; AD: AD-6, AD-11, AD-16, AD-20, AD-21, AD-22, AD-23, AD-24.

**Dependencies:** Stories 6.2 and 6.3.

**Validation Expectations:** Transaction/state-machine tests inject crash/
owner loss at every plan-confirm-admit-launch-verify-terminal cut; cover
duplicate/different keys, pool full, stale coordinator takeover, release lock,
pin retention, late worker/result, and exactly one terminal authority.

**Out of Scope:** Provider command semantics, deciding verification evidence,
TUI notification rendering, and release transaction execution.

**Acceptance Criteria:**

1. **Given** a confirmed, revalidated plan **When** admission commits **Then**
   operation, plan/preflight bytes, audit, pins, pool reservation, and initial
   coordinator ownership become durable together **And** no Host effect may
   precede the launch handoff.
2. **Given** duplicate submission/retry or rapid repeated keys **When**
   admitted **Then** identical requests return the existing OperationId/result
   and different requests conflict **And** at most one launch authorization
   exists.
3. **Given** crash or owner loss before/after launch or verification handoff
   **When** recovery takes ownership **Then** it resumes from durable evidence
   without blindly replaying a possibly executed effect **And** exactly one
   coordinator can publish terminal outcome.

### Story 6.5: Execute Typed Provider-Native Operations

As an Operator,
I want supported lifecycle effects performed through exact Provider semantics,
So that action behavior is bounded, least-privileged, and never shell-invented.

**Implementation Boundary:** Implement ActionExecutor ports/adapters for
systemd start/stop/restart/disable, Docker start/stop/restart/delete, PM2 start/
stop/restart/delete where identity/mechanism supports it, and direct-process
configured signal; explicit argv/end-of-options, per-op deadlines/capture,
typed execution evidence, Promise-origin Start mechanism resolution, cron
read-only, no direct-process Start, and no verification/outcome decision.

**Requirement Mapping:** FR: FR-35, FR-36, FR-39, FR-41; NFR: NFR-2, NFR-3,
NFR-4, NFR-5, NFR-11, NFR-13, NFR-16; UJ: UJ-3, UJ-4; UX: UX-IP-7,
UX-ST-11, UX-ST-20, UX-VT-3; AD: AD-3, AD-6, AD-10, AD-11, AD-15, AD-20,
AD-22.

**Dependencies:** Story 6.4 and CommandRunner Story 1.8.

**Validation Expectations:** Fake-port argv golden matrix covers each
Provider/action/status, Promise Start, direct signals, leading-hyphen/hostile
identities, timeout/exit/signal/truncation, privilege, cancellation boundary,
cron/direct unsupported paths, and no shell or outcome classification.

**Out of Scope:** Verification, outcome precedence, broad process killing,
arbitrary command execution, cron mutation, and action chaining.

**Acceptance Criteria:**

1. **Given** an admitted exact systemd/Docker/PM2 operation **When** execution
   starts **Then** the adapter emits only the canonical argv/env/cwd/privilege/
   deadline contract with immutable identity **And** bounded raw execution
   evidence is persisted under the OperationId.
2. **Given** an admitted Promise-origin Start or direct-process signal **When**
   executed **Then** Start uses only the frozen inspectable Launch Mechanism
   and signal uses exact PID/birth plus configured signal **And** no direct
   Start or arbitrary command path is invented.
3. **Given** cron, unsupported capability, changed adapter precondition,
   timeout, command failure, or cancellation before launch **When** executor
   responds **Then** one typed execution result is stored without shell
   interpolation **And** it does not claim the postcondition or terminal
   Action Outcome.

### Story 6.6: Isolate Asynchronous Actions from Refresh and Navigation

As an Operator,
I want each operation to remain attached to its exact target while I continue
using srvls,
So that refresh races or navigation cannot misattribute progress or results.

**Implementation Boundary:** Implement separate bounded action pool, per-
Operation actor/task, typed event channel, source-generation and identity
binding, duplicate suppression, queue/admitted/running/verifying state,
nonblocking TUI status, pending Snapshot updates, refresh coexistence,
navigation independence, operation history, and one-result notification.

**Requirement Mapping:** FR: FR-39, FR-41; NFR: NFR-1, NFR-2, NFR-3, NFR-6,
NFR-9, NFR-12, NFR-13, NFR-16; UJ: UJ-3, UJ-4, UJ-5; UX: UX-CP-11,
UX-IP-7, UX-ST-11, UX-ST-12, UX-BUD-4, UX-BUD-5; AD: AD-6, AD-10, AD-11,
AD-14, AD-20, AD-22.

**Dependencies:** Stories 6.4 and 6.5 plus Epic 5 event loop.

**Validation Expectations:** Deterministic concurrency tests cover pool bounds,
many operations/refreshes/input events, duplicate submit, selection/filter/
group changes, target disappearance, late/stale events, pending updates, quit/
signal, fairness, and 30-run p95 submit/pending-feedback budgets.

**Out of Scope:** Bulk/group actions, optimistic truth mutation, using refresh
workers for actions, and choosing final Action Outcome.

**Acceptance Criteria:**

1. **Given** multiple admitted operations and overlapping refresh **When**
   tasks run **Then** action and collection pools obey separate frozen bounds,
   input/render remains responsive, and every event carries OperationId,
   target, source generation, and phase **And** no row position can receive it.
2. **Given** navigation, filtering, group collapse, target disappearance, or a
   newer Snapshot **When** progress arrives **Then** status remains attached to
   OperationId/exact identity and one pending-update notice explains stale
   source truth **And** selection never retargets execution.
3. **Given** duplicate submit, late task event, pool saturation, or cancellation
   before launch **When** processed **Then** no duplicate effect is spawned,
   canonical queued/refused state is durable, and UX-BUD submit/pending feedback
   is met **And** terminal truth remains coordinator-owned.

### Story 6.7: Verify Fresh Post-Action Truth and Publish One Outcome

As an Operator,
I want every operation resolved from fresh evidence under one precedence,
So that command exit alone can never masquerade as verified Host truth.

**Implementation Boundary:** Implement Provider-specific fresh verification
plan after execution, exact identity/postcondition probes, bounded retries/
deadline, execution and verification evidence, canonical outcome precedence
for verified, executed-unverified, refused, timed-out, failed, contradiction/
identity-race handling, one terminal compare-and-set, audit/history, and safe
recovery instruction.

**Requirement Mapping:** FR: FR-37, FR-40; NFR: NFR-1, NFR-2, NFR-3, NFR-9,
NFR-12, NFR-13, NFR-16; UJ: UJ-3, UJ-4; UX: UX-CP-11, UX-IP-7,
UX-ST-10, UX-ST-12, UX-ST-13, UX-ST-14, UX-ST-15, UX-BUD-6, UX-VT-4;
AD: AD-5, AD-6, AD-11, AD-18, AD-20, AD-21, AD-22, AD-24.

**Dependencies:** Stories 6.3 through 6.6.

**Validation Expectations:** Canonical outcome matrix covers every action,
preflight refusal, no-launch, successful/failed/timed-out execution, fresh
matching/missing/contradictory/incomplete/unavailable verification, identity
reuse, timeout boundaries, late result, crash/takeover, exactly-once terminal
CAS, precedence, and SM-3.

**Out of Scope:** Treating exit zero as verified, changing the Accepted
Baseline, automatically retrying destructive effects, and hiding contradictory
verification.

**Acceptance Criteria:**

1. **Given** execution evidence and a fresh exact verification observation
   proving the planned postcondition **When** outcome resolves **Then** exactly
   verified is published with before/execute/after evidence **And** one terminal
   CAS/audit record commits.
2. **Given** a launched effect whose verification is incomplete, unavailable,
   timed out, identity-changed, or contradictory **When** precedence applies
   **Then** executed-unverified, timed-out, or failed is chosen exactly as the
   canonical matrix specifies **And** success is never inferred from command
   exit.
3. **Given** preflight refusal/no launch, crash takeover, duplicate/late
   verification, or competing terminal writers **When** resolved **Then**
   refused or the evidence-backed terminal result wins exactly once and later
   inputs cannot rewrite it **And** one safe recovery instruction is shown.

### Story 6.8: Complete Signal-Safe TUI and Human-Linear Action Journeys

As an Operator using either the TUI or a plain terminal,
I want the full exact action journey and in-flight exit behavior proven,
So that accessibility and shutdown never weaken action safety.

**Implementation Boundary:** Implement Action Menu/confirmation/status/outcome
TUI integration; versioned plan/confirm/status/result linear and machine
commands; UX-IP-10 exit/signal disposition by operation phase; terminal restore
before any external authorization; recover/status command; all action states;
full SR-A11Y-1 action path; action budget/golden/PTY/FD3/storage matrices in the
aggregate gate.

**Requirement Mapping:** FR: FR-35 through FR-41; NFR: NFR-1, NFR-2, NFR-5,
NFR-6, NFR-7, NFR-8, NFR-9, NFR-12, NFR-13; UJ: UJ-3, UJ-4, UJ-5; UX:
UX-IA-6, UX-CP-9, UX-CP-10, UX-CP-11, UX-CP-15, UX-IP-4, UX-IP-5,
UX-IP-7, UX-IP-10, UX-IP-11, UX-A11Y-3, UX-A11Y-5, UX-ST-8 through UX-ST-15,
UX-BUD-4, UX-BUD-5, UX-BUD-6, SR-A11Y-1; AD: AD-6, AD-7, AD-8, AD-9,
AD-11, AD-14, AD-15, AD-22, AD-24.

**Dependencies:** Stories 6.1 through 6.7 and Epic 5.

**Validation Expectations:** PTY/linear/machine end-to-end matrix covers
Promise Start and each Provider action/outcome, cancel-first/unknown safety,
identity races, refresh/navigation, every phase at quit/Ctrl-C/SIGINT/SIGTERM,
terminal restoration, owner recovery, TERM=dumb/NO_COLOR screen-reader path,
clean channels, and 30-run UX-BUD p95 evidence.

**Out of Scope:** Release locking, bulk/group action, raw-mode privilege prompt,
automatic cleanup, and claiming external business safety.

**Acceptance Criteria:**

1. **Given** complete/incomplete evidence and each exact supported target under
   TERM=dumb/NO_COLOR **When** the human-linear journey plans, reviews,
   confirms/cancels, watches, and inspects an outcome **Then** every value
   available in TUI is available without cursor motion **And** all five FR-40
   outcomes and identity-race paths are distinguishable.
2. **Given** quit, Ctrl-C, SIGINT, or SIGTERM while planned, queued, launched,
   verifying, or terminal **When** shutdown occurs **Then** the specified
   cancel/detach/wait/recover disposition is explicit, terminal restores first,
   and durable ownership preserves the operation **And** no launched effect is
   blindly replayed.
3. **Given** the aggregate action gate and ARCH-HOST-1 profile **When** run
   **Then** capability, planning, confirmation, identity, privilege, storage,
   execution, races, outcome, signals, linear accessibility, and UX-BUD lanes
   all have checked fixtures and pass **And** any missing AD-11 matrix row
   fails acceptance.

## Epic 7: Release and Recovery

Operators can install or upgrade one checksummed Rust binary and its state and
managed consumers as a quiesced transaction, prove timer-originated consumer
health, survive owner loss at every effect boundary, and restore or roll back
one known-good pair without split truth.

**Primary FR coverage:** FR-42 and FR-43.

**Depends on:** The completed binary, state, compatibility, action-fencing, and
aggregate validation contracts from Epics 1 through 6. It is the only release
and rollback owner.

### Story 7.1: Build and Admit a Verifiable Standalone Release Artifact

As an Operator,
I want a checksummed self-identifying binary proven on the supported baseline,
So that installation never activates an unknown build.

**Implementation Boundary:** Implement locked release build for Rust 2024/MSRV
1.88, version/build/schema/grammar identity, reproducible metadata, stripping/
single-binary packaging, SHA-256 manifest, signature/provenance hooks,
glibc-2.42 ABI/symbol proof, forbidden dependency/descriptor checks, staged
version/self-check smoke, and ReleaseArtifactV1 canonical record.

**Requirement Mapping:** FR: FR-42; NFR: NFR-1, NFR-2, NFR-14, NFR-15;
UJ: UJ-6; UX: UX-IA-9, UX-CP-16, UX-IP-8, UX-VT-3; AD: AD-11, AD-12,
AD-13, AD-20, AD-23, AD-24.

**Dependencies:** Epic 1 foundation gate and completed Epics 2–6.

**Validation Expectations:** Reproducible-build lane, checksum corruption,
version/schema mismatch, glibc symbol ceiling, dynamic dependency allowlist,
single-binary inventory, staged execution/no-state-mutation smoke, canonical
record bytes, and release provenance are gated.

**Out of Scope:** Activation, state migration, consumer rewrite, rollback,
network updater, and accepting a locally rebuilt unmanifested artifact.

**Acceptance Criteria:**

1. **Given** locked source/toolchain/dependencies **When** the release build
   runs twice in the controlled environment **Then** artifact identity,
   version metadata, allowed ABI/dependencies, and checksum manifest are
   reproducible under documented normalization **And** one standalone binary
   is produced.
2. **Given** checksum, ABI, dependency, version, schema-support, or provenance
   mismatch **When** admission runs **Then** the artifact is refused before
   state or consumer effects **And** one exact recovery instruction is recorded.
3. **Given** an admitted staged binary **When** version/self-check smoke runs
   with isolated descriptors and state **Then** build/schema/grammar identity
   matches ReleaseArtifactV1 and exits successfully **And** active installation
   and durable state remain unchanged.

### Story 7.2: Quiesce Stateful Work Behind a Process-Associated POSIX Lock

As an Operator,
I want upgrades admitted only after all srvls stateful work is quiescent,
So that release cannot race collection, baselines, actions, or another release.

**Implementation Boundary:** Implement process-associated POSIX record lock
protocol and lock identity, release admission/preflight, holder diagnostics,
block-new-work barrier, drain/cancel rules for collections and safe prelaunch
actions, detach/wait for launched operations, SQLite transaction drain,
timeout/range, owner-loss semantics, FD_CLOEXEC/descriptor hygiene across all
spawns including FD3/FD4, and read-only command policy during quiescence.

**Requirement Mapping:** FR: FR-39, FR-43; NFR: NFR-2, NFR-3, NFR-5, NFR-9,
NFR-12, NFR-13, NFR-16; UJ: UJ-4, UJ-6; UX: UX-CP-16, UX-IP-8,
UX-IP-10, UX-VT-4; AD: AD-6, AD-10, AD-11, AD-14, AD-15, AD-20, AD-22,
AD-23, AD-25.

**Dependencies:** Story 7.1 and Epic 6 operation handoffs.

**Validation Expectations:** Multi-process lock matrix covers acquire/
contention/reentrancy policy, fork/exec, owner death, FD_CLOEXEC, FD3/FD4
allowlists, active collection/baseline/action/storage/release at each phase,
timeout, launched-effect recovery, no new admission, and deterministic holder
diagnostics.

**Out of Scope:** Killing a lock holder, replacing the lock with a PID file or
SQLite row, cancelling possibly executed effects, and whole-process elevation.

**Acceptance Criteria:**

1. **Given** no competing owner **When** release admission acquires the
   canonical POSIX record lock **Then** lock identity/owner evidence and a
   durable release intent are recorded before quiescence **And** new
   collection, baseline, operation, and release admissions are blocked.
2. **Given** in-flight collection, baseline write, prelaunch operation,
   launched operation, or SQLite transaction **When** quiescence runs **Then**
   each follows its specified cancel/drain/detach/wait rule within bounds
   **And** a possibly executed action is handed to its coordinator rather than
   replayed or abandoned.
3. **Given** competing release, timeout, owner death, or any child spawn
   **When** lock/descriptor policy is tested **Then** one process owns release,
   failure is explicit, lock ownership follows POSIX semantics, and no
   undeclared descriptor leaks across exec **And** recovery can take over from
   durable evidence.

### Story 7.3: Capture Preimages, Migrate State, and Stage Activation

As an Operator,
I want binary and state changes prepared from verified preimages,
So that every activation cut has a recoverable prior pair.

**Implementation Boundary:** Implement canonical ReleaseTransactionV1 and
phase manifest, active binary/state/consumer preimage identities and checksums,
permission/owner metadata, space/capacity checks, fsync discipline, durable
backup/stage directories, SQLite consistent backup/integrity, forward migration
on staged copy, staged new-binary schema smoke, atomic rename/exchange strategy,
directory fsync, and effect receipts.

**Requirement Mapping:** FR: FR-42, FR-43; NFR: NFR-2, NFR-9, NFR-11,
NFR-12, NFR-15, NFR-16; UJ: UJ-6; UX: UX-CP-16, UX-IP-8, UX-ST-18,
UX-VT-3, UX-VT-4; AD: AD-11, AD-12, AD-16, AD-20, AD-23, AD-24.

**Dependencies:** Stories 7.1 and 7.2.

**Validation Expectations:** Filesystem/SQLite fault injection covers missing
first install, existing install, permissions/ownership, low space, backup/
integrity/migration failures, every write/fsync/rename cut, EXDEV refusal,
checksum/readback, future schema, manifest/receipt canonical bytes, and exact
prior/new pairs.

**Out of Scope:** Consumer changes, post-activation validation, KnownGood
publication, irreversible down-migration, and mutating active state before
staged validation.

**Acceptance Criteria:**

1. **Given** an existing valid installation **When** staging begins **Then**
   exact binary/state/consumer preimages, metadata, checksums, SQLite backup,
   and transaction manifest are durably recorded before a replaceable effect
   **And** protected recovery evidence is pinned.
2. **Given** the admitted artifact and state copy **When** migration/staged
   smoke runs **Then** only the staged database advances, integrity/schema/
   binary compatibility and permissions are verified, and the active pair is
   untouched **And** any failure is recoverable from preimages.
3. **Given** each activation write/rename/fsync crash cut **When** recovery
   reads manifest and effect receipts **Then** it can distinguish old/new/
   indeterminate bytes by checksum and complete or restore one coherent pair
   **And** partial state is never declared active.

### Story 7.4: Rewrite and Read Back Managed Consumer Contracts

As an Operator,
I want every managed consumer invoke the activated binary and state contract
exactly,
So that an upgrade cannot leave timers or scripts on a stale executable.

**Implementation Boundary:** Inventory named managed consumers from the final
architecture, parse/freeze their invocation contracts, stage bounded rewrites
to canonical absolute executable/config/state arguments and explicit formats,
preserve unrelated content/metadata, atomic replace/fsync, readback/semantic
parse, daemon-reload where required through typed argv, preimage receipts,
unmanaged-consumer diagnostics, and rollback recipes.

**Requirement Mapping:** FR: FR-16, FR-42, FR-43; NFR: NFR-2, NFR-4, NFR-5,
NFR-9, NFR-14, NFR-15; UJ: UJ-6; UX: UX-IA-9, UX-CP-16, UX-IP-8,
UX-VT-3; AD: AD-9, AD-11, AD-12, AD-15, AD-20, AD-23, AD-24.

**Dependencies:** Story 7.3.

**Validation Expectations:** Named consumer golden/live matrix covers each
supported timer/unit/script, quoting/argv semantics, absolute executable,
explicit format/state/config, unrelated-content preservation, owner/mode,
atomic write/readback, daemon reload, stale/unknown consumer, crash cuts, and
exact restoration.

**Out of Scope:** Rewriting arbitrary user automation, shell-evaluating
consumer text, silently adopting unmanaged consumers, and declaring consumer
health from file write alone.

**Acceptance Criteria:**

1. **Given** every named managed consumer preimage **When** a rewrite is staged
   **Then** only owned invocation fields change to the admitted executable and
   explicit contract while unrelated bytes/metadata are preserved **And** the
   exact old/new semantic forms are recorded.
2. **Given** staged/activated consumer files **When** readback and manager
   reload run **Then** parsed argv, executable identity, config/state paths,
   explicit output profile, ownership/mode, and manager acceptance match the
   manifest **And** mismatch blocks progression.
3. **Given** an unmanaged, malformed, missing, or changed consumer **When**
   admission/readback detects it **Then** release refuses or carries only an
   explicitly approved bounded deviation **And** it never overwrites unknown
   content silently.

### Story 7.5: Prove Timer-Originated Consumer Causality over FD4

As an Operator,
I want release validation prove that managed timers invoked this exact binary,
So that a green command smoke cannot hide a stale consumer path.

**Implementation Boundary:** Implement authenticated FD4 release-validation
proof channel, nonce/transaction/consumer/phase framing, descriptor ownership,
same-binary identity, timer/unit trigger, captured invocation and effective
paths, Snapshot/metrics output identity, bounded evidence, timeout/EOF/cleanup,
systemd timer causality checks, and no stdout proof.

**Requirement Mapping:** FR: FR-42, FR-43; NFR: NFR-2, NFR-3, NFR-4, NFR-5,
NFR-7, NFR-12, NFR-13, NFR-15; UJ: UJ-6; UX: UX-CP-16, UX-IP-8,
UX-VT-3, UX-VT-4; AD: AD-11, AD-12, AD-14, AD-15, AD-23, AD-24.

**Dependencies:** Story 7.4.

**Validation Expectations:** FD4/systemd matrix covers descriptor number/
ownership/CLOEXEC, nonce replay, wrong transaction/consumer/phase/binary,
malformed/oversize/truncated/extra frames, manual-vs-timer invocation, stale
unit, output identity, timeout/signal/EOF, cleanup, and full timer causality.

**Out of Scope:** Treating manual binary invocation as timer proof, using FD3
Collector frames as FD4 proof, accepting stdout markers, and monitoring timers
after transaction completion.

**Acceptance Criteria:**

1. **Given** an activated managed timer and FD4 validation nonce **When** the
   manager triggers its unit **Then** the same admitted binary proves
   transaction, consumer, phase, executable/build, argv/state/config, trigger,
   and output identity over FD4 **And** manual invocation cannot satisfy it.
2. **Given** replayed/mismatched/malformed/oversized/truncated proof, wrong
   descriptor, stale binary, timeout, EOF, or signal **When** validation reads
   FD4 **Then** that consumer fails with bounded evidence **And** release cannot
   publish KnownGood.
3. **Given** metrics and Snapshot consumers **When** timer validation completes
   **Then** both their output contracts and causal invocation are checked
   against the transaction manifest **And** all child descriptors/processes
   are cleaned and reaped.

### Story 7.6: Recover the Release Transaction after Owner Loss

As an Operator,
I want a new owner to resume or restore from durable release evidence,
So that a crash at any effect boundary cannot strand split truth.

**Implementation Boundary:** Implement RecoveryOwner lock takeover,
ReleaseTransactionV1 phase/effect state machine, preimage/staged/active checksum
inspection, ambiguous-effect resolution, idempotent forward/compensating
steps, action/storage handoff reconciliation, consumer/FD4 validation resume,
bounded retry/deadline, durable receipts before/after effects, operator status,
and terminal committed/restored/failed-needs-manual states.

**Requirement Mapping:** FR: FR-43; NFR: NFR-1, NFR-2, NFR-9, NFR-12,
NFR-13, NFR-15, NFR-16; UJ: UJ-6; UX: UX-IA-9, UX-CP-16, UX-IP-8,
UX-IP-10, UX-VT-4; AD: AD-6, AD-11, AD-16, AD-20, AD-22, AD-23, AD-24.

**Dependencies:** Stories 7.2 through 7.5.

**Validation Expectations:** Model/fault-injection matrix cuts owner power
before/after every filesystem, SQLite, lock, consumer, reload, validation,
KnownGood, and cleanup effect; covers stale/repeated owners, indeterminate
checksums, lost launched action, bounded retries, idempotency, and one terminal
state.

**Out of Scope:** Guessing when evidence is irreconcilable, deleting recovery
artifacts before terminal durability, replaying actions, and remote
coordination.

**Acceptance Criteria:**

1. **Given** owner loss at any named release effect boundary **When** a new
   process acquires the same POSIX lock **Then** it reconstructs transaction,
   exact preimages/current bytes, receipts, consumer state, and pending
   validations before choosing forward or restore **And** no effect is blindly
   repeated.
2. **Given** bytes/effects match a known manifest state **When** recovery runs
   repeatedly or crashes again **Then** idempotent steps converge to one
   coherent new or restored pair and one terminal record **And** only one owner
   advances phases.
3. **Given** checksums, preimages, or external manager state are ambiguous or
   irrecoverable within policy **When** recovery stops **Then** failed-needs-
   manual names exact evidence, protected files, and safe commands **And** it
   does not publish KnownGood or erase recovery data.

### Story 7.7: Publish KnownGood Only after Complete Admission

As an Operator,
I want KnownGood to represent a fully validated binary/state/consumer pair,
So that rollback never points at an artifact that merely installed.

**Implementation Boundary:** Implement KnownGoodV1 canonical manifest and
admission predicate requiring checksums, schema/integrity, compatibility corpus
and approved deviations, constrained Host smoke, metrics/Snapshot consumer
readback and FD4 causality, no unresolved release phase, recovery recipe,
retained prior pair, atomic KnownGood compare-and-set, pins, and publication
audit.

**Requirement Mapping:** FR: FR-42, FR-43; NFR: NFR-1, NFR-2, NFR-9,
NFR-14, NFR-15; UJ: UJ-6; UX: UX-IA-9, UX-CP-16, UX-IP-8, UX-VT-3;
AD: AD-9, AD-11, AD-12, AD-20, AD-23, AD-24.

**Dependencies:** Stories 7.1 through 7.6.

**Validation Expectations:** Admission matrix independently flips every
predicate, checks deviation expiry/owner, consumer proof, prior-pair pin,
concurrent publication, crash before/after CAS, manifest bytes/fingerprint,
retention, and assertion that activation alone never moves KnownGood.

**Out of Scope:** Deleting the prior pair, treating a staged artifact as
KnownGood, auto-approving deviations, and beta rollout policy.

**Acceptance Criteria:**

1. **Given** all artifact, state, compatibility, live Host, consumer readback,
   metrics/Snapshot FD4, recovery, and retention predicates pass **When**
   admission runs **Then** one canonical KnownGood manifest and pointer commit
   atomically with audit/pins **And** it names exact binary, state, consumers,
   toolchain, policy, and evidence fingerprints.
2. **Given** any predicate missing, failed, stale, incompatible, or covered by
   an unapproved/expired deviation **When** publication is attempted **Then**
   KnownGood remains unchanged with exact reasons **And** active installation
   is recoverable under the open transaction.
3. **Given** concurrent publication or crash around the pointer CAS **When**
   recovery resumes **Then** at most one admitted manifest becomes KnownGood
   and prior KnownGood remains intact until the new commit **And** retention
   cannot evict either required recovery pair.

### Story 7.8: Recover First Install and Execute Explicit Rollback

As an Operator,
I want first-install absence and installed rollback handled explicitly,
So that recovery never assumes a prior artifact that did not exist.

**Implementation Boundary:** Implement FirstInstallV1 preimage-absence grammar,
partial-first-install cleanup/restoration, installed rollback planning and
explicit confirmation, release lock/quiescence, exact KnownGood target,
binary/state/consumer restoration, schema compatibility/down-transition policy,
readback and FD4 validation of restored consumers, rollback transaction/
receipts, and retained failed-new evidence.

**Requirement Mapping:** FR: FR-43; NFR: NFR-2, NFR-5, NFR-9, NFR-12,
NFR-13, NFR-15, NFR-16; UJ: UJ-6; UX: UX-IA-9, UX-CP-10, UX-CP-16,
UX-IP-5, UX-IP-8, UX-VT-4; AD: AD-6, AD-11, AD-16, AD-20, AD-23, AD-24.

**Dependencies:** Stories 7.2 through 7.7.

**Validation Expectations:** Matrix covers absent/present preimages, every
first-install crash cut, explicit rollback cancel/confirm, KnownGood missing/
corrupt, forward-only schema incompatibility, restore cuts, consumers/FD4,
repeated rollback recovery, retained failed-new evidence, and one coherent
terminal pair.

**Out of Scope:** Pretending absence is a zero-byte backup, destructive schema
downgrade without a proven recipe, implicit rollback on ordinary command
failure, and deleting forensic evidence.

**Acceptance Criteria:**

1. **Given** no prior installation **When** first install crashes at any phase
   **Then** recovery uses explicit absence preimages to remove/complete only
   transaction-owned artifacts and restore unrelated state **And** never seeks
   a nonexistent prior binary/database/consumer.
2. **Given** an installed system and exact retained KnownGood pair **When** an
   Operator reviews and confirms rollback **Then** risk, target checksums,
   schema/consumer implications, and cancel-first choice are explicit before
   the same lock/quiescence protocol begins **And** no raw-mode authorization
   occurs.
3. **Given** rollback interruption at any restore/validation cut **When**
   recovery resumes **Then** exact KnownGood binary/state/consumers converge
   and pass readback/FD4 validation before terminal restored **And** the failed
   new pair/evidence stays retained for diagnosis.

### Story 7.9: Close the Aggregate Release and Recovery Gate

As an Operator preparing a supported release,
I want one machine-checkable release/recovery matrix and linear runbook,
So that no artifact ships on installation success alone.

**Implementation Boundary:** Wire artifact/toolchain/ABI/checksum, POSIX lock/
quiescence, FD3/FD4 descriptors, SQLite/storage/action handoffs, migration/
activation, managed consumers, timer causality, transaction crash recovery,
KnownGood, FirstInstall, explicit rollback, compatibility/live consumers,
UX install phases, terminal/signals, and ARCH-HOST-1 evidence into AD-11;
implement status/recover/install/rollback linear/machine surfaces and release
evidence bundle.

**Requirement Mapping:** FR: FR-16, FR-42, FR-43; NFR: NFR-1 through NFR-16;
UJ: UJ-6; UX: UX-IA-9, UX-CP-15, UX-CP-16, UX-IP-8, UX-IP-10, UX-IP-11,
UX-A11Y-3, UX-A11Y-5, UX-RP-6, UX-VT-1, UX-VT-3, UX-VT-4; AD: AD-7,
AD-8, AD-9, AD-11, AD-12, AD-14, AD-15, AD-16, AD-20, AD-22, AD-23,
AD-24, AD-25.

**Dependencies:** Stories 7.1 through 7.8 and every prior epic aggregate gate.

**Validation Expectations:** Run the full checked-in release/CI matrix with
fault injection at every named cut, all identity/descriptor/consumer lanes,
repeated owner loss, complete UJ-6 linear traversal, clean machine channels,
compatibility/live consumers, checksum/ABI, terminal restoration, retained
evidence, and independent CI lane ownership.

**Out of Scope:** Publishing or pushing a release, remote fleet rollout,
unapproved deviations, automatic rollback without recorded policy/authority,
and using this planning artifact as execution evidence.

**Acceptance Criteria:**

1. **Given** every named release, transition, descriptor, storage/action
   handoff, consumer, timer, FirstInstall, rollback, and owner-loss fixture
   **When** the aggregate gate runs **Then** each checked matrix row reports
   pass/fail and evidence fingerprint under its independent lane **And** missing
   or unwired rows fail AD-11.
2. **Given** TERM=dumb/NO_COLOR and any install/recover/rollback phase **When**
   the linear/machine runbook executes **Then** exact transaction, lock,
   artifact/state/consumer identities, phase, bounds, evidence, non-success,
   and one safe recovery instruction are available with clean channels **And**
   terminal restoration does not depend on the TUI.
3. **Given** a release candidate for supported use **When** final admission is
   evaluated **Then** artifact/checksum/ABI, compatibility/deviations, Host
   smoke, state migration/integrity, metrics/Snapshot consumer causality,
   KnownGood/recovery/rollback, and retained evidence all pass **And** the
   evidence bundle proves UJ-6 without treating self-review as independent
   evidence.
