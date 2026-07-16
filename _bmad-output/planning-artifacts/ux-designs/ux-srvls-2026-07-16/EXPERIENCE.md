---
name: srvls
status: draft
description: "Behavioral contract for the srvls terminal morning handoff, Runtime Promise reconciliation, and exact-target lifecycle control."
sources:
  - ../../prds/prd-srvls-2026-07-16/prd.md
  - ../../prds/prd-srvls-2026-07-16/addendum.md
updated: 2026-07-16
---

# srvls — Experience Spine

## Foundation

**UX-FND-1 — Contract boundary.** srvls is one local Linux terminal product:
an interactive TUI when both stdin and stdout are terminals and TERM is not
dumb, plus deterministic non-interactive CLI and Agent surfaces. DESIGN.md
owns visual semantics; this file owns behavior. All required surfaces are
spine-specified, so no visual mock is necessary. The spines win over source
extracts and legacy candidates when they do not conflict with the PRD.

**UX-FND-2 — Orthogonal truth.** Presentation may summarize, but it never
collapses the canonical axes:

| Axis | Canonical values | UX rule |
| --- | --- | --- |
| Promise Lifecycle | lease-active, heartbeat-late, lease-expired, persistent-active, closed | Closed retains exactly one reason: released, completed, or revoked. |
| Evidence Status | sufficient, incomplete, stale, out-of-scope | Unknown is not a fifth Evidence Status. |
| Promise Outcome | healthy, broken, unresolved, inactive | Active intent with incomplete, stale, or out-of-scope evidence is unresolved. |
| Observation labels | orphaned, duplicate, stale, hot, unmanaged, abandoned | Zero or more labels may coexist on an exact Observation. |
| Safe-to-stop Assessment | safe, unsafe, unknown | Each value includes reasons; none grants authority. |
| Collection Obligation | required, optional, not-applicable | Show the effective obligation and why it applies. |
| Collector outcome | complete, partial, unavailable, denied, timed-out, invalid-output | A non-complete outcome is visible and scoped. |
| Action Outcome | verified, executed-unverified, refused, timed-out, failed | Exactly one terminal value; no alias or sixth state. |

**UX-FND-3 — Exact identity.** Display names, rows, filters, attention rank,
Stack, Project, Agent, and finding groups are navigation context only. Any
operation binds to the canonical Promise or Observation identity, captured
Snapshot generation, resolved Provider-native operation, and a unique
operation ID.

**UX-FND-4 — Honest partial truth.** A Collector failure cannot become an empty
success, a broken Promise, a safe assessment, or a clean Host claim. The last
good Snapshot may remain visible only with a persistent stale label and disabled
actions. Refresh and actions never mix generations.

**UX-FND-5 — No automatic cleanup.** Expiry, closure, abandoned or orphaned
classification, and safe assessment support a human decision. They never
trigger or authorize mutation. All Stack, Project, Agent, and finding groups
are read-only in v1.

**UX-FND-6 — Compatibility is a product surface.** Redirected table output,
explicit JSON, Prometheus, Markdown, inspection, executable name, arguments,
ordering, escaping, exits, and explicit action behavior remain compatible
unless an approved ledger entry names the version impact, assertion, and
consumer disposition. Plane, Git, and Telemetry references remain opaque text;
srvls does not fetch them.

## Information Architecture

The interactive product is one Brief with overlays and responsive panes, not a
set of disconnected screens. Attention is the entry summary; Stack is the
primary exploration hierarchy.

| ID | Surface | Reached from | Purpose and exit |
| --- | --- | --- | --- |
| UX-IA-1 | Brief | Eligible bare invocation, explicit TUI, deprecated fzf alias | Names Evidence Window, baseline, freshness, completeness, changes, and attention. q exits from the base surface. |
| UX-IA-2 | Explorer | Brief body | Shows attention items first, then deterministic Stack groups and Ungrouped. Project, Agent, Provider, and finding facets refine the same hierarchy. |
| UX-IA-3 | Runtime detail | Enter on a Promise, Observation, or linked finding | Presents intent and actual truth together without merging their identities. Esc returns to the preserved Explorer selection. |
| UX-IA-4 | Provider and evidence detail | Enter on an evidence or Provider row in runtime detail | Shows bounded typed evidence, Collector diagnostics, provenance, redaction, and truncation. Esc returns one level. |
| UX-IA-5 | Search and filter | Slash from the base surface | Searches deterministic display fields and composes facets. Esc closes with current constraints preserved; Clear all removes them. |
| UX-IA-6 | Action menu | a on an exact Promise or Observation | Lists only resolved supported actions and reasons for disabled unsafe actions. Start is available from a Promise with a supported Launch Mechanism even without an Observation. |
| UX-IA-7 | Baseline acceptance | b from the Brief | Inspects and accepts an eligible Snapshot or performs an audited override. Esc cancels; refresh alone never accepts. |
| UX-IA-8 | Help | question mark from any non-text-input surface | Documents every global and contextual key, safety level, and assistive alternative. Esc returns to the prior focus. |
| UX-IA-9 | Install and recovery | Explicit install, upgrade, validate, or rollback command | Shows persistent phase results for stage through known-good recovery. It never enters the alternate-screen TUI. |
| UX-IA-10 | Agent and machine result | Explicit Promise, query, renewal, release, strict collection, output, or action command | Emits a deterministic result on stdout and human diagnostics on stderr without ANSI or progress. |

### Explorer hierarchy

The fixed reading order is:

