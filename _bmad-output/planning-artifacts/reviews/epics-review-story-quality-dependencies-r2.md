---
type: epic-story-review
reviewer: SyntaxSorcerer
reviewedCommit: 8ebdc20e2ea08f5bb7529dad1bc1b2d90c50a705
reviewedArtifact: _bmad-output/planning-artifacts/epics.md
requiredSha256: b5368de55ada106282a2b623879feef5ceffea1a4dd0afd54870326aebb1ee27
observedSha256: b5368de55ada106282a2b623879feef5ceffea1a4dd0afd54870326aebb1ee27
verdict: FAIL
findingCount: 23
storyCount: 73
acceptanceCriterionCount: 146
declaredDependencyEdgeCount: 72
batch1FindingsClosed: 9
batch1FindingsOpenOrPartial: 9
---

<!-- markdownlint-disable MD013 -->

# Independent Batch 2 Story Quality and Dependency Review

## Verdict

**FAIL — 23 findings.**

The gate rule is PASS only when the finding count is zero. The reviewed blob
passes the digest, inventory, required-section, declared dependency, JSON
registry, current contract-corpus, release-oracle, and legacy-smoke checks. It
does not pass story quality and dependency closure. The exact-looking declared
chain conceals semantic forward edges and cycles, several stories have
overlapping or future ownership, and the acceptance suite is systematically
templated rather than fully deterministic.

## Frozen Artifact and Digest

| Check | Result |
| --- | --- |
| Reviewed commit | `8ebdc20e2ea08f5bb7529dad1bc1b2d90c50a705` |
| Commit subject | `docs: remediate canonical epics backlog batch 1` |
| Reviewed path | `_bmad-output/planning-artifacts/epics.md` |
| Required SHA-256 | `b5368de55ada106282a2b623879feef5ceffea1a4dd0afd54870326aebb1ee27` |
| SHA-256 from `git show` | `b5368de55ada106282a2b623879feef5ceffea1a4dd0afd54870326aebb1ee27` |
| SHA-256 from working tree | `b5368de55ada106282a2b623879feef5ceffea1a4dd0afd54870326aebb1ee27` |
| Git blob | `aa312adb9e741cde9c459aa8b491c42781344706` |
| Artifact size | 4,527 lines; 183,876 bytes |
| Digest disposition | **MATCH** |

The exact commit changes only `epics.md` and the Batch 1 remediation ledger.
No later working-tree variant was used to fill a gap in the reviewed story
text.

## Scope and Method

1. Pinned the review to commit `8ebdc20` and verified the Git blob stream and
   checked-out file against the required SHA-256.
2. Parsed all seven Epic headings and all 73 Story headings. Verified the
   exact inventory `1.1` through `7.15`, with per-Epic counts
   `10, 6, 11, 10, 9, 12, 15`.
3. Checked each Story for an As/I-want/So-that value statement,
   Implementation Boundary, Requirement Mapping, Dependencies, Validation
   Expectations, Out of Scope, and exactly two numbered GWT criteria.
4. Parsed the declared dependency graph. Story 1.1 alone says `None`; each of
   the other 72 Stories names exactly the immediately preceding Story ID.
5. Built a semantic prerequisite and ownership graph from values consumed or
   acceptance-owned by each Story. This catches later-owned types, UI paths,
   matrices, and validation authorities hidden by the declared linear chain.
6. Parsed the normative coverage JSON. Reconciled 73 Story inventory rows,
   73 `coverageByStory` rows, 213 requirement identifiers, inverse
   `requirementCoverage`, and 68 AD-11 ownership rows.
7. Reviewed C-04, C-05, C-06, and C-11 plus every Story that creates,
   projects, executes, verifies, or aggregates those contracts.
8. Compared the Story text against the declared precedence chain: final PRD,
   addendum, final UX spines, final architecture spine except the approved path
   override, then `epics.md`.
9. Reconciled every original Story-quality finding F-01 through F-18 against
   the live remediated blob and its higher-authority sources.
10. Ran the current validation authorities and isolated the acknowledged
    planning-quarantine stop from the remaining passing suites.
11. Performed a deletion check against the parent artifact. No identifier in
    the parent requirement inventory disappeared; the acceptance contraction
    risk is covered by Finding R2-01 rather than duplicated as a deletion-only
    finding.

