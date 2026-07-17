# Epics Review: Architecture Divergence

<!-- markdownlint-disable MD013 -->

## Review identity

| Field | Value |
| --- | --- |
| Reviewer | Sir Fix-a-Lot, independent read-only implementation and architecture divergence reviewer |
| Target commit | b959e2ada0f61d6928dc270a793280b0acd6217e |
| Reviewed artifact | _bmad-output/planning-artifacts/epics.md from the target commit |
| Settled target SHA-256 | 0189960e42776cf3f5fe86dcf3cc3344ce307d987877d9c5600277b43b1f1523 |
| Measured target SHA-256 | 0189960e42776cf3f5fe86dcf3cc3344ce307d987877d9c5600277b43b1f1523 |
| Target Git blob | 411fef8046992d1222dcc09ac90989fd1b15a5f5 |
| Architecture authority | _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md from the target commit |
| Architecture file SHA-256 | 28a103267a8e4ae5411c314bc2f9c0b62b694352e6e91c2522a2271df16ff575 |
| Architecture body SHA-256 | 06df98f6d201abd47289d6c6771e15b83fb9d8a6c856a3a67e2e20e178a670aa |
| Architecture Git blob | 93e4ecc0799bf251bee6a95522dd490a577e083a |
| Verdict | **FAIL** |
| Findings | 30 |

## Verdict

**FAIL.** The settled epics digest is exact, but zero-finding acceptance is not met. Thirty independent findings allow two implementations to satisfy the story text while producing different behavior, bytes, durable state, recovery outcomes, Host effects, or CI evidence. Several story clauses also directly conflict with the final architecture spine.

This verdict is about the acceptance authority in the reviewed epics artifact. It does not assert that implementation already contains these defects. No implementation was reviewed or changed.

## Scope and digest proof

The review used the immutable Git objects at commit b959e2a. The target epics artifact is 2,810 lines and 144,820 bytes. Its measured SHA-256 equals the required settled value exactly. The target commit changes only epics.md relative to its parent.

The complete 3,335-line final architecture spine was read as the normative authority. The review covered AD-1 through AD-25, the complete AD-11 acceptance matrix, ARCH-LIM-1 through ARCH-LIM-24 and their derived formulas, ARCH-HOST-1, the normative structural seed, the traceability closure, and all named binary, storage, IPC, release, consumer, and CI contracts.

The repository aggregate architecture-contract command was also run against the target state:

- Compatibility replay passed.
- Contract fixtures, IPC fixtures, release fixtures, and the legacy Host smoke lane passed.
- The aggregate gate exited nonzero at planning quarantine with: “planning-root tombstone does not fail closed”.

That failure is direct executable evidence for Finding 1; it is not used as a substitute for the remaining textual trace.

## Method

1. Resolve the abbreviated target to its full commit and read both reviewed artifacts through Git object storage.
2. Hash the exact epics bytes and compare them to the user-supplied settled digest.
3. Read the complete final architecture spine, including every normative table and acceptance fixture obligation.
4. Enumerate all 55 stories and trace their declared AD references, implementation boundaries, dependencies, acceptance criteria, and aggregate-gate language.
5. For each architecture contract, ask whether the story text fixes one observable implementation or permits multiple implementations with different canonical bytes, durable transitions, process behavior, Host effects, recovery results, or test evidence.
6. Run the checked-in aggregate architecture-contract gate and inspect the planning-quarantine failure.
7. Keep findings independent: each finding names a distinct choice that two story-compliant implementations can make differently.

Prior review conclusions were not treated as evidence. The controlling evidence is the target Git object, the final architecture spine at the same commit, and the checked-in validator behavior.

## AD-1 through AD-25 coverage

