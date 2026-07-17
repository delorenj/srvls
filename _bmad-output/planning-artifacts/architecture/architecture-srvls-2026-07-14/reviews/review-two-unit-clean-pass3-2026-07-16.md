---
title: "srvls Architecture Two-Unit Clean Pass 3"
type: architecture-review
status: final
created: 2026-07-16
updated: 2026-07-16
reviewer: Sir Fix-a-Lot
review_mode: independent-final-two-unit-divergence-clean-pass3
reviewed_commit: db70e84c74a301d6e698cddf0c88fb47e78da851
reviewed_spine_sha256: 5907c2f7da67378c6da60de0ed6374b9393d30b7945d271e6e261467ebce9392
reviewed_spine_line_count: 2359
reviewed_memlog_sha256: ea143f28e2bb88b54835ecb2313c950812e02d8d45835cc86124e511226d915c
reviewed_memlog_line_count: 146
reviewed_artifact: _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md
verdict: changes-required
blocking_status: blocked
finding_count: 10
blocking_findings: 8
high_findings: 2
moderate_findings: 0
low_findings: 0
---

<!-- markdownlint-disable MD013 MD025 -->

# Architecture Review: Two-Unit Clean Pass 3

## Verdict

**CHANGES REQUIRED. Blocking status: BLOCKED. Finding count: 10.**

The repaired PolicySnapshotV1 grammar, frozen schedules, process gate, FD3
duplicate rejection, explicit `rollback-unavailable` result, timer
ActivationDetails causal predicate, and persisted validation deadlines converge.
PASS is nevertheless prohibited. Eight blocking counterexamples still let two
independent implementations produce different identity, plan, worker, release,
or recovery truth; two high findings leave the timer race proof and declared
compatibility/golden oracles unenforceable.

The sharpest regressions are at remediated seams. An already-expired reservation
must be terminalized before request-ID allocation, but its required timeout
diagnostic cannot be encoded without that ID. Cron, PM2, and process
ObservationId hash inputs still use an undefined “length-framed” grammar, and
the fixed identity fixtures inject the finished hashes rather than testing those
preimages. CollectionPlanV1 still admits different scope-reason, resource-row,
and opaque baseline bytes. ProviderScopeInputV1, CollectorReportV1, and the
release recovery envelope likewise lack complete nested wire schemas.

This review changed only this report. It did not edit the architecture spine,
memory log, task ledger, product code, tests, or any prior report.

## Frozen Target and Review Isolation

| Property | Frozen value |
| --- | --- |
| Worktree | `worktrees/team-argus/worktrees/sir-fix-a-lot-architecture-clean-pass3` |
| Branch | `feature-sir-fix-a-lot-architecture-clean-pass3` |
| Commit | `db70e84c74a301d6e698cddf0c88fb47e78da851` |
| Spine | 2,359 lines; SHA-256 `5907c2f7da67378c6da60de0ed6374b9393d30b7945d271e6e261467ebce9392` |
| Architecture memory log | 146 lines; SHA-256 `ea143f28e2bb88b54835ecb2313c950812e02d8d45835cc86124e511226d915c` |
| Historical two-unit reports | Ten reports through clean pass 2, all read through EOF |
| New pass-3 peer reports | Zero opened, searched, diffed, or used |
| Starting tree | Clean |

`AGENTS.md`, `tasks.md`, the complete configured BMAD architecture skill, and
its complete `headless.md` and `reviewer-gate.md` references were read before
the gate. `ARCHITECTURE-SPINE.md` and `.memlog.md` were read through EOF. The ten
eligible two-unit reports were replayed as counterexample history, not accepted
as proof. No new pass-3 peer report was read.

The acceptance rule was literal interoperability. Each unit had to select the
same bytes, identities, absolute cuts, child state, durable state, and terminal
result from the normative artifact alone. A convention that two modules could
privately share inside one codebase did not count as an architecture contract.

## Independent Reconstructions

| Unit | Independent implementation |
| --- | --- |
| Unit A — Literal Compiler | Built schema tables, binary preimages, the LPT reservation machine, deadline-first worker admission, diagnostic assignment, repository cuts, action recovery, and release recovery directly from normative sentences and tables. Undefined names, widths, or variants were not silently imported from Rust or serde conventions. |
| Unit B — Recovery Compiler | Independently rebuilt the same system from persisted checksums, crash ownership, FD3/FD4 exchanges, terminal postconditions, and historical compatibility obligations. It chose representations only where the spine made them constructible and attacked recovery with different codec and event-loop choices. |

