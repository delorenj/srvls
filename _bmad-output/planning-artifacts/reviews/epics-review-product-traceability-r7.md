---
project: srvls
review_date: 2026-07-17
review_type: independent-product-traceability-r7
target_commit: b13fc14bcd6ceb8ec590e3681b9694dcc78c3b7c
target_path: _bmad-output/planning-artifacts/epics.md
actual_sha256: 6e993c009d9378de2037ed91934c8b999800d629eadde426ac63c770b836bda7
digest_gate: PASS
verdict: FAIL
findingCount: 18
priorClaimedFindingCountAudited: 61
completionStatus: complete
---

# Epic Product Traceability Review R7

## Verdict

**FAIL — 18 findings. PASS requires zero.**

The current artifact is mechanically exact but semantically incomplete. Its
registry contains all canonical FR, NFR, UJ, UX, accessibility, architecture,
limit, host-profile, and supplemental IDs; every edge is reciprocal; story
prose agrees with the registry; and all repository validators pass. Those
checks do not prove that an owning story's two numbered criteria accept the
complete source meaning.

The full semantic replay finds incomplete journey outcomes, cross-cutting NFRs
owned only by narrow subsystems, UX requirements mapped to data producers or
isolated states instead of their required interactions, incomplete visual-spine
reciprocity, and an acceptance-approval gate that still does not verify its
claimed hashes or implementation dependency. The batch-6 narrowing of Story
6.12 also creates a direct SR-A11Y-1 regression: the sole owner expressly avoids
executing the journey that SR-A11Y-1 requires.

The artifact is correctly still `remediated-draft`, `assignable: false`, and
`implementationAuthority: false` (`epics.md:1-5,30-32`).

## Scope and method

This review read the complete current `epics.md`, PRD, addendum, `DESIGN.md`,
`EXPERIENCE.md`, architecture spine, all five product-traceability reports,
both remediation ledgers, the user-decision record, current story-quality R6,
the normative JSON registry, and the current validators.

The audit:

1. pinned the target commit and SHA-256 before evaluating content;
2. independently enumerated all source FR, NFR, UJ, UX, and accessibility IDs;
3. parsed both registry directions and every story Requirement Mapping;
4. followed each source requirement through every registered owner to its two
   numbered Given/When/Then criteria;
5. rejected tags, boundaries, contracts, future fixtures, and validator names
   as semantic proof when the owning criterion did not observe the source
   consequence;
6. replayed every claimed finding from the initial review through R5 and the
   R6 story-quality findings that affect product acceptance; and
7. ran the repository's planning, approval, compatibility, contract, release,
   and Host-smoke validators.

## Mechanical coverage and executable evidence

| Surface | Source/declaration | Current parse | Result |
| --- | ---: | ---: | --- |
| Epics | 7 | 7 | PASS |
| Stories | 75 | 75 unique | PASS |
| Numbered GWT criteria | 150 | 150 | PASS |
| Functional requirements | 43 | 43 IDs; 150 edges | PASS mechanical |
| Non-functional requirements | 16 | 16 IDs; 35 edges | PASS mechanical |
| User journeys | 6 | 6 IDs; 10 edges | PASS mechanical |
| UX core excluding accessibility | 83 | 83 IDs | PASS mechanical |
| UX accessibility | 5 | 5 IDs | PASS mechanical |
| Screen-reader scenarios | 1 | 1 ID | PASS mechanical |
| Product edges including SR-A11Y | 309 | 309 reciprocal | PASS mechanical |
| All registered IDs | 213 | 213 unique | PASS |
| All story/requirement edges | 480 | 480 reciprocal | PASS |
| Story prose versus registry | 480 | zero directional differences | PASS |
| AD-11 rows | 87 | 87 unique; valid owners | PASS mechanical |
| Semantic owner closure | zero findings permitted | 18 findings | **FAIL** |

| Executable check | Result |
| --- | --- |
| `sha256sum epics.md` | PASS: `6e993c009d...a7` |
| Source inventory versus registry | PASS: zero missing, extra, or invented IDs |
| Registry directionality | PASS: zero differences |
| `python3 tests/validate_planning_quarantine.py` | PASS |
| `python3 tests/validate_story_fixture_approvals.py` | PASS only in no-story discovery mode |
| `bash tests/validate_architecture_contracts.sh` | PASS, including compatibility, contract, release, and Host smoke |