1. Evidence Window and Snapshot freshness.
2. Completeness and effective Collection Obligations.
3. Change summary: new, resolved, changed, and persisting.
4. Attention summary and ranked exact items.
5. Stack groups, then explicit Ungrouped.
6. Selected runtime and evidence detail.
7. Key hints and pending-operation count.

Attention rank is deterministic and does not discard labels. Stack membership
is deterministic, read-only, and inspectable with confidence and evidence.
Ambiguous entries remain Ungrouped. The operator can change grouping context
through facets, but the underlying exact item identity and action scope never
change.

### Search and filter semantics

**UX-IA-11 — Deterministic refinement.**

- Slash opens the **filter-bar** with focus in text search.
- Search is case-insensitive Unicode text matching with deterministic ASCII
  folding where available. It examines Project, Agent, purpose, Provider,
  display name, exact identity, Launch Mechanism, and finding labels.
- Text query and different facet dimensions compose with AND.
- Multiple selected values within Project, Agent, Provider, or finding compose
  with OR.
- Tab and Shift-Tab move among query and facets; Space toggles a facet; Enter
  applies; c on the non-input controls clears all.
- Active query and facets remain visible above results in canonical order:
  Project, Agent, Provider, finding, query.
- filtered-empty names every active constraint and offers **Clear all**.
- Refresh reapplies the same constraints to the new generation.

## Voice and Tone

**UX-VT-1 — Calm, exact, accountable.** srvls reports what it knows, what it
does not know, and what the operator can safely do next. It avoids alarmist
language, jokes, blame, and false reassurance.

| Use | Avoid |
| --- | --- |
| “Docker timed out after the configured limit. Host completeness is incomplete.” | “Docker looks empty.” |
| “Promise is unresolved: systemd user scope is denied.” | “Runtime is probably gone.” |
| “Safe-to-stop: unknown. Missing ownership and recent-use evidence.” | “Should be safe.” |
| “Action refused: stale-identity. Refresh and inspect the replacement.” | “Something changed. Try again.” |
| “executed-unverified: Provider accepted stop; verification evidence timed out.” | “Stop succeeded.” |
| “No Runtime Promises or Observations match the active filters.” | “Nothing here!” |
| “Baseline unavailable: no eligible complete Snapshot.” | “No changes.” |

**UX-VT-2 — Canonical vocabulary.** UI copy uses Host, Runtime, Runtime
Promise, Lease, Heartbeat, Observation, Provider, Collector, Snapshot, Accepted
Baseline, Evidence Window, Stack, Project, Agent, Launch Mechanism, Durable
Ownership, and Safe-to-stop Assessment as defined by the PRD. It does not
invent synonyms for canonical states or outcomes.

**UX-VT-3 — Time and provenance.** Comparative times name timezone or offset.
Policy-derived findings show the effective value, units, source, and default or
override provenance. Redaction and truncation are stated without revealing
removed content.

**UX-VT-4 — Recovery copy.** Every refused, timed-out, failed, and
executed-unverified result includes one reason code, a bounded diagnostic, and
the next safe step. “Retry” is offered only when the same operation can be
idempotently correlated; otherwise the next step is refresh and re-plan.

## Component Patterns

Visual tokens live in DESIGN.md. Names in this table are exact and exhaustive.

| ID | Component | Visual reference | Behavioral contract |
| --- | --- | --- | --- |
| UX-CP-1 | brief-summary | {components.brief-summary} | Always names baseline, current Snapshot, Evidence Window, timezone, freshness, eight morning-answer counts, and active filters. A clean claim is withheld when completeness is not sufficient. |
| UX-CP-2 | completeness-banner | {components.completeness-banner} | Shows each Collector scope, effective obligation, outcome, duration, and diagnostic. Enter opens provider-detail for the first incomplete required scope. |
| UX-CP-3 | attention-row | {components.attention-row} | Represents one exact Promise, Observation, or linked finding. All applicable labels remain; Enter opens runtime-detail; row position never becomes identity. |
| UX-CP-4 | group-row | {components.group-row} | Space expands or collapses. Enter inspects grouping evidence. It never exposes an action or propagates selection to children. |
| UX-CP-5 | runtime-detail | {components.runtime-detail} | Separates Promise and Observation axes, links evidence, shows purpose, Project, Agent, ownership, lifetime, mechanism, policy provenance, and immutable action identity. |
| UX-CP-6 | evidence-table | {components.evidence-table} | Groups supports, contradicts, and missing evidence. Enter opens provider-detail. Missing evidence appears as a row, not whitespace. |
| UX-CP-7 | provider-detail | {components.provider-detail} | Displays bounded Provider-specific fields and separate stdout/stderr where supplied. Ctrl-F searches the captured block; n and N move matches; PgUp/PgDn scroll. |
| UX-CP-8 | filter-bar | {components.filter-bar} | Implements UX-IA-11. Input consumes printable keys; Esc first leaves input, a second Esc closes the overlay without clearing applied constraints. |
| UX-CP-9 | action-menu | {components.action-menu} | Resolves actions from the current exact target and capability. Unsafe supported actions are disabled with reasons; unsupported actions are absent; unknown remains selectable with stronger confirmation. |
| UX-CP-10 | confirmation-dialog | {components.confirmation-dialog} | Captures identity and generation, focuses Cancel, names resolved operation and risk, handles typed unknown acknowledgement, ignores repeat shortcuts, and refuses stale targets. |
| UX-CP-11 | operation-status | {components.operation-status} | Tracks one operation independently of navigation and refresh. Pending and verifying are phases; terminal state is exactly one canonical Action Outcome. |
| UX-CP-12 | baseline-dialog | {components.baseline-dialog} | Shows eligibility and Evidence Window impact. Override requires reason and acknowledgement. Acceptance changes only the baseline pointer and audit history. |
| UX-CP-13 | help-overlay | {components.help-overlay} | Documents global keys, conditional direct actions, confirmation behavior, ASCII/NO_COLOR modes, table/Markdown alternatives, and exit behavior. |
| UX-CP-14 | finding-marker | {components.finding-marker} | Renders every applicable finding as text and optional ASCII abbreviation. Labels coexist and never imply action safety. |
| UX-CP-15 | machine-result | {components.machine-result} | Human rendering and machine envelope share canonical field names and outcomes. stdout remains deterministic; stderr carries human diagnostics. |
| UX-CP-16 | install-phase | {components.install-phase} | Emits persistent phase start/result lines for staging, checksum, smoke, activation, consumer validation, and recovery. Failure stops forward activation and names the known-good target. |

