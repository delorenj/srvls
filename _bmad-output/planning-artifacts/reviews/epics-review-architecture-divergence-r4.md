---
type: architecture-divergence-review
status: complete
assignable: false
implementationAuthority: false
reviewedCommit: 30ce86dab2e73b2cefb30b8ff7616797b873a232
reviewedArtifact: _bmad-output/planning-artifacts/epics.md
reviewedSha256: 8debf05b8fd24bc19a00dfc6ce56961050d56b97ea972613135616df4eaedbd4
architectureSha256: 28a103267a8e4ae5411c314bc2f9c0b62b694352e6e91c2522a2271df16ff575
sourceReviewSha256: f3dfa4d2e405ef86efe4edad978f899871683196513845ad4167d7426e820950
verdict: FAIL
findingCount: 12
---

# Epics Architecture-Divergence Review R4

## Digest and Verdict

**FAIL — 12 findings. PASS requires zero.** The reviewed artifact is exactly the
`epics.md` blob at `30ce86d`; its SHA-256 begins with the requested
`8debf05b` digest and the worktree matched that committed blob. Batch 3 repairs
four of the seven R3 architecture findings, but leaves two incomplete, replaces
one with a different AD-15 divergence, and introduces a backlog-wide result-model
regression. The artifact remains nonassignable and is not implementation
authority.

| Input | SHA-256 |
| --- | --- |
| `30ce86d:_bmad-output/planning-artifacts/epics.md` | `8debf05b8fd24bc19a00dfc6ce56961050d56b97ea972613135616df4eaedbd4` |
| Binding architecture spine | `28a103267a8e4ae5411c314bc2f9c0b62b694352e6e91c2522a2271df16ff575` |
| R3 architecture-divergence review | `f3dfa4d2e405ef86efe4edad978f899871683196513845ad4167d7426e820950` |

## Method

- Pinned and hashed the current `epics.md`, architecture spine, and R3 review;
  parsed the sole normative JSON block independently.
- Checked the declared counts, 73 story IDs, reciprocal coverage maps, 82 unique
  AD-11 IDs, every row owner, every row field, delivery class, fixture,
  assertion, and aggregate command.
- Replayed each R3 finding against the current contracts, story boundaries,
  acceptance criteria, and AD-11 rows.
- Audited AD-1 through AD-25 against their complete binding sections rather than
  relying on mapping tags.
- Executed the compatibility, canonical-contract, release-oracle, Host-smoke,
  planning-quarantine, and aggregate architecture gates independently.
- Searched the complete architecture for the two result tokens introduced by
  Batch 3. Neither `contract_violation` nor `provider_environment_violation`
  exists in the binding spine.

## Findings

1. **R4-01 — Every AD-11 row names an aggregate command that is currently
   red and does not run the current lanes together.** Every one of the 82 rows
   declares `bash tests/validate_architecture_contracts.sh` as its aggregate
   command (`epics.md:1503-2156`). That script runs the planning-quarantine check
   second and exits immediately on failure before the canonical-contract,
   release, and Host-smoke commands at its lines 11-13. The exact execution
   exits 1 at `planning-root tombstone does not fail closed`; the three skipped
   lanes pass only when invoked separately. AD-11 requires this exact aggregate
   to run all current lanes together (`ARCHITECTURE-SPINE.md:518-531`). Thus all
   14 rows marked `current` have passing individual evidence but a failing
   aggregate obligation, and every future row inherits a red acceptance path.

2. **R4-02 — AD-11 reciprocity is still not closed for Story 1.10.** The
   registry maps Story 1.10 to AD-11 in both directions (`epics.md:852,1331-1392`)
   and the story repeats that mapping (`epics.md:2384-2406`), but none of the 82
   `ad11Rows` names Story 1.10 as owner (`epics.md:1503-2156`). All row owners now
   appear in reciprocal coverage, so the forward half of R3-02 is repaired; its
   expressly recorded converse defect remains. An implementation can treat the
   AD-11 coverage list as complete or require a row for every AD-11-mapped owner.

