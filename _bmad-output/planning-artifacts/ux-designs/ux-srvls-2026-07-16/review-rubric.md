---
reviewer: Doctor Von Code
reviewed: 2026-07-16
verdict: FAIL
---

# Spine Pair Independent Rubric Review — srvls

## Overall verdict — FAIL

The spine pair has strong mechanical coverage: every canonical journey,
requirement, success measure, token reference, component, named application
state, and responsive contract checked by this review is present. The packet
nevertheless fails the independent gate because one explicit user-visible
requirement remains behaviorally unclosed and stable UX identifiers do not
uniquely address several state and budget contracts.

No critical finding was identified. There are **2 high**, **2 medium**, and
**0 low** findings. Resolve the high findings, repair the reconciliation links,
and then move both spines from `draft` to `final` before treating them as the
approved downstream UX contract.

## Severity-ranked findings

### High

#### H1 — Invalid-configuration UX is traced but not specified

The canonical requirement says policy defaults, validation, provenance, and
invalid-configuration failure must be visible
(`../../prds/prd-srvls-2026-07-16/prd.md:762-764`). The source extraction makes
the expected UX surface explicit—configuration errors, finding detail, and
help/reference output—and records configuration discovery, precedence,
correction guidance, and invalid-state treatment as still undefined
(`source-extract-prd-ux.md:171`, `source-extract-prd-ux.md:275-277`).

`EXPERIENCE.md` specifies value/source provenance
(`EXPERIENCE.md:136-139`) and validates only the UX-owned budget ranges
(`EXPERIENCE.md:465-469`), then claims NFR-16 coverage through those passages
(`EXPERIENCE.md:701`). It defines no configuration-error surface or state in
the IA/state contracts (`EXPERIENCE.md:65-76`, `EXPERIENCE.md:173-191`) and no
discovery, precedence, correction, or invalid-value recovery behavior.

**Downstream impact:** architecture and story-dev must invent user-visible
behavior for an explicit NFR, so the UX contract cannot claim complete PRD
coverage.

**Required fix:** add an addressable configuration-error contract covering
where the error appears, exact field/value/source/valid-range treatment,
precedence and default provenance, machine-versus-human output, correction/help
path, and recovery or exit behavior. Architecture may own schema and bounds;
UX must own their visible treatment. Update the NFR-16 trace to that contract.

#### H2 — Stable identifiers are not one-to-one for states and budgets

The identifier audit found **83 definition rows but only 72 unique UX IDs**.
Seven IDs are reused across distinct row-level contracts:

- `UX-ST-1` three times; `UX-ST-2`, `UX-ST-3`, and `UX-ST-6` twice each; and
  `UX-ST-5` five times (`EXPERIENCE.md:175-189`).
- `UX-BUD-2` and `UX-BUD-3` each identify two policies with different defaults,
  valid ranges, and acceptance rules (`EXPERIENCE.md:458-461`).

The state reuse could represent intentional families, but no family/sub-ID
convention is declared. The budget reuse is materially ambiguous: a downstream
reference to `UX-BUD-2` cannot identify whether it means 100 ms refresh
acknowledgement or 2,000 ms slow-refresh disclosure. Trace rows cite the bare
IDs (`EXPERIENCE.md:631`, `EXPERIENCE.md:677`, `EXPERIENCE.md:688`,
`EXPERIENCE.md:698`).

**Downstream impact:** architecture, stories, tests, and acceptance evidence
cannot cite one stable identifier for one testable contract.

**Required fix:** assign unique IDs to every independently testable state and
budget row, or define an explicit family ID plus unique child IDs. Update all
traceability and reconciliation references deterministically.

### Medium

#### M1 — Four reconciliation references point to the wrong component contract

The reconciliation ledger cites `UX-CP-8` for Provider inspection in three
places (`reconcile-source-inputs.md:47`, `reconcile-source-inputs.md:63`,
`reconcile-source-inputs.md:103`), but `UX-CP-8` is the **filter-bar**;
Provider inspection is `UX-CP-7` and evidence inspection is `UX-CP-6`
(`EXPERIENCE.md:157-159`).

The ledger also maps legacy row semantics to `UX-CP-13`
(`reconcile-source-inputs.md:57`), but `UX-CP-13` is the **help-overlay**;
textual/coexisting finding semantics are `UX-CP-14`
(`EXPERIENCE.md:164-165`).

**Downstream impact:** source extraction resolves every ID syntactically but
lands on behavior unrelated to the claimed legacy disposition.

**Required fix:** replace the three inspection references to `UX-CP-8` with the
intended evidence/detail contract and replace the legacy row-semantics
reference to `UX-CP-13` with the intended row/marker contract.

#### M2 — Both canonical spines still declare draft status

`DESIGN.md` declares `status: draft` (`DESIGN.md:4`) and `EXPERIENCE.md`
declares `status: draft` (`EXPERIENCE.md:3`), while their canonical PRD and
addendum sources resolve and declare `status: final`. Draft status is reasonable
during review, but it prevents the pair from being handed off as an approved
canonical contract.

