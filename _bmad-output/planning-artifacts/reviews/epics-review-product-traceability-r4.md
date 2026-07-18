---
title: Epic Product Traceability Review R4
project: srvls
review_date: 2026-07-17
review_type: independent-product-traceability-r4
target_path: _bmad-output/planning-artifacts/epics.md
expected_sha256: 8debf05b8fd24bc19a00dfc6ce56961050d56b97ea972613135616df4eaedbd4
actual_sha256: 8debf05b8fd24bc19a00dfc6ce56961050d56b97ea972613135616df4eaedbd4
digest_gate: PASS
verdict: FAIL
findingCount: 13
completionStatus: complete
---

# Epic Product Traceability Review R4

## Verdict

**FAIL — 13 findings.**

The requested digest is exact and the registry is mechanically reciprocal, but
the Batch 3 remediation does not complete semantic ownership. Contract C-22
describes the missing end-to-end consequences and six later aggregate stories
accept parts of that contract. The normative `coverageByStory` and
`requirementCoverage` graph, however, still assigns the affected requirements
to the narrower R3 owners. A requirement traversal therefore cannot reach the
new acceptance gate that is supposed to close it.

R3 finding F-R3-14 is closed. F-R3-01 through F-R3-13 retain at least one
concrete residual each. PASS is prohibited above zero.

## Digest and scope

```text
$ sha256sum _bmad-output/planning-artifacts/epics.md
8debf05b8fd24bc19a00dfc6ce56961050d56b97ea972613135616df4eaedbd4  _bmad-output/planning-artifacts/epics.md
```

The audited bytes are the current committed `epics.md` blob at `30ce86d`.
This review read the complete R3 product review, canonical PRD, addendum,
canonical UX `DESIGN.md` and `EXPERIENCE.md`, the complete target artifact, and
the Batch 3 changes from R3 through the requested digest. No source requirement
was inferred from an older review when a live canonical source was available.

## Method

1. Verified the requested SHA-256 before judging content.
2. Replayed every R3 finding against current contracts, story boundaries,
   numbered GWT ACs, requirement mappings, and the normative JSON registry.
3. Parsed the registry and checked declared counts, uniqueness, story headings,
   two ACs per story, requirement inventory, reciprocal edges, and AD-11 owners.
4. Diffed the FR/NFR/UJ/UX `requirementCoverage` graph at R3 (`919d319`) against
   the requested digest instead of treating new prose as an ownership change.
5. Required the story that acceptance-tests a consequence to be reachable from
   that requirement's reciprocal registry edge. Contract prose, a fixture name,
   or an unmapped aggregate did not count as complete semantic ownership.
6. Ran the frozen compatibility replay, planning-quarantine validator,
   aggregate architecture validator, and whitespace checks.

## Exhaustive mechanical evidence

| Surface | Declared/source | Parsed | Result |
| --- | ---: | ---: | --- |
| Epics | 7 | 7 | PASS |
| Stories | 73 | 73 | PASS |
| Numbered GWT ACs | 146 | 146; exactly two per story | PASS |
| Functional requirements | 43 | 43 inventory and coverage keys | PASS |
| Non-functional requirements | 16 | 16 inventory and coverage keys | PASS |
| User journeys | 6 | 6 inventory and coverage keys | PASS |
| UX core excluding accessibility | 83 | 83 inventory and coverage keys | PASS |
| UX accessibility | 5 | 5 inventory and coverage keys | PASS |
| Screen-reader scenarios | 1 | 1 inventory and coverage key | PASS |
| All registered requirement IDs | 213 | 213 | PASS |
| FR/NFR/UJ/UX reciprocal edges | 226 | 226; zero directional differences | PASS |
| AD-11 rows | 82 | 82 actual / 82 unique | PASS |
| Story mapping/registry mismatches | 0 | 0 | PASS |
| Semantic owner closure | zero permitted | 13 open finding families | **FAIL** |

The mechanical graph is internally consistent. That does not make the graph
semantically complete.

