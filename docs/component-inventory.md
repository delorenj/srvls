# Component Inventory

This CLI has no UI component library. Its reusable components are Python functions and shell automation surfaces.

| Component | Location | Responsibility | Side effects |
|---|---|---|---|
| `run` | `srvls` | Best-effort captured subprocess execution | Spawns read commands |
| `collect_cron` | `srvls` | Parse cron sources into normalized items | Reads host files and crontabs |
| `_systemd` | `srvls` | Collect services/timers by scope | Calls systemctl |
| `collect_docker` | `srvls` | Collect container/Compose metadata | Calls Docker daemon via CLI |
| `collect_pm2` | `srvls` | Collect PM2 process metadata | Calls PM2 daemon via CLI |
| `collect_all` | `srvls` | Sequential aggregation | Invokes all collectors |
| `out_table` | `srvls` | Human-readable inventory | Writes stdout |
| `out_prom` | `srvls` | Prometheus exposition | Reads load average; writes stdout |
| `out_md` | `srvls` | Markdown snapshot | Writes stdout |
| `_unit_cmd` | `srvls` | Map resource type/verb to command argv | None |
| `action` | `srvls` | Run lifecycle commands | Mutates supported host resources |
| `_show` | `srvls` | Bounded command-output display | Spawns inspection commands |
| `inspect` | `srvls` | Resource-specific details/logs | Read-only host inspection |
| `fzf_mode` | `srvls` | Interactive selection/actions | May inspect or mutate resources |
| `main` | `srvls` | CLI routing | Selects all behavior |
| Smoke suite | `tests/test_smoke.sh` | Output contracts and injection regression | Read-only host collection |
| Version helper | `.mise/scripts/versioning.sh` | Semver resolution and mutation | Can edit manifests/create tags |

## Normalized item contract

Every collector returns dictionaries with `type`, `name`, `state`, `schedule`, `source`, and `detail`. Renderers and the interactive layer depend on this shared shape; changing it requires updating the smoke test and all output modes.

## Supported type identifiers

`cron`, `sys-svc`, `sys-timer`, `usr-svc`, `usr-timer`, `docker`, and `pm2`.

