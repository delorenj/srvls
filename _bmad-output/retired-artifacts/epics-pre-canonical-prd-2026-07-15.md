---
stepsCompleted:
  - step-01-validate-prerequisites
  - step-02-design-epics
  - step-03-create-stories
  - step-04-final-validation
inputDocuments:
  - README.md
  - srvls
  - tests/test_smoke.sh
  - docs/architecture.md
  - _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md
status: superseded
supersededBy:
  - _bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md
  - _bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/addendum.md
  - _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/DESIGN.md
  - _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md
  - _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md
---

<!-- markdownlint-disable MD024 -->

# srvls - Superseded Epic Breakdown

> **DO NOT IMPLEMENT OR ASSIGN THESE STORIES.** This retained decomposition
> predates the canonical Runtime Promise PRD/addendum and final UX contracts.
> Its legacy `FR1`–`FR18`, `NFR1`–`NFR10`, `UX-DR1`–`UX-DR8`, `Entry` model,
> action outcomes, and binary-only release stories are historical only. After
> the architecture spine is final, a new epic/story artifact must be generated
> from all 154 canonical requirements, nine supplemental metrics, and AD-1
> through AD-25. Until then there is no authoritative implementation backlog.

## Overview

This document preserves the retired pre-PRD decomposition for audit history.
Nothing below this notice is an implementable or acceptance-bearing story.

## Requirements Inventory

### Functional Requirements

FR1: Collect user, root, `/etc/crontab`, and `/etc/cron.d` cron entries into the unified inventory.

FR2: Collect system and user systemd services and timers, including enablement, runtime state, schedule, and provenance.

FR3: Collect Docker containers with runtime state, health, restart policy, Compose project, and working-directory evidence.

FR4: Collect PM2 processes with runtime state, restart count, working directory, namespace, and stable observed identity.

FR5: Normalize every provider resource into one composed, provider-neutral `Entry` aggregate without provider-specific inheritance.

FR6: Return inventory entries together with explicit per-collector completeness and diagnostic outcomes.

FR7: Open the ratatui interface by default when stdin and stdout are interactive terminals, while retaining non-interactive table behavior for redirected execution.

FR8: Group entries by inferred stack by default using deterministic provider-native, source-location, and conservative name-similarity evidence.

FR9: Display each inferred stack's label, membership, confidence, and evidence while retaining ambiguous entries in an Ungrouped section.

FR10: Provide keyboard navigation, filtering, stack expansion, refresh, help, inspection, and responsive small-terminal behavior in the TUI.

FR11: Display strategic semantic color and provider/status icons with text, `NO_COLOR`, and ASCII fallbacks.

FR12: Inspect cron, systemd, Docker, and PM2 entries with bounded provider-appropriate status and log detail.

FR13: Start, stop, restart, and disable/delete individual supported entries using typed provider actions, identity revalidation, and post-action verification.

FR14: Require TUI confirmation for stop and disable/delete and prevent mutation from stale snapshots; stack groups remain read-only in v1.

FR15: Preserve the flat JSON, Prometheus, Markdown, table, inspection, executable-name, and explicit CLI-action compatibility contracts unless an intentional deviation is recorded.

FR16: Preserve `--fzf` as a deprecated alias to the ratatui interface and remove the undocumented `--fzf-lines` implementation surface.

FR17: Support visible partial-failure diagnostics and a `--strict` mode with deterministic collector-outcome-to-exit behavior.

FR18: Build, version, install, atomically upgrade, validate, and roll back the standalone Rust binary without breaking existing `srvls` systemd timer consumers.

### NonFunctional Requirements

NFR1: Maintain hexagonal dependency direction: the domain remains independent of host commands, ratatui, clap, and export serialization.

NFR2: Use Rust 2024 with MSRV 1.88, ratatui 0.30.2, a committed lockfile, and locked MSRV/current-stable CI gates.

NFR3: Complete normal inventory refreshes without sequential provider latency by using bounded concurrency and hard subprocess deadlines.

NFR4: Prevent shell and option injection by using argv-only execution, safe end-of-options handling, typed locators, bounded output, child termination, and unconditional reaping.

NFR5: Never elevate the whole process; keep privilege provider-scoped and prevent interactive authorization prompts while terminal raw mode is active.

NFR6: Restore raw mode, alternate screen, and cursor on normal return, errors, panic unwind, Ctrl-C, SIGINT, and SIGTERM shutdown paths.