Unit B was isolated without Unit A's working notes or conversation context.
Unit A froze its findings before any Unit B or reviewer-lens result was opened.
They shared no implementation, schema registry, field-name convention, frame
width, timeout fallback, fixture generator, or release shortcut. Both received
only the frozen artifacts and the same adversarial inputs. Separate historical
replay and currentness/reality lenses then tested the combined result; they did
not substitute for either unit.

## Adversarial Input Ledger

| Probe | Frozen input | Unit A result | Unit B result |
| --- | --- | --- | --- |
| Expired epoch-zero reservation | First runtime sample equals the member cut; no capability, socket, or child may exist | Cannot serialize the mandatory diagnostic because `request_id` does not exist | Allocates or synthesizes a UUID to make the diagnostic encodable |
| Worker report | Same complete logical report, one observation, one diagnostic reference | Uses literal snake-case report keys and one tagged option layout | Uses a different shared-schema key/option layout because none is declared |
| Active-Promise scope | Same promoted scope and obligation | Emits reason `active-promise` | Emits reason `promise-required` |
| Resource-history row | Same sample UUID, Snapshot UUID, and process ObservationIdV1 | Encodes the complete ObservationIdV1 as uppercase-percent binary | Follows “three UUIDs” and encodes a UUID-shaped surrogate |
| Cron identity | Schedule `* * * * *`, user `root`, command `/bin/true` | Uses `u32be` component lengths | Uses `u64be` component lengths |
| Provider scope input | Same nonempty argv, environment, and read-root lists | Uses `u32be` nested element and pair lengths | Uses a different legal “length-framed” width |
| Upgrade recovery | Same pending canonical transaction and recovery owner | Checksums prose-listed fields in their narrative order | Checksums repository-owned fields in declaration order |
| Admission child | Child receives `SIGSTOP` after `fork` and before its first close action; parent dies | Assumes the planned first close releases the lease | Observes the child retain the inherited `flock` open-file description |
| First-install failure | No prior managed consumer unit exists | Removes newly written consumer files and proves absence | Cannot satisfy `restore-recorded` and leaves admission recovering |
| Timer signal | Correct timer fires after match setup but no manager `Subscribe()` reply was obtained | Waits until the persisted deadline without the required job signals | Completes the manager subscription handshake and accepts the causal job |

For the cron probe, the exact SHA-256 preimages differ despite identical logical
inputs:

| Inner frame choice | `srvls-cron-entry-v1` hash |
| --- | --- |
| `u32be` length per component | `c210644a8d9810c02bc8bf23b1fea8efe9a0968b0ab125f62fde8b8abdc8feaf` |
| `u64be` length per component | `0a8e4411a037fb07a6a05e0d33571d8e112b1073237b2b84ac4997fa63e6ffb8` |

## Requested Seam Matrix

| Seam | Result | Evidence |
| --- | --- | --- |
| PolicySnapshotV1 byte totality | **CONVERGED.** Top-level order, every nested key, leaf units, exclusions, fingerprint domain, and default token are fixed. | `SPINE:1624-1663`, `526-546` |
| CollectionPlanV1 nested schemas and goldens | **DIVERGED.** Top-level structure is exact; obligation reasons, ResourceHistory observation identity, and opaque baseline-inner bytes are not. The named minimal fixture contains no baseline or history row. | `SPINE:1690-1811`, `526-546`, CLEAN3-B03 |
| ObservationIdV1 variants | **PARTIAL.** Systemd and Docker converge; cron, PM2, and process diverge in their nested hash preimages. | `SPINE:757-777`, `548-560`, CLEAN3-B04 |
| Expired reservation catch-up | **PARTIAL.** Strict-before, no-spawn, earlier-cut, ascending catch-up, and expired-before-live ordering converge; the chosen no-child report is not constructible. | `SPINE:350-382`, `498-506`, `2004-2035`, CLEAN3-B01 |
| FD3 duplicate fail-closed behavior | **CONVERGED at the requested seam.** Every duplicate rejects before Hello and the descriptor-clean fixture alone reaches Result/EOF. The report embedded in an otherwise clean Result remains non-byte-total. | `SPINE:575-589`, `1869-1889`, CLEAN3-B02 |
| Admission lease inheritance and child whitelists | **DIVERGED.** The whitelist is exact after its first child action, but Linux `fork` has an earlier inherited-lock window that contradicts the no-child-lifetime guarantee. | `SPINE:604-611`, `1242-1274`, CLEAN3-B07 |
| FirstInstallAbsentV1 recovery | **DIVERGED for absent prior consumers.** Binary/link and state paths are covered, but consumer absence is not representable. | `SPINE:1487-1501`, `1524-1535`, CLEAN3-B08 |
| FirstInstallAbsentV1 explicit rollback | **CONVERGED.** It performs only the shared ready-admission read and returns byte-identical `rollback-unavailable/no-prior-release` with no mutation. | `SPINE:1537-1548` |
| Timer ActivationDetails causality | **CONVERGED semantically.** `trigger_unit`, Job.Unit, JobType, JobRemoved, invocation, and race exclusions establish causality; the preceding signal-subscription handshake is incomplete. | `SPINE:1431-1472`, CLEAN3-H01 |
| Validation deadline recovery | **CONVERGED.** One persisted `CLOCK_BOOTTIME` attempt cut governs all evidence; equality expires it, recovery retains old attempts and persists a fresh owner-bound attempt before replay. | `SPINE:1297-1314`, `1093-1114` |
| State, action, release, and compatibility replay | **ORIGINAL COUNTEREXAMPLES CLOSED.** Atomic state, sole action outcome ownership, effect recovery, and compatibility mappings hold. New release-byte and absent-oracle findings remain. | Historical Replay Matrix; CLEAN3-B06; CLEAN3-H02 |

