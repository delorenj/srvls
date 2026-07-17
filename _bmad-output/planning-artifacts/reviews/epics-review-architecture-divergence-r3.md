---
type: architecture-divergence-review
status: complete
assignable: false
implementationAuthority: false
reviewedCommit: c237a2a6a42ad0a20b4f660ae7377360a55471fb
reviewedArtifact: _bmad-output/planning-artifacts/epics.md
reviewedSha256: beca731ca618cd89e84ef27070cc1e5a2cb33fc820784faeb989194fc9dd2886
architectureSha256: 28a103267a8e4ae5411c314bc2f9c0b62b694352e6e91c2522a2271df16ff575
sourceReviewSha256: b0f32d57a1cf1f220a80e8c15e6337d4f23913e80132ea05d9e197b810ce0359
verdict: FAIL
findingCount: 7
---

# Epics Architecture-Divergence Review R3

## Digest and Verdict

**FAIL — 7 findings. PASS requires zero.** The reviewed input is exactly the
`epics.md` blob at `c237a2a`; no worktree drift was reviewed. Batch 2 added the
missing R2 rows and closed several story-level seams, but stale normative
contracts and a non-reconciled coverage registry still permit incompatible
implementations.

| Input | SHA-256 |
| --- | --- |
| `c237a2a:_bmad-output/planning-artifacts/epics.md` | `beca731ca618cd89e84ef27070cc1e5a2cb33fc820784faeb989194fc9dd2886` |
| Binding architecture spine | `28a103267a8e4ae5411c314bc2f9c0b62b694352e6e91c2522a2271df16ff575` |
| R2 architecture-divergence review | `b0f32d57a1cf1f220a80e8c15e6337d4f23913e80132ea05d9e197b810ce0359` |

## Methods

- Pinned the reviewed blob with `git show c237a2a:...`, computed its digest,
  and compared the architecture and R2 review digests.
- Parsed the sole fenced JSON registry independently; checked counts, unique
  IDs, fields, owners, delivery classes, AD-1..25 inventory, and reciprocal
  `coverageByStory`/`requirementCoverage` mappings.
- Ran exact `grep`/`rg` probes for every D-01..D-12 remediation seam, including
  Host smoke, Promise/reconciliation/action rows, AD-15, stable/MSRV language,
  consumer authority, rewrite cardinality, commit ordering, and two-pair cuts.
- Ran `bash tests/compat/validate.sh`, both contract validator scripts,
  `bash tests/test_smoke.sh`, and
  `bash tests/validate_architecture_contracts.sh`. All fixed current oracles
  passed; the aggregate exited 1 only at the authorized planning-root tombstone
  assertion. Current-oracle success does not validate future backlog semantics.

## Findings

1. **R3-01 — The normative AD-11 count is false.** `canonicalCounts.ad11Rows`
   remains `68` (`epics.md:482`), while the normative array contains 81 unique
   rows: 14 current and 67 future (`epics.md:1441-2090`). An implementation can
   enforce the declared count and reject the registry, or ignore it and accept
   81 rows. This also disproves the artifact's machine-checkable self-consistency.

2. **R3-02 — Eleven added AD-11 row owners are absent from reciprocal AD-11
   coverage.** The rows own Stories 2.4, 2.5, 2.6, 4.2, 4.5, 4.6, 4.10, 6.4,
   6.11, 7.3, and 7.6, but those stories omit AD-11 from `coverageByStory` and
   from `requirementCoverage["AD-11"]` (`epics.md:784-1004,1282-1332,
   1907-2074`). Thus D-02, D-03, D-05, and D-10 gained rows without closing the
   registry's reciprocal ownership model. Conversely, Story 1.10 is mapped to
   AD-11 but owns no row.

3. **R3-03 — D-06 remains tag-only rather than acceptance-gated.** Contract
   C-18 correctly states AD-15, and the coverage map now tags Stories 3.4-3.8
   and 6.7. Their owning assertions remain collection/identity/suppression or
   executor assertions; their acceptance criteria do not enumerate absolute
   allowlists, cwd `/`, minimal environments, `sudo -n`, ambient credential and
   locale exclusion, redaction, or denial/error mapping (`epics.md:2564-2682,
   3366-3388`). No AD-11 row owns that complete matrix. Two adapters can still
   satisfy the named rows with different privilege/environment behavior.

