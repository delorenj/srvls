---
title: Epic Product Traceability Review R5
project: srvls
review_date: 2026-07-17
review_type: independent-product-traceability-r5
target_path: _bmad-output/planning-artifacts/epics.md
expected_sha256: 7d749899972903b90c76df2825bfbfaf0055e0f83544cd72cb7d648af8ad645c
actual_sha256: 7d749899972903b90c76df2825bfbfaf0055e0f83544cd72cb7d648af8ad645c
digest_gate: PASS
verdict: FAIL
findingCount: 13
r4FindingCountAudited: 33
completionStatus: complete
---

# Epic Product Traceability Review R5

## Verdict

**FAIL — 13 findings. PASS requires zero.**

The requested digest is exact. Batch 4 repairs the mechanical registry, the
aggregate validator, the architecture-native result vocabulary, most release
story boundaries, and the FR/NFR/UJ aggregate-owner graph. It does not close
product traceability. Several UX requirements are still registered only to
narrow stories whose numbered criteria do not accept their complete source
semantics, while the aggregate stories that claim to test those semantics are
not reciprocal owners. Two release stories still name new installed-prior
oracles in Validation Expectations but consume the old FirstInstall authorities
in their normative acceptance criteria. The artifact also records a decisive
user authority that has no independently discoverable source.

All 33 findings from the three R4 reports were replayed. All 12 architecture R4
findings close. The product and story-quality reviews retain concrete residuals
listed below. The artifact is correctly still `remediated-draft`,
`assignable: false`, and `implementationAuthority: false`.

## Digest and audited sources

```text
$ sha256sum _bmad-output/planning-artifacts/epics.md
7d749899972903b90c76df2825bfbfaf0055e0f83544cd72cb7d648af8ad645c  _bmad-output/planning-artifacts/epics.md
```

The target is the committed `epics.md` blob at `a01028a`. This review read the
complete canonical PRD and addendum, canonical `DESIGN.md` and `EXPERIENCE.md`,
the complete architecture spine, all 73 story bodies, the complete normative
registry and AD-11 matrix, and all three R4 reports:

- Product traceability R4: 13 findings.
- Architecture divergence R4: 12 findings.
- Story quality and dependencies R4: 8 findings.

## Method

1. Verified the requested digest and committed target before judging content.
2. Replayed each of the 33 R4 findings against the current contracts, story
   boundaries, mappings, numbered criteria, fixture authorities, and validators.
3. Parsed the normative JSON independently and checked every inventory key,
   story key, reciprocal edge, story-prose mapping, AD-11 row, row owner, field,
   and declared count.
4. Compared the complete R4 and R5 edge sets rather than treating added Contract
   C-22 prose as ownership. The target adds 62 total edges: 38 FR, 19 NFR, four
   UJ, and one AD-11 edge; it adds no UX or screen-reader edge.
5. Traversed every FR, NFR, UJ, UX, and SR-A11Y source ID through its registered
   owner criteria and checked whether the full source consequence is accepted.
6. Re-read the complete action, Provider, release, state, component, voice,
   accessibility, responsive, and command matrices for contradictions between
   source row, contract row, story boundary, fixture authority, and registry.
7. Executed the planning-quarantine and aggregate architecture validators and
   checked the Batch 4 diff for whitespace errors.

## Exhaustive mechanical and semantic matrix evidence

| Surface | Declared/source | Parsed | Result |
| --- | ---: | ---: | --- |
| Epics | 7 | 7 | PASS |
| Stories | 73 | 73 unique | PASS |
| Numbered GWT criteria | 146 | exactly two per story | PASS |
| Functional requirements | 43 | 43 inventory/coverage keys; 150 edges | PASS mechanical |
| Non-functional requirements | 16 | 16 inventory/coverage keys; 35 edges | PASS mechanical |
| User journeys | 6 | 6 inventory/coverage keys; 10 edges | PASS mechanical |
| UX core excluding accessibility | 83 | 83 unique inventory/coverage keys | PASS mechanical |
| UX accessibility | 5 | 5 unique inventory/coverage keys | PASS mechanical |
| Screen-reader scenarios | 1 | 1 inventory/coverage key | PASS mechanical |
| Product edges, including SR-A11Y | 288 | 288 reciprocal edges | PASS mechanical |
| All registered IDs | 213 | 213 unique inventory and coverage keys | PASS |
| All story/requirement edges | 456 | 456 reciprocal; zero directional differences | PASS |
| Story prose versus registry | 456 | zero missing or extra edges | PASS |
| AD-11 rows | 84 | 84 unique; all six fields present | PASS |
| AD-11 row-owner reciprocity | 62 unique owners | zero missing in either direction | PASS |
| Semantic owner closure | zero findings permitted | 13 findings | **FAIL** |

