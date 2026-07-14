# Deployment and Operations Guide

## Installation model

The application is deployed as an executable Python file on a Linux host:

```bash
ln -sf /path/to/repository/srvls ~/.local/bin/srvls
```

Python 3.8+ is the only required runtime. Docker, PM2, fzf, and passwordless sudo are optional and affect available inventory or interaction.

## Privileges

- User cron and user systemd require the invoking user's normal access.
- Root cron is attempted with `sudo -n` and silently omitted when unavailable.
- System systemd lifecycle actions invoke `sudo systemctl`.
- Docker access follows the local Docker socket/daemon policy.
- PM2 visibility follows the invoking user's PM2 home/daemon.

Run the CLI as the same user whose user-scoped workloads should be inventoried.

## Prometheus textfile integration

The README describes a systemd user oneshot/timer that runs every five minutes. It writes to a temporary file and atomically renames it so node-exporter never reads a partial exposition file. The repository does not ship these unit files; operators must create and enable them separately.

Relevant metrics are:

- `srvls_items{type,state}`
- `srvls_unit_problem{type,name}`
- `srvls_loadavg{window}`
- `srvls_collect_timestamp_seconds`

The `srvls_` metric namespace is the stable public metrics contract.

## Markdown snapshot integration

The README also describes a nightly user timer redirecting `srvls --md` into a separate infrastructure repository, followed by a Git commit. This provides drift history but depends on external repository paths, permissions, and Git configuration.

## Operational behavior

- Collection is sequential and may wait on multiple external-command timeouts.
- Errors and timeouts generally become missing inventory rather than nonzero exits.
- Exports can disclose cron commands, process paths, Compose working directories, and service names.
- Lifecycle actions are immediate and have no confirmation prompt.
- `disable` semantics differ: systemd disables, Docker stops, and PM2 deletes.

## Deployment validation

After installation:

```bash
srvls --json | python3 -m json.tool >/dev/null
srvls --prom | grep '^srvls_collect_timestamp_seconds '
srvls --md | head
```

Then verify each expected subsystem appears. An empty subsystem may mean unavailable tooling, insufficient privilege, parse failure, timeout, or genuinely no resources.

## No repository-managed deployment

There is no Dockerfile, Compose stack, package release workflow, CI/CD pipeline, checked-in systemd unit, Terraform, or configuration-management role. README snippets are operational recipes, not deployable artifacts.