## Structural Results

| Dimension | Result | Evidence |
| --- | --- | --- |
| Epic inventory | Pass | Seven unique Epic headings. |
| Story inventory | Pass | 73 unique, contiguous IDs in the normative registry and body. |
| User-value form | Pass structurally | Every Story has As/I-want/So-that text. |
| Required sections | Pass | Every Story has exactly one of all six required sections. |
| GWT cardinality | Pass structurally | 146 total; exactly two per Story; every criterion contains Given, When, Then, And tokens. |
| Declared dependency grammar | Pass | One exact prior Story ID per Story after 1.1; no ranges, Epic prose, future ID, or unresolved ID. |
| Declared dependency graph | Pass | 72 edges, one 73-Story chain, no declared cycle. |
| Semantic dependency graph | **Fail** | Findings R2-07, R2-11, R2-13, R2-15, R2-17, R2-20, and R2-21. |
| Exact duplicate titles/boundaries/value statements | Pass | None. |
| Split/duplicate implementation ownership | **Fail** | Findings R2-02, R2-12, R2-14, R2-17, R2-19, and R2-23. |
| Catch-all closure stories | **Fail** | Findings R2-01 and R2-15. |
| JSON coverage registry | Pass internally | Counts, keys, mappings, inverse mappings, and AD-11 owners reconcile exactly. |

### Hidden semantic cycles

| Earlier Story that consumes later authority | Later owner | Cycle created by the declared chain |
| --- | --- | --- |
| 3.1 freezes `DispatchScheduleV1` | 3.2 implements schedule compilation | 3.2 depends on 3.1 |
| 3.1 freezes obligation-bearing `ScopeManifestV1`; 3.9 freezes completeness | 3.10 compiles obligations/strict outcomes | 3.10 depends transitively on 3.1 and directly on 3.9 |
| 4.8 acceptance-owns TUI `b`, modal focus, and Esc | 5.1–5.3 implement TUI entry/layout/navigation | 5.1 depends transitively on 4.8 |
| 5.2, 5.3, 5.7 consume action-aware UX contracts | Epic 6 implements operation/confirmation behavior | Epic 6 depends on 5.9 and therefore all earlier Epic 5 Stories |
| 5.9 requires action budgets and `SR-A11Y-1` | 6.12 owns them | 6.12 depends on 5.9 |
| 6.7/6.12 require lock-owning action handoff | 7.2 owns POSIX admission and `ActionExecutorHandoffV1` | 7.2 depends on 6.12 |
| 7.8/7.9 require committed KnownGood terminalization | 7.10 owns KnownGood publication/recovery | 7.10 depends on 7.9 |
| 7.5–7.10 consume FirstInstall authorities | 7.11–7.12 own FirstInstall planning/execution | 7.11 depends on 7.10 |

## All-Story Accounting

Finding R2-01 applies to every Story. The table lists additional
Story-specific findings; `—` means no additional finding after the systemic
acceptance defect.

| Story | Additional finding IDs |
| --- | --- |
| 1.1 | — |
| 1.2 | — |
| 1.3 | — |
| 1.4 | — |
| 1.5 | — |
| 1.6 | — |
| 1.7 | R2-02 |
| 1.8 | — |
| 1.9 | — |
| 1.10 | R2-03 |
| 2.1 | R2-04 |
| 2.2 | R2-05 |
| 2.3 | R2-06 |
| 2.4 | — |
| 2.5 | — |
| 2.6 | — |
| 3.1 | R2-07 |
| 3.2 | R2-07 |
| 3.3 | — |
| 3.4 | — |
| 3.5 | — |
| 3.6 | — |
| 3.7 | — |
| 3.8 | — |
| 3.9 | R2-07 |
| 3.10 | R2-07, R2-08 |
| 3.11 | — |
| 4.1 | — |
| 4.2 | R2-09 |
| 4.3 | R2-10 |
| 4.4 | — |
| 4.5 | — |
| 4.6 | R2-10 |
| 4.7 | R2-02 |
| 4.8 | R2-11 |
| 4.9 | — |
| 4.10 | — |
| 5.1 | R2-12, R2-14 |
| 5.2 | R2-12, R2-13 |
| 5.3 | R2-13 |
| 5.4 | — |
| 5.5 | — |
| 5.6 | — |
| 5.7 | R2-13, R2-14 |
| 5.8 | — |
| 5.9 | R2-15 |
| 6.1 | — |
| 6.2 | — |
| 6.3 | — |
| 6.4 | R2-16 |
| 6.5 | — |
| 6.6 | R2-17 |
| 6.7 | R2-17 |
| 6.8 | R2-18 |
| 6.9 | — |
| 6.10 | R2-14 |
| 6.11 | — |
| 6.12 | R2-15, R2-17 |
| 7.1 | — |
| 7.2 | R2-17 |
| 7.3 | R2-23 |
| 7.4 | R2-19 |
| 7.5 | R2-21 |
| 7.6 | R2-19 |
| 7.7 | — |
| 7.8 | R2-20, R2-21 |
| 7.9 | R2-20, R2-21 |
| 7.10 | R2-20, R2-21 |
| 7.11 | R2-21, R2-22 |
| 7.12 | R2-21 |
| 7.13 | R2-22, R2-23 |
| 7.14 | — |
| 7.15 | R2-23 |