The registry is internally exact. The failure is that reciprocal graph
agreement does not prove that a registered owner's criteria accept the complete
source row.

## R4-to-R5 ownership delta

Batch 4 adds 61 product edges and no product edge removals:

| Gate story | Added product ownership |
| --- | --- |
| Story 2.6 | FR-1 through FR-6; NFR-10 |
| Story 3.11 | FR-8 through FR-13, FR-16, FR-17; NFR-2 through NFR-5 |
| Story 4.10 | FR-18 through FR-25, FR-27, FR-28; NFR-1; UJ-3; UJ-5 |
| Story 5.9 | FR-27 through FR-33; NFR-6, NFR-8, NFR-13, NFR-14; UJ-1 |
| Story 6.12 | FR-35 through FR-39, FR-41; NFR-5, NFR-7, NFR-8, NFR-12, NFR-13; UJ-4 |
| Story 7.15 | FR-42; NFR-9, NFR-11, NFR-15, NFR-16 |

These additions close the R4 FR, NFR, and journey reachability findings. The
zero-edge UX delta is controlling for R5-06 through R5-11: Contract C-22 and
Stories 5.9/6.12 assert complete UX gates, but the affected UX requirements
still traverse only to narrower local criteria.

## Complete R4 finding disposition

### Product traceability R4

| R4 finding | R5 disposition | Current evidence |
| --- | --- | --- |
| F-R4-01 Agent consequences | Closed | Story 2.6 now reciprocally owns FR-1 through FR-7 and its AC1 executes the complete lifecycle consequences. |
| F-R4-02 Provider consequences | Closed | Story 3.11 now reciprocally owns FR-8 through FR-17 and the affected Provider NFRs. |
| F-R4-03 Reconciliation consequences | Closed | Story 4.10 now owns the affected FRs, NFR-1, UJ-3, and UJ-5. |
| F-R4-04 Navigation consequences | Closed | Story 5.9 now owns FR-27 through FR-34 and UJ-1. |
| F-R4-05 Action/release consequences | Closed | Story 6.12 now owns FR-35 through FR-41 and Story 7.15 owns FR-42. |
| F-R4-06 Cross-cutting NFR ownership | Closed | Nineteen subsystem-gate NFR edges were added and are reciprocal. |
| F-R4-07 Mid-flow journeys | Closed | UJ-1, UJ-3, UJ-4, and UJ-5 gained end-to-end gate owners; UJ-2 and UJ-6 already had them. |
| F-R4-08 Foundation and IA semantics | **Open** | R5-06 and R5-07. |
| F-R4-09 Voice and component semantics | **Open** | R5-08 and R5-09. |
| F-R4-10 State and interaction semantics | **Open, narrowed** | Local state criteria improved, but UX-IP-7 remains unreachable from the complete action gate; R5-10. |
| F-R4-11 Assistive linear ownership | **Open** | UX-A11Y-3 still reaches only action parity; R5-11. |
| F-R4-12 Foundation technical seams | **Open** | The complete addendum seam/tooling contract is still outside numbered acceptance ownership; R5-12. |
| F-R4-13 Semantic decomposition | **Open** | Aggregate gates remain broad multi-subsystem acceptance owners; R5-13. |

### Architecture divergence R4

