# Canonical PRD UX evidence extraction

This report extracts UX-relevant evidence from the finalized `srvls` PRD and
addendum dated July 16, 2026. It preserves source identifiers and names. It is
an input to UX design, not a new design contract. Statements in the explicit
matrices are requirements from the source. The separate inference section
records reasonable interpretations that still require downstream confirmation.

## Source boundary and reading record

The extraction uses the following canonical source files, read completely:

- `../../prds/prd-srvls-2026-07-16/prd.md`, 823 lines.
- `../../prds/prd-srvls-2026-07-16/addendum.md`, 63 lines.

The PRD states that it is the canonical target-state product contract and that
the addendum preserves implementation direction and readiness corrections. The
current Python inventory CLI is current behavior; Runtime Promises,
direct-process discovery, reconciliation, the TUI, verified actions, and
release automation are target behavior unless labeled as compatibility
contracts.

## Explicit journey evidence

The source defines six named journeys and six named climaxes. These names and
climax statements are preserved verbatim.

| Source ID and journey | Required surface or flow | Explicit states and interaction contract | Named climax (verbatim) | Downstream closure owner |
| --- | --- | --- | --- | --- |
| **UJ-1: Jarad receives the morning handoff** | Interactive-terminal entry into the Brief; change and attention summary; Project and Stack groups; abandoned and broken filters; evidence inspection; exact Runtime Promise or Observation drill-down. | Provider timeout leaves the Brief usable, visibly incomplete, and unable to claim that the Host is clean. Healthy work can be left alone. | “Without opening five Provider tools, he can answer what changed, what should be alive, what is actually alive, and which findings need action.” | UX: Brief hierarchy, filters, incomplete state, and evidence drill-down. Architecture: refresh/completeness data. |
| **UJ-2: An Agent declares and renews an overnight runtime** | Deterministic Agent flow to declare, receive Promise ID and Lease expiry, launch, Heartbeat, attach optional opaque Plane or Git reference, release, or leave an expiring Lease. | Healthy after Promise/Observation reconciliation; Agent exit without release stops renewal; expiry plus surviving Observation becomes abandoned. Non-interactive contracts must support the complete flow. | “The Runtime appears as healthy once the Promise and Observation reconcile.” | UX: Agent-facing response and error contracts. Architecture: Lease, Heartbeat, idempotency, and reconciliation semantics. |
| **UJ-3: Jarad diagnoses a broken promise** | Brief broken finding; inspection of purpose, Launch Mechanism, expected lifetime, last renewal, Collector completeness, and candidate near-matches; contextual Action Menu start or evidence-backed return to Project. | Must distinguish a missing Runtime, Collector failure, and identity mismatch. Start must resolve to an exact supported resource. | “He can distinguish a true missing Runtime from a collector failure or identity mismatch.” | UX: diagnosis presentation and start path. Architecture: matching, completeness, and supported start planning. |
| **UJ-4: Jarad removes an abandoned runtime safely** | Abandoned finding inspection; contextual Action Menu; resolved Provider-native operation review; exact-identity confirmation; execution; refresh; verified or explicit non-success report; audit history. | Identity drift between inspection and execution causes refusal. Observation disappearance proves success. Promise history is retained. | “`srvls` revalidates identity, performs the scoped action, refreshes truth, and reports verified success or an explicit non-success outcome.” | UX: confirmation, pending, refusal, verification, and audit feedback. Architecture: identity revalidation, scoped action, and audit persistence. |
| **UJ-5: Jarad triages duplicate and hot runtime findings** | Combined duplicate and hot presentation; comparison of stable identities, start times, resource evidence, Agent provenance, and intended instance count; exact-Observation action or defer. | Labels coexist. Unknown Safe-to-stop Assessment supports deferral. Group-wide mutation is unavailable. | “He can identify the intended instance and understand why the other is a duplicate candidate.” | UX: multi-label comparison and exact-target action affordance. Architecture: evidence, label, and intended-count computation. |
| **UJ-6: Jarad upgrades and recovers** | Stage, checksum verification, compatibility smoke, atomic activation, scheduled-consumer validation, and rollback to the previous known-good target. | Upgrade either proves compatible or preserves a clear rollback path; failed validation cannot leave a partial replacement. | “The upgrade either proves compatible or automatically preserves a clear rollback path.” | UX: terminal progress, validation result, and recovery guidance. Architecture/Release: staging, atomicity, checks, and rollback. |

## Explicit domain vocabulary and state model

The UX contract must use the source vocabulary without collapsing orthogonal
states. Presentation can summarize the axes, but filters, exports, fixtures,
and inspection retain them.

