---
title: Epic Product Traceability Review R2
project: srvls
reviewer: Doctor Von Code
review_date: 2026-07-17
review_type: independent-batch-2-product-traceability
target_commit: 8ebdc20e2ea08f5bb7529dad1bc1b2d90c50a705
target_path: _bmad-output/planning-artifacts/epics.md
expected_sha256: b5368de55ada106282a2b623879feef5ceffea1a4dd0afd54870326aebb1ee27
actual_sha256: b5368de55ada106282a2b623879feef5ceffea1a4dd0afd54870326aebb1ee27
digest_gate: PASS
verdict: FAIL
findingCount: 13
completionStatus: complete
coverageCounts:
  functionalRequirements:
    total: 43
    represented: 43
  functionalAcceptanceConsequences:
    total: 97
    strong: 58
    weak: 32
    missing: 7
  nonFunctionalRequirements:
    total: 16
    strong: 2
    weak: 14
    missing: 0
  userJourneys:
    total: 6
    strong: 1
    weak: 5
    missing: 0
  uxRequirements:
    total: 88
    strong: 47
    weak: 41
    missing: 0
  screenReaderScenarios:
    total: 1
    strong: 1
    weak: 0
    missing: 0
  addendumConstraints:
    total: 15
    strong: 11
    weak: 4
    missing: 0
  registryRequirementIds: 213
  registryStories: 73
  registryAcceptanceCriteria: 146
  registryAd11Rows: 68
  registryMechanicalErrors: 0
---

## Verdict

**FAIL — 13 findings.**

The settled artifact passes the commit and digest gate, source-inventory counts,
structural parser, reciprocal JSON registry, Plane/Git/Telemetry boundary, and
the exact expected planning-quarantine override. It fails semantic product
traceability. Requirement tags are complete, but many registered owners do not
turn the complete source consequence into a numbered acceptance contract.

PASS is permitted only with zero findings. The 13 findings in this report are
therefore gate-blocking for promotion of `epics.md` from remediated draft to
assignable implementation authority.

## Scope and authority

The reviewed object is the exact committed `epics.md` blob at
`8ebdc20e2ea08f5bb7529dad1bc1b2d90c50a705`. The authoritative product inputs
were read completely:

- `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md`
- `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/addendum.md`
- `_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/DESIGN.md`
- `_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md`

The final architecture spine was used only to resolve named addendum seams,
registered `AD-*` references, the Plane/Git/Telemetry boundary, and the expected
planning-quarantine override. It was not used to fill a missing story
acceptance consequence. The Batch 1 ledger and all three Batch 1 reviews were
used only to verify claimed dispositions.

No implementation file or `epics.md` content was changed by this review.

## Method

1. Resolved `8ebdc20` to its full commit and hashed the exact Git blob before
   reviewing content.
2. Independently enumerated 43 `FR-*`, 16 `NFR-*`, six `UJ-*`, 88 `UX-*`, and
   `SR-A11Y-1` from the final source artifacts.
3. Split the 43 FRs into all 97 explicit PRD `Consequences` bullets and audited
   each consequence against numbered story GWT acceptance criteria.
4. Parsed the normative JSON registry and compared source inventory, story
   headings, story `Requirement Mapping` fields, `coverageByStory`, and
   `requirementCoverage` in both directions.
5. Treated a consequence as **Strong** only when a registered story owner has a
   numbered AC that asserts the observable consequence or an exact named
   source contract. A mapping tag, story title, implementation boundary,
   validation-path name, generic “capability is exercised” clause, or unrelated
   story did not make the edge strong.
6. Treated a consequence as **Weak** when it is only partial, indirect, or
   present outside the reciprocal owner edge. Treated it as **Missing** when no
   registered owner AC establishes the consequence.
7. Checked all 15 addendum bullets, the external-system boundary, all 55 Batch 1
   disposition rows, and the prior product review's disposition accounting.
8. Ran structural, digest, compatibility, quarantine, shell, whitespace, and
   Markdown checks after writing the report.

## Settled-object and digest evidence

```text
$ git rev-parse 8ebdc20
8ebdc20e2ea08f5bb7529dad1bc1b2d90c50a705

$ git show 8ebdc20:_bmad-output/planning-artifacts/epics.md | sha256sum
b5368de55ada106282a2b623879feef5ceffea1a4dd0afd54870326aebb1ee27  -
```

**Digest gate: PASS.** Expected and observed bytes are identical.

## Canonical inventory

