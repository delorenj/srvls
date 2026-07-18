# PRD Structural Review — srvls Runtime Promise Reconciliation and Morning Handoff

## Document Summary

- **Purpose:** This document exists to help the product owner and downstream UX, architecture, epic, story, and readiness workflows agree on what `srvls` must do and how its product outcomes are proven.
- **Audience:** Solo builder-operator, product and design reviewers, architects, implementers, test planners, and planning agents.
- **Reader type:** Humans.
- **Structure model:** Strategic/Context (Pyramid), with a reference-shaped requirement core.
- **Current length:** 7,759 words across 19 major sections: 7,212 words and 14 H2 sections in `prd.md`, plus 547 words and five H2 sections in `addendum.md`.

## Structural Map

| PRD section | Words | Structural job |
| --- | ---: | --- |
| 0. Document Purpose | 177 | Establish canonical status, current-versus-target reading rule, and evidence basis. |
| 1. Vision | 220 | State the product thesis, authority boundary, and why-now case. |
| 2. Target User | 830 | Define users, jobs, and six outcome-driving journeys. |
| 3. Glossary | 1,068 | Define domain nouns, reconciliation axes, and deterministic transitions before requirements use them. |
| 4. Features and Functional Requirements | 3,311 | Provide the canonical, consistently shaped `FR-*` contract. |
| 5. Non-Goals | 118 | Preserve permanent product boundaries. |
| 6. MVP Scope | 292 | Preserve owner-approved phase scope and revisit conditions. |
| 7. Success Metrics | 274 | Define primary, secondary, and counter-metric acceptance evidence. |
| 8. Cross-Cutting Non-Functional Requirements | 475 | Define system-wide quality and safety constraints. |
| 9. Constraints and Guardrails | 140 | Consolidate safety, privacy, and compatibility invariants. |
| 10. Integrations and Dependencies | 94 | Name external and local authority boundaries. |
| 11. Risks and Mitigations | 150 | Make principal product risks and required controls scannable. |
| 12. Open Questions | 29 | State phase-blocking question status. |
| 13. Assumptions Index | 26 | Close the assumptions roundtrip. |

## Recommendations

No substantive changes recommended — document structure is sound.

### 1. PRESERVE — Purpose, vision, user journeys, then vocabulary

**Rationale:** The sequence gives decision-makers the conclusion and product boundary first, then supplies user context and domain definitions before the reference-heavy requirement core.

**Impact:** 0 words.

### 2. PRESERVE — Separate Non-Goals from MVP Scope

**Rationale:** Non-Goals encode durable product identity, while MVP Scope records phase-specific inclusions, exclusions, and revisit conditions; merging them would erase that distinction.

**Impact:** 0 words.

### 3. PRESERVE — Keep the requirement core in one canonical file

**Rationale:** The six feature groups and consistent requirement schema support random access and stable-ID extraction; sharding 43 requirements now would increase navigation and traceability cost.

**Impact:** 0 words.

### 4. PRESERVE — Keep technical direction and legacy mapping in the addendum

**Rationale:** The addendum prevents solution mechanisms and migration history from interrupting the product contract while retaining authoritative downstream constraints.

**Impact:** 0 words.

### 5. PRESERVE — Keep explicit Open Questions and Assumptions Index sections

**Rationale:** Their short negative declarations are closure evidence for downstream gates, not redundant narrative.

**Impact:** 0 words.

## Summary

- **Total recommendations:** Five preservation decisions; zero cuts, merges, moves, or condensations.
- **Estimated reduction:** 0 words (0%).
- **Meets length target:** No target specified.
- **Comprehension trade-offs:** None. The current length is earned by safety-sensitive product contracts and stable-ID requirements rather than orientation or persona theater.