3. **R4-03 — Story 1.10 makes the authorized canonical-path override both its
   goal and its failure condition.** The authority section says the canonical
   `epics.md` override is active and that Story 1.10 must revise validation so
   canonical discovery and archive quarantine both pass (`epics.md:20-31`). The
   story boundary likewise requires the canonical final artifact to be
   discoverable (`epics.md:2384-2403`), but AC2 says an active user override must
   produce `contract_violation`, exit 4 (`epics.md:2405-2406`). The current
   tombstone-only validator proves the contradiction operationally. There is no
   acceptance state in which the requested override is both active and passing.

4. **R4-04 — Batch 3 replaces architecture-native typed results with one
   architecture-foreign result across 69 stories.** Sixty-nine negative ACs now
   require the capability to return `contract_violation` in CanonicalJsonV1,
   exit 4, usually with no write. That token does not occur anywhere in the
   binding architecture. It overwrites closed result models across AD-3, AD-5,
   AD-6, AD-10, AD-11, AD-15, AD-17, AD-19 through AD-23, and AD-25. A direct
   contradiction is Contract C-15's requirement that either missing persistent
   prerequisite return `lease_prerequisite_missing`, exit 2, no write
   (`epics.md:391-402`) while Story 2.3 requires invalid persistent intent to
   return `contract_violation`, exit 4 (`epics.md:2460-2482`). Story 7.3 was
   specially corrected to retain `invalid_arguments`, exit 2
   (`epics.md:3647-3652`), proving the universal replacement is not a legitimate
   architecture-wide envelope. Every AD-11 row except FUT-07 and FUT-53 maps to
   an owning story with this result regression; FUT-68 has the separate foreign
   token in R4-09.

5. **R4-05 — Story 3.3 replaces AD-25's exhaustive transport normalization
   with a foreign universal result.** Its AC2 maps duplicate descriptors,
   replay, wrong credentials, boundary sizes, expired reservations, bare exits,
   signals, and late reap to `contract_violation`, exit 4, no write
   (`epics.md:2608-2630`). AD-25 instead requires the total ordered reasons
   `worker-timeout`, `worker-spawn`, `request-encode`, size reasons,
   `fd-peer-auth`, `frame-invalid`, schema/version/identity/capability/assignment
   reasons, worker errors, signals, or exits, normalized into exactly one
   `timed-out` or `invalid-output` CollectorReport (`ARCHITECTURE-SPINE.md:2756-2769,2784-2825`).
   AD-5 prohibits a seventh outcome (`ARCHITECTURE-SPINE.md:166-177`). This
   diverges AD11-FUT-14 through FUT-17 and the implementation matrix behind the
   current FD3 rows.

6. **R4-06 — Story 3.4 turns ordinary cron partial/denied evidence into a fatal
   contract error.** Permissions and partial sources are valid collection
   outcomes, but AC2 maps them to `contract_violation`, exit 4, no write
   (`epics.md:2632-2654`). AD-5 requires preserved `partial` or `denied` reports
   (`ARCHITECTURE-SPINE.md:166-186`), while Contract C-16 requires the identical
   reason token with exit 3 for required scopes and exit 0 for optional scopes
   (`epics.md:404-413`). AD11-FUT-18 therefore accepts a result model forbidden
   by AD-5, AD-11, AD-15, and AD-21.

7. **R4-07 — Story 3.5 similarly destroys systemd scoped-failure semantics.** A
   manager-owner change, disappearing property, denied access, or conflicting
   timer evidence must remain a scoped, typed collection result, but AC2 maps all
   four to `contract_violation`, exit 4, no write (`epics.md:2656-2678`). AD-15
   requires daemon unavailable, permission denied, timeout, invalid output, and
   nonzero status to remain distinct diagnostics and collection outcomes
   (`ARCHITECTURE-SPINE.md:1082-1101`). AD11-FUT-19 can therefore be implemented
   incompatibly while still satisfying the story text.

