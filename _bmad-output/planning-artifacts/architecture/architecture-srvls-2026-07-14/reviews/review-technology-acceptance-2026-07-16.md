---
title: "Technology Remediation Acceptance Review - srvls Architecture"
document_type: architecture_review
review_dimension: technology_acceptance
status: final
verdict: "CHANGES REQUIRED"
blocking: true
reviewed_commit: b917bcc89b5e386789cd0d0e8dfd01ce0cd42d0f
review_date: 2026-07-16
reviewer: WidgetWhisperer
team: Team Argus
evidence_mode: completed_research_acceptance
scope: technology remediation closure and downstream story assignability
---

<!-- markdownlint-disable MD025 -->

# Technology Remediation Acceptance Review

## Verdict

**CHANGES REQUIRED.** The remediation at
`b917bcc89b5e386789cd0d0e8dfd01ce0cd42d0f` closes most of the technology
currency gate. Rust 2024 with resolver 3, MSRV 1.88 and current-stable locked
lanes, the remediated bundled SQLite graph, TOML crate/spec separation,
Linux `CLOCK_BOOTTIME`, deterministic strsim correlation, one-binary delivery,
explicit systemd action limits, and bootstrap-before-Provider sequencing are
now explicit and assignable.

Three dispositions remain insufficiently binding for downstream stories:

1. Tier 0 does not positively require managed absolute-path unit consumers to
   be rewritten to the canonical installed binary or require successful
   timer-triggered execution after the rewrite.
2. Tier 1 does not state the complete SQLite pragma initialization sequence and
   required readbacks for `journal_mode=WAL` and `synchronous=FULL`.
3. Tier 2 chooses glibc 2.42 and a pinned build image but does not name the
   required `readelf` failure gate or a smoke run on the oldest supported
   glibc 2.42 runtime.

Because the first gap leaves a prior release blocker open, the technology
remediation is not accepted yet.

## Review Basis

Citation keys:

- `SPINE` —
  `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md`
- `CURRENCY` —
  `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/reviews/review-technology-currency-2026-07-16.md`

Both artifacts were read completely. The remediation delta from the prior
reviewed commit `799fc092f5d35149e082cce7efab2f6f2a189c99` to the acceptance
commit was inspected. This is acceptance of completed research, not a new
currency survey. The completed graph probes and official-source conclusions in
`CURRENCY:71-124` and `CURRENCY:234-251` are accepted as evidence; no graph
probe was rerun and no disposable probe directory was created.

The acceptance test is the prior approval gate: both Tier 0 remediations must
be present, every Tier 1 semantic must be explicit, and Tier 2 proof must be
assigned to acceptance-testable work (`CURRENCY:253-257`). Token presence alone
does not close a claim when a conforming story could still choose incompatible
behavior.

## Claim Closure Matrix