| Decision | Primary story coverage inspected | Result |
| --- | --- | --- |
| AD-1 | 1.1, 1.6 | Story layering is present; exact architecture-boundary enforcement remains open in Finding 6. |
| AD-2 | 2.1–2.5, 3.3–3.8, 4.1–4.6 | Lifecycle and identity ownership are broadly traced; persistence ambiguity remains in Finding 10. |
| AD-3 | 1.1, 1.6, 1.8, 6.1, 6.5 | Typed ports are named; mutation execution conflicts remain in Finding 19. |
| AD-4 | 4.9 | Absolute grouping tiers are acceptance-owned without a separate finding. |
| AD-5 | 1.6–1.7, 3.1, 3.8, 4.1–4.8, 6.7 | Snapshot and durable truth are traced; retention and capacity diverge in Finding 9. |
| AD-6 | 1.6, 4.5–4.6, 6.1–6.8, 7.2, 7.6, 7.8 | Action and release ownership is traced; Findings 15–19 and 26 cover conflicting state and execution contracts. |
| AD-7 | 1.2, 1.8, 2.5, 3.9, 5.1, 5.6–5.7, 6.8, 7.9 | Profile routing is named; the human-linear release interface is incomplete in Finding 29. |
| AD-8 | 1.3, 2.1, 2.5, 3.9, 5.1–5.7, 6.1, 6.8, 7.9 | Canonical presentation is traced; newline and search behavior diverge in Findings 4–5. |
| AD-9 | 1.2, 2.1, 2.5, 3.9, 5.1, 5.6, 6.8, 7.4, 7.7, 7.9 | Meaning preservation is named; compatibility, consumer, and release-surface ambiguity remains in Findings 3, 23, and 29. |
| AD-10 | 1.8, 3.1, 3.8, 5.5, 6.5–6.6, 7.2 | Frozen scheduling is substantially represented; FD3 preallocation and timing gaps remain in Finding 13. |
| AD-11 | All epics through story-level references and aggregate claims | The matrix was checked obligation by obligation; Findings 7, 13–14, 20–21, 23–25, 27–30 show uncovered or unfrozen rows. |
| AD-12 | 1.1, 7.1, 7.3–7.9 | Rust release intent is present; exact toolchain and ABI evidence diverges in Finding 20. |
| AD-13 | 1.3, 2.1, 2.5, 3.2–3.9, 4.1, 4.3, 4.9, 5.3–5.6, 6.3, 7.1 | Typed identity is broadly traced; provider identity and release type names diverge in Findings 11 and 22. |
| AD-14 | 1.2, 1.8, 3.2, 3.7, 5.1–5.6, 6.6, 6.8, 7.2, 7.5, 7.9 | Deterministic ordering is named; exact search and FD3 ordering gaps remain in Findings 5 and 13. |
| AD-15 | 1.8, 3.2–3.7, 6.1–6.5, 6.8, 7.2, 7.4–7.5, 7.9 | Typed Host execution is named; child-process mutation divergence remains in Finding 19. |
| AD-16 | 1.5–1.7, 3.8, 4.4, 4.7, 6.4, 7.3, 7.6, 7.8–7.9 | SQLite and atomic truth are traced; exact initialization, recovery, and state-machine gaps remain in Findings 8–9 and 26–28. |
| AD-17 | 1.5–1.6, 2.1–2.5, 4.2, 4.5 | Lifecycle persistence is traced; invalid intent disposition diverges in Finding 10. |
| AD-18 | Most collection, reconciliation, and presentation stories | Evidence ownership is broad; provider identity and direct-process boundaries diverge in Findings 11–12. |
| AD-19 | 1.4, 2.2, 5.7 | Provenance is traced; exact configuration and SQLite pragma enforcement remains open in Finding 8. |
| AD-20 | 1.4–1.5, 1.7–1.8, 2.2–2.3, 3.1–3.2, 3.9, 4.2, 4.4, 4.6–4.7, 5.3, 5.7, 6.2–6.6, 7.1–7.9 | Limits are referenced globally; exact limit ownership is summarized below and Findings 8–9, 13–14, 17, 21, and 25 remain. |
| AD-21 | 1.3–1.4, 2.1–2.4, 3.1, 3.7–3.8, 4.1–4.8, 5.5, 6.2, 6.4, 6.7 | Frozen cuts are traced; ActionPlan identity allocation diverges in Finding 16. |
| AD-22 | 1.6–1.7, 4.6, 6.1–6.8, 7.2, 7.6, 7.9 | Action durability is traced; Findings 15–18 and 26 cover enum, allocation, phase, and terminal-outcome conflicts. |
| AD-23 | 1.5, 1.7, 6.4, 7.1–7.9 | Release and locking are traced; exact lock, type, recovery, and consumer gaps remain in Findings 21–29. |
| AD-24 | 1.3–1.5, 2.1–2.5, 3.1–3.2, 3.8–3.9, 4.1, 4.3–4.4, 4.7–4.9, 6.2, 6.4, 6.7–6.8, 7.1, 7.3–7.9 | Closed schemas are referenced; Findings 4, 13, 22, and 24–28 identify incompatible schema choices. |
| AD-25 | 1.3, 1.8, 3.1–3.8, 7.2, 7.9 | Same-binary FD3 is traced; exact protocol and lifecycle divergence remains in Findings 13–14. |