## Ownership-delta evidence

The product-edge diff from R3 to the requested digest contains no FR, NFR, or
UJ change. It adds only these four UX edges, all to Story 6.12:

- `UX-A11Y-1`
- `UX-A11Y-2`
- `UX-A11Y-5`
- `UX-RP-5`

Contract C-22 at `epics.md:466-486` says the aggregate gates prove the residual
Agent, Provider, reconciliation, product-navigation, action, release, UJ, NFR,
and foundation consequences. The aggregate stories that invoke those gates
retain these reciprocal product mappings:

| Aggregate gate | Current FR/NFR/UJ/UX mappings |
| --- | --- |
| Story 1.10 | `FR-16`, `NFR-13` |
| Story 2.6 | `FR-7`, `NFR-7`, `UJ-2`, `UX-IA-10`, `UX-IP-9` |
| Story 3.11 | `FR-14`, `FR-15`, `UX-CP-7`, `UX-IA-4`, `UX-ST-17` |
| Story 4.10 | `FR-26`, `FR-29`, `UX-CP-4` |
| Story 5.9 | `FR-34`, `UX-BUD-1/2/3/7` |
| Story 6.12 | `FR-40`, `UX-A11Y-1/2/5`, `UX-BUD-4/5/6`, `UX-RP-5` |
| Story 7.15 | `FR-43`, `UJ-6`, `UX-CP-16`, `UX-IA-9`, `UX-IP-8` |

This is the controlling counterexample. For example, C-22 and Story 2.6 AC1
now test FR-2 metadata minimization, but `requirementCoverage["FR-2"]` still
names only Story 2.2. Story 2.2 AC1 tests revision/idempotency and AC2 tests
invalid fields; neither accepts metadata minimization. Both directions of the
registry agree on that incomplete owner, so the parser passes while semantic
ownership fails.

## R3 finding disposition

| R3 finding | R4 result | Current evidence |
| --- | --- | --- |
| F-R3-01 | **OPEN** | Agent residuals moved into C-22 and Story 2.6 (`epics.md:466-470,2532-2555`), but FR-2/3/5/6 remain registered only to Stories 2.2/2.3/2.5. |
| F-R3-02 | **OPEN** | Provider residuals moved into C-22 and Story 3.11 (`epics.md:469-472,2800-2823`), while FR-8/10/11/12/13 remain registered to Stories 3.4/3.6/3.7/3.8/3.9. |
| F-R3-03 | **OPEN** | Reconciliation residuals moved into C-22 and Story 4.10 (`epics.md:472-476,3043-3066`), while FR-18 through FR-25 retain their narrow R3 owners. |
| F-R3-04 | **OPEN** | Product-navigation residuals moved into C-22 and Story 5.9 (`epics.md:476-478,3262-3285`), but FR-27 through FR-32 ownership did not change. |
| F-R3-05 | **OPEN** | Action/release residuals moved into aggregate gates, but FR-36 still maps only to enum Story 6.1, FR-39 to Story 6.6, FR-41 to Story 6.2, and FR-42 to Story 7.1. |
| F-R3-06 | **OPEN** | C-22 says NFR-1 through NFR-16 run across all subsystem gates (`epics.md:483-485`), but no NFR edge changed. NFR-13 still maps only to foundation Story 1.10. |
| F-R3-07 | **OPEN** | C-22 declares end-to-end UJ-1 through UJ-6 gates, but no UJ edge changed. UJ-1/3/4/5 still point to one mid-flow story each; UJ-2 still omits launch-to-healthy behavior. |
| F-R3-08 | **OPEN** | Foundation/IA ownership did not move to the new product gate. `UX-FND-3` remains owned by encoding Story 1.4 and `UX-IA-2` by geometry Story 5.2. |
| F-R3-09 | **OPEN** | Story 5.9 now says every voice/component row matches goldens, but no `UX-VT-*` edge points to it and `UX-CP-14` remains owned by duplicate-set Story 4.3. |
| F-R3-10 | **OPEN** | State/interaction aggregate coverage remains outside the affected reciprocal edges; `UX-ST-7/12/14/15/16`, `UX-IP-7`, and `UX-IP-11` retain their R3 owners. |
| F-R3-11 | **OPEN, narrowed** | Story 6.12 now owns explicit 100/1000/100 ms budgets and receives four UX edges, closing the budget residual and strengthening keyboard coverage. `UX-A11Y-3` still maps only to Story 6.11, whose action parity does not accept the full Brief/inspect linear alternative required at `EXPERIENCE.md:472-475`. |
| F-R3-12 | **OPEN** | C-22 names hexagonal, Elm, and Strategy/Adapter/Command gates (`epics.md:485-486`), but Story 1.10 does not invoke C-22 and Story 1.1 ACs do not accept the complete named seams or the full format/lint/toolchain gate. |
| F-R3-13 | **OPEN** | The aggregate prose does not repair reciprocal ownership; Epic 1 remains technical-horizontal and Stories 6.12/7.15 remain multi-subsystem aggregates. |
| F-R3-14 | **CLOSED** | `canonicalCounts.ad11Rows` is 82 and the array has 82 unique rows with valid story owners. |