4. **R3-04 — D-08's permanent point-pin remains normative.** C-11 still says
   `StableToolchainEvidenceV1` binds stable `1.97.1` and rejects `1.97.0`
   (`epics.md:319-322`), while C-19 and Stories 1.1/7.1 require symbolic moving
   stable (`epics.md:416-425,2106,3520`). The architecture permits 1.97.1 only
   as reviewed-current evidence and forbids replacing the moving lane with a
   permanent point release. Both interpretations remain backlog-compliant.

5. **R3-05 — D-09's architecture-foreign release authority remains binding.**
   C-11 still declares `ManagedConsumerManifestV1` architecture-native and
   alias-exclusive, then makes it the preimage authority (`epics.md:297-325`).
   C-21 declares the same type forbidden and permits only ordered
   `ManagedConsumerUnitContractV1`, `BrownfieldConsumerPairsV1`, transaction
   consumers, and hashes (`epics.md:437-446`). This is a direct normative
   schema and checksum-boundary contradiction.

6. **R3-06 — D-10's rewrite cardinality remains globally ambiguous.** C-11
   requires exactly two deployed-executable replacements, and Story 7.6's user
   outcome and positive AC still say “the two ... byte spans”
   (`epics.md:324-328,3635-3655`). Its implementation boundary instead requires
   the source fragment and loaded ExecStart occurrence for **each** metrics and
   snapshot pair: four pair-qualified occurrences. AD11-FUT-46 therefore still
   accepts incompatible global-two and per-pair-two implementations.

7. **R3-07 — The release command grammar diverges from AD-7 and AD-23.** C-11
   matches the architecture's exact `install|upgrade|validate|status|rollback`
   namespace and says `recover` does not exist (`epics.md:301-304`). C-19,
   Story 7.3, and AD11-FUT-53 instead require
   `plan|apply|status|recover|rollback` (`epics.md:416-425,1963-1970,
   3562-3585`). Implementations following either closed grammar cannot
   interoperate and will disagree on routing, confirmation, results, and exits.

## R2 Finding Closure Matrix

| R2 finding | R3 result | Evidence |
| --- | --- | --- |
| D-01 | Closed, registry still fails R3-01 | AD11-CUR-14 names `tests/test_smoke.sh`; declared total was not updated. |
| D-02 | Not closed | FUT-57..59 exist, but their owners are absent from reciprocal AD-11 coverage (R3-02). |
| D-03 | Not closed | FUT-60..63 exist, but their owners are absent from reciprocal AD-11 coverage (R3-02). |
| D-04 | Closed | FUT-56 owns the required canonical/identity property surface. |
| D-05 | Not closed | FUT-64..65 exist, but their owners are absent from reciprocal AD-11 coverage (R3-02). |
| D-06 | Not closed | C-18 and tags exist; no complete privilege/environment acceptance row exists (R3-03). |
| D-07 | Closed | Story 6.4 admits safe and acknowledged-unknown, rejects unsafe, and treats Start as not-applicable. |
| D-08 | Not closed | Moving-stable language was added without removing C-11's permanent point contract (R3-04). |
| D-09 | Not closed | C-21 forbids the foreign type while C-11 still requires it (R3-05). |
| D-10 | Not closed | FUT-46 moved to Story 7.6, but reciprocal ownership and pair cardinality remain divergent (R3-02/R3-06). |
| D-11 | Closed | Story 7.8 ends at `commit-decided`; Story 7.10 owns publication, ready admission, and terminal commit. |
| D-12 | Closed | FUT-67 and Story 7.15 require both pairs through every named effect and crash cut. |

## AD-1 Through AD-25 Matrix

