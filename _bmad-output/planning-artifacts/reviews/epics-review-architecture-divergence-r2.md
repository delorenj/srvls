---
type: architecture-divergence-review
status: complete
assignable: false
implementationAuthority: false
reviewBatch: independent-batch-2
reviewedCommit: 8ebdc20e2ea08f5bb7529dad1bc1b2d90c50a705
reviewedArtifact: _bmad-output/planning-artifacts/epics.md
reviewedSha256: b5368de55ada106282a2b623879feef5ceffea1a4dd0afd54870326aebb1ee27
architectureArtifact: _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md
architectureSha256: 28a103267a8e4ae5411c314bc2f9c0b62b694352e6e91c2522a2271df16ff575
override: source-review-F-01-tombstone-destination-only
verdict: FAIL
findingCount: 12
---

# Independent Batch 2 Epics Architecture-Divergence Review

## Verdict

**FAIL.** The reviewed `epics.md` blob is pinned correctly and the sole
user-authorized tombstone-destination override is quarantine-safe, but 12
architecture divergences remain. PASS requires zero findings.

This review treats the complete final architecture spine as binding except for
source-review finding F-01's tombstone destination. It does not treat prior
review or remediation prose as authority. It does not assess implementation
completion: the reviewed artifact is correctly marked draft, nonassignable, and
not implementation authority.

## Source Pin and Override-Aware Quarantine

| Check | Result |
| --- | --- |
| Commit | `8ebdc20e2ea08f5bb7529dad1bc1b2d90c50a705` exists and is HEAD. |
| Commit subject | `docs: remediate canonical epics backlog batch 1` |
| Reviewed blob | `_bmad-output/planning-artifacts/epics.md` |
| Requested SHA-256 | `b5368de55ada106282a2b623879feef5ceffea1a4dd0afd54870326aebb1ee27` |
| Computed SHA-256 | Exact match. The worktree copy is byte-identical to the commit blob. |
| Override scope | Only the planning-root tombstone destination is overridden. No runtime, release, discovery, authority, or archive rule is waived. |
| Canonical discovery | PASS: the two exact discovery globs resolve uniquely to canonical `epics.md`; fuzzy aliases remain excluded. |
| Authority | PASS: `status: remediated-draft`, `assignable: false`, and `implementationAuthority: false`. |
| Retired archive | PASS: the only retired epic artifact remains outside discovery and preserves SHA-256 `9a256682785733c23fbf017c138115b067ec894fe8b697da75da134905d7effd`. |
| Legacy quarantine validator | Expected override-only failure: `planning-root tombstone does not fail closed`. |
| Override-aware probe | PASS: after replacing only that obsolete tombstone assertion, every other quarantine invariant passes. |

The authorized override therefore does **not** produce a finding. The legacy
validator should still be interpreted narrowly: any failure other than the
exact tombstone assertion remains blocking.

## Findings

1. **D-01 — The AD-11 registry omits the current legacy Host-smoke lane.**
   AD-11 defines the current executable inventory as compatibility, canonical
   contract families, the release subcorpus, **and** the legacy Host smoke suite
   (`ARCHITECTURE-SPINE.md:518-525`). The registry ends its current rows at
   AD11-CUR-13 for release oracles (`epics.md:2029-2092`) and has no current row
   for `tests/test_smoke.sh`. AD11-FUT-54 is a future exact-Rust-artifact Host
   smoke and cannot stand in for the explicitly current Python smoke lane. The
   aggregate happens to invoke the smoke script, but the normative registry can
   omit it while still satisfying its own count and reciprocal-owner checks.

2. **D-02 — AD-11 cannot detect missing Heartbeat, closure, or Agent-interface
   acceptance.** AD-11 requires Promise lifecycle/idempotency and human-linear
   journeys (`ARCHITECTURE-SPINE.md:533-543`). The future registry covers
   principal authorization, declare/revise, and Lease at AD11-FUT-07 through
   AD11-FUT-09, then jumps to collection scheduling (`epics.md:2141-2164`). It
   contains no row for the owning oracles named by Story 2.4 Heartbeats, Story
   2.5 closure, or Story 2.6 typed Agent argv/records/exits
   (`epics.md:2896-2976`). The aggregate can therefore pass while those Agent
   contracts are absent.