## AD-11 acceptance-matrix coverage

| AD-11 obligation family | Story evidence inspected | Review result |
| --- | --- | --- |
| Current pre-implementation inventory and aggregate command | 1.1, 1.8, 5.7, 6.8, 7.9 | Aggregate language exists, but target placement violates quarantine and exact future ownership is not frozen; Findings 1, 6, and 30. |
| Promise lifecycle, idempotency, boot and clock discontinuity | 2.1–2.5 | Broad acceptance coverage exists; invalid persistent-intent disposition remains ambiguous; Finding 10. |
| Migrations, crash recovery, configuration precedence, invalid values | 1.4–1.7, 7.3, 7.6–7.8 | Exact SQLite and release recovery contracts are not fully owned; Findings 8–9 and 26–28. |
| Reconciliation axes, classification, safe-to-stop, grouping | 4.1–4.9 | Story acceptance is sufficiently specific for this review. |
| Retention and every AD-20 limit | 1.4, 1.7, 2.2, 4.4, 6.4–6.7, 7.5–7.9 | Alternative capacity behavior, phase vocabulary, timing, and shared-cut behavior remain; Findings 9, 17, and 25. |
| Human-linear journeys, UX states and budgets, terminal lifecycle | 5.1–5.7, 6.8, 7.9 | Release Agent and linear invocation/output contract is not frozen; Finding 29. |
| Action races, signals, handoffs, and no-detach behavior | 6.1–6.8 | Enum, identifier allocation, durable phases, detachment, and execution ownership conflict; Findings 15–19. |
| AD-21 read cut, atomic admission, baseline races, hot history, no post-admission lookup | 3.1, 3.8, 4.4, 4.7, 6.2–6.7 | Core read-cut language is present; ActionPlan identity timing remains wrong; Finding 16. |
| DispatchSchedule default, near-tie, latency, missed-epoch, LPT-position, and zero-margin fixtures | 1.4, 1.8, 3.1–3.2 | Schedule intent is present, but FD3 preallocation and exact no-allocation boundary are not fully carried into acceptance; Finding 13. |
| Byte-complete policy, identity, scope, diagnostic, candidate, and process properties | 1.3–1.4, 3.2–3.9 | Self-generated-golden risk plus provider and process identity divergence remain; Findings 7 and 11–12. |
| Fixed policy, collection-plan, observation-id, provider-assignment, and independent-codec goldens | 1.2–1.4, 3.1–3.9, 7.9 | Story gates do not prohibit expected bytes generated by the encoder under test; Finding 7. |
| Every FD3 peer, framing, descriptor, failure-precedence, timeout, cleanup, and reap row | 1.8, 3.2, 3.8–3.9, 6.5, 7.2 | Generic protocol language omits exact fields, ownership transitions, credentials, preallocation, and immutable-report/reap separation; Findings 13–14. |
| Fresh/existing SQLite, CAS, action handoffs, release transitions, sidecar recovery, and unavailable storage | 1.5–1.7, 6.4–6.8, 7.3, 7.6–7.8 | Exact initialization and release terminal state machine are not fully accepted; Findings 8 and 26–28. |
| Traditional POSIX record-lock fixtures and rejected flock/OFD controls | 7.2 | Lock family and owner/reopen/dup invariants are not frozen; Finding 21. |
| Stable toolchain evidence, stale-manifest failure, and exact-artifact ABI proof | 7.1, 7.9 | Generic locked-toolchain and ABI wording admits materially different proof; Finding 20. |
| Managed consumer rewrite/readback and exact brownfield two-pair authority | 7.4, 7.9 | Story permits extra rewrites, scripts, and bounded deviations; Finding 23. |
| D-Bus subscription handshake, timer causality, fresh invocation, and one shared ARCH-LIM-24 cut | 7.5, 7.9 | Handshake ordering and the single persisted cut are not acceptance-complete; Finding 25. |
| FirstInstall forward/recovery/rollback absence matrix | 7.6–7.9 | Generic recovery language does not freeze the exact sentinel, removal cuts, foreign-path refusal, and zero-mutation rollback; Finding 28. |
| Seven transition histories, replacement-owner chronology, and complete terminal mapping | 7.6–7.9 | Story aliases and invented durable type names admit incompatible histories; Findings 22 and 26. |
| KnownGood publication and explicit rollback directionality | 7.7–7.8 | Story adds incompatible pointer content and omits displaced-source publication; Finding 27. |
| FD4 request/result standalone bytes and candidate-bound evidence | 7.5, 7.9 | Story adds fields outside the closed FD4 schemas; Finding 24. |
| Action-executor handoff, systemd-job recovery, Host smoke, and future isolated service-manager CI | 6.4–6.8, 7.6, 7.9 | Handoffs are named, but row-to-gate ownership is not machine-verifiable; Finding 30. |