## State Patterns

### Application and collection states

| ID | State | Treatment and allowed interaction |
| --- | --- | --- |
| UX-ST-1 | loading | With no prior Snapshot, render the Brief shell, loading text, elapsed time, and completed/total Collector scopes. Navigation to help and quit remains available. |
| UX-ST-1 | refreshing | Keep the last committed Snapshot visible and marked stale-while-refreshing. Show new-generation progress separately. Navigation remains active; actions on stale truth are disabled. |
| UX-ST-1 | stale | Name last successful refresh time, failed refresh reason, and affected scope. Do not claim current Host truth or allow mutation. |
| UX-ST-2 | partial-failure | Keep successful evidence usable. The completeness-banner names each incomplete scope and every conclusion withheld because of it. |
| UX-ST-2 | unavailable-Provider | Preserve other Providers. The unavailable Provider has outcome, effective obligation, bounded diagnostic, and retry guidance. |
| UX-ST-3 | empty | Only after sufficient required collection: “No Runtime Promises or Observations were found.” Completeness remains visible. |
| UX-ST-3 | filtered-empty | Name active query and facets, show unfiltered item count, and focus **Clear all**. |
| UX-ST-4 | pending-action | operation-status persists by operation ID while the operator navigates. Duplicate submit is suppressed; resource truth is not changed optimistically. |
| UX-ST-5 | verified | Terminal outcome. State the fresh evidence that proves the expected effect. |
| UX-ST-5 | executed-unverified | Terminal outcome. State that execution occurred, why verification is insufficient, and the next safe step. |
| UX-ST-5 | refused | Terminal outcome. No mutation occurred; show reason such as stale-identity, unsupported, unsafe, ambiguous, or unauthorized. |
| UX-ST-5 | timed-out | Terminal outcome. State which bounded phase timed out and whether execution may have occurred; never imply rollback unless verified. |
| UX-ST-5 | failed | Terminal outcome. State the failed operation or local invariant, bounded diagnostic, and next safe step. |
| UX-ST-6 | stale-identity before execution | Refuse without mutation, close confirmation, preserve the old target details for comparison, and focus Refresh. |
| UX-ST-6 | replacement after execution | Classify as executed-unverified, show old and replacement immutable evidence, and prohibit automatic retry. |
| UX-ST-7 | baseline-unavailable | Show first-run, incompatible, incomplete, missing, or unreadable reason. Changes remain “since no accepted baseline” rather than zero. |
| UX-ST-10 | redacted or truncated detail | Put a notice before the affected block, name the applied architecture-owned bound, escape control bytes visibly, and keep search/scroll within captured content. |

### Selection and focus recovery

**UX-ST-9 — Stable focus.**

- Initial focus is the first attention-row. If none exists, use the first item
  in the first Stack, then Ungrouped, then completeness-banner.
- A refresh preserves focus by exact identity, not row number.
- If the focused item disappears, focus the next sibling, then previous
  sibling, then parent group, then completeness-banner. Announce the move in
  the status line.
- If filters hide the focused item, focus the first result and retain the
  previous identity in navigation history until filters change again.
- Closing an overlay restores the element that opened it if it still exists;
  otherwise apply the same recovery order.
- A modal never silently retargets. Generation or identity drift yields
  UX-ST-6.

### Safety and action availability

**UX-ST-8 — Conservative controls.**

| Target state | Availability |
| --- | --- |
| Unsupported Provider operation | Absent from action-menu. |
| Supported but Safe-to-stop is unsafe | Disabled with all safety reasons. |
| Supported and Safe-to-stop is unknown | Available; requires the typed resolved verb before Confirm enables. |
| Supported, safe, and nondestructive Start | Plan is shown; Enter initiates without destructive confirmation unless privilege or policy introduces uncertainty. |
| Supported, safe Restart | Normal confirmation because the Runtime is interrupted. |
| Supported Stop, disable, or delete | Normal confirmation; PM2 delete and persistent-scheduler disable are labeled destructive. |
| Stale Snapshot, incomplete exact identity, or pending operation on target | Disabled or refused with refresh/wait guidance. |

Safe-to-stop is recalculated during planning and pre-execution revalidation.
Assessment, expiry, closure, and labels never authorize the operation.

## Interaction Primitives

### Startup and output selection

**UX-IP-1 — Deterministic routing.**

- Bare invocation enters the TUI only when stdin and stdout are terminals and
  TERM is not dumb.
- If either stream is redirected or TERM is dumb, bare invocation emits the
  legacy table and no terminal decoration.
- Explicit table, JSON, Prometheus, Markdown, and Agent flags always select
  non-interactive output.
- Explicit TUI requests fail diagnostically if initialization is unavailable;
  they do not silently emit a different format.