3. **D-03 — AD-11's complete reconciliation and Safe-to-stop matrix is not
   represented.** The architecture requires every reconciliation axis and
   classification, Safe-to-stop rules, and grouping property cases
   (`ARCHITECTURE-SPINE.md:536-543`). Registry rows AD11-FUT-25 through
   AD11-FUT-30 cover correlation, duplicate sets, stale/hot history, Snapshot,
   baseline, and Brief, but omit the validation oracles for Story 4.2
   orthogonal outcomes, Story 4.5 unmanaged/abandoned, Story 4.6 Safe-to-stop,
   and Story 4.10 Stack/Ungrouped grouping (`epics.md:3308-3547`). Those are
   distinct architecture-required result spaces, not aliases of correlation or
   Brief rendering.

4. **D-04 — Current fixed identity/plan goldens are used where AD-11 requires
   future implementation property suites.** AD-11 explicitly distinguishes
   current assertion inputs from future implementation acceptance and requires
   property suites for byte-complete policy JSON, ScopeId/ScopeManifest,
   non-UTF-8 paths, arbitrary diagnostic subjects/parameters, mixed candidate
   references, and process ownership ties (`ARCHITECTURE-SPINE.md:527-531,
   590-598`). AD11-CUR-07 through CUR-10 point only to the checked-in fixed
   corpus, while no AD11-FUT row owns that property-suite surface. Story 1.4's
   oracle is the current Python contract validator, not the required Rust
   implementation property suite (`epics.md:2623-2649`). A conforming fixed
   vector can therefore mask a divergent general encoder or identity reducer.

5. **D-05 — AD-11 has no row for immediate action revalidation or action
   linear/machine parity.** The registry covers enum, confirmation, pool,
   admission, executor, outcome, shutdown, and an aggregate at AD11-FUT-36
   through FUT-43. It omits Story 6.4's immediate identity/capability/safety
   race oracle and Story 6.11's typed linear/machine parity oracle
   (`epics.md:3878-3903,4066-4092`). Story 6.12's aggregate boundary enumerates
   plan, pool, admission, executor, status, outcome, shutdown, and parity but
   does not name immediate revalidation (`epics.md:4093-4119`). Thus the
   machine registry does not make omission of two AD-11-required action races
   and human-linear contracts detectable.

6. **D-06 — AD-15 is falsely assigned to Agent principal binding instead of
   Provider privilege and environment ownership.** AD-15 binds cron, systemd,
   Docker, PM2, direct process, and lifecycle actions and fixes `sudo -n`,
   legacy interactive-sudo isolation, absolute allowlisted executables, `/` as
   cwd, minimal Provider environments, and distinct denial/error mapping
   (`ARCHITECTURE-SPINE.md:1082-1101`). The coverage registry maps all of AD-15
   only to Story 2.1 (`epics.md:1808-1810`), whose boundary and acceptance cover
   local Promise actor/owner credentials only (`epics.md:2816-2841`). Story
   6.7 rejects `broad privilege`, but no story acceptance-owns the complete
   collection/action environment, cwd, executable, sudo-lane, diagnostic, and
   logging contract. Two Provider adapters can therefore satisfy the backlog
   while using incompatible privilege and inherited-environment policies.

7. **D-07 — Story 6.4 contradicts the canonical `unknown` Safe-to-stop path.**
   Contract C-05 and AD-6 allow `Safe-to-stop: unknown` after cancel-first
   confirmation and the exact resolved verb (`epics.md:91-108`;
   `ARCHITECTURE-SPINE.md:223-228`). Story 6.4 instead says that after fresh
   revalidation **only an unchanged `safe` result authorizes submit**
   (`epics.md:3895-3898`). A target that remains canonically `unknown` after
   the operator supplied the required acknowledgement is therefore rejected by
   Story 6.4 but permitted by the architecture and Story 6.3. The stories admit
   incompatible action availability and outcome behavior.

8. **D-08 — The toolchain story turns the moving `stable` lane into a point
   pin and omits the dual-lane bootstrap contract.** AD-12 requires both
   bootstrap and release CI to run a pinned MSRV 1.88 lane plus a symbolic,
   moving `stable` lane that is never permanently point-pinned, with fresh
   manifest/compiler identity before any compile and locked gates at MSRV and
   stable (`ARCHITECTURE-SPINE.md:835-859`). Contract C-11 and Story 7.1 instead
   prescribe `stable 1.97.1` as the implementation input and never acceptance-
   own the MSRV lane, resolver 3, both CI entry points, or the moving-channel
   rule (`epics.md:262-265,4124-4149`). The ABI/readelf/same-artifact smoke
   portion is correct, but an implementation can permanently install 1.97.1
   and satisfy the story after official stable has moved, which AD-12 forbids.

