---
title: Epic Product Traceability Review
project: srvls
reviewer: Doctor Von Code
review_date: 2026-07-17
target_commit: b959e2ada0f61d6928dc270a793280b0acd6217e
target_path: _bmad-output/planning-artifacts/epics.md
expected_sha256: 0189960e42776cf3f5fe86dcf3cc3344ce307d987877d9c5600277b43b1f1523
actual_sha256: 0189960e42776cf3f5fe86dcf3cc3344ce307d987877d9c5600277b43b1f1523
digest_gate: PASS
verdict: FAIL
findingCount: 8
completionStatus: complete
coverageCounts:
  functionalRequirements:
    total: 43
    strong: 43
    weak: 0
    missing: 0
  functionalAcceptanceConsequences:
    total: 97
    strong: 90
    weak: 7
    missing: 0
  nonFunctionalRequirements:
    total: 16
    strong: 16
    weak: 0
    missing: 0
  userJourneys:
    total: 6
    strong: 6
    weak: 0
    missing: 0
  canonicalUxContracts:
    total: 89
    strong: 86
    weak: 3
    missing: 0
  incorrectUxMappingEdges: 21
  epics: 7
  stories: 55
  numberedAcceptanceCriteria: 165
stepsCompleted:
  - document-discovery
  - prd-analysis
  - epic-coverage-validation
  - ux-alignment
  - epic-quality-review
  - final-assessment
canonical_inputs:
  - _bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md
  - _bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/addendum.md
  - _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md
  - _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/DESIGN.md
---

# Epic Product Traceability Review

**Date:** 2026-07-17  
**Project:** srvls  
**Review target:** canonical `epics.md` at commit `b959e2ada0f61d6928dc270a793280b0acd6217e`

## Document inventory and scope

The candidate plan is the exact committed `_bmad-output/planning-artifacts/epics.md` blob at `b959e2a`. Its SHA-256 matches the required settled digest. The assessment uses the final PRD, binding addendum, and both canonical UX spines listed in frontmatter. Supporting reviews, source extracts, memlogs, the retired pre-canonical epic artifact, architecture reviews, working-tree variants, and implementation files are excluded as normative inputs.

## Review method

1. Read the candidate from Git with `git show b959e2a:_bmad-output/planning-artifacts/epics.md`, hashed those exact bytes with SHA-256, and stopped the digest gate only after the expected and actual values matched.
2. Read the final PRD, binding addendum, EXPERIENCE spine, and DESIGN spine completely. Enumerated canonical IDs independently, rejected legacy aliases as authority, and checked for gaps and duplicates.
3. Expanded every range in the epic requirement mappings. For each FR, NFR, journey, and UX contract, inspected the mapped story's numbered Given/When/Then acceptance criteria for an observable implementation consequence. A requirement tag, implementation note, validation note, or `Out of Scope` statement alone did not count as strong AC coverage.
4. Split the 43 FRs into their 97 individually testable `Consequences` bullets and checked each consequence separately. This prevents a broad FR mapping from concealing an omitted acceptance consequence.
5. Compared all story-to-UX edges against the final UX contract definitions, not merely against ID presence. Counted an ID as weak when the AC proves only a subset of its mandatory behavior and counted a mapping edge as incorrect when the story AC describes a different canonical state.
6. Reviewed the addendum's named technical direction, mandatory planning corrections, architecture-decision seams, and the PRD's Plane/Git/Telemetry ownership boundary. Checked story sizing, user-value orientation, dependency direction, and Given/When/Then structure.
7. Re-ran identifier/count scripts, digest and Git-scope checks, and Markdown validation after completing this report. Evidence references below use `Story x.y ACn` to identify numbered acceptance criteria in the committed candidate.

### Digest evidence

```text
$ git rev-parse b959e2a
b959e2ada0f61d6928dc270a793280b0acd6217e
$ git show b959e2a:_bmad-output/planning-artifacts/epics.md | sha256sum
0189960e42776cf3f5fe86dcf3cc3344ce307d987877d9c5600277b43b1f1523  -
```

**Digest gate: PASS.** Review continued because the settled candidate matched exactly.

## Canonical product requirement inventory

The PRD contains a gapless, duplicate-free inventory of **43 Functional Requirements**, **16 Non-Functional Requirements**, and **6 User Journeys**.

### Functional Requirements

