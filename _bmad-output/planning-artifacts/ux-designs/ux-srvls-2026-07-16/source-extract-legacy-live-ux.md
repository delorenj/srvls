# Source Extract: Legacy and Live UX Evidence

**Date:** 2026-07-16
**Purpose:** Reconcile observable Python behavior, legacy `UX-DR1`–`UX-DR8` intent, approved architecture interaction constraints, the 2026-07-15 readiness findings, and the finalized PRD. This is evidence, not a design decision.

## Classification key

- **CURRENT** — observable in the checked-in Python executable or smoke suite.
- **APPROVED TARGET** — required by the finalized PRD and/or final architecture spine, but not current Python behavior.
- **LEGACY CANDIDATE** — intent from `epics.md` or pre-PRD review material that the finalized PRD preserves only partly or with changed semantics; downstream UX must reconcile it.
- **CONTRADICTED** — superseded or explicitly prohibited by newer approved evidence.
- **MISSING** — required detail or verification is absent from the reviewed evidence.

## Live compatibility and UX surfaces

| Status | Evidence item | Reconciliation |
| --- | --- | --- |
| **CURRENT** | Bare `srvls` always collects synchronously and prints a flat table with `TYPE`, `NAME`, `STATE`, `SCHED`, and `SOURCE`, followed by item/failed/unhealthy counts. | There is no current TTY detection or TUI. Table widths cap name at 52 and state at 22 characters, but source text and the total table width are not terminal-responsive. (`srvls`: `out_table`, `main`.) |
| **CURRENT** | Redirected bare execution produces the same legacy table as terminal execution. Explicit `--json`, `--prom`, and `--md` modes also remain non-interactive. | The smoke suite captures all four outputs and checks parse/shape basics. This is the live compatibility surface the target conditional launch must preserve. (`tests/test_smoke.sh`.) |
| **APPROVED TARGET** | Bare invocation opens ratatui only when both stdin and stdout are terminals and `TERM != dumb`; otherwise it emits the legacy table. `--tui` must fail diagnostically if initialization fails. | Final architecture AD-7 and PRD FR-30 approve the predicate. The Python executable does not implement it. |
| **CURRENT** | `--fzf` launches external `fzf`, requires it on `PATH`, previews through `srvls inspect`, and binds `ctrl-s`, `ctrl-r`, and `ctrl-x` to stop, restart, and disable followed by reload. Enter inspects the selected row. | The header exposes these bindings. No confirmation, identity generation, stale check, or verification is present. (`srvls`: `fzf_mode`.) |
| **CURRENT** | Undocumented `--fzf-lines` emits tab-separated type, name, state, and source for fzf reload. | It is an internal-but-invocable implementation surface in the live executable. |
| **APPROVED TARGET** | `--fzf` becomes a deprecated alias to the ratatui TUI without requiring external `fzf`; `--fzf-lines` is removed through the compatibility ledger. | Final architecture AD-7 and PRD FR-30 resolve the architecture review's earlier ambiguity. This intentionally changes the current implementation while preserving the public entry point. |
| **CURRENT** | Inventory is a flat concatenation of cron, system systemd, user systemd, Docker, and PM2 entries. Markdown alone sorts by type and name. | No Project or Stack grouping exists. Provider bucket order and presenter shapes are compatibility-sensitive. (`srvls`: `collect_all`, `out_md`; architecture AD-9.) |
| **CURRENT** | `inspect TYPE NAME` supports cron, systemd, Docker, and PM2. Docker inspection includes 15 recent log lines, merged stderr, and 200-column truncation; systemd/PM2 output is capped at 30 lines; cron prints matching source, schedule, and command. | Commands use argv arrays, and hostile-name smoke tests cover Docker, PM2, and user systemd injection. The current inspector does not sanitize terminal control sequences or enforce a general byte cap. |
| **CURRENT** | Explicit CLI actions are `start`, `stop`, `restart`, and `disable` for systemd, Docker, and PM2; cron refuses with editing guidance. Public `disable` maps to Docker stop and PM2 delete. | System systemd uses interactive `sudo systemctl`; commands execute immediately and return the provider exit code. There is no planning, confirmation, identity revalidation, duplicate suppression, or post-action verification. |
| **MISSING** | The smoke suite does not test `--fzf`, `--fzf-lines`, action mappings, action output/exit behavior, table column values/order, inspection truncation/control sanitization, redirected ANSI absence, terminal sizing, or any TUI behavior. | The architecture requires a one-time compatibility corpus and deterministic TUI snapshots; the current smoke suite proves only a narrower live floor. |
| **MISSING** | Collection failures are generally converted to empty output by `run()`, and no user-facing diagnostic distinguishes unavailable, denied, timed-out, malformed, or genuinely empty providers. | This live ambiguity motivates architecture AD-5 and the PRD completeness/state vocabulary; it must not be mistaken for an approved UX behavior. |

## Legacy UX-DR reconciliation