## ARCH-LIM and Host-contract coverage

| Contract set | Story ownership inspected | Review result |
| --- | --- | --- |
| ARCH-LIM-1 collection concurrency | 1.4, 3.1 | Inclusive range is referenced; FD3 admission mechanics still diverge in Finding 13. |
| ARCH-LIM-2 and ARCH-LIM-3 provider deadlines, scheduler margin, makespan, and cutoff | 1.4, 1.8, 3.1–3.2 | Formula intent is present; exact preallocation and missed-cut behavior remains incomplete in Finding 13. |
| ARCH-LIM-4, ARCH-LIM-16, and ARCH-LIM-17 child/scope/generation capture caps | 1.4, 1.8, 3.2, 3.9 | Referenced through compiled policy and bounded Host execution; no separate finding. |
| ARCH-LIM-5 inspection bytes and lines | 1.4, 3.9 | Earlier-bound disclosure is represented; no separate finding. |
| ARCH-LIM-6, ARCH-LIM-7, ARCH-LIM-18, and ARCH-LIM-19 retention counts, pins, and state-byte ceiling | 1.4, 1.7, 2.2 | Story adds noncanonical archive, delete, vacuum, and low-disk behavior and allows two capacity responses; Finding 9. |
| ARCH-LIM-8 Lease, Heartbeat, and grace | 1.4, 2.2–2.3 | Range coverage exists; invalid persistent intent remains ambiguous; Finding 10. |
| ARCH-LIM-9 and ARCH-LIM-10 stale and hot evidence | 1.4, 4.4 | Positive-evidence rules are acceptance-owned; no separate finding. |
| ARCH-LIM-11, ARCH-LIM-12, and ARCH-LIM-13 action execution, verification, polling, graceful termination, and forced observation | 1.4, 6.3, 6.5–6.7 | Noncanonical phases, detachment, and reap timing remain; Findings 14, 17, and 18. |
| ARCH-LIM-14 SQLite busy timeout | 1.4–1.5, 6.4 | Exact pragma/readback and unavailable-result behavior are not fully frozen; Finding 8. |
| ARCH-LIM-15 ActionPlan TTL | 1.4, 6.2–6.3 | TTL is referenced, but OperationId is allocated in the plan; Finding 16. |
| ARCH-LIM-20 action concurrency | 1.4, 6.4 | Saturation exists, but the persisted admission vocabulary differs; Finding 17. |
| ARCH-LIM-21 revalidation deadline | 1.4, 6.3–6.4 | Refusal intent is present; no separate finding. |
| ARCH-LIM-22 durable finalization attempt | 1.4, 6.6–6.8 | Detach and terminal-state language conflict with keep-alive and retry semantics; Findings 18 and 26. |
| ARCH-LIM-23 derived total decision bound | 1.4, 6.2, 6.6, 6.8 | Generic action phases and reap semantics permit different calculations; Findings 14 and 17. |
| ARCH-LIM-24 release validation timeout and sole persisted cut | 1.4, 7.5–7.9 | Stories do not freeze one shared cut across all four required evidence classes; Finding 25. |
| ARCH-HOST-1 live Host smoke boundary | 1.8, 7.9 | Named, but architecture-boundary CI ownership and exact future row coverage remain open; Findings 6 and 30. |

## Findings

