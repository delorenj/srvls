---
name: srvls UX source reconciliation
status: final
updated: 2026-07-16
canonical_sources:
  - ../../prds/prd-srvls-2026-07-16/prd.md
  - ../../prds/prd-srvls-2026-07-16/addendum.md
evidence_inputs:
  - source-extract-prd-ux.md
  - source-extract-legacy-live-ux.md
---

# srvls UX Source Reconciliation

This ledger records how the canonical UX contract was derived. It is not a
third spine. DESIGN.md owns visual semantics, EXPERIENCE.md owns behavior, and
the finalized PRD plus addendum own product scope and vocabulary.

## Precedence

When evidence conflicts, the order is:

1. Final PRD and addendum.
2. Canonical UX spines.
3. Approved architecture constraints that do not conflict with the PRD.
4. Current Python behavior and smoke tests as a compatibility floor.
5. Legacy UX candidates and readiness-review observations.

The current Python executable proves present behavior, not target product
scope. Legacy identifiers remain useful for migration traceability but do not
supersede canonical FR, NFR, UJ, or UX identifiers.

## Canonical decisions

| Decision | Canonical disposition | Contract IDs |
| --- | --- | --- |
| Entry hierarchy | The Brief opens with an attention and completeness summary; deterministic Stack groups are the primary exploration hierarchy, followed by explicit Ungrouped. | UX-IA-1, UX-IA-2 |
| Initial focus | Focus starts on the first attention item. With no attention item it starts on the first Stack or Ungrouped item; with no Runtime it starts on the completeness banner. | UX-IP-2, UX-ST-19 |
| Terminal styling | Inherit the operator terminal foreground, background, and monospaced type. Text carries all meaning; optional style never creates a semantic dependency. | UX-A11Y-1, UX-A11Y-3 |
| Action discovery | The **action-menu** opens with a. Direct s, R, and x are conditional accelerators for an exact Observation. Start is available from a Promise through the menu even when no Observation exists. | UX-IA-6, UX-IP-4 |
| Action safety | Supported actions assessed unsafe are absent or disabled with a textual reason. Unknown safety remains available only through stronger typed acknowledgement. Safe does not imply authorization. | UX-ST-20, UX-IP-5 |
| Confirmation | Confirmation captures exact identity and generation, defaults to Cancel, accepts Esc as cancel, suppresses repeated submission, and refuses if identity or generation becomes stale. | UX-IP-5, UX-IP-7 |
| Action lifecycle | Plan, optional confirmation, pending execution, verification, and exactly one canonical terminal outcome are distinct. The outcome precedence table is never shown as progress. | UX-ST-8, UX-ST-9 through UX-ST-13, UX-IP-7, UX-IP-10 |
| Baseline | b opens a dedicated baseline dialog. Normal acceptance requires an eligible complete snapshot; override requires a reason and explicit acknowledgement. Refresh never advances the baseline. | UX-IA-7, UX-IP-6 |
| Search and filters | Slash opens one combined filter surface. Text query and facets compose with AND; multiple values within one facet compose with OR. Active constraints remain visible. | UX-IA-5, UX-IP-3 |
| Responsive floor | Full is at least 120 by 30, compact at least 80 by 24, narrow at least 60 by 20. Below 60 by 20 the TUI shows a resize/table-mode diagnostic rather than an unusable layout. | UX-RP-1 through UX-RP-5 |
| Inspection | Provider evidence is structured, vertically scrollable, searchable, sanitized, and explicitly marked when redacted or truncated. Architecture owns numeric capture caps. | UX-CP-6, UX-CP-7, UX-ST-17 |
| Assistive access | The TUI is keyboard-only and text-first. The additive --linear command sequence is the complete no-cursor human path; legacy table and Markdown remain compatibility views and JSON remains machine-facing. | UX-A11Y-2, UX-A11Y-3, UX-IP-11, SR-A11Y-1 |
| Feedback budgets | Local input, refresh acknowledgement, action acknowledgement, resize, and terminal outcome rendering have numeric UX acceptance targets. Architecture still owns Collector deadlines and action-verification limits. | UX-BUD-1 through UX-BUD-7 |
| Configuration errors | Validation happens before side effects or TUI entry; diagnostics and explain output expose field, value or redaction, source, precedence, default, valid range, correction command, and deterministic machine envelope. | UX-IA-12, UX-ST-18, UX-IP-12 |
| Exit with active operations | q is unavailable during submitted work; Ctrl-C/SIGINT/SIGTERM use phase-specific bounded cancellation or reaping and persist exactly one truthful outcome before terminal restoration. | UX-IP-10 |
| Character and motion modes | NO_COLOR controls color only, --ascii controls glyphs, TERM=dumb implies ASCII table output, and v1 has no animation or spinner mode. | UX-IP-1, UX-A11Y-1, UX-A11Y-5 |
| Mock coverage | Every required terminal surface is fully specified in the two spines. No visual mock is needed for this headless terminal contract. | UX-FND-1 |

## Legacy UX-DR disposition