## Findings

### CLEAN3-B01 — Expired reservations cannot encode their mandatory timeout diagnostic

**Evidence.** Before capability allocation, socket creation, or spawn, AD-10
samples `CLOCK_BOOTTIME`. At equality with either cut, it creates none of those
objects and synthesizes a no-child timeout (`SPINE:350-366`). Request ID and
capability are allocated only after that strict-before check (`SPINE:376-382`).
AD-25 nevertheless requires every `WorkerTransportDiagnosticV1` candidate to
contain `request_id` as a tagged UUID, never tagged absent
(`SPINE:2004-2015`). Its matrix explicitly assigns that same schema to
“deadline with no child” (`SPINE:2034-2035`).

**Exact counterexample.** Resume an admitted epoch-zero reservation exactly at
its scope cut. Unit A obeys the allocation order and has no UUID, so it cannot
encode the one required candidate. Unit B allocates a UUID before or after the
cut, or synthesizes one from the reservation, and emits a valid-looking
candidate. None of those choices is declared. The same frozen plan therefore
yields no CollectorReport, a noncanonical candidate, or implementation-private
diagnostic bytes.

**Required correction.** Either persist a reservation-scoped request UUID in
CollectionPlanV1 and make it available before the runtime check, or make
`request_id` an exact tagged `absent | id` union with `absent` required for
pre-allocation failures. Freeze the no-child candidate bytes and prove that the
fix does not allocate a capability, socket, child, root, or reap record.

### CLEAN3-B02 — The FD3 shared report schemas are not byte-total

**Evidence.** AD-5 lists CollectorReportV1's logical generation, scope,
obligation, observations, duration, diagnostics, and outcome
(`SPINE:143-160`). AD-13 similarly lists DiagnosticCandidateV1's logical fields
(`SPINE:709-748`). WorkerHelloV1, WorkerReadyV1, WorkerRequestV1, and
WorkerResultV1 declare narrative field order but do not exhaustively publish
literal JSON key names and every nested object/union shape
(`SPINE:1901-1932`, `2060-2145`). Most critically, WorkerResult says
CollectorReportV1 and candidates use their “declared-order shared schemas,” but
no such complete schemas exist (`SPINE:2126-2133`).

**Exact counterexample.** Encode the same complete report with one observation,
one candidate reference, no capture truncation, and outcome `complete`. Unit A
uses keys derived from the AD-5 nouns and tagged option objects. Unit B uses its
repository type's distinct report keys, candidate-reference object, and process
extension placement. Both preserve every listed logical field and the stated
order. Their CanonicalJsonV1 payloads differ, so the parent rejects the worker
before any otherwise valid report can become evidence.

**Required correction.** Publish exhaustive CanonicalJsonV1 schemas for all
four frames, CollectorReportV1, ObservationV1 plus every Provider detail,
DiagnosticCandidateV1 and candidate references, capture accounting, and the
process-only self-root/member extension. Fix literal key names, key order,
variant membership, options, arrays, scalar encodings, rejection rules, and
complete independent golden payloads.