1. **F-01 — The reviewed artifact occupies a path that the architecture requires to remain a non-story tombstone.** The architecture spine at lines 59–77 requires planning-root epics.md to remain a quarantine tombstone, forbids Epic and Story headings there, and requires regenerated canonical stories elsewhere after architecture finalization. The reviewed file contains seven Epic headings and 55 Story headings. A team following the stories can treat this file as implementation authority, while a team following the architecture must reject it before story execution. The checked-in aggregate gate confirms the conflict by failing with “planning-root tombstone does not fail closed”. There is no single compliant interpretation until the artifact is generated into the architecture-authorized location or the architecture contract is changed.

2. **F-02 — The artifact declares itself draft, nonassignable, and nonauthoritative while presenting executable story acceptance.** Frontmatter lines 1–20 say status draft, assignable false, implementationAuthority false, and record only two workflow steps as complete. The body then calls itself the implementation backlog and supplies assignment-ready stories. One implementation manager can refuse all work because the artifact disclaims authority; another can accept the body as authoritative. Both readings follow explicit text, so the artifact cannot be a deterministic implementation contract.

3. **F-03 — Story 1.2 creates an unfrozen compatibility lane.** Lines 455–467 permit a “semantic normalizer” while AD-9 and the compatibility closure define exactly two lanes: byte-exact output comparison and explicitly typed semantic exceptions. The story neither names the allowed exception types nor prohibits normalization outside them. One implementation can compare exact bytes; another can normalize ordering, whitespace, paths, Unicode, or aliases before comparison and still claim story compliance. That changes which regressions pass.

4. **F-04 — Story 1.3 conflates CanonicalJsonV1 bytes with presenter line termination.** Lines 494–496 require canonical machine JSON with exactly one trailing newline. AD-24 lines 2354–2374 define CanonicalJsonV1 with no trailing newline; the output presenter adds exactly one line terminator at the outer surface. One encoder can hash and frame newline-free bytes and let presentation terminate the line; another can include the newline in the canonical payload. Both satisfy the story wording but produce different fingerprints, IPC frames, manifests, and JSONL checksums.

5. **F-05 — Search matching is not frozen to the architecture’s exact Unicode algorithm.** Story 5.3 lines 1831–1849 asks for Unicode/raw-byte matching but does not require the AD-8 sequence of UTF-8 decode status, Unicode 16.0 NFC, full default case folding, NFC again, and raw-byte uppercase-percent fallback. Implementations may choose lowercase, simple case folding, NFKC, locale-sensitive matching, lossy UTF-8, or raw substring matching. Each can present reasonable “Unicode/raw-byte” behavior while returning different result sets and focus positions.

6. **F-06 — Story 1.1 does not freeze the architecture-boundary CI contract.** Lines 407–434 ask for a boundary test and aggregate gate but omit the architecture’s exact path, exact test name, dependency-direction assertions, release-CI ownership, and fail-closed quarantine behavior. A team can use lint rules, compile-only checks, or a differently scoped module test and satisfy the story. Another can implement the normative tests/architecture-boundaries.rs contract and aggregate commands. Those suites reject different dependency graphs and planning states.

7. **F-07 — The stories do not prohibit expected canonical goldens generated by the encoder under test.** AD-11 repeatedly requires fixed checked-in assertion inputs, two independent encoders, and explicitly forbids recapture or generation from the Rust encoder under test. Stories 1.2–1.4, 3.1–3.9, and 7.9 say to wire goldens or compare expected bytes but do not impose independent provenance. One implementation can snapshot its own output and pass; another must match externally fixed bytes. Both are story-compliant, but only one detects a coherently wrong codec.

8. **F-08 — SQLite initialization and migration behavior admits incompatible databases.** Story 1.5 lines 559–590 refers to required pragmas, migration, backup, restore, and integrity checks, but does not freeze the AD-16 sequence and readbacks for journal_mode WAL, synchronous FULL, foreign_keys ON, trusted_schema OFF, busy timeout, application_id, user_version, page-size constraints, fresh-versus-existing handling, or exact backup/replace/crash cuts. It also explicitly permits “repair or refusal” for mode mismatch. One implementation can mutate an existing database back into policy; another can fail closed. Both satisfy the story, but they differ in side effects, admissible files, and post-crash truth.