- The deprecated fzf flag enters the TUI without an external fzf dependency
  and emits a deprecation diagnostic on stderr.
- The legacy fzf-lines helper is removed only through the compatibility ledger.

### Global keyboard contract

**UX-IP-2 — Navigation and focus.**

| Key | Base behavior | Overlay or modal behavior |
| --- | --- | --- |
| Arrow keys or j/k | Move one visible row. | Move menu/list selection when not editing text. |
| Page Up/Page Down | Move one viewport. | Scroll the focused detail/help block. |
| Tab/Shift-Tab | Cycle status, Explorer, detail, and footer regions in reading order. | Cycle interactive controls; never escape a modal. |
| Enter | Inspect or activate the focused nondestructive control. | Activate the focused control; repeated Enter while pending is ignored. |
| Space | Expand/collapse group. | Toggle a facet or checkbox. |
| r | Start a new refresh generation. | Ignored in confirmation; available after an outcome closes. |
| Slash | Open filter-bar. | Printable input when the filter query is focused. |
| a | Open action-menu for an exact target. | Ignored while a confirmation or operation submit is active. |
| b | Open baseline-dialog. | Ignored while another modal is open. |
| question mark | Open help-overlay. | Help may open from non-text overlays, one level only. |
| Esc | Return one level; at base, clear a transient status before doing nothing. | Cancel or close the topmost overlay and restore prior focus. |
| q | Quit only from the base Brief after terminal restoration. | Treated as input or ignored; it never bypasses confirmation. |

**UX-IP-3 — Search and filter.** Behavior is defined by UX-IA-11. Search
results are stable for identical data and constraints. The filter-bar never
changes action identity or widens a selected target.

### Action invocation and confirmation

**UX-IP-4 — Discoverable actions.**

- a is the canonical entry. Start appears on a Promise when its supported
  Launch Mechanism resolves an exact start target, even if no Observation
  exists.
- s, R, and x are accelerators only when focus is an exact Observation, the
  corresponding Provider operation is supported, identity is sufficient, the
  Snapshot is current, and no operation is pending on that target.
- x never means a generic destructive action in the confirmation. The menu and
  dialog spell out the resolved operation, such as disable systemd unit or
  delete PM2 process.
- Direct shortcuts open the same plan and confirmation path as action-menu.
  There is no direct Start shortcut.

**UX-IP-5 — Confirmation mechanics.**

1. The confirmation-dialog captures exact identity, Snapshot generation,
   resolved Provider operation, current Safe-to-stop Assessment, reasons,
   privilege, expected effect, and verification expectation.
2. Cancel is focused by default. Enter on Cancel cancels; Esc always cancels.
   Tab or arrow navigation is required to focus Confirm.
3. Unknown safety adds a text field. Confirm remains disabled until the
   operator types the exact resolved verb shown by the dialog, such as stop,
   restart, disable, or delete.
4. Printable action shortcuts, y, and repeated Enter do not confirm unless
   they are valid input in the acknowledgement field or Confirm is explicitly
   focused.
5. The modal does not auto-confirm or time out into execution. If the
   architecture expires the plan, Confirm becomes disabled and Refresh is
   focused.
6. Submit creates one operation ID and immediately disables all submit
   controls. A duplicate event with the same caller-operation identity returns
   the same operation.
7. Revalidation happens after confirmation and before execution. Any identity,
   capability, generation, or safety drift refuses without mutation.

**UX-IP-6 — Baseline acceptance.**

- b opens baseline-dialog against the currently committed Snapshot.
- Eligible complete Snapshot: Cancel is focused; Confirm accepts exactly that
  Snapshot and records operator, time, and timezone.
- Incomplete or incompatible Snapshot: normal Confirm is disabled. An explicit
  Override path requires a nonempty reason, shows every incomplete obligation,
  and requires typing **override** before confirmation.
- Baseline acceptance never mutates Host resources and never occurs as a side
  effect of refresh, exit, or action.
- On success, the Brief recomputes its Evidence Window from the newly accepted
  boundary and reports the audit event.

### Asynchronous action lifecycle

**UX-IP-7 — Plan to outcome.**

1. **Plan:** resolve exact target, Provider operation, capability, privilege,
   expected effect, known limits, safety, and confirmation policy.
2. **Confirm if required:** apply UX-IP-5.
3. **Pending:** create operation-status within 100 ms, preserve displayed Host
   truth, and allow navigation.
4. **Revalidate:** refuse stale, reused, absent, ambiguous, unsupported, or
   unsafe identity before mutation.
5. **Execute:** invoke only the resolved typed Provider operation. No raw shell
   interpolation or group expansion.
6. **Verify:** collect bounded fresh truth correlated to the operation and
   expected effect. Refresh generations and operation verification remain
   independent.
7. **Outcome:** render exactly one of verified, executed-unverified, refused,
   timed-out, or failed with evidence, reason code, and next safe step.

The numerical ordering used to decide a terminal outcome is not a user-visible
progress meter. No phase changes the Runtime row optimistically.

### Install, Agent, and machine interactions

**UX-IP-8 — Install and recovery.** Explicit commands produce install-phase
lines on stderr for human progress and deterministic final results on stdout
when a machine format is requested. Stage and checksum precede compatibility
smoke; activation is atomic; scheduled consumers validate before the previous
known-good target is released. Failure preserves or restores the known-good
target and names the rollback command or completed automatic recovery.

**UX-IP-9 — Agent lifecycle.** Declare, query, renew, release, complete,
revoke, validate, and action operations never require prose parsing. Each
machine-result includes operation, status or Action Outcome, canonical
identity, Lease state where applicable, evidence/completeness where applicable,
reason code, and retry correlation. Field errors identify exact fields and
create no partial record. Human diagnostics remain on stderr.