### CLEAN3-B03 — CollectionPlanV1 nested bytes and its named goldens remain incomplete

**Evidence.** The repaired plan fixes its top-level and most nested field order
(`SPINE:1690-1811`), but three observable branches remain open:

1. `ScopeManifestV1` persists a nonempty stable-ASCII obligation reason without
   an exhaustive vocabulary or deterministic winning-reason rule
   (`SPINE:1827-1840`). The only fixed example is `default-supported`
   (`SPINE:532-546`).
2. ResourceHistoryCutV1 declares `sample_id`, `snapshot_id`, and
   `observation_id`, then says every value after “the three UUIDs” is unsigned
   (`SPINE:1798-1802`). ObservationIdV1 is a Provider-tagged binary identity,
   not a UUID (`SPINE:757-777`).
3. Baseline byte fields are copied from an immutable persisted Snapshot
   aggregate without semantic reconstruction (`SPINE:1772-1782`), while the
   persisted aggregate is only described as versioned JSON with no exhaustive
   field schema (`SPINE:956-965`). The named minimal CollectionPlan fixture has
   baseline `none` and zero resource rows (`SPINE:532-544`), so it cannot
   arbitrate either nonempty branch.

**Exact counterexample.** For one active-Promise promotion, Unit A emits reason
`active-promise`; Unit B emits `promise-required`. For one history row, Unit A
encodes the complete uppercase-percent ObservationIdV1; Unit B follows “three
UUIDs” and encodes a UUID-shaped surrogate. For one baseline Provider detail,
one unit copies canonical JSON bytes while the other copies a versioned binary
record. Each pair has identical domain truth but different ScopeManifest,
baseline-row, or CollectionPlan fingerprints.

**Required correction.** Freeze the complete obligation-reason vocabulary and
precedence algorithm; name ResourceHistory row scalar types explicitly and use
the complete ObservationIdV1; publish every copied Snapshot aggregate's domain
schema and byte envelope. Add fixed nonempty scope-promotion, baseline-row, and
resource-history fixture inputs with complete expected preimages and hashes.

### CLEAN3-B04 — Three ObservationId hash preimages omit their frame grammar

**Evidence.** The outer ObservationIdV1 envelope, Provider tags, field tags,
widths, display, and final fingerprint are exact (`SPINE:757-777`). The cron
entry hash, PM2 executable/name fingerprint, and process executable/command
fingerprint, however, cover “length-framed” values without defining length
width, byte order, or a shared inner framing rule (`SPINE:763`, `766-767`). No
other spine occurrence defines that phrase. The identity goldens inject
finished hash bytes `0x55`, `0x22`, and `0x44` instead of raw hash inputs
(`SPINE:548-560`).

**Exact counterexample.** For cron schedule `* * * * *`, user `root`, and
command `/bin/true`, `u32be` component lengths yield
`c210644a8d9810c02bc8bf23b1fea8efe9a0968b0ab125f62fde8b8abdc8feaf`;
`u64be` lengths yield
`0a8e4411a037fb07a6a05e0d33571d8e112b1073237b2b84ac4997fa63e6ffb8`.
Both are literal length frames. The same choice changes PM2 and process birth
fingerprints, so the units disagree on ObservationId, baseline ordering,
diagnostic subjects, and Snapshot identity. Systemd and Docker do not use these
inner hash frames and converge.

**Required correction.** Replace every “length-framed” phrase with one exact
binary grammar, including width, endianness, count/order, empty values, raw-path
and NFC treatment, and rejection of trailing bytes. Change each golden to start
from raw logical inputs and assert the inner digest before asserting the full
ObservationId envelope, display, and final fingerprint.

### CLEAN3-B05 — ProviderScopeInputV1 leaves nested list and environment widths open

**Evidence.** The outer field envelope uses `length:u32be`, but list and set
value kinds use `count:u32be` plus undefined “length-framed values”
(`SPINE:2080-2089`). CommandSpecV1 fixes executable and argument lengths, while
the environment set merely uses ASCII-name/raw-value “length pairs” and the
read-root list again relies on the undefined outer list framing
(`SPINE:2089-2097`). These bytes feed ScopeAssignmentFingerprint and are
recomputed before Host work (`SPINE:2103-2114`).