| ID | Canonical title |
| --- | --- |
| FR-1 | Declare a Runtime Promise |
| FR-2 | Preserve declaration provenance |
| FR-3 | Make Runtime Promises ephemeral by default |
| FR-4 | Renew ownership with Heartbeats |
| FR-5 | Release, complete, or revoke intent |
| FR-6 | Declare explicit persistent intent |
| FR-7 | Expose deterministic Agent contracts |
| FR-8 | Collect cron work |
| FR-9 | Collect systemd work |
| FR-10 | Collect Docker work |
| FR-11 | Collect PM2 work |
| FR-12 | Collect direct Host processes |
| FR-13 | Normalize Observations |
| FR-14 | Report collection completeness |
| FR-15 | Inspect bounded Provider detail |
| FR-16 | Preserve compatibility surfaces |
| FR-17 | Support strict collection policy |
| FR-18 | Correlate Runtime Promises and Observations |
| FR-19 | Identify healthy intent |
| FR-20 | Identify broken intent |
| FR-21 | Identify orphaned Observations |
| FR-22 | Identify duplicate Observations |
| FR-23 | Identify stale Runtimes |
| FR-24 | Identify hot Runtimes |
| FR-25 | Identify unmanaged and abandoned Runtimes |
| FR-26 | Explain findings and Safe-to-stop Assessment |
| FR-27 | Detect change through bounded Snapshots |
| FR-28 | Produce the Brief |
| FR-29 | Organize attention and Stack context |
| FR-30 | Select interactive or non-interactive presentation |
| FR-31 | Navigate and refine the TUI |
| FR-32 | Inspect intent and truth together |
| FR-33 | Communicate without color or Unicode dependence |
| FR-34 | Represent application and terminal states explicitly |
| FR-35 | Provide a discoverable Action Menu |
| FR-36 | Plan supported lifecycle actions |
| FR-37 | Revalidate identity before mutation |
| FR-38 | Confirm destructive and uncertain actions |
| FR-39 | Isolate asynchronous operations |
| FR-40 | Verify and report action outcomes |
| FR-41 | Keep groups read-only and privilege scoped |
| FR-42 | Build and install a verifiable release |
| FR-43 | Upgrade, validate automation, and roll back |

### Non-Functional Requirements

| ID | Canonical title |
| --- | --- |
| NFR-1 | Deterministic domain outcomes |
| NFR-2 | Honest partial truth |
| NFR-3 | Bounded refresh behavior |
| NFR-4 | Host command safety |
| NFR-5 | Least privilege |
| NFR-6 | Terminal restoration |
| NFR-7 | Clean machine interfaces |
| NFR-8 | Accessible terminal communication |
| NFR-9 | Atomic and durable local state |
| NFR-10 | Defensible Lease time semantics |
| NFR-11 | Local data minimization |
| NFR-12 | Concurrency correctness |
| NFR-13 | Testability without Host mutation |
| NFR-14 | Brownfield compatibility |
| NFR-15 | Supported release baseline |
| NFR-16 | Configurable policy without hidden defaults |

### User Journeys

| ID | Canonical title |
| --- | --- |
| UJ-1 | Jarad receives the morning handoff |
| UJ-2 | An Agent declares and renews an overnight runtime |
| UJ-3 | Jarad diagnoses a broken promise |
| UJ-4 | Jarad removes an abandoned runtime safely |
| UJ-5 | Jarad triages duplicate and hot runtime findings |
| UJ-6 | Jarad upgrades and recovers |

### Binding addendum constraints and planning seams

The addendum contributes six approved technical-direction constraints, four mandatory planning corrections, and five architecture-decision seams:

- one initial Rust binary and one-tool operator experience;
- hexagonal domain/application isolation from Host commands, terminal rendering, parsing, and serialization;
- an Elm-style ratatui model/message/update/view/effect shell;
- explicit Strategy, Adapter, and Command seams using composition;
- a layered migration oracle with behavior inventory, frozen fixtures/goldens, live-Host smoke, named-consumer E2E checks, and a compatibility ledger;
- preserved deterministic table, JSON, Prometheus, Markdown, inspection, executable-name, and explicit-action behavior;
- bootstrap/module/lockfile/harness/format/lint/locked-test/MSRV 1.88/current-stable CI gates before Provider implementation;
- separation of total bounded subprocess execution from concurrent Provider orchestration and outcome policy;
- an explicit TUI start interaction or consistent non-TUI scoping;
- separation of mutation initiation/confirmation from asynchronous execution, race handling, verification, and outcome rendering;
- durable state formats and locations;
- Agent-facing declaration/heartbeat/renewal/release/query contracts;
- Lease-clock behavior across Agent exit, restart, suspend, and clock discontinuity;
- evidence-weighted cross-Provider identity/correlation rules; and
- retention that enables morning change detection without becoming a general Telemetry store.

