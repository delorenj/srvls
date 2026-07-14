# Taskforce Ferris Architecture Review

## Review verdict

The Python-to-Rust and ratatui epic is not implementation-ready until it defines explicit compatibility, identity, grouping, effect, and action-safety contracts. The migration direction is reasonable, but a direct translation of the current Python structures into Rust would preserve accidental coupling while adding asynchronous UI and privilege boundaries that the existing fzf workflow does not safely handle.

This is a gate review, not a replacement architecture. At reviewed HEAD `63757c5`, this worktree contains the Python baseline and `_bmad/` framework files, but no Rust manifest, ratatui implementation, `_bmad-output/` directory, or canonical architecture draft. Winston's canonical artifacts were therefore neither read nor modified. Proposal-facing observations below are acceptance gates derived from the verified brownfield implementation, not claims about text that is absent here.

The current smoke suite passed on the review host with 10 discovered items. It proves that the baseline runs; it does not provide deterministic migration parity or mutation-safety coverage.

## Consolidated findings

- The six-field export record must remain a compatibility projection rather than become the Rust domain model. `state`, `schedule`, `source`, and `detail` carry adapter-specific meanings across cron, systemd, Docker, and PM2, yet every renderer and the interactive layer currently consume them directly ([`srvls`](../srvls#L59), [`docs/component-inventory.md`](component-inventory.md#L25)). A typed internal resource needs stable identity, runtime kind, status/health, provenance, capabilities, and structured diagnostics; only the compatibility presenter should reconstruct the legacy `{type,name,state,schedule,source,detail}` shape.

- Compatibility is broader than JSON field names. The current contract includes the executable name, clone-and-symlink installation, fixed collector order, type identifiers, pretty-printed JSON, metric names and labels, Markdown/table formatting, stdout-versus-stderr placement, exit codes, and surprising argument behavior ([`README.md`](../README.md#L19), [`srvls`](../srvls#L189), [`srvls`](../srvls#L338)). A conventional Rust argument parser would change observable behavior because `--help` and unknown flags currently run the default inventory, flag precedence is hard-coded, and extra inventory arguments are ignored. Every intentional change needs a compatibility ledger and an explicit version boundary.

- Discovery semantics must be frozen with fixtures before collectors are rewritten or parallelized. Cron uses whitespace and username heuristics, systemd filters inactive units and infers timer state from `next`, Docker batches a single inspect over all IDs, and PM2 is scoped to the invoking user's daemon ([`srvls`](../srvls#L41), [`srvls`](../srvls#L83), [`srvls`](../srvls#L141), [`srvls`](../srvls#L169)). Parallel completion order, different timestamp handling, stricter parsing, or per-container error isolation can all produce a more defensible design while still breaking existing snapshots and consumers.

- Partial collection failure is currently indistinguishable from an empty subsystem. The process wrapper ignores child return codes, discards stderr, and converts exceptions/timeouts to an empty string; downstream JSON failures then become empty collections ([`srvls`](../srvls#L31), [`docs/deployment-guide.md`](deployment-guide.md#L40)). Rust `Result` propagation must not accidentally convert tolerated failures into a total CLI failure, but preserving silent absence is also unsafe. The application contract should return inventory plus per-source completeness/diagnostic status, while compatibility modes retain a deliberate, tested exit policy.

- The minimum useful hexagonal seams are inventory source, inspector, action planner/executor, stack resolver, audit sink, clock, and load provider. External-process/filesystem parsing belongs in adapters; orchestration, policy, and capability intersection belong in the application/domain; CLI, exports, and ratatui belong in presentation. Without these ports, widgets or renderers will acquire subprocess, privilege, timing, and adapter knowledge that cannot be tested independently.

- A multi-crate workspace would be premature for a 364-line product whose own brownfield documentation warns against structure for structure's sake ([`docs/source-tree-analysis.md`](source-tree-analysis.md#L49)). Start with one package and enforce dependency direction between `domain`, `application`, `ports`, `adapters`, and `presentation` modules. The domain must not import ratatui/crossterm, process execution, or legacy serialization concerns; crates should be split only when independent compilation, ownership, reuse, or release becomes real.

- Stack grouping cannot safely be inferred from the existing `source` string. Docker uses a Compose working directory or project, systemd uses enablement state or an activated unit, PM2 uses a working directory, and cron uses an account/file source ([`srvls`](../srvls#L59), [`srvls`](../srvls#L111), [`srvls`](../srvls#L131), [`srvls`](../srvls#L159), [`srvls`](../srvls#L179)). A stack resolver should emit a stable stack ID, membership evidence, provenance, and confidence/unknown state. Display grouping must remain distinct from mutation scope.

- Group actions are unsafe unless capability is computed as the conservative intersection of member capabilities. The current shared verb `disable` means systemd disable, Docker stop, and PM2 delete ([`srvls`](../srvls#L255), [`docs/deployment-guide.md`](deployment-guide.md#L45)). A group must never inherit the union of adapter verbs, and a display group must not become actionable merely because one member supports an operation. Mixed-scope, partial-failure, ordering, and rollback semantics must be specified before any stack-level action is exposed.

- Resource names are not stable identities. CLI actions currently accept arbitrary `type` and `name` values without binding them to the snapshot from which an operator selected them ([`srvls`](../srvls#L267), [`srvls`](../srvls#L338)). In a refreshing TUI, a container, process, or unit can disappear and be replaced under the same name between render and execution. Confirmation must bind action, stable resource identity, and snapshot generation; execution must revalidate immediately before mutation.

- Ratatui needs a unidirectional state/effect architecture rather than I/O in event handlers. Current collection is sequential and individual calls can wait 15 to 30 seconds ([`srvls`](../srvls#L31), [`srvls`](../srvls#L143), [`srvls`](../srvls#L153)). Terminal and worker events should become intents processed by a pure reducer; effects should run off-loop and return operation/generation-tagged results; rendering should consume an immutable view model. The design also needs cancellation, stale-result rejection, single-flight mutation, and explicit pending/degraded states.

- Interactive command construction is presently more dangerous than direct CLI dispatch. fzf preview and keybindings interpolate the script path, resource type, and resource name into shell-parsed command strings, while the hostile-name regression test covers only direct `inspect` argument arrays ([`srvls`](../srvls#L317), [`tests/test_smoke.sh`](../tests/test_smoke.sh#L82)). Ratatui must pass opaque typed IDs to application commands and must not reproduce command strings or shell interpolation.

- Argument arrays eliminate ordinary shell interpolation but do not eliminate option injection. A resource name beginning with `-` can still be interpreted by systemctl, Docker, or PM2 as an option ([`srvls`](../srvls#L255), [`srvls`](../srvls#L296)). Each adapter needs a typed identifier policy, supported end-of-options handling, and command-contract tests for leading dashes, tabs, newlines, Unicode, and control characters.

- Privilege escalation cannot be delegated to a ratatui widget. System actions currently use potentially interactive `sudo systemctl`, whereas root-cron collection uses `sudo -n` ([`srvls`](../srvls#L65), [`srvls`](../srvls#L258)). A password prompt during raw/alternate-screen mode can hang the action or corrupt terminal restoration. Authorization should be preflighted and represented through a noninteractive privilege/executor boundary, with terminal cleanup guaranteed for failures and panics.

- Every mutation needs a single policy pipeline: plan, authorize, confirm, revalidate, execute, verify, and audit. Current actions execute immediately, return only the child status, and have no confirmation or durable record ([`srvls`](../srvls#L267), [`docs/architecture.md`](architecture.md#L86)). Destructive PM2 deletion warrants typed confirmation; repeated keys and duplicate events must not double-submit; the audit record should capture redacted target identity, requested and resolved action, policy decision, timestamps, result, and postcondition.

- Executable and environment resolution is a trust boundary. All adapters inherit `PATH` and process environment, while mise prepends project paths and materializes `.env` on entry ([`srvls`](../srvls#L31), [`mise.toml`](../mise.toml#L4)). The command-runner port should use a defined executable-resolution policy and explicit environment allowlist so a poisoned path, Docker context, PM2 home, locale, or timezone cannot silently redirect collection or privileged action behavior.

- Inventory fields and inspected logs are untrusted terminal and export content. The tool can expose cron commands, service names, process paths, Compose directories, and Docker logs; Markdown and Prometheus escaping are already incomplete ([`srvls`](../srvls#L211), [`srvls`](../srvls#L237), [`srvls`](../srvls#L296), [`docs/architecture.md`](architecture.md#L102)). Ratatui must sanitize terminal controls, cap bytes/lines, and define redaction boundaries. Safer escaping is an intentional output-contract change and should be validated semantically rather than hidden inside the rewrite.

- The existing smoke test is too weak to serve as a migration oracle. It runs against the live host, checks required JSON keys only on the first record, does not mock failures, and deliberately avoids state-changing coverage ([`tests/test_smoke.sh`](../tests/test_smoke.sh#L12), [`docs/development-guide.md`](development-guide.md#L47), [`docs/architecture.md`](architecture.md#L98)). Deterministic fixtures are required for every adapter, record type, output mode, CLI exit/stdout/stderr case, malformed response, timeout, permission denial, escaping edge, replacement race, cancellation, duplicate submission, and audit failure.

- Combining the language rewrite, domain extraction, asynchronous TUI, stack grouping, safer actions, diagnostics, packaging, and release changes in one vertical cut removes any trustworthy parity checkpoint. The epic should be decomposed so each stage has a runnable compatibility oracle and an independently reversible boundary. Otherwise a failure can be attributed to parsing, scheduling, grouping, presentation, privilege, or packaging with no stable reference point.

## Implementation decomposition gates

- Capture Python behavior first with deterministic adapter fixtures, golden exports, CLI behavior cases, and an intentional-deviation ledger. Include malformed and unavailable-tool behavior, not only happy-path host snapshots.

- Introduce the typed Rust domain, structured collection outcome, ports, and compatibility presenters in a single package. Prove dependency direction and byte/semantic parity without ratatui or mutations.

- Replace collectors one adapter at a time behind the same inventory-source contract. Compare Python and Rust results from identical fixtures and retain per-source diagnostics without changing the chosen compatibility exit policy accidentally.

- Add the CLI and noninteractive export path before the TUI. Validate executable naming, installation/release behavior, stdout/stderr, exit codes, JSON, metrics, Markdown, ordering, and operational timer compatibility.

- Add ratatui as a presentation adapter over a pure reducer and effect runner. Prove terminal restoration, cancellation, generation handling, stale-result rejection, control-sequence sanitization, and read-only inspection before enabling mutation.

- Add stack resolution as independently observable metadata with evidence and confidence. Keep groups read-only until identity stability, capability intersection, mixed-scope policy, and partial-failure behavior are tested.

- Enable actions last through the centralized plan/authorize/confirm/revalidate/execute/verify/audit pipeline. Use fake executors for destructive and privilege tests; keep live-host smoke tests read-only.

## Exit criteria for architecture approval

- Every preserved and intentionally changed brownfield behavior is enumerated and testable.
- Domain types do not depend on ratatui, external command execution, or legacy output serialization.
- Collection returns explicit completeness and diagnostics without making one adapter failure erase healthy inventory.
- Stack identity includes evidence/confidence and cannot silently expand display grouping into an action scope.
- TUI effects cannot block rendering or apply stale results, and mutation submission is idempotent/single-flight.
- Target identity is revalidated and action capability is resolved per resource immediately before execution.
- Privilege, confirmation, environment, terminal-sanitization, redaction, and audit policies have executable tests.
- A staged rollout can stop after any phase with a usable noninteractive CLI and a known rollback path.