## Complete prior-finding audit

The five earlier product reports claim 61 findings: 8 in the initial
frontmatter, then 13, 14, 13, and 13. The initial body exposes only seven named
findings; that historical accounting defect is retained rather than silently
inventing an eighth title.

### Initial-review disposition

| Prior finding | R7 disposition | Current evidence |
| --- | --- | --- |
| F-REQ-1 | Closed | All 43 FR IDs and their direct consequences have reciprocal semantic owners. Current residuals are UJ, NFR, and UX contracts, not a missing direct FR owner. |
| F-UX-1 baseline TUI | **Open** | R7-08. The sole mapped owner is noninteractive while the actual adapter is unmapped. |
| F-UX-2 incorrect action-state edges | Closed | Action state IDs now reach the relevant stage owners and the Story 6.13 integration path. |
| F-UX-3 external-system boundary | Closed | Story 5.5 affirmatively accepts Plane/Git/Telemetry display-only semantics and rejects their use as runtime authority. |
| F-QUAL-1 enabling Epic 1 | Closed at product-traceability altitude | Epic 1 now delivers an operator-visible compatibility and architecture preflight; it remains an intentional enabling epic. |
| F-QUAL-2 aggregate-sized stories | **Partially open** | The navigation/action gates were split, but semantic aggregate claims still overstate UJ/NFR/UX ownership; R7-01 through R7-04 and R7-17. |
| F-QUAL-3 pre-seeded later state | Closed | Story 1.7 is aggregate-neutral and explicitly excludes later Promise, Snapshot, action, baseline, and release schemas. |
| Unnamed eighth initial finding | Historical source defect | The initial body has seven titled findings despite `findingCount: 8`; no fabricated disposition is added. |

### R2/R3/R4 lineage disposition

R2 and R3 restated the same principal semantic families; R4 converted them to
reciprocal-owner findings. This table accounts for every R2, R3, and R4 ID.

| Lineage | R7 disposition |
| --- | --- |
| F-R2-01 / F-R3-01 / F-R4-01 Agent FR consequences | Closed for FRs; UJ-2 remains incomplete under R7-01. |
| F-R2-02 / F-R3-02 / F-R4-02 Provider consequences | Closed for direct FRs; cross-cutting failure/safety NFRs remain under R7-03. |
| F-R2-03 / F-R3-03 / F-R4-03 reconciliation consequences | Closed for direct FRs; UJ-3/UJ-5 action resolutions remain under R7-02. |
| F-R2-04 / F-R3-04 / F-R4-04 navigation consequences | Closed for direct FRs by Story 5.10; UX reciprocity remains under R7-06 through R7-09 and R7-17. |
| F-R2-05 / F-R3-05 / F-R4-05 action/release consequences | Closed for direct FRs by Stories 6.13 and 7.15; generic machine/install UX remains under R7-12 and R7-13. |
| F-R2-06 / F-R3-06 / F-R4-06 cross-cutting NFRs | **Open/regressed** as R7-03 and R7-04. Registry additions still do not reach all source subsystems. |
| F-R2-07 / F-R3-07 / F-R4-07 journeys | **Open** as R7-01 and R7-02. UJ-2, UJ-3, and UJ-5 still stop before required outcomes. |
| F-R2-08 / F-R3-08 / F-R4-08 foundation/IA | **Open, narrowed** as R7-05 through R7-09. UX-FND-3 and UX-IA-10 close; other semantic mismatches remain. |
| F-R2-09 / F-R3-09 / F-R4-09 voice/components | Voice and UX-CP-14 close; provider-detail, machine/install components, and DESIGN visual ownership remain under R7-07, R7-12, R7-13, and R7-18. |
| F-R2-10 / F-R3-10 / F-R4-10 state/interactions | UX-IP-7 closes; baseline, config, machine, install, and linear paths remain under R7-08 through R7-13 and R7-17. |
| F-R2-11 / F-R3-11 / F-R4-11 accessibility/budgets | Budgets close; keyboard, restoration, linear, and screen-reader coverage remain under R7-14 through R7-17. |
| F-R2-12 / F-R3-12 / F-R4-12 addendum seams | Closed. Story 1.1 directly accepts format, lint, both toolchains, hexagonal direction, Elm isolation, and Strategy/Adapter/Command seams. |
| F-R2-13 / F-R3-13 / F-R4-13 overstatement/decomposition | **Partially open** through the semantic aggregates in R7-01 through R7-04 and R7-17. |
| F-R3-14 AD-11 count | Closed: 87 declared and 87 unique. |

