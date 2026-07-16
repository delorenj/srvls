---
name: srvls
description: "Visual identity contract for the srvls terminal morning handoff and runtime reconciliation experience."
status: draft
sources:
  - ../../prds/prd-srvls-2026-07-16/prd.md
  - ../../prds/prd-srvls-2026-07-16/addendum.md
updated: 2026-07-16
typography:
  terminal-body:
    note: "Inherit the operator terminal monospaced font, size, weight, and line height."
  terminal-emphasis:
    note: "Inherit the terminal font; use bold only as a supplement to explicit heading text."
  terminal-meta:
    note: "Inherit the terminal font; use dim only as a supplement and never for required meaning."
spacing:
  cell: 1ch
  row: 1lh
  gap-sm: 1ch
  gap-md: 2ch
  gap-lg: 4ch
  panel-gap: 1lh
  gutter: 2ch
components:
  brief-summary:
    text: "{typography.terminal-body}"
    heading: "{typography.terminal-emphasis}"
    column-gap: "{spacing.gap-md}"
    section-gap: "{spacing.panel-gap}"
  completeness-banner:
    text: "{typography.terminal-body}"
    heading: "{typography.terminal-emphasis}"
    padding-inline: "{spacing.gutter}"
    padding-block: "{spacing.row}"
  attention-row:
    text: "{typography.terminal-body}"
    meta: "{typography.terminal-meta}"
    column-gap: "{spacing.gap-sm}"
    height: "{spacing.row}"
  group-row:
    text: "{typography.terminal-body}"
    meta: "{typography.terminal-meta}"
    indent: "{spacing.gap-md}"
    height: "{spacing.row}"
  runtime-detail:
    text: "{typography.terminal-body}"
    heading: "{typography.terminal-emphasis}"
    field-gap: "{spacing.gap-sm}"
    section-gap: "{spacing.panel-gap}"
  evidence-table:
    text: "{typography.terminal-body}"
    heading: "{typography.terminal-emphasis}"
    column-gap: "{spacing.gap-md}"
    row-gap: "{spacing.row}"
  provider-detail:
    text: "{typography.terminal-body}"
    heading: "{typography.terminal-emphasis}"
    section-gap: "{spacing.panel-gap}"
  filter-bar:
    text: "{typography.terminal-body}"
    heading: "{typography.terminal-emphasis}"
    item-gap: "{spacing.gap-sm}"
  action-menu:
    text: "{typography.terminal-body}"
    heading: "{typography.terminal-emphasis}"
    item-gap: "{spacing.row}"
    padding-inline: "{spacing.gutter}"
  confirmation-dialog:
    text: "{typography.terminal-body}"
    heading: "{typography.terminal-emphasis}"
    field-gap: "{spacing.row}"
    padding-inline: "{spacing.gutter}"
  operation-status:
    text: "{typography.terminal-body}"
    heading: "{typography.terminal-emphasis}"
    field-gap: "{spacing.gap-sm}"
  baseline-dialog:
    text: "{typography.terminal-body}"
    heading: "{typography.terminal-emphasis}"
    field-gap: "{spacing.row}"
    padding-inline: "{spacing.gutter}"
  help-overlay:
    text: "{typography.terminal-body}"
    heading: "{typography.terminal-emphasis}"
    column-gap: "{spacing.gap-md}"
    padding-inline: "{spacing.gutter}"
  finding-marker:
    text: "{typography.terminal-emphasis}"
    gap-after: "{spacing.gap-sm}"
  machine-result:
    text: "{typography.terminal-body}"
    field-gap: "{spacing.row}"
  install-phase:
    text: "{typography.terminal-body}"
    heading: "{typography.terminal-emphasis}"
    field-gap: "{spacing.gap-sm}"
---

# srvls — Visual Spine

## Brand & Style

srvls should feel like a calm instrument panel built into the shell, not a
dashboard transplanted into a terminal. Its visual job is to make actual Host
truth, intended Agent ownership, incomplete evidence, and action risk readable
at a glance. Density is useful; ambiguity is not.

The posture is **forensic calm**:

- Lead with direct nouns and exact states.
- Preserve alignment and stable reading order across refreshes.
- Use decoration only to reinforce text already present.
- Let the operator's terminal theme remain in control.
- Make partial truth visibly different from a clean Host.
- Keep destructive controls visually quieter than the evidence needed to judge
  them.