| R4 finding | R5 disposition | Current evidence |
| --- | --- | --- |
| R4-01 red aggregate | Closed | `bash tests/validate_architecture_contracts.sh` passes all lanes. |
| R4-02 Story 1.10 AD-11 reciprocity | Closed | AD11-FUT-69 is owned by Story 1.10 and reciprocal. |
| R4-03 override contradiction | Closed | Story 1.10 AC2 now passes the active override when canonical discovery and archive quarantine hold. |
| R4-04 universal foreign result | Closed | Generic negative criteria now reject implementations in the owning test instead of inventing a runtime result. |
| R4-05 FD3 normalization | Closed | Story 3.3 AC2 uses AD-25 precedence and typed CollectorReport outcomes. |
| R4-06 cron partial/denied | Closed | Story 3.4 preserves Contract C-16 partial, denied, and invalid-output results. |
| R4-07 systemd scoped failures | Closed | Story 3.5 preserves distinct scoped architecture-native results. |
| R4-08 process cleanup model | Closed | Story 3.8 preserves distinct identity and synthesized worker-timeout behavior. |
| R4-09 dual oracle/foreign Provider result | Closed | Story 6.7 names both fixture families and uses architecture-native result classes. |
| R4-10 action revalidation/verification results | Closed | Stories 6.4 and 6.9 use the five AD-6 outcomes and exact reasons. |
| R4-11 duplicate/expired admission | Closed | Story 6.6 uses refused/duplicate-operation and refused/plan-expired. |
| R4-12 recovery terminal ownership | Closed | Story 7.9 now ends only in the two installed-prior pre-decision terminal results and excludes KnownGood/FirstInstall. |

### Story quality and dependencies R4

| R4 finding | R5 disposition | Current evidence |
| --- | --- | --- |
| R4-01 unspecified future corpora | **Open, narrowed** | The temporal rule improved, but rows and expected values remain undefined; R5-02. |
| R4-02 path override contradiction | Closed | Story 1.10 AC2 and the live validator agree. |
| R4-03 reversed authority | **Open, changed** | General precedence is restored, but the decisive replacement authority is not independently traceable; R5-01. |
| R4-04 release command matrix | Closed | Contract C-19 now defines required/optional/forbidden argv, confirmation, result, and exit per verb. |
| R4-05 Story 7.9 scope crossing | Closed | Its boundary, validation authority, and AC1 now agree on installed-prior pre-decision recovery. |
| R4-06 Stories 7.8/7.10 FirstInstall authorities | **Open** | Validation Expectations changed, but their AC1 authorities did not; R5-03 and R5-04. |
| R4-07 forbidden consumer manifest | **Open, narrowed** | Story title/value/boundary are corrected; AC2 still names a manifest; R5-05. |
| R4-08 missing Action Menu noun | Closed | Story 6.2 explicitly owns the Action Menu and emits only an action-selection value. |

## Findings

### F-R5-01 — The decisive post-source user authority is not traceable

The artifact now restores PRD/addendum/UX/architecture precedence, but then
uses `UD-EPIC-C-1` to select FR-6 rejection and the duplicate set/cardinality
rule (`epics.md:33-38`). That identifier occurs nowhere else in the repository:
no checkpoint artifact, decision record, task entry, source digest, date, or
quoted approval makes the claimed user decision independently auditable. A
statement inside the lower artifact cannot be its own proof that it received
authority to resolve two higher-source alternatives. Story R4-03 therefore
changed form rather than closed.

### F-R5-02 — Future acceptance corpora remain authorable by the implementation story

The repeated repair says each story “begins by checking in” fixture rows and
expected bytes “for independent review before production implementation”
(representative `epics.md:2287-2296`). It still does not identify the required
row IDs, concrete inputs, expected bytes/results, independent producer, or an
approval dependency. Most future paths do not exist yet. The same assignee can
write a permissive corpus first, call that chronological independence, and then
implement to it. R4-01's self-fulfilling-oracle risk is narrowed but remains an
acceptance ambiguity across the future story corpus.

### F-R5-03 — Story 7.8 still consumes the FirstInstall forward authority