## Findings

### F-R4-01 — Agent consequence gate is not the registered FR owner

FR-2, FR-3, FR-5, and FR-6 source consequences at `prd.md:190-236` are accepted
only by the C-22/Story 2.6 aggregate. Their reciprocal edges still end at the
narrow lifecycle stories. An implementation can satisfy each registered owner
AC without metadata minimization, response expiry/renewal, next-refresh
inactive/abandoned projection, or audited revocation.

### F-R4-02 — Provider consequence gate is not the registered FR owner

The C-22/Story 3.11 AC covers cron denial/hostile text, Docker isolation, PM2
invalid JSON, direct-process attribution, and provenance. FR-8 and FR-10 through
FR-13 at `prd.md:249-303` still point only to provider-local stories whose ACs
do not accept those complete consequences.

### F-R4-03 — Reconciliation consequence gate is not the registered FR owner

The C-22/Story 4.10 aggregate now names confidence, coexistence, explanatory
evidence, policy fields, safety separation, and history. FR-18 through FR-25 at
`prd.md:364-438` still traverse only Stories 4.1 through 4.5, leaving the R3
explanatory-payload residuals outside their reciprocal edges.

### F-R4-04 — Navigation consequence gate is not the registered FR owner

Story 5.9 now acceptance-tests the C-22 morning/navigation path, but FR-27
through FR-32 at `prd.md:456-518` do not map to Story 5.9. Retention,
baseline/window/drill-down detail, Stack inspection, `--fzf-lines` removal,
nonblocking refresh, and unmatched-item inspection therefore remain owned only
outside the affected FR edges.

### F-R4-05 — Action and release consequence gates are not the registered FR owners

FR-36, FR-39, FR-41, and FR-42 at `prd.md:549-628` retain the R3 owner graph.
The complete plan, refresh/navigation isolation, raw-mode prompt prohibition,
installed version/compatibility output, and activation-after-checks assertions
exist in aggregate or downstream stories that those FRs cannot reach.

### F-R4-06 — Cross-cutting NFR gate has no cross-cutting ownership edges

Contract C-22 states that all NFRs are exercised across all owning subsystem
gates, but the R3-to-R4 graph has zero NFR changes. The clearest counterexample
remains NFR-13 at `prd.md:750-753`: only Story 1.10 owns it, while its AC covers
the foundation registry rather than deterministic fixtures, fakes, goldens,
and terminal backends for every later product domain.

### F-R4-07 — Five journey owners remain mid-flow

C-22's global sentence does not change journey ownership. UJ-1 through UJ-5 at
`prd.md:52-94` retain one mid-flow owner apiece. Story 2.6 is the strongest new
case, but its AC still does not execute UJ-2's launch, Heartbeat-to-healthy
reconciliation, and full release/expiry resolution.