The PRD also establishes the external-system boundary: Plane is authoritative for intended work, Git for code changes, and Telemetry for events/measurements. `srvls` may retain optional opaque references only; none of those systems may determine Runtime health.

## Functional Requirement to story-AC coverage

The epic-level coverage table claims all 43 FRs. The following matrix checks the claim against numbered story acceptance criteria rather than accepting requirement tags alone.

| Requirement | Concrete story-AC evidence | Result |
| --- | --- | --- |
| FR-1 | Story 2.1 AC1–AC2; Story 2.5 AC1 | Covered |
| FR-2 | Story 2.1 AC1/AC3; Story 2.4 AC2–AC3; Story 1.3 AC2 | Covered |
| FR-3 | Story 2.2 AC1 | Covered |
| FR-4 | Story 2.3 AC1–AC3 | Covered |
| FR-5 | Story 2.4 AC1–AC3; Story 4.5 AC2 | Covered |
| FR-6 | Story 2.2 AC2; Story 2.4 AC1/AC3 | Covered |
| FR-7 | Story 2.5 AC1–AC3 | Covered |
| FR-8 | Story 3.3 AC1–AC3 | Covered |
| FR-9 | Story 3.4 AC1–AC3 | Covered |
| FR-10 | Story 3.5 AC1–AC3 | Covered |
| FR-11 | Story 3.6 AC1–AC3 | Covered |
| FR-12 | Story 3.7 AC1–AC3 | Covered |
| FR-13 | Story 3.8 AC1; Story 1.3 AC1–AC3 | Covered |
| FR-14 | Story 3.1 AC1; Stories 3.3–3.7 AC2/AC3; Story 3.8 AC2 | Covered |
| FR-15 | Story 3.9 AC1–AC3; Story 5.4 AC2–AC3 | Covered |
| FR-16 | Story 1.2 AC1–AC3; Story 2.5 AC1; Story 7.4 AC1–AC3 | Covered |
| FR-17 | Story 3.8 AC2; Story 2.5 AC2 | Covered |
| FR-18 | Story 4.1 AC1–AC3 | Covered |
| FR-19 | Story 4.2 AC2–AC3; Story 4.4 AC2 | Covered |
| FR-20 | Story 4.2 AC2–AC3 | Covered |
| FR-21 | Story 4.3 AC1/AC3 | Covered |
| FR-22 | Story 4.3 AC2–AC3 | Covered |
| FR-23 | Story 4.4 AC1/AC3 | Covered |
| FR-24 | Story 4.4 AC2–AC3 | Covered |
| FR-25 | Story 4.5 AC1–AC3; Story 4.2 AC1 | Covered |
| FR-26 | Story 4.6 AC1–AC3; Story 5.4 AC1–AC2 | Covered |
| FR-27 | Story 4.7 AC1–AC3; Story 4.8 AC1 | Covered |
| FR-28 | Story 4.8 AC1–AC3 | Covered |
| FR-29 | Story 4.9 AC1–AC2; Story 5.2 AC1/AC3; Story 5.3 AC2 | Covered |
| FR-30 | Story 5.1 AC1–AC2 | Covered |
| FR-31 | Story 5.3 AC1–AC3; Story 5.5 AC1–AC2 | Covered |
| FR-32 | Story 5.4 AC1–AC2; Story 4.8 AC2 | Covered |
| FR-33 | Story 5.6 AC1–AC2; Story 5.2 AC1 | Covered |
| FR-34 | Story 5.2 AC2; Story 5.5 AC1–AC2; Story 5.7 AC2; Story 6.8 AC1–AC2 | Covered |
| FR-35 | Story 6.1 AC1–AC3; Story 6.8 AC1 | Covered |
| FR-36 | Story 6.1 AC1–AC3; Story 6.5 AC1–AC3 | Covered |
| FR-37 | Story 6.3 AC1–AC3; Story 6.7 AC1–AC3 | Covered |
| FR-38 | Story 6.2 AC2–AC3; Story 6.3 AC2–AC3 | Covered |
| FR-39 | Story 6.4 AC1–AC3; Story 6.6 AC1–AC3 | Covered |
| FR-40 | Story 6.7 AC1–AC3; Story 6.8 AC1 | Covered |
| FR-41 | Story 6.1 AC3; Story 6.3 AC3; Story 5.2 AC3 | Covered |
| FR-42 | Story 7.1 AC1–AC3; Story 7.3 AC2; Story 7.7 AC1–AC2 | Covered |
| FR-43 | Story 7.2 AC1–AC3; Stories 7.3–7.8 AC1–AC3; Story 7.9 AC1–AC3 | Covered |

### FR coverage statistics