| Family | Canonical inventory | Count | Registry count | Result |
| --- | --- | ---: | ---: | --- |
| Functional requirements | FR-1 through FR-43 | 43 | 43 | PASS |
| Non-functional requirements | NFR-1 through NFR-16 | 16 | 16 | PASS |
| User journeys | UJ-1 through UJ-6 | 6 | 6 | PASS |
| Core UX excluding accessibility | UX-FND, IA, VT, CP, ST, IP, RP, BUD | 83 | 83 | PASS |
| UX accessibility | UX-A11Y-1 through UX-A11Y-5 | 5 | 5 | PASS |
| All `UX-*` | 83 core plus 5 accessibility | 88 | 88 | PASS |
| Screen-reader scenario | SR-A11Y-1 | 1 | 1 | PASS |

The Batch 1 count formulation is correct: 83 non-accessibility UX IDs plus five
`UX-A11Y-*` IDs equals 88 `UX-*`; adding `SR-A11Y-1` yields 89 total UX
acceptance contracts.

## Exhaustive Functional Requirement consequence ledger

The PRD has 97 explicit acceptance consequences. All 43 FR IDs occur in the
registry, but ID presence is not consequence closure.

| FR | Consequences | Strong | Weak | Missing | Exact exception or principal owner evidence |
| --- | ---: | ---: | ---: | ---: | --- |
| FR-1 | 2 | 2 | 0 | 0 | Story 2.2 AC1-AC2 concretely covers human/machine PromiseId plus Lease and deterministic no-partial field failure. |
| FR-2 | 2 | 0 | 1 | 1 | Story 2.2's boundary names revisions/provenance, but its ACs do not require an auditable correction event on the same PromiseId; no owner AC excludes secrets or unrestricted output from required Promise metadata. |
| FR-3 | 2 | 1 | 1 | 0 | Story 2.3 AC1 fixes a finite default Lease; no owner AC makes expiry and renewal expectations explicit in the response. |
| FR-4 | 2 | 1 | 1 | 0 | Story 2.4 AC1 proves idempotency; AC2 does not require distinct deterministic results for every late, unauthorized, malformed, closed, and unknown-Promise case. |
| FR-5 | 3 | 2 | 0 | 1 | Story 2.5 prevents Host mutation and preserves one close reason; no registered FR-5 owner AC requires the next refresh to make the Promise inactive and a surviving match abandoned with that reason. |
| FR-6 | 2 | 1 | 1 | 0 | Story 2.3 rejects invalid persistence; auditability and explicit revocation of valid persistent intent are not concrete in its ACs. |
| FR-7 | 2 | 2 | 0 | 0 | Stories 2.1-2.6 cover retry-safe outcomes, stable exits, clean stdout, and human stderr. |
| FR-8 | 2 | 0 | 2 | 0 | Story 3.4 names diagnostic contracts and hostile inputs only in boundary/negative setup; its ACs do not require visible denied/unavailable diagnostics and terminal/shell-injection-safe rendering. |
| FR-9 | 2 | 2 | 0 | 0 | Story 3.5 keeps system/user scope distinct and emits scoped manager/access failures. |
| FR-10 | 2 | 1 | 1 | 0 | Story 3.6 rejects name-based identity; Docker failure isolation from every other Provider is only supplied by the separate completeness story and is absent from the FR-10 edge. |
| FR-11 | 2 | 1 | 1 | 0 | Story 3.7 prevents mutable numeric/PID identity; bounded invalid/unexpected PM2 JSON diagnostics are not asserted by its owner ACs. |
| FR-12 | 2 | 0 | 2 | 0 | Story 3.8 covers part of the PID/birth/executable and self-descendant rules, but not the full parent/user/working-directory field set or kernel-thread attribution consequence. |
| FR-13 | 2 | 0 | 2 | 0 | Story 3.9 freezes candidate reduction, but typed Provider detail without domain inheritance and encounter provenance for compatibility output are not concrete owner ACs. |
| FR-14 | 3 | 3 | 0 | 0 | Story 3.10 AC1-AC2 freezes all outcomes, the complete default/promotion table, usable partial evidence, and withheld absence conclusions. |
| FR-15 | 2 | 2 | 0 | 0 | Story 3.11 asserts winning byte/line bounds, sanitization, and failure locality. |
| FR-16 | 5 | 3 | 2 | 0 | Stories 1.2-1.3 cover inventory, frozen corpus, and additive/versioned fields; ACs do not fully state that live smoke cannot substitute for the corpus or require every deviation's rationale, version impact, replacement assertion, and consumer disposition. |
| FR-17 | 2 | 1 | 1 | 0 | Story 3.10 preserves usable partial truth; deterministic strict-mode exit plus machine error envelope remains boundary-level rather than an AC consequence. |
| FR-18 | 2 | 1 | 1 | 0 | Story 4.1 rejects weak-name matching, but the matched edge's complete contributing evidence, conflicts, and confidence record is only partial. |
| FR-19 | 2 | 1 | 0 | 1 | Story 4.2 prevents health under incomplete/conflicting evidence; no owner AC preserves logically compatible hot or stale evidence alongside health. |
| FR-20 | 2 | 1 | 0 | 1 | Story 4.2 yields unresolved rather than false broken; no owner AC retains last Heartbeat, Lease, Launch Mechanism, and candidate near-match evidence in the finding. |
| FR-21 | 2 | 1 | 0 | 1 | Story 4.3 prevents unsupported Agent-created attribution; no owner AC explains why no declaration matched and whether collection was complete. |
| FR-22 | 2 | 1 | 1 | 0 | Story 4.3 prevents silent destructive target selection; start times and complete matching evidence are not required alongside each duplicate identity. |
| FR-23 | 2 | 1 | 1 | 0 | Story 4.4 rejects missing samples/age-only staleness; the applied window and evidence source are not concrete finding fields in an AC. |
| FR-24 | 2 | 0 | 2 | 0 | Story 4.4's boundary names thresholds/timestamps/provenance, but its ACs do not require displayed metric/sample/source data or state that hot never implies safe. |
| FR-25 | 3 | 2 | 1 | 0 | Story 4.5 prevents cleanup and covers positive unmanaged/abandoned evidence; retention of the historical Promise match and exact expiry/closure reason is only indirect. |
| FR-26 | 2 | 2 | 0 | 0 | Story 4.6 recomputes after refresh; Story 6.4 recomputes immediately before mutation and refuses insufficient evidence. |
| FR-27 | 5 | 4 | 1 | 0 | Stories 4.7-4.8 concretely cover baseline interaction, window timestamps/timezone, first run, incompatibility, and override audit. Deterministic retention that preserves active truth exists in Story 1.8 but is absent from the reciprocal FR-27 edge. |
| FR-28 | 3 | 1 | 2 | 0 | Story 4.9 fixes BQ-1 through BQ-8 and withheld clean claims; complete baseline/window-unavailable presentation and exact Promise/Observation/evidence drill-down remain boundary-level. |
| FR-29 | 2 | 1 | 1 | 0 | Story 4.10 keeps ambiguity in Ungrouped; its ACs do not require inspectable Stack label, membership, confidence, and evidence. |
| FR-30 | 2 | 1 | 1 | 0 | Story 5.1 routes explicit output and deprecated fzf; it does not concretely require `--fzf-lines` removal through the compatibility ledger. |
| FR-31 | 2 | 1 | 1 | 0 | Story 5.3 references exact focus recovery; nonblocking refresh plus fresh/refreshing/stale treatment is implemented by an unregistered FR-31 owner, Story 5.6. |
| FR-32 | 2 | 1 | 1 | 0 | Story 5.5 fully closes opaque external references; independent inspection of unmatched declarations and unmatched Observations is only implicit in Story 5.4. |
| FR-33 | 2 | 2 | 0 | 0 | Story 5.7 covers NO_COLOR, ASCII/monochrome, hostile controls, and non-UTF-8 input. |
| FR-34 | 2 | 2 | 0 | 0 | Stories 5.1-5.9 cover responsive collapse and prohibit color, glyph, motion, or disappearing content as sole meaning. |
| FR-35 | 2 | 2 | 0 | 0 | Story 6.2 and Contract C-04 cover Promise-origin Start and absent/disabled unsupported or unsafe actions. |
| FR-36 | 2 | 1 | 0 | 1 | The sole registry owner, Story 6.1, covers only the enum/provider matrix and explicitly excludes planning. No FR-36 owner AC requires the plan's exact target, Provider-native operation, privilege, expected effect, and limitations. |
| FR-37 | 2 | 2 | 0 | 0 | Story 6.4 concretely revalidates identity and rejects display/row/cached identity. |
| FR-38 | 2 | 2 | 0 | 0 | Story 6.3 fixes destructive labels, unknown-safety acknowledgement, cancel focus, and bypass resistance. |
| FR-39 | 2 | 0 | 2 | 0 | Story 6.6 owns admission/idempotency, while the actual refresh overwrite and navigation/misattribution ACs live in Stories 1.7 and 6.8 outside the reciprocal FR-39 edge. |
| FR-40 | 3 | 3 | 0 | 0 | Stories 6.8-6.11 cover operation identity, fresh evidence, exact outcomes, diagnostics, next step, and command-exit insufficiency. |
| FR-41 | 2 | 1 | 1 | 0 | Story 6.2 prevents group widening; whole-process elevation and interactive authorization in raw mode are covered elsewhere but not by the FR-41 owner edge. |
| FR-42 | 2 | 0 | 1 | 1 | Story 7.1 builds a verified artifact, but activation-after-checks is owned only by unregistered Story 7.8 and no FR-42 owner AC requires deterministic installed version and compatibility output. |
| FR-43 | 2 | 2 | 0 | 0 | Stories 7.1-7.15 retain prior authority through validation and make failed forward work crash-recoverable without split truth. |
| **Total** | **97** | **58** | **32** | **7** | **39 consequences are not strong registered acceptance contracts.** |