### R5 disposition

| R5 finding | R7 disposition |
| --- | --- |
| F-R5-01 user-decision authority | Closed by the separate accepted `UD-EPIC-C-1` decision record and source pins. |
| F-R5-02 future acceptance corpora | **Open, narrowed** as R7-05. C-23 exists and is invoked by sprint planning, but its validator does not prove the recorded hashes or explicit implementation dependency. |
| F-R5-03 Story 7.8 FirstInstall authority | Closed. Story 7.8 now names and consumes `installed-prior-forward-v1`. |
| F-R5-04 Story 7.10 FirstInstall authority | Closed. Story 7.10 now names and consumes `installed-prior-known-good-v1`. |
| F-R5-05 forbidden consumer manifest | Closed. Story 7.4 uses ordered unit-contract and pair readback. |
| F-R5-06 UX-FND-3 operation binding | Closed by Stories 6.6 and 6.13 in addition to encoding ownership. |
| F-R5-07 UX-IA-2/UX-IA-10 | **Half open.** UX-IA-10 closes; UX-IA-2 remains R7-09. |
| F-R5-08 voice contracts | Closed by Story 5.9 approved-byte voice goldens. |
| F-R5-09 UX-CP-14 | Closed by Story 5.9 finding-marker goldens. |
| F-R5-10 UX-IP-7 | Closed by stage-owner fanout plus Story 6.13. |
| F-R5-11 UX-A11Y-3 | **Open/regressed** as R7-17 together with UX-IP-11 and SR-A11Y-1. |
| F-R5-12 foundation addendum | Closed by Story 1.1. |
| F-R5-13 semantic catch-alls | **Partially open** through R7-01 through R7-04 and R7-17. |

## Findings

### F-R7-01 — UJ-2 never launches or reaches healthy reconciliation

UJ-2 requires declaration, returned Promise ID and Lease, actual Runtime launch,
Heartbeats, healthy Promise/Observation reconciliation, release or expiry, and
abandoned-survivor behavior (`prd.md:61-68`). Its sole owner is Story 2.6. That
story accepts declare/revise/renew/close/query, retry, expiry, revocation, and
abandoned projection, but never launches a Runtime or reaches healthy
reconciliation (`epics.md:2726-2741`). Contract C-22's assertion that every UJ
executes entry through resolution is therefore not realized.

### F-R7-02 — UJ-3 and UJ-5 stop before their required resolutions

UJ-3 resolves by starting the exact supported resource through the Action Menu
or returning to the Project with evidence; UJ-5 resolves by acting on one exact
Observation or explicitly deferring for unknown safety (`prd.md:70-76,87-93`).
Their registry owners are only Stories 4.2/4.10 and 4.4/4.10. Story 4.10 accepts
reconciliation, grouping, and drill-down IDs and explicitly excludes mutation
(`epics.md:3216-3231`). Neither journey reaches Story 6.13 or a criterion that
accepts the complete alternative resolution.

### F-R7-03 — Four failure, command, machine, and concurrency NFRs are partial

NFR-2, NFR-4, NFR-7, and NFR-12 span Collector/storage/inspection/mutation
failure honesty, every Host command, every machine surface, and refresh/
Collector/action/write concurrency (`prd.md:706-716,726-728,746-748`). Their
owners cover only collection/inspection, the read-only runner, Agent/action
interfaces, and action admission/journey respectively (`epics.md:1355,1357,
1360,1365`). Storage/mutation failure, release commands, strict-collection and
general output/release machine surfaces, and refresh/late-Collector/concurrent-
write cases remain unreachable from the relevant requirement edge.

### F-R7-04 — Four durability, minimization, testability, and compatibility NFRs are partial

NFR-9, NFR-11, NFR-13, and NFR-14 bind concrete product aggregates,
permission/minimization/redaction, all subsystem testability, and the complete
live/deployed-consumer compatibility oracle (`prd.md:734-756`). Story 1.7 tests
only a generic aggregate and excludes the Promise/Snapshot/release aggregates;
Story 1.8 tests retention/capacity only; NFR-13's owners omit Agent lifecycle,
Collectors, correlation, and Lease behavior; and NFR-14 does not reach the
release gate that owns named deployed consumers and exact Prometheus families
(`epics.md:2515-2553,2584-2599,3449-3462,4091-4112`).

