# Development Guide

## Prerequisites

- Linux host for full systemd/cron behavior.
- Python 3.8 or newer; no Python packages are required.
- Bash for the smoke suite.
- Optional `mise` for task shortcuts.
- Optional `docker`, `pm2`, `fzf`, and passwordless `sudo` expand coverage/features.

## Setup

There is no build or dependency-install step. Ensure the script is executable, then run it directly:

```bash
./srvls --json
```

The documented user install is a repository clone followed by a symlink from `srvls` into `~/.local/bin/srvls`.

## Tests

```bash
mise run test
# equivalent
bash tests/test_smoke.sh
```

The exhaustive documentation scan validated:

```text
--json: 287 items
--prom: 18 samples
--md: ok
table: ok
inspect cron git-checkpoint: ok
inspect hostile-name: no injection
PASS
```

Counts and the selected cron item are host-dependent. Python syntax also passed with bytecode redirected outside the repository:

```bash
PYTHONPYCACHEPREFIX=/tmp/srvls-pycache python3 -m py_compile srvls
```

## Coding conventions

- Keep the runtime standard-library-only unless a deliberate product decision changes that constraint.
- Execute external commands as argument arrays, never through a shell.
- Preserve the normalized six-field item contract across collectors.
- Treat collector failure as an explicit design question; the current empty-string fallback hides errors.
- Keep state-changing tests out of the live-host smoke suite.
- Add hostile-input regression cases for every new command surface.

## Common changes

### Add a collector

Return normalized dictionaries, add the collector to `collect_all()`, decide how its type maps to inspect/actions, and extend smoke assertions. Make unavailable tooling degrade safely.

### Add an output mode

Implement a renderer over the normalized list, add routing in `main()`, and test both structure and escaping.

### Add a lifecycle type

Extend `_unit_cmd()` and `inspect()`. Document privilege requirements and ensure the resource name remains an argv element.

## Versioning

`mise run version`, `version:bump*`, `version:check`, and `version:sync` delegate to `.mise/scripts/versioning.sh`. The manifest currently tracks only Git tags. Until the first release is tagged, `version` returns `v0.0.0` and `version:check` reports no version found.

## Known development gaps

- No unit tests or mocks for collector edge cases.
- No CI configuration.
- No linter, formatter, type checker, or coverage target.
- No `--help`/argument parser; unknown options trigger normal inventory.
- No package metadata or reproducible release artifact beyond the script.