| Source term or model | UX consequence | Required surface or flow | States or interaction contract | Accessibility constraint | Downstream closure owner |
| --- | --- | --- | --- | --- | --- |
| **Action Menu** | A contextual surface lists only actions supported for the selected Observation and opens with `a`. | Selection context, supported actions, disabled explanations, help. | Start, stop, restart, and disable or delete where supported; exact target only. | Bindings must be documented with `?`; meaning cannot depend on color. | UX |
| **Action Outcome** | Exactly one canonical terminal result is shown for each lifecycle operation. | TUI and machine-readable result with operation, target, evidence, diagnostics, reason code, and next safe step. | `verified`, `executed-unverified`, `refused`, `timed-out`, or `failed`; no aliases. | Textual, persistent result; no animation-only or disappearing result. | UX and Architecture |
| **Accepted Baseline** and **Evidence Window** | Change claims must name their comparison boundary and timezone. | Brief summary, baseline acceptance, override, first-run, incompatible-baseline, and window inspection. | Baseline-to-current closed interval; refresh never advances baseline; explicit acceptance only. | Baseline status must survive monochrome, ASCII, and small terminals. | UX and Architecture |
| **Collection Obligation** and Collector outcomes | The UI must distinguish required, optional, and excluded evidence and explain incomplete conclusions. | Brief completeness summary and Provider/scope detail. | `required`, `optional`, `not-applicable`; `complete`, `partial`, `unavailable`, `denied`, `timed-out`, `invalid-output`. | Text labels and sanitized diagnostics; no color-only distinction. | UX and Architecture |
| **Promise Lifecycle** | Lifecycle is an independent axis, not a replacement for evidence or finding labels. | Promise rows, filters, details, exports, and fixtures. | `lease-active`, `heartbeat-late`, `lease-expired`, `persistent-active`, `closed`; closed retains exactly one of `released`, `completed`, or `revoked`. | Full text/ASCII semantics. | UX and Architecture |
| **Evidence Status** | Uncertainty remains visible and blocks false healthy/broken conclusions. | Findings, filters, inspection, exports. | `sufficient`, `incomplete`, `stale`, `out-of-scope`. | Must not depend on color or icons. | UX and Architecture |
| **Promise Outcome** | Promise conclusions remain independent from Observation labels. | Findings, filters, inspection, exports. | `healthy`, `broken`, `unresolved`, `inactive`. Incomplete, stale, or out-of-scope evidence makes active intent unresolved. | Text labels; no false-clean empty state. | UX and Architecture |
| **Observation labels** | Every applicable label remains visible; attention rank cannot discard labels. | Summary counts, rows, multi-label filters, comparison, detail. | `orphaned`, `duplicate`, `stale`, `hot`, `unmanaged`, `abandoned`; zero or more per exact Observation. | Multiple labels must remain legible without color or icons. | UX and Architecture |
| **Safe-to-stop Assessment** | Decision support is conservative and never a guarantee or mutation authorization. | Finding detail, action plan, confirmation, and pre-execution recalculation. | `safe`, `unsafe`, `unknown`, each with reasons. Missing or contradictory evidence produces `unknown`. | Words and reasons are mandatory; color may only supplement. | UX and Architecture |
| **Stack** | Grouping is deterministic and read-only, with inspectable confidence and evidence. | Stack-first exploration after attention summary and explicit Ungrouped section. | Ambiguous items remain Ungrouped; Stack membership never becomes action identity. | Collapse secondary detail before primary identity/status on small terminals. | UX |

### Explicit transition rules

The UX must preserve the source transition distinctions:

- A missed renewal cadence plus grace under a valid Lease yields
  `heartbeat-late`; a matching Observation is not yet abandoned.
- Lease expiry yields `inactive`; a fresh matching survivor receives
  `abandoned` with reason `lease-expired`.
- Closure as `released`, `completed`, or `revoked` yields `inactive`; a fresh
  matching survivor receives `abandoned` with that closure reason.
- Inactive intent without a survivor remains history, but absence is asserted
  only under sufficient Collection Obligations.
- Incomplete, stale, or out-of-scope evidence makes active intent `unresolved`,
  not healthy or broken. A positive fresh match is still required to label a
  survivor abandoned.
- Closure, expiry, classification, and `safe` assessment never authorize
  mutation.

## Explicit functional requirement matrix

Every canonical `FR-*` is included below. The consequence column extracts only
the UX-relevant product consequence and does not replace the full requirement.

### Runtime Promise lifecycle

| Source ID and name | UX consequence | Required surface or flow | States and interaction contract | Accessibility constraint | Downstream closure owner |
| --- | --- | --- | --- | --- | --- |
| **FR-1: Declare a Runtime Promise** | Required identity, purpose, lifetime, and ownership errors are field-level and create no partial record; success returns Promise ID and Lease state. | Human- and machine-readable declaration input/result. | Deterministic validation; success versus field errors. | Errors must identify fields in text and remain machine parseable. | UX: form/CLI feedback. Architecture: schema and atomicity. |
| **FR-2: Preserve declaration provenance** | History shows source, creation time, supplied identities, revisions, and lifecycle events without silent rewrite. | Promise detail and audit/history inspection. | Correction is an auditable revision/event under the same Promise ID. | Sensitive output is excluded or redacted. | UX and Architecture |
| **FR-3: Make Runtime Promises ephemeral by default** | Omitted persistence cannot look indefinite; responses state expiry and renewal expectations. | Declaration defaults and result microcopy. | Finite Lease by default; explicit persistence only. | Expiry must be textual and time-zone clear. | UX and Architecture |
| **FR-4: Renew ownership with Heartbeats** | Callers can distinguish late, unauthorized, malformed, released, and unknown-Promise outcomes. | Non-interactive renewal result and Promise/Heartbeat detail. | Caller-operation identity makes retries idempotent. | Diagnostics stay off machine stdout. | UX and Architecture |
| **FR-5: Release, complete, or revoke intent** | Closing intent explicitly does not stop the Runtime; one closure reason remains visible. | Close-intent command/result, history, next-refresh finding. | `released`, `completed`, or `revoked`; then inactive and possibly abandoned. | Destructive misunderstanding must be prevented with explicit text. | UX and Architecture |
| **FR-6: Declare explicit persistent intent** | Persistent intent needs Durable Ownership and inspectable Launch Mechanism; otherwise reject or show unmanaged. | Persistence choice, validation, and finding detail. | Accepted persistent, rejected, or retained unmanaged; never healthy by assertion alone. | Validation and unmanaged reason must be textual. | UX and Architecture |
| **FR-7: Expose deterministic Agent contracts** | Agents can retry and distinguish accepted, refused, stale, conflict, and unavailable. | Non-interactive declaration, query, renewal, release, and validation. | Deterministic schemas and exit behavior; clean stdout. | Human diagnostics must not corrupt stdout. | UX: contract clarity. Architecture: protocol and exit policy. |