## Findings

The order follows the backlog and then cross-cutting dependency order. It is
not a severity or priority ranking.

1. **R2-01 — The 146 GWT criteria are structurally complete but use a
   backlog-wide catch-all template instead of deterministic scenarios.** Sixty-
   eight of 73 positive criteria say only `When the story capability is
   exercised`; all 73 negative criteria start from unspecified “fixed negative,
   boundary, race, and crash-cut fixtures for this story”; and 72 require “its
   exact typed result” without naming the result token, schema, or precedence
   row. Fifty-three named future oracle targets do not exist yet, as expected
   for implementation deliverables, so their unspecified future contents
   cannot presently disambiguate the Story. This permits an implementer to
   choose a narrower fixture set and still satisfy the prose. Examples are
   Stories 1.1–1.10 at `epics.md:2542-2810`, and the same templates continue
   through Story 7.15 at `4124-4527`. Replace catch-all fixture language with
   enumerated scenario rows and exact observable results, or cite exact closed
   source matrix rows for every branch.

2. **R2-02 — Story 1.7 duplicates concrete Snapshot/current-pointer ownership
   and pre-seeds later aggregate repositories.** Story 1.7 says Promise,
   policy, plan, operation, baseline, and Snapshot transactions are atomic and
   implements the “one current-generation gate” (`epics.md:2704-2729`). C-03
   and Story 4.7 say only Story 4.7 creates `SnapshotV1` and owns the current-
   pointer CAS (`60-69`, `3443-3468`). Narrow Story 1.7 to aggregate-neutral
   repository/CAS primitives and leave concrete plan, operation, baseline, and
   Snapshot transactions to their later owning Stories.

3. **R2-03 — Story 1.10 has a known-failing aggregate and an unowned external
   prerequisite.** The artifact says the approved path override keeps the
   quarantine validator red until separately revised (`epics.md:19-25`). Story
   1.10 owns the aggregate, excludes changing quarantine policy, and explicitly
   requires the active override to fail (`2785-2810`). The live command stops
   at `planning-root tombstone does not fail closed`. Assign the approved
   validator assertion change to this or an exact prior Story and require a
   green completion state, or name a resolvable external prerequisite before
   Story 1.10.

4. **R2-04 — Story 2.1 names an authentication contract without defining a
   testable trust boundary.** It does not specify how the local principal is
   derived, what credential proves an Agent ID, how Owner binds to it, or exact
   rotation/replay rules (`epics.md:2816-2841`). Mapped AD-15 defines privilege
   and environment handling, not Agent authentication
   (`ARCHITECTURE-SPINE.md:1082-1101`); the PRD defines Agent IDs as supplied
   and remote authentication as out of scope (`prd.md:107`, `657-670`). Freeze
   one same-Host trust model and complete authorization/result matrix, or
   explicitly adopt same-principal local trust and remove unsupported
   credential/rotation claims.

