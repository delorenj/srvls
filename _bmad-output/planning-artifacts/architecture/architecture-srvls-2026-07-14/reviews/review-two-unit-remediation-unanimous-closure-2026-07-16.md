---
title: "srvls Architecture Two-Unit Remediation Unanimous Closure"
type: architecture-review
status: final
created: 2026-07-16
updated: 2026-07-16
reviewer: independent-configured-two-unit-reviewer
review_mode: adversarial-two-unit-remediation-unanimous-closure
reviewed_base_commit: d4515067af8314cadf979da7b17921fbafc92d21
reviewed_worktree_spine_sha256: 754b956cc4fa345017415257ce2f3e295ad421d6ea6e9ff7d2b0d8555b42aee1
reviewed_spine_line_count: 1758
reviewed_artifact: _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md
verdict: approved
blocking_status: cleared
original_probe_count: 20
original_acceptance_findings_retested: 13
prior_remediation_findings_retested: 12
finding_count: 0
blocking_findings: 0
high_findings: 0
moderate_findings: 0
---

<!-- markdownlint-disable MD013 MD025 -->

# Architecture Review: Two-Unit Remediation Unanimous Closure

## Verdict

**APPROVED. Blocking status: CLEARED. Finding count: 0.**

Two independently reconstructed implementations now converge on the same
request admission, internal-process exclusion, process-scope failure, immutable
report, Snapshot, release-recovery, and storage results. The exact frozen spine
reviewed here closes REALITY-B01 without weakening any previously closed
contract. No Seed or Deferred item is needed to make the architecture
implementable.

Approval applies only to the exact 1,758-line candidate with SHA-256
`754b956cc4fa345017415257ce2f3e295ad421d6ea6e9ff7d2b0d8555b42aee1`.

## Frozen Target and Review Basis

The reviewer read the complete current `ARCHITECTURE-SPINE.md`, including all
AD-1 through AD-25 decisions, limits, structural seed, traceability, and
Deferred sections. The review also replayed the original two-unit divergence
report, its acceptance report, every two-unit remediation gate/rerun/final/
closure/reality finding, and the required technology, storage, trace, and
fixture seams.

The candidate was hashed before semantic review and again after this report was
created. Both reads produced the exact digest above. The spine, source,
`tasks.md`, and every existing review report remained untouched by this
reviewer.

## Independently Reconstructed Units

The critical reality seam was reconstructed without importing the prose's
conclusions as implementation behavior.

### Unit C-A — Coordinator and worker-lifecycle implementation

C-A owns deterministic LPT batch transitions, the pre-spawn dispatch epoch,
absolute deadlines, successful PID ownership, process-group and executable
identity refinement, Hello/Ready authentication, terminal transport reports,
typed cancellation, exact cleanup, result admission, and eventual reaping. Its
only pre-root states after a successful PID return are `OwnedSpawnV1` followed
by either a complete `SpawnedWorkerRootV1` or `UnrootableSpawnV1`
(`SPINE:316-419`, `SPINE:597-634`, `SPINE:1314-1572`).

### Unit C-B — Direct-process collector and reducer implementation

C-B receives one frozen `SelfProcessSetV1`, collects direct process candidates
without rediscovery, and applies the exact ownership-hint, winner, conflict,
self-suppression, and retained-diagnostic rules. It cannot suppress from a
partial root and cannot start Host reads while the coordinator's process gate
or unrootable-child absence barrier is closed (`SPINE:524-671`).

### Runtime/configuration pair

The runtime scheduler and configuration validator independently consume the
same batch assignment, Ready/failure outcome, root-freeze, dispatch epoch,
process barrier, completion trace, half-open cut, and mandatory one-nanosecond
headroom. Setup consumes the scope budget rather than extending it
(`SPINE:316-419`, `SPINE:873-923`).

### Remaining original pairs

The Promise/repository, action/executor, configuration/history, and
installer/migration pairs were reconstructed against the frozen plan,
repository, action, policy, release, and recovery contracts. They remain
convergent; their individual regression results appear below.

## REALITY-B01 Closure Proof

### State construction is total before a process request