## Non-Functional Requirement ledger

| NFR | Registered owner | Result | Exact gap or evidence |
| --- | --- | --- | --- |
| NFR-1 | Story 4.1 | Weak | Correlation is deterministic, but findings, attention rank, Safe-to-stop, ordering, and serialization are outside this owner AC. |
| NFR-2 | Story 3.10 | Weak | Collector partial truth is covered; storage, inspection, and mutation failure truthfulness are not covered by the registered owner. |
| NFR-3 | Story 3.2 | Weak | Scheduling is bounded, but subprocess capture, forced termination, unconditional reaping, and non-sequential failure isolation are owned elsewhere. |
| NFR-4 | Story 1.9 | Weak | Typed argv and no shell are concrete; safe end-of-options or identifier rejection is not. |
| NFR-5 | Story 6.7 | Weak | Exact Provider privilege and broad-privilege rejection are present; the raw-mode interactive-authorization prohibition is outside the owner edge. |
| NFR-6 | Story 5.1 | Strong | RAII restoration and invalid-init, normal, panic, and signal paths are concrete. |
| NFR-7 | Story 2.6 | Weak | Agent lifecycle stdout is clean; the cross-product requirement also binds strict collection, exports, actions, and release surfaces. |
| NFR-8 | Story 5.7 | Strong | Text-first, color/Unicode/motion independence, hostile-text safety, geometry independence, and assistive fixtures are concrete. |
| NFR-9 | Story 1.7 | Weak | Repository CAS is concrete, but lifecycle events, compatibility metadata, schema-versioned recovery, and partial-write rejection are not fully asserted. |
| NFR-10 | Story 2.3 | Weak | Boot/suspend/wall rollback behavior is partial; displayed wall time and every restart/discontinuity result are not concrete owner AC consequences. |
| NFR-11 | Story 1.8 | Weak | Retention/capacity is covered; local-default storage, permission restriction, minimized field set, and secret/unrestricted-log exclusion are outside the owner AC. |
| NFR-12 | Story 6.6 | Weak | Action admission/idempotency is covered; stale refresh, late Collector, and concurrent repository write replacement are owned by other unmapped stories. |
| NFR-13 | Story 1.10 | Weak | The registered owner is only a foundation aggregate and explicitly excludes later epics, while the NFR requires fixtures/fakes/goldens for every product domain. |
| NFR-14 | Story 1.3 | Weak | Frozen/live compatibility lanes are concrete; source inventory, named deployed consumers, exact Prometheus families, and full deviation disposition are not all in the owner AC. |
| NFR-15 | Story 7.1 | Weak | Target/checksum/locked artifact evidence is concrete; reversible installation is outside the owner edge. |
| NFR-16 | Story 1.5 | Weak | Defaults/ranges/config provenance are concrete; provenance in every user-visible finding is not. |
| **Total** || **2 Strong / 14 Weak / 0 Missing** ||