| Requirement | Status | Legacy intent and finalized-PRD disposition |
| --- | --- | --- |
| UX-DR1 | **LEGACY CANDIDATE** | Legacy intent: inferred Stacks first, ambiguous entries under explicit Ungrouped. **Preserved and expanded** by PRD FR-29: a concise attention summary now precedes deterministic Stack groups, with Project, Agent, Provider, and finding filters. “Stacks first” is therefore no longer literally the complete top-level hierarchy, although Stack-first exploration and Ungrouped remain approved. |
| UX-DR2 | **APPROVED TARGET** | Every row communicates provider, name, normalized state/health, and stale/pending/problem status without color alone. **Preserved in principle** by PRD FR-33/FR-34 and NFR-8, with the newer reconciliation vocabulary and linked evidence broadening what must be communicated. |
| UX-DR3 | **LEGACY CANDIDATE** | Central `Theme`/`IconSet`, strategic status color, Unicode symbols, monochrome, and ASCII fallback. **Behavioral intent preserved** by PRD NFR-8; architecture AD-8 still approves centralized deterministic fallbacks. Exact icon/token choices remain a downstream UX/visual contract, not a PRD decision. |
| UX-DR4 | **LEGACY CANDIDATE** | Legacy keys: `q`/`Esc`, `r`, `/`, arrows or `j/k`, `Enter`, `Space`, `s`, `R`, `x`, `?`. **Changed** by PRD FR-35: `a` opens a discoverable Action Menu containing start/stop/restart/disable-or-delete; direct `s`, `R`, and `x` remain only where unambiguous. The legacy list is incomplete as a finalized key map because it lacks `a` and a start path. |
| UX-DR5 | **LEGACY CANDIDATE** | Explicit loading, refreshing, stale, partial-failure, unavailable-provider, empty, pending, verified, unverified, refused, and failed treatments. **Preserved and normalized** by PRD FR-34/FR-40, which add filtered-empty, timed-out, baseline-unavailable, and the canonical term `executed-unverified`. Legacy `unverified` and architecture-era post-action `Stale` are not canonical final outcomes. |
| UX-DR6 | **LEGACY CANDIDATE** | Confirmation names the exact entry and resolved native operation, captures identity/generation, and makes PM2 deletion destructive. **Preserved and expanded** by PRD FR-38 to include Safe-to-stop assessment and uncertainty; persistent-scheduler disablement is also visibly destructive. Identity capture remains an architecture interaction constraint. |
| UX-DR7 | **APPROVED TARGET** | Small terminals hide/collapse detail before degrading the primary list, retaining essential status and navigation. **Preserved** by PRD FR-34 and NFR-8. No breakpoint, minimum geometry, focus behavior, or exact collapse order beyond “detail first” is specified. |
| UX-DR8 | **APPROVED TARGET** | Inspection/log content is line/byte bounded and unsafe terminal controls are stripped. **Preserved** by PRD FR-16 and NFR-8 and architecture AD-8. Exact caps and truncation affordance remain unspecified. |

## Approved architecture interaction constraints

| Status | Constraint | UX consequence |
| --- | --- | --- |
| **APPROVED TARGET** | The TUI is a single-owner `Model -> Event -> Update -> View` loop with a terminal-session guard restoring raw mode, alternate screen, and cursor on every shutdown path. | Startup, errors, panic/interrupt handling, and exit must not leave the shell damaged. This is architecture support, not proof of a complete interaction design. |
| **APPROVED TARGET** | Stack inference is deterministic and evidence-ranked; groups have stable IDs/labels, confidence/evidence, collision handling, and ambiguous entries remain Ungrouped. | Grouping is explanatory and read-only, never an action identity or implicit action scope. |
| **APPROVED TARGET** | Snapshot truth includes provider diagnostics and completeness. Failed refresh may retain last-good content only when visibly stale; stale rows cannot initiate actions. | Empty-looking success is prohibited for provider failure, and actions must visibly disable/refuse against stale state. |
| **APPROVED TARGET** | Selection and modal targets bind to canonical entry identity plus snapshot generation, never row position. Refresh generations and operation IDs are separate lanes. | A refresh cannot silently retarget an open confirmation; older refresh results cannot replace newer truth; action verification can finish independently. |
| **APPROVED TARGET** | Individual actions follow plan, capability/authorization preflight, confirmation policy, identity revalidation, execution, and correlated verification. Groups remain read-only. | The UI must expose supported/unsupported state and truthful outcomes; it cannot optimistically mutate the displayed resource state. |
| **APPROVED TARGET** | TUI confirmation is required for stop and disable/delete; PM2 public disable resolves to delete. | Confirmation copy must name the exact resource and resolved provider-native operation. The finalized PRD additionally requires Safe-to-stop evidence and uncertainty. |
| **APPROVED TARGET** | Semantic state never depends only on color or Unicode; `NO_COLOR` and `--ascii` have deterministic fallbacks, and selection/focus remains visible. | Accessibility is a behavior floor across rows, diagnostics, modals, and outcomes—not merely a theme option. |
| **APPROVED TARGET** | Inspection is structured, bounded, sanitized, and provider-appropriate; CLI compatibility remains ledger-governed. | TUI detail may improve structure without silently breaking established CLI inspection output. |
| **CONTRADICTED** | Architecture/epic outcome language that reports post-execution replacement as `Stale`. | Final PRD FR-40 makes `stale-identity` a pre-execution refusal reason and post-execution replacement `executed-unverified`; `stale` is not a sixth canonical Action Outcome. |