8. **R4-08 — Story 3.8 discards the architecture's process-root and cleanup
   result model.** PID reuse and unresolved internal-child cleanup are runtime
   races, not schema violations, yet AC2 maps them to `contract_violation`, exit
   4, no write (`epics.md:2728-2750`). AD-25 requires unresolved absence to
   prevent a process Request/Host read and, if it misses the cut, synthesize a
   `worker-timeout` report without exposing the child (`ARCHITECTURE-SPINE.md:2790-2797`);
   the AD-11 matrix requires the same absence, timeout, suppression, diagnostic,
   and immutable-report evidence (`ARCHITECTURE-SPINE.md:660-691`). This breaks
   AD11-FUT-22's obligation.

9. **R4-09 — The new AD-15 closure row has two owning oracles and invents a
   non-architectural result.** AD11-FUT-68 names
   `provider-privilege-environment-v1` and its own assertion
   (`epics.md:2151-2156`), while owner Story 6.7's singular Validation
   Expectations names `action-executor-v1` (`epics.md:3434-3447`). Its positive
   AC unexpectedly expands the executor story to every collector and executor,
   then AC2 requires `provider_environment_violation`, exit 4
   (`epics.md:3451-3456`). The architecture has no such result and requires
   distinct missing-executable, unsupported-capability, daemon-unavailable,
   permission-denied, timeout, invalid-output, and nonzero-status diagnostics
   and outcomes (`ARCHITECTURE-SPINE.md:1087-1101`). R3-03 gained a row but did
   not gain one closed fixture/result authority; AD11-FUT-40 and FUT-68 diverge.

10. **R4-10 — Action revalidation and verification no longer terminate in the
    AD-6 outcome vocabulary.** Story 6.4's positive AC correctly refuses stale,
    reused, missing, ambiguous, expired, or unsafe targets, but AC2 changes a
    stale path that passes into `contract_violation`, exit 4
    (`epics.md:3362-3384`). Story 6.9 does the same when command exit alone is
    offered as verification or replacement changes identity
    (`epics.md:3482-3504`). AD-6 requires pre-launch identity drift to be
    `refused/stale-identity`, post-launch replacement to be
    `executed-unverified`, unsafe to be unavailable, and every execution to end
    in exactly `verified | executed-unverified | refused | timed-out | failed`
    (`ARCHITECTURE-SPINE.md:215-240`). AD11-FUT-41 and FUT-64 do not preserve the
    closed architecture outcomes.

11. **R4-11 — Story 6.6 makes ordinary duplicate and expired admissions schema
    violations.** AC2 maps a duplicate exact target and an expired plan to
    `contract_violation`, exit 4 (`epics.md:3410-3432`). AD-6 instead requires a
    conflicting submission to be `refused/duplicate-operation`, while expiry
    requires a new plan and confirmation (`ARCHITECTURE-SPINE.md:229-238`).
    AD11-FUT-39 can therefore encode either the architecture's admission result
    or the backlog's foreign result.

12. **R4-12 — Story 7.9 still owns terminal results that its boundary excludes.**
    The story excludes KnownGood publication, ready admission, and terminal
    commit (`epics.md:3774-3790`) but AC1 requires pre-decision takeover to end
    at `commit-decided`, `forward-failed-recovered`, or
    `upgrade-recovery-required` “without terminal commit” (`epics.md:3791-3796`).
    AD-23 requires pre-decision recovery to restore and validate the whole prior
    pair and produce its terminal result, while post-decision recovery must
    finish publication, ready admission, and terminal commit in order
    (`ARCHITECTURE-SPINE.md:2232-2244,2329-2339`). The current story still splits
    the terminal owner from terminalization and leaves `commit-decided`—an
    internal irreversible step—alongside public terminal results. AD11-FUT-49
    remains architecturally ambiguous.

## R3 Architecture-Finding Closure