| Decision | Result | Backlog evidence |
| --- | --- | --- |
| AD-1 | Conforms | Story 1.1 owns dependency direction and the architecture boundary gate. |
| AD-2 | Conforms | Repository aggregates and reconciliation axes remain separate. |
| AD-3 | Conforms | Ports and in-process owners retain side-effect authority. |
| AD-4 | Conforms with AD-11 gap | Story 4.10 owns grouping; FUT-63 is not reciprocally mapped (R3-02). |
| AD-5 | Conforms | Candidate, Snapshot/current, baseline, and report ownership remain separated. |
| AD-6 | Conforms | Canonical actions and acknowledged-unknown safety behavior are preserved. |
| AD-7 | Diverges | Release namespace has two incompatible closed grammars (R3-07). |
| AD-8 | Conforms | Text-primary, Unicode, hostile-text, ASCII, and motion rules remain represented. |
| AD-9 | Conforms | Inherited and approved-deviation lanes remain separate and byte-exact. |
| AD-10 | Conforms | Frozen reservations, cuts, pools, FD3 workers, and immutable reports remain explicit. |
| AD-11 | Diverges | Count, reciprocity, and AD-15 semantic coverage fail (R3-01..R3-03); affected semantic rows also diverge. |
| AD-12 | Diverges | C-11 still permanently binds the reviewed point release (R3-04). |
| AD-13 | Conforms | Typed identities plus FUT-56 property acceptance are represented. |
| AD-14 | Conforms | One terminal owner, no detach, and durable finalization remain explicit. |
| AD-15 | Diverges | Story tags do not acceptance-own or gate the complete adapter matrix (R3-03). |
| AD-16 | Conforms | SQLite modes, transactions, CAS, retention, and recovery remain owned. |
| AD-17 | Conforms with AD-11 gap | Promise lifecycle stories and FUT-57..59 exist; reciprocal mapping fails (R3-02). |
| AD-18 | Conforms with AD-11 gap | Full reconciliation space exists; FUT-60..63 reciprocal mapping fails (R3-02). |
| AD-19 | Conforms | Typed precedence, provenance, validation, and no-hot-reload remain explicit. |
| AD-20 | Conforms | ARCH-LIM-1..24 remain inventoried and owned. |
| AD-21 | Conforms | Frozen cuts, scheduling, reduction, and sole current CAS remain explicit. |
| AD-22 | Conforms with AD-11 gap | Action semantics close D-07; FUT-64..65 reciprocal mapping fails (R3-02). |
| AD-23 | Diverges | Command grammar, consumer authority, and rewrite cardinality conflict (R3-05..R3-07). |
| AD-24 | Conforms | Canonical JSON, IDs, paths, fingerprints, fixed bytes, and FUT-56 are represented. |
| AD-25 | Conforms | FD3 framing, identity, cuts, EOF, cleanup, and precedence remain explicit. |

## Every AD-11 Registry Row

All 81 IDs are unique and every row has a valid owner, fixture, assertion,
aggregate command, and current/future delivery value. “Conforms” below is a
row-semantic judgment; it does not cure R3-01's false normative total.