| Coordinator event | Required state and consequence | Result |
| --- | --- | --- |
| Spawn fails before returning a child PID | No owned record or self root exists; AD-25 synthesizes `worker-spawn`. | **PASS** |
| Spawn returns a child PID | Before any later setup read, C-A records `OwnedSpawnV1` with request ID, exact PID, and the parent's unreaped owned-child handle. | **PASS** |
| Birth, executable, and dedicated process group are all recorded | The owned record refines to complete `SpawnedWorkerRootV1`; the root remains frozen until its group is proved empty. | **PASS** |
| Any required pre-root construction fails after PID return | The record becomes `UnrootableSpawnV1` with the exact PID/handle, tagged group-setup result, and reap evidence. No partial root is invented. | **PASS** |
| Group setup is `succeeded(pgid)` | Cleanup targets only that exact dedicated group; absence requires exact-child reap and zero `/proc` members for that exact group. | **PASS** |
| Group setup is `not-attempted` or `failed` | Cleanup targets the exact unreaped owned child PID and never signals or suppresses the inherited coordinator group. | **PASS** |
| A current or superseded generation retains an unrootable child | The coordinator-wide barrier survives supersession; no current or later process request or Host read is admitted until exact absence. | **PASS** |
| Absence misses the process scope or generation cut | The process scope receives `worker-timeout`, unless its earlier AD-25 failure already owns the report; both cases perform no Host read and reopen the gate. | **PASS** |
| Reap completes only after the immutable failure cut | `WorkerReapEvidenceV1` records cleanup truth but cannot rewrite report bytes, DiagnosticId, Snapshot, or current truth. | **PASS** |

The normative transition is constructible at PID return and total at the
request boundary. `OwnedSpawnV1` is deliberately internal and transient;
`SelfProcessSetV1` contains only complete roots. A child that cannot become a
complete root must instead cross the coordinator-wide absence barrier before
process Host truth can exist (`SPINE:597-634`, `SPINE:1378-1385`).

### In-flight-owned-spawn adversarial challenge

The reviewer specifically challenged whether an older in-progress
`OwnedSpawnV1` could escape both the root freeze and the
`UnrootableSpawnV1` barrier while a later process worker reads `/proc`. It
cannot:

1. Within the process worker's batch, AD-10 step 5 waits for every member to
   reach authenticated Ready or one terminal failure before any batch request.
   A still-in-progress owned spawn is neither and therefore blocks the request.
2. A prior batch cannot release its requests or advance the ordered batch
   transition while one member has no Ready/failure outcome. Once terminal, a
   pre-root owned spawn becomes unrootable; once Ready, it has a complete root.
3. A later batch cannot spawn after the process worker closes the worker-spawn
   gate.
4. Supersession cancellation closes result admission and is terminal under
   AD-25. Failure to refine a PID-owning record produces the coordinator-wide
   `UnrootableSpawnV1`, which the same/later-generation process barrier must
   resolve.
5. AD-13's final invariant is therefore literal: before request release, every
   earlier possibly live internal process is either carried by a complete
   frozen root/group or proved absent (`SPINE:326-367`, `SPINE:629-634`,
   `SPINE:1562-1569`).

This rejects the apparent counterexample where the default Docker lane remains
in setup while ordinary 15- and 20-second lanes complete and a process lane
starts at second 25. The initial batch's Ready/failure barrier forbids those
ordinary requests from dispatching while that Docker spawn is still only
owned. A failure trace may time out scopes, but it cannot expose an internal
child as Host truth or create a second legal schedule.

### Interleaving regression

| Adversarial interleaving | Required convergent result | Result |
| --- | --- | --- |
| Ready process sibling plus post-PID setup failure in the same batch | Failure refines to unrootable; process waits for absence or times out without Request/Host read. | **PASS** |
| Ready process in a later batch or generation plus retained failed child | Complete roots are carried; unrootable children are proved absent across generations before request. | **PASS** |
| Birth/executable failure after successful group setup | Exact group termination, exact-child reap, and zero exact-PGID membership are all required. | **PASS** |
| Group setup failure while the child remains in the coordinator group | Exact PID cleanup only; no inherited-group signal, membership, or suppression. | **PASS** |
| Process worker fails while the absence barrier is pending | Its earlier AD-25 report wins, no Host read occurs, the gate reopens, and cleanup remains visible to the next process barrier. | **PASS** |
| Process deadline equals final absence proof | Half-open admission rejects equality as timeout; mailbox or reap observation order cannot change the report. | **PASS** |
| Child is reaped after the process failure cut | Reap evidence advances, but immutable collection and diagnostic bytes do not. | **PASS** |
| Unrelated same-inode or same-name srvls process is live | It is not self merely by executable, ancestry, name, command, cwd, or partial cgroup evidence. | **PASS** |