## User Journey ledger

Each journey is registered to exactly one story. Five of those single-story
edges cover only one stage of the canonical end-to-end flow.

| UJ | Registered owner | Result | Exact end-to-end gap or evidence |
| --- | --- | --- | --- |
| UJ-1 | Story 4.9 | Weak | Produces eight Brief questions but does not accept the interactive Explorer/filter/inspection path or timed-out-Provider recovery. |
| UJ-2 | Story 2.6 | Weak | Covers Agent CLI results but not launch, Heartbeat progression, reconciliation to healthy, release, or expiry-to-abandoned behavior. |
| UJ-3 | Story 4.2 | Weak | Classifies broken/unresolved but does not cover evidence inspection, candidate near matches, or Promise-origin Start. |
| UJ-4 | Story 6.9 | Weak | Decides action outcome but omits abandoned finding inspection, menu, confirmation, pre-mutation revalidation, and retained audit history. |
| UJ-5 | Story 4.4 | Weak | Covers stale/hot evidence but not the duplicate-plus-hot coexistence, exact identity comparison, unknown-safety deferral, or exact-target action. |
| UJ-6 | Story 7.15 | Strong | The aggregate binds command, staged artifact, checksum/smoke, consumers, recovery, KnownGood, rollback, and final Host smoke rows. |
| **Total** || **1 Strong / 5 Weak / 0 Missing** ||

