# srvls

**Background-task inventory in one view.** Every cron job, systemd service/timer
(system *and* user), docker container, and pm2 process on the box — one command,
one table. The antidote to "what is killing my server right now?".

Single-file Python CLI. **Stdlib only** — no pip install, no venv, no dependencies.

## Why

Background work on a long-lived server accretes across at least five schedulers:
user crontab, root crontab, `/etc/cron.d`, systemd (system + user scopes), docker
restart policies/healthchecks, and pm2. No single stock tool shows all of them,
so the failure mode is always the same: something is eating CPU at 3am and you
spend twenty minutes remembering where to even look. `srvls` collapses that search
space to one command — and exports the same inventory as Prometheus metrics and
markdown snapshots so drift is observable over time.

## Install

```bash
git clone git@github.com:delorenj/srvls.git ~/code/srvls && ln -sf ~/code/srvls/srvls ~/.local/bin/srvls
```

Requires Python 3.8+. Optional: `fzf` (for `--fzf`), `docker`, `pm2`,
passwordless `sudo` (for the root crontab; silently skipped otherwise).

## Usage

### Item types

| type | what |
| --- | --- |
| `cron` | user crontab, root crontab, `/etc/crontab`, `/etc/cron.d/*` |
| `sys-svc` / `sys-timer` | systemd system scope services / timers |
| `usr-svc` / `usr-timer` | systemd `--user` scope services / timers |
| `docker` | all containers (state, health, restart policy, compose project) |
| `pm2` | pm2 processes (status, restart count) |

### Modes

**Table (default)** — the unified inventory with a failed/unhealthy tally:

```console
$ srvls
TYPE       NAME                          STATE            SCHED             SOURCE
---------------------------------------------------------------------------------
cron       backup.sh                     scheduled        0 3 * * *         crontab:delorenj
sys-svc    docker.service                active/running                     enabled
usr-timer  srvls-metrics.timer            waiting          next 06-10 11:15  srvls-metrics.service
docker     traefik                       running(healthy) hc:30s            /home/delorenj/docker/stacks/proxy
pm2        n8n                           online           restarts:3        /home/delorenj/code/n8n

312 items (2 failed, 1 unhealthy)
```

**`--json`** — machine-readable inventory (list of `{type, name, state, schedule, source, detail}`):

```bash
srvls --json | jq '[.[] | select(.state | test("failed|unhealthy"))]'
```

**`--prom`** — Prometheus textfile exposition: `srvls_items{type,state}` counts,
`srvls_unit_problem{type,name}` per failed/unhealthy/restarting/errored unit,
`srvls_loadavg{window}`, and `srvls_collect_timestamp_seconds`:

```bash
srvls --prom > /var/lib/node_exporter/textfile/srvls.prom
```

**`--md`** — markdown snapshot grouped by type (for nightly inventory commits):

```bash
srvls --md > docs/inventory/$(date +%F).md
```

**`--fzf`** — interactive triage. Fuzzy-find any item; the preview pane shows a
live inspect (status + recent logs). Keybinds act in place and reload the list:

| key | action |
| --- | --- |
| `enter` | inspect (status + recent logs) |
| `ctrl-s` | stop |
| `ctrl-r` | restart |
| `ctrl-x` | disable (docker → stop, pm2 → delete) |

### Action subcommands

```bash
srvls inspect TYPE NAME    # detail view: systemctl status / docker logs / pm2 describe / cron line
srvls stop TYPE NAME       # systemctl [--user] stop / docker stop / pm2 stop
srvls restart TYPE NAME    # systemctl [--user] restart / docker restart / pm2 restart
srvls start TYPE NAME      # symmetric start
srvls disable TYPE NAME    # systemctl disable / docker stop / pm2 delete
```

Examples:

```bash
srvls inspect docker traefik
srvls restart usr-svc srvls-metrics.service
srvls stop pm2 n8n
```

`cron` items are read-only (edit with `crontab -e`; `inspect` shows the exact
source file and line). System-scope (`sys-*`) actions go through `sudo`.

## Integration pattern: metrics + nightly snapshots

How this runs in production on big-chungus — two systemd user timers:

The unit files are host-managed rather than deployable assets in this repo.
Their normalized 2026-07-17 source/candidate contracts and two-pair rollback
direction are frozen by
`tests/fixtures/contracts/release-transaction-v1/brownfield-consumer-pairs.json`.

**1. Prometheus textfile collector, every 5 minutes** (`srvls-metrics.timer`):

```ini
# ~/.config/systemd/user/srvls-metrics.service
[Unit]
Description=srvls inventory metrics -> node-exporter textfile collector

[Service]
Type=oneshot
ExecStart=/bin/sh -c 'srvls --prom > %h/.local/state/node-exporter-textfile/srvls.prom.tmp && mv %h/.local/state/node-exporter-textfile/srvls.prom.tmp %h/.local/state/node-exporter-textfile/srvls.prom'
```

```ini
# ~/.config/systemd/user/srvls-metrics.timer
[Timer]
OnBootSec=2min
OnUnitActiveSec=5min
RandomizedDelaySec=20

[Install]
WantedBy=timers.target
```

Write to a `.tmp` file and `mv` so node-exporter never scrapes a half-written
file. Point node-exporter's `--collector.textfile.directory` at the state dir,
then alert on e.g. `srvls_unit_problem == 1` or a stale
`srvls_collect_timestamp_seconds`.

**2. Nightly markdown snapshot, committed to git** (`srvls-snapshot.timer`,
`OnCalendar=*-*-* 04:10:00`):

```ini
[Service]
Type=oneshot
ExecStart=/bin/sh -c 'srvls --md > %h/code/infra/docs/inventory/$(date +%%F).md'
ExecStartPost=/bin/sh -c 'cd %h/code/infra && git add docs/inventory && git commit -m "inventory: nightly srvls snapshot $(date +%%F)" --quiet || true'
```

`git diff` between two dated snapshots answers "what changed on this box since
last week?" for free.

## Tests

```bash
mise run test          # or: bash tests/test_smoke.sh
```

## License

MIT — see [LICENSE](LICENSE).