Story 7.8's Validation Expectations and AD11-FUT-70 name the new
`installed-prior-forward-v1` authority, and its boundary ends at the
pre-publication `commit-decided` handoff. AC1 still normatively invokes
`tests/fixtures/contracts/release-transaction-v1/forward.transitions.jsonl`
(`epics.md:3792-3811`). R4 parsed that corpus as FirstInstall-absent from
generation zero through committed. The changed registry row does not supersede
the story's numbered criterion. Story 7.8 still crosses Story 7.10 terminal
publication and Stories 7.11-7.12 FirstInstall ownership.

### F-R5-04 — Story 7.10 still consumes a FirstInstall KnownGood authority

Story 7.10 declares `installed-prior-known-good-v1`, excludes FirstInstall, and
owns post-decision publication through terminal commit. AC1 instead invokes
`known-good-publication-pending.manifest.json` (`epics.md:3838-3857`), whose R4
parse proved `prior_release.kind=first-install-absent`. The new future AD-11 row
and Validation Expectations path do not erase that explicit criterion input.
Story 7.10 still depends semantically on FirstInstall before Stories 7.11-7.12.

### F-R5-05 — Story 7.4 retains the forbidden manifest as an acceptance boundary

Contract C-21 permits only ordered unit-contract rows, pair authority,
transaction consumers, and hashes and expressly forbids
`ManagedConsumerManifestV1` (`epics.md:469-478`). Story 7.4's title, value, and
boundary now correctly use unit discovery, but AC2 still rejects preimage
capture that “precedes the manifest” (`epics.md:3700-3721`). There is no legal
manifest to precede. An implementer must either reintroduce the forbidden
aggregate or guess that “manifest” means the unit/pair discovery authority.

### F-R5-06 — UX-FND-3 remains registered to encoding instead of operation binding

UX-FND-3 requires every operation to bind canonical Promise/Observation
identity, captured Snapshot generation, resolved Provider-native operation,
and unique OperationId (`EXPERIENCE.md:36-40`). Its sole reciprocal owner is
Story 1.4, whose criteria accept CanonicalJsonV1 bytes, key order, identity
fields, and newline behavior. Story 1.4 does not accept action binding or an
OperationId. The action aggregate claims exact binding but has no UX-FND-3
edge, so a requirement traversal still terminates at the wrong semantic owner.

### F-R5-07 — UX-IA-2 and UX-IA-10 remain narrower than their source rows

UX-IA-2 owns attention-first Explorer hierarchy, deterministic Stack and
Ungrouped, and Project/Agent/Provider/finding refinement (`EXPERIENCE.md:68,78-94`).
Its only owner, Story 5.2, acceptance-tests geometry and resize behavior
(`epics.md:3164-3185`), not that hierarchy. UX-IA-10 covers Promise, query,
renewal, release, strict collection, output, and action command results
(`EXPERIENCE.md:76`), but its sole owner remains Agent-only Story 2.6. The
release, collection, output, and action result surfaces are unreachable from
the UX-IA-10 edge.

### F-R5-08 — Voice contracts are not accepted by their registered owners

UX-VT-1/2 require calm accountable copy and the exact canonical vocabulary;
UX-VT-3/4 require provenance/time copy plus reason, diagnostic, next step, and
safe retry rules for every non-success (`EXPERIENCE.md:140-168`). Their owners
remain Stories 5.7 and 5.8. Those criteria accept accessibility/hostile-text and
help/config behavior (`epics.md:3278-3322`), not the complete voice matrices.
Story 5.9 AC1 claims every voice row matches goldens (`epics.md:3340-3343`) but
no UX-VT edge points to Story 5.9. Registry traversal and acceptance traversal
therefore still disagree.

### F-R5-09 — UX-CP-14 still lacks a complete component owner

UX-CP-14 requires every applicable finding marker as text or ASCII, label
coexistence, and no implication of action safety (`EXPERIENCE.md:189`). Its sole
owner remains Story 4.3, which accepts duplicate membership and excess
cardinality, not every finding marker or the complete coexistence/safety
matrix. Story 5.9 says every component row matches immutable goldens but has no
UX-CP-14 edge. The complete component matrix is asserted outside its reciprocal
owner graph.

### F-R5-10 — UX-IP-7 still maps only to the middle of its seven-step lifecycle