9. **D-09 — The epics invent `ManagedConsumerManifestV1`, an architecture-
   foreign release authority.** Contract C-11 declares the type architecture-
   native and says aliases are forbidden; Stories 7.4 and 7.5 build transaction
   authority from it (`epics.md:240-245,4205-4239`). The complete architecture
   defines `ManagedConsumerUnitContractV1`, the transaction payload's ordered
   `consumers`, `BrownfieldConsumerPairsV1`, and their hashes, but defines no
   `ManagedConsumerManifestV1` (`ARCHITECTURE-SPINE.md:869-879,1743-1764,
   2028-2077`). This creates a second possible schema, checksum boundary, and
   preimage owner inside an otherwise closed AD-23 registry.

10. **D-10 — AD11-FUT-46 assigns consumer rewrite acceptance to a story that
    excludes replacement, and the rewrite cardinality is not pair-qualified.**
    AD11-FUT-46 names `assert_two_pair_consumer_rewrite` but owns it with Story
    7.4, whose Out of Scope explicitly excludes consumer replacement
    (`epics.md:2453-2460,4205-4229`). Story 7.6 performs the migration but has
    no AD-11 row and states only two manifest-authorized spans globally
    (`epics.md:4259-4284`). The architecture requires each candidate unit
    contract to derive the source service fragment and loaded ExecStart
    occurrence, with both sorted pairs independently bound
    (`ARCHITECTURE-SPINE.md:787-807`). The registry can accept discovery bytes
    without executing the in-owner two-pair rewrite it claims to own.

11. **D-11 — Story 7.8 reaches `committed` while putting the required commit
    effects out of scope.** Story 7.8 says its forward sequence advances to
    `committed`, yet its boundary stops at durable decision and its Out of Scope
    excludes KnownGood publication (`epics.md:4313-4334`). AD-23 makes
    `publish-known-good`, `persist-ready-admission`, and `commit-transaction`
    ordered effects after `commit-decided`; terminal `committed` is legal only
    after those effects (`ARCHITECTURE-SPINE.md:1878-1889,1915-1919,
    2224-2241`). Story 7.10 owns publication later. The dependency chain
    therefore asks Story 7.8 to assert a terminal state whose authority is not
    implemented until a later story.

12. **D-12 — The required full two-pair effect/crash convergence gate is
    absent.** The architecture warns that the seven transition histories use a
    single synthetic `metrics` pair and are not deployed-command evidence, then
    requires a future implementation gate to execute **both** metrics and
    snapshot pairs together through every forward effect, rollback effect, and
    crash boundary (`ARCHITECTURE-SPINE.md:787-818`). Story 7.15 wires the seven
    single-pair histories and generic future service-manager rows but never
    requires both pairs through every cut (`epics.md:4502-4527`). AD11-FUT-46
    covers only consumer rewrite and AD11-FUT-55 only isolated service-manager
    rows. FirstInstall's current positive two-pair mutation does not prove
    upgrade, installed-prior recovery, owner takeover, KnownGood continuation,
    or explicit rollback convergence. A single-pair recovery engine can pass
    the backlog while the real two-unit installation splits.

## AD-1 Through AD-25 Trace

This table judges architecture-contract coverage. A conforming row may still
depend on a missing AD-11 implementation gate identified above.