## Exhaustive UX and accessibility ledger

Every ID appears exactly once in `requirementCoverage`, but 41 of 88 `UX-*`
owners assert only a subset of the canonical UX contract or a different
behavior. The lists below enumerate all 89 IDs without omission.

| Family | Strong IDs | Weak IDs | Missing | Result |
| --- | --- | --- | ---: | --- |
| UX-FND (6) | UX-FND-1 | UX-FND-2, UX-FND-3, UX-FND-4, UX-FND-5, UX-FND-6 | 0 | 1 Strong / 5 Weak |
| UX-IA (12) | UX-IA-3, UX-IA-6, UX-IA-7, UX-IA-8, UX-IA-11 | UX-IA-1, UX-IA-2, UX-IA-4, UX-IA-5, UX-IA-9, UX-IA-10, UX-IA-12 | 0 | 5 Strong / 7 Weak |
| UX-VT (4) | None | UX-VT-1, UX-VT-2, UX-VT-3, UX-VT-4 | 0 | 0 Strong / 4 Weak |
| UX-CP (16) | UX-CP-8, UX-CP-9, UX-CP-10, UX-CP-11, UX-CP-12, UX-CP-13, UX-CP-15 | UX-CP-1, UX-CP-2, UX-CP-3, UX-CP-4, UX-CP-5, UX-CP-6, UX-CP-7, UX-CP-14, UX-CP-16 | 0 | 7 Strong / 9 Weak |
| UX-ST (20) | UX-ST-1, UX-ST-2, UX-ST-3, UX-ST-4, UX-ST-5, UX-ST-6, UX-ST-8, UX-ST-9, UX-ST-10, UX-ST-11, UX-ST-13, UX-ST-17, UX-ST-18, UX-ST-19, UX-ST-20 | UX-ST-7, UX-ST-12, UX-ST-14, UX-ST-15, UX-ST-16 | 0 | 15 Strong / 5 Weak |
| UX-IP (12) | UX-IP-3, UX-IP-4, UX-IP-5, UX-IP-6, UX-IP-10, UX-IP-12 | UX-IP-1, UX-IP-2, UX-IP-7, UX-IP-8, UX-IP-9, UX-IP-11 | 0 | 6 Strong / 6 Weak |
| UX-A11Y (5) | UX-A11Y-1, UX-A11Y-4, UX-A11Y-5 | UX-A11Y-2, UX-A11Y-3 | 0 | 3 Strong / 2 Weak |
| UX-RP (6) | UX-RP-1, UX-RP-2, UX-RP-3, UX-RP-4, UX-RP-5, UX-RP-6 | None | 0 | 6 Strong / 0 Weak |
| UX-BUD (7) | UX-BUD-1, UX-BUD-2, UX-BUD-3, UX-BUD-7 | UX-BUD-4, UX-BUD-5, UX-BUD-6 | 0 | 4 Strong / 3 Weak |
| **All UX-*** | **47 IDs** | **41 IDs** | **0** | **47 Strong / 41 Weak** |
| SR-A11Y (1) | SR-A11Y-1 | None | 0 | 1 Strong / 0 Weak |

### Principal UX edge defects

- `UX-FND-3` is registered only to Story 1.4, whose ACs test canonical JSON
  bytes and identity encoding. The UX contract requires display/group context
  never to become an action identity and requires Snapshot generation,
  Provider operation, and OperationId binding. Those behaviors live in later
  action stories, not the reciprocal owner.
- `UX-IA-2` and `UX-CP-3` are registered to responsive layout Story 5.2, but
  their source contracts require the attention/Stack/Ungrouped hierarchy,
  facets, exact-item row behavior, and inspection entry.
- `UX-VT-1` and `UX-VT-2` are registered to accessibility Story 5.7; its ACs
  test display modes and hostile bytes, not calm accountable copy or canonical
  vocabulary. `UX-VT-4` is registered to help/config Story 5.8 rather than the
  action-outcome recovery copy owner.
- `UX-CP-14` is registered to duplicate-set Story 4.3, whose ACs do not render
  every orphaned, duplicate, stale, hot, unmanaged, and abandoned marker or
  prove that coexisting markers never imply action safety.
- `UX-ST-7` does not concretely require the active query/facets, unfiltered
  count, and focused Clear-all control. `UX-ST-14` does not require preserved
  old target details, closed confirmation, and Refresh focus. `UX-ST-15` does
  not require both old/replacement immutable evidence and no automatic retry.
- `UX-IP-7` is registered only to status-surface Story 6.8 even though it owns
  the complete plan-confirm-pending-revalidate-execute-verify-outcome flow.
  `UX-IP-11` is registered only to action parity Story 6.11 even though it owns
  the full Brief, facets, inspect, plan, execute, and status linear sequence.