UX-IP-7 specifies Plan, Confirm, Pending, Revalidate, Execute, Verify, and
Outcome (`EXPERIENCE.md:356-374`). Its sole owner is Story 6.8, whose boundary
and criteria cover operation-status phase projection and navigation only
(`epics.md:3512-3533`). Story 6.12 AC1 now executes the complete plan-to-outcome
journey (`epics.md:3604-3625`), but UX-IP-7 does not map to it. The registered
owner can pass while six of seven required lifecycle stages are absent.

### F-R5-11 — UX-A11Y-3 still omits the Brief and inspect linear alternative

UX-A11Y-3 requires `brief --linear` and the complete six-command UX-IP-11 path,
including Brief, facets, inspection, plan, execute, and status
(`EXPERIENCE.md:412-480`). Its only owner remains Story 6.11, whose criteria
accept action plan/execute/status parity but not Brief, facets, or inspect
(`epics.md:3581-3602`). Story 6.12 runs the complete linear journey but does not
own UX-A11Y-3. The R4 assistive ownership defect remains unchanged.

### F-R5-12 — The foundation gate still does not acceptance-test the complete addendum

The addendum requires format, lint, locked tests, both toolchains, a hexagonal
core, a complete Elm model/message/update/view/effect shell, and explicit
Strategy/Adapter/Command seams before Provider implementation
(`addendum.md:14-28`). Contract C-22 repeats that gate (`epics.md:498-501`).
Story 1.1 names some bootstrap/toolchain/boundary work but its criteria test only
the prescribed dependency graph and two forbidden imports/effects
(`epics.md:2280-2296`). Story 1.10 tests registry discovery and planning
quarantine, not format, lint, Elm, or all three named seams
(`epics.md:2482-2503`). The mandatory foundation correction remains prose-only.

### F-R5-13 — Aggregate gates remain non-assignable semantic catch-alls

Batch 4 closes many FR/NFR/UJ reachability gaps by adding them to Stories 2.6,
3.11, 4.10, 5.9, 6.12, and 7.15. It does not decompose the gates into
independently assignable value slices. Story 5.9 owns retention, baseline,
refresh, Stack, unmatched detail, compatibility removal, every read-only
state/component/voice/detail golden, and performance budgets. Story 6.12 owns
the enum, matrix, plan, pool, admission, executor, status, outcome, shutdown,
parity, accessibility, responsiveness, and every action UX row. This centralizes
acceptance after implementation across multiple subsystems and preserves the
R4 concern that passing a narrow story does not close the user consequence.
The artifact's explicit nonassignable/non-authority status is therefore still
required (`epics.md:30-32`).

## Executable evidence

| Check | Result |
| --- | --- |
| Requested SHA-256 | PASS: exact `7d749899...645c` |
| Registry parser | PASS: 213 IDs, 73 stories, 456 reciprocal edges, 146 ACs |
| Product matrix | PASS mechanical: 288 reciprocal product edges; FAIL semantic: findings above |
| AD-11 parser | PASS: 84 unique rows, complete fields, reciprocal owners |
| R4-to-R5 edge diff | 62 additions, zero removals; no UX/SR-A11Y change |
| `python3 tests/validate_planning_quarantine.py` | PASS |
| `bash tests/validate_architecture_contracts.sh` | PASS, including compatibility, quarantine, contract, release, and Host smoke lanes |
| `git diff --check 30ce86d..a01028a -- epics.md validator` | PASS |
| R4 replay | FAIL: product and story-quality residuals remain |

## Final assessment

Batch 4 is a substantial mechanical and architecture correction. It does not
reach the zero-finding product threshold. The next remediation must record the
actual source of `UD-EPIC-C-1`, make future oracle rows independently closed,
align Stories 7.8/7.10 with their declared installed-prior authorities, remove
the last forbidden-manifest wording, and make every affected UX requirement
reach the story that actually acceptance-tests its full source semantics. The
aggregate gates then need assignable decomposition or an explicit, enforceable
integration-story model that does not pretend the narrow stories independently
close those consequences.

**Final verdict: FAIL — 13 findings. PASS is prohibited above zero.**