NFR7: Keep machine-readable stdout free of ANSI, icons, logs, and diagnostics and make emitted ordering deterministic.

NFR8: Make status understandable without color or Unicode and sanitize untrusted control characters before terminal rendering.

NFR9: Verify adapters, grouping, presenters, action safety, and TUI behavior with deterministic fixtures, fakes, goldens, and `TestBackend`; live-host tests remain opt-in.

NFR10: Ship initially for `x86_64-unknown-linux-gnu` on the verified big-chungus glibc 2.42 baseline with checksum verification and reversible installation.

### Additional Requirements

- Capture the checked-in Python compatibility corpus before replacing any provider adapter; `tests/compat` becomes the singular migration authority.
- Start as one binary crate with `domain`, `application`, `ports`, `adapters`, `presentation`, and `cli` modules; split crates only after three proven consumers.
- Model runtime variation with Strategy, Adapter, and Command patterns at their explicit seams; use composition for `Entry` facets and stack view projections.
- Keep collection completion order separate from compatibility output order by retaining adapter encounter ordinals and fixed provider buckets.
- Use monotonic refresh generations and separate operation IDs so stale refreshes cannot replace newer truth or lose action-verification results.
- Define canonical provider identities, including immutable Docker IDs, full systemd unit names, PM2 birth fingerprints, and collision-safe cron locators.
- Keep stack grouping a read-only projection; grouping must never silently widen an action target.
- Centralize host-process semantics in a total `ProcessResult` and reduce collector outcomes through one shared policy.
- Preserve interactive `sudo` only for explicit non-TUI legacy system actions; use non-interactive `sudo -n` for collection and TUI system mutations.
- Stage releases under a versioned path, smoke them before atomic symlink replacement, record the previous target, and support tested rollback.
- Maintain an explicit compatibility ledger for deliberate parser, escaping, privilege, or UX changes from the Python baseline.

### UX Design Requirements

UX-DR1: The default TUI information architecture presents inferred stacks first and ambiguous entries under an explicit Ungrouped section.

UX-DR2: Every row communicates provider, resource name, normalized state/health, and stale/pending/problem status without depending on color alone.

UX-DR3: Central `Theme` and `IconSet` tokens provide strategic status colors and broadly supported Unicode provider/status symbols, with deterministic monochrome and ASCII fallbacks.

UX-DR4: The v1 key map is `q`/`Esc` back or quit, `r` refresh, `/` filter, arrows or `j/k` navigate, `Enter` inspect/expand, `Space` expand/collapse, `s` stop, `R` restart, `x` disable/delete, and `?` help.

UX-DR5: Loading, refreshing, stale, partial-failure, unavailable-provider, empty-inventory, pending-action, verified, unverified, refused, and failed states each have explicit visible treatment.

UX-DR6: Confirmation modals name the exact entry and resolved provider-native operation, capture its identity/generation, and make PM2 deletion visibly destructive.

UX-DR7: Small terminals collapse or hide the detail pane before degrading the primary stack/entry list, while essential status and navigation remain available.

UX-DR8: Inspection/log content is line/byte bounded and stripped of unsafe terminal control sequences before rendering.

### FR Coverage Map

FR1: Epic 1 - Collect all supported cron sources.

FR2: Epic 1 - Collect system and user systemd services and timers.

FR3: Epic 1 - Collect Docker containers and Compose evidence.

FR4: Epic 1 - Collect PM2 processes and stable observed identity.

FR5: Epic 1 - Normalize providers into the composed Entry aggregate.

FR6: Epic 1 - Expose collection completeness and diagnostics.

FR7: Epic 2 - Select ratatui or legacy table based on terminal context.

FR8: Epic 2 - Infer deterministic stacks by native, source, and name evidence.

FR9: Epic 2 - Present grouping evidence, confidence, and Ungrouped entries.

FR10: Epic 2 - Navigate, filter, refresh, inspect, and adapt to small terminals.

FR11: Epic 2 - Render accessible semantic color and icon treatments.

FR12: Epic 2 - Inspect provider resources with bounded detail and logs.

FR13: Epic 3 - Execute supported individual lifecycle actions safely.

FR14: Epic 3 - Confirm destructive actions and prohibit stale/group mutation.

FR15: Epic 1 - Preserve non-interactive and explicit CLI compatibility contracts.

FR16: Epic 2 - Preserve `--fzf` as a deprecated ratatui alias.

