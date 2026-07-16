---
title: "Final Technology Remediation Gate - srvls Architecture"
document_type: architecture_review
review_dimension: technology_remediation_final
status: final
verdict: "APPROVED"
blocking: false
reviewed_head: d4515067af8314cadf979da7b17921fbafc92d21
reviewed_spine_sha256: 66e90f988cc607c1b90b2bb841ca6b1cdd7f7bdf49ccd74920a7e65916df436d
reviewed_state: frozen working-tree remediation
review_date: 2026-07-16
reviewer: Professor Fiddlesticks
team: Team Argus
evidence_mode: accepted-research-final-reality-gate
scope: final technology, worker transport, scheduling, process ownership, and release recovery closure
finding_count: 0
blocking_findings: 0
---

<!-- markdownlint-disable MD013 MD025 -->

# Final Technology Remediation Gate

## Verdict

**APPROVED.** The exact 1,535-line spine with SHA-256
`66e90f988cc607c1b90b2bb841ca6b1cdd7f7bdf49ccd74920a7e65916df436d`
literally closes `TRR-B01`, `TRR-B02`, and `TRR-H01` from the prior technology
rerun. No technology/reality finding remains.

The revised rules now force every worker transport failure into one existing
AD-5 report and outcome; simulate the actual one-shot process-worker spawn
barrier before accepting a generation cutoff; conservatively own Provider
children and escaped descendants; and bind crash-resumed FD4 validation to a
durably published current recovery attempt rather than a dead original owner.

The previously accepted SQLite, ABI, managed systemd consumer, atomic release
journal, KnownGood, rollback, and release-event contracts remain intact. The
spine correctly remains `status: draft`; this report does not finalize it.

This review writes only this new report. It does not amend the spine, memlog,
canonical product or UX artifacts, product code, `tasks.md`, or any prior
review.

## Review Basis

Citation keys:

- `SPINE` —
  `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md`
- `PRIOR` —
  `reviews/review-technology-remediation-rerun-2026-07-16.md`
- `TECH-CURRENCY` — `reviews/review-technology-currency-2026-07-16.md`
- `TECH-ACCEPT` — `reviews/review-technology-acceptance-2026-07-16.md`

The current SPINE and PRIOR were read completely. The current target was read
from line 1 through line 1,535 and rehashed before and after review. The
completed same-day research and acceptance record remains the technology
currency basis; this is a fresh semantic gate, not a new dependency survey.

Repository reality still has no product `Cargo.toml`, `Cargo.lock`, or release
artifact. The approval therefore means the architecture assigns complete,
acceptance-testable proof. It does not claim implementation evidence already
exists. `readelf` and the configured Markdown linter are present on the review
Host.

The gate used the prior literal standard: a story cannot choose a different
report, outcome, schedule, self-process set, active release owner, FD4 peer, or
crash result while still satisfying the Rule. Fixtures support the production
contract; they are not treated as substitutes for it.

## Prior-Finding Closure

### TRR-B01 - Worker transport failure terminalization

**CLOSED.** AD-5 retains exactly six Collector outcomes and now explicitly
requires every AD-25 transport, authentication, framing, schema, identity,
abnormal-exit, and pre-deadline size failure to become a coordinator-synthesized
`invalid-output` CollectorReportV1, never a seventh outcome or missing report
(`SPINE:149-165`).

AD-25 makes that report constructible for the complete lifecycle
(`SPINE:1233-1266`):

- worker spawn and process-group setup;
- pre-request encoding and request-size rejection;
- post-dispatch FD and peer authentication, framing, schema, version, identity,
  capability, assignment, and result-size failure;
- valid protocol-error and worker-error frames;
- worker exits 64, 70, and 77, plus abnormal exit or signal; and
- deadline equality or later, which uses the existing `timed-out` report rather
  than `invalid-output`.

Every pre-deadline synthesized report has the frozen generation, scope, and
obligation, zero Observations and trusted capture bytes, exact zero-or-elapsed
duration, one stable WorkerTransportFailureV1 diagnostic, and no partial result
fields. AD-5 completeness, current-pointer, Brief, baseline, required/optional,
strict, and non-strict behavior then applies without a special transport lane.
AD-11 tests the complete persisted report and public result at exact and
one-byte-over boundaries (`SPINE:400-407`).