- Canonical PRD FRs: **43**
- FRs claimed in the epic coverage map: **43**
- FRs with concrete numbered story AC evidence: **43**
- Missing FRs: **0**
- Extra/noncanonical FRs used as authority: **0**
- FR-level coverage: **100%**

### Exhaustive FR acceptance-consequence audit

The PRD's 43 FRs contain **97** separate acceptance consequences. The table below accounts for every one; `Strong` means the consequence itself is asserted by a numbered story AC, not merely named in a mapping or implementation boundary.

| FR | Consequences | Strong | Weak | Missing | Exception or principal evidence |
| --- | ---: | ---: | ---: | ---: | --- |
| FR-1 | 2 | 1 | 1 | 0 | Story 2.1 AC2 strongly covers deterministic field errors/no partial record; success returns Lease/ID but no AC requires both human and machine forms. |
| FR-2 | 2 | 2 | 0 | 0 | Story 2.1 AC1/AC3; Story 2.4 AC2–AC3 |
| FR-3 | 2 | 2 | 0 | 0 | Story 2.2 AC1 |
| FR-4 | 2 | 2 | 0 | 0 | Story 2.3 AC1–AC3 |
| FR-5 | 3 | 3 | 0 | 0 | Story 2.4 AC1–AC3 |
| FR-6 | 2 | 2 | 0 | 0 | Story 2.2 AC2; Story 2.4 AC1/AC3 |
| FR-7 | 2 | 2 | 0 | 0 | Story 2.5 AC1–AC3 |
| FR-8 | 2 | 2 | 0 | 0 | Story 3.3 AC1–AC3 |
| FR-9 | 2 | 2 | 0 | 0 | Story 3.4 AC1–AC3 |
| FR-10 | 2 | 2 | 0 | 0 | Story 3.5 AC1–AC3 |
| FR-11 | 2 | 2 | 0 | 0 | Story 3.6 AC1–AC3 |
| FR-12 | 2 | 2 | 0 | 0 | Story 3.7 AC1–AC3 |
| FR-13 | 2 | 2 | 0 | 0 | Story 3.8 AC1; Story 1.3 AC1–AC3 |
| FR-14 | 3 | 2 | 1 | 0 | Story 3.1 AC1 and Stories 3.3–3.8 cover outcomes/absence gates; no AC asserts the full per-scope default and Promise-promotion obligation table. |
| FR-15 | 2 | 2 | 0 | 0 | Story 3.9 AC1–AC3; Story 5.4 AC2–AC3 |
| FR-16 | 5 | 3 | 2 | 0 | Story 1.2 covers frozen/live/consumer layers and deviation governance; no AC requires a checked-in source-and-test behavior inventory or additive/versioned compatibility for new fields. |
| FR-17 | 2 | 2 | 0 | 0 | Story 3.8 AC2; Story 2.5 AC2 |
| FR-18 | 2 | 2 | 0 | 0 | Story 4.1 AC1–AC3 |
| FR-19 | 2 | 2 | 0 | 0 | Story 4.2 AC2–AC3; Story 4.4 AC2 |
| FR-20 | 2 | 2 | 0 | 0 | Story 4.2 AC2–AC3 |
| FR-21 | 2 | 2 | 0 | 0 | Story 4.3 AC1/AC3 |
| FR-22 | 2 | 2 | 0 | 0 | Story 4.3 AC2–AC3 |
| FR-23 | 2 | 2 | 0 | 0 | Story 4.4 AC1/AC3 |
| FR-24 | 2 | 2 | 0 | 0 | Story 4.4 AC2–AC3 |
| FR-25 | 3 | 3 | 0 | 0 | Story 4.5 AC1–AC3; Story 4.2 AC1 |
| FR-26 | 2 | 1 | 1 | 0 | Story 4.6 AC1–AC3 strongly covers conservative evidence/reasons; no AC requires recalculation after refresh and again immediately before mutation. |
| FR-27 | 5 | 4 | 1 | 0 | Story 4.7 AC1–AC3 covers storage, exact-ID acceptance, eligibility, audit, incompatibility, and override; the canonical TUI/non-interactive interaction consequences are only partial. |
| FR-28 | 3 | 3 | 0 | 0 | Story 4.8 AC1–AC3 |
| FR-29 | 2 | 2 | 0 | 0 | Story 4.9 AC1–AC2; Story 5.2 AC1/AC3 |
| FR-30 | 2 | 2 | 0 | 0 | Story 5.1 AC1–AC2 |
| FR-31 | 2 | 2 | 0 | 0 | Story 5.3 AC1–AC3; Story 5.5 AC1–AC2 |
| FR-32 | 2 | 1 | 1 | 0 | Story 5.4 AC1 covers independent unmatched inspection; AC2 forbids fetch but does not require named references to render only as references and never influence truth. |
| FR-33 | 2 | 2 | 0 | 0 | Story 5.6 AC1–AC2; Story 5.2 AC1 |
| FR-34 | 2 | 2 | 0 | 0 | Story 5.2 AC2; Story 5.5 AC1–AC2; Story 5.7 AC2; Story 6.8 AC1–AC2 |
| FR-35 | 2 | 2 | 0 | 0 | Story 6.1 AC1–AC3; Story 6.8 AC1 |
| FR-36 | 2 | 2 | 0 | 0 | Story 6.1 AC1–AC3; Story 6.5 AC1–AC3 |
| FR-37 | 2 | 2 | 0 | 0 | Story 6.3 AC1–AC3; Story 6.7 AC1–AC3 |
| FR-38 | 2 | 2 | 0 | 0 | Story 6.2 AC2–AC3; Story 6.3 AC2–AC3 |
| FR-39 | 2 | 2 | 0 | 0 | Story 6.4 AC1–AC3; Story 6.6 AC1–AC3 |
| FR-40 | 3 | 3 | 0 | 0 | Story 6.7 AC1–AC3; Story 6.8 AC1 |
| FR-41 | 2 | 2 | 0 | 0 | Story 6.1 AC3; Story 6.3 AC3; Story 5.2 AC3 |
| FR-42 | 2 | 2 | 0 | 0 | Story 7.1 AC1–AC3; Story 7.3 AC2; Story 7.7 AC1–AC2 |
| FR-43 | 2 | 2 | 0 | 0 | Story 7.2 AC1–AC3; Stories 7.3–7.9 |
| **Total** | **97** | **90** | **7** | **0** | **All consequences accounted for.** |