| Row | Owner | Result | Note |
| --- | --- | --- | --- |
| AD11-CUR-01 | Story 1.3 | Conforms | Legacy CLI matrix. |
| AD11-CUR-02 | Story 1.3 | Conforms | Legacy output bytes. |
| AD11-CUR-03 | Story 1.3 | Conforms | Legacy Provider matrix. |
| AD11-CUR-04 | Story 1.3 | Conforms | Legacy inspection matrix. |
| AD11-CUR-05 | Story 1.3 | Conforms | Legacy action argv matrix. |
| AD11-CUR-06 | Story 1.4 | Conforms | Contract manifest. |
| AD11-CUR-07 | Story 1.4 | Conforms | Fixed policy bytes. |
| AD11-CUR-08 | Story 3.1 | Conforms | Fixed plan/scope bytes. |
| AD11-CUR-09 | Story 1.4 | Conforms | Fixed identity bytes. |
| AD11-CUR-10 | Story 3.1 | Conforms | Fixed assignment bytes. |
| AD11-CUR-11 | Story 3.3 | Conforms | FD3 four-frame bytes. |
| AD11-CUR-12 | Story 3.3 | Conforms | FD3 no-allocation cut. |
| AD11-CUR-13 | Story 7.15 | Conforms | Current release subcorpus. |
| AD11-CUR-14 | Story 1.3 | Conforms | Legacy Host smoke; omitted from declared count (R3-01). |
| AD11-FUT-01 | Story 1.1 | Conforms | Dependency direction and side-effect owner. |
| AD11-FUT-02 | Story 1.5 | Conforms | Configuration and limits. |
| AD11-FUT-03 | Story 1.6 | Conforms | SQLite initialization. |
| AD11-FUT-04 | Story 1.7 | Conforms | Repository CAS/unavailability. |
| AD11-FUT-05 | Story 1.8 | Conforms | Retention and capacity. |
| AD11-FUT-06 | Story 1.9 | Conforms | Runner terminal-before-reap. |
| AD11-FUT-07 | Story 2.1 | Conforms | Principal/owner authentication. |
| AD11-FUT-08 | Story 2.2 | Conforms | Promise declare/revise idempotency. |
| AD11-FUT-09 | Story 2.3 | Conforms | Boot/clock and persistent rejection. |
| AD11-FUT-10 | Story 3.2 | Conforms | Default schedule. |
| AD11-FUT-11 | Story 3.2 | Conforms | Near-tie schedule. |
| AD11-FUT-12 | Story 3.2 | Conforms | Zero-margin schedule. |
| AD11-FUT-13 | Story 3.2 | Conforms | No post-cut allocation. |
| AD11-FUT-14 | Story 3.3 | Conforms | Peer credentials and Ready. |
| AD11-FUT-15 | Story 3.3 | Conforms | Descriptor ownership and EOF. |
| AD11-FUT-16 | Story 3.3 | Conforms | Total transport precedence. |
| AD11-FUT-17 | Story 3.3 | Conforms | Report immutability. |
| AD11-FUT-18 | Story 3.4 | Gap | Cron assertion does not enumerate complete AD-15 behavior (R3-03). |
| AD11-FUT-19 | Story 3.5 | Gap | Systemd assertion does not enumerate complete AD-15 behavior (R3-03). |
| AD11-FUT-20 | Story 3.6 | Gap | Docker identity assertion does not enumerate complete AD-15 behavior (R3-03). |
| AD11-FUT-21 | Story 3.7 | Gap | PM2 identity assertion does not enumerate complete AD-15 behavior (R3-03). |
| AD11-FUT-22 | Story 3.8 | Gap | Process assertion does not enumerate complete AD-15 behavior (R3-03). |
| AD11-FUT-23 | Story 3.9 | Conforms | Candidate is not Snapshot. |
| AD11-FUT-24 | Story 3.10 | Conforms | Obligation/strict matrix. |
| AD11-FUT-25 | Story 4.1 | Conforms | Correlation vectors. |
| AD11-FUT-26 | Story 4.3 | Conforms | Duplicate cardinality. |
| AD11-FUT-27 | Story 4.4 | Conforms | History races. |
| AD11-FUT-28 | Story 4.7 | Conforms | Snapshot/current CAS. |
| AD11-FUT-29 | Story 4.8 | Conforms | Baseline races/override. |
| AD11-FUT-30 | Story 4.9 | Conforms | Eight Brief rows. |
| AD11-FUT-31 | Story 5.1 | Conforms | Routing and terminal restoration. |
| AD11-FUT-32 | Story 5.3 | Conforms | Unicode search and focus. |
| AD11-FUT-33 | Story 5.5 | Conforms | External-system boundary. |
| AD11-FUT-34 | Story 5.7 | Conforms | Accessibility states. |
| AD11-FUT-35 | Story 5.9 | Conforms | Read-only budgets/goldens. |
| AD11-FUT-36 | Story 6.1 | Conforms | Action enum matrix. |
| AD11-FUT-37 | Story 6.3 | Conforms | Confirmation matrix. |
| AD11-FUT-38 | Story 6.5 | Conforms | Pool-before-admission. |
| AD11-FUT-39 | Story 6.6 | Conforms | Operation phases and IDs. |
| AD11-FUT-40 | Story 6.7 | Gap | Executor assertion does not enumerate complete AD-15 behavior (R3-03). |
| AD11-FUT-41 | Story 6.9 | Conforms | Action outcome precedence. |
| AD11-FUT-42 | Story 6.10 | Conforms | No detach/finalization. |
| AD11-FUT-43 | Story 6.12 | Conforms | Action/accessibility aggregate. |
| AD11-FUT-44 | Story 7.1 | Diverges | Moving stable conflicts with C-11's permanent point binding (R3-04). |
| AD11-FUT-45 | Story 7.2 | Conforms | Traditional POSIX locks. |
| AD11-FUT-46 | Story 7.6 | Diverges | Reciprocal owner and rewrite cardinality fail (R3-02/R3-05/R3-06). |
| AD11-FUT-47 | Story 7.7 | Conforms | Exact FD4 bytes. |
| AD11-FUT-48 | Story 7.7 | Conforms | D-Bus handshake/shared cut. |
| AD11-FUT-49 | Story 7.9 | Conforms | Owner-takeover chronology. |
| AD11-FUT-50 | Story 7.10 | Conforms | KnownGood publication. |
| AD11-FUT-51 | Story 7.12 | Conforms | FirstInstall absence/recovery. |
| AD11-FUT-52 | Story 7.14 | Conforms | Rollback displaced-source direction. |
| AD11-FUT-53 | Story 7.3 | Diverges | Reciprocal owner and command grammar fail (R3-02/R3-07). |
| AD11-FUT-54 | Story 7.15 | Conforms | Exact-artifact Host smoke. |
| AD11-FUT-55 | Story 7.15 | Conforms | Isolated service-manager rows. |
| AD11-FUT-56 | Story 1.4 | Conforms | Canonical/identity properties. |
| AD11-FUT-57 | Story 2.4 | Gap | Heartbeat row is not reciprocally mapped to AD-11 (R3-02). |
| AD11-FUT-58 | Story 2.5 | Gap | Closure row is not reciprocally mapped to AD-11 (R3-02). |
| AD11-FUT-59 | Story 2.6 | Gap | Agent-interface row is not reciprocally mapped to AD-11 (R3-02). |
| AD11-FUT-60 | Story 4.2 | Gap | Outcome row is not reciprocally mapped to AD-11 (R3-02). |
| AD11-FUT-61 | Story 4.5 | Gap | Unmanaged/abandoned row is not reciprocally mapped to AD-11 (R3-02). |
| AD11-FUT-62 | Story 4.6 | Gap | Safe-to-stop row is not reciprocally mapped to AD-11 (R3-02). |
| AD11-FUT-63 | Story 4.10 | Gap | Grouping row is not reciprocally mapped to AD-11 (R3-02). |
| AD11-FUT-64 | Story 6.4 | Gap | Revalidation row is not reciprocally mapped to AD-11 (R3-02). |
| AD11-FUT-65 | Story 6.11 | Gap | Linear/machine row is not reciprocally mapped to AD-11 (R3-02). |
| AD11-FUT-66 | Story 7.4 | Diverges | Discovery uses C-21 while C-11 requires the forbidden authority (R3-05). |
| AD11-FUT-67 | Story 7.15 | Conforms | Both pairs through all effects/cuts. |

## Executable Evidence and Final Gate

| Check | Result |
| --- | --- |
| Pinned blob digest and worktree equality | PASS |
| Frozen compatibility oracle | PASS — 90 inherited plus 4 approved deviations |
| Canonical contract validator | PASS |
| Release oracle validator | PASS |
| Legacy Host smoke | PASS |
| Architecture aggregate | Expected override-only exit 1 at the planning-root tombstone assertion |
| JSON parse and row field/ID uniqueness | PASS — 81 rows, 14 current and 67 future |
| Declared row count versus actual rows | FAIL — 68 versus 81 |
| AD-11 reciprocal owner map | FAIL — 11 row owners omitted; one aggregate owner has no row |
| Semantic architecture review | FAIL — R3-03 through R3-07 |

PASS requires all seven findings to be removed from a newly pinned `epics.md`
blob and a repeat independent audit to return zero findings. This draft remains
nonassignable and not implementation authority.