### Actual Host state discovery

| Source ID and name | UX consequence | Required surface or flow | States and interaction contract | Accessibility constraint | Downstream closure owner |
| --- | --- | --- | --- | --- | --- |
| **FR-8: Collect cron work** | Schedule, command identity, source, user, and provenance are inspectable; denied/unavailable sources are explicit. | Cron rows, detail, completeness diagnostic. | Source-specific success or incomplete outcomes. | Hostile names and commands are sanitized. | UX and Architecture |
| **FR-9: Collect systemd work** | System/user scope, unit identity, enablement, runtime, health, schedule, and provenance stay distinguishable. | systemd rows and Provider detail. | Partial authorization or manager unavailability is explicit. | Text scope/state labels. | UX and Architecture |
| **FR-10: Collect Docker work** | Immutable identity is action identity; names are display data. Other Providers remain visible on daemon failure. | Container rows/detail and Docker diagnostic. | Runtime, health, restart policy, image, Compose Project, labels, and working-directory evidence. | Text identity/state; sanitized untrusted data. | UX and Architecture |
| **FR-11: Collect PM2 work** | Reused numeric IDs cannot silently retarget; invalid JSON yields bounded diagnostics. | PM2 rows/detail and local error state. | Stable identity, runtime, restarts, namespace, script, directory, start time. | Bounded, sanitized diagnostics. | UX and Architecture |
| **FR-12: Collect direct Host processes** | Direct processes are identifiable without double-counting Provider children. | Process rows/detail and provenance attribution. | PID plus birth evidence, fingerprint, parent, user, and directory when permitted; redaction explicit. | Sensitive command data is sanitized/redacted. | UX and Architecture |
| **FR-13: Normalize Observations** | Common projections stay consistent while typed Provider detail remains available. | Shared inventory/list model with Provider-specific detail route. | Encounter provenance retained for deterministic compatibility ordering. | Common text semantics across Providers. | UX and Architecture |
| **FR-14: Report collection completeness** | Every refresh exposes completeness, duration, diagnostics, obligations, inclusions, exclusions, and permission boundaries. | Brief summary plus per-Collector/scope drill-down. | Six Collector outcomes; active Promise may promote optional to required, never not-applicable to observed. | No false-clean or color-only completeness state. | UX and Architecture |
| **FR-15: Inspect bounded Provider detail** | Detail is Provider-appropriate, bounded, sanitized, and failure-local. | Observation inspection with status, schedule, provenance, identity, logs/output. | Byte/line bounds; selected-item failure does not collapse the Brief. | Unsafe controls sanitized; truncation disclosed textually. | UX and Architecture |
| **FR-16: Preserve compatibility surfaces** | Existing flat JSON, Prometheus, Markdown, table, inspection, executable name, ordering, escaping, arguments, exits, and explicit actions remain stable unless ledgered. | Legacy outputs, CLI behavior, fixtures, consumer validation, compatibility ledger. | New fields additive or versioned; deviations explicit and tested. | Existing machine and terminal consumers remain usable. | Architecture/Implementation; UX owns visible compatibility impacts. |
| **FR-17: Support strict collection policy** | Default gives usable partial truth; strict mode deterministically fails while preserving structured errors. | CLI option, result, diagnostics, exit behavior. | Default versus strict completeness outcome. | Clean machine-readable error structure. | UX and Architecture |

### Reconciliation and explainability

