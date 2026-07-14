# Project Documentation Index

## Project overview

- **Project identity:** `srvls`
- **Type:** Single-part monolithic CLI
- **Primary language:** Python
- **Architecture:** Sequential collectors → normalized records → renderers/actions
- **Entry point:** `../srvls`

The executable, documentation, metrics, tests, project metadata, and operational examples consistently use the `srvls` identity.

## Quick reference

- **Runtime:** Python 3.8+, standard library only
- **Test:** `mise run test`
- **Inventory:** `./srvls`, `./srvls --json`, `./srvls --prom`, `./srvls --md`
- **Interactive:** `./srvls --fzf`
- **Actions:** `./srvls inspect|start|stop|restart|disable TYPE NAME`
- **Version status:** `v0.0.0` until active Git history/tags are established

## Generated documentation

- [Project Overview](./project-overview.md)
- [Architecture](./architecture.md)
- [Source Tree Analysis](./source-tree-analysis.md)
- [Component Inventory](./component-inventory.md)
- [Development Guide](./development-guide.md)
- [Deployment and Operations Guide](./deployment-guide.md)

API contracts and data-model documents are not applicable: the project exposes no network API and has no durable data model. Integration architecture is included in the single-part architecture document.

## Existing documentation

- [README](../README.md) — current `srvls` user, usage, and operations guide
- [Agent Instructions](../AGENTS.md) — repository-local orchestration policy
- [Task Ledger](../tasks.md) — current documentation workflow claim

## Getting started

1. Read [Project Overview](./project-overview.md) for project scope and capabilities.
2. Read [Architecture](./architecture.md) before changing collectors, output contracts, or actions.
3. Use [Development Guide](./development-guide.md) to validate changes.
4. Use [Deployment and Operations Guide](./deployment-guide.md) before installing timers or granting privileges.

For AI-assisted changes, treat live code and current metadata as the source of truth.