No setup, pre-request, or post-dispatch path remains without one canonical
scope report.

### TRR-H01 - Barrier-aware scheduling and process descendants

**CLOSED.** AD-10 now defines one event-by-event algorithm for runtime and
configuration admission. It uses one-shot workers in LPT order, includes queue
and closed-gate time, prevents successor spawn while the process Host-read cut
is open, and simulates each scope at its full configured deadline before
accepting the cutoff (`SPINE:321-340`).

The arithmetic is consistent:

- the default `[30,20,15,15,10,10,10,10]` schedule keeps its exact
  barrier-aware 35-second makespan because process is the final equal-deadline
  dispatch; the 5-second margin yields the configured 40 seconds; and
- four workers with one 60-second process scope, seven 1-second scopes, zero
  margin, and cutoff 60 are rejected because the closed gate leaves completed
  slots idle and raises the exact makespan to 61 seconds
  (`SPINE:817-824`).

The process-ownership side is also technologically coherent. Each worker is a
dedicated process-group leader before FD3 authentication; Provider children
inherit that group; every possibly live frozen group is carried into the
process assignment; exact PID/birth members of those groups are materialized;
and the report echoes the roots and sorted members (`SPINE:532-562`). A child
or grandchild that escapes the group is deliberately emitted as Host truth
unless independent Provider ownership evidence suppresses it. It is never
hidden merely by ancestry. Deadline and cancellation terminate the dedicated
group, while escaped work receives conservative observation rather than false
self-suppression (`SPINE:1333-1345`).

AD-11 covers the 60/1 counterexample, process in every LPT position,
near-deadline reads, in-group children and grandchildren, and escaped-group
emission (`SPINE:388-407`). Runtime scheduling, admission validation, process
suppression, and termination therefore share one rule.

### TRR-B02 - Crash-resumed FD4 owner binding

**CLOSED.** UpgradeTransactionV1 now distinguishes the immutable original
owner from an ordered, gap-free `ReleaseRecoveryAttemptV1` chain. A replacement
process can publish the next active attempt only while holding the exclusive
admission-lock capability. Publication checks the prior PID, BootIdentity,
birth, executable identity, predecessor checksum, and sequence, treats PID
reuse as evidence rather than identity, atomically replaces and reads back the
manifest, and allows no recovery effect before that readback
(`SPINE:956-975`). A crash before publication retains the prior authority; a
crash after publication lets the next exclusive owner append another attempt.

FD4 then authenticates the candidate's peer PID, birth, and executable against
the manifest's **active** attempt. Request and result both bind the attempt UUID
and sequence plus exact manifest revision and checksum; capability use is
single-attempt and old sockets or requests fail closed (`SPINE:977-1008`).
Pending candidate validation reruns only after the current attempt is durable
and uses a fresh attempt-bound exchange (`SPINE:1038-1045`). Every resumed
branch repeats the active-attempt publication/readback gate, and release events
retain that attempt identity (`SPINE:1075-1118`).

The original crash interleaving is therefore total: process B does not compare
itself with dead process A; it atomically becomes active recovery attempt B
under the exclusive lock, and the candidate validates B plus the exact current
manifest. Old-PID reuse, forged publication, and a second recovery-owner crash
have explicit refusal or continuation behavior and named fixtures
(`SPINE:408-417`).

## Retained Technology and Release Gate