9. **F-09 — Retention and capacity stories add behavior and a choice the architecture does not permit.** Story 1.7 lines 636–664 introduces archive/delete, low-disk handling, and optional vacuum behavior, then allows either “degraded or refusal” when capacity is exhausted. AD-16 and ARCH-LIM-6, 7, 18, and 19 require deterministic pins and watermarks, physical st_blocks times 512 accounting, pruning eligible truth, and one disclosed capacity-exhausted mode without deleting pins. An implementation may archive and keep admitting writes in degraded mode; another may refuse immediately; another may vacuum. Their retained rows, disk writes, and availability differ while all meet the story.

10. **F-10 — Invalid persistent intent can either be rejected or retained as unmanaged.** Story 2.2 lines 778–806 permits “reject or retain unmanaged” invalid or expired persistent intent. AD-17 requires one typed lifecycle and prevents silent reinterpretation of durable truth. Rejection leaves no durable Promise; retention creates a durable row with later reconciliation and retention consequences. Those are observably different repository histories, snapshots, briefs, and lease-capacity outcomes, yet both are explicitly story-compliant.

11. **F-11 — Docker and PM2 ObservationId inputs include mutable evidence excluded by AD-18.** Story 3.5 lines 1141–1144 permits Docker creation/start anchors in identity, and Story 3.6 lines 1181–1184 includes the OS PID for PM2. The architecture’s exact identities use Docker endpoint/context plus immutable container ID bytes, and PM2_HOME, PM2 ID, created_at, normalized executable, and NFC name; start evidence and OS PID are observations, not identity. Two implementations can include or omit those mutable values and both satisfy the stories, causing the same logical object to acquire different ObservationIds across restarts.

12. **F-12 — Direct-process self-suppression removes descendants that AD-18 requires to remain observable.** Story 3.7 lines 1200–1203 and 1227–1230 excludes descendants of srvls. The architecture suppresses only the exact srvls PID and in-group Provider child/grandchild identities; escaped descendants are emitted with evidence. One implementation can suppress the entire descendant tree, while another emits escaped descendants. Both can claim they avoided self-reporting, but their Snapshot, orphan, unmanaged, and safe-to-stop results differ.

13. **F-13 — Story 3.2 leaves the FD3 protocol, descriptor lifecycle, credentials, and preallocation boundary open.** Lines 993–1010 describe a generic nonce/plan/provider/scope handshake. AD-25 fixes the socketpair type, FD number, exact Hello/Ready/Request/Result fields and CanonicalJsonV1 frames, SO_PEERCRED checks, prctl parent-death behavior, capability derivation, per-descriptor ownership table, EOF sequence, exit codes, failure precedence, and the no-capability/socket/child/root/reap allocation rule at expired cuts. A compliant story implementation can use different fields, credential timing, endpoint ownership, allocation timing, or EOF semantics than another. The resulting protocol is not interoperable and exercises different security boundaries.

14. **F-14 — FD3 and CommandRunner cleanup can rewrite or erase the immutable terminal report.** Story 3.2 lines 1025–1028 says workers are reaped before the terminal report, and the generic CommandRunner language similarly treats reap as part of bounded completion. AD-10 and AD-25 explicitly allow no timed reap guarantee for D-state work and require the coordinator report to become immutable before a separate pending-reaper lifecycle; later reap evidence cannot rewrite candidate bytes. One implementation may wait and fold exit status into the result; another may publish at the deadline and retain WorkerReapEvidenceV1 separately. Both satisfy the story family but generate different diagnostics, decision bounds, and process liveness.

15. **F-15 — The action stories add signal as a canonical action verb.** Story 6.1 line 2050, Story 6.2 line 2121, and Story 6.5 lines 2222–2225 treat signal as a separate selectable action. AD-6 fixes the canonical action enum and expresses direct-process signaling through the stop action with an exact predicate. One implementation can serialize action=signal and another action=stop with signal parameters. Both follow story language, but their ActionPlan bytes, fingerprints, policy decisions, CLI surface, and durable events are incompatible.

16. **F-16 — Story 6.2 allocates OperationId inside ActionPlan, before submit.** Lines 2092–2097 include OperationId in the frozen ActionPlan. AD-22 lines 1416–1429 require PlanId in the plan and allocate OperationId only at atomic submit. One implementation can reserve durable operation identity during planning; another can allocate it only after admission. They produce different retry, cancel, concurrency, idempotency, and abandoned-plan histories while satisfying different explicit authorities.