## Readiness gaps and closure status

| Status | Gap from 2026-07-15 readiness review | Reconciliation after finalized PRD |
| --- | --- | --- |
| **APPROVED TARGET** | Missing canonical PRD made all epic FRs orphaned. | Closed as a source gap by the finalized 2026-07-16 PRD. This report does not reassess full implementation readiness. |
| **MISSING** | No canonical UX artifact; IA, focus order, pane hierarchy, modal behavior, responsive thresholds, state composition, and usability acceptance were distributed across stories. | Still open for the UX artifact. The PRD supplies stronger product requirements but deliberately does not settle all layout/focus/threshold details. |
| **APPROVED TARGET** | The TUI start interaction was undefined: FR13 included start, while UX-DR4 and Story 3.5 exposed only `s`, `R`, and `x`. | Product-level gap closed by PRD FR-35: `a` opens the Action Menu and start has an explicit path from a Runtime Promise even without a running Observation. The architecture spine's legacy key table has not been reconciled to include `a`; exact Action Menu mechanics remain UX work. |
| **LEGACY CANDIDATE** | Story 3.5 bundled action keys, confirmation, duplicate suppression, identity, refresh races, verification, and five outcome presentations. | Final PRD separates these concerns across FR-35 through FR-40, but the legacy implementation story remains overbroad until implementation planning is updated. It must not be treated as the UX screen contract. |
| **CONTRADICTED** | Any reading of lifecycle stories that permits Stack-wide, Project-wide, Agent-group, finding-group, or row-position mutation. | PRD FR-41 and Non-Goals explicitly keep all groups read-only in v1 and require exact individual identity. Group labels, attention rank, expiry, and “safe” assessment never authorize mutation. |
| **LEGACY CANDIDATE** | Legacy actions were framed only around observed provider entries. | Final PRD changes start planning: start may originate from an active Runtime Promise and declared Launch Mechanism even when no running Observation exists. Existing-entry shortcuts remain secondary to the Action Menu. |
| **MISSING** | Responsive behavior says “detail first,” but no breakpoint, minimum supported terminal, truncation/wrapping policy, focus transfer, modal fit, or behavior below the minimum is approved. | PRD NFR-8 requires comprehension without a large terminal; downstream UX must specify testable behavior without inventing product scope. |
| **MISSING** | Accessibility lacks approved focus order, focus indicator behavior in monochrome, screen-reader/terminal assistive assumptions, reduced-motion/animation policy, and help discoverability acceptance criteria. | Text, ASCII, `NO_COLOR`, and keyboard-only operation are approved floors, not a complete accessibility contract. |
| **MISSING** | Exact inspection byte/line caps, truncation indicator/copy, scrolling/search behavior, stderr treatment, and control-character replacement display are not finalized. | Live Python has inconsistent provider-specific line caps and no general sanitization; target requirements establish safety but not detailed UX. |
| **MISSING** | Confirmation behavior does not yet specify default focus, confirm/cancel keys, Esc semantics, repeated-key handling while modal is open, timeout behavior, or presentation when target identity changes before confirmation. | Architecture requires captured identity/generation and refusal; PRD requires exact target, operation, Safe-to-stop assessment, and uncertainty. Interaction details remain unapproved. |
| **MISSING** | Action planning/verification lacks an approved presentation sequence for preflight, pending execution, refresh/verification progress, evidence, reason codes, retry, and next safe step. | PRD FR-36–FR-40 defines truth and canonical outcomes, but not the complete screen/state transition contract. |
| **MISSING** | The current smoke tests do not verify the approved redirected-output predicate or absence of ANSI/icons/diagnostics on stdout. | Architecture and PRD clearly require it; deterministic compatibility and terminal tests remain necessary evidence. |

## Preservation summary against the finalized PRD

- **Preserved:** deterministic Stack grouping with Ungrouped; keyboard-only navigation; accessible text/ASCII/monochrome fallbacks; explicit application states; bounded/sanitized inspection; exact-target confirmation; read-only groups; redirected legacy table; deprecated `--fzf` entry point.
- **Changed:** attention summary now precedes Stack exploration; the Action Menu (`a`) is the discoverable lifecycle surface and supplies the missing start path; state/outcome vocabulary is expanded and canonicalized; confirmations include Safe-to-stop assessment and uncertainty; start may originate from a Runtime Promise without an Observation.
- **Retired or prohibited:** external-fzf implementation dependency; `--fzf-lines`; post-action `Stale` as a canonical outcome; optimistic state mutation; row-position targeting; mutation of Stack/Project/Agent/finding groups; treating expiry, labels, or Safe-to-stop assessment as automatic authorization.

## Sources reviewed

- `srvls`
- `tests/test_smoke.sh`
- `_bmad-output/planning-artifacts/epics.md`
- `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md`
- All four reviews under `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/reviews/`
- `_bmad-output/planning-artifacts/implementation-readiness-report-2026-07-15.md`
- `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md` (reconciliation only)
