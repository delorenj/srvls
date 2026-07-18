---
title: Epic Product Traceability Review R3
project: srvls
review_date: 2026-07-17
review_type: independent-product-traceability-r3
target_commit: c237a2a6a42ad0a20b4f660ae7377360a55471fb
target_path: _bmad-output/planning-artifacts/epics.md
actual_sha256: beca731ca618cd89e84ef27070cc1e5a2cb33fc820784faeb989194fc9dd2886
digest_gate: PASS
verdict: FAIL
findingCount: 14
completionStatus: complete
---

# Epic Product Traceability Review R3

## Verdict

**FAIL — 14 findings.**

The Batch 2 artifact has complete ID presence and reciprocal mapping, but the
registered owner ACs still do not accept the complete source consequences.
All 13 R2 finding families retain residual defects, and the normative registry
adds one mechanical count contradiction. PASS is prohibited above zero.

## Digest

```text
$ git rev-parse c237a2a
c237a2a6a42ad0a20b4f660ae7377360a55471fb

$ git show c237a2a:_bmad-output/planning-artifacts/epics.md | sha256sum
beca731ca618cd89e84ef27070cc1e5a2cb33fc820784faeb989194fc9dd2886  -
```

The audited bytes are the exact committed `epics.md` blob at `c237a2a`.

## Methods

1. Read the complete target blob, R2 product review, canonical PRD, PRD
   addendum, and canonical UX `EXPERIENCE.md` and `DESIGN.md` at `c237a2a`.
2. Replayed every R2 finding against the revised closed contracts, story
   boundaries, requirement mappings, validation oracles, and numbered GWT ACs.
3. Used `rg` to enumerate source FR, NFR, UJ, UX, accessibility, and addendum
   IDs; split all 43 FR sections and counted their explicit Consequences.
4. Parsed the normative JSON registry and checked declared counts, uniqueness,
   story headings, GWT AC count, mapping text, inventory coverage, reciprocal
   `coverageByStory`/`requirementCoverage` edges, and AD-11 owners.
5. Ran `python3 tests/validate_planning_quarantine.py`,
   `bash tests/validate_architecture_contracts.sh`, the frozen compatibility
   replay reached by that aggregate, and `git diff --check` for the target
   `epics.md` change.

## Exhaustive count evidence

| Surface                               | Source or declared |                       Parsed or covered | Result                  |
| ------------------------------------- | -----------------: | --------------------------------------: | ----------------------- |
| Epics                                 |                  7 |                              7 headings | PASS                    |
| Stories                               |                 73 | 73 unique headings and registry entries | PASS                    |
| Numbered GWT ACs                      |                146 |              146; exactly two per story | PASS                    |
| Functional requirements               |                 43 |   43 inventory IDs and 43 coverage keys | PASS                    |
| FR acceptance consequences            |                 97 |         59 strong / 31 weak / 7 missing | **FAIL: 38 not strong** |
| Non-functional requirements           |                 16 |          2 strong / 14 weak / 0 missing | **FAIL: 14 weak**       |
| User journeys                         |                  6 |           1 strong / 5 weak / 0 missing | **FAIL: 5 weak**        |
| UX core excluding accessibility       |                 83 |   83 inventory IDs and 83 coverage keys | PASS                    |
| UX accessibility                      |                  5 |     5 inventory IDs and 5 coverage keys | PASS                    |
| All UX requirements                   |                 88 |         47 strong / 41 weak / 0 missing | **FAIL: 41 weak**       |
| Screen-reader scenarios               |                  1 |           1 strong / 0 weak / 0 missing | PASS                    |
| Addendum constraints                  |                 15 |          11 strong / 4 weak / 0 missing | **FAIL: 4 weak**        |
| Architecture decisions                |                 25 |      25 inventory IDs and coverage keys | PASS                    |
| Architecture limits                   |                 24 |      24 inventory IDs and coverage keys | PASS                    |
| Host profiles                         |                  1 |         1 inventory ID and coverage key | PASS                    |
| Supplemental metrics                  |                  9 |       9 inventory IDs and coverage keys | PASS                    |
| All requirement IDs                   |                213 | 213 inventory IDs and 213 coverage keys | PASS                    |
| Reciprocal registry edges             |           0 errors |                                0 errors | PASS                    |
| Story mapping/registry mismatches     |                  0 |                                       0 | PASS                    |
| AD-11 row owners missing from stories |                  0 |                                       0 | PASS                    |
| AD-11 row IDs                         |        68 declared |                          81 unique rows | **FAIL**                |

The 81-row array consists of the prior 68 rows plus `AD11-CUR-14` and
`AD11-FUT-56` through `AD11-FUT-67`. There are no duplicate row IDs and every
row names a valid story owner.

Presence is not semantic closure. A mapping tag, generic named-oracle clause,
closed contract elsewhere, or behavior owned by an unregistered story does not
make the registered owner edge strong. Compared with R2, only the auditable
same-Promise revision/event consequence in FR-2 became strong; the aggregate
FR ledger moves from 58/32/7 to 59/31/7.

## Findings

### F-R3-01 — Runtime Promise lifecycle consequences remain incomplete

FR-2 still omits metadata minimization; FR-3 omits response expiry/renewal;
FR-5 omits next-refresh inactive/abandoned projection; and FR-6 omits explicit
audit/revocation. Story 2.2 now closes the auditable revision/event portion,
but Stories 2.2 through 2.5 do not close the remaining registered edges.