The named IPC fixtures exercise the same- and later-generation failure cases,
absence-cut miss, no unrelated-group signal or suppression, no leaked internal
Observation, gate reopening, and no later-reap rewrite (`SPINE:452-466`).

## Original Twenty-Probe Closure Matrix

| Finding | Result | Current binding contract |
| --- | --- | --- |
| DVG-B01 — common reconciliation cut | **CLOSED** | CollectionPlanV1 freezes every comparison input and reducer use (`SPINE:924-998`). |
| DVG-B02 — Snapshot/Findings atomicity | **CLOSED** | One Snapshot transaction owns reports, diagnostics, observations, findings, pins, and latest-generation CAS (`SPINE:714-784`). |
| DVG-B03 — current-truth generation | **CLOSED** | Persisted latest requested generation alone may move repository/display current truth (`SPINE:143-192`, `SPINE:386-397`). |
| DVG-B04 — action-plan handoff | **CLOSED** | Immutable ActionPlanV1, identity, expiry, submit CAS, and OperationId allocation are explicit (`SPINE:999-1023`). |
| DVG-B05 — durable outcome vs bounded exit | **CLOSED** | Storage-failure exception preserves the last durable nonterminal phase for next-start recovery (`SPINE:672-692`, `SPINE:714-784`). |
| DVG-B06 — policy fingerprint preimage | **CLOSED** | Byte-complete PolicySnapshotV1 CanonicalJsonV1 and domain-separated digest are normative (`SPINE:1226-1288`). |
| DVG-B07 — upgrade writer quiescence | **CLOSED** | ReleaseAdmissionV1 gates every ordinary stateful entry before SQLite (`SPINE:1024-1055`). |
| DVG-B08 — crash-safe upgrade state machine | **CLOSED** | Checksummed replacement, pending-before-effect, complete-after-readback, resume, and recovery truth table are total (`SPINE:1056-1194`). |
| DVG-H01 — lifecycle replay order | **CLOSED** | Gap-free event sequence and authoritative projections prevent independent refolds (`SPINE:785-805`). |
| DVG-H02 — scope identity | **CLOSED** | ScopeIdV1 tagged bytes and ordered ScopeManifestV1 define identity, equality, and ordering (`SPINE:1289-1313`). |
| DVG-H03 — obligation drift | **CLOSED** | Obligation is frozen in CollectionPlanV1 and echoed/validated by workers (`SPINE:924-998`, `SPINE:1482-1540`). |
| DVG-H04 — diagnostic construction | **CLOSED** | Post-evidence candidate refs, canonical ordinals, byte grammar, and atomic rewrite are constructible (`SPINE:524-596`). |
| DVG-H05 — equality and late reports | **CLOSED** | Atomic registry plus strict-before scope/generation cuts make equality timed out (`SPINE:399-418`). |
| DVG-H06 — overlap and fairness | **CLOSED** | Latest-wins cancellation, retained attempt evidence, LPT epochs, and latest-only CAS are explicit (`SPINE:316-397`). |
| DVG-H07 — process attribution | **CLOSED** | Complete roots/unrootable absence plus deterministic hints, winner, conflicts, and retained suppression diagnostics converge (`SPINE:597-671`). |
| DVG-H08 — launch/verification boundary | **CLOSED** | Durable launch receipt and OperationId-correlated post-launch verification are owned by AD-22 (`SPINE:999-1023`). |
| DVG-H09 — terminal outcome owner | **CLOSED** | OperationCoordinator alone owns FR-40 and the terminal revision CAS (`SPINE:193-243`, `SPINE:672-692`). |
| DVG-H10 — historical decision version | **CLOSED** | Persisted decision-contract version renders old results without silent recomputation (`SPINE:806-842`). |
| DVG-H11 — backup/restore ownership | **CLOSED** | Release transaction owns backup hashes, sidecars, fsync/readback, validation, and restore (`SPINE:1024-1194`). |
| DVG-M01 — canonical historical policy | **CLOSED** | Every artifact references the complete normalized PolicySnapshotV1; unsupported versions are typed read-only (`SPINE:1226-1288`). |