**Downstream impact:** consumers cannot distinguish an accepted spine pair from
work still open to change.

**Required fix:** after H1, H2, and M1 are resolved and revalidated, set both
spines to `status: final` together and retain the shared update date.

## Seven-lens rubric

### 1. Flow coverage — strong

Checked the two frontmatter sources, all six PRD `UJ-*` journeys, the Key Flows,
and the source-traceability tables.

- All **6 of 6** source journeys appear under the exact source IDs and names.
- Every flow has a named protagonist, six numbered steps, a marked climax, and
  an explicit failure path (`EXPERIENCE.md:471-594`).
- All **43 FRs**, **16 NFRs**, and **9 SM/SM-C measures** appear once in Source
  Traceability with exact source names (`EXPERIENCE.md:612-701`).
- Baseline acceptance receives an additional supporting flow
  (`EXPERIENCE.md:596-610`).

No flow-coverage miss was found.

### 2. Token completeness — strong

Checked every DESIGN frontmatter token, every token-like `{path.to.token}`
reference in both spines, token types against the local DESIGN.md reference,
section order, inherited terminal semantics, and contrast treatment.

- The audit found **97 reference occurrences / 25 unique paths / 0 unresolved**.
- Typography uses permitted semantic `note` inheritance
  (`DESIGN.md:9-15`); spacing values are explicit (`DESIGN.md:16-23`).
- All component token references resolve through DESIGN frontmatter
  (`DESIGN.md:24-96`).
- The absent product palette is deliberate terminal-theme inheritance, not a
  missing hex palette (`DESIGN.md:122-148`); load-bearing contrast targets and
  text-only fallback are explicit (`DESIGN.md:140-148`).
- Present DESIGN sections remain in canonical order; omitted Elevation and
  Shapes sections are optional.

No token or shape miss was found.

### 3. Component and responsive coverage — strong

Checked component names across DESIGN frontmatter, DESIGN component prose, and
EXPERIENCE Component Patterns, then walked every IA and responsive contract.

- All three component sets contain the same **16 names**, with no extra or
  missing component (`DESIGN.md:24-96`, `DESIGN.md:197-313`,
  `EXPERIENCE.md:146-167`).
- The IA defines **10 surfaces** spanning Brief, inspection, filtering, action,
  baseline, help, install/recovery, and machine output
  (`EXPERIENCE.md:59-76`).
- The responsive contract defines **6 conditions**: full, compact, narrow,
  below-minimum startup, below-minimum resize, and redirected/TERM-dumb output
  (`EXPERIENCE.md:394-411`).

No component or responsive-coverage miss was found.

### 4. Accessibility and states — adequate

Checked every IA surface against applicable loading, refresh, empty, filter,
Provider denial/failure, focus, action, baseline, terminal, and detail states;
also checked keyboard-only access, text semantics, ASCII/NO_COLOR, assistive
alternatives, hostile text, progress, motion, geometry, and restoration.

- All **14 FR-34 states** are present, plus stale-identity,
  post-execution-replacement, and redaction/truncation treatments
  (`EXPERIENCE.md:169-225`).
- Focus recovery is exact-identity based (`EXPERIENCE.md:193-208`).
- Accessibility contracts cover text independence, keyboard/focus, linear
  alternatives, sanitization/redaction, progress/motion, and the acceptance
  matrix (`EXPERIENCE.md:357-392`).

Content coverage is strong, but H2 prevents state rows from being cited as
one-to-one stable contracts.

### 5. Mock/wireframe coverage — strong

Checked `imports/`, `mockups/`, and `wireframes/`, all inline references, the
Foundation disposition, reconciliation ledger, and memlog decision.

- The three artifact directories are absent and contain **0 files**; neither
  spine contains an inline visual-artifact reference, so there are no orphans.
- The packet explicitly declares every required terminal surface spine-only and
  records that no layout blocker requires a mock (`EXPERIENCE.md:15-20`,
  `reconcile-source-inputs.md:50`, `.memlog.md:13`).
- Full, compact, narrow, and failure geometry are specified textually and
  testably, making the no-mock disposition defensible for this terminal product.

No mock/wireframe-coverage miss was found.

### 6. Voice and operational states — thin

Checked canonical nouns, axis values, state/outcome words, time/provenance,
recovery language, empty/error copy, lifecycle stages, baseline handling,
machine/human separation, and install/recovery feedback.

- The four source axis value sets match the PRD exactly
  (`EXPERIENCE.md:25-34`; source at
  `../../prds/prd-srvls-2026-07-16/prd.md:151-156`).
- Voice is calm, exact, and recovery-oriented, with prohibited false reassurance
  stated explicitly (`EXPERIENCE.md:114-144`).
- Action, Agent, baseline, install, and machine-result contracts use the
  canonical operational vocabulary and preserve clean stdout
  (`EXPERIENCE.md:268-355`).

