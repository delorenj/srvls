# srvls Project Overview

## Executive summary

`srvls` is a single-file, standard-library-only Python CLI that inventories background work on a Linux host across cron, systemd system and user scopes, Docker, and PM2. It renders the unified inventory as a terminal table, JSON, Prometheus text exposition, or Markdown, and offers inspect and lifecycle actions for supported resources.

## Classification

| Attribute | Value |
|---|---|
| Repository structure | Single-part monolith |
| BMAD project type | CLI |
| Primary language | Python 3.8+; validated with Python 3.14.4 |
| Runtime dependencies | Python standard library only |
| Optional integrations | `fzf`, Docker CLI, PM2 CLI, `sudo`, systemd, cron |
| Architecture | Collector pipeline with normalized records, renderers, and command adapters |
| Persistence | None; reads host state and writes only to stdout unless redirected |

## Product capabilities

- Collect user/root/system cron entries.
- Collect systemd services and timers in system and user scopes.
- Collect Docker containers, health, restart policy, and Compose provenance.
- Collect PM2 process status and restart counts.
- Emit a human-readable table, JSON records, Prometheus metrics, or Markdown snapshots.
- Inspect cron, systemd, Docker, and PM2 resources.
- Start, stop, restart, or disable supported resources; cron remains read-only.
- Use `fzf` for interactive inspection and lifecycle actions.

## Current project state

- The repository has no release tags. Version tasks therefore report `v0.0.0` until the first release is tagged.
- No package manifest or installable Python package exists; the executable script itself is the distribution artifact.
- No CI pipeline is present.
- README deployment examples describe production integration but are not deployment automation in this repository.

## Documentation map

- [Architecture](./architecture.md)
- [Source Tree Analysis](./source-tree-analysis.md)
- [Component Inventory](./component-inventory.md)
- [Development Guide](./development-guide.md)
- [Deployment and Operations Guide](./deployment-guide.md)