#### F-REQ-1 — Seven binding FR consequences are not concrete story acceptance contracts

The seven weak cells above are individually binding PRD consequences, not optional elaboration: FR-1's human-and-machine success response; FR-14's per-scope default/promotion obligation table; FR-16's checked-in source/test behavior inventory and additive/versioned new fields; FR-26's post-refresh and pre-mutation safety recalculation; FR-27's canonical baseline interaction; and FR-32's display/reference/truth rule. Implementation boundaries or validation prose mention parts of several, but the review standard requires numbered AC coverage. These seven omissions make the requirement-consequence audit fail even though every FR has some concrete AC evidence.

## Non-Functional Requirement coverage

| Requirement | Concrete story-AC evidence | Result |
| --- | --- | --- |
| NFR-1 | Story 1.3 AC1; Story 4.1 AC3; Story 4.2 AC1–AC3 | Strong |
| NFR-2 | Story 3.8 AC2; Story 4.2 AC2; Story 6.7 AC2 | Strong |
| NFR-3 | Story 1.8 AC1; Story 3.1 AC2–AC3; Story 3.2 AC3 | Strong |
| NFR-4 | Story 1.8 AC1; Story 3.8 AC3; Story 6.5 AC1/AC3 | Strong |
| NFR-5 | Story 1.8 AC2; Story 6.3 AC3 | Strong |
| NFR-6 | Story 5.1 AC3; Story 6.8 AC2 | Strong |
| NFR-7 | Story 2.5 AC1–AC2; Story 5.1 AC2; Story 7.9 AC2 | Strong |
| NFR-8 | Story 5.2 AC1–AC3; Story 5.6 AC1–AC3; Story 6.8 AC1 | Strong |
| NFR-9 | Story 1.5 AC1–AC3; Story 4.7 AC1–AC3; Story 6.4 AC1–AC3 | Strong |
| NFR-10 | Story 2.2 AC1/AC3; Story 2.3 AC2 | Strong |
| NFR-11 | Story 1.3 AC2; Story 1.5 AC1/AC3; Story 1.7 AC1–AC3 | Strong |
| NFR-12 | Story 1.6 AC2–AC3; Story 3.1 AC3; Story 6.4 AC1–AC3; Story 6.7 AC1–AC3 | Strong |
| NFR-13 | Story 1.8 AC3; Story 5.7 AC2; Story 6.8 AC3; Story 7.9 AC1 | Strong |
| NFR-14 | Story 1.2 AC1–AC3; Stories 7.4 and 7.7; Story 7.9 AC1–AC2 | Strong |
| NFR-15 | Story 1.1 AC1; Story 7.1 AC1–AC3; Stories 7.8–7.9 | Strong |
| NFR-16 | Story 1.4 AC1–AC3; Story 5.7 AC3; Story 6.8 AC3 | Strong |