H1 is a required operational-state miss: invalid configuration has no visible
treatment or correction voice.

### 7. Inheritance discipline — adequate

Checked frontmatter, source resolution/status, exact UJ/FR/NFR/SM names,
canonical axis vocabulary, section shape, component naming, token references,
legacy precedence, UX-ID definitions/references, and phase-closure statements.

- DESIGN and EXPERIENCE list the same two relative sources; all four references
  resolve to the final PRD and final addendum (`DESIGN.md:5-8`,
  `EXPERIENCE.md:5-8`).
- Source IDs and names match exactly; all token and canonical UX references
  resolve; no undefined canonical UX ID was found.
- Spine/source precedence is explicit and consistent
  (`DESIGN.md:118-120`, `EXPERIENCE.md:15-20`,
  `reconcile-source-inputs.md:19-31`).

M1 weakens semantic traceability despite syntactic resolution, and M2 leaves
the pair explicitly unfinalized.

## Frontmatter, vocabulary, and source-resolution notes

- YAML frontmatter parsed successfully in DESIGN, EXPERIENCE, reconciliation,
  PRD, and addendum.
- Spine source lists are identical; every relative source exists and has
  `status: final`.
- Canonical Promise Lifecycle, Evidence Status, Promise Outcome, Observation
  label, Safe-to-stop, Collector, and Action Outcome vocabulary is preserved.
- No undefined `{path.to.token}` or canonical `UX-*` reference was found.
- There is no Mermaid content to validate.
- No `[ASSUMPTION]`, `[NOTE FOR UX]`, `TODO`, or `TBD` marker remains in the UX
  packet. The memlog's original visual assumption is superseded by a Team Argus
  decision (`.memlog.md:10-13`).

## Phase blockers

1. **UX approval is blocked** by H1 and H2. M1 must be repaired before the
   reconciliation ledger is reliable, and M2 must be closed before handoff.
2. **Implementation readiness remains externally conditional** on the
   Architecture-owned Collector deadlines, capture caps, retention, Heartbeat
   grace, and verification limits. The PRD requires both UX- and
   Architecture-owned operational budgets before `READY`
   (`../../prds/prd-srvls-2026-07-16/prd.md:814-819`), and the reconciliation
   ledger correctly leaves those numeric bounds to Architecture
   (`reconcile-source-inputs.md:107-109`). This is not an additional UX defect.
3. The Operator-impact measure is required before beta evaluation but is
   explicitly not an implementation-planning blocker
   (`../../prds/prd-srvls-2026-07-16/prd.md:816-819`).

## What was checked

- `.agents/skills/bmad-ux/references/validate.md` in full.
- All configured DESIGN/EXPERIENCE examples and the local DESIGN.md token spec.
- `DESIGN.md`, `EXPERIENCE.md`, `reconcile-source-inputs.md`, both source
  extracts, `.memlog.md`, the canonical PRD, and its addendum in full.
- Seven requested lenses: flow; tokens; components/responsive; accessibility/
  states; mocks/wireframes; voice/operational states; inheritance.
- Stable identifiers, frontmatter, source paths/status, canonical vocabulary,
  section shape, unresolved markers, and phase blockers.

## Deterministic command results

### Structured YAML/Markdown audit

An inline read-only Python 3 + PyYAML audit parsed the five frontmatter-bearing
contracts, resolved relative sources and token paths, and extracted Markdown
IDs/tables/headings.

```text
exit: 0
frontmatter: DESIGN=draft, EXPERIENCE=draft, reconciliation=final,
             PRD=final, addendum=final
sources: 4/4 resolved; spine source lists equal
token references: 97 occurrences, 25 unique, 0 unresolved
components: 16 frontmatter = 16 DESIGN body = 16 EXPERIENCE; no differences
flows: 6/6 exact names; each 6 steps + protagonist + climax + failure
traceability: FR 43/43; NFR 16/16; SM/SM-C 9/9; 0 name mismatches
FR-34 states: 14/14 plus 3 additional treatments
IA surfaces: 10; responsive contracts: 6
visual artifacts: 0; inline visual references: 0; orphans: 0
UX IDs: 83 definition rows, 72 unique IDs, 0 undefined references
canonical axis values: exact match
```

### UX packet Markdown lint

Command:

```sh
markdownlint-cli2 --config _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/.markdownlint-cli2.jsonc \
  _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/DESIGN.md \
  _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md \
  _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/reconcile-source-inputs.md \
  _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/source-extract-prd-ux.md \
  _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/source-extract-legacy-live-ux.md
```

Result: **exit 0; 5 files; 0 errors**.

### Canonical-source lint note

Adding the canonical PRD and addendum to the same lint command produced
**exit 1; 2 errors**: MD025 at
`../../prds/prd-srvls-2026-07-16/prd.md:8` and
`../../prds/prd-srvls-2026-07-16/addendum.md:8`, because each source has a
frontmatter `title` plus an H1. The five-file UX packet itself is clean; the two
upstream style findings do not control this UX verdict.
