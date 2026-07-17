---
type: remediation-ledger
status: remediated-draft
assignable: false
implementationAuthority: false
sourceArtifact: _bmad-output/planning-artifacts/epics.md
reviews:
  - _bmad-output/planning-artifacts/reviews/epics-review-product-traceability.md
  - _bmad-output/planning-artifacts/reviews/epics-review-story-quality-dependencies.md
  - _bmad-output/planning-artifacts/reviews/epics-review-architecture-divergence.md
---

# Epics Remediation Batch 1 Ledger

## Scope and Authority

This ledger records the batch-1 disposition of every finding in the three
review reports. The remediated epics artifact remains a draft, nonassignable,
and not implementation authority.

Architecture F-01 is the sole source-contract override. The user mission
requires the canonical planning-root epics.md to replace the tombstone at the
workflow discovery path. The override preserves the retired archive and digest,
does not weaken runtime architecture, and intentionally changes the quarantine
validator's tombstone expectation. Until that validator is changed by its
owner, its expected failure is exactly "planning-root tombstone does not fail closed"; any other quarantine failure remains blocking.

## Product and Traceability Review

| Finding | Disposition | Remediation evidence |
| --- | --- | --- |
| F-REQ-1 | Remediated | FR-1 human and machine results are concrete in Stories 2.2 and 2.6; FR-14's complete obligation/default/promotion contract is Story 3.10; FR-16's checked-in behavior inventory, additive fields, two lanes, and live consumer proof are Stories 1.2-1.3; FR-26 recalculation after refresh and immediately before mutation is Stories 4.6 and 6.4; FR-27's Snapshot/baseline/Evidence Window consequences are Stories 4.7-4.8; FR-32's full inspection and opaque-reference boundary is Stories 5.4-5.5. |
| F-UX-1 | Remediated | Story 4.8 acceptance owns b entry, Cancel-first focus, Esc cancellation, exact typed override, baseline-pointer-only mutation, and immediate Evidence Window recomputation. |
| F-UX-2 | Remediated | UX-ST action outcomes map only to Story 6.9, pending-action only to Story 6.8, stale identity only to Story 6.4, baseline states only to Story 4.8, collection states only to Stories 3.10/5.6, and invalid configuration only to Story 5.8. The JSON registry makes every corrected edge machine-checkable. |
| F-UX-3 | Remediated | Contract C-13 and Story 5.5 affirm Plane owns intended work, Git owns code changes, Telemetry owns events/measurements, and all three references are display-only and prohibited from runtime truth or mutation. |
| F-QUAL-1 | Remediated | Exactly seven epics are framed as independently valuable operator/Agent outcomes. Epic 1 lets an operator prove trust before Host truth is touched rather than presenting a technical horizontal milestone. |
| F-QUAL-2 | Remediated | Former oversized Story 1.2 is Stories 1.2-1.3; former 1.8 is Stories 1.9-1.10; collection planning/scheduling/FD3 are Stories 3.1-3.3; former 5.7 is Stories 5.7-5.9; former 6.8 is Stories 6.8-6.12; former 7.9 is split across Stories 7.3 and 7.15. |
| F-QUAL-3 | Remediated | Dependencies contain only the exact immediately preceding Story ID. Later aggregates are not preseeded: CollectionCandidateV1 is owned by Story 3.9, SnapshotV1/current CAS by Story 4.7, ActionPlan/Operation by Stories 6.3/6.6, and release authorities by Stories 7.4-7.14. |

The UX count is intentionally explicit: the final UX spine contains 83 core
UX IDs excluding accessibility, plus UX-A11Y-1 through UX-A11Y-5, plus
SR-A11Y-1. The registry preserves all 89 identifiers, not merely the 84-ID
subtotal stated in the mission.

## Story Quality and Dependency Review