| ID | Prior gate | Result | Acceptance evidence |
| --- | --- | --- | --- |
| C01 | T2.1 | **CLOSED** | Rust 2024 and explicit resolver 3 are required by AD-12, with the boundary gate placed in bootstrap CI (`SPINE:374-380`, `SPINE:81-83`). |
| C02 | T0.1 / T2.1 | **CLOSED** | MSRV 1.88 is retained and must run locked all-target tests alongside stable (`SPINE:374-380`, `SPINE:799-800`). |
| C03 | T0.1 | **CLOSED** | The lock target is `rusqlite = "=0.39.0"` selecting `libsqlite3-sys 0.37.0` and SQLite 3.51.3 (`SPINE:794-805`). |
| C04 | T0.1 / T2.1 | **CLOSED** | Prior 1.95/1.97 compile evidence remains evidence rather than MSRV proof; AD-12 makes current stable a locked CI lane (`CURRENCY:101-124`, `SPINE:374-380`). |
| C05 | T2.2 | **CLOSED** | `x86_64-unknown-linux-gnu` is the named release target (`SPINE:374-380`). |
| C06 | T2.2 | **CLOSED AS A CHOICE** | The spine no longer treats host glibc as incidental proof: v1 deliberately supports x86_64 glibc 2.42 and defers broader portability (`SPINE:374-380`, `SPINE:927-938`). Enforcement remains open under C14. |
| C07 | T0.1 / T2.1 | **CLOSED** | The Stack records reviewed lock targets, while committed `Cargo.lock` and locked CI own resolution (`SPINE:792-814`). |
| C08 | T0.1 | **CLOSED** | The incompatible rusqlite 0.40.1 choice is replaced by the exact 0.39.0 chain (`SPINE:805`). |
| C09 | T1.1 | **CLOSED** | Cargo syntax is `toml = "=1.1.3"`; TOML specification 1.1.0 is separate metadata (`SPINE:806`). |
| C10 | T1.3 | **CLOSED** | The durable-state adapter owns one bundled SQLite database, and the Stack pins the embedded library chain through SQLite 3.51.3 (`SPINE:461-473`, `SPINE:805`). |
| C11 | T1.3 | **PARTIAL** | WAL, FULL, foreign keys, and `BEGIN IMMEDIATE` are named, but their complete initialization order and readbacks are not (`SPINE:467-474`). See T1-A. |
| C12 | T1.3 | **OPEN** | `synchronous=FULL` is annotated as value `2`, but no rule requires reading the effective value back and failing unless it equals `2` (`SPINE:470-473`). See T1-A. |
| C13 | T2.1 / T2.2 | **CLOSED** | AD-12 requires one Rust binary crate, one versioned binary in the release tarball, its SHA-256, and release-asset smoke (`SPINE:369-393`). |
| C14 | T2.2 | **OPEN** | glibc 2.42 and a pinned glibc-2.42 build image are explicit, but the `readelf` threshold gate and oldest-runtime smoke are not (`SPINE:374-381`). See T2-A. |
| C15 | systemd policy | **CLOSED** | systemd action execution is explicitly 100 seconds by default, configurable from 5 to 600 seconds, and included in the derived 143-second decision bound (`SPINE:625-649`). |
| C16 | T1.2 | **CLOSED** | Same-boot Lease and cadence decisions use suspend-inclusive Linux `CLOCK_BOOTTIME`; the Stack pins `libc 0.2.186` and the Linux clock adapter is assigned (`SPINE:526-545`, `SPINE:812`, `SPINE:854`). |
| C17 | T0.2 | **PARTIAL** | Preflight inventories shell resolution and every absolute `ExecStart`; managed and foreign dispositions exist, but a positive canonical-path rewrite postcondition is absent (`SPINE:381-391`, `SPINE:735-737`). See T0-A. |
| C18 | T0.2 | **PARTIAL** | The known broken unit target is retained as prior evidence and named consumer checks are required, but the two affected managed services are not bound to a corrected `ExecStart` (`CURRENCY:126-152`, `SPINE:384-391`). See T0-A. |
| C19 | T0.2 | **PARTIAL** | AD-12 reruns timers and named consumer checks, but does not explicitly require a timer-triggered execution from each rewritten unit with successful exit status (`SPINE:388-392`). See T0-A. |
| C20 | T2.1 | **CLOSED** | Bootstrap CI must create the boundary gate before any Provider implementation; AD-12 assigns the crate, lockfile, MSRV/stable lanes, and release proof to the bootstrap story (`SPINE:76-83`, `SPINE:369-381`). |

## Tiered Findings

### T0-A — Managed unit rewrite and timer success are not postconditions

The prior remediation requires discovery of every bypass, explicit consumer
classification, rewrite of `srvls-metrics.service` and
`srvls-snapshot.service` to the canonical installed binary, user-manager
daemon reload, loaded-definition verification, and a successful
timer-triggered run from each rewritten unit (`CURRENCY:126-152`).

AD-12 now inventories every absolute consumer and unit `ExecStart`, requires a
foreign-bypass disposition, stages and activates managed unit definitions,
daemon-reloads, validates, and restores definitions and daemon state on failure
(`SPINE:381-392`). AD-23 also makes managed definitions and daemon-reload state
part of one recovery result (`SPINE:707-737`). Those are substantial closures.

The remaining gap is the positive postcondition. No rule says a managed
absolute `ExecStart` must be rewritten to the canonical activated binary. No
rule names the two known managed services as required migrations. "Reruns ...
timers" does not explicitly mean a timer-triggered service execution whose exit
status must succeed. A story could stage the existing definition, daemon-reload
it, perform a generic read-only check, and still satisfy the literal rule while
retaining the broken bypass.

Closure requires acceptance-testable wording that:

- rewrites every managed absolute `ExecStart`, including both known user
  services, to the canonical activated binary;
