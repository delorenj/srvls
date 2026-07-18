---
type: epic-story-review
reviewedCommit: c237a2a6a42ad0a20b4f660ae7377360a55471fb
reviewedArtifact: _bmad-output/planning-artifacts/epics.md
observedSha256: beca731ca618cd89e84ef27070cc1e5a2cb33fc820784faeb989194fc9dd2886
verdict: FAIL
findingCount: 13
storyCount: 73
acceptanceCriterionCount: 146
declaredDependencyEdgeCount: 72
---

# R3 Story Quality and Dependency Review

## Verdict

**FAIL — 13 findings.** PASS requires zero.

The batch-2 rewrite closes 12 of the 23 R2 findings, but 11 remain open or
partial and two structural regressions were introduced. The artifact remains
nonassignable and is not implementation authority.

## Digest

| Check | Result |
| --- | --- |
| Commit | `c237a2a6a42ad0a20b4f660ae7377360a55471fb` |
| Commit subject | `docs(planning): record batch 2 remediation dispositions` |
| Artifact | `_bmad-output/planning-artifacts/epics.md` |
| SHA-256 from commit | `beca731ca618cd89e84ef27070cc1e5a2cb33fc820784faeb989194fc9dd2886` |
| SHA-256 from worktree | Exact match |
| Git blob | `ce8b24ec62bb979420763ecb4c30d2c9e1788dd0` |
| Size | 3,873 lines; 204,546 bytes |

## Methods

1. Pinned the artifact to `c237a2a`, verified commit/worktree SHA-256 and Git
   blob identity, and reviewed the complete `8ebdc20..c237a2a` artifact diff.
2. Re-ran a structural parser over all headings, required story sections, GWT
   criteria, dependencies, coverage inverses, and AD-11 rows.
3. Reconciled every R2-01 through R2-23 finding against changed Contracts
   C-15 through C-21 and the affected stories/oracles.
4. Inspected the release JSON/JSONL authorities named by Stories 7.5 and
   7.8-7.13 rather than relying on their labels.
5. Ran `tests/validate_planning_quarantine.py`, contract and release oracle
   validators, compatibility validation, legacy Host smoke, and
   `tests/validate_architecture_contracts.sh`.

Structural parsing found seven epics, 73 unique stories in counts
`10,6,11,10,9,12,15`, all six required sections per story, 146 GWT criteria,
and 72 declared backward dependency edges. Coverage inverses and AD-11 owner
references reconcile. Contract, release, compatibility, and Host-smoke suites
pass. Planning quarantine and the aggregate architecture command fail at
`planning-root tombstone does not fail closed`.

## R2 Finding Accounting

| R2 finding | Result | R3 finding |
| --- | --- | --- |
| R2-01 | Open | R3-01 |
| R2-02 | Closed | — |
| R2-03 | Open | R3-02 |
| R2-04 | Closed | — |
| R2-05 | Closed | — |
| R2-06 | Open | R3-03 |
| R2-07 | Closed | — |
| R2-08 | Closed | — |
| R2-09 | Closed | — |
| R2-10 | Open | R3-04 |
| R2-11 | Closed | — |
| R2-12 | Open | R3-05 |
| R2-13 | Open | R3-06 |
| R2-14 | Closed | — |
| R2-15 | Closed | — |
| R2-16 | Closed | — |
| R2-17 | Closed | — |
| R2-18 | Closed | — |
| R2-19 | Open | R3-07 |
| R2-20 | Open | R3-08 |
| R2-21 | Open | R3-09 |
| R2-22 | Open | R3-10 |
| R2-23 | Open | R3-11 |
| New | Regression | R3-12, R3-13 |

## All-Story Accounting

R3-01 applies to all 73 stories. Additional findings are exhaustive below;
`—` means no additional finding.

| Stories | Additional findings |
| --- | --- |
| 1.1-1.9 | — |
| 1.10 | R3-02 |
| 2.1-2.2 | — |
| 2.3 | R3-03 |
| 2.4-4.2 | — |
| 4.3 | R3-04 |
| 4.4-4.5 | — |
| 4.6 | R3-04 |
| 4.7-4.8 | — |
| 4.9 | R3-12 |
| 4.10-5.1 | — |
| 5.2 | R3-05, R3-06 |
| 5.3 | R3-06 |
| 5.4-5.6 | — |
| 5.7 | R3-06 |
| 5.8-7.2 | — |
| 7.3 | R3-11 |
| 7.4 | R3-07 |
| 7.5 | R3-09 |
| 7.6 | R3-07 |
| 7.7 | — |
| 7.8 | R3-09 |
| 7.9 | R3-08, R3-09 |
| 7.10 | R3-08, R3-09 |
| 7.11 | R3-09, R3-10 |
| 7.12 | R3-09 |
| 7.13 | R3-10, R3-11 |
| 7.14-7.15 | — |

R3-13 is registry-wide and is not assigned to one story.

## Findings