- `UX-A11Y-2`'s single owner does not prove keyboard/focus behavior across every
  core journey and modal. `UX-A11Y-3`'s owner proves action parity, not the full
  first-class human-linear Brief and inspection alternative.
- Story 6.12 names `UX-BUD-4/5/6` in its negative omission gate but its positive
  AC never asserts the 100 ms submit, 1,000 ms progress, or 100 ms terminal
  rendering thresholds and visible acceptance fields.

## Plane, Git, and Telemetry boundary

**PASS — Strong.** Contract C-13 and Story 5.5 AC1-AC2 state the complete
affirmative and negative boundary:

- Plane owns intended work, state, and scheduling.
- Git owns code changes and reviewable history.
- Telemetry owns events and measurements.
- References are labeled display-only.
- `srvls` never fetches or mutates them and never uses them as Runtime identity,
  health, reconciliation, ownership, Safe-to-stop, or mutation authority.

This closes prior F-UX-3 without relying on an `Out of Scope` clause.

## Addendum direction and named-seam ledger

| Addendum obligation | Primary epic evidence | Result |
| --- | --- | --- |
| One initial Rust binary and one-tool experience | Stories 1.1, 5.1, and 7.1 | Strong |
| Hexagonal domain/application isolation | Story 1.1 maps AD-1/AD-3, but no numbered AC names the hexagonal boundary or complete prohibited dependency set | Weak |
| Elm-style model/message/update/view/effect shell | Architecture precedence supplies it; no story AC names or tests the full shell seam | Weak |
| Explicit Strategy, Adapter, and Command seams with composition | Architecture supplies the design paradigm; no story AC makes all three named variation seams concrete | Weak |
| Layered migration oracle | Stories 1.2-1.3 | Strong |
| Preserved deterministic legacy surfaces | Stories 1.2-1.4 and 5.1 | Strong |
| Bootstrap, module, lockfile, harness, format, lint, locked test, MSRV 1.88, and current-stable gates before Provider work | Story 1.1 mentions Rust 2024, locked dependencies, boundary test, and release-CI ownership, but its AC omits format/lint/MSRV 1.88/current-stable execution | Weak |
| Total bounded subprocess execution separated from concurrent orchestration/outcome policy | Stories 1.9 and 3.1-3.3 | Strong |
| Explicit TUI Start path | Stories 6.1-6.2 | Strong |
| Mutation initiation/confirmation separated from async execution/races/verification/rendering | Stories 6.2-6.12 | Strong |
| Durable formats and locations | Contracts C-07/C-10/C-11 and Stories 1.6-1.8, 4.7, 6.3-6.6, 7.4-7.14 | Strong |
| Agent declaration/heartbeat/renewal/release/query contracts | Stories 2.1-2.6 | Strong |
| Lease clock across exit/restart/suspend/discontinuity | Story 2.3 and AD-17 | Strong |
| Evidence-weighted cross-Provider identity/correlation | Stories 3.4-3.9 and 4.1 | Strong |
| Retention supports morning change without becoming Telemetry | Contract C-07, Contract C-13, Stories 1.8 and 4.7-4.9 | Strong |
| **Total** || **11 Strong / 4 Weak / 0 Missing** |

## Reciprocal registry audit

The JSON registry is mechanically sound. It is not semantically sufficient.

| Check | Result |
| --- | --- |
| One parseable fenced JSON registry | PASS |
| Canonical source counts | PASS: 43 FR, 16 NFR, 6 UJ, 83 core UX, 5 UX-A11Y, 1 SR-A11Y |
| Registry inventory keys equal `requirementCoverage` keys | PASS: 213/213 |
| Story headings equal `storyInventory` | PASS: 73/73 |
| Story `Requirement Mapping` equals `coverageByStory` | PASS: 73/73 |
| `coverageByStory` reverses exactly to `requirementCoverage` | PASS: 213/213, zero differences |
| Story acceptance structure | PASS: 73 stories, exactly two GWT criteria each, 146 total |
| Dependency chain | PASS: Story 1.1 alone is `None`; every later story names the exact preceding Story ID |
| AD-11 row shape | PASS: 68 unique rows, valid owner, nonempty fixture/assertion/command, current/future delivery |
| Current/future AD-11 delivery | PASS structurally: 13 current, 55 future |
| Semantic consequence ownership | FAIL: 39 FR consequences, 14 NFRs, five UJs, and 41 UX IDs are weak or missing despite reciprocal tags |

The registry proves exact set membership. It does not prove that the mapped AC
contains the source consequence; the exhaustive ledgers above provide that
second check.

## Batch 1 disposition audit