## Accessibility Floor

**UX-A11Y-1 — Semantic independence.** Provider, identity, state, health,
freshness, labels, safety, completeness, focus, pending work, and outcomes are
present as text. NO_COLOR removes semantic color. ASCII mode supplies stable
bracketed markers. No animation, spinner, icon, or terminal style carries
unique meaning.

**UX-A11Y-2 — Keyboard and focus.** Every core journey is keyboard-only.
Focused rows have a persistent **>** prefix in addition to optional style.
Reading order and Tab order match. Help is one question-mark key away.
Confirmation defaults to Cancel, Esc cancels, and q cannot bypass a modal.

**UX-A11Y-3 — Terminal assistive alternatives.** srvls uses ordinary text
cells rather than graphics. Because alternate-screen TUIs vary across terminal
screen readers, redirected table and Markdown are first-class linear
alternatives; JSON is the machine alternative. TERM=dumb automatically selects
the undecorated table. These modes preserve the same canonical state words and
do not require color or Unicode.

**UX-A11Y-4 — Hostile and sensitive text.** C0, DEL, ESC, bidirectional
controls, and invalid byte sequences from names, commands, diagnostics, and
logs render as visible escaped forms, such as hex escapes or the replacement
character, according to one deterministic sanitizer. Tabs and newlines are
accepted only in fields whose layout contract explicitly permits them.
Secrets and sensitive arguments are excluded or visibly redacted.

**UX-A11Y-5 — Progress and motion.** The TUI uses no required animation.
Loading, refreshing, pending, and verifying show words, elapsed time, and
counts. Optional spinners stop under reduced/no-animation configuration and
never replace the text. Terminal restoration is required for normal exit,
error, panic, Ctrl-C, SIGINT, and SIGTERM.

Acceptance covers color on/off, Unicode/ASCII, monochrome, keyboard-only,
60-by-20 geometry, redirected stdout, TERM=dumb, hostile controls, and terminal
restoration.

## Responsive & Platform

srvls v1 targets the supported x86_64 GNU/Linux Host and terminal. Geometry is
measured after terminal initialization and on every resize.

| ID | Geometry | Contract |
| --- | --- | --- |
| UX-RP-1 | At least 120 columns by 30 rows | Full layout: brief-summary across the top; Explorer and runtime-detail side by side; evidence-table or provider-detail in the detail region; footer keys persistent. |
| UX-RP-2 | At least 80 by 24 but below full | Compact layout: brief-summary, completeness-banner, and one primary Explorer pane. runtime-detail and overlays occupy the primary pane; Esc returns. |
| UX-RP-3 | At least 60 by 20 but below compact | Narrow layout: one list or detail at a time; labels wrap; secondary timestamps and policy provenance move into detail; help and overlays scroll. Exact identity, states, labels, completeness, focus, and action safety remain. |
| UX-RP-4 | Below 60 columns or 20 rows at startup | Do not enter the full alternate-screen experience. Restore the terminal and print current geometry, minimum 60 by 20, and guidance to resize or use table/Markdown. |
| UX-RP-5 | Resize below minimum while active | Preserve model and focus, replace content with a text-only resize diagnostic, keep q and resize active, and restore the prior surface when geometry recovers. |
| UX-RP-6 | Redirected stream or TERM=dumb | Emit deterministic legacy table unless an explicit non-interactive format wins. No ANSI, icon, cursor control, progress, or human diagnostic enters stdout. |

Primary lists never scroll horizontally. In narrow mode the collapse order is
optional symbols, redundant badges, secondary timestamps, policy provenance,
then side-by-side detail. Exact target identity and canonical states are never
the truncation victim. Resizing preserves focus through UX-ST-9.

## Inspiration & Anti-patterns

**Preserved from the live tool:** one executable, direct terminal use,
deterministic redirected table, explicit JSON/Prometheus/Markdown modes,
Provider-specific inspection, and familiar j/k, Enter, Space, r, slash, s, R,
x, question-mark, Esc, and q vocabulary.

**Preserved from the approved migration direction:** deterministic Stack and
Ungrouped exploration, a centralized semantic theme/icon fallback boundary,
Elm-style asynchronous state ownership, exact identity plus generation,
failure-local inspection, read-only groups, and verifiable actions.

**Changed intentionally:** attention precedes Stack; a is the discoverable
action surface; b owns baseline acceptance; Start originates from Promise
intent; unknown safety requires typed acknowledgement; unverified becomes
executed-unverified; post-execution replacement is not called stale.

**Rejected anti-patterns:**

- A green dashboard that hides incomplete collection.
- One blended status badge for lifecycle, evidence, outcome, findings, and
  safety.
- External fzf as the target interaction shell.
- Row-position or friendly-name mutation.
- Group actions, bulk cleanup, or automatic remediation.
- Confirmation focused on Confirm, y-as-confirm, or repeated-key confirmation.
- Blocking refreshes, optimistic resource-state changes, and vanishing results.
- Unbounded or unsanitized logs and raw terminal controls.
- Icons, color, animation, or large-terminal layout as prerequisites.
- Fetching or duplicating Plane, Git, or Telemetry content.

## Operational Acceptance Budgets

These are UX response contracts, not Collector, retention, Lease, capture, or
verification limits. Architecture owns those operational limits and must make
their effective values and provenance available to the UI.

