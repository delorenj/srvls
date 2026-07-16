---
title: "Technology Remediation Gate - srvls Architecture"
document_type: architecture_review
review_dimension: technology_remediation_gate
status: final
verdict: "APPROVED"
blocking: false
reviewed_head: d4515067af8314cadf979da7b17921fbafc92d21
reviewed_spine_sha256: d9128bcc347f553045198a5402f0b91f068013728460de64c6105ec3d57429b2
reviewed_state: frozen working-tree remediation
review_date: 2026-07-16
reviewer: Professor Fiddlesticks
team: Team Argus
evidence_mode: accepted-research-remediation-gate
scope: technology and release decision closure and downstream story assignability
---

<!-- markdownlint-disable MD013 MD025 -->

# Technology Remediation Gate

## Verdict

**APPROVED.** The frozen working-tree spine with SHA-256
`d9128bcc347f553045198a5402f0b91f068013728460de64c6105ec3d57429b2`
closes `T0-A`, `T1-A`, and `T2-A` from the immutable technology acceptance
report. The SQLite initialization sequence, glibc artifact proof, and deployed
systemd consumer migration are each explicit enough to assign to an
implementation story without allowing a second conforming story to choose a
weaker proof.

No previously accepted technology contract regressed. Rust 2024, Cargo
resolver 3, MSRV 1.88 plus current-stable locked lanes, the remediated bundled
SQLite graph, TOML crate/spec separation, Linux `CLOCK_BOOTTIME`, bounded
strsim correlation, one-binary delivery, explicit systemd action limits, and
bootstrap-before-Provider sequencing remain binding.

This is acceptance of the completed 2026-07-16 research record, not a new
currency survey. The prior acceptance report expressly accepts the completed
graph probes and official-source conclusions as evidence
(`review-technology-acceptance-2026-07-16.md:53-64`). No product
`Cargo.toml`, `Cargo.lock`, or release artifact exists in the reviewed tree;
the spine correctly assigns those proofs to bootstrap and release stories
instead of asserting that implementation evidence already exists.

## Review Basis

Citation keys:

- `SPINE` —
  `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md`
- `MEMLOG` —
  `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/.memlog.md`
- `TECH-ACCEPT` —
  `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/reviews/review-technology-acceptance-2026-07-16.md`
- `TECH-CURRENCY` —
  `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/reviews/review-technology-currency-2026-07-16.md`
- `DIVERGENCE-ACCEPT` —
  `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/reviews/review-two-unit-divergence-acceptance-2026-07-16.md`
- `RUBRIC-ACCEPT` —
  `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/reviews/review-rubric-acceptance-2026-07-16.md`
- `PRD` —
  `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md`
- `ADDENDUM` —
  `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/addendum.md`
- `DESIGN` —
  `_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/DESIGN.md`
- `EXPERIENCE` —
  `_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md`

The complete current `SPINE`, complete `MEMLOG`, canonical PRD and addendum,
canonical `DESIGN` and `EXPERIENCE`, all three immutable acceptance reports,
and the accepted technology-currency evidence were read. The acceptance
standard was not weakened: both Tier 0 remediations must be explicit, every
Tier 1 semantic must be ordered and observable, and Tier 2 proof must be
acceptance-testable work rather than an architectural aspiration
(`TECH-ACCEPT:60-64`).

## Required Gate Closure

### T1-A — Ordered SQLite initialization and readback

**CLOSED.** AD-16 defines one fail-closed sequence on both fresh and existing
databases (`SPINE:515-527`):

1. Outside a transaction, set `PRAGMA journal_mode=WAL` and require returned
   value `wal`.
2. On every opened connection, read `journal_mode` and require `wal`.
3. Set `PRAGMA synchronous=FULL` and require numeric readback `2`.
4. Set `PRAGMA foreign_keys=ON` and require readback `1`.
5. Set the typed busy timeout.
6. Permit no read or write transaction after any missing, mistyped, or
   mismatched readback.
7. Only then allow writers to use `BEGIN IMMEDIATE`.