**NFR result:** **16/16 strong**, 0 weak, 0 missing. This does not erase the more specific FR consequence and addendum-seam findings.

## User Journey coverage

| Journey | End-to-end story-AC evidence | Result |
| --- | --- | --- |
| UJ-1 | Story 4.8 AC1–AC3 produces the complete deterministic morning Brief; Stories 5.2 and 5.6 preserve interactive/accessibility presentation. | Strong |
| UJ-2 | Story 2.1 AC1–AC3 declares intent; Stories 2.2–2.4 enforce Lease/Heartbeat/release; Story 2.5 AC3 proves the Agent workflow. | Strong |
| UJ-3 | Story 4.2 AC2–AC3 classifies broken intent; Story 5.4 inspects evidence; Story 6.1 AC2–AC3 and Stories 6.3/6.7 keep action diagnosis safe. | Strong |
| UJ-4 | Stories 4.5–4.6 classify abandoned work and safety; Stories 6.2–6.3/6.7–6.8 confirm, revalidate, execute, and report exact-target removal. | Strong |
| UJ-5 | Stories 4.3–4.4 classify duplicate/hot findings; Stories 5.2–5.4 make them triageable; Stories 6.1 and 6.8 preserve individual-action scope and outcome. | Strong |
| UJ-6 | Stories 7.1–7.8 build, install, migrate, validate automation, and roll back; Story 7.9 AC2–AC3 closes full upgrade/recovery evidence. | Strong |

**Journey result:** **6/6 strong**, 0 weak, 0 missing.

## UX contract alignment and the 89-versus-83 count

The two final UX spines define **88 unique `UX-*` IDs**, not 83:

| Family | IDs | Count |
| --- | --- | ---: |
| Foundation | UX-FND-1 through UX-FND-6 | 6 |
| Information architecture | UX-IA-1 through UX-IA-12 | 12 |
| Voice and tone | UX-VT-1 through UX-VT-4 | 4 |
| Components | UX-CP-1 through UX-CP-16 | 16 |
| States | UX-ST-1 through UX-ST-20 | 20 |
| Interaction primitives | UX-IP-1 through UX-IP-12 | 12 |
| Accessibility | UX-A11Y-1 through UX-A11Y-5 | 5 |
| Responsive/platform | UX-RP-1 through UX-RP-6 | 6 |
| Operational budgets | UX-BUD-1 through UX-BUD-7 | 7 |
| **`UX-*` subtotal** |  | **88** |
| Screen-reader acceptance scenario | SR-A11Y-1 | 1 |
| **Canonical UX acceptance total** |  | **89** |

The reported **83** is reproducible only as the subtotal that omits all five `UX-A11Y-*` contracts: `88 - 5 = 83`. Adding those five and the separately prefixed `SR-A11Y-1` yields the mission total: `83 + 5 + 1 = 89`. Thus the mission's 89 total is correct, while the characterization of 83 as all discoverable `UX-*` IDs is not.

All 89 canonical IDs occur in at least one story `Requirement Mapping`. Independent AC review finds 86 strong mappings, three weak baseline-interaction mappings, and zero wholly unmapped IDs. The unnumbered DESIGN visual contract is exercised by Stories 5.2, 5.6, and 5.7 across responsive layout, text-first/no-style parity, hostile-text handling, component/state matrices, and deterministic terminal goldens.

### UX family coverage summary

| Family | Strong | Weak | Missing | Principal numbered AC evidence |
| --- | ---: | ---: | ---: | --- |
| UX-FND | 6 | 0 | 0 | Stories 1.1–1.3, 3.8, 4.1–4.5, 5.1–5.2, 5.6, 6.3 |
| UX-IA | 11 | 1 | 0 | Stories 3.9, 4.7–4.9, 5.1–5.4, 5.7, 6.1, 7.9 |
| UX-VT | 4 | 0 | 0 | Stories 1.3–1.5, 2.4–2.5, 4.4, 4.6, 5.6, 6.7, 7.9 |
| UX-CP | 15 | 1 | 0 | Stories 3.8–3.9, 4.3–4.9, 5.2–5.7, 6.1–6.8, 7.1–7.9 |
| UX-ST | 20 | 0 | 0 | Stories 4.7, 5.3, 5.5–5.7, 6.3, 6.6–6.8 |
| UX-IP | 11 | 1 | 0 | Stories 1.4, 2.5, 4.7–4.8, 5.1, 5.3, 6.1–6.8, 7.1–7.9 |
| UX-A11Y | 5 | 0 | 0 | Stories 1.3, 4.8, 5.3–5.6, 6.8, 7.9 |
| UX-RP | 6 | 0 | 0 | Stories 5.1–5.2, 5.6–5.7, 7.9 |
| UX-BUD | 7 | 0 | 0 | Stories 5.5, 5.7, 6.6–6.8 |
| SR-A11Y | 1 | 0 | 0 | Stories 4.8 AC3, 5.6 AC3, 6.8 AC1 |
| **Total** | **86** | **3** | **0** |  |