| R3 finding | R4 result | Evidence |
| --- | --- | --- |
| R3-01 — false AD-11 count | Closed | Declared and parsed totals are both 82: 14 current plus 68 future (`epics.md:497-512,1501-2157`). |
| R3-02 — reciprocal AD-11 ownership | **Not closed** | All row owners now map reciprocally, but mapped Story 1.10 still owns no row (R4-02). |
| R3-03 — AD-15 tag-only coverage | **Not closed** | FUT-68 and a complete positive matrix exist, but fixture authority and result vocabulary diverge (R4-09). |
| R3-04 — permanent stable point-pin | Closed | C-11 and C-19 both require symbolic moving `stable`; point pins are forbidden (`epics.md:322-326,433-443`). |
| R3-05 — foreign release authority | Closed | C-11 and C-21 now use only `ManagedConsumerUnitContractV1`, `BrownfieldConsumerPairsV1`, transaction consumers, and hashes (`epics.md:299-333,455-464`). |
| R3-06 — global rewrite cardinality | Closed | Story 7.6 requires two pair-qualified occurrences for each independently bound pair (`epics.md:3702-3724`). |
| R3-07 — incompatible release grammar | Closed | C-11, C-19, Story 7.3, and FUT-53 agree on the five verbs install, upgrade, validate, status, and rollback; invalid arguments are explicitly exit 2 (`epics.md:299-307,433-443,3630-3652,2023-2028`). |

## AD-1 Through AD-25 Audit

| Decision | Result | Evidence |
| --- | --- | --- |
| AD-1 | Conforms | Story 1.1 owns inward dependency direction and the boundary gate. |
| AD-2 | Conforms | Promise, Observation, Finding, Snapshot, and Operation ownership remains separated. |
| AD-3 | Conforms | Ports and in-process owners retain side-effect authority. |
| AD-4 | Conforms | Story 4.10 and FUT-63 retain deterministic evidence-based grouping. |
| AD-5 | **Diverges** | Collection/transport failures are collapsed into foreign exit-4 results (R4-05 through R4-08). |
| AD-6 | **Diverges** | Revalidation, admission, and verification can bypass the closed action outcomes (R4-10, R4-11). |
| AD-7 | Conforms | Routing and the release namespace are closed; Story 7.3 retains `invalid_arguments`/exit 2. |
| AD-8 | Conforms | Text-primary, hostile-text, Unicode, ASCII, and motion rules remain owned. |
| AD-9 | Conforms subject to R4-01 | The compatibility lane passes independently but not through the required aggregate. |
| AD-10 | Conforms subject to R4-01 | Frozen scheduling, reservations, cuts, and pools remain explicit. |
| AD-11 | **Diverges** | Aggregate, reciprocity, row semantics, and acceptance ownership fail (R4-01 through R4-12). |
| AD-12 | Conforms | Moving stable, MSRV, final-artifact hash, ABI proof, and smoke remain represented. |
| AD-13 | Conforms | Typed identities and canonical property coverage remain represented. |
| AD-14 | Conforms | One terminal/shutdown owner and durable no-detach behavior remain explicit. |
| AD-15 | **Diverges** | Provider error distinctions and the FUT-68 authority/result contract conflict (R4-06 through R4-09). |
| AD-16 | Conforms | SQLite transactions, CAS, retention, recovery, and capacity remain owned. |
| AD-17 | **Diverges** | Persistent-prerequisite failure has two incompatible exact results (R4-04). |
| AD-18 | Conforms | Frozen pure reconciliation, orthogonal axes, grouping, and safety remain represented. |
| AD-19 | Conforms | Typed precedence, provenance, validation, and no-hot-reload remain explicit. |
| AD-20 | Conforms | ARCH-LIM-1 through ARCH-LIM-24 remain inventoried and mapped. |
| AD-21 | **Diverges** | FD3, Provider, and process-scope failure cuts lose required reports/outcomes (R4-05 through R4-08). |
| AD-22 | **Diverges** | Action revalidation and admission results conflict with AD-6/AD-22 (R4-10, R4-11). |
| AD-23 | **Diverges** | Story 7.9 still splits recovery terminal result from terminal ownership (R4-12). |
| AD-24 | Conforms | Canonical JSON, binary IDs, paths, fingerprints, and fixed bytes remain owned. |
| AD-25 | **Diverges** | Story 3.3 replaces total transport precedence and synthesized reports (R4-05). |

## Every AD-11 Row and Obligation