AD-11 assigns fresh- and existing-database readback fixtures
(`SPINE:377-379`). A SQLite adapter story can therefore implement one exact
order, exact values, fail-closed result, and two required integration cases.
This closes prior claims `C11` and `C12` without weakening bundled SQLite
ownership.

### T2-A — glibc support-floor proof

**CLOSED.** AD-12 keeps the deliberate `x86_64-unknown-linux-gnu` and glibc
2.42 v1 support choice, then requires release CI to:

- build in a pinned glibc 2.42 image;
- run `readelf --version-info` on the exact final artifact;
- fail when any imported `GLIBC_*` version exceeds `GLIBC_2.42`; and
- smoke that same artifact in the pinned oldest-supported glibc 2.42 runtime
  image (`SPINE:393-403`).

AD-11 separately assigns exact-artifact ABI proof to release fixtures
(`SPINE:382-385`). Broader portability remains explicitly Deferred, so a
release story cannot silently substitute a newer runtime or treat a sample Host
build as floor proof (`SPINE:1166-1167`). This closes prior claim `C14`.

### T0-A — Managed absolute-path consumers and timer success

**CLOSED.** AD-12 and AD-23 jointly require the complete migration
postcondition:

- preflight inventories the shell-resolved command and every managed or
  foreign absolute consumer, while every foreign bypass receives an explicit
  disposition (`SPINE:403-409`, `SPINE:858-859`);
- every managed absolute `ExecStart`, expressly including
  `srvls-metrics.service` and `srvls-snapshot.service`, is staged to the
  canonical activated binary with matching state, timer definition, and
  enablement (`SPINE:409-412`);
- after `systemctl --user daemon-reload`, validation reads back every loaded
  `ExecStart` (`SPINE:412-413`);
- validation proves one activation originating through each paired timer,
  observes timer-trigger advancement, and requires service `Result=success`
  plus `ExecMainStatus=0` (`SPINE:413-415`, `SPINE:849-855`); and
- any failure restores and revalidates binary/link, matching database,
  service/timer definitions and enablement, and daemon state as one whole pair
  (`SPINE:415-417`, `SPINE:856-858`).

AD-11 assigns every managed rewrite, loaded readback, paired timer-triggered
success, and whole-pair rollback fixture (`SPINE:382-385`). The explicit
`KnownGoodReleaseV1` contract retains the prior pair after successful
validation, and `release rollback` starts a new upgrade transaction rather
than performing a binary-only repoint (`SPINE:861-869`). This closes prior
claims `C17`, `C18`, and `C19` and preserves FR-43/UJ-6 recovery semantics.

## Previously Closed Technology Contracts

| Prior claims | Current disposition | Binding evidence |
| --- | --- | --- |
| C01-C02, C04-C05, C20 | **REMAIN CLOSED** | Rust 2024, MSRV 1.88, resolver 3, `x86_64-unknown-linux-gnu`, locked MSRV/current-stable lanes, and bootstrap-before-Provider enforcement remain explicit (`SPINE:75-87`, `SPINE:388-403`). |
| C03, C07-C08 | **REMAIN CLOSED** | The reviewed lock target remains `rusqlite = "=0.39.0"`, `libsqlite3-sys 0.37.0`, and bundled SQLite 3.51.3; committed `Cargo.lock` and locked CI own resolution (`SPINE:1022-1034`). |
| C06 | **REMAINS CLOSED AS THE V1 CHOICE** | glibc 2.42 is deliberate and enforced, while broader portability remains Deferred (`SPINE:393-403`, `SPINE:1166-1167`). |
| C09 | **REMAINS CLOSED** | Cargo uses `toml = "=1.1.3"`; TOML specification 1.1.0 remains separate metadata (`SPINE:1033-1034`). |
| C10 | **REMAINS CLOSED** | AD-16 retains one bundled SQLite durable-state owner, and the Stack retains the embedded chain (`SPINE:510-527`, `SPINE:1033`). |
| C13 | **REMAINS CLOSED** | One Rust binary crate, one versioned release binary, its SHA-256, and release smoke remain mandatory (`SPINE:393-405`). |
| C15 | **REMAINS CLOSED** | systemd execution remains 100 seconds by default, valid from 5 to 600 seconds, within the derived 143-second decision bound (`SPINE:691-703`). |
| C16 | **REMAINS CLOSED** | Lease and cadence use suspend-inclusive Linux `CLOCK_BOOTTIME`; `libc 0.2.186` remains pinned (`SPINE:585-599`, `SPINE:1040`). |