### UX alignment findings

#### F-UX-1 — Baseline TUI contracts are only partially asserted

`UX-IA-7`, `UX-CP-12`, and `UX-IP-6` map only to Story 4.7. Story 4.7 AC2–AC3 prove exact Snapshot acceptance, pointer-only mutation, audit identity/time/timezone, ineligibility reasons, and override reason/acknowledgement. They do not assert every canonical interaction consequence: `b` entry from the Brief, Cancel focus and Esc cancellation, the exact typed `override` token, or recomputation and display of the resulting Evidence Window after success. No Epic 5 AC adopts the baseline dialog. This is weak, not absent, coverage.

#### F-UX-2 — Canonical action-state IDs are attached to stories whose ACs describe different states

The following mapping edges do not match the final EXPERIENCE state definitions. Later stories provide real coverage for the affected IDs, so these are incorrect traceability edges rather than missing product behavior.

| Story mapping edge | Canonical state | Why the edge is incorrect or weak | Actual concrete AC owner |
| --- | --- | --- | --- |
| Story 1.5 → UX-ST-18 | invalid-configuration | AC3 covers storage permissions/schema/corruption failure, not field/source/type/range configuration validation. | Story 1.4 AC1–AC3; Story 5.7 AC1 |
| Story 1.6 → UX-ST-12 | timed-out Action Outcome | ACs cover repository commit/conflict/idempotency and no lifecycle timeout. | Story 6.7 AC2; Story 6.8 AC1 |
| Story 1.7 → UX-ST-5 | unavailable-Provider | Retention/capacity ACs do not cover an unavailable Provider. | Stories 3.3–3.8 failure ACs; Story 5.5 AC2 |
| Story 1.7 → UX-ST-12 | timed-out Action Outcome | Retention recovery has no action timeout or outcome. | Story 6.7 AC2; Story 6.8 AC1 |
| Story 1.7 → UX-ST-16 | baseline-unavailable | Pin survival is a prerequisite, but no AC renders or resolves baseline unavailability. | Story 4.7 AC3; Story 5.7 AC2 |
| Story 1.8 → UX-ST-10 | executed-unverified | CommandRunner explicitly excludes action-outcome policy. | Story 6.7 AC2; Story 6.8 AC1 |
| Stories 2.2 and 2.3 → UX-ST-4 | collection partial-failure | Lease/Heartbeat validation outcomes are not Collector partial-failure. | Story 3.8 AC2; Story 5.5 AC2 |
| Stories 3.5, 3.6, and 3.7 → UX-ST-10 | executed-unverified | Collector identity races occur before any lifecycle action and each story excludes mutation. | Story 6.7 AC2; Story 6.8 AC1 |
| Stories 6.1 and 6.2 → UX-ST-8 | pending-action | Menu preview and confirmation occur before submission; their ACs require no operation/side effect yet. | Story 6.6 AC1–AC3; Story 6.8 AC1 |
| Story 6.2 → UX-ST-9 | verified | Confirmation explicitly excludes execution and outcome verification. | Story 6.7 AC1; Story 6.8 AC1 |
| Story 6.3 → UX-ST-10 | executed-unverified | Preflight ACs cover launch authorization or no-launch stale-identity refusal, not post-execution uncertainty. | Story 6.7 AC2; Story 6.8 AC1 |
| Story 6.4 → UX-ST-11 and UX-ST-12 | refused and timed-out outcomes | Operation admission owns durable handoffs but explicitly excludes verification/outcome decisions and TUI notification rendering. | Story 6.7 AC2–AC3; Story 6.8 AC1 |
| Story 6.5 → UX-ST-11 | refused outcome | AC3 explicitly says its typed executor result does not claim the terminal Action Outcome. | Story 6.7 AC3; Story 6.8 AC1 |
| Story 6.6 → UX-ST-11 and UX-ST-12 | refused and timed-out outcomes | The story says terminal truth remains coordinator-owned and excludes choosing the final outcome. | Story 6.7 AC2–AC3; Story 6.8 AC1 |
| Story 7.3 → UX-ST-18 | invalid-configuration | Release preimage/migration staging ACs do not exercise configuration field/source/type/range recovery. | Story 1.4 AC1–AC3; Story 5.7 AC1 |