Result: **20 of 20 original probes closed; zero residual divergence.**

## Original Acceptance-Finding Regression

| Finding | Result | Closure evidence |
| --- | --- | --- |
| ACC-B01 — accepted baseline missing from cut | **CLOSED** | AcceptedBaselineCutV1 embeds the complete comparison projection and forbids a later baseline lookup (`SPINE:941-958`, `SPINE:984-997`). |
| ACC-B02 — nonterminal operations missing from cut | **CLOSED** | OperationCutV1 is frozen in the same admission and reconciliation reads it only from the plan (`SPINE:955-958`, `SPINE:973-997`). |
| ACC-B03 — release gate lost on crash | **CLOSED** | Permission-restricted ReleaseAdmissionV1 persists independently and is checked before SQLite (`SPINE:1024-1055`). |
| ACC-B04 — plan fingerprint ambiguity | **CLOSED** | CollectionPlanV1 has one complete ordered canonical byte stream and domain-separated hash (`SPINE:1273-1288`). |
| ACC-H01 — scope grammar ambiguity | **CLOSED** | Every Provider variant has a tagged, length-total ScopeIdV1 grammar (`SPINE:1289-1313`). |
| ACC-H02 — diagnostic ordinal unconstructible | **CLOSED** | Candidate references exist after evidence; coordinator and worker partitions merge before final ID rewrite (`SPINE:524-596`). |
| ACC-H03 — dedup decision contract missing | **CLOSED** | Exact ownership evidence, self rules, deterministic winner, conflicts, and retained diagnostics are complete, including the pre-root barrier (`SPINE:597-671`). |
| ACC-H04 — history outside read cut | **CLOSED** | ResourceHistoryCutV1 freezes revision, rows, timestamps, and completeness in the plan (`SPINE:959-963`). |
| ACC-H05 — non-atomic plan admission | **CLOSED** | One repository BEGIN IMMEDIATE operation allocates, reads, validates, inserts, and pins the plan atomically (`SPINE:924-982`). |
| ACC-H06 — journal tear/effect boundary | **CLOSED** | Every effect is bracketed by checksummed atomic pending and complete writes with fsync/readback (`SPINE:1056-1142`). |
| ACC-H07 — successful validation erases rollback | **CLOSED** | Commit retains exactly one KnownGoodReleaseV1; explicit rollback starts a new transaction (`SPINE:1163-1189`). |
| ACC-M01 — wall sample ambiguity | **CLOSED** | Paired boot and UTC wall cuts freeze generation start/end and stamp every downstream artifact (`SPINE:931-940`, `SPINE:984-994`). |
| ACC-M02 — release phase/recovery output gap | **CLOSED** | Every durable internal step maps to one public event, UX label, and final recovery result (`SPINE:1195-1224`). |

Result: **13 of 13 acceptance findings closed.**

## Remediation, Rerun, Final, and Reality Regression

| Finding | Result | Closure evidence |
| --- | --- | --- |
| NEW-B01 — baseline projection/no late lookup | **CLOSED** | AcceptedBaselineCutV1 is complete and immutable in the atomic plan. |
| NEW-B02 — bounded worker envelope/oversize | **CLOSED** | Request/result identities, byte caps, exact-boundary/one-byte-over behavior, and Collector projections are exhaustive (`SPINE:1469-1572`). |
| NEW-B03 — KnownGood commit-decision crash truth | **CLOSED** | Commit decision is irreversible; publication and ready/terminal completion follow; rollback is new work. |
| NEW-H01 — diagnostic reference/grammar | **CLOSED** | Post-evidence references and canonical bytes are total. |
| NEW-H02 — self set and owner winner | **CLOSED** | Complete-root freeze plus unrootable absence closes the last reality edge; winner/conflict behavior remains deterministic. |
| NEW-H03 — authenticated recovery bypass | **CLOSED** | Attempt-bound, one-use FD4 validation is owner-authenticated, read-only, non-forwardable, and fail-closed (`SPINE:1101-1137`). |
| NEW-H04 — release event/UX mapping | **CLOSED** | Every durable step and crash-recovery path has one public projection. |
| RERUN-B01 — oversize Collector outcome | **CLOSED** | Both request/result oversize reasons create one canonical AD-5 report without a seventh outcome. |
| RERUN-B02 — replacement recovery owner | **CLOSED** | Active attempt publication, peer identity, PID reuse, and second-crash behavior are explicit. |
| FINAL-B01 — synthesized diagnostic bytes | **CLOSED** | Seven-field parameter matrix, evidence cut, subject, occurrence, and final ID are byte-complete (`SPINE:1398-1480`). |
| FINAL-H01 — deterministic dispatch epoch | **CLOSED** | Runtime and configuration use one pre-spawn epoch/batch/barrier transition and identical trace. |
| REALITY-B01 — live failed pre-root child | **CLOSED** | PID ownership, unrootable absence, exact cleanup, no inherited-group behavior, no Host read, and immutable reap handling are total. |