| Legacy ID | Disposition | Canonical replacement |
| --- | --- | --- |
| UX-DR1 | **Changed and preserved.** Attention now precedes Stack exploration; deterministic Stack and Ungrouped remain. | UX-IA-1, UX-IA-2 |
| UX-DR2 | **Preserved and expanded.** Rows retain provider, identity, and state while adding the orthogonal Promise, evidence, outcome, labels, and safety axes. | UX-FND-2, UX-CP-3, UX-CP-14 |
| UX-DR3 | **Preserved without invented branding.** Centralized semantic styling, NO_COLOR, monochrome, and ASCII behavior remain; no canonical icon or color palette is introduced. | UX-A11Y-1, DESIGN.md |
| UX-DR4 | **Changed.** Legacy navigation remains, a and b are added, and s/R/x become exact-target conditional accelerators. Start has no direct single-key shortcut. | UX-IP-2 through UX-IP-6 |
| UX-DR5 | **Preserved and normalized.** filtered-empty, timed-out, and baseline-unavailable are added; unverified becomes executed-unverified; Stale is not an Action Outcome. | UX-ST-1 through UX-ST-16 |
| UX-DR6 | **Preserved and expanded.** Confirmation includes current Safe-to-stop Assessment, exact Provider-native operation, privilege, captured generation, and stronger unknown-safety acknowledgement. | UX-CP-10, UX-IP-5 |
| UX-DR7 | **Preserved and made testable.** Detail collapses before primary identity/status at the three canonical terminal breakpoints. | UX-RP-1 through UX-RP-5 |
| UX-DR8 | **Preserved with split ownership.** UX specifies treatment and disclosure; Architecture must set line, byte, time, and retention limits. | UX-CP-6, UX-CP-7, UX-ST-17 |

## Live compatibility disposition

| Current behavior | UX disposition |
| --- | --- |
| Bare invocation prints a flat table everywhere. | Preserve that table when either stdin or stdout is not a terminal or TERM is dumb. On an eligible terminal, bare invocation enters the TUI. |
| JSON, Prometheus, Markdown, and table modes are non-interactive. | Preserve deterministic stdout without ANSI, icons, progress, logs, or human diagnostics. |
| External fzf supplies inspection and direct actions. | Retire the dependency. --fzf becomes a deprecated alias to the TUI; --fzf-lines is removed only through the compatibility ledger. |
| Provider buckets and presenters expose stable legacy behavior. | Preserve ordering, fields, escaping, exits, inspection, and action mappings unless the compatibility ledger records an approved deviation. |
| Actions execute immediately and trust names/row position. | Contradicted by the PRD. Replace with exact identity, planning, confirmation policy, revalidation, correlated verification, and canonical outcomes. |
| Provider failure can look empty. | Contradicted by honest partial truth. Show Collector outcome, effective obligation, diagnostic, and why a conclusion is withheld. |
| Provider inspection has inconsistent caps and incomplete sanitization. | Preserve compatible CLI shape while applying bounded and sanitized capture through ledgered behavior. The TUI always discloses redaction and truncation. |

## Retired or prohibited ideas

- External fzf as a runtime dependency.
- The invocable --fzf-lines helper without a compatibility-ledger removal.
- Row position, display name, Stack, Project, Agent, or finding as mutation
  identity.
- Group-wide mutation or automatic remediation.
- Lease expiry, closure, a finding label, or a safe assessment as authorization.
- Optimistic mutation of displayed Host truth.
- Stale as a sixth Action Outcome or unverified as an alias.
- Color, Unicode, animation, or spinner-only semantics.
- Fetching Plane, Git, or Telemetry references from the TUI; they remain opaque.
- A visual palette, icon vocabulary, or brand treatment unsupported by source
  evidence.

## Closed readiness gaps

| Prior gap | UX closure |
| --- | --- |
| No canonical UX artifact | DESIGN.md and EXPERIENCE.md are the canonical paired spines. |
| Undefined TUI start interaction | Promise detail opens the action-menu; supported Start plans from declared Launch Mechanism without requiring an Observation. |
| Undefined focus, pane, and back behavior | UX-IA-1 through UX-IA-12 and UX-IP-2 define hierarchy, initial focus, overlays, selection recovery, and Esc/q behavior. |
| Undefined confirmation mechanics | UX-IP-5 defines default Cancel, exact keys, typed unknown acknowledgement, Esc, repeat suppression, and stale-target refusal. |
| Undefined action-state sequence | UX-ST-8, UX-ST-9 through UX-ST-13, UX-IP-7, and UX-IP-10 define plan through terminal outcome and phase-specific exit. |
| Undefined responsive minimum | UX-RP-1 through UX-RP-5 define geometry, collapse order, resize, and below-minimum behavior. |
| Incomplete accessibility contract | UX-A11Y-1 through UX-A11Y-5 define textual semantics, keyboard focus, assistive alternatives, sanitization, and progress. |
| Undefined inspection treatment | UX-CP-6, UX-CP-7, and UX-ST-17 define scrolling, search, stderr separation, control escaping, redaction, and truncation disclosure. |
| Missing redirected-output and screen-reader acceptance | UX-RP-6 preserves deterministic undecorated compatibility output; UX-A11Y-3, UX-IP-11, and SR-A11Y-1 define and test the complete human-linear journey. |
| Missing user-visible budgets | UX-BUD-1 through UX-BUD-7 publish unique numeric defaults, ranges, and acceptance checks. |
| Undefined configuration-error treatment | UX-IA-12, UX-ST-18, and UX-IP-12 define startup, human, machine, provenance, correction, and recovery behavior. |
| Undefined active-operation exit and signal behavior | UX-IP-10 defines q, Esc, Ctrl-C/SIGINT, SIGTERM, repeated signals, Provider child reaping, durable outcomes, and retrieval for every phase. |
| Conflicting below-minimum q behavior | UX-RP-5 gives underlying modal and operation semantics priority, with q available only from a restored base Brief with no active operation. |
| Undefined ASCII and motion activation | UX-IP-1 defines NO_COLOR, --ascii, TERM=dumb, and precedence; UX-A11Y-5 removes animation and spinners from v1. |

No phase-blocking UX assumption remains. Operational numeric bounds that the
PRD assigns to Architecture are intentionally not invented here and must be
closed in the architecture spine.