| Required seam | Result | Binding evidence |
| --- | --- | --- |
| Fresh and existing SQLite initialization | **PASS** | Outside a transaction set WAL and require returned `wal`; every connection then reads WAL, sets FULL and reads numeric `2`, enables foreign keys and reads `1`, and sets busy timeout before any transaction; writers then use `BEGIN IMMEDIATE` (`SPINE:627-640`). |
| Exact release ABI floor | **PASS** | Release CI runs `readelf --version-info` on the final artifact, fails above `GLIBC_2.42`, and smokes that same artifact in the pinned oldest-supported glibc 2.42 runtime (`SPINE:431-440`). |
| Managed absolute `ExecStart` migration | **PASS** | Every managed path, expressly `srvls-metrics.service` and `srvls-snapshot.service`, is rewritten; loaded path, timer-trigger advancement, `Result=success`, and `ExecMainStatus=0` are read back; failure restores and proves the whole pair (`SPINE:444-456`, `SPINE:1047-1057`). |
| Atomic plan admission and bounded FD3 assignment | **PASS** | One `BEGIN IMMEDIATE` plan admission freezes every reconciliation cut; workers receive only the canonical scope assignment and echo plan and assignment fingerprints. Framing, caps, streams, exits, timeout, signal, and no-discovery behavior remain fixed (`SPINE:830-901`, `SPINE:1217-1349`). |
| Diagnostic and ownership grammar | **PASS** | Per-scope diagnostic allocation, tagged subject and parameter bytes, candidate references, post-evidence rewrite, exact ownership evidence, winner order, conflict retention, and self suppression remain deterministic (`SPINE:459-578`). |
| Crash-persistent release admission | **PASS** | Every ordinary stateful entry holds shared admission and refuses before SQLite unless ready; only release holds exclusive recovery ownership (`SPINE:940-954`). |
| Atomic UpgradeTransaction journal | **PASS** | Checksummed no-follow temporary write, file fsync, atomic rename, directory fsync, pending-before-effect, complete-after-readback, and may-have-executed recovery remain binding (`SPINE:1010-1045`). |
| KnownGood and explicit rollback | **PASS** | `commit-decided` is irreversible; KnownGood publication/readback precedes ready; post-decision recovery finishes forward; exactly one record remains; rollback is a new transaction (`SPINE:1059-1091`). |
| Durable release events | **PASS** | Events carry the active attempt, every internal step maps to one public and UX phase, pending/running/passed/failed/skipped projections are exact, and final machine results remain exhaustive (`SPINE:1093-1128`). |

No previously accepted technology choice moved into Deferred or became a
non-testable aspiration.

## Validation Record

| Validation | Command or method | Result |
| --- | --- | --- |
| Frozen target identity | `git rev-parse HEAD`; `sha256sum <SPINE>` before and after review | **PASS** - head `d4515067af8314cadf979da7b17921fbafc92d21`; exact required SHA-256 retained. |
| Required complete reads | Line-bounded reads through EOF for the 1,535-line SPINE and complete PRIOR | **PASS** - all three prior interleavings reconstructed against current rules. |
| Accepted reality evidence | TECH-CURRENCY and TECH-ACCEPT disposition retained from the same-day gate | **PASS** - no absent product artifact presented as current proof. |
| Architecture linter | `uv run .agents/skills/bmad-architecture/scripts/lint_spine.py --workspace _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14` | **PASS** - `ok: true`; zero findings. |
| AD integrity | Ordered heading extraction | **PASS** - AD-1 through AD-25 exactly once; original AD-1 through AD-24 remain unrenumbered. |
| ARCH-LIM integrity | Ordered table-definition extraction | **PASS** - ARCH-LIM-1 through ARCH-LIM-23 exactly once. |
| Required-term inspection | Exact `rg -n` sweep for synthesized reports, barrier-aware scheduling, process groups, recovery attempts, SQLite, ABI, managed services, commit decision, KnownGood, and release events | **PASS** - every term lands in an enforceable Rule and was inspected semantically. |
| Final technology/reality gate | Transport lifecycle, 60/1 event simulation, default schedule, descendant handling, PID reuse, second crash, and FD4 current-attempt interleavings | **PASS** - zero findings. |
| Markdown lint | `markdownlint-cli2` with the canonical UX lint profile against this report | **PASS** - one file; zero errors. |
| Whitespace/error check | `git diff --check` | **PASS** - no output. |
| Changed-file scope | Target-path presence and `git status --short` | **PASS** - this reviewer added only this new final report; shared remediation artifacts were already present. |

The deterministic linter and semantic reality gate agree on this frozen hash.

## Final Gate Status

**APPROVED. Blocking status: CLEAR for technology and release architecture.**
`TRR-B01`, `TRR-B02`, and `TRR-H01` are closed without weakening any accepted
contract. Any later semantic change to AD-5, AD-10 through AD-13, AD-16,
AD-20, AD-23, AD-25, the Stack, or Deferred requires a new technology gate.
