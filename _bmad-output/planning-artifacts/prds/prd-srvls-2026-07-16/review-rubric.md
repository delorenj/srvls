# PRD Quality Review — srvls Runtime Promise Reconciliation and Morning Handoff

- **PRD:** `prd.md`
- **Addendum:** `addendum.md`
- **Rubric:** `.agents/skills/bmad-prd/assets/prd-validation-checklist.md`
- **Review date:** 2026-07-16
- **Review scope:** Independent documentation review of the current PRD and addendum; permitted evidence artifacts were used only to test source support and residual gaps.

## Overall verdict

This is a substantive, unusually traceable chain-top PRD: it has a specific product thesis, honest coverage and safety semantics, contiguous requirements, testable Functional Requirement consequences, and a clean current-state/target-state boundary. The remaining weakness is narrower than a phase blocker: success is expressed mainly as fixture conformance, while several performance, output, and retention constraints promise a bound without supplying an acceptance budget. The rubric gate **passes** with no critical or high findings; those two medium gaps should close before beta evaluation and implementation acceptance, respectively.

## Weighted score and pass/fail gate

The canonical rubric defines qualitative verdicts but does not supply numeric weights, a verdict-to-number mapping, or a pass threshold (`prd-validation-checklist.md:7-13`). To satisfy the commissioned weighted-score requirement without attributing invented rules to the rubric, this review applies the following explicit overlay: `strong = 100%`, `adequate = 75%`, `thin = 50%`, and `broken = 0%` of each dimension's weight. Weights reflect this chain-top PRD's downstream use and the rubric's instruction to be especially unforgiving about done-ness (`prd-validation-checklist.md:78-88`) and downstream extraction (`prd-validation-checklist.md:102-123`).

| Dimension | Weight | Verdict | Factor | Weighted points |
| --- | ---: | --- | ---: | ---: |
| Decision-readiness | 15 | strong | 1.00 | 15.00 |
| Substance over theater | 10 | strong | 1.00 | 10.00 |
| Strategic coherence | 15 | adequate | 0.75 | 11.25 |
| Done-ness clarity | 20 | thin | 0.50 | 10.00 |
| Scope honesty | 15 | adequate | 0.75 | 11.25 |
| Downstream usability | 15 | strong | 1.00 | 15.00 |
| Shape fit | 10 | strong | 1.00 | 10.00 |
| **Total** | **100** |  |  | **82.50** |

**Gate rule:** PASS requires a weighted score of at least 75, no critical or high finding, no broken dimension, and no more than one thin dimension. **Result: PASS (82.50/100; 0 critical, 0 high, 2 medium, 0 low; 0 broken, 1 thin).** The corresponding qualitative grade is **Good**: one thin dimension and no critical/high finding.

## Decision-readiness — strong

The document states its decisions as contracts. Section 0 distinguishes the checked-in Python product from target behavior and assigns product-visible requirements to the PRD while isolating implementation mechanisms (`prd.md:10-16`). The Vision chooses a narrow ownership boundary—runtime liveness and reconciliation rather than Plane, Git, or Telemetry replacement (`prd.md:18-28`)—and Sections 5 and 6 name what is given up: no unattended cleanup, group mutation, hosted control plane, fleet scope, non-Linux support, or broad Provider coverage (`prd.md:620-658`). Deferred scope has revisit conditions rather than neutral “later” language (`prd.md:648-657`).

The previously inherited Rust, TUI, safe-mutation, and release direction is explicitly identified as owner-approved brownfield scope rather than disguised as research-derived product truth (`prd.md:633-646`). The addendum separates approved technical direction from mandatory planning corrections and unresolved architecture decisions (`addendum.md:14-28`, `addendum.md:57-63`). That makes the principal trade-offs visible and actionable.

### Findings

No findings.

## Substance over theater — strong

The Vision is product-specific: “The product makes a machine stop feeling haunted” is immediately grounded in a Brief that combines Agent-declared intent, fresh scoped observations, uncertainty, provenance, and conservative action evidence (`prd.md:18-28`). The two protagonists are not persona furniture: Jarad's five journeys and Ava's machine-user journey each terminate in requirements for handoff, declaration, diagnosis, exact-target mutation, duplicate/hot triage, or upgrade recovery (`prd.md:50-101`).