**Exact counterexample.** Give one worker a two-command list, one non-UTF-8
argument, two environment entries, and two read roots. Unit A wraps every list
element and environment name/value with `u32be` lengths. Unit B uses `u16be`
nested lengths while retaining the declared `u32be` counts and exact inner
CommandSpec fields. Both satisfy the prose, but their ProviderScopeInput and
ScopeAssignmentFingerprint differ; the worker rejects the parent's otherwise
identical request.

**Required correction.** Declare the complete binary grammar for every value
kind and Provider variant: element-length width, environment entry envelope,
name/value widths, count and size maxima, empty handling, sort keys, duplicate
rules, and trailing-byte rejection. Add a nonempty golden per Provider with
multiple commands, environment entries, read roots, empty raw values, and
non-UTF-8 path/argument bytes.

### CLEAN3-B06 — The checksummed release recovery envelope is not canonical

**Evidence.** UpgradeTransactionV1 is a cross-version recovery authority with a
domain-separated checksum over CanonicalJsonV1 bytes, but the artifact only
lists conceptual contents; it does not name the checksum domain, literal
top-level keys, key order, or complete nested variants (`SPINE:1354-1366`).
ReleaseRecoveryAttemptV1, ManagedConsumerUnitContractV1,
TimerInvocationAcceptanceV1, KnownGoodCandidateV1, KnownGoodReleaseV1, manifest
step records, and ReleaseEventV1 are likewise logical or partially ordered
schemas (`SPINE:1276-1295`, `1398-1478`, `1487-1510`, `1550-1575`).
ReleaseValidationAttemptV1 and FirstInstallAbsentV1 are locally exact, but they
do not totalize the containing envelope.

**Exact counterexample.** A release process persists a pending consumer
validation effect and crashes after a new recovery owner is published. Unit A
orders UpgradeTransaction fields exactly as the narrative list and uses a
domain token derived from the type name. Unit B uses repository declaration
order and a different version token. Both contain every required fact and use
CanonicalJsonV1, but the new binary rejects the old binary's checksum or parses
the same step/union differently. Recovery stops or performs a different
idempotent effect.

**Required correction.** Give UpgradeTransactionV1 and every nested persisted
release type exhaustive key names/order, union membership, scalar encodings,
sort order, stable reason/step vocabularies, checksum domain and preimage, and
unknown-version behavior. Freeze complete golden manifests at every crash cut,
including owner takeover, FirstInstallAbsentV1, commit decision, KnownGood
publication, ready admission, explicit rollback, and rollback-unavailable.

### CLEAN3-B07 — A forked child can outlive the parent while retaining the admission flock

**Evidence.** AD-23 uses an open-file-description `flock`, requires
`O_CLOEXEC`, and then requires every child to close the admission descriptor as
its first spawn file action. It asserts that no pre-exec failure, child
lifetime, exec, or reap may extend the shared or exclusive lease
(`SPINE:1242-1274`). The fixtures stall after the first close action
(`SPINE:604-611`), not in the earlier post-fork window.