### Product and traceability dispositions

| Prior finding | R2 result | Evidence |
| --- | --- | --- |
| F-REQ-1 | Closed as scoped | The seven previously named FR consequences are concrete in Stories 1.2-1.3, 2.2, 3.10, 4.6-4.8, 5.4-5.5, and 6.4. New full-corpus gaps remain elsewhere. |
| F-UX-1 | Closed | Story 4.8 owns b-entry, Cancel focus, Esc, exact override, pointer-only mutation, and immediate Evidence Window recomputation. |
| F-UX-2 | Closed as scoped | The 21 previously incorrect action-state edges were removed and now point to Stories 3.10, 4.8, 5.6, 5.8, 6.4, 6.8, and 6.9. New non-action UX edge defects remain. |
| F-UX-3 | Closed | Story 5.5 is a complete affirmative Plane/Git/Telemetry acceptance contract. |
| F-QUAL-1 | Not closed | Epic 1 is still architecture tests, compatibility corpus, configuration, SQLite, repositories, retention, CommandRunner, and aggregate gates. Renaming this as operator trust does not create an independently usable product outcome. |
| F-QUAL-2 | Not closed | Stories 6.12 and 7.15 remain aggregate, multi-subsystem work packages. Story 7.15 still wires commands, locks, toolchain, artifact, manifest, FD4, D-Bus, takeover, KnownGood, FirstInstall, rollback, seven transition histories, and Host smoke. |
| F-QUAL-3 | Not closed | Story 1.7 pre-seeds plan, operation, baseline, Snapshot transactions and current CAS; Story 3.1 pre-seeds baseline, operation, history, and current cuts before their owning epics. |

### Story-quality and architecture dispositions

| Review family | Rows | Current disposition |
| --- | ---: | --- |
| Story quality/dependency | 18 | 17 claims remain satisfied; F-05 is contradicted by Story 1.7's explicit current-pointer CAS while the ledger says Story 4.7 alone owns it. |
| Architecture divergence | 30 | 29 remediations remain represented; F-01 remains the explicit user path override and produces exactly the documented legacy-validator failure. No additional architecture verdict is inferred by this product review. |

### Disposition accounting defect

The prior product review frontmatter states `findingCount: 8`, but the report has
seven titled findings and the Batch 1 ledger has seven product disposition rows.
The ledger therefore cannot demonstrate “every finding” against its own source
count until the source count or missing disposition is reconciled.

## Findings

### F-R2-01 — Runtime Promise lifecycle consequences are not fully accepted

FR-2 through FR-6 retain six weak or missing consequences: auditable same-ID
correction, minimized Promise metadata, response renewal expectations, the full
distinct Heartbeat result set, next-refresh close-to-abandoned projection, and
valid persistent-intent audit/revocation. The lifecycle stories contain related
boundaries, but their registered numbered ACs do not close these outcomes.

### F-R2-02 — Provider collection and normalization lose source consequences

FR-8, FR-10 through FR-13, FR-16, and FR-17 retain provider-specific gaps:
visible denied/unavailable diagnostics, hostile-text behavior, cross-Provider
failure isolation, bounded invalid PM2 JSON, complete direct-process fields and
kernel-thread attribution, typed detail without inheritance, encounter
provenance, complete deviation-ledger fields, and strict machine exit behavior.

### F-R2-03 — Reconciliation findings omit required evidence and coexistence

FR-18 through FR-25 do not fully accept match confidence/conflicts, compatible
hot/stale evidence alongside health, broken-finding Heartbeat/Lease/mechanism
detail, orphan no-match explanations, duplicate start/match evidence, stale/hot
policy display, hot-not-safe separation, and abandoned historical Promise
context. Classification tags exist, but required explanatory payloads do not.

### F-R2-04 — Snapshot, Brief, Stack, and navigation edges remain partial

FR-27 through FR-32 leave retention outside FR-27 reciprocity, baseline/window
and drill-down detail weak in FR-28, Stack confidence/evidence inspection weak
in FR-29, `--fzf-lines` ledger removal weak in FR-30, refresh behavior outside
FR-31 reciprocity, and unmatched-item inspection only implicit for FR-32.

### F-R2-05 — Action and release owner edges omit binding consequences

FR-36 is registered only to enum Story 6.1, which explicitly excludes planning,
so no owner AC asserts the complete plan fields. FR-39's refresh and navigation
isolation lives outside its registry edge. FR-41 omits the raw-mode privilege
prompt prohibition. FR-42 omits deterministic installed version/compatibility
output and maps activation-after-checks only indirectly.

### F-R2-06 — Fourteen NFRs are mapped to narrower single-story behavior