### F-R7-05 — C-23 approval does not verify the evidence it claims to gate

C-23 requires closed row IDs, approved fixture/result hashes, reviewer
independence, and an explicit pre-implementation dependency (`epics.md:503-514`).
Fourteen negative criteria do not name their `AC-*.N01` row in the criterion
body: Stories 1.10, 2.1, 2.3, 3.3, 3.4, 3.5, 3.8, 6.4, 6.6, 6.7, 6.9, 7.3,
7.4, and 7.12. The validator checks token presence, hash syntax, and reviewer/
fixture-author string inequality; it does not recompute either hash, prove a
pending implementer differs from the reviewer, or prove the approval commit is
an implementation dependency (`tests/validate_story_fixture_approvals.py:30-54`).
No-argument aggregate execution reports PASS without validating any story.

### F-R7-06 — UX-FND-2 collapses eight orthogonal axes to Promise outcomes

UX-FND-2 requires Promise Lifecycle, Evidence Status, Promise Outcome,
Observation labels, Safe-to-stop, Collection Obligation, Collector outcome, and
Action Outcome to remain orthogonal (`EXPERIENCE.md:22-34`). Its sole owner,
Story 4.2, accepts healthy/broken/unresolved/inactive and sufficient absence and
explicitly places Observation labels outside its boundary
(`epics.md:3027-3048`). Five source axes cannot be reached from the requirement.

### F-R7-07 — UX-FND-4 and UX-FND-5 terminate at domain classification

UX-FND-4 also requires persistent stale display, disabled actions, and refresh/
action generation isolation; UX-FND-5 also makes every Stack, Project, Agent,
and finding group read-only (`EXPERIENCE.md:42-50`). Their sole owners are Story
3.10 and Story 4.5, which accept incomplete-evidence reduction and label/no-
automatic-mutation behavior, not the presentation/action/group consequences
(`epics.md:2954-2975,3096-3117`).

### F-R7-08 — The Brief entry and exit contract is mapped to a non-TUI producer

UX-IA-1 requires eligible bare/TUI/fzf entry and `q` exit from the Brief
(`EXPERIENCE.md:67`). Its sole owner is Story 4.9, which materializes Brief
content and excludes grouping and TUI rendering (`epics.md:3187-3208`). Story
5.1 owns routing and terminal exit behavior but has no UX-IA-1 edge.

### F-R7-09 — UX-IA-2 still omits facet refinement

UX-IA-2 requires attention-first Explorer hierarchy plus Project, Agent,
Provider, and finding facets refining the same Stack/Ungrouped hierarchy
(`EXPERIENCE.md:68,78-94`). Its owners accept grouping/drill-down and geometry/
resize only (`epics.md:3216-3231,3260-3281`). Story 5.3 implements the facets
but does not own UX-IA-2 (`epics.md:3283-3304`).

### F-R7-10 — Provider/evidence detail UX maps to the data producer

UX-IA-4 and UX-CP-7 require Enter reachability, Esc return, bounded detail, and
Ctrl-F/n/N/PgUp/PgDn interaction (`EXPERIENCE.md:70,182`). Their sole owner,
Story 3.11, produces bounded sanitized detail and excludes TUI layout. Story 5.4
accepts the required keys and navigation but owns neither ID
(`epics.md:2977-3000,3306-3327`).

### F-R7-11 — Baseline dialog reciprocity remains broken

UX-IA-7, UX-CP-12, and UX-IP-6 require `b` entry, eligibility and Evidence
Window display, Cancel focus, Esc cancellation, typed `override`, pointer-only
mutation, and immediate recomputation (`EXPERIENCE.md:73,187,341-352`). All map
only to Story 4.8, whose boundary delegates the TUI key/modal/focus/Esc adapter
to Story 5.3 and whose criteria accept noninteractive baseline behavior
(`epics.md:3165-3185`). Story 5.3 describes the adapter only in its boundary and
owns none of the three IDs (`epics.md:3283-3304`).

### F-R7-12 — Configuration validation and recovery omit observable fields

UX-IA-12, UX-ST-18, and UX-IP-12 require the exact field/value/source/type/
range/precedence/default/correction envelope, successful `config explain`
provenance, and restart-only recovery (`EXPERIENCE.md:114-136,216,450-457`).
Story 5.8 observes one deterministic pre-side-effect error and rejects silent
clamping/hidden sources, but its criteria do not require the complete envelope,
successful explain output, or restart behavior (`epics.md:3397-3418`).