No accepted technology claim was weakened, renamed into Deferred, or changed
from a required proof into seed text.

## Story Assignability

| Story boundary | Required acceptance evidence now fixed by the spine |
| --- | --- |
| Bootstrap crate and CI | Rust 2024/resolver 3, committed lockfile, exact dependency graph, MSRV 1.88 plus stable locked lanes, architecture boundary test before Provider work. |
| SQLite state adapter | Fresh and existing database sequence; WAL/FULL/FK typed readbacks; fail closed before any transaction; busy timeout; `BEGIN IMMEDIATE`. |
| Release artifact CI | Exact final artifact, `readelf --version-info`, maximum `GLIBC_2.42`, same-artifact oldest-runtime smoke. |
| Managed consumer migration | Inventory and disposition, both named services, canonical loaded path, paired timer-originated activation, trigger advancement, service result and exit status. |
| Release rollback and recovery | Whole binary/state/unit/timer/daemon pair, persistent known-good bundle, explicit rollback as a new transaction, and restored-pair revalidation. |

Each row has an owner, an observable pass/fail result, and a named deterministic
fixture. No additional technology decision is required before these stories can
be written.

## Validation Record

| Validation | Command or method | Result |
| --- | --- | --- |
| Frozen review identity | `git rev-parse HEAD`; `sha256sum ARCHITECTURE-SPINE.md` | **PASS** — head `d4515067af8314cadf979da7b17921fbafc92d21`; spine SHA-256 `d9128bcc347f553045198a5402f0b91f068013728460de64c6105ec3d57429b2`. |
| Required complete reads | Line-bounded reads through EOF | **PASS** — SPINE 1,176; MEMLOG 142; PRD 823; ADDENDUM 63; DESIGN 329; EXPERIENCE 813; TECH-ACCEPT 193; DIVERGENCE-ACCEPT 362; RUBRIC-ACCEPT 286 lines. |
| Accepted reality evidence | Complete `TECH-CURRENCY` and acceptance matrix comparison | **PASS** — all accepted facts preserved; no unimplemented artifact presented as current proof. |
| Architecture linter | `uv run .agents/skills/bmad-architecture/scripts/lint_spine.py --workspace _bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14` | **PASS** — `ok: true`; zero findings. |
| Identifier definitions | Ordered AD and ARCH-LIM definition extraction | **PASS** — AD-1 through AD-25 and ARCH-LIM-1 through ARCH-LIM-23, with no gaps or duplicate definitions. |
| Required term inspection | Exact term and line-number search over the frozen spine | **PASS** — all ordered SQLite, ABI, managed consumer, timer, and whole-pair recovery terms land in enforceable Rules and fixtures. |
| Markdown lint | `markdownlint-cli2 --config _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/.markdownlint-cli2.jsonc <this-report>` | **PASS** — one file, zero errors. |
| Whitespace/error check | `git diff --check` | **PASS** — no output after report creation. |
| Product bootstrap reality | Presence check for `Cargo.toml` and `Cargo.lock` | **PASS AS PLANNING STATE** — both absent; proof remains correctly assigned to bootstrap. |

## Final Gate Status

**APPROVED. Blocking status: CLEAR for technology and release architecture.**
No technology remediation finding remains open. This verdict approves the
frozen working-tree spine identified above; any later semantic change to AD-11,
AD-12, AD-16, AD-20, AD-23, the Stack, or Deferred requires re-review.