17. **F-17 — The durable action phase vocabulary is noncanonical and internally inconsistent.** Story 6.4 lines 2180–2184 uses planned, confirmed, and admitted; Story 6.6 lines 2266–2270 and 2297–2300 uses queued, admitted, running, verifying, and even a durable refused row. AD-16 and the AD-22 OperationCut fix planned, launch-authorized, executing, and verifying, with refusal before launch represented as the prescribed outcome rather than an invented queue state. Implementations can persist different phase graphs and still satisfy individual stories, making recovery, status, and transition validation incompatible.

18. **F-18 — Stories permit detachment even though submitted operations must never detach.** Story 6.8 lines 2386–2390 and Story 7.2 lines 2459–2460 offer cancel, detach, wait, or recover behavior for launched work. AD-6 lines 1066–1080 requires a submitted operation to remain process-owned until one terminal outcome is durable, including storage-unavailable finalization retries. One implementation can return while a mutation continues; another must keep the process alive. Both are story-compliant, but they differ in lock lifetime, signal semantics, terminal truth, and owner-loss recovery.

19. **F-19 — Story 6.5 and Story 7.4 allow mutating Host commands through child argv execution.** Story 6.5 lines 2221–2238 routes provider mutations through CommandRunner, and Story 7.4 lines 2548–2553 models daemon reload and timer control as typed argv. AD-23 requires release filesystem, database, release, daemon-reload, and timer-control mutations to occur in the process-associated lock owner, explicitly forbidding mutating fork/exec children for systemctl and timer control. One implementation can spawn systemctl while holding the lock; another must use the in-process manager interface. Their inherited-lock risk and recovery ownership differ.

20. **F-20 — Toolchain and ABI acceptance does not freeze the architecture’s evidence.** Story 7.1 lines 2416–2449 asks for a locked stable toolchain and ABI proof but does not require StableToolchainEvidenceV1, the official freshly fetched Rust 1.97.1 manifest/component/compiler identity, failure before compile when a stale cached 1.97.0 compiler is selected, or proof against the exact final artifact that is admitted. One implementation can rely on rust-toolchain metadata and generic ldd output; another can bind the fetched manifest and exact artifact hash. Both pass the story but establish different supply-chain and ABI claims.

21. **F-21 — The release-lock story does not freeze the exact POSIX primitive or lock-file invariants.** Story 7.2 lines 2457–2495 says process-associated POSIX lock and quiescence, but does not require traditional F_SETLK/F_SETLKW byte-range [0,1), F_GETLK owner proof, FD_CLOEXEC, or the prohibitions on flock, lockf, F_OFD_SETLK, owner reopen, dup, stdio access, and inode close. It also leaves enough ordering freedom to sample state before all shared leases are drained. Two implementations can use materially different lock primitives or cuts and both describe them as POSIX locks, but only one has the architecture’s owner-loss semantics.

22. **F-22 — Release stories invent four durable type names outside the closed AD-24 vocabulary.** The epics use ReleaseArtifactV1, ReleaseTransactionV1, KnownGoodV1, and FirstInstallV1. The architecture fixes ReleaseBinaryArtifactV1, UpgradeTransactionV1, KnownGoodReleaseV1, and FirstInstallAbsentV1. A team can implement the story names as distinct schemas or aliases; another can implement only the architecture names. Both can claim compliance, but serialized type tags, migration identifiers, validators, and public interfaces diverge.

23. **F-23 — Consumer migration permits edits beyond the exact executable substitution.** Story 7.4 lines 2548–2553 authorizes unit, script, configuration, state, and output rewrites; lines 2581–2584 accept a bounded deviation. AD-11 and AD-23 fix two sorted service/timer pairs and require replacing exactly the two canonical encoded deployed-executable occurrences while every other fragment byte, shell operator, timer property, enablement value, and scalar remains unchanged. One implementation can rewrite scripts or normalize units and record a deviation; another must reject any byte beyond the two substitutions. Their candidate hashes and rollback authorities differ.