Result: **12 of 12 named remediation findings closed.**

## Hello, Ready, Timing, and Diagnostic Gate

| Contract | Result | Evidence |
| --- | --- | --- |
| Reserved same-binary route and no discovery | **PASS** | Exact current executable, sole raw worker token, authenticated FD3, no clap/config/XDG/SQLite/PATH rediscovery (`SPINE:1314-1329`, `SPINE:1569-1572`). |
| FD3 framing and direction | **PASS** | Versioned length-prefixed canonical JSON, four-frame direction, limits, EOF, trailing, replay, and mismatch behavior are exhaustive (`SPINE:1330-1376`). |
| Parent-to-child authentication | **PASS** | Child checks FD3 stream, SO_PEERCRED parent PID/UID, and executable device/inode. |
| Child-to-parent authentication | **PASS** | Ready's first byte carries exactly one SCM_CREDENTIALS record plus all expected identity echoes (`SPINE:1343-1366`). |
| Setup/work timing | **PASS** | Dispatch boot epoch, absolute scope/generation cuts, full setup-within-budget, and strict-before equality are shared. |
| Failure selection and EOF | **PASS** | Deadline-first causal matrix, zero/partial EOF, bare exits, signals, trusted results, and cleanup origin are deterministic (`SPINE:1387-1480`). |
| Diagnostic identity | **PASS** | Failure cut freezes all seven parameter values; later cleanup/reap cannot alter candidate bytes or final DiagnosticId. |
| Process ownership | **PASS** | Exact PID/birth/device-inode/group evidence, deterministic hint strength/order, conflicts, and retained diagnostics are complete. |

## Release, Storage, Installer, and Trace Gate

| Required seam | Result | Binding evidence |
| --- | --- | --- |
| SQLite fresh/existing initialization | **PASS** | Ordered WAL, synchronous FULL, foreign-key and busy-timeout readbacks fail closed before transactions (`SPINE:714-742`). |
| Exact artifact ABI | **PASS** | `readelf --version-info` rejects imports above GLIBC_2.42 and the same artifact smokes in the oldest supported runtime (`SPINE:491-507`). |
| Absolute ExecStart rewrite | **PASS** | Every managed absolute path, including `srvls-metrics.service` and `srvls-snapshot.service`, receives loaded readback and whole-pair rollback (`SPINE:508-523`). |
| Timer-triggered validation | **PASS** | Each paired timer must advance and its service must succeed against the activated pair (`SPINE:1138-1157`). |
| Crash-persistent admission | **PASS** | Every stateful entry checks ReleaseAdmissionV1 before SQLite and refuses non-ready/nonterminal state. |
| Upgrade effect ordering | **PASS** | Checksummed atomic replacement plus write-ahead pending and write-after complete surround every effect. |
| KnownGood and rollback | **PASS** | Exactly one KnownGoodReleaseV1 is retained after validation; rollback is an explicit new transaction. |
| Public release truth | **PASS** | Durable phases map to public events, UX states, skipped/resumed behavior, and four final results. |
| UJ-5 | **PASS** | Trace remains bound to exact duplicate evidence and retained timestamped resource history (`SPINE:1715`). |
| Seed and Deferred discipline | **PASS** | Structural modules carry only already-decided contracts; deferred items do not reopen accepted invariants (`SPINE:1626-1695`, `SPINE:1738-1758`). |