### F-R4-08 — Foundation and IA semantic mismatches remain reciprocal

The aggregate UX golden story is not registered to the affected IDs.
`UX-FND-3` at `EXPERIENCE.md:36-40` remains mapped to canonical-encoding Story
1.4, while `UX-IA-2` at `EXPERIENCE.md:68` remains mapped to responsive-layout
Story 5.2. `UX-IA-10` still maps only to Agent Story 2.6 although it binds Agent,
strict collection, output, and action commands.

### F-R4-09 — Voice and component semantics remain outside their owner edges

Story 5.9's new “every voice/detail row” assertion is not reachable from any
`UX-VT-*` mapping. The four voice contracts at `EXPERIENCE.md:140-169` retain
their narrower owners. `UX-CP-14` at `EXPERIENCE.md:189` still points to Story
4.3, whose duplicate-set AC does not accept every marker and coexistence state.

### F-R4-10 — State and interaction semantics remain outside their owner edges

The C-22 navigation/action gates cover the missing transitions, but the
affected IDs do not map to those gates. The residual includes `UX-ST-7/12/14/15/16`
at `EXPERIENCE.md:205-214`, the full plan-to-outcome `UX-IP-7` at line 356, and
the human-linear operator path `UX-IP-11` at line 412.

### F-R4-11 — Assistive linear ownership remains incomplete

The new Story 6.12 edges and explicit budgets close the R3 budget defect and
strengthen core keyboard/modal coverage. `UX-A11Y-3`, however, still maps only
to Story 6.11. That story accepts action parity, not the complete ordinary-text
Brief, inspection, and exact UX-IP-11 command sequence required by
`EXPERIENCE.md:472-475`.

### F-R4-12 — Foundation technical seams remain prose-only

The addendum requires a hexagonal core, complete Elm-style shell, explicit
Strategy/Adapter/Command seams, and format/lint/locked/MSRV/current-stable gates
before Provider work (`addendum.md:14-28`). C-22 repeats those obligations, but
no numbered foundation AC invokes that contract or enumerates the complete
seams. The four R3 addendum gaps remain outside acceptance ownership.

### F-R4-13 — Aggregate prose does not complete semantic decomposition

The repair centralizes many requirements in six aggregate gates without adding
their reciprocal ownership edges. This preserves the exact defect R3 warned
about: registry traversal and acceptance traversal disagree. It also leaves
Epic 1 technical-horizontal and Stories 6.12 and 7.15 as broad multi-subsystem
gates rather than independently assignable user-value slices.

## Script evidence

| Command/check | Result |
| --- | --- |
| Requested SHA-256 | PASS: exact `8debf05b...bd4` |
| Registry counts, uniqueness, and reciprocity parser | PASS: 213 IDs, 73 stories, 146 ACs, 82 unique AD-11 rows |
| R3-to-R4 FR/NFR/UJ/UX edge diff | FAIL semantic closure: zero FR/NFR/UJ changes; four UX additions only |
| Frozen compatibility replay | PASS: Provider, output, CLI, inspection, action, source-pin, immutable-hash, and AD-9 checks |
| Planning quarantine | Exit 1: `planning-root tombstone does not fail closed` |
| Architecture aggregate | Exit 1 only after compatibility PASS, at the same quarantine assertion |
| `git diff --check HEAD^ HEAD -- .../epics.md` | PASS |
| Review worktree whitespace | PASS before report creation |

## Final assessment

The artifact now contains enough prose to identify how the R3 gaps should be
tested, and it repairs the AD-11 count contradiction. It does not make those
tests the reciprocal semantic owners of the FR/NFR/UJ/UX requirements they are
intended to close. The artifact remains correctly marked `remediated-draft`,
`assignable: false`, and `implementationAuthority: false`.

**Final verdict: FAIL — 13 findings. PASS is permitted only at zero.**