24. **F-24 — Story 7.5 expands the closed FD4 request/result schemas.** Lines 2592–2626 carry transaction, consumer, phase, executable, build, argv, state, config, trigger, and output data over FD4. AD-23 and AD-24 define exact FD4 request/result fields bound to the pending envelope, recovery owner, validation attempt, directional authorities, evidence UUID, deadline, and prescribed result evidence; consumer, phase, argv, trigger, and output are not free extension keys. One implementation can serialize the story’s expanded payload; another must reject it as noncanonical. Their frames and checksums cannot interoperate.

25. **F-25 — Timer validation does not acceptance-own the full D-Bus subscription handshake or one shared ARCH-LIM-24 cut.** Story 7.5 names causality and a deadline, but does not freeze the owner-match, first owner lookup, Manager.Subscribe reply, unchanged-owner recheck, queue-drain barrier, baseline capture, trigger order, manager-change and sequence-gap failures, or the requirement that loaded-unit readback, timer causality, terminal service evidence, and matching FD4 validation share one persisted CLOCK_BOOTTIME attempt cut. Implementations can use separate local timeouts or subscribe after baseline and still meet the story. They accept different races and crash recoveries.

26. **F-26 — Release recovery introduces terminal aliases outside the architecture state machine.** Story 7.6 lines 2634–2639 and 2668–2671 uses committed, restored, and failed-needs-manual. The architecture fixes the complete release terminal-result vocabulary and corresponding public event/UX mapping, including forward-failed-recovered, rollback-unavailable, and the exact forward and rollback outcomes. One implementation can persist story aliases; another can persist canonical results. Both appear terminal but drive different recovery eligibility, status output, KnownGood publication, and transition-oracle bytes.

27. **F-27 — KnownGood publication can contain noncanonical pointer data and explicit rollback lacks the displaced-source rule.** Story 7.7 lines 2679–2706 describes a KnownGood manifest/pointer containing policy and evidence fingerprints. AD-23 fixes KnownGoodReleaseV1 and its publication point; extra pointer semantics can change canonical bytes and atomic replacement behavior. The architecture also requires successful explicit rollback to publish the displaced installed source as the future KnownGood target, which the story does not acceptance-own. One implementation can retain the old target or embed extra fields; another publishes the displaced source in the exact schema. Future rollback direction then differs.

28. **F-28 — FirstInstall recovery is described generically rather than by the exact absence contract.** Story 7.8 lines 2722–2759 does not freeze FirstInstallAbsentV1, reserved ready generation zero, every automatic absent-restore effect and crash cut, exact link/binary/state/sidecar/unit/enablement absence, nonempty prior-absence records, foreign-path or symlink replacement refusal without deletion, completed-absence readback, and byte-identical rollback-unavailable with zero mutation. Two implementations can delete a foreign replacement, preserve partial state, or create a rollback transaction and still satisfy generic “recover first install” language. Their safety and durable histories diverge.

29. **F-29 — The release CLI and Agent/linear interface is not canonical.** Story 7.9 lines 2772 and 2800 exposes status, recover, install, and rollback, omitting the architecture’s exact install, upgrade, validate, status, and rollback namespace while adding recover. Story 2.5 lines 897–927 also leaves Agent stdin-versus-argv invocation, record framing, exit mapping, and linear result interface unspecified. One implementation can expose recover and accept JSON on stdin; another can expose only the canonical verbs and typed argv. Both can satisfy the stories, but operators and automation cannot rely on one interface.

30. **F-30 — Blanket “all”, “full”, and “every named row” clauses do not create a verifiable AD-11 ownership map.** Stories 1.1, 6.8, and 7.9 claim all AD-11 rows are checked and missing rows fail, but the epics contain no machine-readable row registry mapping each matrix obligation to an owning story, fixture path, validator assertion, and aggregate command. The architecture distinguishes already checked-in evidence from mandatory future implementation deliverables. A team can declare a reduced set to be “all” and pass its gate; another can implement the complete matrix. Both satisfy the prose because omission itself is not detectable from the story artifact.

## Conclusion

The target digest is settled and exact, but the epics artifact is not architecture-closed. The 30 findings include direct contradictions, omitted closed-schema details, alternative durable state machines, alternative Host mutation models, and acceptance language that cannot detect missing matrix rows. The verdict can become PASS only when all findings are removed and a repeat review returns zero findings against the same or an explicitly re-settled epics digest.