| Decision | Result | Backlog landing and review note |
| --- | --- | --- |
| AD-1 | Conforms | Story 1.1 owns the prescribed private dependency graph, exact boundary test, aggregate command, and release-CI ownership. |
| AD-2 | Conforms | Distinct repository aggregates and orthogonal reconciliation axes land across Stories 1.7 and 4.2; legacy EntryV1 remains in the separate compatibility lane. |
| AD-3 | Conforms | Story 1.1 rejects alternate side-effect owners; Stories 1.9, 6.7, and Epic 7 retain the read-only runner and in-process mutation boundaries. |
| AD-4 | Conforms with D-03 verification gap | Story 4.10 owns evidence-only Stack/Ungrouped grouping; its required AD-11 property row is missing. |
| AD-5 | Conforms | Contract C-03 plus Stories 3.9, 3.10, 4.7, and 4.8 preserve scoped reports, candidate/current separation, completeness, and baseline authority. |
| AD-6 | Diverges | Canonical kinds, plans, confirmations, executors, and outcome precedence are present, but Story 6.4 contradicts the permitted `unknown` path (D-07). |
| AD-7 | Conforms | Stories 5.1, 2.6, and 7.3 preserve pre-side-effect routing, reserved profiles, namespaces, bare routing, Agent output, and exact release verbs. |
| AD-8 | Conforms | Contract C-02 and Stories 5.3/5.7 own exact Unicode search, raw-byte fallback, text-primary state, hostile-text safety, ASCII, and no-motion behavior. |
| AD-9 | Conforms | Contract C-01 and Stories 1.2/1.3 preserve byte-exact inherited and typed approved-deviation lanes with independent goldens. |
| AD-10 | Conforms | Contract C-08 and Stories 3.2/3.3 own frozen reservations, exact schedule vectors, cuts, separate action pool, FD3 workers, and immutable terminal evidence. |
| AD-11 | Diverges | The 68-row registry is structurally valid but omits or misowns mandatory lanes (D-01 through D-05, D-10, D-12). |
| AD-12 | Diverges | Exact artifact ABI/smoke evidence is present, but the moving stable plus MSRV dual-lane contract is not (D-08). |
| AD-13 | Conforms with D-04 verification gap | Contract C-02 and Stories 1.4, 3.6, 3.7, and 3.8 preserve typed Observation identities, generations, diagnostics, roots, and exact suppression; the general property gate is missing. |
| AD-14 | Conforms | Stories 5.1 and 6.10 retain one RAII terminal owner, phase-specific cancellation, no detach, and durable finalization retry. |
| AD-15 | Diverges | Provider privilege, executable, cwd, environment, diagnostic, and logging rules lack a complete owner (D-06). |
| AD-16 | Conforms | Contract C-07 and Stories 1.6-1.8/4.7 preserve SQLite path/modes/PRAGMAs, transactions, CAS, retention, capacity mode, and read-only recovery. |
| AD-17 | Conforms with D-02 verification gap | Stories 2.2-2.5 preserve typed events, idempotency, CLOCK_BOOTTIME/boot rules, finite Lease, Durable Ownership, Heartbeat, and no-mutation closure; registry rows are incomplete. |
| AD-18 | Conforms with D-03 verification gap | Epic 4 decomposes correlation, axes, classifications, safety, Snapshot, baseline, Brief, and grouping without changing the pure decision authority. |
| AD-19 | Conforms | Story 1.5 and Story 5.8 own exact source precedence, provenance, invalid-lower-source failure, explain/validate surfaces, and no hot reload. |
| AD-20 | Conforms | Contract C-08 exactly reproduces ARCH-LIM-1 through ARCH-LIM-24, their ranges/formulas, and all three schedule vectors. |
| AD-21 | Conforms | Stories 3.1-3.11 preserve one admitted frozen cut, plan/schedule fingerprints, bounded per-scope worker inputs, candidate reduction, and sole current CAS. |
| AD-22 | Diverges | Plan/Operation IDs, phases, pools, in-process effects, fresh verification, terminal ownership, and parity are represented, but D-05 and D-07 leave incompatible acceptance. |
| AD-23 | Diverges | Locks, FD4, release state, FirstInstall, rollback, and KnownGood are broadly represented, but D-09 through D-12 alter schema, ownership, ordering, and two-pair convergence. |
| AD-24 | Conforms with D-04 verification gap | Contract C-02 and Story 1.4 preserve CanonicalJsonV1, typed paths/IDs, policy/plan/snapshot fingerprints, and fixed bytes; future property acceptance is missing. |
| AD-25 | Conforms | Contract C-09 and Story 3.3 own same-binary FD3, exact descriptor table, peer proof, four frames, caps, cuts, report schemas, EOF, cleanup, and total failure precedence. |

## Every AD-11 Registry Row

`Conforms` means the row's declared backlog contract is architecture-consistent;
it does not claim that a future Rust fixture already exists. `Gap` means the row
is valid for its stated slice but cannot cover a separate omitted obligation.