The canonical UX fixture contains 2,000 Observations, 500 Runtime Promises,
eight Collector scopes, 500 attention-bearing exact items, and bounded Provider
detail. Acceptance uses a deterministic terminal backend, 30 measured
iterations after warm-up, and p95 on the Architecture-published canonical Host.

| ID | Visible policy | Default | Valid implementation range | Acceptance |
| --- | --- | --- | --- | --- |
| UX-BUD-1 | Local key, focus, overlay, and filter feedback | 100 ms p95 maximum | 50–150 ms p95 | Focus marker, query text, or overlay is visible within the budget under the canonical fixture. |
| UX-BUD-2 | Refresh acknowledgement | 100 ms maximum | 50–150 ms | refreshing text, new generation ID, elapsed zero point, and Collector count appear without clearing the prior Snapshot. |
| UX-BUD-2 | Slow-refresh disclosure | 2,000 ms | 1,000–5,000 ms | At threshold, incomplete Collector names, elapsed time, and effective obligations are visible; navigation remains within UX-BUD-1. |
| UX-BUD-3 | Action-submit acknowledgement | 100 ms maximum | 50–150 ms | operation-status and operation ID appear, submit controls disable, and duplicate input is suppressed. |
| UX-BUD-3 | Pending progress refresh | 1,000 ms | 500–2,000 ms | Phase and elapsed time update at least this often without animation dependence. |
| UX-BUD-4 | Terminal outcome rendering | 100 ms maximum after architecture emits outcome | 50–150 ms | Exactly one outcome, evidence, reason, and next safe step render together. |
| UX-BUD-5 | Resize response | 100 ms p95 | 50–150 ms p95 | Correct layout or below-minimum diagnostic replaces the prior frame while identity focus is preserved. |

Defaults are built-in policy values with provenance **srvls UX default**.
Architecture may expose validated configuration only within the listed ranges;
outside-range values fail visibly rather than clamp silently. User-visible
Collector, stale, hot, Lease, grace, retention, detail-bound, and verification
values show their separate Architecture-owned default or override provenance.

## Key Flows

### UJ-1 — Jarad receives the morning handoff

1. Jarad runs srvls in an eligible terminal. The Brief shell appears within
   UX-BUD-2 and preserves any last committed Snapshot as stale while refreshing.
2. brief-summary names Accepted Baseline, current Snapshot, Evidence Window,
   timezone, and what changed. completeness-banner names every required,
   optional, and excluded scope.
3. Initial focus lands on the first attention-row. Jarad can immediately tell
   which items are broken, abandoned, orphaned, duplicate, stale, hot, or
   unmanaged without losing coexisting labels.
4. He opens Stack groups, uses slash to combine Project and finding facets, and
   leaves healthy work alone.
5. He presses Enter on an item to inspect Promise, Observation, ownership,
   purpose, Launch Mechanism, evidence, and Safe-to-stop reasons.
6. **Climax:** “Without opening five Provider tools, he can answer what
   changed, what should be alive, what is actually alive, and which findings
   need action.”

Failure: Docker times out. The Brief remains usable, marks completeness
incomplete, keeps Docker-dependent conclusions unresolved, and does not claim
the Host is clean. Enter on completeness opens the bounded diagnostic.

### UJ-2 — An Agent declares and renews an overnight runtime

1. Ava submits a deterministic declaration with Agent, Project, purpose,
   Launch Mechanism, expected lifetime, optional opaque references, and a
   caller-operation identity.
2. machine-result returns the Promise ID, finite Lease expiry, renewal
   expectation, and accepted provenance. A retry returns the same operation
   result.
3. Ava launches the Runtime and sends Heartbeats. Renewal results distinguish
   accepted, late, unauthorized, malformed, released, and unknown-Promise
   outcomes without prose parsing.
4. A refresh links the active Promise to an exact Observation while retaining
   the contributing evidence.
5. Ava releases, completes, or stops renewal. The response explicitly says
   that closing intent does not stop the Runtime.
6. **Climax:** “The Runtime appears as healthy once the Promise and
   Observation reconcile.”

Failure: Ava exits without release. Renewal stops; the Promise becomes
heartbeat-late, then inactive after Lease expiry. A fresh surviving
Observation becomes abandoned with reason lease-expired; srvls never
auto-stops it.

### UJ-3 — Jarad diagnoses a broken promise

1. Jarad focuses a broken Promise in the attention list and opens
   runtime-detail.
2. The detail shows purpose, Agent, Project, expected lifetime, last
   Heartbeat, Lease, Launch Mechanism, collection completeness, and
   candidate near-matches.
3. evidence-table separates supports, contradicts, and missing evidence so a
   Collector failure or identity mismatch cannot look like absence.
4. With sufficient absence evidence and a supported Launch Mechanism, Jarad
   presses a and selects Start from action-menu even though no Observation
   exists.
5. The plan names the exact Promise/start target, Provider operation,
   privilege, expected effect, and verification expectation before execution.
6. **Climax:** “He can distinguish a true missing Runtime from a collector
   failure or identity mismatch.”

Failure: The Launch Mechanism cannot resolve an exact supported target. Start
is absent or disabled with a reason; the next safe step returns Jarad to the
Project reference without inventing a command.

### UJ-4 — Jarad removes an abandoned runtime safely

1. Jarad opens an abandoned attention-row and verifies the historical Promise,
   closure or expiry reason, exact Observation identity, ownership gaps, and
   current Safe-to-stop Assessment.
2. He presses a and selects the resolved stop or disable/delete action. The
   plan names Provider-native operation, privilege, expected effect, and limits.
3. confirmation-dialog defaults to Cancel. If safety is unknown, Jarad types
   the exact verb before Confirm enables.
