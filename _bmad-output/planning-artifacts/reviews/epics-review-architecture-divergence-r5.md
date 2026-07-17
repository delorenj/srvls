---
type: architecture-divergence-review
status: complete
assignable: false
implementationAuthority: false
reviewedCommit: a01028a449a67b57c571d534e40721e8ee5da453
reviewedArtifact: _bmad-output/planning-artifacts/epics.md
reviewedSha256: 7d749899972903b90c76df2825bfbfaf0055e0f83544cd72cb7d648af8ad645c
architectureSha256: 28a103267a8e4ae5411c314bc2f9c0b62b694352e6e91c2522a2271df16ff575
sourceReviewSha256: a70810aab2adbd9b98e3d58f3a298ae638ffd8f2ff04b1ebb620d4127e53ad6c
verdict: FAIL
findingCount: 1
---

# Epics Architecture-Divergence Review R5

## Digest and Verdict

**FAIL — 1 finding. PASS requires zero.** The reviewed artifact is exactly the
`epics.md` blob at `a01028a`; its SHA-256 begins with the requested `7d749899`
digest and the worktree matched that committed blob before this report was
written. Batch 4 closes all 12 R4 findings, restores the aggregate gate, adds
complete AD-11 reciprocity, and returns the affected stories to
architecture-native outcomes. The candidate still leaves two AD-23 stories
with two incompatible fixture authorities, so it remains nonassignable and is
not implementation authority.

| Input | SHA-256 |
| --- | --- |
| `a01028a:_bmad-output/planning-artifacts/epics.md` | `7d749899972903b90c76df2825bfbfaf0055e0f83544cd72cb7d648af8ad645c` |
| Binding architecture spine | `28a103267a8e4ae5411c314bc2f9c0b62b694352e6e91c2522a2271df16ff575` |
| R4 architecture-divergence review | `a70810aab2adbd9b98e3d58f3a298ae638ffd8f2ff04b1ebb620d4127e53ad6c` |

## Method

- Pinned and hashed the current `epics.md`, binding architecture spine, and R4
  review; parsed the sole normative JSON block independently.
- Checked all declared counts, 73 story IDs, reciprocal coverage maps, 84
  unique AD-11 IDs, every row owner, all six required row fields, delivery
  classes, fixture paths, assertions, and aggregate commands.
- Replayed every R4 finding against Batch 4's contracts, story boundaries,
  acceptance criteria, AD-11 rows, and executable gates.
- Audited AD-1 through AD-25 against their complete binding rules rather than
  accepting requirement-mapping tags as semantic evidence.
- Ran the planning-quarantine, compatibility, canonical-contract, release,
  Host-smoke, and aggregate architecture gates independently. Every applicable
  checked-in gate passed.
- Compared each future row's named fixture authority with its owning story's
  Validation Expectations and concrete acceptance fixture. This exposed the
  remaining split authority below.

## Finding

1. **R5-01 — Stories 7.8 and 7.10 each retain two incompatible AD-23 fixture
   authorities.** AD11-FUT-70 declares
   `tests/fixtures/implementation/installed-prior-forward-v1` and
   `assert_installed_prior_forward_to_commit_decided` as Story 7.8's future
   implementation obligation (`epics.md:2258-2263`), and Story 7.8 repeats that
   directory as its singular owning oracle (`epics.md:3800-3804`). Its positive
   AC instead executes
   `tests/fixtures/contracts/release-transaction-v1/forward.transitions.jsonl`
   (`epics.md:3808-3811`). AD11-FUT-50 and Story 7.10 similarly declare
   `tests/fixtures/implementation/installed-prior-known-good-v1` as the owning
   future implementation oracle (`epics.md:2090-2095,3846-3850`), while AC1
   executes only the checked-in standalone
   `known-good-publication-pending.manifest.json`
   (`epics.md:3854-3857`). AD-11 distinguishes checked-in declarative release
   contracts from the mandatory future implementation gate
   (`ARCHITECTURE-SPINE.md:518-531,729-769`) and explicitly says the current
   transaction histories are not deployed-command execution evidence
   (`ARCHITECTURE-SPINE.md:789-793`). Therefore both stories can pass their ACs
   without creating or executing the registry's named implementation fixture,
   or an implementer can treat the registry/Validation Expectations as
   authoritative and ignore the AC fixture. AD-11 requires one deterministic
   acceptance authority. Repoint each positive AC to its registered
   implementation fixture, or explicitly define and gate a single composition
   that proves the current contract bytes through that implementation fixture.