- verifies the loaded `ExecStart` and executable target after
  `systemctl --user daemon-reload`;
- proves one successful timer-triggered execution and successful exit status
  for each rewritten unit; and
- restores binary, link, unit/timer definitions, enablement, application state,
  and daemon state together on any failed check.

### T1-A — SQLite pragma ordering and readback remain incomplete

The prior requirement is ordered and observable: establish and verify WAL
during controlled initialization; set `synchronous=FULL` and read back numeric
`2`; set `foreign_keys=ON` before every transaction and read back `1`; only then
enter write-critical work with `BEGIN IMMEDIATE`; integration-test the sequence
on fresh and existing databases (`CURRENCY:176-194`).

AD-16 explicitly verifies `foreign_keys=ON` as `1` before transactions and
names WAL, FULL as `2`, the busy timeout, and `BEGIN IMMEDIATE`
(`SPINE:461-474`). It does not explicitly require WAL readback, FULL readback,
failure on mismatched effective values, controlled-initialization ownership for
WAL, or the complete ordered sequence before `BEGIN IMMEDIATE`.

Closure requires one ordered adapter rule and fresh/existing-database fixture
that fail closed unless `journal_mode` reads back `wal`, `synchronous` reads
back `2`, and `foreign_keys` reads back `1` before any write transaction begins.

### T2-A — The glibc support choice lacks its named ABI gate

The support decision itself is closed: v1 is intentionally limited to
x86_64 glibc 2.42, the build image is pinned to glibc 2.42, and broader
portability is deferred (`SPINE:374-380`, `SPINE:927-938`).

The proof rule is not yet story-assignable. "Verify symbol versions" does not
name `readelf`, define the maximum permitted import, state that CI fails above
the floor, or require a runtime smoke test on the oldest supported image. The
prior disposition requires all four (`CURRENCY:211-223`).

Closure requires release CI to inspect the final binary with `readelf`, fail if
any imported `GLIBC_*` symbol exceeds `GLIBC_2.42`, and smoke-test that exact
release artifact in a pinned glibc 2.42 runtime image.

## Closed Disposition Summary

No further findings remain for these requested surfaces:

- Rust edition 2024, Cargo resolver 3, MSRV 1.88, current-stable, committed
  lockfile, and locked all-target/release lanes;
- `rusqlite = "=0.39.0"` to `libsqlite3-sys 0.37.0` and bundled SQLite
  3.51.3;
- `toml = "=1.1.3"` separated from TOML specification 1.1.0;
- `libc 0.2.186`, suspend-inclusive Linux `CLOCK_BOOTTIME`, and an injectable
  clock boundary;
- strsim 0.11.1 Jaro-Winkler over the AD-4 normalized name, a 256-scalar cap,
  and the inclusive `>= 0.94` threshold;
- one Rust binary crate and one versioned release binary;
- explicit systemd execution and total-decision limits; and
- bootstrap CI and the dependency-boundary gate before Provider work.

## Validation Record

| Validation | Command or method | Result |
| --- | --- | --- |
| Reviewed commit | `git rev-parse --verify HEAD` | **PASS** — `b917bcc89b5e386789cd0d0e8dfd01ce0cd42d0f` |
| Required inputs | Complete line-numbered reads of `SPINE` and `CURRENCY` | **PASS** — 947 and 259 lines |
| Remediation delta | `git diff --unified=80 799fc092... b917bcc... -- ARCHITECTURE-SPINE.md` plus full-spine term search | **PASS** — all requested surfaces traced; three semantic gaps recorded above |
| Dependency graph evidence | Completed compile and release probes in `CURRENCY` | **ACCEPTED** — no graph probe rerun |
| Architecture linter | `python3 .agents/skills/bmad-architecture/scripts/lint_spine.py --workspace <architecture-folder>` | **PASS** — `ok: true`; zero findings |
| One-file Markdown lint | `markdownlint-cli2 --config <UX profile> <this report>` | **PASS** — one file; zero errors |
| Whitespace/error check | `git diff --check` | **PASS** — no output |
| Changed-file scope | `git status --short` and staged-name inspection | **PASS** — only this report |

## Final Acceptance Status

**BLOCKED. Verdict: CHANGES REQUIRED.** The report is final. A focused
documentation remediation for T0-A, T1-A, and T2-A followed by independent
re-review is required; no new broad technology research is needed.