4. Submit creates one operation-status. srvls revalidates captured identity and
   generation before executing the typed operation.
5. Fresh correlated evidence determines exactly one Action Outcome; audit
   history retains plan, actor, result, evidence, and Promise history.
6. **Climax:** “srvls revalidates identity, performs the scoped action,
   refreshes truth, and reports verified success or an explicit non-success
   outcome.”

Failure: PID birth evidence or Provider identity changes after inspection.
Execution is refused with stale-identity, no mutation occurs, and Refresh is
the next focused step.

### UJ-5 — Jarad triages duplicate and hot runtime findings

1. Jarad selects an item carrying both duplicate and hot finding-marker values.
2. runtime-detail compares each exact Observation's immutable identity, start
   time, resource evidence, Agent provenance, intended count, and policy
   threshold.
3. He sees that hot does not imply safe and that duplicate is a comparison, not
   an automatically selected loser.
4. He opens action-menu on one exact Observation, or defers when safety remains
   unknown.
5. No Stack or duplicate group exposes a mutation control.
6. **Climax:** “He can identify the intended instance and understand why the
   other is a duplicate candidate.”

Failure: Evidence cannot establish the intended instance. Safety remains
unknown, the comparison names the missing evidence, and Jarad defers without a
false recommendation.

### UJ-6 — Jarad upgrades and recovers

1. Jarad runs the explicit upgrade flow outside the TUI. install-phase names
   the current known-good target and the staged candidate.
2. The candidate checksum and compatibility smoke complete before activation.
3. Activation swaps the target atomically and retains the previous version.
4. srvls-metrics, srvls-snapshot, version, and required compatibility consumers
   validate against the activated candidate.
5. On failure, the flow restores or preserves the known-good target and names
   every validation result.
6. **Climax:** “The upgrade either proves compatible or automatically
   preserves a clear rollback path.”

Failure: Consumer validation fails after activation. Forward release stops,
rollback restores the previous known-good target, scheduled-consumer
validation reruns, and the final machine result reports failed plus recovery
evidence rather than a partial success.

### Supporting flow — Jarad accepts an Evidence Window baseline

1. Jarad presses b from the Brief after inspecting the current complete
   Snapshot and collection obligations.
2. baseline-dialog shows current Accepted Baseline, candidate Snapshot,
   timezone, completeness, and the resulting closed Evidence Window.
3. Cancel has focus. Jarad explicitly moves to Confirm and accepts the exact
   candidate.
4. The next Brief recomputes new, resolved, changed, and persisting against the
   accepted boundary and records an audit event.
5. **Climax:** the meaning of “changed” is explicit and stable across refreshes.

Failure: The candidate is incomplete or incompatible. Normal acceptance is
disabled; an override requires reason plus typed acknowledgement and records
the incomplete obligations. Cancel leaves the baseline unchanged.

## Source Traceability

### User journeys and success measures

| Source | UX coverage |
| --- | --- |
| UJ-1: Jarad receives the morning handoff | UX-IA-1 through UX-IA-5; Key Flow UJ-1 |
| UJ-2: An Agent declares and renews an overnight runtime | UX-IP-9; Key Flow UJ-2 |
| UJ-3: Jarad diagnoses a broken promise | UX-IA-3, UX-IA-6, UX-IP-4; Key Flow UJ-3 |
| UJ-4: Jarad removes an abandoned runtime safely | UX-IP-5, UX-IP-7; Key Flow UJ-4 |
| UJ-5: Jarad triages duplicate and hot runtime findings | UX-FND-2, UX-FND-5; Key Flow UJ-5 |
| UJ-6: Jarad upgrades and recovers | UX-IP-8, UX-CP-16; Key Flow UJ-6 |
| SM-1: Complete morning answer set. | UX-CP-1, UX-CP-2; UJ-1 |
| SM-2: Reconciliation correctness. | UX-FND-2, UX-CP-14; canonical fixtures |
| SM-3: Safe action truthfulness. | UX-ST-8, UX-IP-5, UX-IP-7 |
| SM-4: Compatibility closure. | UX-FND-6, UX-IP-1, UX-RP-6 |
| SM-5: Agent lifecycle closure. | UX-IP-9; UJ-2 |
| SM-6: Explainable operator decisions. | UX-CP-5 through UX-CP-9; UJ-1, UJ-3, UJ-4, UJ-5 |
| SM-C1: Do not optimize anomaly count. | UX-FND-4; evidence and precision fixtures |
| SM-C2: Do not optimize speed by hiding incompleteness. | UX-CP-2, UX-ST-2, UX-BUD-2 |
| SM-C3: Do not optimize cleanup volume. | UX-FND-5, UX-ST-8 |

### Functional requirements