## R4 Finding Closure

| R4 finding | R5 result | Current evidence |
| --- | --- | --- |
| R4-01 — red aggregate command | Closed | Planning discovery/quarantine passes and `bash tests/validate_architecture_contracts.sh` runs all five current lanes to PASS. |
| R4-02 — Story 1.10 lacks a row | Closed | AD11-FUT-69 owns Story 1.10; row-owner and AD-11 coverage are reciprocal. |
| R4-03 — canonical override contradicts failure AC | Closed | Story 1.10 now passes the authorized canonical artifact and fails only missing/non-final canonical or discoverable archive states. |
| R4-04 — universal foreign result model | Closed | `contract_violation` is absent; structural violations are test rejection and runtime cases use architecture-native typed outcomes. |
| R4-05 — FD3 loses AD-25 normalization | Closed | Story 3.3 AC2 requires exactly one AD-25 reason in a `timed-out` or `invalid-output` CollectorReport. |
| R4-06 — cron partial/denied becomes fatal | Closed | Story 3.4 preserves usable evidence and Contract C-16 `denied`, `invalid-output`, or `partial`. |
| R4-07 — systemd scoped failures collapse | Closed | Story 3.5 retains scoped `unavailable`, `partial`, `denied`, or `invalid-output` with distinct diagnostics. |
| R4-08 — process cleanup semantics collapse | Closed | Story 3.8 preserves weak evidence, PID-reuse identity, and synthesized `worker-timeout` without child exposure/read. |
| R4-09 — FUT-68 has two oracles and a foreign result | Closed | Story 6.7 explicitly owns both fixture families and uses the complete architecture-native Provider result vocabulary. |
| R4-10 — action races bypass five outcomes | Closed | Stories 6.4 and 6.9 require `refused/stale-identity` pre-launch and `executed-unverified` after launch. |
| R4-11 — duplicate/expired admissions become schema errors | Closed | Story 6.6 requires `refused/duplicate-operation` and `refused/plan-expired`. |
| R4-12 — Story 7.9 splits recovery terminalization | Closed | Story 7.8 now owns forward-to-decision; Story 7.9 owns installed-prior pre-decision restoration and its two terminal results; Story 7.10 owns post-decision publication/admission/commit. |

## AD-1 Through AD-25 Audit

| Decision | Result | Backlog evidence |
| --- | --- | --- |
| AD-1 | Conforms | Story 1.1 owns inward dependency direction and the boundary gate. |
| AD-2 | Conforms | Promise, Observation, Finding, Snapshot, and Operation ownership remains separated. |
| AD-3 | Conforms | Ports and in-process owners retain all side-effect authority. |
| AD-4 | Conforms | Story 4.10 and FUT-63 own deterministic evidence-based Stack/Ungrouped grouping. |
| AD-5 | Conforms | Stories 3.3-3.10 retain the six scoped collection outcomes, usable evidence, and Candidate/Snapshot separation. |
| AD-6 | Conforms | Stories 6.1-6.9 retain exact-target plans, revalidation, admission, and the closed five-outcome vocabulary. |
| AD-7 | Conforms | Routing and the exact five-verb release grammar remain explicit. |
| AD-8 | Conforms | Text-primary, Unicode, hostile-text, ASCII, accessibility, and motion rules remain owned. |
| AD-9 | Conforms | Compatibility and approved-deviation lanes pass independently and in the aggregate. |
| AD-10 | Conforms | Frozen scheduling, reservations, cuts, pools, typed capture, and immutable reports remain explicit. |
| AD-11 | **Diverges** | Registry mechanics and the current aggregate pass, but FUT-50 and FUT-70 do not have one acceptance authority (R5-01). |
| AD-12 | Conforms | Moving stable, Rust 1.88 MSRV, exact-artifact hash, ABI proof, and Host smoke remain represented. |
| AD-13 | Conforms | Typed identities and canonical property coverage remain represented. |
| AD-14 | Conforms | One terminal/shutdown owner and durable no-detach behavior remain explicit. |
| AD-15 | Conforms | Provider privilege/environment and distinct denial/error semantics are acceptance-owned by Story 6.7 and FUT-68. |
| AD-16 | Conforms | SQLite transactions, CAS, retention, recovery, capacity, and sole durable truth remain owned. |
| AD-17 | Conforms | Promise lifecycle and `lease_prerequisite_missing` persistence rejection are exact and reciprocal. |
| AD-18 | Conforms | Frozen pure reconciliation, orthogonal axes, duplicate cardinality, grouping, and safety remain represented. |
| AD-19 | Conforms | Typed precedence, provenance, validation, visibility, and no-hot-reload remain explicit. |
| AD-20 | Conforms | ARCH-LIM-1 through ARCH-LIM-24 remain inventoried and acceptance-mapped. |
| AD-21 | Conforms | Collection scheduling, frozen cuts, scoped results, reduction, and sole current CAS remain explicit. |
| AD-22 | Conforms | Revalidation, pool, admission, execution, verification, recovery, and UI parity retain one durable handoff. |
| AD-23 | **Diverges** | Transaction ownership and terminal boundaries now conform, but two release stories retain split implementation-versus-contract fixture authority (R5-01). |
| AD-24 | Conforms | Canonical JSON, binary identities, paths, fingerprints, and fixed bytes remain owned. |
| AD-25 | Conforms | Story 3.3 preserves total FD3 precedence, synthesized reports, cleanup, and immutable post-cut evidence. |