| Row | Owner | Review | Note |
| --- | --- | --- | --- |
| AD11-CUR-01 | Story 1.3 | Conforms | Frozen legacy CLI matrix. |
| AD11-CUR-02 | Story 1.3 | Conforms | Frozen legacy output bytes. |
| AD11-CUR-03 | Story 1.3 | Conforms | Frozen Provider matrix. |
| AD11-CUR-04 | Story 1.3 | Conforms | Frozen inspection matrix. |
| AD11-CUR-05 | Story 1.3 | Conforms | Frozen action argv matrix. |
| AD11-CUR-06 | Story 1.4 | Conforms | Contract-manifest integrity; does not replace D-04's future property suite. |
| AD11-CUR-07 | Story 1.4 | Conforms | Fixed policy bytes; does not replace D-04. |
| AD11-CUR-08 | Story 3.1 | Conforms | Fixed plan/scope bytes; does not prove the future admission implementation. |
| AD11-CUR-09 | Story 1.4 | Conforms | Fixed Observation identity bytes; does not replace D-04. |
| AD11-CUR-10 | Story 3.1 | Conforms | Fixed Provider assignment bytes. |
| AD11-CUR-11 | Story 3.3 | Conforms | Fixed complete FD3 exchange bytes. |
| AD11-CUR-12 | Story 3.3 | Conforms | Fixed preallocation-timeout cut. |
| AD11-CUR-13 | Story 7.15 | Conforms | Current release oracle subcorpus. D-01 is the missing current smoke row. |
| AD11-FUT-01 | Story 1.1 | Conforms | Dependency direction and side-effect ownership. |
| AD11-FUT-02 | Story 1.5 | Conforms | Typed configuration and all limits. |
| AD11-FUT-03 | Story 1.6 | Conforms | Fresh/existing SQLite initialization. |
| AD11-FUT-04 | Story 1.7 | Conforms | Repository CAS and typed unavailability. |
| AD11-FUT-05 | Story 1.8 | Conforms | Retention pins, watermarks, and capacity. |
| AD11-FUT-06 | Story 1.9 | Conforms | CommandRunner terminal-before-reap. |
| AD11-FUT-07 | Story 2.1 | Conforms for its slice | Principal/owner authentication; D-06 remains. |
| AD11-FUT-08 | Story 2.2 | Gap | Declare/revise idempotency only; Heartbeat/close/Agent rows are missing (D-02). |
| AD11-FUT-09 | Story 2.3 | Conforms | Boot/clock and invalid persistent intent. |
| AD11-FUT-10 | Story 3.2 | Conforms | Default schedule. |
| AD11-FUT-11 | Story 3.2 | Conforms | Near-tie reservation schedule. |
| AD11-FUT-12 | Story 3.2 | Conforms | Sixty-second zero-margin schedule. |
| AD11-FUT-13 | Story 3.2 | Conforms | No allocation at/past either cut. |
| AD11-FUT-14 | Story 3.3 | Conforms | FD3 peer credentials and Ready. |
| AD11-FUT-15 | Story 3.3 | Conforms | FD3 ownership table, clean EOF, and duplicates. |
| AD11-FUT-16 | Story 3.3 | Conforms | Total transport-failure precedence. |
| AD11-FUT-17 | Story 3.3 | Conforms | Immutable report before cleanup/reap. |
| AD11-FUT-18 | Story 3.4 | Conforms | Cron matrix. |
| AD11-FUT-19 | Story 3.5 | Conforms | Systemd matrix. |
| AD11-FUT-20 | Story 3.6 | Conforms | Docker immutable identity. |
| AD11-FUT-21 | Story 3.7 | Conforms | PM2 birth identity. |
| AD11-FUT-22 | Story 3.8 | Conforms | Direct-process identity and suppression. |
| AD11-FUT-23 | Story 3.9 | Conforms | Candidate is not Snapshot/current. |
| AD11-FUT-24 | Story 3.10 | Conforms | Complete obligation/strict matrix. |
| AD11-FUT-25 | Story 4.1 | Conforms for its slice | Correlation vectors only; D-03 remains. |
| AD11-FUT-26 | Story 4.3 | Conforms | Duplicate-set cardinality. |
| AD11-FUT-27 | Story 4.4 | Conforms | Stale/hot history races. |
| AD11-FUT-28 | Story 4.7 | Conforms | Snapshot/current CAS. |
| AD11-FUT-29 | Story 4.8 | Conforms | Baseline races and audited override. |
| AD11-FUT-30 | Story 4.9 | Conforms | Eight Brief questions. |
| AD11-FUT-31 | Story 5.1 | Conforms | Routing and terminal restoration. |
| AD11-FUT-32 | Story 5.3 | Conforms | Unicode/raw-byte search and focus. |
| AD11-FUT-33 | Story 5.5 | Conforms | Plane/Git/Telemetry display-only boundary. |
| AD11-FUT-34 | Story 5.7 | Conforms | Accessibility and hostile-text states. |
| AD11-FUT-35 | Story 5.9 | Conforms | Host budget and state goldens. |
| AD11-FUT-36 | Story 6.1 | Conforms | Closed ActionKind/provider matrix. |
| AD11-FUT-37 | Story 6.3 | Conforms | Confirmation matrix. |
| AD11-FUT-38 | Story 6.5 | Conforms | Action pool before admission. |
| AD11-FUT-39 | Story 6.6 | Conforms | Operation IDs and phases. |
| AD11-FUT-40 | Story 6.7 | Conforms for its slice | In-process mutation owner; complete AD-15 remains D-06. |
| AD11-FUT-41 | Story 6.9 | Conforms | Action outcome precedence. |
| AD11-FUT-42 | Story 6.10 | Conforms | No detach and durable finalization. |
| AD11-FUT-43 | Story 6.12 | Gap | Aggregate cannot discover omitted revalidation/parity rows (D-05). |
| AD11-FUT-44 | Story 7.1 | Diverges | Point-pinned stable contract conflicts with AD-12 (D-08). |
| AD11-FUT-45 | Story 7.2 | Conforms | Traditional POSIX lock and handoff proof. |
| AD11-FUT-46 | Story 7.4 | Diverges | Rewrite assertion is owned by a preimage story that excludes replacement (D-09/D-10/D-12). |
| AD11-FUT-47 | Story 7.7 | Conforms | Exact FD4 bytes. |
| AD11-FUT-48 | Story 7.7 | Conforms | D-Bus handshake and shared cut. |
| AD11-FUT-49 | Story 7.9 | Conforms | Recovery-owner chronology. |
| AD11-FUT-50 | Story 7.10 | Conforms | Commit-bound KnownGood publication. |
| AD11-FUT-51 | Story 7.12 | Conforms | FirstInstall absence/recovery matrix. |
| AD11-FUT-52 | Story 7.14 | Conforms | Explicit rollback and displaced-source publication. |
| AD11-FUT-53 | Story 7.15 | Conforms | Canonical release commands/results. |
| AD11-FUT-54 | Story 7.15 | Conforms for future Rust artifact | It does not replace D-01's current legacy Host-smoke row. |
| AD11-FUT-55 | Story 7.15 | Gap | Isolated service-manager rows do not require both pairs through every effect/crash cut (D-12). |