#### F-UX-3 — Plane/Git/Telemetry ownership is not an affirmative story acceptance contract

The PRD makes Plane authoritative for intended work, Git authoritative for code changes, Telemetry authoritative for events/measurements, and forbids their availability from determining Runtime health. The epic inventory repeats optional opaque references, and several `Out of Scope` clauses prohibit fetching them. Story 5.4 AC2 proves only that an opaque-reference fetch does not occur. No numbered AC asserts the three named ownership boundaries, display-as-reference-only behavior, and health independence together. The boundary is therefore weakly mapped and vulnerable to implementation drift.

## Epic and story quality review

### Epic outcome and dependency matrix

| Epic | User-value assessment | Dependency assessment |
| --- | --- | --- |
| 1 — Trustworthy Rust and Durable Storage Foundation | Technical enabling milestone; no Operator receives the target Brief, lifecycle, discovery, action, or release outcome from this epic alone. | No forward dependency is declared, but later-domain contracts are pre-seeded. |
| 2 — Runtime Promise Lifecycle | Complete Agent/Operator declare, renew, query, persist, and close outcome without discovery. | Depends only on Epic 1. |
| 3 — Five-Provider Discovery | Complete scoped Host-observation and inspection outcome even without Promises. | Depends only on Epics 1–2. |
| 4 — Reconciliation, Baseline, and Morning Brief | Complete deterministic linear/machine Brief and baseline value before TUI/actions. | Depends only on Epics 2–3. |
| 5 — Interactive TUI | Complete read-only interactive Brief/Explorer value. | Depends only on Epic 4 and earlier compatibility contracts. |
| 6 — Safe Exact-Target Actions | Complete exact-target plan/confirm/execute/verify journey. | Depends only on Epics 3–5. |
| 7 — Release and Recovery | Complete verifiable install/upgrade/recovery/rollback value. | Depends only on completed Epics 1–6. |

Mechanical dependency review found **0 explicit forward story references**, **0 dependency cycles**, and monotonically earlier within-epic dependencies. All **55 stories** contain exactly **3 numbered Given/When/Then ACs**, for **165/165 structurally valid ACs**. The semantic exceptions are the traceability and sizing findings below.

### Quality findings

#### F-QUAL-1 — Epic 1 is a technical horizontal milestone

Epic 1 is framed around crate structure, encodings, policy compilation, SQLite, repositories, retention, command execution, and gates. Its content is required by the addendum and materially reduces brownfield risk, but it does not satisfy the implementation-readiness skill's user-value test: it delivers no independently usable target-state product outcome. Stories 1.1–1.8 are primarily maintainer/platform capabilities. Treating this as a formal enabling epic would make the exception explicit; presenting it as a normal user-value epic overstates independence.

#### F-QUAL-2 — Four stories are multi-subsystem, epic-sized work packages

| Story | Bundled scope that prevents ordinary story sizing |
| --- | --- |
| 1.2 | Every inherited output/action surface, byte and semantic corpus, live Host smoke, deployed consumers, and deviation governance |
| 1.8 | Typed process execution, environment/cwd/descriptors, privilege, capture/deadline/TERM/KILL/reaping, fake backend, aggregate architecture gate, and constrained-Host budget evidence |
| 3.1 | Atomic plan admission, seven frozen cuts, schedule compilation, LPT/setup/epoch semantics, generation ownership, latest-wins cancellation, and race policy |
| 7.9 | The complete artifact, ABI, lock, FD3/FD4, storage/action handoff, migration, consumer, causality, owner-loss, KnownGood, FirstInstall, rollback, accessibility, signal, and evidence-bundle gate |

Each has testable ACs, but each AC closes a matrix containing several independently fail-prone capabilities. These are implementation work packages or aggregate verification epics rather than conventionally completable stories.

#### F-QUAL-3 — Later-domain contracts are pre-seeded without explicit dependency ownership

- Story 1.6 introduces immutable Snapshot inputs and maps FR-39 before Snapshot and operation use cases exist.
- Story 1.7 implements baseline, operation, and release pins and maps FR-43 before Epics 4, 6, and 7 own those records.
- Story 3.1 freezes AcceptedBaselineCut, OperationCut, ResourceHistoryCut, and PriorCurrentCut while declaring dependencies only on Epics 1–2.

The architecture may intentionally freeze these cross-cutting grammars early, but the story dependency graph does not distinguish “type/empty-cut contract available” from “later aggregate implemented.” That creates hidden forward coupling and encourages creation of later-domain persistence/schema before the owning story needs it.