### F-R3-02 — Provider collection and normalization still lose source consequences

Registered owner ACs remain incomplete for cron denied/unavailable and hostile
text, Docker cross-Provider isolation, bounded PM2 invalid JSON, the full
direct-process identity/attribution fields, and typed-detail/encounter
provenance. The compatibility and strict-policy gaps also remain outside their
complete reciprocal owner edges.

### F-R3-03 — Reconciliation findings still omit required explanatory evidence

FR-18 through FR-25 remain partial for match confidence/conflicts, compatible
hot/stale coexistence, broken-finding Heartbeat/Lease/mechanism context, orphan
no-match explanations, duplicate comparison evidence, stale/hot policy fields,
hot-not-safe separation, and abandoned historical Promise context.

### F-R3-04 — Snapshot, Brief, Stack, and navigation edges remain partial

FR-27 through FR-32 still omit reciprocal acceptance for retention, complete
baseline/window/drill-down detail, inspectable Stack evidence, compatibility-
ledger removal of `--fzf-lines`, nonblocking refresh state, and independent
inspection of unmatched declarations and Observations.

### F-R3-05 — Action and release owner edges remain incomplete

FR-36 is still registered only to Story 6.1, whose Out of Scope excludes
planning; the complete plan lives in unmapped Story 6.3. FR-39 still omits
refresh/navigation isolation, FR-41 omits the raw-mode privilege-prompt ban,
and FR-42 omits installed version/compatibility output and activation only
after checks.

### F-R3-06 — Fourteen NFR owner edges remain narrower than their requirements

The ledger remains 2 strong and 14 weak. For example, NFR-13 still maps only
to Story 1.10, whose foundation scope excludes the later product domains that
the source NFR requires to be testable without Host mutation.

### F-R3-07 — Five user journeys remain non-end-to-end

UJ-1 through UJ-5 still map to a single mid-flow story rather than accepting
their complete entry, path, climax, resolution, and edge cases. Only UJ-6 is
strong end to end.

### F-R3-08 — Foundation and Information Architecture mappings remain semantic mismatches

Examples remain `UX-FND-3` mapped to canonical-JSON Story 1.4 and `UX-IA-2`
mapped to geometry Story 5.2. `UX-IA-10` still lacks complete ownership across
strict collection, output, Agent, and action machine results.

### F-R3-09 — Voice/tone and component mappings remain incomplete

All four `UX-VT-*` edges remain weak, and component mappings still omit source
anatomy, interaction, or all-state behavior. `UX-CP-14`, for example, remains
owned by duplicate-set behavior rather than the complete finding-marker
vocabulary.

### F-R3-10 — State and interaction mappings still omit transitions and controls

Residuals include filtered-empty anatomy, timeout uncertainty, stale-target
comparison/focus, replacement evidence/no-retry, complete baseline-unavailable
reasons, modal routing, the full plan-to-outcome chain, and the complete
human-linear path.

### F-R3-11 — Accessibility and action-budget acceptance remains incomplete

`UX-A11Y-2` and `UX-A11Y-3` still do not accept every core keyboard/modal
journey or the complete linear alternative. Story 6.12 detects omitted
`UX-BUD-4/5/6` rows but its positive AC does not assert the required 100 ms,
1,000 ms, and 100 ms thresholds and visible results.

### F-R3-12 — Four addendum gates remain implicit or partial

The registered story ACs still do not accept the complete hexagonal boundary,
Elm shell, and Strategy/Adapter/Command seams. MSRV and moving-stable are now
explicit, but the complete pre-Provider format/lint/toolchain gate is not.

### F-R3-13 — R2 closure still overstates ownership repair

Story 1.7's duplicate current-pointer ownership is repaired, but Epic 1 remains
technical-horizontal and Stories 6.12 and 7.15 remain aggregates. The generic
oracle language does not repair the semantic owner-edge gaps enumerated above.

### F-R3-14 — The normative AD-11 count understates its own registry

`canonicalCounts.ad11Rows` is `68` at `epics.md:482`, but the normative
`ad11Rows` array contains 81 unique IDs. The 13 added rows are present and
valid, so this is not an extraction ambiguity or duplicate-row artifact.

A machine consumer that trusts `canonicalCounts` can accept an incomplete
68-row traversal or reject the valid 81-row array. This is a mechanical
traceability contradiction inside the declared normative registry. Change the
declared count to 81 and rerun the reciprocal/count parser.

## Script evidence

| Command                                             | Result                                                                                                             |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Exact Git-blob SHA-256                              | PASS                                                                                                               |
| Source-ID versus registry set comparison            | PASS; no missing or extra FR/NFR/UJ/UX/SR IDs                                                                      |
| Registry uniqueness and reciprocity parser          | FAIL only on `ad11Rows`: declared 68, actual/unique 81                                                             |
| `git diff --check c237a2a^ c237a2a -- .../epics.md` | PASS                                                                                                               |
| Frozen compatibility replay                         | PASS: Provider, output, CLI, inspection, action, source-pin, immutable-hash, and AD-9 checks                       |
| Planning quarantine script                          | Expected exit 1: the canonical path intentionally overrides the planning-root tombstone, as already accepted by R2 |
| Architecture aggregate script                       | Expected exit 1 only because it chains the same quarantine check; compatibility replay passed                      |

**Final verdict: FAIL — 14 findings. PASS is permitted only at zero.**