| Source ID and name | UX consequence | Required surface or flow | States and interaction contract | Accessibility constraint | Downstream closure owner |
| --- | --- | --- | --- | --- | --- |
| **FR-18: Correlate Runtime Promises and Observations** | Matches show contributing evidence, conflict, and confidence; weak names cannot imply action identity or health. | Linked Promise/Observation inspection and match explanation. | Supported evidence only; bounded secondary evidence. | Evidence and conflicts readable as text. | UX and Architecture |
| **FR-19: Identify healthy intent** | Healthy requires intended count, compatible running matches, and sufficient collection; compatible hot/stale evidence may coexist. | Finding row, labels, filters, detail. | Healthy withheld on incomplete collection or identity conflict. | Multi-axis meaning survives monochrome/ASCII. | UX and Architecture |
| **FR-20: Identify broken intent** | Broken retains last Heartbeat, Lease, Launch Mechanism, and near-matches; incomplete evidence is unknown, not broken. | Broken finding diagnosis flow. | Sufficient absence evidence required. | Unknown versus broken stated textually. | UX and Architecture |
| **FR-21: Identify orphaned Observations** | Operator sees why no Promise matched and whether collection was complete; preexisting managed resources are not mislabeled Agent-created. | Orphaned finding detail and match explanation. | Running Observation with no matching Promise. | Text reasons and provenance. | UX and Architecture |
| **FR-22: Identify duplicate Observations** | Excess exact Observations are comparable; the product does not silently choose a destructive target. | Duplicate comparison and exact-item selection. | Stable identities, start times, and evidence visible; no group mutation. | Comparison must remain usable without color. | UX and Architecture |
| **FR-23: Identify stale Runtimes** | Stale shows configured policy window and evidence source; missing Telemetry is not proof. | Stale finding and policy/evidence detail. | Explainable non-use or obsolescence evidence. | Textual policy and timestamps. | UX and Architecture |
| **FR-24: Identify hot Runtimes** | Hot shows metric, sample time, threshold, and source and never implies safe to stop. | Hot finding, metric evidence, combined labels. | Configured threshold or trend crossing. | Text values, units, and labels. | UX and Architecture |
| **FR-25: Identify unmanaged and abandoned Runtimes** | Findings retain ownership/Launch Mechanism gaps, expiry or closure reason, and historical Promise match. | Unmanaged/abandoned rows, filters, and detail. | Persistent-without-ownership remains unmanaged; expiry never auto-stops. | Reasons cannot rely on color/icons. | UX and Architecture |
| **FR-26: Explain findings and Safe-to-stop Assessment** | Every attention finding explains rules, identity, contradictions, missing evidence, confidence, ownership, purpose, lifetime, mechanism, and safety reasons. | Finding detail, action planning, confirmation, refresh/recalculation. | `safe`, `unsafe`, `unknown` under the full deterministic decision table. | Full text reasons are required. | UX and Architecture |
| **FR-27: Detect change through bounded Snapshots** | Change views name baseline, current snapshot, timezone, and first-run/incompatible/incomplete conditions; acceptance is explicit. | Change summary, accept-baseline command/TUI action, override/audit flow. | New, resolved, changed, persisting; fixed start across refresh; incomplete ineligible by default. | Baseline status and override risk need persistent text. | UX and Architecture |

### Morning Brief, CLI, and TUI

| Source ID and name | UX consequence | Required surface or flow | States and interaction contract | Accessibility constraint | Downstream closure owner |
| --- | --- | --- | --- | --- | --- |
| **FR-28: Produce the Brief** | One Brief answers all eight named morning questions, exposes completeness and multi-label counts, names the Evidence Window, and drills into all evidence. | Attention summary, change summary, completeness, baseline/current/timezone, drill-down. | Baseline unavailable and incomplete window are explicit. | Summary meaning cannot depend on color/icons. | UX |
| **FR-29: Organize attention and Stack context** | Attention precedes deterministic Stack groups; filters cover Project, Agent, Provider, and finding; Ungrouped is explicit. | Default TUI hierarchy, filters, Stack inspection. | Membership, confidence, and evidence inspectable; ambiguous stays Ungrouped. | Keyboard and small-terminal usability. | UX |
| **FR-30: Select interactive or non-interactive presentation** | TUI default requires both stdin and stdout terminals; redirection preserves table; explicit flags win. | Startup routing, output flags, deprecation behavior. | `--fzf` deprecated alias; `--fzf-lines` removed through compatibility ledger. | Non-interactive output has no terminal decoration. | UX and Architecture |
| **FR-31: Navigate and refine the TUI** | All core exploration is keyboard-operable and selection/focus remains predictable under filter and refresh. | Navigate, expand/collapse, filter, search, refresh, inspect, help, back, quit. | Fresh, refreshing, and stale are distinct; refresh does not block navigation. | Keyboard-only; focus not color-only. | UX |
| **FR-32: Inspect intent and truth together** | Promise, Heartbeat, Lease, Observation, Project, Agent, mechanism, evidence, and Provider detail are linked; unmatched items remain independent. | TUI/CLI inspection. | Plane/Git/Telemetry references display as opaque, unfetched references. | Clear labels and bounded content. | UX |
| **FR-33: Communicate without color or Unicode dependence** | Text always carries Provider, identity, runtime, health, freshness, pending work, and findings; color/icons are optional. | Every row and summary. | `NO_COLOR`, monochrome, deterministic ASCII fallback. | Explicit accessibility contract; sanitize unsafe controls. | UX and Architecture |
| **FR-34: Represent application and terminal states explicitly** | Every named application state gets visible treatment and responsive behavior. | Global/list/detail/action state presentation. | `loading`, `refreshing`, `stale`, `partial-failure`, `unavailable-Provider`, `empty`, `filtered-empty`, `pending-action`, `verified`, `executed-unverified`, `refused`, `timed-out`, `failed`, `baseline-unavailable`. | Never animation-, color-, or disappearance-only; small layouts preserve list/status first. | UX |
| **FR-35: Provide a discoverable Action Menu** | `a` opens supported lifecycle actions; direct `s`, `R`, `x` remain only where unambiguous; `?` documents bindings. | Contextual Action Menu, help, start-from-Promise path. | Unsupported/unsafe actions absent or disabled with explanation. | Keyboard discoverability and textual disabled reasons. | UX |

