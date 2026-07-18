---
title: "srvls PRD Addendum: Downstream Design Constraints"
status: final
created: 2026-07-16
updated: 2026-07-16
---

# srvls PRD Addendum: Downstream Design Constraints

## Purpose

This addendum preserves user-supplied implementation direction and readiness corrections that constrain downstream UX, architecture, and story planning. It is not a substitute for product requirements in `prd.md`.

## Approved Technical Direction

- Deliver one Rust binary initially, preserving the one-tool operator experience.
- Keep a hexagonal core: domain and application policy do not depend on host commands, terminal rendering, argument parsing, or export serialization.
- Use an Elm-style ratatui shell with explicit model, message, update, view, and effect boundaries.
- Keep Strategy, Adapter, and Command as explicit variation seams; prefer composition for normalized inventory and reconciliation projections.
- Build a layered migration oracle from the checked-in Python behavior inventory, a frozen deterministic fixture and golden corpus, `tests/test_smoke.sh` as live-Host integration evidence, and end-to-end checks for named deployed consumers. Any deliberate deviation belongs in an explicit compatibility ledger.
- Preserve deterministic non-interactive table, JSON, Prometheus, Markdown, inspection, executable-name, and explicit-action behavior until an approved requirement changes it.

## Mandatory Planning Corrections

- Put the Rust 2024 crate bootstrap, module boundaries, committed lockfile, baseline harness, formatting, linting, locked tests, MSRV 1.88, and current-stable CI gates before provider implementation.
- Separate total bounded subprocess execution from concurrent provider orchestration and outcome policy.
- Define an explicit TUI start interaction or consistently scope start to a non-TUI surface.
- Separate mutation initiation and confirmation from asynchronous execution, race handling, verification, and outcome rendering.

## Legacy Requirement Reconciliation

The 2026-07-15 epic artifact used non-canonical `FR1` through `FR18` identifiers. The canonical PRD retires those identifiers and maps their intent as follows.

| Legacy ID | Canonical requirement(s) | Disposition |
| --- | --- | --- |
| FR1 | FR-8 | Cron collection preserved |
| FR2 | FR-9 | systemd collection preserved |
| FR3 | FR-10 | Docker collection preserved |
| FR4 | FR-11 | PM2 collection preserved |
| FR5 | FR-13 | Provider-neutral normalization preserved |
| FR6 | FR-14 | Collection completeness and diagnostics preserved |
| FR7 | FR-30 | Interactive default and redirected table behavior preserved |
| FR8 | FR-29 | Deterministic Stack grouping preserved and placed after attention summary |
| FR9 | FR-29 | Stack confidence, evidence, and Ungrouped behavior preserved |
| FR10 | FR-31, FR-34 | Navigation, refresh, help, inspection entry, and small-terminal behavior preserved |
| FR11 | FR-33 | Semantic color, icon, text, `NO_COLOR`, and ASCII behavior preserved |
| FR12 | FR-15, FR-32 | Bounded Provider detail preserved and linked to declared intent |
| FR13 | FR-35 through FR-40 | Individual lifecycle actions preserved and decomposed into interaction, planning, identity, execution, and verification contracts |
| FR14 | FR-37 through FR-41 | Confirmation, stale protection, and read-only groups preserved |
| FR15 | FR-16 | Layered Python-behavior compatibility preserved |
| FR16 | FR-30 | Deprecated `--fzf` alias and `--fzf-lines` removal preserved |
| FR17 | FR-14, FR-17 | Partial diagnostics and strict outcome policy preserved |
| FR18 | FR-42, FR-43 | Release, install, validation, upgrade, and rollback preserved and split |

Legacy `NFR1` through `NFR10` are reconciled into canonical `NFR-1` through `NFR-16` plus the Approved Technical Direction above. The old `UX-DR1` through `UX-DR8` identifiers remain legacy candidate inputs until the dedicated UX contract is created and approved; that final UX contract will supersede them as the downstream UX source while this PRD remains the canonical product source.

## Architecture Decisions to Resolve Downstream

- Durable format and location for Runtime Promise records, observations, reconciliation snapshots, and audit history.
- Agent-facing declaration, heartbeat, renewal, release, and query contracts.
- Lease-clock and expiry semantics across agent exit, host restart, suspend, and clock discontinuity.
- Evidence-weighting and identity rules that correlate declarations to cron, systemd, Docker, PM2, and process observations.
- Retention boundaries that support morning change detection without turning srvls into a general telemetry store.