5. **R2-05 — Story 2.2 owns revise but has no positive revise oracle.** The
   boundary includes declare, revise, revisions, event sequence, and
   idempotency, but AC1 exercises only valid declaration or declaration retry;
   AC2 covers invalid fields (`epics.md:2843-2867`). The registry assertion is
   only `assert_promise_idempotency` (`2149-2154`). Add an exact revise
   scenario with prior revision, changed fields, event sequence, retry identity,
   stale-revision result, and no-write behavior, or split revise into a bounded
   Story.

6. **R2-06 — Batch 1 F-02 is locally narrowed but remains ambiguous under the
   declared source precedence.** Story 2.3 chooses rejection
   (`epics.md:2869-2894`), while higher-authority PRD FR-6 still permits
   “rejected or retained as unmanaged” and FR-25 says those declarations remain
   unmanaged (`prd.md:229-233`, `429-433`; precedence at `epics.md:30-31`).
   Select one behavior across the PRD and Story, state whether either missing
   prerequisite or only both triggers it, and name the exact no-write or
   persisted effect.

7. **R2-07 — Epic 3 hides schedule and obligation forward cycles behind exact
   dependency fields.** Story 3.1 freezes an obligation-bearing
   `ScopeManifestV1` and `DispatchScheduleV1`, while dependent Story 3.2 later
   implements schedule compilation (`epics.md:2981-3033`). Story 3.10 later
   owns obligation compilation and strict scope outcomes, although Story 3.1
   already needs obligations and Story 3.9 has frozen candidate completeness
   (`3197-3248`). Put obligation/manifest compilation first, schedule
   compilation second, admission third, and strict completeness reduction
   before the immutable candidate freezes.

8. **R2-08 — Story 3.10 does not close the strict obligation/outcome-to-exit
   matrix, and AC1 is malformed.** The boundary promises deterministic strict
   exit, but no row maps required/optional/not-applicable plus complete,
   partial, unavailable, denied, timed-out, and invalid-output to exact result
   and exit (`epics.md:3224-3248`; `ARCHITECTURE-SPINE.md:166-177`). The final
   line `identical input produce...` is detached from an And clause
   (`epics.md:3243-3244`). Add the complete ordered matrix, exact reason/result/
   exit values, and fixed cases; repair the GWT sentence.

9. **R2-09 — Story 4.2 omits the canonical `inactive` Promise Outcome.** Its
   value and AC reduce outcomes to healthy, broken, and otherwise unresolved
   (`epics.md:3308-3333`). The binding PRD defines `healthy | broken |
   unresolved | inactive`, assigns expired/closed intent to inactive, and
   limits unresolved to active intent with insufficient evidence
   (`prd.md:151-156`, `166-172`). Add explicit lifecycle/evidence/outcome rows
   for inactive and constrain unresolved to active intent.

10. **R2-10 — Batch 1 F-06 is locally rewritten but not source-closed.** Story
    4.3 correctly emits an unordered duplicate set plus excess cardinality and
    forbids loser designation (`epics.md:3341-3359`). The higher-authority PRD
    still allows `safe` only for “the exact excess instance,” and AD-18 still
    says intended count classifies exact excess instances (`prd.md:446-452`;
    `ARCHITECTURE-SPINE.md:1218-1222`). Story 4.6 consumes that unresolved rule
    (`epics.md:3422-3440`). Align the sources to set-plus-cardinality with no
    duplicate-derived safe member, or define one deterministic, explicitly
    non-action member selection across all three artifacts.

11. **R2-11 — Story 4.8 mixes domain mutation, CLI, and a future TUI path.** It
    owns baseline persistence, audit, Evidence Window recomputation, TUI `b`,
    modal focus, and Esc while depending only on Story 4.7
    (`epics.md:3476-3492`). Stories 5.1–5.3 later implement TUI entry, modal
    layout/focus, and navigation (`3558`, `3585`, `3612`). AC1 also makes TUI
    `b` or a deterministic command one When branch, then requires Cancel focus
    and Esc for both. Keep domain plus exact noninteractive acceptance in 4.8;
    move the TUI adapter after its prerequisites and give each surface its own
    scenario.