### Safe Runtime lifecycle control

| Source ID and name | UX consequence | Required surface or flow | States and interaction contract | Accessibility constraint | Downstream closure owner |
| --- | --- | --- | --- | --- | --- |
| **FR-36: Plan supported lifecycle actions** | A plan states exact target, Provider operation, privilege, expected effect, and limits before execution. | Start from Promise; per-Observation stop/restart/disable/delete where supported. | Cron read-only; direct process identity-safe signal only unless Launch Mechanism supplies start/restart. | Plan must be readable as text. | UX and Architecture |
| **FR-37: Revalidate identity before mutation** | Stale, reused, missing, or ambiguous identity refuses without mutation; row, name, and Stack are never identities. | Pre-execution revalidation and refusal result. | Exact Observation identity, or Promise/absence/start target when no Observation. | Refusal and reason remain visible. | UX and Architecture |
| **FR-38: Confirm destructive and uncertain actions** | Confirmation names exact Runtime/operation and current safety/uncertainty; unknown can be explicitly chosen but never shown safe. | Stop and disable/delete confirmation. | PM2 deletion and persistent-scheduler disablement visibly destructive. | Explicit text; no color-only risk cue. | UX |
| **FR-39: Isolate asynchronous operations** | Pending work remains tied to one operation and source generation; navigation/cancel cannot duplicate or misattribute it. | Pending-action presentation during concurrent refresh/navigation. | Unique operation identity, duplicate suppression, race isolation. | Persistent text status independent of animation. | UX and Architecture |
| **FR-40: Verify and report action outcomes** | Command exit is not success; post-action truth selects exactly one outcome and supplies next safe step. | Operation result in TUI and machine output. | Precedence: `verified`, `refused`, `timed-out`, `failed`, `executed-unverified`; diagnostics/reasons are metadata. | Outcome and evidence in text; clean machine output. | UX and Architecture |
| **FR-41: Keep groups read-only and privilege scoped** | Group interaction cannot widen targets; privilege belongs only to the selected Provider operation. | Read-only group affordances and exact-item action flow. | No whole-process elevation or auth prompt in raw mode. | Disabled/absent group actions need understandable treatment. | UX and Architecture |

### Installation, automation, and recovery

| Source ID and name | UX consequence | Required surface or flow | States and interaction contract | Accessibility constraint | Downstream closure owner |
| --- | --- | --- | --- | --- | --- |
| **FR-42: Build and install a verifiable release** | Activation follows staging, checksum, smoke, and required checks; version/compatibility output is deterministic. | Install terminal flow and machine-readable version/compatibility. | Staged, validated, activated, or rejected before activation. | Text status and clean machine output. | UX and Release/Architecture |
| **FR-43: Upgrade, validate automation, and roll back** | Previous target stays identifiable until binary and consumers validate; recovery is documented and partial replacement prohibited. | Upgrade, `srvls-metrics`/`srvls-snapshot` validation, rollback. | Known-good, staged, active-validating, validated, failed, rolled back. | Explicit progress/result without color or animation dependence. | UX and Release/Architecture |

## Explicit non-functional requirement matrix

