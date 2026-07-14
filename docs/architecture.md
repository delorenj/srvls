# srvls Architecture

## Executive summary

The implemented `srvls` CLI is a procedural, single-process Python application. Its main pipeline collects host scheduler/process state into one normalized item schema, then selects a renderer or interactive mode. Action subcommands bypass collection and dispatch directly to external command adapters. There is no server, database, API, background daemon, or internal persistence layer.

## Technology stack

| Category | Technology | Version/evidence | Purpose |
|---|---|---|---|
| Runtime | CPython | README requires 3.8+; validated on 3.14.4 | CLI execution |
| Language | Python | Single executable `srvls` | Product implementation |
| Libraries | Standard library | `json`, `os`, `re`, `shutil`, `subprocess`, `sys`, `datetime` | Parsing, process execution, formatting |
| Task runner | mise | `mise.toml` | Tests, agent links, versioning |
| Tests | Bash + Python assertions | `tests/test_smoke.sh` | End-to-end smoke/regression checks |
| Interactive UI | fzf | Optional executable | Selection, preview, action keybindings |
| Host adapters | cron, systemd, Docker, PM2 | External CLIs/files | Inventory and lifecycle operations |

## Architectural pattern

```text
CLI arguments
   |-- action verb ----------------> command adapter ------> systemctl/docker/pm2
   |
   `-- inventory mode
          |
          +--> cron collector -----+
          +--> systemd collectors -+--> normalized item[] --> table/JSON/Prometheus/Markdown
          +--> Docker collector ---+                         `--> fzf interactive adapter
          `--> PM2 collector ------+
```

The normalized record is the central contract:

```json
{
  "type": "docker",
  "name": "traefik",
  "state": "running(healthy)",
  "schedule": "hc:30s",
  "source": "/path/to/compose/project",
  "detail": "restart=unless-stopped"
}
```

## Components

### Process wrapper

`run(cmd, timeout=15)` executes argument arrays with captured text output and returns an empty string on any exception. This keeps collectors best-effort but intentionally hides command errors and timeouts.

### Collectors

- `collect_cron()` parses the user crontab, passwordless-root crontab, `/etc/crontab`, and `/etc/cron.d/*`. Environment assignments and comments are ignored. System crontab user fields are stripped heuristically.
- `_systemd(scope)` requests JSON from `systemctl list-units`, `list-unit-files`, and `list-timers`. Inactive services are retained only when enabled.
- `collect_docker()` enumerates container IDs then performs one formatted `docker inspect` call to obtain state, health, restart policy, Compose project, working directory, and healthcheck interval.
- `collect_pm2()` uses `pm2 jlist` when PM2 is available.
- `collect_all()` concatenates collector results in fixed order; it does not deduplicate or parallelize.

### Renderers

- `out_table()` derives bounded column widths and prints problem totals.
- `--json` serializes the normalized records directly.
- `out_prom()` aggregates counts by type and coarse state, emits one gauge for each detected problem resource, adds host load averages, and timestamps collection.
- `out_md()` groups records by type into Markdown tables.

### Actions and inspection

`_unit_cmd()` maps normalized types to argument-array commands. User systemd units use `systemctl --user`; system units use `sudo systemctl`; Docker uses its CLI; PM2 uses its CLI. `disable` maps to `stop` for Docker and `delete` for PM2. Cron actions are rejected.

Inspection uses `_show()` with argument arrays and output limits. Docker inspection includes recent logs; systemd shows bounded status; PM2 uses `describe`; cron searches the collected entries.

### Interactive fzf mode

`fzf_mode()` feeds tab-separated inventory records to `fzf`. Preview and keybinding commands invoke the absolute script path for inspect, stop, restart, and disable. Names are substituted by fzf into command strings, so this surface deserves continued adversarial testing even though direct Python subprocess calls avoid shell invocation.

## Security and privilege model

- Direct subprocess calls use argument arrays, preventing ordinary shell interpolation. The hostile-name regression test covers inspect paths.
- Root cron collection uses non-interactive `sudo -n`; lack of privilege degrades to an empty result.
- System-scope mutations invoke `sudo systemctl` and can prompt/fail according to host policy.
- The tool has broad visibility into process names, command lines, Compose paths, and cron commands. JSON/Markdown exports should be handled as potentially sensitive operational data.
- Collector exceptions are swallowed, so absence in output does not prove absence on the host.
- `.env` is generated from 1Password references and ignored. Documentation must never include resolved secret values.

## Data and state

There are no domain models or durable application data stores. Each invocation builds an in-memory list of six-field dictionaries from current host state. Redirected Markdown, JSON, and Prometheus outputs become external snapshots managed by the caller.

## Development workflow

The source is directly executable. `mise run test` invokes the smoke suite. The versioning helper supports multiple manifest formats, but this repo's manifest contains only `gittag .`; until the first release tag it resolves to `v0.0.0`.

## Deployment architecture

Installation is a clone plus symlink into `~/.local/bin`. README examples show two optional systemd user-timer patterns: atomic Prometheus textfile generation every five minutes and nightly Markdown snapshots committed in another infrastructure repository. Those units are examples, not checked-in deployable units.

## Testing strategy

The smoke test exercises JSON validity/schema, Prometheus metric families, Markdown structure, table summary output, read-only cron inspection when available, and hostile names across PM2, Docker, and user-systemd inspect paths. It intentionally uses the live host and therefore is integration-oriented rather than deterministic unit coverage.

## Constraints and risks

- Packaging and release automation are not yet implemented.
- `--help` is not a real help mode; unknown flags fall through to the default inventory table.
- Best-effort error swallowing makes partial inventory indistinguishable from a clean empty subsystem.
- Live-host smoke tests may be slow or environment-sensitive.
- Markdown output does not escape pipe characters in fields.
- Prometheus labels only strip double quotes from problem names; backslashes/newlines are not fully escaped.
- No CI, packaging metadata, structured logging, or typed internal model exists.