The detail is earned. The Collection Obligation table assigns concrete policy to cron, systemd, Docker, PM2, and direct-process scopes (`prd.md:299-324`); the reconciliation model defines four orthogonal axes and lost-Heartbeat transitions (`prd.md:146-170`); and Safe-to-stop has reproducible `safe`, `unsafe`, and `unknown` rules (`prd.md:432-449`). The NFRs are specific to hostile Host data, partial truth, terminal restoration, local-state integrity, Lease clocks, compatibility, and concurrency rather than generic security/reliability prose (`prd.md:680-744`).

### Findings

No findings.

## Strategic coherence — adequate

The thesis is consistent from Vision through scope: `srvls` compares ephemeral-by-default Runtime Promises with fresh, explicitly scoped Host Observations and turns the delta into an evidence-backed morning handoff (`prd.md:18-28`, `prd.md:172-176`, `prd.md:356-358`, `prd.md:463-465`). That matches the landscape's identified whitespace—an evidence-backed comparison layer across authority boundaries rather than another manager or dashboard (`research-current-landscape.md:12-42`, `research-current-landscape.md:351-364`)—and every feature group names the journeys it realizes.

The Success Metrics trace directly to FR ranges, and the counter-metrics prevent optimizing anomaly count, apparent speed, or cleanup volume (`prd.md:660-678`). They are strong conformance gates, but they do not yet establish whether the product materially improves the operator's morning outcome; that keeps this dimension at adequate rather than strong.

### Findings

- **medium** Product success stops at conformance (§ 7, `prd.md:660-678`; `source-extract-live-evidence.md:47-57`; `reconcile-source-inputs.md:240-245`, `reconcile-source-inputs.md:376-381`) — SM-1 through SM-6 prove fixture correctness, compatibility, safe outcome reporting, and evidence reachability, but none measures reduced reconstruction effort, decision time, or unsafe action. The permitted evidence explicitly says no such target exists and must not be inferred from Host counts or current timeouts. *Fix:* Before beta evaluation, add one owner-approved operator-impact measure with a baseline, target, measurement window, and collection method; elicit the value rather than copying an implementation observation.

## Done-ness clarity — thin

All 43 FRs have at least one testable consequence, and the difficult contracts are particularly concrete: collection outcomes and obligations (`prd.md:299-324`), layered compatibility evidence (`prd.md:335-345`), Accepted Baseline behavior (`prd.md:451-461`), action identity and verification (`prd.md:553-587`), and rollback (`prd.md:602-618`). This is materially stronger than a feature list and gives story creation stable behavioral consequences.

The thin point is concentrated in non-functional acceptance. “Bounded” inspection, refresh, output, and retention are required, and NFR-16 requires documented defaults, but the PRD gives neither a product budget nor an explicit downstream closure owner for those values (`prd.md:326-333`, `prd.md:690-692`, `prd.md:722-724`, `prd.md:742-744`). The source evidence confirms that acceptable latency and outcome thresholds were never established (`source-extract-live-evidence.md:171-177`, `source-extract-live-evidence.md:214-223`, `source-extract-live-evidence.md:257-272`), so inventing numbers would be wrong; leaving the acceptance handoff implicit is the actual defect.

### Findings

- **medium** Bounds are promised but not bounded (§ 4.2 FR-15 and § 8 NFR-3/NFR-11/NFR-16, `prd.md:326-333`, `prd.md:690-692`, `prd.md:722-744`; `reconcile-source-inputs.md:376-383`) — Byte/line output caps, Collector deadlines, end-to-end refresh behavior, retention, Heartbeat grace, and action-verification timing have no acceptance budget or named downstream closure point. An implementation can choose materially different values and still claim textual conformance. *Fix:* Add a compact acceptance-budgets table with owner-approved defaults and limits, or explicitly assign each unresolved value to UX/architecture with an owner, required evidence, and a closure gate before implementation acceptance.

## Scope honesty — adequate

Scope is unusually explicit. The PRD identifies the primary and secondary users (`prd.md:30-48`), distinguishes current Python behavior from target contracts (`prd.md:10-16`), names product non-goals (`prd.md:620-629`), separates inherited constraints from core thesis (`prd.md:631-646`), and dispositions fleet, platform, Provider, grouping-override, and group-mutation omissions with revisit triggers (`prd.md:648-658`). It also narrows Runtime Promise semantics to runtime liveness rather than arbitrary business outcomes (`prd.md:121-128`).