## Required Fixture Gate

AD-11 names property, concurrency, crash, IPC, timer, and rollback fixtures for
every acceptance seam. In particular, the frozen suite covers:

- complete PolicySnapshotV1 JSON, ScopeIdV1/ScopeManifestV1 bytes, arbitrary
  diagnostic subjects/parameters, duplicates, and post-evidence reference
  resolution;
- default, pathological, zero-margin, every-process-position, nonzero setup,
  multi-batch, same-generation, and superseded-generation schedule traces;
- exact PID/group/cgroup ownership, Provider children and grandchildren,
  escaped descendants, weak-evidence emission, ties, conflicts, and retained
  suppression diagnostics;
- every Hello/Ready credential and echo failure, replay, partial/oversized
  frames, exact-boundary and one-byte-over messages, all mismatches, stdout and
  stderr isolation, timeout, signal, EOF, cleanup, and no-discovery behavior;
- the post-PID root-construction failure with same/later-generation process
  workers, exact absence, missed-cut timeout, no Host read, no inherited-group
  signal/suppression, and later-reap non-rewrite;
- SQLite migrations and recovery, every release pending/complete crash edge,
  bad checksums and torn manifests, dead/replacement recovery owners, FD4
  forwarding refusal, whole-pair restore, KnownGood publication, explicit
  rollback, absolute ExecStart readback, and timer-triggered success
  (`SPINE:420-490`).

No named acceptance behavior remains dependent on a future test-design choice.

## Pair Verdicts

| Pair | Verdict | Reason |
| --- | --- | --- |
| Promise lifecycle / reconciliation and storage | **ACCEPTED** | One atomic frozen plan and one atomic Snapshot/current transaction. |
| Collection workers / process collector and reducer | **ACCEPTED** | Every internal child is complete-root self truth or absent before Host read. |
| Action planning / execution, verification, and shutdown | **ACCEPTED** | One durable handoff, launch boundary, evidence lane, and terminal owner. |
| Runtime scheduling / configuration validation | **ACCEPTED** | One event transition, budget, barrier, and half-open cutoff model. |
| Configuration / historical policy interpretation | **ACCEPTED** | Canonical policy and decision versions prevent current-default reinterpretation. |
| Installer / SQLite migration and recovery | **ACCEPTED** | Admission, write ordering, whole-pair truth, recovery ownership, and rollback converge. |

## Findings

No blocking, high, moderate, or low finding was identified against the frozen
candidate.

## Mechanical Validation Record

| Validation | Command or method | Result |
| --- | --- | --- |
| Frozen identity | `sha256sum .../ARCHITECTURE-SPINE.md` before and after semantic review | **PASS** — exact `754b956...aee1` digest both times |
| Complete source read | line-bounded reads covering line 1 through line 1,758 and EOF | **PASS** |
| Architecture linter | `uv run .agents/skills/bmad-architecture/scripts/lint_spine.py --workspace _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14` | **PASS** — `ok: true`, zero findings |
| AD integrity | ordered AD heading extraction | **PASS** — AD-1 through AD-25 exactly once and in order |
| ARCH-LIM integrity | ordered limits-table extraction | **PASS** — ARCH-LIM-1 through ARCH-LIM-23 exactly once |
| Adversarial reality replay | two independent state machines across PID/setup/Ready/failure/process/reap cuts | **PASS** — one result for every legal interleaving |
| Markdown lint | `markdownlint-cli2` with canonical UX configuration | **PASS** — zero errors |
| Tracked whitespace | `git diff --check` | **PASS** — no whitespace errors |
| New-report whitespace | `git diff --no-index --check /dev/null <this-report>` | **PASS** — no whitespace errors |
| Required-term inspection | exact search over plan, FD3, ownership, diagnostic, release, SQLite, ABI, timer, UJ-5, and fixture anchors | **PASS** |
| Changed-file scope | `git status --short` before and after review | **PASS** — reviewer added only this report; concurrent spine and earlier-report changes were not edited |

## Final Status

**APPROVED.** The exact frozen spine SHA-256 is
`754b956cc4fa345017415257ce2f3e295ad421d6ea6e9ff7d2b0d8555b42aee1`.
All original divergence, acceptance, remediation, final, and reality findings
are closed with zero residual two-unit implementation divergence.