| Source requirement | UX coverage |
| --- | --- |
| FR-1: Declare a Runtime Promise | UX-IP-9, UX-CP-15, UJ-2 |
| FR-2: Preserve declaration provenance | UX-CP-5, UX-IP-9 |
| FR-3: Make Runtime Promises ephemeral by default | UX-FND-2, UX-IP-9, UJ-2 |
| FR-4: Renew ownership with Heartbeats | UX-IP-9, UJ-2 |
| FR-5: Release, complete, or revoke intent | UX-FND-2, UX-IP-9, UJ-2 |
| FR-6: Declare explicit persistent intent | UX-CP-5, UX-IP-9 |
| FR-7: Expose deterministic Agent contracts | UX-CP-15, UX-IP-9 |
| FR-8: Collect cron work | UX-CP-2, UX-CP-7 |
| FR-9: Collect systemd work | UX-CP-2, UX-CP-7 |
| FR-10: Collect Docker work | UX-CP-2, UX-CP-7 |
| FR-11: Collect PM2 work | UX-CP-2, UX-CP-7 |
| FR-12: Collect direct Host processes | UX-CP-5, UX-CP-7, UX-A11Y-4 |
| FR-13: Normalize Observations | UX-FND-2, UX-CP-3, UX-CP-5 |
| FR-14: Report collection completeness | UX-CP-2, UX-ST-2 |
| FR-15: Inspect bounded Provider detail | UX-CP-6, UX-CP-7, UX-ST-10 |
| FR-16: Preserve compatibility surfaces | UX-FND-6, UX-IP-1, UX-RP-6 |
| FR-17: Support strict collection policy | UX-CP-15, UX-IP-9 |
| FR-18: Correlate Runtime Promises and Observations | UX-CP-5, UX-CP-6 |
| FR-19: Identify healthy intent | UX-FND-2, UX-CP-3 |
| FR-20: Identify broken intent | UX-FND-2, UX-CP-5, UJ-3 |
| FR-21: Identify orphaned Observations | UX-CP-14, UX-CP-5 |
| FR-22: Identify duplicate Observations | UX-FND-5, UX-CP-5, UJ-5 |
| FR-23: Identify stale Runtimes | UX-CP-14, UX-CP-5 |
| FR-24: Identify hot Runtimes | UX-CP-14, UX-CP-5, UJ-5 |
| FR-25: Identify unmanaged and abandoned Runtimes | UX-CP-14, UX-CP-5, UJ-4 |
| FR-26: Explain findings and Safe-to-stop Assessment | UX-CP-5, UX-CP-6, UX-ST-8 |
| FR-27: Detect change through bounded Snapshots | UX-IA-7, UX-IP-6, baseline supporting flow |
| FR-28: Produce the Brief | UX-IA-1, UX-CP-1, UJ-1 |
| FR-29: Organize attention and Stack context | UX-IA-2, UX-CP-3, UX-CP-4 |
| FR-30: Select interactive or non-interactive presentation | UX-IP-1, UX-RP-6 |
| FR-31: Navigate and refine the TUI | UX-IA-11, UX-IP-2, UX-IP-3, UX-ST-9 |
| FR-32: Inspect intent and truth together | UX-IA-3, UX-CP-5, UX-CP-6 |
| FR-33: Communicate without color or Unicode dependence | UX-A11Y-1, UX-A11Y-3 |
| FR-34: Represent application and terminal states explicitly | UX-ST-1 through UX-ST-10, UX-RP-1 through UX-RP-5 |
| FR-35: Provide a discoverable Action Menu | UX-IA-6, UX-CP-9, UX-IP-4 |
| FR-36: Plan supported lifecycle actions | UX-CP-9, UX-IP-7 |
| FR-37: Revalidate identity before mutation | UX-FND-3, UX-ST-6, UX-IP-5 |
| FR-38: Confirm destructive and uncertain actions | UX-CP-10, UX-ST-8, UX-IP-5 |
| FR-39: Isolate asynchronous operations | UX-CP-11, UX-ST-4, UX-IP-7 |
| FR-40: Verify and report action outcomes | UX-ST-5, UX-IP-7, UX-CP-15 |
| FR-41: Keep groups read-only and privilege scoped | UX-FND-5, UX-CP-4, UX-ST-8 |
| FR-42: Build and install a verifiable release | UX-CP-16, UX-IP-8, UJ-6 |
| FR-43: Upgrade, validate automation, and roll back | UX-CP-16, UX-IP-8, UJ-6 |

### Non-functional requirements

| Source requirement | UX coverage |
| --- | --- |
| NFR-1: Deterministic domain outcomes | UX-FND-2, UX-IA-11, UX-ST-9 |
| NFR-2: Honest partial truth | UX-FND-4, UX-CP-2, UX-ST-2 |
| NFR-3: Bounded refresh behavior | UX-ST-1, UX-BUD-2 |
| NFR-4: Host command safety | UX-A11Y-4, UX-IP-7 |
| NFR-5: Least privilege | UX-CP-9, UX-CP-10, UX-ST-8 |
| NFR-6: Terminal restoration | UX-A11Y-5, UX-RP-4 |
| NFR-7: Clean machine interfaces | UX-CP-15, UX-IP-1, UX-IP-9 |
| NFR-8: Accessible terminal communication | UX-A11Y-1 through UX-A11Y-5, UX-RP-1 through UX-RP-6 |
| NFR-9: Atomic and durable local state | UX-ST-7, UX-IP-6, recovery copy |
| NFR-10: Defensible Lease time semantics | UX-FND-2, UX-VT-3, UX-CP-5 |
| NFR-11: Local data minimization | UX-ST-10, UX-A11Y-4 |
| NFR-12: Concurrency correctness | UX-FND-3, UX-ST-4, UX-ST-6, UX-IP-7 |
| NFR-13: Testability without Host mutation | UX-BUD-1 through UX-BUD-5; state, accessibility, and journey fixtures |
| NFR-14: Brownfield compatibility | UX-FND-6, UX-IP-1, UX-RP-6 |
| NFR-15: Supported release baseline | UX-IP-8, UX-CP-16, UJ-6 |
| NFR-16: Configurable policy without hidden defaults | UX-VT-3, UX-CP-5, Operational Acceptance Budgets |

Every canonical UJ, FR, NFR, SM, and safeguard has a named UX contract,
surface, behavior, or acceptance path. Architecture owns the remaining
operational limits explicitly assigned to it by the PRD.