12. **R2-12 — Redirected-output ownership is duplicated between Stories 5.1
    and 5.2.** Story 5.1 owns routing, legacy noninteractive output, and
    UX-RP-6 (`epics.md:3556-3577`). Story 5.2 still includes redirected
    fixtures in its value, boundary, and AC while mapping only UX-RP-1 through
    UX-RP-5 (`3583-3604`). UX-RP-6 is the redirected-stream contract
    (`EXPERIENCE.md:507-514`). Remove redirected behavior from 5.2 and keep it
    solely in 5.1.

13. **R2-13 — Epic 5 maps complete UX contracts whose mandatory action
    behavior belongs to later Stories.** Story 5.2 maps UX-RP-5, whose source
    contract requires active-operation preservation and UX-IP-10-aware quit;
    Story 5.3 maps UX-A11Y-2, including future help and confirmation behavior;
    Story 5.7 maps UX-A11Y-1/5 while excluding action submission
    (`epics.md:3585-3604`, `3612-3631`, `3718-3737`). The source contracts
    require pending/outcome text and submitted-operation disposition
    (`EXPERIENCE.md:461-493`), implemented only in Epic 6. Narrow each mapping
    to pre-action rows or add later integration ownership and dependencies.

14. **R2-14 — Terminal restoration has multiple implementation owners.** Story
    5.1 establishes one RAII terminal owner for every exit, panic, and signal
    (`epics.md:3558`, `3574-3577`), Story 5.7 again says it implements terminal
    restoration (`3718`), and Story 6.10 claims restoration during action
    shutdown (`4045`). Keep 5.1 as the sole implementation owner; later Stories
    should consume it and add state-specific validation only.

15. **R2-15 — Story 5.9 remains the F-09 catch-all and creates a hidden cycle
    with Story 6.12.** It combines immutable state/component goldens, a
    constrained benchmark harness, and an aggregate UX/accessibility gate
    (`epics.md:3766-3791`). It maps only UX-BUD-1/2/3/7, but ACs require all
    UX-ST, each UX-BUD, and any SR row. UX-BUD-4/5/6 and SR-A11Y-1 are owned by
    6.12, which depends transitively on 5.9 (`epics.md:1008-1015`,
    `1687-1715`, `4093-4117`). Split exact read-only goldens from the Host
    benchmark and leave action budgets/SR closure after Epic 6.

16. **R2-16 — Story 6.4 contradicts the closed confirmation/availability
    matrix.** C-05 and the architecture allow Safe-to-stop `unknown` after the
    exact typed acknowledgement; Safe-to-stop is advisory, with only `unsafe`
    unavailable (`epics.md:91-108`; `ARCHITECTURE-SPINE.md:225-228`). Story
    6.4 instead says only an unchanged `safe` result authorizes submit
    (`epics.md:3878-3903`). That also leaves Promise-origin Start, where
    Safe-to-stop may not apply, without an admissible branch. Make pre-mutation
    revalidation preserve the complete C-05 matrix: safe, acknowledged unknown,
    unsafe refusal, and action kinds for which stop safety is not applicable.

17. **R2-17 — Epic 6 depends on an action lock/handoff implemented only in
    Epic 7, forming a cycle.** Story 6.7 requires mutation in the lock-owning
    owner and 6.12 closes the action gate (`epics.md:3958-3983`,
    `4093-4118`), but 7.2 later owns the POSIX admission lock and
    `ActionExecutorHandoffV1` (`4151-4176`). The architecture requires that
    exact persisted/read-back handoff before mutation
    (`ARCHITECTURE-SPINE.md:1475-1492`). The cited lock trace and AD-11 row cover
    only lock-owner loss, not handoff (`epics.md:2445-2450`). Move the shared
    action-lock/handoff primitive and positive/owner-loss/generation-change
    fixtures before 6.7; retain release-exclusive orchestration in Epic 7.

18. **R2-18 — Story 6.8 does not close the durable-phase-to-UX projection.**
    C-10 defines durable phases exactly as planned, launch-authorized,
    executing, and verifying (`epics.md:225-231`). Story 6.8 says it shows
    pending/executing/verifying phase updates without mapping planned or
    launch-authorized (`3985-4010`). Pending-action may be a UX state, but the
    Story does not say which durable phases project into it or preserve the raw
    phase for cancellation. Add the complete four-phase projection table and
    fixtures.