### F-R7-13 — Generic machine-result UX is narrowed to Agent or action slices

UX-IP-9 requires Promise lifecycle **and action** machine results with identity,
evidence, reason, retry correlation, and clean stderr separation; its sole owner
is Promise-only Story 2.6 (`EXPERIENCE.md:385-390`; `epics.md:2726-2741`).
UX-CP-15 requires generic human/machine canonical-field and outcome parity, but
its sole owner is action-only Story 6.11 (`EXPERIENCE.md:190`;
`epics.md:3698-3719`). Strict collection, general output, and release results
remain outside these edges.

### F-R7-14 — Install/recovery UX does not accept its phase rendering contract

UX-IA-9, UX-CP-16, and UX-IP-8 require persistent named phase lines,
stdout/stderr policy, no alternate screen, stop-on-failure, and explicit known-
good/rollback recovery copy (`EXPERIENCE.md:75,191,378-383`). Story 7.15 maps all
three but accepts installed version/compatibility output and activation checks,
not the phase rendering or recovery-copy contract (`epics.md:4091-4112`).

### F-R7-15 — UX-A11Y-2 does not cover every core journey

UX-A11Y-2 requires every core journey to be keyboard-only with matching reading
and Tab order, persistent focus, help access, and modal safeguards
(`EXPERIENCE.md:467-470`). Its only owners are navigation-focused Story 5.3 and
isolated action-state Story 6.12. The actual morning/action journey stories,
Stories 5.10 and 6.13, do not own it, and the Agent/release journeys have no
accessibility owner (`epics.md:1475,3443-3462,3721-3763`).

### F-R7-16 — UX-A11Y-5 omits terminal restoration and signal disposition

UX-A11Y-5 requires normal/error/panic/Ctrl-C/SIGINT/SIGTERM restoration plus
UX-IP-10 submitted-operation disposition (`EXPERIENCE.md:489-493`). Its owners,
Stories 5.7 and 6.12, accept semantic accessibility and isolated action states,
not exit/panic/signal restoration. The actual owners are Stories 5.1 and 6.10,
which have no UX-A11Y-5 edge (`epics.md:3237-3258,3374-3395,3675-3696,
3721-3742`).

### F-R7-17 — The full linear path and SR-A11Y-1 have no accepting owner

UX-IP-11 defines Brief, facets/query, inspect, plan, execute, and status;
UX-A11Y-3 requires that exact first-class human-linear alternative; SR-A11Y-1
runs all six steps under TERM=dumb/NO_COLOR across complete, incomplete,
destructive-confirmation, and all-outcome fixtures
(`EXPERIENCE.md:412-448,472-480`). UX-IP-11 reaches action-only Story 6.11;
UX-A11Y-3 reaches isolated-golden Story 5.9 and action-only Stories 6.11/6.13;
SR-A11Y-1 reaches only Story 6.12. Story 6.12 now explicitly renders isolated
states **without executing the complete action journey** (`epics.md:3739-3742`).
Story 5.10 owns the Brief/filter/inspect linear route but none of these IDs.

### F-R7-18 — The canonical DESIGN visual spine has no reciprocal row inventory

`DESIGN.md` expressly owns visual semantics, including exact text markers and
colors, collapse order, and component anatomy (`DESIGN.md:118-149,189-314`).
The normative registry inventories EXPERIENCE IDs only and has no addressable
DESIGN row. Story 5.9 says it renders every read-only component golden, but its
criterion accepts only “every mapped component/voice row,” and only UX-CP-14 is
mapped to Story 5.9 (`epics.md:516-697,3420-3441`). A missing focus prefix,
changed attention anatomy, broken collapse order, or hard-coded palette can
therefore regress without violating any source-row ownership edge.

## Final assessment

R7 confirms that the artifact's mechanical registry and architecture gates are
healthy. It does not accept the backlog as product-complete. A conforming team
can satisfy every reciprocal edge and all current repository validators while
omitting required journey endings, cross-subsystem NFR behavior, baseline and
detail interactions, complete machine/install UX, terminal restoration, the
full linear screen-reader route, and canonical visual-spine rules.

**Final verdict: FAIL — 18 findings. PASS is prohibited above zero.**