## Every AD-11 Row and Obligation

All 84 IDs are unique: 14 current and 70 future. Every row has all six required
fields, a valid story owner, a valid delivery class, and the exact aggregate
command. All 62 unique row owners appear in reciprocal AD-11 coverage, and no
AD-11-mapped story lacks a row. “Conforms” below means the row's named fixture,
assertion, owner, delivery, story semantics, and acceptance authority agree.

| Row | Owner | Result | Obligation evidence |
| --- | --- | --- | --- |
| AD11-CUR-01 | Story 1.3 | Conforms | Legacy CLI matrix passes in the aggregate. |
| AD11-CUR-02 | Story 1.3 | Conforms | Legacy output bytes pass in the aggregate. |
| AD11-CUR-03 | Story 1.3 | Conforms | Legacy Provider matrix passes in the aggregate. |
| AD11-CUR-04 | Story 1.3 | Conforms | Legacy inspection matrix passes in the aggregate. |
| AD11-CUR-05 | Story 1.3 | Conforms | Legacy action argv matrix passes in the aggregate. |
| AD11-CUR-06 | Story 1.4 | Conforms | Contract manifest passes in the aggregate. |
| AD11-CUR-07 | Story 1.4 | Conforms | Fixed policy bytes pass in the aggregate. |
| AD11-CUR-08 | Story 3.1 | Conforms | Fixed plan/scope bytes pass in the aggregate. |
| AD11-CUR-09 | Story 1.4 | Conforms | Fixed identity bytes pass in the aggregate. |
| AD11-CUR-10 | Story 3.1 | Conforms | Fixed assignment bytes pass in the aggregate. |
| AD11-CUR-11 | Story 3.3 | Conforms | FD3 four-frame bytes pass in the aggregate. |
| AD11-CUR-12 | Story 3.3 | Conforms | FD3 no-allocation cut passes in the aggregate. |
| AD11-CUR-13 | Story 7.15 | Conforms | Release subcorpus passes in the aggregate. |
| AD11-CUR-14 | Story 1.3 | Conforms | Legacy Host smoke passes in the aggregate. |
| AD11-FUT-01 | Story 1.1 | Conforms | Dependency direction and sole side-effect owner. |
| AD11-FUT-02 | Story 1.5 | Conforms | Configuration and all architecture limits. |
| AD11-FUT-03 | Story 1.6 | Conforms | Fresh/existing SQLite initialization and readback. |
| AD11-FUT-04 | Story 1.7 | Conforms | Atomic repository CAS and unavailable results. |
| AD11-FUT-05 | Story 1.8 | Conforms | Pins, watermarks, retention, and capacity. |
| AD11-FUT-06 | Story 1.9 | Conforms | Runner terminal result freezes before reap. |
| AD11-FUT-07 | Story 2.1 | Conforms | Principal and Promise-owner authentication. |
| AD11-FUT-08 | Story 2.2 | Conforms | Declare/revise idempotency and revision conflict. |
| AD11-FUT-09 | Story 2.3 | Conforms | Boot/clock rules and exact persistent-prerequisite rejection. |
| AD11-FUT-10 | Story 3.2 | Conforms | Default frozen dispatch schedule. |
| AD11-FUT-11 | Story 3.2 | Conforms | Near-tie frozen schedule. |
| AD11-FUT-12 | Story 3.2 | Conforms | Sixty-second zero-margin schedule. |
| AD11-FUT-13 | Story 3.2 | Conforms | Missed-cut admission with no post-cut allocation. |
| AD11-FUT-14 | Story 3.3 | Conforms | Peer credentials and Ready behavior preserve AD-25. |
| AD11-FUT-15 | Story 3.3 | Conforms | Descriptor ownership and EOF preserve AD-25. |
| AD11-FUT-16 | Story 3.3 | Conforms | Total failure precedence yields one typed report. |
| AD11-FUT-17 | Story 3.3 | Conforms | Report remains immutable before late reap evidence. |
| AD11-FUT-18 | Story 3.4 | Conforms | Cron retains partial/denied/invalid-output and usable evidence. |
| AD11-FUT-19 | Story 3.5 | Conforms | Systemd retains distinct scoped results and diagnostics. |
| AD11-FUT-20 | Story 3.6 | Conforms | Docker identity matrix. |
| AD11-FUT-21 | Story 3.7 | Conforms | PM2 identity matrix. |
| AD11-FUT-22 | Story 3.8 | Conforms | Process suppression, PID reuse, and unresolved cleanup. |
| AD11-FUT-23 | Story 3.9 | Conforms | CollectionCandidate remains distinct from Snapshot. |
| AD11-FUT-24 | Story 3.10 | Conforms | Obligation, strict-mode, reason, and evidence matrix. |
| AD11-FUT-25 | Story 4.1 | Conforms | Correlation vectors, conflicts, ties, and frozen input. |
| AD11-FUT-26 | Story 4.3 | Conforms | Duplicate set/cardinality without loser selection. |
| AD11-FUT-27 | Story 4.4 | Conforms | Stale/hot positive evidence and history races. |
| AD11-FUT-28 | Story 4.7 | Conforms | Snapshot materialization and sole current CAS. |
| AD11-FUT-29 | Story 4.8 | Conforms | Baseline races, compatibility, and override. |
| AD11-FUT-30 | Story 4.9 | Conforms | Eight Brief rows and drill-down evidence. |
| AD11-FUT-31 | Story 5.1 | Conforms | Routing and terminal restoration. |
| AD11-FUT-32 | Story 5.3 | Conforms | Unicode search, focus, and retarget protection. |
| AD11-FUT-33 | Story 5.5 | Conforms | Plane/Git/telemetry remain display-only. |
| AD11-FUT-34 | Story 5.7 | Conforms | Text-primary accessibility and hostile text. |
| AD11-FUT-35 | Story 5.9 | Conforms | Read-only Host budgets and independent goldens. |
| AD11-FUT-36 | Story 6.1 | Conforms | Closed ActionKind matrix. |
| AD11-FUT-37 | Story 6.3 | Conforms | Immutable plan and complete confirmation matrix. |
| AD11-FUT-38 | Story 6.5 | Conforms | Separate pool before admission; saturation refuses. |
| AD11-FUT-39 | Story 6.6 | Conforms | Operation phases, IDs, duplicate, and expiry outcomes. |
| AD11-FUT-40 | Story 6.7 | Conforms | Exact in-process mutation owner. |
| AD11-FUT-41 | Story 6.9 | Conforms | Five-outcome action precedence and replacement race. |
| AD11-FUT-42 | Story 6.10 | Conforms | No detach and durable finalization. |
| AD11-FUT-43 | Story 6.12 | Conforms | Action, budgets, journey, and accessibility aggregate. |
| AD11-FUT-44 | Story 7.1 | Conforms | Moving stable/MSRV, exact artifact, ABI, and smoke. |
| AD11-FUT-45 | Story 7.2 | Conforms | Traditional POSIX record-lock ownership. |
| AD11-FUT-46 | Story 7.6 | Conforms | Pair-qualified source and ExecStart rewrite cardinality. |
| AD11-FUT-47 | Story 7.7 | Conforms | Exact FD4 request/result bytes and authentication. |
| AD11-FUT-48 | Story 7.7 | Conforms | D-Bus handshake and one shared validation cut. |
| AD11-FUT-49 | Story 7.9 | Conforms | Installed-prior pre-decision restore and terminalization. |
| AD11-FUT-50 | Story 7.10 | **Diverges** | Registered implementation fixture is not the fixture executed by AC1 (R5-01). |
| AD11-FUT-51 | Story 7.12 | Conforms | FirstInstall absence restoration and recovery. |
| AD11-FUT-52 | Story 7.14 | Conforms | Explicit rollback and displaced-source publication. |
| AD11-FUT-53 | Story 7.3 | Conforms | Exact release grammar, results, arguments, and confirmation. |
| AD11-FUT-54 | Story 7.15 | Conforms | Exact final-artifact Host smoke. |
| AD11-FUT-55 | Story 7.15 | Conforms | Isolated service-manager CI rows. |
| AD11-FUT-56 | Story 1.4 | Conforms | Canonical policy/scope/diagnostic/candidate/process properties. |
| AD11-FUT-57 | Story 2.4 | Conforms | Heartbeat idempotency, cadence, Lease ceiling, and owner checks. |
| AD11-FUT-58 | Story 2.5 | Conforms | Close idempotency and inactive projection. |
| AD11-FUT-59 | Story 2.6 | Conforms | Agent linear/JSON argv/result/exit matrix. |
| AD11-FUT-60 | Story 4.2 | Conforms | Orthogonal healthy/broken/unresolved/inactive outcomes. |
| AD11-FUT-61 | Story 4.5 | Conforms | Unmanaged/abandoned coexistence without cleanup. |
| AD11-FUT-62 | Story 4.6 | Conforms | Complete conservative Safe-to-stop matrix. |
| AD11-FUT-63 | Story 4.10 | Conforms | Deterministic Stack/Ungrouped grouping. |
| AD11-FUT-64 | Story 6.4 | Conforms | Immediate revalidation uses closed AD-6 results. |
| AD11-FUT-65 | Story 6.11 | Conforms | TUI/linear/JSON action parity. |
| AD11-FUT-66 | Story 7.4 | Conforms | Two-pair discovery/readback before preimages. |
| AD11-FUT-67 | Story 7.15 | Conforms | Both pairs through every effect and crash cut. |
| AD11-FUT-68 | Story 6.7 | Conforms | Privilege/environment fixture and architecture-native results share explicit ownership. |
| AD11-FUT-69 | Story 1.10 | Conforms | Canonical discovery and retired-archive quarantine. |
| AD11-FUT-70 | Story 7.8 | **Diverges** | Registered implementation fixture is not the fixture executed by AC1 (R5-01). |