The two spines are canonical. DESIGN.md owns visual semantics and
EXPERIENCE.md owns behavior; source extracts and legacy plans cannot override
them.

## Colors

srvls defines no product palette. Foreground and background inherit from the
operator's terminal. ANSI color and style may supplement a textual marker only
when the active terminal supports them and NO_COLOR is absent.

Load-bearing pairs use terminal defaults, not hard-coded colors:

| Role | Required treatment | Optional supplement |
| --- | --- | --- |
| Focus | Prefix the focused row with **>** and preserve the full label. | Reverse or underline the same row. |
| Healthy | Render the word **healthy**. | Conventional success color. |
| Attention | Render every finding label and a **[!]** marker. | Conventional warning color. |
| Incomplete | Render **INCOMPLETE** plus the affected Collector and reason. | Conventional warning color. |
| Failed or refused | Render the exact Action Outcome. | Conventional error color. |
| Stale | Render **STALE** with the last successful refresh time. | Dim nonessential metadata only. |
| Disabled | Keep the action label and append its reason. | Dim the label only if the reason remains full contrast. |

When the application controls both foreground and background, normal text and
focus text target at least 4.5:1 contrast and large heading text targets at
least 3:1. Because the operator may choose any terminal theme, acceptance does
not rely on contrast alone: the no-style rendering must remain complete and
usable.

NO_COLOR disables semantic colors. ASCII mode replaces decorative Unicode
without changing layout meaning. A theme may never hide, reorder, abbreviate
away, or rename a state.

## Typography

All text uses {typography.terminal-body}. srvls neither bundles nor requests a
font. This preserves terminal preferences, remote-session behavior, and
assistive-tool compatibility.

- {typography.terminal-emphasis} is reserved for surface titles, focused
  dialog titles, exact action outcomes, and subsection labels.
- {typography.terminal-meta} may distinguish timestamps, policy provenance,
  and secondary evidence only when the same text remains readable without dim
  styling.
- Uppercase is limited to short persistent states such as INCOMPLETE, STALE,
  PENDING, and VERIFIED. It is not used for prose.
- Truncation never changes canonical state words or exact target identity.
- Times include timezone or offset when a comparison boundary could otherwise
  be ambiguous.

## Layout & Spacing

The grid is terminal-cell native. Horizontal rhythm uses {spacing.cell};
vertical rhythm uses {spacing.row}. Adjacent fields use
{spacing.gap-sm}, columns use {spacing.gap-md}, and major regions use
{spacing.panel-gap}. Dialog content has {spacing.gutter} of horizontal
breathing room whenever geometry permits.

Primary reading order is always:

1. Brief status and Evidence Window.
2. Completeness and attention.
3. Stack or Ungrouped exploration.
4. Runtime and evidence detail.
5. Available action and help hints.

Columns align only when the full labels fit. Narrow layouts wrap prose and
switch structured detail to one label-value pair per line. Primary lists never
require horizontal scrolling. Detail and evidence regions scroll vertically;
long values wrap after preserving their field label.

The responsive contract lives in EXPERIENCE.md. Visual collapse order is:

1. Remove decorative dividers and optional symbols.
2. Hide redundant Provider badges while retaining the Provider word.
3. Move secondary timestamps and policy provenance into detail.
4. Replace side-by-side detail with a full-pane overlay.
5. Keep exact identity, primary state, all finding labels, completeness, focus,
   navigation, and help discoverability.

## Components

Component names are shared exactly with EXPERIENCE.md.

### brief-summary

Uses {components.brief-summary}. The first line names the Evidence Window,
timezone, Accepted Baseline status, current Snapshot, and freshness. The
following lines answer the morning questions with compact labeled counts.
Counts never imply a clean Host when collection is incomplete.

### completeness-banner

Uses {components.completeness-banner}. A complete state is one text line. Any
partial, denied, timed-out, invalid, or excluded evidence expands into one line
per affected Collector with obligation, outcome, duration, and short reason.
The words **INCOMPLETE** and **cannot conclude clean** remain visible.

### attention-row

Uses {components.attention-row}. Anatomy:

**focus marker · finding markers · Provider · exact display identity · Promise
Outcome · Evidence Status · safety · age**

All applicable finding markers remain visible. On narrow terminals, secondary
age moves to detail before any state word is removed.

### group-row

Uses {components.group-row}. Stack and Ungrouped rows begin with **[+]** or
**[-]**, followed by group label, item count, attention count, confidence, and
evidence hint. Group rows never show an action affordance.