19. **R2-19 — Stories 7.4 and 7.6 claim the same owning oracle while the
    registry assigns rewrite ownership to the wrong boundary.** Story 7.4
    freezes the manifest and excludes replacement; 7.6 owns replacement
    (`epics.md:4205-4230`, `4259-4284`). Both cite
    `brownfield-consumer-pairs.json`, while AD11-FUT-46 assigns
    `assert_two_pair_consumer_rewrite` to 7.4 (`epics.md:2452-2458`). Split
    manifest discovery/readback and rewrite/effect assertions into distinct
    owned rows even if they share immutable input data.

20. **R2-20 — Stories 7.8–7.10 create a KnownGood terminalization cycle.**
    Story 7.8 promises committed while excluding KnownGood publication; 7.9
    says every crash cut may end committed while excluding KnownGood-specific
    recovery; 7.10 implements publication only afterward
    (`epics.md:4313-4392`). The exact forward and takeover oracles include
    `publish-known-good`, ready admission, and `commit-transaction`; the
    architecture requires those before terminal commit
    (`ARCHITECTURE-SPINE.md:1876-1892`, `2232-2243`). End 7.8 at a named
    pre-publication handoff, restrict 7.9 to named generic/pre-decision cuts,
    and let 7.10 own publication, ready admission, terminal commit, and their
    recovery cuts.

21. **R2-21 — FirstInstall authority is consumed before Stories 7.11–7.12 own
    it.** Story 7.5's initial-transaction oracle already contains
    `prior_release.kind=first-install-absent`; 7.8/7.9 use FirstInstall
    transition authorities; 7.10's oracle is also FirstInstall despite its Out
    of Scope. Story 7.11 only later freezes `FirstInstallAbsentV1`, and 7.12
    later claims execution (`epics.md:4232-4257`, `4313-4446`). Move absence
    planning before transaction construction, or restrict 7.5–7.10 to
    installed-prior input and leave the complete FirstInstall path to
    7.11–7.12.

22. **R2-22 — Stories 7.11 and 7.13 use validation oracles that require their
    Out-of-Scope execution.** Story 7.11 excludes FirstInstall execution but
    cites a mid-recovery pending-consumer-removal manifest; 7.13 excludes
    rollback execution/validation but cites a manifest containing restore, FD4
    validation, KnownGood publication, and ready-admission effects
    (`epics.md:4394-4419`, `4448-4473`). Give both planning Stories revision-
    zero/plan-only oracles; reserve pending-effect/transition manifests for
    7.12 and 7.14.

23. **R2-23 — Release command and rollback-confirmation ownership remains
    open.** C-11 names five verbs but does not enumerate each verb's argv,
    result, exit, or confirmation contract (`epics.md:240-254`). Story 7.3
    claims exact argument sets without defining them (`4178-4203`), and 7.13
    requires “explicit confirmation” without defining the accepted input
    (`4448-4473`). AD11-FUT-53 assigns the release-command fixture/assertion to
    aggregate Story 7.15 rather than command Story 7.3 (`2509-2514`). Add a
    closed per-verb argv/result/exit/confirmation table, assign its fixture to
    7.3, and keep 7.15 limited to aggregate invocation.

## Batch 1 F-01 Through F-18 Closure

“Closed” means the original finding is removed end-to-end under the declared
source precedence, not merely rewritten locally in `epics.md`.