FR17: Epic 1 - Report partial failures and implement deterministic strict mode.

FR18: Epic 4 - Install, validate, upgrade, and roll back releases safely.

## Epic List

### Epic 1: Trustworthy Rust Inventory

Operators receive the same unified cron/systemd/Docker/PM2 inventory and exports from the Rust binary, with deterministic compatibility and visible diagnostics.

**FRs covered:** FR1, FR2, FR3, FR4, FR5, FR6, FR15, FR17

### Epic 2: Stack-First Interactive Triage

Operators can explore automatically grouped stacks through ratatui, filter resources, inspect details, refresh safely, and understand state through accessible colors and icons.

**FRs covered:** FR7, FR8, FR9, FR10, FR11, FR12, FR16

### Epic 3: Safe Resource Lifecycle Control

Operators can start, stop, restart, and disable/delete individual resources with confirmation, identity revalidation, privilege safety, and verified outcomes.

**FRs covered:** FR13, FR14

### Epic 4: Reliable Installation and Upgrades

Operators can install, validate, atomically upgrade, and roll back the Rust binary without disrupting existing timers or automation.

**FRs covered:** FR18

## Epic 1: Trustworthy Rust Inventory

Operators receive the same unified cron/systemd/Docker/PM2 inventory and exports from the Rust binary, with deterministic compatibility and visible diagnostics.

### Story 1.1: Freeze the Compatibility Baseline

**Requirements:** FR15; NFR7, NFR9

As an operator,
I want the Python utility's observable behavior captured as deterministic fixtures and goldens,
So that the Rust rewrite cannot silently break my automation.

**Acceptance Criteria:**

**Given** the current Python utility
**When** `tests/compat/capture-baseline.sh` runs
**Then** it captures scrubbed provider fixtures and golden table, JSON, Prometheus, Markdown, inspection, stdout, stderr, ordering, and exit-code behavior
**And** volatile values use documented placeholders.

**Given** an intentional behavioral change
**When** compatibility tests are updated
**Then** `tests/compat/compatibility-ledger.md` identifies and explains it.

### Story 1.2: Run a Typed Rust Cron Inventory

**Requirements:** FR1, FR5, FR6; NFR1, NFR4

As an operator,
I want cron entries represented by the new Rust inventory model,
So that I can validate the architecture through a useful end-to-end slice.

**Acceptance Criteria:**

**Given** the Rust 2024 binary crate
**When** cron collection runs
**Then** all supported cron sources become composed `Entry` values with canonical identities, schedules, provenance, capabilities, and diagnostics
**And** duplicate entries remain independently identifiable.

**Given** unavailable or denied cron sources
**When** collection completes
**Then** available entries remain visible and typed diagnostics describe incomplete sources.

**Given** hostile or malformed fixture content
**When** it is parsed
**Then** no shell is invoked and the result matches the compatibility corpus.

### Story 1.3: Inventory System and User Systemd Work

**Requirements:** FR2, FR5, FR6; NFR1, NFR5

As an operator,
I want systemd services and timers from both scopes in the Rust inventory,
So that I can see scheduled and persistent host work together.

**Acceptance Criteria:**

**Given** captured systemd fixtures
**When** collection runs
**Then** services, enablement, active/sub states, timers, schedules, and scopes match the compatibility corpus.

**Given** one required systemd sub-operation fails
**When** another returns usable entries
**Then** the collector returns `Partial` with entries and subsidiary diagnostics.

**Given** user-scope collection
**When** commands run
**Then** they retain the invoking user's environment and never elevate the process.

### Story 1.4: Inventory Docker Containers

**Requirements:** FR3, FR5, FR6; NFR1, NFR4

As an operator,
I want Docker state and Compose evidence in the Rust inventory,
So that container workloads participate in unified host visibility.

**Acceptance Criteria:**

**Given** Docker containers
**When** collection runs
**Then** state, health, restart policy, image, immutable container identity, Compose project, and working directory are normalized.

**Given** Docker is absent
**When** it is configured as optional
**Then** the outcome is non-fatal `Unavailable`.

**Given** the CLI exists but its daemon is denied, unavailable, malformed, or timed out
**When** collection runs
**Then** the distinct condition is preserved in diagnostics and strict-mode policy.

### Story 1.5: Inventory PM2 Processes Safely

**Requirements:** FR4, FR5, FR6; NFR1, NFR4