1. **R3-01 — The backlog-wide acceptance template remains nondeterministic.**
   Sixty-eight positive criteria still say only that a future named oracle
   executes its rows; 70 negative criteria refer to unspecified enumerated
   rows; 70 require a generic “row's named result token, schema bytes,
   precedence, and exit.” Most referenced implementation fixtures do not yet
   exist, so those rows cannot currently close the story contract. This is the
   same implementer-choice defect as R2-01 with renamed template prose.

2. **R3-02 — Story 1.10 still owns a known-red aggregate.** The authority text
   says the quarantine failure remains acceptable until a separate revision
   (`epics.md:22-28`), while Story 1.10 claims the discovery assertion and uses
   the failing aggregate as its oracle (`2316-2338`). Both the direct
   quarantine script and aggregate command exit 1 at that assertion.

3. **R3-03 — Story 2.3 cannot close the persistent-intent ambiguity at this
   artifact's precedence level.** C-15 and Story 2.3 require rejection, but the
   higher-authority PRD still permits “rejected or retained as unmanaged” and
   says such declarations remain unmanaged. The epics explicitly place the PRD
   above themselves, so R2-06 remains source-ambiguous.

4. **R3-04 — Duplicate safety is still contradicted by binding sources.** C-17
   correctly forbids selecting or marking a duplicate member safe
   (`398-405`), but the higher-authority PRD still allows the “exact excess
   instance” to be safe and the architecture still classifies exact excess
   instances. Stories 4.3 and 4.6 therefore consume incompatible authority;
   lower-precedence epics prose cannot close R2-10.

5. **R3-05 — Redirected-output ownership remains duplicated.** Story 5.1 owns
   routing and UX-RP-6, but Story 5.2 still includes redirected fixtures in its
   value and redirected contracts in its implementation boundary
   (`3027-3035`). Only its positive AC was narrowed. R2-12 is partial.

6. **R3-06 — Full UX identifiers remain assigned to pre-action stories whose
   boundaries exclude required action behavior.** Story 5.2 still solely maps
   UX-RP-5, Story 5.3 maps UX-A11Y-2, and Story 5.7 maps UX-A11Y-1/5 while
   excluding action submission. The registry contains no row-level partition
   or reciprocal ownership of those same contracts in Epic 6. R2-13 is not
   closed by saying later action rows close elsewhere.

7. **R3-07 — Consumer discovery and rewrite ownership still disagree between
   stories and the AD-11 registry.** AD11-FUT-66 assigns Story 7.4 a future
   `consumer-discovery-v1` oracle (`2075-2081`), but Story 7.4 still names the
   same `brownfield-consumer-pairs.json` oracle as rewrite Story 7.6
   (`3587-3608`, `3635-3656`). The requested story-level split in R2-19 was
   added only to the registry.

8. **R3-08 — Story 7.9 still consumes Story 7.10 terminalization.** Its boundary
   excludes KnownGood, ready admission, and terminal commit, but AC1 requires
   recovery to end `committed` (`3707-3728`). The named owner-takeover oracle
   also contains committed rows, while Story 7.10 owns publication, ready
   admission, and terminal commit (`3731-3753`). The R2-20 cycle remains.

9. **R3-09 — FirstInstall authorities are still consumed before Stories
   7.11-7.12 own them.** Story 7.5 explicitly excludes FirstInstall but its
   initial-transaction fixture has `prior_release.kind=first-install-absent`;
   the Story 7.8 and 7.9 transition corpora are wholly FirstInstall and include
   committed rows; Story 7.10 excludes FirstInstall but its publication fixture
   is FirstInstall. The prose restrictions do not match the cited authorities,
   so R2-21 remains a semantic cycle.

10. **R3-10 — Stories 7.11 and 7.13 still validate planning with execution
    authorities.** Their Validation Expectations now name nonexistent
    revision-zero files, while AC1 still cites the old
    pending-consumer-removal and ready-admission-pending manifests
    (`3755-3777`, `3803-3825`). The automated path comparison reports exactly
    these two mismatches. R2-22 remains open.

11. **R3-11 — The release command contract is not a closed per-verb matrix.**
    C-19 leaves “verb-appropriate” arguments and apply confirmation undefined
    (`416-425`); Story 7.3's AC2 conflates rollback argv with the confirmation
    token and contains a detached `exact typed result ... And` fragment
    (`3562-3585`). Story 7.13 merely says confirmation is explicit. R2-23 is
    still not deterministic.

12. **R3-12 — Inserting C-15 through C-21 emptied C-14 and attached its Brief
    rows to C-21.** `Contract C-14` has no body (`372-374`); BQ-1 through BQ-8
    now appear after the C-21 release contract (`437-458`). Story 4.9 therefore
    cites an empty contract while the release authority accidentally contains
    Brief semantics.

13. **R3-13 — The machine registry's AD-11 count is stale.**
    `canonicalCounts.ad11Rows` declares 68 (`482`), but `ad11Rows` contains 81
    unique rows (`1441-2091`) after the remediation additions. Existing owner
    and inverse checks pass, but the registry is not internally count-consistent.

## Final Gate

**FAIL. Finding count: 13. PASS threshold: 0.**