All 82 IDs are unique; every row has all six required fields, a valid owner, and
the declared delivery value. “Conforms” below means the row's **positive named
obligation** maps to the architecture. It is not a full-row PASS: R4-04 overlays
every row except FUT-07 and FUT-53 because its owning negative AC requires the
foreign universal result; FUT-68 instead carries R4-09's foreign result. Every
current row is shown separately because current delivery also includes a live
aggregate obligation, not merely a future fixture promise.

| Row | Owner | Result | Obligation evidence |
| --- | --- | --- | --- |
| AD11-CUR-01 | Story 1.3 | **Aggregate FAIL** | Legacy CLI matrix passes independently; aggregate stops before it can complete all current lanes (R4-01). |
| AD11-CUR-02 | Story 1.3 | **Aggregate FAIL** | Legacy output bytes pass independently; aggregate obligation fails (R4-01). |
| AD11-CUR-03 | Story 1.3 | **Aggregate FAIL** | Legacy Provider matrix passes independently; aggregate obligation fails (R4-01). |
| AD11-CUR-04 | Story 1.3 | **Aggregate FAIL** | Legacy inspection matrix passes independently; aggregate obligation fails (R4-01). |
| AD11-CUR-05 | Story 1.3 | **Aggregate FAIL** | Legacy action argv matrix passes independently; aggregate obligation fails (R4-01). |
| AD11-CUR-06 | Story 1.4 | **Aggregate FAIL** | Contract manifest passes independently; aggregate aborts before this lane (R4-01). |
| AD11-CUR-07 | Story 1.4 | **Aggregate FAIL** | Fixed policy bytes pass independently; aggregate aborts before this lane (R4-01). |
| AD11-CUR-08 | Story 3.1 | **Aggregate FAIL** | Fixed plan/scope bytes pass independently; aggregate aborts before this lane (R4-01). |
| AD11-CUR-09 | Story 1.4 | **Aggregate FAIL** | Fixed identity bytes pass independently; aggregate aborts before this lane (R4-01). |
| AD11-CUR-10 | Story 3.1 | **Aggregate FAIL** | Fixed assignment bytes pass independently; aggregate aborts before this lane (R4-01). |
| AD11-CUR-11 | Story 3.3 | **Aggregate FAIL** | FD3 four-frame bytes pass independently; aggregate aborts before this lane (R4-01). |
| AD11-CUR-12 | Story 3.3 | **Aggregate FAIL** | FD3 no-allocation cut passes independently; aggregate aborts before this lane (R4-01). |
| AD11-CUR-13 | Story 7.15 | **Aggregate FAIL** | Release subcorpus passes independently; aggregate aborts before this lane (R4-01). |
| AD11-CUR-14 | Story 1.3 | **Aggregate FAIL** | Legacy Host smoke passes independently; aggregate aborts before this lane (R4-01). |
| AD11-FUT-01 | Story 1.1 | Conforms | Dependency direction and side-effect owner. |
| AD11-FUT-02 | Story 1.5 | Conforms | Configuration and all architecture limits. |
| AD11-FUT-03 | Story 1.6 | Conforms | Fresh/existing SQLite initialization and fail-closed readback. |
| AD11-FUT-04 | Story 1.7 | Conforms | Repository CAS and unavailable results. |
| AD11-FUT-05 | Story 1.8 | Conforms | Pins, retention watermarks, and capacity mode. |
| AD11-FUT-06 | Story 1.9 | Conforms | CommandRunner terminal result before reap. |
| AD11-FUT-07 | Story 2.1 | Conforms | Principal and owner authentication. |
| AD11-FUT-08 | Story 2.2 | Conforms | Promise declare/revise idempotency and revision conflict. |
| AD11-FUT-09 | Story 2.3 | **Diverges** | Persistent-prerequisite exact result conflicts with C-15 (R4-04). |
| AD11-FUT-10 | Story 3.2 | Conforms | Default frozen dispatch schedule. |
| AD11-FUT-11 | Story 3.2 | Conforms | Near-tie frozen schedule. |
| AD11-FUT-12 | Story 3.2 | Conforms | Sixty-second zero-margin schedule. |
| AD11-FUT-13 | Story 3.2 | Conforms | Missed-cut admission with no post-cut allocation. |
| AD11-FUT-14 | Story 3.3 | **Diverges** | Peer/Ready failures lose AD-25 reasons and synthesized report (R4-05). |
| AD11-FUT-15 | Story 3.3 | **Diverges** | Descriptor/EOF failures lose AD-25 reasons and synthesized report (R4-05). |
| AD11-FUT-16 | Story 3.3 | **Diverges** | Total failure precedence is replaced by universal exit 4 (R4-05). |
| AD11-FUT-17 | Story 3.3 | **Diverges** | Reap immutability path is replaced by universal exit 4 (R4-05). |
| AD11-FUT-18 | Story 3.4 | **Diverges** | Cron partial/denied semantics conflict with AD-5/C-16 (R4-06). |
| AD11-FUT-19 | Story 3.5 | **Diverges** | Systemd scoped failures conflict with AD-15 (R4-07). |
| AD11-FUT-20 | Story 3.6 | Conforms | Docker identity matrix. |
| AD11-FUT-21 | Story 3.7 | Conforms | PM2 identity matrix. |
| AD11-FUT-22 | Story 3.8 | **Diverges** | PID-reuse/unresolved-cleanup result conflicts with AD-25 (R4-08). |
| AD11-FUT-23 | Story 3.9 | Conforms | CollectionCandidate remains distinct from Snapshot. |
| AD11-FUT-24 | Story 3.10 | Conforms | Obligation, strict-mode, reason, and evidence matrix. |
| AD11-FUT-25 | Story 4.1 | Conforms | Correlation vectors, conflicts, ties, and frozen input. |
| AD11-FUT-26 | Story 4.3 | Conforms | Duplicate set and excess cardinality without loser selection. |
| AD11-FUT-27 | Story 4.4 | Conforms | Stale/hot positive evidence and history races. |
| AD11-FUT-28 | Story 4.7 | Conforms | Snapshot materialization and sole current CAS. |
| AD11-FUT-29 | Story 4.8 | Conforms | Baseline races, compatibility, and override. |
| AD11-FUT-30 | Story 4.9 | Conforms | Eight Brief rows and drill-down evidence. |
| AD11-FUT-31 | Story 5.1 | Conforms | Routing and terminal restoration. |
| AD11-FUT-32 | Story 5.3 | Conforms | Unicode search, focus, and retarget protection. |
| AD11-FUT-33 | Story 5.5 | Conforms | Plane/Git/telemetry display-only boundary. |
| AD11-FUT-34 | Story 5.7 | Conforms | Text-primary accessibility and hostile text. |
| AD11-FUT-35 | Story 5.9 | Conforms | Read-only Host budgets and independent goldens. |
| AD11-FUT-36 | Story 6.1 | Conforms | Closed ActionKind matrix. |
| AD11-FUT-37 | Story 6.3 | Conforms | Immutable plan and complete confirmation matrix. |
| AD11-FUT-38 | Story 6.5 | Conforms | Separate pool before admission; saturation refuses pre-launch. |
| AD11-FUT-39 | Story 6.6 | **Diverges** | Duplicate/expired admission result conflicts with AD-6 (R4-11). |
| AD11-FUT-40 | Story 6.7 | **Diverges** | Executor failure vocabulary conflicts with AD-15 and FUT-68 (R4-09). |
| AD11-FUT-41 | Story 6.9 | **Diverges** | Verification races bypass the closed action outcomes (R4-10). |
| AD11-FUT-42 | Story 6.10 | Conforms | No detach and durable finalization. |
| AD11-FUT-43 | Story 6.12 | Conforms | Action aggregate, budgets, journeys, and accessibility. |
| AD11-FUT-44 | Story 7.1 | Conforms | Moving stable/MSRV, exact artifact, ABI, and smoke. |
| AD11-FUT-45 | Story 7.2 | Conforms | Traditional POSIX record-lock ownership. |
| AD11-FUT-46 | Story 7.6 | Conforms | Per-pair source and loaded-ExecStart rewrite cardinality. |
| AD11-FUT-47 | Story 7.7 | Conforms | Exact FD4 request/result bytes and authentication. |
| AD11-FUT-48 | Story 7.7 | Conforms | D-Bus handshake and one shared validation cut. |
| AD11-FUT-49 | Story 7.9 | **Diverges** | Pre-decision terminal ownership remains split (R4-12). |
| AD11-FUT-50 | Story 7.10 | Conforms | Post-decision KnownGood publication and readback. |
| AD11-FUT-51 | Story 7.12 | Conforms | FirstInstall absence restoration and recovery. |
| AD11-FUT-52 | Story 7.14 | Conforms | Explicit rollback and displaced-source publication. |
| AD11-FUT-53 | Story 7.3 | Conforms | Exact release grammar, results, arguments, and confirmation. |
| AD11-FUT-54 | Story 7.15 | Conforms | Exact final-artifact Host smoke. |
| AD11-FUT-55 | Story 7.15 | Conforms | Isolated service-manager CI rows. |
| AD11-FUT-56 | Story 1.4 | Conforms | Canonical policy/scope/diagnostic/candidate/process properties. |
| AD11-FUT-57 | Story 2.4 | Conforms | Heartbeat idempotency, cadence, Lease ceiling, and owner checks. |
| AD11-FUT-58 | Story 2.5 | Conforms | Close idempotency and inactive projection. |
| AD11-FUT-59 | Story 2.6 | Conforms | Agent linear/JSON argv, result, and exit matrix. |
| AD11-FUT-60 | Story 4.2 | Conforms | Orthogonal healthy/broken/unresolved/inactive outcomes. |
| AD11-FUT-61 | Story 4.5 | Conforms | Unmanaged/abandoned coexistence without cleanup. |
| AD11-FUT-62 | Story 4.6 | Conforms | Complete conservative Safe-to-stop matrix. |
| AD11-FUT-63 | Story 4.10 | Conforms | Deterministic Stack/Ungrouped grouping properties. |
| AD11-FUT-64 | Story 6.4 | **Diverges** | Revalidation result conflicts with AD-6 (R4-10). |
| AD11-FUT-65 | Story 6.11 | Conforms | TUI/linear/JSON action parity. |
| AD11-FUT-66 | Story 7.4 | Conforms | Two-pair consumer discovery and readback before preimages. |
| AD11-FUT-67 | Story 7.15 | Conforms | Both pairs through every effect and crash cut. |
| AD11-FUT-68 | Story 6.7 | **Diverges** | Fixture authority and Provider result vocabulary conflict (R4-09). |