As an operator,
I want PM2 processes represented without confusing reused process IDs,
So that refreshed inventory refers to the same observed process.

**Acceptance Criteria:**

**Given** PM2 process data
**When** entries are created
**Then** identity includes PM2 scope, numeric ID, birth timestamp, and executable/name fingerprint.

**Given** PM2 is absent
**When** collection runs
**Then** it produces optional `Unavailable` without failing normal inventory.

**Given** malformed, denied, or timed-out PM2 output
**When** collection completes
**Then** it returns the correct shared outcome and diagnostic categories.

### Story 1.6: Collect Providers Concurrently with Honest Diagnostics

**Requirements:** FR6, FR17; NFR3, NFR4, NFR7

As an operator,
I want inventory to remain responsive and explicit about incomplete providers,
So that missing entries never masquerade as a healthy empty host.

**Acceptance Criteria:**

**Given** all provider adapters
**When** unified collection runs
**Then** a bounded worker set executes them concurrently with hard subprocess deadlines, output caps, termination, and reaping.

**Given** collectors finish in arbitrary order
**When** the snapshot is assembled
**Then** legacy provider buckets and adapter encounter ordinals produce deterministic output.

**Given** `--strict`
**When** outcomes include Partial, Failed, TimedOut, Denied, or required Unavailable
**Then** the command exits nonzero
**And** optional Unavailable alone remains successful.

### Story 1.7: Deliver Compatible Read-Only Outputs

**Requirements:** FR15, FR17; NFR7, NFR9

As an operator,
I want the Rust inventory to preserve existing machine and human outputs,
So that I can evaluate and adopt it without rewriting consumers.

**Acceptance Criteria:**

**Given** identical checked-in fixtures
**When** Python and Rust emit table, JSON, Prometheus, and Markdown modes
**Then** their normalized golden output, ordering, formatting, and exit behavior match except for ledger-approved changes.

**Given** redirected output
**When** any non-interactive mode runs
**Then** stdout contains no ANSI, icons, logs, or diagnostics.

**Given** partial collection
**When** a compatible output is emitted
**Then** healthy entries remain on stdout and diagnostics remain on stderr.

**Given** the Rust read-only milestone
**When** the existing smoke suite and new deterministic suite run
**Then** both pass without requiring live Docker, PM2, sudo, populated cron, or systemd in CI.

## Epic 2: Stack-First Interactive Triage

Operators can explore automatically grouped stacks through ratatui, filter resources, inspect details, refresh safely, and understand state through accessible colors and icons.

### Story 2.1: Infer Stacks Deterministically

**Requirements:** FR8, FR9; UX-DR1

As an operator,
I want related resources grouped into likely stacks automatically,
So that I can reason about services as systems instead of isolated processes.

**Acceptance Criteria:**

**Given** provider-native Docker Compose or PM2 namespace evidence
**When** grouping runs
**Then** it takes precedence over source and semantic evidence.

**Given** Docker/PM2 source paths
**When** grouping runs
**Then** purely lexical normalization produces stable, explainable source keys without resolving symlinks.

**Given** similarly named entries without stronger evidence
**When** at least three share a non-generic project prefix
**Then** a semantic stack is formed using the architecture's normalization and greedy-resolution rules.

**Given** ambiguous or insufficient evidence
**When** grouping completes
**Then** entries remain Ungrouped rather than being forced into a false stack.

**Given** a stack projection
**When** inspected or snapshot-tested
**Then** its stable key, label, confidence tier, evidence reason, and deterministic members are available.

### Story 2.2: Enter and Leave the TUI Safely

**Requirements:** FR7; NFR6; UX-DR5

As an operator,
I want `srvls` to open an interactive terminal interface without risking my shell state,
So that interactive triage feels native and reliable.

**Acceptance Criteria:**

**Given** interactive stdin/stdout and a usable terminal
**When** bare `srvls` runs
**Then** it enters ratatui using the Crossterm backend.

**Given** redirected input/output or `TERM=dumb`
**When** bare `srvls` runs
**Then** it emits the legacy table instead.

**Given** `--tui` and terminal initialization failure
**When** startup runs
**Then** it exits with a clear diagnostic rather than silently changing mode.

**Given** normal exit, error, panic unwind, Ctrl-C, SIGINT, or SIGTERM
**When** the TUI closes
**Then** raw mode, alternate screen, and cursor state are restored by the single terminal-session owner.

### Story 2.3: Browse, Filter, and Refresh Stack Inventory