| Source ID and name | UX consequence | Required surface or flow | States and interaction contract | Accessibility constraint | Downstream closure owner |
| --- | --- | --- | --- | --- | --- |
| **NFR-1: Deterministic domain outcomes** | Identical input, policy, and baseline yield identical ordering, findings, rank, safety, and serialization. | Lists, filters, exports, refresh comparisons, fixtures. | No unexplained reordering or conclusion drift. | Predictable focus and reading order. | Architecture; UX validates presentation ordering. |
| **NFR-2: Honest partial truth** | Failures stay explicit and scoped; missing evidence never becomes success, absence, or safety. | All empty, summary, detail, and action states. | Partial/unavailable/unknown remain distinct. | Textual distinctions. | UX and Architecture |
| **NFR-3: Bounded refresh behavior** | One Provider cannot hang the Brief; timeout remains visible while other evidence stays usable. | Refresh progress and Collector diagnostics. | Bounded concurrency, deadlines, capture, termination, and reaping. | Navigation remains available; no animation-only progress. | Architecture; UX owns feedback expectations. |
| **NFR-4: Host command safety** | Untrusted data cannot become shell behavior. | Inspection, action plan, diagnostic rendering. | Typed argv-only execution and safe end-of-options. | Sanitized display. | Architecture/Security |
| **NFR-5: Least privilege** | UI communicates operation-specific privilege and never prompts interactively in raw mode. | Action plan/confirmation and refusal guidance. | No whole-process elevation. | Text privilege requirement and safe terminal behavior. | UX and Architecture/Security |
| **NFR-6: Terminal restoration** | Every exit and signal path restores the user's terminal. | Return, error, panic, Ctrl-C, SIGINT, SIGTERM. | Raw mode, alternate screen, cursor, and input restored. | Foundational terminal accessibility/usability. | Architecture/Implementation |
| **NFR-7: Clean machine interfaces** | stdout is deterministic and free of ANSI, icons, progress, logs, and human diagnostics. | JSON, table, Markdown, Prometheus, and Agent contracts. | Stable order, exits, encoding, escaping. | Compatible with assistive and automated consumers. | Architecture; UX owns contract wording. |
| **NFR-8: Accessible terminal communication** | Status and focus work without color, Unicode, animation, or a large terminal. | Entire TUI and terminal output. | Sanitized untrusted controls; responsive layout. | Direct accessibility mandate. | UX and Architecture |
| **NFR-9: Atomic and durable local state** | Partial writes cannot appear as truth; recovery states must be explicit if encountered. | Promise, event, Snapshot, and compatibility state operations. | Atomic, crash-safe, versioned, recoverable. | Recovery diagnostics readable and deterministic. | Architecture |
| **NFR-10: Defensible Lease time semantics** | Clock rollback, restart, suspend, and discontinuity cannot silently extend ownership; displayed wall time remains understandable. | Lease/Heartbeat detail and revalidation/expiry states. | Explicit revalidation or expiry behavior. | Clear timestamps and timezone context. | Architecture; UX presents semantics. |
| **NFR-11: Local data minimization** | UI and history expose only required local, bounded, permission-restricted data; secrets/logs excluded or redacted. | Promise metadata, Provider detail, history, retention/deletion feedback. | Retention-bounded local state. | Redaction must be apparent without revealing data. | Architecture/Privacy; UX presents redaction. |
| **NFR-12: Concurrency correctness** | Late refreshes/actions cannot replace or mislabel newer truth. | Refresh and pending/action result states. | Generation and operation identities govern races. | Stable, non-flickering state communication. | Architecture; UX validates behavior. |
| **NFR-13: Testability without Host mutation** | Every TUI state, action, domain rule, and presentation needs deterministic test evidence without live mutation. | Fixtures, fakes, goldens, terminal backends. | Live-Host tests opt-in. | Accessibility fallbacks require test coverage. | Architecture/QA and UX |
| **NFR-14: Brownfield compatibility** | Visible and machine behavior remains covered by inventory, fixtures/goldens, smoke, consumer checks, and deviation ledger. | Legacy outputs/actions and migration reporting. | Intentional deviations include version impact, assertion, and consumer disposition. | Existing accessible/machine behavior cannot silently regress. | Architecture/Implementation; UX reviews deviations. |
| **NFR-15: Supported release baseline** | Supported platform and verification/recovery expectations must be stated accurately. | Install/upgrade/version help. | `x86_64-unknown-linux-gnu`, verified Host baseline, lock, reproducible checks, checksum, reversible install. | Text-only terminal path. | Release/Architecture; UX documents. |
| **NFR-16: Configurable policy without hidden defaults** | Every UX-visible policy value has a documented default, validation, and provenance in findings. | Configuration errors, finding detail, help/reference output. | Lease, grace, stale, hot, retention, deadlines, and bounds; invalid config fails visibly. | Values, units, source, and errors in text. | UX and Architecture |

## Explicit acceptance and budget implications

The source supplies outcome-level acceptance targets rather than numeric
latency, capacity, or retention budgets.

| Source ID and name | UX acceptance implication | Required evidence | Downstream closure owner |
| --- | --- | --- | --- |
| **SM-1: Complete morning answer set.** | One Brief answers all eight FR-28 questions and exposes incompleteness. | Canonical scenarios covering FR-14 and FR-18 through FR-29. | UX and QA |
| **SM-2: Reconciliation correctness.** | All eight finding terms and their evidence render without false certainty. | Canonical fixtures for healthy, broken, orphaned, duplicate, stale, hot, unmanaged, and abandoned. | Architecture, UX, and QA |
| **SM-3: Safe action truthfulness.** | Every mutation ends in exactly one FR-40 outcome and never claims verified without fresh evidence. | Mutation acceptance cases for FR-36 through FR-41. | Architecture, UX, and QA |
| **SM-4: Compatibility closure.** | User-visible and machine-visible legacy behavior either passes or has an approved disposition. | Fixture/golden corpus, smoke, consumer checks, compatibility ledger. | Architecture/Implementation and Product Owner |
| **SM-5: Agent lifecycle closure.** | Agents complete the entire lifecycle without parsing human prose. | Declare, retry, renew, query, release, and expiry scenarios. | Architecture, UX, and QA |
| **SM-6: Explainable operator decisions.** | Operators reach evidence and exact targets from the Brief without native discovery commands. | Core journey fixtures for FR-26, FR-28 through FR-35, and FR-37. | UX and QA |
| **SM-C1: Do not optimize anomaly count.** | Unsupported or false-positive labels are defects. | Finding precision review. | Product Owner, Architecture, and QA |
| **SM-C2: Do not optimize speed by hiding incompleteness.** | Timeout/denial cannot render as absence to improve apparent speed. | Partial/timeout acceptance fixtures. | UX, Architecture, and QA |
| **SM-C3: Do not optimize cleanup volume.** | Broad or automatic stopping is prohibited and fewer Runtimes is not success. | Exact-target and no-auto-remediation tests. | Product Owner, UX, and QA |

### Operational acceptance budget closure