## Executable Evidence and Final Gate

| Check | Result |
| --- | --- |
| Pinned SHA-256 and requested `8debf05b` prefix | PASS |
| JSON parse, counts, row IDs, fields, owners, delivery classes | PASS — 82 unique rows; 14 current, 68 future |
| Row-owner to AD-11 coverage | PASS — all 60 unique row owners covered |
| AD-11 coverage to row-owner reciprocity | FAIL — Story 1.10 has no row |
| `bash tests/compat/validate.sh` | PASS — 90 inherited plus 4 approved deviations |
| `python3 tests/fixtures/contracts/validate.py` | PASS |
| `python3 tests/fixtures/contracts/release-transaction-v1/validate_oracles.py` | PASS — 11 crash cuts, 7 complete chains, all reported mutation families |
| `bash tests/test_smoke.sh` | PASS — JSON, Prometheus, Markdown, table, inspect, hostile-name safety |
| `python3 tests/validate_planning_quarantine.py` | FAIL — `planning-root tombstone does not fail closed` |
| `bash tests/validate_architecture_contracts.sh` | FAIL at the same quarantine assertion before contract/release/smoke lanes |
| R3 architecture-finding replay | FAIL — R3-02 and R3-03 not closed; Batch-3 regressions remain |
| Semantic AD-1..25 and every-row audit | FAIL — 12 findings |

**Final gate: FAIL — 12 findings. PASS is prohibited above zero.** A later
candidate must repair the aggregate/quarantine contract, give Story 1.10 one
coherent AD-11 obligation, remove the invented universal result model, restore
each architecture-native typed outcome, close FUT-68 to one fixture authority,
and reunify Story 7.9's recovery terminal ownership before another independent
zero-finding review.