**Requirements:** FR9, FR10; NFR3; UX-DR1, UX-DR4, UX-DR5, UX-DR7

As an operator,
I want to navigate stacks and resources, filter the inventory, and refresh it safely,
So that I can quickly isolate the workload I care about.

**Acceptance Criteria:**

**Given** grouped inventory
**When** the TUI renders
**Then** stack groups appear before an explicit Ungrouped section with stable selection by identity.

**Given** keyboard input
**When** the operator uses arrows or `j/k`, `Enter`, `Space`, `/`, `r`, `?`, `q`, or `Esc`
**Then** navigation, inspection/expansion, filtering, refresh, help, and back/quit behavior follow the v1 key map.

**Given** overlapping refreshes
**When** results arrive out of order
**Then** only the latest refresh generation can replace displayed inventory.

**Given** a failed refresh after a good snapshot
**When** the failure arrives
**Then** the prior snapshot remains visibly stale and actions remain unavailable.

**Given** a small terminal
**When** space becomes constrained
**Then** detail collapses before the primary stack/entry list loses essential status or navigation.

### Story 2.4: Apply Accessible Color and Icons

**Requirements:** FR11; NFR8; UX-DR2, UX-DR3, UX-DR5

As an operator,
I want strategic visual cues for provider and health state,
So that problems stand out without turning the interface into a rainbow crime scene.

**Acceptance Criteria:**

**Given** normal color and Unicode support
**When** rows render
**Then** semantic status color is primary, provider/status icons are secondary, and text labels always remain.

**Given** `NO_COLOR`
**When** the TUI renders
**Then** no semantic meaning is lost and selection remains visible without color.

**Given** `--ascii`
**When** the TUI renders
**Then** all icons use the deterministic ASCII set.

**Given** stale, pending, healthy, degraded, failed, denied, timed-out, or unavailable state
**When** displayed
**Then** each has a centralized theme token and textual treatment.

### Story 2.5: Inspect Entries and Collection Problems

**Requirements:** FR12; NFR8; UX-DR5, UX-DR8

As an operator,
I want provider-specific details, recent logs, and collection diagnostics in the TUI,
So that I can understand a problem without leaving the inventory.

**Acceptance Criteria:**

**Given** a selected cron, systemd, Docker, or PM2 entry
**When** inspection is requested
**Then** the appropriate inspector returns structured, bounded detail through the application port.

**Given** Docker logs or other untrusted output
**When** details render
**Then** C0/C1 controls are sanitized and byte/line caps are applied before terminal rendering.

**Given** Partial, Unavailable, Denied, TimedOut, or Failed collection outcomes
**When** the operator opens diagnostics
**Then** provider, scope, severity, and safe remediation context are visible without leaking commands, secrets, or environment values.

**Given** loading, empty, stale, unavailable, or failed state
**When** the relevant pane renders
**Then** it presents a specific state treatment instead of an empty-looking success view.

### Story 2.6: Complete Read-Only TUI Compatibility and Tests

**Requirements:** FR16; NFR6, NFR9

As an operator,
I want the new interactive experience to replace the old fzf mode cleanly,
So that I get one maintained interface without losing familiar entry points.

**Acceptance Criteria:**

**Given** `srvls --fzf`
**When** it runs
**Then** it launches the ratatui interface, emits a deprecation notice safely, and does not require `fzf`.

**Given** the undocumented `--fzf-lines` option
**When** invoked
**Then** it is rejected according to the compatibility ledger.

**Given** TUI fixtures
**When** `TestBackend` snapshots and reducer/effect tests run
**Then** grouping, navigation, filtering, small-terminal layout, themes, icons, diagnostics, stale refresh rejection, and terminal shutdown behavior are deterministic.

**Given** the completed Epic 2 milestone
**When** the full test suite runs
**Then** the TUI remains read-only and no lifecycle command can be submitted.

## Epic 3: Safe Resource Lifecycle Control

Operators can start, stop, restart, and disable/delete individual resources with confirmation, identity revalidation, privilege safety, and verified outcomes.

### Story 3.1: Plan and Validate Individual Actions

**Requirements:** FR13, FR14; NFR4, NFR5

As an operator,
I want every lifecycle request resolved into a typed, validated action plan,
So that the utility cannot mutate an unintended or unsupported resource.

**Acceptance Criteria:**