| Finding | Disposition | Remediation evidence |
| --- | --- | --- |
| F-01 | Remediated | Bounded read-only CommandRunner is Story 1.9; aggregate foundation gate is Story 1.10. |
| F-02 | Remediated | Story 2.3 deterministically rejects invalid persistent intent and creates no durable Promise. |
| F-03 | Remediated | Story 2.1 defines local principal proof, owner binding, impersonation refusal, credential rotation, and authorization before lifecycle writes. |
| F-04 | Remediated | Every Dependencies field is either None for Story 1.1 or one exact earlier Story ID; no range, Epic reference, capability prose, or future ID appears. |
| F-05 | Remediated | Story 3.9 owns immutable non-current CollectionCandidateV1; Story 4.7 alone owns SnapshotV1 persistence and current CAS. |
| F-06 | Remediated | Story 4.3 emits one duplicate set plus excess cardinality and forbids member-level loser designation or action recommendation. |
| F-07 | Remediated | Contract C-14 and Story 4.9 enumerate and fixture BQ-1 through BQ-8 verbatim. |
| F-08 | Remediated | Story 4.10 contains only deterministic grouping implementation; external Product Owner approval and research gates are explicitly out of scope. |
| F-09 | Remediated | Accessibility/hostile text is Story 5.7, help/config recovery Story 5.8, and state goldens/performance/aggregate UX gate Story 5.9. |
| F-10 | Remediated | Contract C-04 and Story 6.1 own the closed lowercase ActionKindV1 enum and complete Provider matrix consumed by all surfaces and storage. |
| F-11 | Remediated | Contract C-05 and Story 6.3 classify Start, Restart, Stop, Disable, Delete, safe/unsafe/unknown/stale/pending states and exact tokens. |
| F-12 | Remediated | Story 6.5 implements the bounded separate pool before Story 6.6 atomic admission; no later story reowns the primitive. |
| F-13 | Remediated | Contract C-06 and Story 6.9 provide the complete ordered five-outcome decision matrix. |
| F-14 | Remediated | Operation status, verification, signal/recovery, parity, and aggregate closure are separate Stories 6.8-6.12. |
| F-15 | Remediated | Story 7.4 freezes ManagedConsumerManifestV1 before Story 7.5 captures UpgradeTransactionV1 preimages. |
| F-16 | Remediated | Generic owner takeover is Story 7.9 and is prior to KnownGood-specific publication/recovery in Story 7.10. |
| F-17 | Remediated | FirstInstall planning/execution-recovery are Stories 7.11-7.12; rollback planning/confirmation and execution/recovery are Stories 7.13-7.14. |
| F-18 | Remediated | Release command parsing is Story 7.3; aggregate release verification and Host smoke are Story 7.15. |

## Architecture Divergence Review

| Finding | Disposition | Remediation evidence |
| --- | --- | --- |
| F-01 | User override | Canonical epics.md intentionally replaces the planning-root tombstone. The archive/digest and all non-path quarantine invariants remain. Contract and ledger both state the expected legacy-validator failure. |
| F-02 | Remediated | Frontmatter is remediated-draft, assignable false, implementationAuthority false; authority prose says concrete GWT is review material and cannot promote the artifact. |
| F-03 | Remediated | Contract C-01 and Story 1.3 permit exactly byte-exact inherited assertions and typed approved-deviation replacements; generic normalization is prohibited. |
| F-04 | Remediated | Contract C-02 and Story 1.4 keep CanonicalJsonV1 newline-free and add exactly one presenter terminator outside hashes/frames/persistence. |
| F-05 | Remediated | Contract C-02 and Story 5.3 freeze decode status, Unicode 16.0 NFC, full default fold, NFC, scalar substring, and uppercase-percent raw-byte fallback. |
| F-06 | Remediated | Story 1.1 owns tests/architecture_boundaries.rs, cargo test --locked --test architecture_boundaries, dependency/side-effect assertions, and release-CI aggregate ownership; override behavior is isolated. |
| F-07 | Remediated | Contracts C-01/C-02, Stories 1.2-1.4, and AD11 registry require fixed checked-in goldens, two independent encoders, provenance, and prohibit generation/recapture by Rust under test. |
| F-08 | Remediated | Contract C-07 and Story 1.6 freeze the exact current AD-16 WAL/synchronous/foreign-key/busy-timeout order/readbacks, modes, transactions, migration, and fail-closed behavior for fresh/existing databases. The final spine does not specify trusted_schema, application_id, or page-size, so batch 1 explicitly does not invent them. |
| F-09 | Remediated | Contract C-07 and Story 1.8 freeze age/count/pins, st_blocks times 512, eligible pruning, one capacity-exhausted mode, admitted finalization allowance, refusal classes, and stateless compatibility. |
| F-10 | Remediated | Story 2.3 rejects invalid persistent intent with no durable Promise. |
| F-11 | Remediated | Stories 3.6/3.7 use only immutable Docker and PM2 identity inputs; timestamps and OS PID are evidence. |
| F-12 | Remediated | Story 3.8 suppresses only exact srvls and in-group worker/provider descendants; escaped descendants remain unless independently Provider-owned. |
| F-13 | Remediated | Contract C-09 and Story 3.3 freeze AF_UNIX stream socketpair, FD3 ownership, credentials, four frames/key order, caps, cuts, diagnostic parameters, EOF, and failure precedence. |
| F-14 | Remediated | Contracts C-09/C-10 and Stories 1.9/3.3 freeze terminal report/candidate before pending reaper; WorkerReapEvidenceV1 cannot rewrite truth. |
| F-15 | Remediated | ActionKindV1 omits signal; Story 6.7 carries direct-process signal as stop parameters. |
| F-16 | Remediated | Story 6.3 ActionPlanV1 contains PlanId only; Story 6.6 allocates OperationId atomically at submit. |
| F-17 | Remediated | Contract C-10 and Story 6.6 use only planned, launch-authorized, executing, verifying; pre-launch refusal is an outcome. |
| F-18 | Remediated | Contracts C-10 and Story 6.10 prohibit detachment and require process liveness/finalization retry until durable terminal truth. |
| F-19 | Remediated | Contract C-10 and Stories 6.7/7.6 require in-process lock-owning mutation; CommandRunner remains read-only and mutating child systemctl is forbidden. |
| F-20 | Remediated | Contract C-11 and Story 7.1 require StableToolchainEvidenceV1, fresh official 1.97.1 identity, precompile failure for 1.97.0, exact artifact readelf glibc-2.42 proof, checksum, and smoke. |
| F-21 | Remediated | Contract C-11 and Story 7.2 freeze F_SETLK/F_SETLKW, [0,1), F_RDLCK/F_WRLCK, F_GETFD CLOEXEC, prohibitions, owner-loss, and shared-drain ordering. |
| F-22 | Remediated | Contract C-11 and Stories 7.1/7.5/7.10/7.11 use only ReleaseBinaryArtifactV1, UpgradeTransactionV1, KnownGoodReleaseV1, FirstInstallAbsentV1. |
| F-23 | Remediated | Stories 7.4/7.6 freeze two sorted metrics/snapshot pairs, exactly two executable substitutions, and byte identity for every other fragment/property/scalar. |
| F-24 | Remediated | Contract C-12 and Story 7.7 freeze exact ReleaseValidationRequestV1/ResultV1 key orders and reject every extension field. |
| F-25 | Remediated | Contract C-12 and Story 7.7 own AddMatch acknowledgement, owner lookup/matches, Subscribe reply, owner recheck, drain barrier, baseline, trigger, failure rows, and one ARCH-LIM-24 cut. |
| F-26 | Remediated | Contract C-11 and Stories 7.8-7.15 use exactly pending, committed, forward-failed-recovered, rolled-back, rollback-unavailable, upgrade-recovery-required; public output excludes pending. |
| F-27 | Remediated | Contract C-11 and Stories 7.10/7.14 publish KnownGood only after decision with no extra pointer data and publish displaced source after successful rollback. |
| F-28 | Remediated | Contract C-11 and Stories 7.11-7.13 freeze FirstInstallAbsentV1, generation zero, every absence authority/cut, foreign replacement refusal, complete readback, and zero-mutation rollback-unavailable. |
| F-29 | Remediated | Contract C-11 and Story 7.3 expose exactly install/upgrade/validate/status/rollback; Stories 2.6/6.11/7.3 freeze typed argv, records, exits, and no stdin alternative. |
| F-30 | Remediated | The JSON registry maps every explicit AD-11 row ID to owning Story, exact fixture path, validator assertion, aggregate command, and current/future delivery status. |