Only NFR-6 and NFR-8 have complete registered AC ownership. The remaining 14
are cross-cutting but registered to one narrow owner, leaving required domains
outside the reciprocal edge. NFR-13 is the clearest counterexample: its only
owner is the Epic 1 foundation gate, whose scope explicitly excludes every
later product epic that NFR-13 requires to be testable.

### F-R2-07 — Five user-journey edges are not end to end

UJ-1 through UJ-5 each map to one mid-flow story instead of the complete source
journey. A registry traversal cannot reach the full entry, path, climax,
resolution, and edge case for morning handoff, Agent lifecycle, broken-promise
diagnosis, abandoned-runtime removal, or duplicate-plus-hot triage.

### F-R2-08 — UX Foundation and Information Architecture owners are semantic mismatches

The strongest counterexamples are `UX-FND-3` mapped to canonical JSON Story
1.4, `UX-IA-2` mapped to responsive geometry Story 5.2, and `UX-IA-10` mapped
only to Agent lifecycle Story 2.6 despite binding strict collection, outputs,
and actions. Twelve Foundation/IA IDs are weak across these families.

### F-R2-09 — Voice/tone and component contracts are mapped to different behavior

All four `UX-VT-*` IDs are weak. Accessibility Story 5.7 does not accept calm
copy or canonical vocabulary, and config/help Story 5.8 does not accept action
recovery copy. Nine component IDs likewise omit required anatomy, interaction,
or all-state coverage; `UX-CP-14` is restricted to duplicate behavior instead
of the complete finding-marker vocabulary.

### F-R2-10 — State and interaction mappings omit required transitions and controls

Weak state owners omit filtered-empty anatomy, timeout uncertainty, stale-target
comparison/focus, replacement evidence/no-retry, and complete
baseline-unavailable reasons. Weak interaction owners omit full deterministic
routing, modal navigation, the complete plan-to-outcome chain, install output,
cross-domain machine fields, and the six-step human-linear path.

### F-R2-11 — Accessibility and action-budget acceptance is incomplete

`UX-A11Y-2` and `UX-A11Y-3` do not cover every core keyboard/modal journey or
the complete linear Brief/inspect/action alternative. Story 6.12 detects a
missing `UX-BUD-4/5/6` row but its positive AC does not assert the three timing
thresholds or their required visible results.

### F-R2-12 — Four binding addendum gates remain implicit

Hexagonal isolation, the complete Elm-style shell, all three named
Strategy/Adapter/Command seams, and the pre-Provider format/lint/MSRV 1.88/
current-stable gate are recoverable only through architecture precedence. The
story ACs never name and test these planning constraints, so the addendum is not
fully traceable at story acceptance altitude.

### F-R2-13 — Batch 1 closure overstates disposition and ownership repair

Batch 1 marks F-QUAL-1 through F-QUAL-3 and story-quality F-05 remediated, but
Epic 1 remains technical-horizontal, Stories 6.12/7.15 remain aggregate-sized,
Stories 1.7/3.1 still pre-seed later aggregate state, and Story 1.7 duplicates
current-pointer CAS ownership. Separately, the prior product report claims eight
findings while exposing and disposing only seven.

## Validation evidence

| Check | Result |
| --- | --- |
| Target commit | PASS: `8ebdc20e2ea08f5bb7529dad1bc1b2d90c50a705` |
| Target SHA-256 | PASS: `b5368de55ada106282a2b623879feef5ceffea1a4dd0afd54870326aebb1ee27` |
| Source/registry structural parser | PASS: 43/16/6/88+1, 73 stories, 146 ACs, 213 reciprocal IDs, zero mechanical errors |
| Compatibility oracle | PASS: providers, outputs, CLI, inspection, actions, source pin, immutable hashes, AD-9 coverage |
| Planning quarantine | EXPECTED OVERRIDE: exact sole observed failure `planning-root tombstone does not fail closed` |
| Aggregate architecture gate | EXPECTED OVERRIDE: compatibility passes, then the same planning-quarantine assertion halts the current legacy gate |
| Shell syntax | PASS: aggregate, compatibility, and smoke scripts |
| Target commit whitespace | PASS: `git diff --check 8ebdc20^ 8ebdc20` |
| Report Markdown | PASS under the repository profile |
| Review diff scope | PASS: this R2 report only |

## Final assessment

The candidate is mechanically complete but not semantically implementation
ready. A conforming implementation team could follow the reciprocal registry
and satisfy every mapped story AC while still omitting binding PRD consequence
fields, cross-cutting NFR behavior, five journey stages, 41 UX contracts, and
four addendum gates. The artifact remains correctly marked
`remediated-draft`, `assignable: false`, and `implementationAuthority: false`.

**Final verdict: FAIL — 13 findings.**