All 68 declared rows have unique IDs, owners, fixtures, assertion names,
aggregate commands, and current/future status. The failure is semantic
completeness and ownership, not JSON shape or row duplication.

## Named Architecture Concerns

| Concern | Result | Evidence |
| --- | --- | --- |
| ARCH-LIM-1 through ARCH-LIM-24 | Conforms | Contract C-08 reproduces every default, inclusive range, formula, half-open/equality rule, and default/near-tie/60-second vector. |
| SQLite | Conforms | Contract C-07 and Stories 1.6-1.8 preserve path/modes, WAL/FULL/FK readbacks, exact busy timeout, BEGIN IMMEDIATE, migration/read-only recovery, CAS, pins, physical accounting, and capacity mode. |
| FD3 | Conforms | Contract C-09 and Story 3.3 preserve socket type, FD3 mapping, descriptor ownership table, credentials, four frames/key order, caps, deadlines, EOF, cleanup, synthesized report, and precedence. |
| FD4 | Conforms | Contract C-12 and Story 7.7 preserve exact request/result keys, peer/recovery owner, one-use capability, one result plus EOF, 1 MiB caps, directional authorities, and the one persisted ARCH-LIM-24 cut. |
| Typed identities | Conforms with D-04 gate gap | Canonical JSON, ScopeId/manifest, Observation IDs, diagnostic IDs/parameters, roots, process ownership, plans, operations, and release identities are represented; the general future property suite is absent. |
| Direct processes | Conforms | Story 3.8 retains PID/birth/executable identity, exact roots/group membership, ownership hints/conflict, escaped descendants, and no weak suppression; Story 6.7 keeps signal as `stop` parameters. |
| Canonical actions | Diverges | Closed enum/matrix, plans, phases, in-process mutation, and outcome precedence exist, but action revalidation both contradicts `unknown` and lacks a registry row (D-05/D-07). |
| Agent interfaces | Diverges in acceptance gating | Typed argv, no stdin grammar, deterministic linear/JSON stdout, human stderr, and fixed exits are stated in Story 2.6, but no AD-11 row makes that interface or Heartbeat/close lifecycle acceptance mandatory (D-02). |
| Toolchain and ABI | Diverges | Exact-artifact readelf/glibc-2.42/smoke is correct; symbolic moving stable, MSRV 1.88 dual lanes, and both precompile evidence gates are not (D-08). |
| Consumer migration | Diverges | Byte-preserving two-pair intent exists, but the type, row owner, occurrence scope, and full convergence gate differ from AD-23 (D-09/D-10/D-12). |
| FirstInstall | Conforms for single-pair semantics | Stories 7.11-7.13 preserve absence authority, generation zero, foreign-replacement refusal, crash recovery, readback, and zero-mutation rollback-unavailable. Full two-pair execution remains D-12. |
| Upgrade and owner takeover | Diverges | Locks, attempt ownership, idempotent replay, FD4/D-Bus validation, and terminal vocabulary are present, but Story 7.8 claims commit before later commit effects (D-11) and the multi-pair gate is missing (D-12). |
| KnownGood | Conforms in isolation | Story 7.10 preserves decision-before-publication, exact payload/checksum/readback, and ready admission; Story 7.14 preserves displaced-source direction. Story 7.8's earlier terminal claim still violates ordering. |
| Explicit rollback | Conforms for single-pair semantics | New reverse transaction, confirmation, fresh directional validation, displaced-source KnownGood, exact results, and sentinel no-mutation behavior are represented. Full two-pair recovery remains D-12. |
| Multi-pair recovery and two-unit convergence | Diverges | Current oracles prove two-pair authority and one positive FirstInstall mutation, but no future row/story executes both pairs through every forward/rollback effect and crash cut (D-12). |