## Validation Contract

Batch-1 completion requires all of the following:

1. Exactly seven unique Epic headings and unique sequential Story headings.
2. Every story has user value, Implementation Boundary, Requirement Mapping,
   Dependencies, Validation Expectations, Out of Scope, and exactly two
   numbered concrete Given/When/Then/And acceptance criteria.
3. Dependencies are None only for Story 1.1; every other dependency is one exact
   earlier Story ID.
4. The JSON registry parses and proves 43 FR, 16 NFR, 6 UJ, 83 core UX IDs,
   5 UX accessibility IDs, SR-A11Y-1, AD-1 through AD-25, ARCH-LIM-1 through
   ARCH-LIM-24, ARCH-HOST-1, and all supplemental metrics are covered.
5. Every AD-11 row has owner, fixture, assertion, aggregate command, and
   current/future status.
6. Markdown structure and whitespace pass the repository profile.
7. The architecture aggregate passes except for the single user-overridden
   planning-root tombstone expectation; a quarantine-specific probe proves the
   archive digest, discovery uniqueness, and exact expected legacy failure.
8. Git diff contains only epics.md and this ledger before commit.

## Validation Results

| Check | Result |
| --- | --- |
| Strict structural parser | PASS: one H1, seven unique sequential Epic headings, 73 unique sequential Story headings, every required story section, and exactly two numbered GWT criteria per story. |
| Fenced JSON and coverage | PASS: one fenced JSON registry parses; 213 required and supplemental IDs have reciprocal Story ownership; all 68 AD-11 rows have unique IDs and complete owner/fixture/assertion/aggregate/delivery fields. |
| Dependencies | PASS: Story 1.1 alone is None; every later story names exactly the immediately prior Story ID. |
| Finding dispositions | PASS: one ordered disposition exists for all 7 product, 18 story-quality, and 30 architecture findings. |
| Markdown | PASS: both artifacts report zero errors under the repository Markdown profile. |
| Legacy quarantine validator | EXPECTED OVERRIDE: the sole failure is "planning-root tombstone does not fail closed". |
| Override-aware quarantine probe | PASS: canonical discovery is unique; draft/nonassignable authority is explicit; discovery globs, fuzzy-alias guard, retired archive, and archive digest are unchanged. |
| Architecture aggregate | EXPECTED OVERRIDE: all frozen compatibility, source-pin, immutable-hash, and AD-9 lanes pass before the same sole legacy quarantine assertion. |
| Diff hygiene | PASS: whitespace is clean and the commit scope contains only canonical epics.md and this ledger. |