The PRD explicitly leaves numeric budgets downstream. The named closure item is
**Operational acceptance budgets**. Its ownership is split as follows:

- **UX owns user-visible refresh and feedback expectations.** UX must publish
  defaults, valid ranges, and acceptance checks for perceived refresh and
  action feedback using canonical-Host measurements and fixture sizes.
- **Architecture owns Collector deadlines, output caps, retention, Heartbeat
  grace, and action-verification limits.** Architecture must publish defaults,
  valid ranges, and acceptance checks consistent with privacy, safety, and the
  supported Host.
- The closure gate is the canonical UX and architecture contracts and their
  stories before implementation readiness can report `READY`.

The second named closure item, **Operator-impact measure**, belongs to the
**Product Owner**. Before beta evaluation, the owner must approve the baseline,
target, measurement window, and collection method comparing the current
Provider-by-Provider reconstruction journey with the canonical Brief journey.
Host inventory counts cannot stand in for user impact.

## Explicit addendum constraints with UX implications

| Source constraint | UX consequence | Required closure owner |
| --- | --- | --- |
| Deliver one Rust binary while preserving the one-tool operator experience. | UX cannot split the required operator journey across separate products or executables. | UX and Architecture |
| Use an Elm-style ratatui shell with explicit model, message, update, view, and effect boundaries. | UX state and asynchronous interaction specifications must be explicit enough to map to these boundaries. | Architecture, informed by UX state contract |
| Preserve deterministic non-interactive table, JSON, Prometheus, Markdown, inspection, executable-name, and explicit-action behavior. | UX must treat terminal and non-interactive behavior as first-class surfaces, not only the TUI. | UX and Architecture |
| Define an explicit TUI start interaction or consistently scope start to a non-TUI surface. | The PRD resolves this correction in FR-35: start has an explicit TUI path from a Runtime Promise when no Observation exists. | UX |
| Separate mutation initiation and confirmation from asynchronous execution, race handling, verification, and outcome rendering. | The UX flow needs distinct plan/initiate, confirm, pending, verification, and terminal-outcome stages. | UX and Architecture |
| Legacy `FR1` through `FR18` are retired. | UX artifacts must cite canonical `FR-*` IDs, using the addendum mapping only for traceability. | UX and Product/Planning |
| Legacy `UX-DR1` through `UX-DR8` remain candidate inputs until a dedicated UX contract is approved. | They are not requirements in this extraction and cannot supersede the PRD. | UX |

## Reasonable but unconfirmed inferences

The following interpretations are useful for UX planning but are not explicitly
fixed by the canonical source. They require confirmation in the UX contract.

| Inference ID | Source basis | Reasonable inference | Confirmation owner |
| --- | --- | --- | --- |
| **INF-UX-1** | UJ-1, FR-28, FR-29 | The initial TUI focus likely begins in the attention summary or first attention-bearing Stack, but the source does not define initial focus. | UX |
| **INF-UX-2** | FR-29, FR-31 | Filters likely compose and expose active-filter chips or equivalent persistent text, but composition rules and representation are unspecified. | UX |
| **INF-UX-3** | FR-31, FR-34 | Refresh likely preserves selection by stable identity and announces row disappearance or relocation, but exact focus-recovery rules are unspecified. | UX |
| **INF-UX-4** | FR-26, FR-32 | Evidence detail likely benefits from a consistent “supports / contradicts / missing” structure, but the information layout and labels are unspecified. | UX |
| **INF-UX-5** | FR-34, NFR-8 | A minimum supported terminal geometry and breakpoint set are needed for acceptance, but no rows/columns are supplied. | UX owns expectation; Architecture owns terminal capability constraints. |
| **INF-UX-6** | FR-35 through FR-40 | A staged action flow likely uses plan → confirmation → pending → verification → outcome, but exact screens, overlays, and dismissal behavior are unspecified. | UX |
| **INF-UX-7** | FR-38 | Unknown-safety confirmation likely requires stronger acknowledgment than safe actions, but the source does not require typed confirmation or a specific gesture. | UX and Product Owner |
| **INF-UX-8** | FR-27 | Accepting or overriding a baseline likely needs a dedicated confirmation surface, but key binding, placement, and override input are unspecified. | UX |
| **INF-UX-9** | FR-33 | Icons may supplement text, but no icon vocabulary, theme, contrast target, or color palette is canonical. | UX |
| **INF-UX-10** | FR-7, NFR-7 | Machine responses likely need a versioned envelope for new Agent operations, but the source does not prescribe schema shape. | Architecture, reviewed by UX for diagnostics |
| **INF-UX-11** | UJ-6, FR-42, FR-43 | Install/upgrade likely needs phase-labelled terminal progress, but the exact command workflow and progress granularity are unspecified. | UX and Release/Architecture |
| **INF-UX-12** | NFR-16 | Findings likely show effective value plus configuration source, but precedence display and configuration-editing UX are unspecified. | UX and Architecture |

## Gaps and conflicts requiring downstream closure

No phase-blocking product question remains according to the PRD. The following
gaps are nevertheless required inputs to a complete UX contract or are tensions
that need an explicit presentation decision.

### Confirmed gaps