## Executable Validation Evidence

| Command or probe | Result |
| --- | --- |
| `git show 8ebdc20:_bmad-output/planning-artifacts/epics.md \| sha256sum` | PASS; exact requested digest. |
| `git diff --exit-code 8ebdc20 -- _bmad-output/planning-artifacts/epics.md` | PASS; worktree artifact equals pinned commit. |
| `bash tests/compat/validate.sh` | PASS; 90 inherited plus 4 approved deviations. |
| `python3 tests/fixtures/contracts/validate.py` | PASS. |
| `python3 tests/fixtures/contracts/release-transaction-v1/validate_oracles.py` | PASS; 7 complete chains, release/FD4/brownfield/toolchain mutations, live lock/handoff proofs, and positive two-pair FirstInstall proof. |
| `bash tests/test_smoke.sh` | PASS; JSON, Prometheus, Markdown, table, inspection, and hostile-name lanes. |
| `bash tests/validate_architecture_contracts.sh` | Expected override-only nonzero exit after compatibility: `planning-root tombstone does not fail closed`. |
| Independent override-aware quarantine probe | PASS; only destination/tombstone assertion replaced. |
| Independent registry parser | PASS structurally; 7 epics, 73 stories, AD-1..25, ARCH-LIM-1..24, 68 unique rows, and reciprocal coverage. |
| Story-oracle-to-AD11 comparison | FAIL semantically; 28 story oracle paths are absent from the registry, including the architecture-mandated classes in D-02 through D-05. |
| Canonical Markdown profile | PASS; zero errors for `epics.md` and the Batch 1 ledger. |

Passing current fixed-oracle validators proves that the architecture corpus is
healthy. It does not close future story-contract contradictions or omissions;
AD-11 explicitly forbids treating current fixed inputs as nonexistent Rust
implementation evidence.

## PASS Gate

PASS requires a new pinned epics digest in which all D-01 through D-12 findings
are closed, the override remains limited to the F-01 destination, the registry
can detect every architecture-mandated current and future row, and a repeat
independent review returns zero findings. No implementation should be assigned
from this draft before that gate.