### runtime-detail

Uses {components.runtime-detail}. Sections are **Intent**, **Actual Host
truth**, **Reconciliation**, **Ownership**, **Launch**, **Policy**, and
**History**. Promise and Observation axes stay separate. Exact mutation
identity is labeled explicitly and never inferred from the display name.

### evidence-table

Uses {components.evidence-table}. Rows are grouped under **supports**,
**contradicts**, and **missing**. Each row names source, captured time,
freshness, confidence contribution, and bounded value. Missing evidence is an
affirmative row, not blank space.

### provider-detail

Uses {components.provider-detail}. Shows typed Provider fields, provenance,
status output, logs or schedule data, and separate stdout/stderr labels where
available. Truncation and redaction notices appear before the affected block.

### filter-bar

Uses {components.filter-bar}. The first row is the text query; subsequent rows
show active Project, Agent, Provider, and finding facets. Applied facets remain
visible above results in a stable textual form.

### action-menu

Uses {components.action-menu}. The title names the selected Promise or exact
Observation. Each row includes the resolved verb, Provider-native operation,
confirmation level, privilege requirement, and enabled or disabled reason.
Unsupported actions are absent; supported but unsafe actions may remain
disabled so their explanation is discoverable.

### confirmation-dialog

Uses {components.confirmation-dialog}. The dialog gives maximum visual weight
to exact target identity, resolved operation, current generation, Safe-to-stop
Assessment, reasons, expected effect, and verification limit. **Cancel** is
listed first and focused by default. Unknown-safety acknowledgement appears as
a labeled input, never as subtle styling.

### operation-status

Uses {components.operation-status}. Shows one operation ID, target, phase,
elapsed time, and last evidence. Pending and verifying are intermediate phases,
not outcomes. A terminal rendering shows exactly one canonical Action Outcome,
reason code, evidence summary, and next safe step.

### baseline-dialog

Uses {components.baseline-dialog}. Shows candidate Snapshot, current Accepted
Baseline, completeness, Evidence Window effect, timezone, and eligibility.
Override fields appear only when normal acceptance is ineligible.

### help-overlay

Uses {components.help-overlay}. Keys are grouped as **Navigate**, **Inspect**,
**Refine**, **Act**, **Baseline**, and **Exit**. Conditional shortcuts state
their enablement rules. Help fits the compact layout and scrolls at the narrow
layout.

### finding-marker

Uses {components.finding-marker}. The primary form is an ASCII bracketed word
or stable abbreviation followed by the full word in the row or detail:
**[BROKEN]**, **[ORPHAN]**, **[DUP]**, **[STALE]**, **[HOT]**,
**[UNMANAGED]**, and **[ABANDONED]**. Multiple markers coexist; no severity
color replaces them.

### machine-result

Uses {components.machine-result}. Human terminal rendering is one field per
line with the same canonical names used by the machine envelope. Machine
stdout has no borders, color, icons, progress, or prose diagnostics.

### install-phase

Uses {components.install-phase}. Each phase is a persistent text row:
**stage**, **checksum**, **compatibility smoke**, **activate**, **validate
consumers**, and **rollback or retain known-good**. A phase has one of pending,
running, passed, failed, or skipped-with-reason. A spinner may supplement
running but never replace the word.

## Do's and Don'ts

| Do | Do not |
| --- | --- |
| Say **Docker timed out; Host completeness is incomplete.** | Show an empty Docker section as success. |
| Keep Promise Lifecycle, Evidence Status, Promise Outcome, labels, and safety separate. | Compress orthogonal axes into one red/yellow/green status. |
| Prefix focus with **>** and name the selected target. | Depend on reverse video or cursor location alone. |
| Show **executed-unverified** and the missing verification evidence. | Turn a zero Provider exit code into a green success claim. |
| Show disabled unsafe actions with their reason when useful. | Hide risk behind an unexplained missing shortcut. |
| Preserve exact identity before display metadata. | Truncate the immutable target while keeping a friendly name. |
| Escape hostile controls as visible text and disclose truncation. | Render raw control sequences, secrets, or unbounded logs. |
| Keep the previous Snapshot visibly stale during refresh. | Blank the interface or block navigation while collecting. |
| Use the inherited terminal and stable ASCII layout. | Invent a brand palette, logo treatment, animation language, or icon-only vocabulary. |
| Make group rows visibly read-only. | Place action hints on Stack, Project, Agent, or finding groups. |