**Given** an Entry and requested public verb
**When** an action is planned
**Then** the plan contains the observed identity, snapshot generation, intrinsic capability, authorization state, resolved provider operation, destructiveness, and verification predicate.

**Given** a cron entry, stack group, stale snapshot, or unsupported capability
**When** an action is requested
**Then** it is refused before any subprocess is created.

**Given** an Entry selected by row position
**When** inventory changes
**Then** the action still targets only its captured EntryId and never a reused row index.

**Given** fake executors and hostile identifiers
**When** plans are tested
**Then** no shell command strings are constructed and unsafe option-like identifiers are rejected unless safely delimited.

### Story 3.2: Control Systemd Units Safely

**Requirements:** FR13; NFR4, NFR5

As an operator,
I want to start, stop, restart, and disable system and user units,
So that I can manage host workloads from the unified utility.

**Acceptance Criteria:**

**Given** a user unit
**When** an action executes
**Then** `systemctl --user` runs in the invoking user's environment.

**Given** a system unit from the TUI
**When** an action executes
**Then** narrowly scoped `sudo -n systemctl` is used and authorization denial cannot prompt inside raw mode.

**Given** an explicit non-TUI system action
**When** it executes
**Then** legacy interactive `sudo systemctl` behavior is preserved and compatibility-tested.

**Given** start, stop, restart, or disable succeeds
**When** verification runs
**Then** it checks active state, inactive state, a newer invocation/start timestamp, or disabled unit-file state respectively.

### Story 3.3: Control Docker Containers Safely

**Requirements:** FR13; NFR4

As an operator,
I want to start, stop, restart, and disable Docker containers,
So that I can recover or quiet container workloads without leaving srvls.

**Acceptance Criteria:**

**Given** a Docker action plan
**When** it is revalidated
**Then** the current immutable container ID must match the observed identity before execution.

**Given** start, stop, restart, or public disable
**When** the adapter resolves it
**Then** it maps to Docker start, stop, restart, or stop respectively using argv-only execution.

**Given** verification
**When** the command completes
**Then** start requires running, stop/disable requires not running, and restart requires the same container ID with changed `StartedAt`.

**Given** the Docker daemon is denied, unavailable, or times out
**When** an action runs
**Then** the result preserves the distinct condition without affecting another entry.

### Story 3.4: Control PM2 Processes Without ID Reuse

**Requirements:** FR13, FR14; NFR4; UX-DR6

As an operator,
I want PM2 lifecycle controls bound to the observed process birth,
So that a recycled numeric ID cannot target a replacement process.

**Acceptance Criteria:**

**Given** a PM2 action
**When** it is revalidated against `pm2 jlist`
**Then** PM2 scope, numeric ID, birth timestamp, executable path, and name fingerprint must all match.

**Given** start, stop, restart, or public disable
**When** resolved
**Then** they map to PM2 start, stop, restart, or delete respectively.

**Given** public disable
**When** presented interactively
**Then** the confirmation explicitly says the PM2 process will be deleted.

**Given** post-action verification
**When** collection completes
**Then** start requires online, stop requires stopped, restart requires a newer restart counter/uptime, and delete requires absence of the full observed identity.

### Story 3.5: Execute and Verify Actions Through the TUI

**Requirements:** FR13, FR14; NFR5, NFR6; UX-DR5, UX-DR6

As an operator,
I want lifecycle actions integrated into the TUI with clear confirmation and outcomes,
So that I can act quickly without sacrificing safety.

**Acceptance Criteria:**

**Given** a current individual entry
**When** `s`, `R`, or `x` is pressed
**Then** stop, restart, or disable/delete is planned for that exact identity; stack headers and stale rows expose no action.

**Given** stop or disable/delete
**When** requested
**Then** a modal names the resource and resolved provider-native operation and requires explicit confirmation; start/restart do not require destructive confirmation.

**Given** repeated keys or duplicate events
**When** one operation is pending
**Then** only one command is submitted for its OperationId.

**Given** a normal refresh races with action verification
**When** results arrive
**Then** operation verification completes independently, while only the latest refresh generation may replace global inventory.

**Given** execution completes
**When** verification succeeds, times out, observes replacement, is refused, or observes a negative predicate
**Then** the TUI displays Verified, Executed-Unverified, Stale, Refused, or Failed respectively and performs no optimistic state mutation.

### Story 3.6: Prove Mutation Safety and CLI Compatibility

**Requirements:** FR14, FR15; NFR4, NFR5, NFR9