- **Numeric acceptance budgets are absent.** Refresh feedback timing, action
  feedback timing, small-terminal dimensions, Collector deadlines, output
  bounds, retention, Heartbeat grace, and verification windows are delegated
  through **Operational acceptance budgets**.
- **Exact information architecture is not fixed.** Attention precedes Stack
  context, and Project/Stack grouping and filters are required, but pane model,
  detail hierarchy, initial focus, breadcrumbs, and back-stack behavior are not
  specified.
- **Search and filter semantics are incomplete.** The source requires both but
  does not define searchable fields, matching rules, composition, clearing, or
  no-result recovery.
- **Responsive behavior lacks breakpoints.** Primary list and essential status
  survive while secondary detail collapses, but minimum geometry and each
  breakpoint's content priority remain open.
- **Microcopy is mostly vocabulary-level.** Canonical state and outcome terms,
  closure reasons, and `stale-identity` are fixed, but headings, explanations,
  confirmations, empty-state text, recovery guidance, and help text are not.
- **Accessibility lacks testable terminal specifics.** Color/Unicode/animation
  independence, ASCII fallback, keyboard access, sanitization, and small-screen
  behavior are explicit; contrast targets, focus indicator form, screen-reader
  expectations, and terminal/backend test matrix are not.
- **Baseline acceptance interaction is incomplete.** Eligibility, override
  audit fields, and explicit acceptance are fixed, but discovery, confirmation,
  key binding/command naming, and incompatible-baseline recovery flow are open.
- **Configuration UX is undefined.** Defaults, validation, and provenance must
  be visible, but configuration file/CLI discovery, precedence explanation, and
  correction guidance are not specified.
- **Installation interaction is outcome-defined, not command-defined.** Staging,
  checks, activation, consumer validation, and rollback are required, but the
  commands, prompts, progress representation, and remediation copy are open.
- **Non-interactive schemas are behaviorally constrained but not specified.**
  Determinism, clean stdout, outcomes, and compatibility are fixed; new Promise
  and reconciliation envelope schemas and version negotiation remain an
  architecture obligation.

### Source tensions and resolutions

| Tension | Source evidence | Required downstream treatment |
| --- | --- | --- |
| “Stack-first TUI” versus attention-first Brief | Section 6.1 calls the TUI Stack-first; FR-29 requires a concise attention summary followed by Stack groups. | Treat attention as the entry summary and Stack as the primary exploration hierarchy. Do not omit either. |
| `unknown` wording versus canonical Evidence Status | FR-20 says incomplete collection yields “`unknown` evidence,” while the canonical Evidence Status values are `sufficient`, `incomplete`, `stale`, and `out-of-scope`. | Do not introduce `unknown` as a fifth Evidence Status without Product clarification. Represent the applicable canonical evidence value and reserve `unknown` for Safe-to-stop Assessment or explanatory prose. |
| Unsafe actions absent/disabled versus informed unknown-safety choice | FR-35 permits unsupported or unsafe actions to be absent or disabled; FR-38 permits an explicit informed choice when safety is unknown. | Distinguish known `unsafe` from `unknown`. Unknown cannot be labeled safe and may proceed only through explicit confirmation; supported but known-unsafe treatment requires UX/Product clarification. |
| Direct shortcuts and contextual menu | FR-35 preserves `s`, `R`, and `x` only where unambiguous and requires `a` plus `?`. | Specify exactly where each shortcut is enabled and ensure the menu/help remain the discoverable path. |
| Action Outcome precedence table is not numerical execution chronology | FR-40 lists `verified` first and `executed-unverified` last while describing terminal classification. | Present exactly one terminal outcome based on the decision rules; do not expose the precedence number as process progress unless UX explicitly validates that interpretation. |
| Optional Provider default may become required | FR-14 promotes supported optional scopes when detected or referenced by an active Promise. | Show effective obligation and its reason, not only static Provider defaults. |

## Downstream closure checklist

The UX contract can claim complete PRD coverage only when it closes or traces
the following items:

- All six `UJ-*` journeys and their named climaxes.
- All 43 `FR-*` requirements, including Agent, CLI, TUI, install, and recovery
  surfaces.
- All 16 `NFR-*` requirements, especially deterministic output, terminal
  restoration, accessibility, partial truth, and concurrency behavior.
- The orthogonal Promise Lifecycle, Evidence Status, Promise Outcome,
  Observation labels, Safe-to-stop Assessment, Collector outcomes, and Action
  Outcome vocabularies.
- Every named FR-34 state and the first-run, incompatible-baseline, incomplete
  baseline, refreshing, stale-identity, and redaction/truncation conditions.
- Keyboard-only navigation; `a`, `?`, and conditional `s`, `R`, and `x` paths;
  explicit TUI start from a Runtime Promise.
- Text, `NO_COLOR`, monochrome, ASCII, sanitized-untrusted-data, and
  small-terminal behavior.
- Default partial-truth and strict non-interactive behavior, clean stdout,
  deterministic exits, and legacy output compatibility.
- Exact-target planning, confirmation, pending/race behavior, identity
  revalidation, verification, and one canonical terminal Action Outcome.
- Numeric user-visible refresh and feedback expectations owned by UX, with the
  Architecture-owned operational bounds they depend on.
- Traceability to **SM-1** through **SM-6** and safeguards **SM-C1** through
  **SM-C3**.