| Finding | Disposition | Batch 2 evidence |
| --- | --- | --- |
| F-01 | **Closed** | CommandRunner is isolated in 1.9; aggregate composition is 1.10. R2-03 is a separate aggregate prerequisite defect. |
| F-02 | **Open** | Story 2.3 chooses reject, but binding PRD still permits reject or persist unmanaged. See R2-06. |
| F-03 | **Open** | Story 2.1 names but does not define the authentication/Owner trust contract. See R2-04. |
| F-04 | **Open semantically** | Dependency fields are exact, but schedule, obligation, TUI, action, release, and FirstInstall forward cycles remain. |
| F-05 | **Open / partial** | Candidate/Snapshot handoff improved; Story 1.7 and 4.7 still duplicate Snapshot/current CAS ownership. See R2-02. |
| F-06 | **Open end-to-end** | Story 4.3 uses set plus cardinality, but PRD/architecture still require an undefined exact excess instance. See R2-10. |
| F-07 | **Closed** | C-14 and Story 4.9 enumerate BQ-1 through BQ-8. |
| F-08 | **Closed** | Story 4.10 has deterministic grouping scope and no external approval gate. |
| F-09 | **Open / partial** | Story 5.9 remains a goldens/performance/aggregate catch-all and reaches forward into 6.12. See R2-15. |
| F-10 | **Closed** | C-04 and 6.1 own one lowercase enum and complete Provider matrix. |
| F-11 | **Closed for the original Restart omission** | C-05/6.3 classify all kinds and safety states. R2-16 is a later consumer contradiction. |
| F-12 | **Closed** | 6.5 owns the pool before 6.6 admission. |
| F-13 | **Closed** | C-06 and 6.9 own the ordered five-outcome precedence. |
| F-14 | **Closed for the original oversizing defect** | Status, verification, shutdown, parity, and aggregate closure are split across 6.8–6.12. |
| F-15 | **Closed for manifest-before-preimage order** | 7.4 precedes 7.5. R2-19 is a distinct oracle-ownership defect. |
| F-16 | **Open** | 7.9 and its oracle still require KnownGood-specific terminalization before 7.10. See R2-20. |
| F-17 | **Open** | Named Stories were split, but FirstInstall execution remains duplicated and planning oracles include later effects. See R2-21/R2-22. |
| F-18 | **Open** | Parsing exists in 7.3, but its normative oracle is re-owned by 7.15 and the command/confirmation grammar is incomplete. See R2-23. |

Closure count: **9 closed; 9 open or partial.**

## Closed Matrix Review

| Matrix | Disposition | Evidence |
| --- | --- | --- |
| C-04 ActionKindV1 / Provider | Closed in contract and 6.1 | Exactly five lowercase values; unsupported cells absent/refused; signal remains stop parameters. |
| C-05 confirmation / availability | Contract closed; consumer inconsistent | All action/safety rows are present, but 6.4 rejects acknowledged unknown and non-stop-safe Start. See R2-16. |
| C-06 Action Outcome precedence | Closed | Exactly five ordered outcomes; 6.9 is sole terminal CAS owner. |
| C-11 ReleaseTerminalResultV1 enum | Enum closed; transition ownership open | KnownGood, FirstInstall, planning-oracle, and command ownership defects remain in R2-20 through R2-23. |

## Validation Evidence

| Command/check | Result |
| --- | --- |
| SHA-256 of working file | Pass; exact required digest. |
| SHA-256 of `git show 8ebdc20:.../epics.md` | Pass; exact required digest. |
| Story/section/GWT/dependency parser | Pass structurally: 73 Stories, 146 ACs, 72 exact declared edges. |
| Coverage-registry parser/inverse reconciliation | Pass: 213 requirements, 73 Story rows, 68 AD-11 rows. |
| `bash tests/validate_architecture_contracts.sh` | Expected fail at `planning-root tombstone does not fail closed`; compatibility lane passed before the stop. |
| `python3 tests/fixtures/contracts/validate.py` | Pass: `contract oracles: PASS`. |
| `python3 tests/fixtures/contracts/release-transaction-v1/validate_oracles.py` | Pass: release oracle corpus, crash cuts, live locks/handoffs, mutations, and canonical-byte checks. |
| `bash tests/test_smoke.sh` | Pass: JSON, Prometheus, Markdown, table, inspect, and hostile-name safety. |

The aggregate failure is precisely the declared path-override failure; no other
current contract or smoke failure was observed. It still blocks Story 1.10's
own stated completion because no prior Story owns the validator transition.

## Deletion Check

The parent artifact contained 55 Stories and 165 ACs; the reviewed artifact has
73 Stories and 146 ACs. No source requirement identifier present in the parent
was lost, and the new registry adds explicit ARCH-LIM ownership. No additional
deletion-only finding remains after R2-01 accounts for the behavioral risk of
collapsing more specific scenarios into two generic templates.

## Conclusion

The digest is exact and the backlog is mechanically tidy, but it is not
assignment-ready. The declared graph's 72 prior-only edges are not the real
implementation graph, nine Batch 1 findings are not end-to-end closed, and the
GWT/validation text does not yet force one observable implementation. Under the
required zero-finding rule, the only valid verdict is **FAIL**.