As an operator,
I want lifecycle behavior protected by deterministic tests,
So that future changes cannot weaken targeting or privilege safety.

**Acceptance Criteria:**

**Given** the compatibility corpus and fake command runner
**When** action tests run
**Then** direct CLI verb parsing, provider argv, privilege lane, exit status, stdout, and stderr match the approved compatibility ledger.

**Given** leading dashes, whitespace, tabs, newlines, Unicode, control characters, reused IDs, replaced resources, duplicate submissions, timeouts, and denials
**When** adversarial tests run
**Then** the action is safely delimited, refused, or reported without shell execution or wrong-target mutation.

**Given** terminal-mode system authorization denial
**When** tested
**Then** no interactive password prompt occurs and terminal restoration remains intact.

**Given** the completed Epic 3 milestone
**When** all suites run
**Then** groups remain read-only, cron remains non-actionable, and live-host state-changing tests remain opt-in.

## Epic 4: Reliable Installation and Upgrades

Operators can install, validate, atomically upgrade, and roll back the Rust binary without disrupting existing timers or automation.

### Story 4.1: Produce a Reproducible Release Artifact

**Requirements:** FR18; NFR2, NFR9, NFR10

As an operator,
I want a versioned, verifiable srvls release binary,
So that I know exactly what is being installed.

**Acceptance Criteria:**

**Given** a release tag
**When** CI builds the project
**Then** it uses the committed lockfile and pinned `x86_64-unknown-linux-gnu` glibc 2.42 build environment.

**Given** the resulting binary
**When** release validation runs
**Then** `cargo fmt`, locked clippy, locked tests, MSRV 1.88, current stable, `readelf` ABI inspection, and artifact smoke tests pass.

**Given** a successful release build
**When** artifacts are published
**Then** the release contains a versioned tarball, installer, and SHA-256 checksum
**And** `srvls --version` matches the release/tag version.

### Story 4.2: Install or Upgrade Atomically

**Requirements:** FR18; NFR10

As an operator,
I want installation to validate the new binary before changing my active command,
So that a failed upgrade cannot strand me without srvls.

**Acceptance Criteria:**

**Given** a downloaded release
**When** installation begins
**Then** its checksum is verified and the staged binary passes `--version`, `--json`, `--prom`, and `--md` smoke checks before link mutation.

**Given** an absent, managed, or known repository `~/.local/bin/srvls` symlink
**When** installation succeeds
**Then** the binary is placed under `~/.local/lib/srvls/<version>/srvls` and a same-directory temporary symlink is atomically renamed over the active link.

**Given** a foreign regular file or foreign symlink
**When** installation runs without `--force`
**Then** it refuses without changing the existing target.

**Given** failure before atomic rename
**When** cleanup runs
**Then** staging is removed and the prior active command remains untouched.

### Story 4.3: Validate Existing Automation After Upgrade

**Requirements:** FR18; NFR7, NFR9, NFR10

As an operator,
I want the installed Rust binary verified against my existing timers and redirected outputs,
So that background metrics and snapshots continue operating after migration.

**Acceptance Criteria:**

**Given** the new active binary
**When** post-install validation runs
**Then** JSON parses, Prometheus contains only approved metric families, Markdown has the expected structure, and redirected outputs contain no ANSI or icons.

**Given** configured srvls metrics and snapshot user services
**When** post-install validation invokes them
**Then** each resolves the new binary, completes successfully, and produces a valid atomic output file.

**Given** a validation failure
**When** installation finalization runs
**Then** the previous target is restored automatically and the failed version remains inactive.

**Given** no configured timer unit
**When** validation runs
**Then** it reports the skipped integration explicitly without treating absence as a product failure.

### Story 4.4: Roll Back to the Previous Version

**Requirements:** FR18; NFR9, NFR10

As an operator,
I want a tested rollback path,
So that I can recover immediately from a release problem.

**Acceptance Criteria:**

**Given** a successful installation
**When** it becomes active
**Then** the previous resolved target and version are recorded in managed installation state.

**Given** a rollback request
**When** the recorded target still exists and passes checksum/ownership validation
**Then** the active symlink is atomically restored to that target.

**Given** the restored binary
**When** rollback validation runs
**Then** version, JSON, Prometheus, Markdown, and configured timer smoke checks pass.

**Given** rollback validation failure
**When** reported
**Then** the installer preserves available binaries and emits manual recovery instructions without deleting either version.