Linux `fork()` inherits the parent's open file descriptions and its `flock`;
the lock is released only when every duplicate descriptor is closed. `O_CLOEXEC`
acts on successful exec, not between fork and the first child action. These are
the documented semantics of [fork(2)](https://man7.org/linux/man-pages/man2/fork.2.html),
[flock(2)](https://man7.org/linux/man-pages/man2/flock.2.html), and
[open(2)](https://man7.org/linux/man-pages/man2/open.2.html).

**Exact counterexample.** The exclusive release owner forks a validator or
`systemctl` child. The child is stopped after fork but before its first close
action, and the parent is killed. The stopped child still references the same
locked open file description, so a recovery owner cannot acquire the exclusive
lease. Unit A trusts the installed close action and expects immediate takeover;
Unit B observes the kernel lock and remains blocked. `FD_CLOEXEC` and the
post-exec audit cannot repair this pre-exec state.

**Required correction.** Use a spawn/locking design with no inherited
admission-lock window, such as an out-of-process spawn broker that never held
the lease, or replace `flock` with a precisely specified primitive whose lock is
not inherited by the selected spawn path. Otherwise weaken the no-child-lifetime
guarantee and define bounded stranded-child recovery. Add a fixture that stops
the child between process creation and its first file action, kills the owner,
and proves takeover without waiting for child exit.

### CLEAN3-B08 — FirstInstallAbsentV1 cannot represent absent prior consumers

**Evidence.** FirstInstallAbsentV1 may describe prior state as `absent` or
`restore-recorded`, but its only consumer disposition is `restore-recorded`
(`SPINE:1487-1501`). Automatic pre-decision recovery must restore recorded
consumer fragments and enablement, reload, and prove exact unit/timer
postconditions (`SPINE:1524-1535`). No variant records that a managed service or
timer did not exist before first install, nor does an empty record list declare
removal of newly installed consumers. The explicit sentinel rollback path is
separately exact and is not the defect (`SPINE:1537-1548`).

**Exact counterexample.** Start with no managed binary, link, service, or timer;
fail first install after writing and loading its consumer units but before
commit decision. Unit A treats an empty prior-contract list as authoritative
absence, removes the new units, reloads, and returns
`forward-failed-recovered`. Unit B follows `restore-recorded`, finds no prior
contract to restore or validate, and returns `upgrade-recovery-required` or
leaves the new units behind. Both preserve binary/link absence but expose
different Host truth.

**Required correction.** Make `consumer_disposition` an exact tagged
`absent | restore-recorded` union and record absence per managed service/timer
path and enablement target. Define ordered removal, reload, absence readbacks,
pending/complete crash recovery, and exact side effects for the absent variant.
Keep explicit rollback from a published FirstInstallAbsentV1 sentinel as the
existing no-mutation `rollback-unavailable` result.

### CLEAN3-H01 — Timer signal capture omits the manager-subscription handshake

**Evidence.** TimerInvocationAcceptanceV1 says it “subscribes race-free” to
JobNew, JobRemoved, and property changes before taking baselines
(`SPINE:1431-1438`), but it does not require D-Bus match installation,
successful `org.freedesktop.systemd1.Manager.Subscribe()`, their ordering, or
fail-closed handling of a manager bus-owner change. systemd documents that most
signals are emitted only after at least one client invokes `Subscribe()`; see
the [systemd v257 D-Bus specification](https://raw.githubusercontent.com/systemd/systemd/v257/man/org.freedesktop.systemd1.xml).

The later causal predicate is sound: exact `trigger_unit`, Job.Unit, JobType,
JobRemoved result, invocation, start, terminal result, and competing-activation
exclusions bind the timer to the service (`SPINE:1440-1472`). The gap is making
those signals race-free and available.

**Exact counterexample.** Unit A installs local match rules, reads baselines,
and triggers the timer without a successful manager Subscribe reply. The timer
runs, but required job signals need not be emitted, so it reaches the persisted
deadline and restores. Unit B installs match rules, receives Subscribe success,
then reads baselines and triggers; it accepts the same causal activation. The
same Host action yields recovery versus commit.

**Required correction.** Freeze this order: connect and bind the expected bus
owner, install all match rules, obtain successful Manager.Subscribe reply,
capture baselines, then trigger or await. Treat owner change, subscription loss,
or signal stream discontinuity as validation failure. Recovery must repeat the
full handshake before taking its fresh baselines.

### CLEAN3-H02 — The declared frozen compatibility and contract-golden corpora are absent

**Evidence.** AD-9 calls
`tests/compat/{capture-baseline.sh,fixtures,golden,compatibility-ledger.md}` a
checked-in frozen oracle (`SPINE:290-314`). AD-11 similarly names
`tests/fixtures/contracts` PolicySnapshot, CollectionPlan, ObservationId, and
IPC assertions (`SPINE:526-589`). Neither directory exists at the reviewed
commit. The only checked-in test is the opt-in, Host-dependent
`tests/test_smoke.sh`; it passed here with 293 live inventory items, but AD-9
explicitly forbids recaptured live truth as an assertion source.

**Exact counterexample.** Both units implement the same legacy semantic mapping
but differ on a hostile identifier, missing-PM2 stderr placement, or an empty
legacy output byte. Both also generate internally self-consistent contract
goldens from their own encoders. With no checked-in frozen input/output bytes,
neither corpus can reject the wrong implementation, and recapture would bless
the divergence.

**Required correction.** Before implementation starts, commit the named
compatibility and contract corpora, pin the exact Python source blob/hash from
which legacy fixtures were captured, declare every volatile substitution, and
store fixture provenance. Goldens must be fixed assertion inputs with hashes,
not generated or refreshed by the encoder under test.

## Historical Counterexample Replay Matrix

| Historical IDs | Clean-pass3 replay |
| --- | --- |
| `DVG-B01`, `DVG-H03` | **Closed.** One atomic plan freezes Promise projections, event sequences, policy, obligations, and the paired clocks (`SPINE:1116-1203`). |
| `DVG-B02`, `DVG-B03`, `DVG-H05`, `DVG-H06` | **Closed.** Snapshot plus Findings commit atomically; latest-only CAS, half-open admission, cancellation, and immutable reservations select one current truth (`SPINE:898-968`, `316-456`). |
| `DVG-B04`, `DVG-B05`, `DVG-H08`, `DVG-H09` | **Closed.** Durable ActionPlan/Operation handoff, launch receipt, sole coordinator, terminal CAS, and storage-failure recovery converge (`SPINE:856-875`, `1205-1228`). |
| `DVG-B06`, `DVG-H10`, `DVG-M01` | **Closed at the original policy probes.** PolicySnapshotV1 and materialized historical decisions are canonical (`SPINE:1589-1663`, `1842-1845`). |
| `DVG-B07`, `DVG-B08`, `DVG-H11` | **Original journal and backup cases closed.** Durable admission, effect journaling, and the typed backup contract select one recovery truth; CLEAN3-B06 and CLEAN3-B07 are distinct surviving release seams (`SPINE:1230-1396`). |
| `DVG-H01` | **Closed.** Repository event sequence and authoritative projection prevent replay drift (`SPINE:969-988`). |
| `DVG-H02` | **Closed.** ScopeIdV1 field tags, normalization, ordering, display, and equality converge (`SPINE:1813-1827`). |
| `DVG-H04`, `ACC-H02`, `NEW-H01`, `FINAL-B01` | **Closed at the original diagnostic seam.** Post-evidence candidate sorting, reference rewrite, exact-owner suppression, and the transport diagnostic matrix converge (`SPINE:709-755`, `1973-2053`). |
| `DVG-H07`, `NEW-H02`, `REALITY-B01` | **Closed.** OwnedSpawnV1, unrootable-child absence barriers, exact self roots/groups, and reducer-owned suppression converge (`SPINE:779-854`, `1953-1960`). |
| `ACC-B01`, `ACC-B02`, `ACC-H04`, `ACC-H05`, `ACC-M01`, `NEW-B01` | **Original frozen-cut cases closed.** Baseline, operation, history, paired time, and pointer cuts are atomic and embedded. CLEAN3-B03 is a nested-byte derivative (`SPINE:1122-1203`, `1690-1811`). |
| `ACC-B03`, `ACC-H06`, `ACC-H07`, `ACC-M02`, `NEW-B03`, `NEW-H04` | **Original release-order cases closed.** Recovery ownership, effect readback, KnownGood publication, event mapping, and commit decision converge (`SPINE:1242-1587`). |
| `ACC-B04`, `ACC-H01`, `ACC-H03` | **Original byte, scope, and deduplication probes closed.** CLEAN3-B02 through CLEAN3-B06 are narrower surviving byte streams (`SPINE:1602-1663`, `709-854`, `1813-1840`). |
| `NEW-B02`, `RERUN-B01` | **Original bounded-worker and transport-outcome probes closed.** CLEAN3-B02 and CLEAN3-B05 show the remaining nested schemas (`SPINE:1847-2169`). |
| `NEW-H03`, `RERUN-B02` | **Closed.** Attempt-bound FD4 authentication and replacement-owner publication converge (`SPINE:1276-1352`). |
| `FINAL-H01`, `FINALPASS-B01` | **Closed.** Frozen DispatchScheduleV1, held early-free slots, process placement, and one-nanosecond cutoff headroom converge (`SPINE:321-456`, `484-500`). |
| `CLEAN2-B01` | **Top-level repair closes; derivative remains.** PolicySnapshotV1 is exact, but CLEAN3-B03 leaves nested plan bytes open. |
| `CLEAN2-B02` | **Chosen scheduling behavior closes; derivative remains.** No child is created at or after a cut, but CLEAN3-B01 makes its required report unconstructible. |
| `CLEAN2-B03` | **Provider field-table repair closes; derivative remains.** Outer ObservationIdV1 converges, while CLEAN3-B04 leaves three inner hash preimages open. |
| `CLEAN2-B04` | **Explicit rollback closes; derivative remains.** `rollback-unavailable` is exact, while CLEAN3-B08 leaves automatic absent-consumer recovery open. |
| `CLEAN2-H01` | **Closed.** Every injected FD3 duplicate fails before Hello; only a clean descriptor lane reaches Result/EOF (`SPINE:575-589`, `1869-1889`). |
| `CLEAN2-H02` | **Closed semantically.** ActivationDetails `trigger_unit` and job/invocation evidence establish timer causality. CLEAN3-H01 is the preceding subscription gap (`SPINE:1431-1472`). |
| `CLEAN2-H03` | **Closed.** ARCH-LIM-24 and ReleaseValidationAttemptV1 define one persisted, equality-expired, recovery-attempt-bound cut (`SPINE:1093-1114`, `1297-1314`). |

## Schedule, Process-Gate, Diagnostic, State, Action, Release, and Compatibility Checks

| Family | Replayed result |
| --- | --- |
| Default schedule | Four workers, LPT epochs `0,15,20,25 s`, process gate `[25,35 s)`, makespan `35 s`, cutoff `40 s`: converged. |
| Near-tie schedule | Process plus three cron scopes at epoch `20 s`, makespan `30 s`, cutoff `35 s`: converged. |
| Zero-margin schedule | One `60 s` process plus seven `1 s` scopes produces makespan `61 s` and the mandatory one-nanosecond half-open cutoff headroom: converged. |
| Silent, early, and late lanes | Early completion never advances a reservation; deadline equality wins; expired members terminalize in epoch/worker order before live spawn: converged except CLEAN3-B01's diagnostic encoding. |
| Process gate | Non-process Ready dispatch is immediate; process waits only for same-epoch parent spawn outcomes and exact unrootable-child absence: converged. |
| Diagnostics | Candidate allocation, immutable evidence cuts, complete tuple sorting, reference rewrite, exact-owner suppression, and cleanup/reap exclusion: converged. |
| State | SQLite `wal`, numeric synchronous `2`, foreign keys `1`, atomic plan/Snapshot/Finding transactions, retention pins, and recovery owner truth: converged. |
| Actions | Exact target, immutable ActionPlan, capability/authorization, launch receipt, OperationId-correlated verification, one terminal owner, and storage-unavailable recovery: converged. |
| Release | Toolchain refresh, ABI proof, FD4 attempt binding, whole-pair effects, KnownGood boundary, ActivationDetails causality, deadline recovery, and explicit rollback-unavailable: converged at their original probes; CLEAN3-B06 through CLEAN3-H01 remain. |
| Compatibility | Merge order, legacy surface ownership, hostile identifiers, output lanes, and ledger discipline are exact in prose. Executable replay remains blocked by CLEAN3-H02. |

## Currentness and Mechanical Validation

The reviewed Rust target remains current: the official
[Rust 1.97.1 announcement](https://blog.rust-lang.org/2026/07/16/Rust-1.97.1/)
confirms the point release. The host currently reports systemd `257.9`, glibc
`2.42`, Python `3.14.4`, and local Rust `1.95.0`; AD-12's mandatory fresh
toolchain-manifest check correctly prevents the stale local compiler from
silently satisfying release evidence. systemd's documented `trigger_unit`
ActivationDetails semantics support the repaired causal predicate; the missing
Subscribe handshake is CLEAN3-H01, not a rejection of that predicate.

| Check | Result |
| --- | --- |
| Exact base commit and clean starting tree | PASS: `db70e84c74a301d6e698cddf0c88fb47e78da851` |
| Architecture spine lint | PASS: zero findings |
| Legacy live smoke | PASS: JSON 293 items, Prometheus 15 samples, Markdown, table, real cron inspect, and hostile-name injection cases |
| Canonical Markdown lint for this report | PASS |
| `git diff --check` and staged diff check | PASS |
| AD identifier sequence and uniqueness | PASS: AD-1 through AD-25, one defining heading each |
| ARCH-LIM identifier sequence and uniqueness | PASS: ARCH-LIM-1 through ARCH-LIM-24, one defining row each |
| Review finding identifier uniqueness | PASS: ten distinct defining headings |
| Frozen spine and memlog hashes after review | PASS: unchanged |
| Changed-path and staged-path isolation | PASS: only this report |

## Final Gate

Clean pass 3 requires exact convergence and zero findings. The independent
units converge on the repaired high-level control flow but diverge on eight
load-bearing identity, IPC, plan, admission, and release contracts; two further
verification gaps remain. The verdict is therefore **CHANGES REQUIRED**.

Correct the normative contracts and check in the frozen oracles, then rerun two
fresh isolated units against the resulting commit. Prior reports, private codec
conventions, self-generated goldens, and this report are not substitutes for
that rerun.