Section 12 is carefully limited to “no phase-blocking product questions” rather than claiming that no downstream choices exist (`prd.md:790-792`), and the addendum enumerates those downstream choices (`addendum.md:57-63`). The dimension remains adequate because the two non-blocking measurement/budget decisions above are not named in Open Questions or given explicit closure owners; no additional finding is needed beyond the two medium findings already recorded.

### Findings

No additional findings.

## Downstream usability — strong

The PRD is built for clean source extraction. It provides a stable glossary and reconciliation vocabulary (`prd.md:103-170`), named protagonists in every journey (`prd.md:52-101`), globally numbered requirements, direct journey-to-feature statements, and explicit FR ranges in every Success Metric (`prd.md:172-618`, `prd.md:660-744`). The addendum maps every legacy FR to canonical requirements and clearly leaves legacy UX identifiers pending a future dedicated UX contract (`addendum.md:30-55`).

Mechanical verification found contiguous, unique definitions for UJ-1 through UJ-6, FR-1 through FR-43, and NFR-1 through NFR-16; every UJ/FR/NFR reference in `prd.md` and `addendum.md` resolves. Section 0 also gives downstream consumers a precise current-versus-target reading rule (`prd.md:10-16`).

### Findings

No findings.

## Shape fit — strong

This is a brownfield, chain-top contract for a single-operator internal tool with a secondary machine actor, meaningful terminal UX, compatibility-sensitive automation, and safety-critical Host mutation (`prd.md:10-16`, `prd.md:30-32`, `prd.md:540-618`). A capability-spec spine is therefore appropriate, while journeys still earn their place: they cover the morning handoff, Agent lifecycle, broken-intent diagnosis, exact-target removal, multi-label triage, and upgrade recovery rather than manufacturing extra personas (`prd.md:50-101`).

The document's length is supported by 43 distinct behavioral contracts, an explicit coverage policy, orthogonal reconciliation semantics, safe-action invariants, and a brownfield migration oracle. Technical mechanisms that do not belong in the product narrative are moved to the short addendum (`addendum.md:10-28`, `addendum.md:57-63`). The shape is rigorous because the PRD feeds UX, architecture, epics, stories, and readiness, not because a template demanded density.

### Findings

No findings.

## Mechanical notes

- **Glossary drift:** No material drift found. Capitalized domain nouns are defined in § 3; Provider-native health remains evidence, while `healthy` is explicitly a Promise Outcome (`prd.md:103-170`).
- **ID continuity and cross-references:** UJ-1–UJ-6, FR-1–FR-43, NFR-1–NFR-16, SM-1–SM-6, and SM-C1–SM-C3 are unique and contiguous within their schemes. All UJ/FR/NFR references resolve across the reviewed pair.
- **Assumptions Index roundtrip:** No inline `[ASSUMPTION]` tags appear, and § 13 states that no unresolved inline assumptions remain (`prd.md:794-796`). No index mismatch was found.
- **UJ protagonist naming:** Jarad is named in UJ-1 and UJ-3–UJ-6; Ava is named in UJ-2 (`prd.md:52-101`). No floating journey was found.
- **Required sections:** Vision, users/jobs, journeys, glossary, FRs, non-goals, MVP scope, Success Metrics with counter-metrics, NFRs, constraints, dependencies, risks, Open Questions, and Assumptions Index are present and appropriate to this chain-top brownfield PRD.
- **Stale evidence disposition:** The reconciliation artifact's PB-1 through PB-8 findings (`reconcile-source-inputs.md:359-370`) predate corresponding current-PRD corrections: Collection Obligations (`prd.md:309-324`), orthogonal state and lost-Heartbeat rules (`prd.md:146-170`), the liveness-only Promise boundary (`prd.md:121-128`), Accepted Baseline semantics (`prd.md:451-461`), the Safe-to-stop decision table (`prd.md:441-449`), owner-approved inherited scope (`prd.md:633-646`), the layered migration oracle (`prd.md:10-16`, `prd.md:335-345`), and future-tense UX handoff wording (`addendum.md:55`). None was recycled as a current defect.
- **Evidence availability:** No `project-context.md` exists in this worktree. No score or finding depends on it, and its absence was not treated as a PRD defect.