## Executable Evidence and Final Gate

| Check | Result |
| --- | --- |
| Pinned SHA-256 and requested `7d749899` prefix | PASS |
| JSON parse, counts, row IDs, fields, owners, delivery classes | PASS — 84 unique rows; 14 current, 70 future |
| AD-11 row-owner reciprocity | PASS — 62 unique owners; no missing or extra mapped owner |
| AD-1..25 reciprocal registry mappings | PASS |
| `python3 tests/validate_planning_quarantine.py` | PASS — two exact globs, one canonical artifact, one byte-exact retired archive |
| `bash tests/compat/validate.sh` | PASS — 90 inherited plus 4 approved deviations |
| `python3 tests/fixtures/contracts/validate.py` | PASS through aggregate |
| `python3 tests/fixtures/contracts/release-transaction-v1/validate_oracles.py` | PASS through aggregate — all reported live and mutation families |
| `bash tests/test_smoke.sh` | PASS — JSON, Prometheus, Markdown, table, inspect, hostile-name safety |
| `bash tests/validate_architecture_contracts.sh` | PASS — all current lanes run together |
| R4 architecture-finding replay | PASS — all 12 findings closed |
| Semantic AD-1..25 and every-row audit | FAIL — R5-01 affects AD-11, AD-23, FUT-50, and FUT-70 |

**Final gate: FAIL — 1 finding. PASS is prohibited above zero.** A later
candidate must make each of Stories 7.8 and 7.10 execute the same future
implementation fixture named by its AD-11 row and Validation Expectations, or
define one explicit composed oracle that makes the checked-in contract fixture
an input to that registered implementation gate.
