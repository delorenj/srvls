---
title: "srvls Architecture Review: Live Operations and Migration Oracle"
status: final
review_date: 2026-07-16
reviewed_commit: ae011f3
verdict: changes-required
---

<!-- markdownlint-disable MD013 MD025 -->

# srvls Architecture Review: Live Operations and Migration Oracle

## Verdict

**CHANGES REQUIRED.** The hexagonal core, one-crate start, typed identity,
unidirectional TUI, deterministic compatibility corpus, read-only groups, and
single terminal owner remain sound. The 2026-07-14 spine is not a sufficient
build substrate for the now-canonical product.

The finalized PRD and UX add Runtime Promises, Heartbeats and Leases, direct
Host processes, durable accepted baselines and Snapshots, local lifecycle and
action history, configuration provenance, a larger command surface, and a
different action-outcome algebra. The spine still describes an inventory
replacement whose only durable contract is the legacy `Entry` projection.

The practical gate is:

- **GO:** one-time Python compatibility capture and a non-provider Rust
  bootstrap with early CI.
- **NO-GO:** Provider replacement, durable-state implementation, TUI mutation,
  or release implementation until the architecture and epics absorb the
  canonical PRD, UX, and the operational envelope recommended here.

This review is documentation-only. It does not amend the architecture spine,
its memlog, any canonical PRD or UX artifact, `tasks.md`, or product code.

## Review basis and evidence labels

The reviewed worktree was clean on
`feature-codemaster-zigzag-architecture-live` at `ae011f3` before this report
was created.

Evidence precedence for this review is:

1. **LIVE:** checked-in executable behavior, current tests, and commands run on
   the review Host.
2. **CANONICAL:** finalized PRD/addendum and UX spine pair for target behavior.
3. **RECOMMENDED:** architecture-owned defaults proposed here where neither
   live behavior nor a canonical artifact supplies a number.

Current behavior is not automatically the desired Rust behavior. Where LIVE
and CANONICAL conflict, the current behavior remains the migration oracle and
the canonical requirement requires an explicit compatibility-ledger deviation.
The PRD makes that layered-oracle rule explicit
(`_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:339-349`).

## Executed command evidence

### Baseline gates

```text
$ PYTHONPYCACHEPREFIX=/tmp/srvls-pycache-zigzag \
    python3 -m py_compile srvls
exit 0

$ bash tests/test_smoke.sh
  --json: 467 items
  --prom: 25 samples
  --md: ok
  table: ok
  inspect cron git-checkpoint: ok
  inspect hostile-name: no injection
PASS
```

The smoke assertions cover JSON parsing and the first record's required keys,
the exact project-owned Prometheus family allowlist, Markdown structure, the
table summary, one real cron inspection when available, and hostile names on
three direct inspection paths
(`tests/test_smoke.sh:12-90`). They do not freeze Provider parsing, all-record
schema, argument routing, partial failure, output escaping, fzf command
construction, action execution, verification, cancellation, or durable state.

The mandatory deterministic corpus is not present:

```text
$ if test -d tests/compat; then echo tests/compat=PRESENT; \
    else echo tests/compat=ABSENT; fi
tests/compat=ABSENT

$ git ls-files '*.rs' Cargo.toml Cargo.lock 'rust-toolchain*' '.github/**' |
    wc -l
0
```

That confirms the architecture's named `tests/compat` authority and the Rust
bootstrap are designs, not live assets
(`_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:93-109`).

### Live output snapshot

The following probes ran each mode in a separate process. Counts and byte sizes
are Host- and time-dependent evidence, not golden values.

| Invocation | Exit | stdout | stderr | Observed discriminator |
| --- | ---: | ---: | ---: | --- |
| `./srvls --json` | 0 | 95,266 bytes | 0 | 467 records; all records used key order `type,name,state,schedule,source,detail` |
| `./srvls --prom` | 0 | 1,700 bytes | 0 | 25 samples; HELP-family order was items, unit_problem, loadavg, timestamp |
| `./srvls --md` | 0 | 32,924 bytes | 0 | UTC title; type sections sorted lexically |
| `./srvls` | 0 | 58,647 bytes | 0 | `467 items (7 failed, 0 unhealthy)` |
| `./srvls --fzf-lines` | 0 | 29,567 bytes | 0 | tab-separated `type,name,state,source` |
| `./srvls --help` | 0 | 58,647 bytes | 0 | default inventory table, not help |
| `./srvls --definitely-unknown ignored` | 0 | 58,647 bytes | 0 | default inventory table |
| `./srvls --md --json` | 0 | 95,266 bytes | 0 | JSON wins |
| `./srvls --prom --md` | 0 | 1,700 bytes | 0 | Prometheus wins |
| `./srvls --json --prom` | 0 | 95,266 bytes | 0 | JSON wins |
| `./srvls inspect bogus name` | 0 | 0 | 0 | unknown inspect type is successful and empty |
| `./srvls stop cron name` | 1 | 61 bytes | 0 | refusal is on stdout |
| `./srvls stop bogus name` | 1 | 23 bytes | 0 | refusal is on stdout |
| `./srvls inspect cron` | 1 | 0 | 31 bytes | usage is on stderr |

The live JSON bucket transitions were `cron`, `sys-svc`, `sys-timer`,
`usr-svc`, `usr-timer`, and `docker`. PM2 was absent on this Host. The transition
order follows fixed concatenation, not lexical sorting
(`srvls:189-191`).

Three controlled failure probes exposed additional compatibility behavior:

```text
$ ./srvls inspect docker __srvls_zigzag_missing__
exit 0
stdout:

--- recent logs ---
Error response from daemon: No such container: __srvls_zigzag_missing__
stderr bytes: 0

$ ./srvls start pm2 __srvls_zigzag_missing__
exit 1, stdout bytes 0
stderr first line: Traceback (most recent call last):
stderr last line: FileNotFoundError: [Errno 2] No such file or directory: 'pm2'

$ PATH=/nonexistent /usr/bin/python3 ./srvls --fzf
exit 1, stdout bytes 0
stderr: fzf not installed
```

The Docker separator is unconditional, child-failed known inspection still
returns zero, action spawn failure escapes as a Python traceback, and absent fzf
uses stderr plus exit 1 (`srvls:267-276`, `srvls:296-320`). These ugly cases
belong in the frozen corpus; a safer replacement requires ledger entries rather
than silent cleanup.

### Canonical-Host timing and capture measurements

Each command below was sampled seven times. The table reports the median,
maximum, and final captured stream sizes without retaining the output content.

| Live command or source | Median | Max | stdout bytes | stderr bytes / exit |
| --- | ---: | ---: | ---: | --- |
| `crontab -l` | 0.6 ms | 0.8 ms | 2,841 | 0 / exit 0 |
| `sudo -n crontab -l` | 19.7 ms | 21.0 ms | 0 | 20 / exit 1 |
| system `systemctl list-units` | 5.1 ms | 7.3 ms | 36,313 | 0 / exit 0 |
| system `systemctl list-unit-files` | 390.6 ms | 413.9 ms | 29,236 | 0 / exit 0 |
| system `systemctl list-timers` | 10.6 ms | 11.5 ms | 3,095 | 0 / exit 0 |
| user `systemctl list-units` | 5.4 ms | 6.3 ms | 32,408 | 0 / exit 0 |
| user `systemctl list-unit-files` | 149.2 ms | 167.1 ms | 21,461 | 0 / exit 0 |
| user `systemctl list-timers` | 7.0 ms | 8.4 ms | 7,939 | 0 / exit 0 |
| `docker ps -a --format '{{.ID}}'` | 13.3 ms | 13.8 ms | 1,222 | 0 / exit 0 |
| formatted batch `docker inspect` | 33.9 ms | 39.9 ms | 8,781 | 0 / exit 0 |
| `ps -eo pid=,ppid=,user=,lstart=,args=` proxy | 61.5 ms | 68.8 ms | 280,431 | 0 / exit 0 |
| six checked cron files | n/a | n/a | 2,762 total | largest file 1,136 |

The Host reported 32 logical CPUs and 1,948 numeric `/proc` entries. These
measurements support bounded parallel collection and multi-megabyte capture
headroom. They do not justify millisecond subprocess deadlines: daemon
unavailability, privilege mediation, cold caches, and Host load need orders of
magnitude of safety margin.

The live Provider-tool context for the capture was:

```text
Python 3.14.4
systemd 257 (257.9-0ubuntu2.5)
Docker client/server 29.2.1
PM2 ABSENT
fzf 0.60 (devel)
sudo-rs 0.2.8
```

The compatibility capture must record these versions/capabilities with its
fixtures. In particular, root-cron denial observed here came from sudo-rs, not
the traditional sudo implementation, and PM2 success behavior cannot be
captured from this Host without a controlled fixture.

The live system and user managers both expose 90-second default start and stop
job timeouts. That makes a 30-second universal action deadline invalid for
systemd even before unit-specific overrides:

```text
$ systemctl show --property=DefaultTimeoutStartUSec \
    --property=DefaultTimeoutStopUSec
DefaultTimeoutStartUSec=1min 30s
DefaultTimeoutStopUSec=1min 30s

$ systemctl --user show --property=DefaultTimeoutStartUSec \
    --property=DefaultTimeoutStopUSec
DefaultTimeoutStartUSec=1min 30s
DefaultTimeoutStopUSec=1min 30s
```

## Exact live compatibility oracle

### CLI routing and exit behavior

The Rust compatibility suite must freeze these behaviors before using clap:

1. The first argument is treated as an action only when it is exactly
   `inspect`, `stop`, `restart`, `disable`, or `start`. Exactly three arguments
   are required (`srvls:338-345`).
2. Inventory collection happens before output-mode selection
   (`srvls:347-360`). Even `--help` and unknown flags run every Collector.
3. Flags are detected by membership anywhere in argv, not parsed. Precedence is
   `--json`, `--prom`, `--md`, `--fzf-lines`, `--fzf`, then table
   (`srvls:347-360`). Extra arguments are ignored.
4. Bare invocation always prints the legacy table today. Canonical terminal
   auto-routing is an intentional target change, not current behavior
   (`srvls:359-360`;
   `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:491-499`).
5. Unknown or unmatched inspection returns 0 with no output because
   `inspect()` always returns 0 (`srvls:296-314`).
6. Cron and unsupported actions return 1 but put their refusal text on stdout
   (`srvls:267-276`).
7. A launched action inherits the child's stdout and stderr and returns only
   its exit code; it has no deadline, capture, verification, or audit boundary
   (`srvls:267-276`).

A conventional clap help/error contract would change points 2, 3, 5, and 6.
Rust must emulate them until an approved ledger entry supplies the replacement
assertion, version impact, and affected-consumer disposition.

### Collector command and parsing oracle

The common `run(cmd, timeout=15)` wrapper captures both streams, returns stdout
even when the child exits nonzero, discards stderr, and converts spawn errors,
decode errors, and timeouts to an empty string (`srvls:31-36`). This is why a
denied or failed Provider can look empty. Rust must fixture this behavior, then
depart from it explicitly to satisfy honest partial truth.

| Scope | Exact live source or argv | Live bound and reduction |
| --- | --- | --- |
| Invoking-user cron | `crontab -l` | 15-second subprocess timeout; nonzero stdout is still parsed |
| Root cron | `sudo -n crontab -l` | 15 seconds; denial stderr and exit are discarded |
| System cron files | `/etc/crontab` and sorted regular files in `/etc/cron.d` | direct whole-file text reads; no byte or time cap; only `PermissionError` for a `/etc/cron.d` file is skipped |
| System services | `systemctl list-units --type=service --all --output=json --no-pager` | 15 seconds; invalid/empty JSON becomes an empty list |
| System unit files | `systemctl list-unit-files --type=service --output=json --no-pager` | 15 seconds; invalid JSON leaves the enablement map empty |
| System timers | `systemctl list-timers --all --output=json --no-pager` | 15 seconds; invalid/empty JSON becomes an empty list |
| User systemd | the same three commands with `--user` immediately after `systemctl` | three independent 15-second calls |
| Docker IDs | `docker ps -a --format {{.ID}}` | 20 seconds; empty stdout means no Docker records |
| Docker detail | one `docker inspect --format DOCKER_FORMAT ID...` batch | 30 seconds; malformed rows with fewer than seven tab fields are skipped |
| PM2 | `pm2 jlist` | executed only when `pm2` resolves on PATH; 20 seconds; invalid JSON becomes empty |

`DOCKER_FORMAT` above is exactly this single argv value, with literal tab
characters between fields (`srvls:147-153`):

```text
{{.Name}}\t{{.State.Status}}\t{{if .State.Health}}{{.State.Health.Status}}{{else}}-{{end}}\t{{.HostConfig.RestartPolicy.Name}}\t{{index .Config.Labels "com.docker.compose.project"}}\t{{index .Config.Labels "com.docker.compose.project.working_dir"}}\t{{if .Config.Healthcheck}}{{.Config.Healthcheck.Interval}}{{else}}-{{end}}
```

Cron parsing ignores blank lines, comments, and uppercase-looking environment
assignments; requires at least six whitespace fields; strips a plausible user
field from every source beginning with `/etc/cron`; derives name from the first
command token; and preserves source/physical encounter order
(`srvls:41-80`).

The direct `/etc/crontab` read has no exception boundary, and `/etc/cron.d`
catches only `PermissionError`; other I/O and decode errors abort the entire
invocation (`srvls:67-79`). Likewise, systemd and PM2 catch JSON syntax errors
but not every valid-JSON/wrong-shape type error (`srvls:89-137`,
`srvls:169-185`). The deterministic corpus must include both malformed JSON and
valid JSON with incompatible shapes.

Systemd keeps inactive services only when unit-file state is `enabled` or
`enabled-runtime`. Timer state is `waiting` only when the JSON `next` value is
truthy, and the timestamp is divided by one million and formatted in local time
as `%m-%d %H:%M` (`srvls:83-138`).

Docker strips a leading slash from names, composes health into
`state(health)`, prefixes healthcheck schedule with `hc:`, prefers Compose
working directory over project as source, and emits `restart=POLICY` detail
(`srvls:141-166`).

PM2 visibility belongs to the invoking user's daemon. It emits name/status,
`restarts:N`, cwd, and executable path but no numeric or birth identity in the
legacy record (`srvls:169-186`).

Collection is strictly sequential in this order: cron, system systemd, user
systemd, Docker, PM2 (`srvls:189-191`). Concurrent Rust completion must never
change presenter order.

### Presenter oracle

- **Table:** width derives from data. Type is unbounded; name is capped at 52
  characters; state at 22; schedule at 16. The summary counts substring
  `failed` and `unhealthy` independently (`srvls:196-208`).
- **JSON:** `json.dumps(items, indent=2)` serializes the live six-key dictionaries
  directly and adds a trailing newline through `print` (`srvls:347-349`).
- **Prometheus:** count state is split at `/`, then `(`. Counts sort by
  `(type,state)`. Problem matching is substring-based for failed, unhealthy, and
  restarting, plus exact `errored`. Problem names remove only double quotes.
  Load average is formatted to two decimals and collection time to integer UTC
  epoch seconds (`srvls:211-234`).
- **Markdown:** title includes current UTC minute. Types sort lexically and
  names sort within type. Cells are not escaped, so pipes and newlines can alter
  structure (`srvls:237-250`;
  `docs/architecture.md:102-109`).
- **fzf lines:** encounter-order tab-separated `type,name,state,source` with no
  escaping (`srvls:354-356`).
- **fzf mode:** preview executes
  `python3 ABSOLUTE_SCRIPT inspect {1} {2}`. The stop/restart/disable bindings
  execute the same script and reload through `--fzf-lines`
  (`srvls:317-335`). fzf parses those constructed command strings; the current
  hostile-name smoke test covers direct Python inspect argv, not the fzf shell
  surface (`tests/test_smoke.sh:82-90`).
- **fzf absent:** the exact controlled probe above exits 1, writes
  `fzf not installed` to stderr, and writes no stdout (`srvls:317-320`).

The exact project-owned metric families are:

1. `srvls_items`
2. `srvls_unit_problem`
3. `srvls_loadavg`
4. `srvls_collect_timestamp_seconds`

The smoke suite rejects every other family and permits
`srvls_unit_problem` to be absent (`tests/test_smoke.sh:27-55`).

### Inspection oracle

`_show()` captures output with a 15-second default timeout, silently returns on
every exception, optionally merges stderr after stdout, splits lines, then
applies line and character-column truncation. It has no byte cap. The public
`inspect()` returns zero for every recognized child failure and every unknown
type (`srvls:279-314`).

| Type | Exact live argv | Live presentation limit |
| --- | --- | --- |
| Docker metadata | `docker inspect TARGET --format INSPECT_FORMAT` | no explicit line, column, or byte cap; format normally produces three lines |
| Docker logs | `docker logs --tail 15 TARGET` | stderr appended after stdout; no more than 15 requested log records; each rendered line sliced to 200 characters |
| System systemd | `systemctl status TARGET --no-pager -n 8` | first 30 returned lines; no column/byte cap |
| User systemd | `systemctl --user status TARGET --no-pager -n 8` | first 30 returned lines; no column/byte cap |
| PM2 | `pm2 describe TARGET` | first 30 returned lines; no column/byte cap |
| Cron | re-run all cron collection and match exact derived name or command prefix | every match and full command text; no line/byte cap |
| Unknown | no command | exit 0, empty stdout/stderr |

`INSPECT_FORMAT` is the one argv value below, including its two literal newline
characters (`srvls:296-303`):

```text
{{.Name}} {{.State.Status}} restart={{.HostConfig.RestartPolicy.Name}}
image: {{.Config.Image}}
compose: {{index .Config.Labels "com.docker.compose.project.working_dir"}}
```

Docker prints `--- recent logs ---` even if metadata spawn or inspection fails,
then merges log stderr after log stdout. Known inspections still return zero;
only bad public arity exits before inspection (`srvls:296-314`,
`srvls:338-345`).

The Rust legacy inspector must freeze these limits and stream-placement rules.
The canonical TUI/linear inspector additionally needs global byte and line
limits plus sanitization. Pathological legacy truncation changes must be named
in the ledger rather than hidden as an implementation detail.

### Action argv oracle

No command below uses an end-of-options marker. System actions use interactive
`sudo`, unlike root-cron collection's `sudo -n`.

| Public type | start | stop | restart | disable |
| --- | --- | --- | --- | --- |
| `usr-svc` / `usr-timer` | `systemctl --user start TARGET` | `systemctl --user stop TARGET` | `systemctl --user restart TARGET` | `systemctl --user disable TARGET` |
| `sys-svc` / `sys-timer` | `sudo systemctl start TARGET` | `sudo systemctl stop TARGET` | `sudo systemctl restart TARGET` | `sudo systemctl disable TARGET` |
| `docker` | `docker start TARGET` | `docker stop TARGET` | `docker restart TARGET` | `docker stop TARGET` |
| `pm2` | `pm2 start TARGET` | `pm2 stop TARGET` | `pm2 restart TARGET` | `pm2 delete TARGET` |
| `cron` | refused before argv construction | refused | refused | refused |
| unknown | refused before argv construction | refused | refused | refused |

This mapping is implemented at `srvls:255-276`. Public `disable` therefore has
three materially different native meanings. The canonical action planner must
retain the public compatibility mapping while showing the resolved native
operation before TUI execution.

## Canonical contradictions and missing architecture decisions

The table below distinguishes a contradiction from an ordinary elaboration.
Each row identifies an old spine assumption that independent implementations
could still follow even though the finalized target no longer permits it.

| ID | Old architecture assumption | Contradicting canonical truth | Required architecture disposition |
| --- | --- | --- | --- |
| C-1 | Scope is a Rust replacement for inventory, grouping, exports, inspection, actions, and ratatui; sources stop at Python-era files (`_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:7-23`). | The PRD is canonical and adds Promise lifecycle, direct processes, reconciliation, Briefs, durable state, and Agent contracts (`_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:10-16`). | Add PRD/addendum and UX spines as binding sources; expand the architecture altitude or create inherited feature spines before stories. |
| C-2 | Every Collector produces one `Entry` aggregate, which is the shared inventory center (`_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:51-55`). | Runtime Promise and Observation identities are separate, and reconciliation retains four orthogonal axes (`_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:119-130`, `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:147-164`). | Make `RuntimePromise`, `Observation`, `CollectionReport`, `ReconciliationFinding`, and `ActionOperation` separate aggregates. Keep `EntryV1` only as a compatibility projection. |
| C-3 | The old live model has no durable store; redirected output is caller-owned (`docs/architecture.md:86-88`). The spine has no storage port or state module (`_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:165-201`). | Promise records, lifecycle events, Snapshots, accepted baselines, and compatibility metadata must be atomic and durable (`_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:734-744`, `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:789-795`). | Add a local state repository, schema/version migration, atomic writer, recovery, retention/GC, permission, corruption, and audit contracts. |
| C-4 | `Snapshot` owns one collection generation and stale last-good is only a TUI display option (`_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:69-73`). | Snapshot is a durable Evidence Window boundary; baseline acceptance is explicit, incomplete acceptance is normally forbidden, and refresh never advances it (`_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:456-466`; `_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md:341-352`). | Separate ephemeral `CollectionGeneration`, durable `Snapshot`, current pointer, and `AcceptedBaseline`. Persist acceptance and override audit events. |
| C-5 | Supported adapters are cron, systemd, Docker, and PM2 (`_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:186-191`). | Direct Host processes are a v1 Provider with PID plus birth evidence and deduplication rules (`_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:285-292`). | Add process Collector, inspector, identity, attribution/deduplication, and identity-safe signal action seams. |
| C-6 | Collector outcomes reduce through Success/Partial/Failed/TimedOut/Denied/Unavailable plus only Required/Optional availability (`_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:69-73`). | Canonical outcomes are complete, partial, unavailable, denied, timed-out, and invalid-output; obligations are required, optional, or not-applicable and can be promoted by active Promises (`_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:303-328`; `_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md:25-34`). | Replace the algebra and add per-scope obligation provenance, dynamic promotion, excluded-scope reporting, and absence-evidence rules. |
| C-7 | Configuration is “CLI and environment only in v1” (`_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:145`). | Every policy value must expose effective value, source, overridden chain, default, units, and valid range; invalid config fails before state/TUI/effects (`_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md:114-136`, `_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md:450-457`). | Define a schema, user config path, source precedence, provenance value type, validation command surfaces, and no-hot-reload rule. |
| C-8 | Grouping is the TUI's primary concept and AD-4 permits only Provider-native, source, and name evidence (`_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:63-67`, `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:216-224`). | Attention and completeness precede Stack exploration, ambiguous Observations remain Ungrouped, and a supplied Project identity is first-class Stack evidence (`_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:123-131`, `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:470-489`; `_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md:59-94`). | Make Brief/completeness/attention the root view model. Add an exact, non-transitive supplied-Project evidence tier above native evidence, retain the remaining AD-4 algorithm, and keep Stack read-only. |
| C-9 | The key map exposes only direct `s`, `R`, and `x` actions; no Action Menu or baseline interaction exists (`_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:147`). | `a` is the canonical Action Menu, `b` owns baseline acceptance, and Start comes from a Promise with a resolved Launch Mechanism; there is no direct Start shortcut (`_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:536-543`; `_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md:280-317`). | Replace the key contract and add Promise-targeted action planning plus baseline effects. |
| C-10 | TUI confirmation is required for stop and disable/delete only (`_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:75-79`). | Safe Restart has normal confirmation; unknown safety needs typed acknowledgement; safe Start is nondestructive unless privilege/policy adds uncertainty (`_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md:235-250`, `_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md:319-339`). | Bind the full availability/confirmation matrix and make every shortcut enter the same plan path. |
| C-11 | Action results include `Stale`, map timeout/unavailable to ExecutedUnverified, and do not name a standalone TimedOut outcome (`_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:75-79`). | Exactly five terminal outcomes exist: verified, executed-unverified, refused, timed-out, failed. Pre-execution identity drift is refused/stale-identity; post-execution replacement is executed-unverified (`_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:585-605`). | Replace the action result enum and implement the canonical precedence table. “Stale” may exist only as a reason/state, never a sixth Action Outcome. |
| C-12 | The action target is an observed Entry; direct process and Promise-only start are absent (`_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:117-121`, `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:216-225`). | Start can be planned from an active Promise without an Observation; direct-process stop is allowed only through identity-safe signals (`_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:549-565`). | Generalize `ActionTarget` to Promise or exact Observation and bind Provider-specific target resolvers. |
| C-13 | A single terminal guard and signal-hook event are sufficient shutdown semantics (`_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:123-127`). | Pending, executing, and verifying operations have different signal outcomes; every submitted operation/outcome is durable and retrievable before exit (`_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md:392-410`). | Add operation-phase cancellation, durable outcome-before-exit, bounded shutdown, forced process-group termination/reaping, and `action status` recovery. |
| C-14 | UTC `SystemTime`/duration is the entire time convention (`_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:141`). | Lease calculation must resist wall-clock rollback and explicitly handle boot change, suspend, and discontinuity (`_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:738-740`). | Add Clock and BootIdentity ports, monotonic in-boot deadlines, persisted wall timestamps, and restart revalidation/expiry rules. |
| C-15 | External contracts are legacy presenters only, and the spine never allocates a top-level namespace ahead of the argv-membership router (`_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:93-97`; `srvls:338-360`). | Canonical Agent Promise commands, Brief/inspect/action `--linear`, config validate/explain, baseline acceptance, and durable action status are additive required surfaces (`_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md:385-457`). | Add a deterministic namespace dispatcher and versioned machine/linear presenters. Reserved canonical subcommands must dispatch before legacy flag membership, with every routing change ledgered. |
| C-16 | Detail caps, Collector deadlines, subprocess caps, retention, and verification bounds are named but numeric values are omitted (`_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:87-103`, `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:227-235`). | UX requires every effective value and provenance, and implementation readiness cannot become READY without defaults/ranges (`_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:762-764`, `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:814-819`; `_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md:552-577`). | Adopt an architecture-owned numeric envelope and generate validation, explain, fixture, and acceptance cases from one schema. |
| C-17 | AD-13 says v1 `EntryId` is not a durable external API (`_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:117-121`). | Promise IDs and operation IDs are durable lookup/idempotency keys, canonical IDs cross inspect/action machine surfaces, and released Provider identity becomes public (`_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:181-196`, `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:576-592`, `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:782-787`; `_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md:423-436`). | Limit legacy `EntryId` to compatibility projection. Define separately versioned, durable `PromiseId`, `ObservationId`, `OperationId`, `PlanId`, and Provider-native identity encodings plus migration/lookup rules. |
| C-18 | The old interaction summary treats Esc as back and `q` as quit (`_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:147`). | Esc never cancels a submitted operation, `q` quits only from the base Brief with no active operation, and signal disposition depends on operation phase (`_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md:280-297`, `_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md:392-410`). | Replace the summary with an explicit state/event matrix; route navigation, operation cancellation capability, signals, terminal restoration, and process exit as separate effects. |
| C-19 | NFR-7 requires “unconditional child reaping” (`_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:710-712`). | Linux cannot kill or reap a process sleeping in uninterruptible I/O until the kernel call returns. A blocking `/etc`, `/proc`, Provider, or state-filesystem operation can therefore outlive every userspace deadline. | Interpret the requirement as unconditional bounded **attempts** plus nonblocking eventual reaping while the parent lives. Put blocking reads in supervised same-binary workers, cut decisions without waiting for them, record unreaped descendants, and never claim a universal process-exit bound. |

The finalized visual spine is also binding, not decorative: it declares the UX
pair canonical, requires partial truth and exact state words to survive every
theme, and forbids visual treatment from renaming or hiding a state
(`_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/DESIGN.md:118-149`).
Its Provider detail puts truncation/redaction notices before separately labeled
stdout and stderr, its confirmation dialog shows the verification limit, and
operation status renders exactly one terminal outcome
(`_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/DESIGN.md:246-279`).
The architecture must therefore expose capture, deadline, verification, and
provenance values in the view model; widgets may not infer them.

### Live-to-target deviations that require ledger entries

The architecture should predeclare, not discover during implementation, these
required deviations:

- silent Collector failure becomes scoped diagnostics and obligation-aware
  completeness (`srvls:31-36` versus `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:303-328`);
- eligible bare invocation changes from table to TUI, while redirection retains
  table (`srvls:359-360` versus `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:491-499`);
- external fzf becomes a deprecated alias and `--fzf-lines` is removed
  (`srvls:317-358` versus `_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md:256-278`);
- unsafe option-like identifiers, terminal controls, Markdown delimiters, and
  Prometheus labels gain typed delimiting/sanitization/escaping
  (`docs/architecture.md:102-109`; `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:714-716`);
- previously unbounded or only line/column-bounded capture receives byte caps
  for Collector streams, direct reads, and inspection
  (`srvls:31-36`, `srvls:67-79`, `srvls:279-313`;
  `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:330-337`);
- live cron commands each receive 15 seconds, systemd receives three independent
  15-second subprocess budgets, and Docker receives 20 plus 30 seconds; target
  Collectors instead share one scope budget and a queued-generation cut, so
  timeout and partial-failure results deliberately change (`srvls:31-36`,
  `srvls:89-153`);
- live actions are unbounded and inherit child streams; target actions gain
  Provider-specific execution, verification, capture, and total-operation
  bounds (`srvls:267-276`);
- TUI system mutation changes from possible interactive `sudo` to `sudo -n`,
  while explicit legacy non-TUI actions retain interactive behavior
  (`srvls:255-276`; `_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:129-133`);
- command exit is no longer reported as verified success; action outcomes use
  fresh postcondition evidence (`srvls:267-276`; `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:585-605`);
- help, unknown-option, bad-arity, stdout/stderr, and exit behavior must either
  be emulated or deliberately versioned because clap defaults differ from the
  live router (`srvls:338-360`).

The target dispatcher must run on raw argv **before** clap or legacy membership
tests. Its exact first-match order is:

1. If argv[1] is `brief`, `promise`, `config`, or `action`, dispatch the entire
   tail to that canonical namespace. A legacy-looking flag later in the tail is
   owned by that namespace and can never select inventory output.
2. If argv[1] is `inspect` and argv[2] is exactly `--id`, dispatch to canonical
   inspect. Missing canonical values and all later parse errors are canonical
   errors and perform no legacy collection.
3. If argv[1] is `inspect`, `start`, `stop`, `restart`, or `disable`, dispatch to
   the legacy action router. It preserves the current exact-three-argument
   arity check, stdout/stderr placement, and exit behavior, including bad
   `inspect` shapes.
4. Every other argv shape, including empty argv, `--help`, an unknown first
   word, or a flag first, selects the legacy inventory profile. Only then are
   `--json`, `--prom`, `--md`, `--fzf-lines`, and `--fzf` tested by membership
   anywhere in argv in that order.

Consequently `srvls config validate --json` is canonical configuration JSON;
`srvls --json config validate` is legacy inventory JSON with ignored extra
words; `srvls inspect bogus name` is the live successful-empty legacy case; and
`srvls inspect --id X --linear` is canonical. Namespace words are reserved only
in argv[1]. This changes today's “unknown first word plus `--json` means
inventory JSON” behavior for the four reserved words and therefore needs
version impact and consumer disposition, not merely a clap unit test
(`srvls:338-360`;
`_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:339-349`).

## Recommended architecture-owned operational envelope

### Configuration and provenance contract

**RECOMMENDED:** one typed `PolicyValue<T>` owns every configurable field:

```text
effective value
units
winning source
overridden source chain
built-in default
valid range or allowed set
```

Source precedence is fixed, lowest to highest: compiled defaults,
`/etc/srvls/config.toml`, the XDG user file, one explicit `--config PATH`,
`SRVLS_` environment values, then repeatable CLI `--set key=value` values.
Dotted TOML names are canonical. Environment names uppercase path components
and join them with `__`; for example,
`SRVLS_COLLECTION__MAX_CONCURRENCY`. The released binary never implicitly reads
a repository `.env`. The current mise hook prepends project paths and
materializes `.env` (`mise.toml:4-18`), so executable resolution and environment
provenance remain trust boundaries rather than application defaults.

Every discovered source is parsed and schema-validated independently before
merge. A malformed or out-of-range lower-precedence value still fails; a later
valid override cannot hide it. Unknown keys, duplicate semantic keys, invalid
types, duplicate assignments within one source, and values outside the
inclusive ranges below fail before collection, durable writes, TUI raw mode,
or Host mutation. Values are rejected, never clamped. v1 reads one immutable
configuration snapshot at process start and does not hot-reload, matching
`_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md:114-136`.

Snapshots, Findings, Accepted Baselines, action plans, and operations retain
the complete effective policy values, winning and overridden provenance chain,
and one deterministic policy fingerprint. Historical truth is interpreted
under that retained policy rather than whichever configuration happens to be
current later.

### Numeric defaults and valid ranges

Every row below is **RECOMMENDED**. Live measurements justify scale; they do not
silently redefine the contract. Ranges are inclusive.

| Policy | Default | Valid range and invariant |
| --- | ---: | --- |
| `collection.max_concurrency` | 4 workers | 1–8 |
| `collection.deadline.cron_user`, `.cron_root`, `.cron_system` | 10 s each | 1–60 s each; one budget covers the scope's file and command work |
| `collection.deadline.systemd_system`, `.systemd_user` | 15 s each | 1–60 s each; one budget covers all sub-operations in that scope |
| `collection.deadline.docker` | 30 s | 1–60 s; enumeration and inspect share the scope budget |
| `collection.deadline.pm2` | 20 s | 1–60 s; fixtures own the absent-on-review-Host case |
| `collection.deadline.process` | 10 s | 1–60 s; includes supervised `/proc` work |
| `collection.scheduler_margin` | 5 s | 0–30 s |
| `collection.generation_cutoff` | 40 s | 10–120 s and at least exact LPT makespan plus scheduler margin |
| `process.child_stdout_bytes` | 4 MiB | 64 KiB–16 MiB |
| `process.child_stderr_bytes` | 256 KiB | 16 KiB–1 MiB |
| `process.scope_stdout_bytes` | 8 MiB | 64 KiB–64 MiB and at least the child stdout cap |
| `process.scope_stderr_bytes` | 512 KiB | 16 KiB–4 MiB and at least the child stderr cap |
| `process.generation_stdout_bytes` | 32 MiB | 256 KiB–256 MiB and at least `max_concurrency * child_stdout_bytes` |
| `process.generation_stderr_bytes` | 2 MiB | 64 KiB–16 MiB and at least `max_concurrency * child_stderr_bytes` |
| `inspection.max_lines`, `inspection.max_bytes` | 200 lines, 256 KiB | 10–2,000 lines and 4 KiB–2 MiB; the earlier bound wins and is disclosed |
| `retention.snapshot_days`, `retention.snapshot_count` | 14 d, 256 historical | 2–90 d and 16–4,096; both limits apply |
| `retention.event_days`, `retention.events_per_promise` | 90 d, 50,000 | 30–365 d and 1,000–1,000,000 |
| `retention.promise_count`, `retention.operation_count` | 10,000 each | 100–100,000 Promises and 100–1,000,000 operations |
| `retention.lifecycle_event_count` | 1,000,000 | 10,000–10,000,000 global events |
| `state.byte_ceiling` | 512 MiB | 64 MiB–8 GiB |
| `state.busy_timeout` | 5 s | 100 ms–30 s |
| `lease.default_duration` | 12 h | 5 min–30 d |
| `heartbeat.default_cadence` | 5 min | 10 s–1 h |
| `heartbeat.grace` | 5 min | 30 s–30 min; never extends Lease expiry |
| `stale.no_use_window` | 24 h | 5 min–30 d; unsupported activity evidence cannot produce `stale` |
| `hot.cpu_percent`, `hot.memory_percent` | 80%, 25% | 1–100% each |
| `hot.sample_count`, `hot.window` | 3 samples, 2 min | 1–12 samples and 1 min–1 h; insufficient samples produce no `hot` claim |
| `action.max_concurrency` | 4 operations | 1–16 and separate from collection workers |
| `action.plan_ttl` | 5 min | 10 s–30 min |
| `action.revalidation_deadline` | 5 s | 1–15 s |
| `action.execution.systemd` | 100 s | 5–600 s; exceeds the live system and user manager 90 s defaults |
| `action.execution.docker` | 45 s | 5–300 s |
| `action.execution.pm2` | 30 s | 5–300 s |
| `action.execution.process` | 10 s | 1–60 s |
| `action.execution.launch_mechanism` | 120 s | 5–600 s |
| `action.verification_window`, `action.poll_interval` | 30 s, 500 ms | 5–120 s and 100–2,000 ms |
| `action.finalization_deadline` | 5 s | 1–30 s |
| `action.graceful_termination`, `action.forced_observation` | 2 s, 1 s | 100 ms–10 s and 100 ms–5 s; neither promises reap of Linux D-state work |

The fixed v1 scope jobs have default budgets
`[30, 20, 15, 15, 10, 10, 10, 10]`. The scheduler sorts by descending budget,
then canonical scope ID, and assigns each job to the earliest available worker,
breaking worker ties by worker ID. On four workers the exact simulated makespan
is 35 seconds; the five-second margin therefore yields the 40-second generation
decision cutoff. Validation simulates this same queue-aware LPT algorithm for
the effective values. It rejects any cutoff below the resulting makespan plus
margin and `config explain` prints the ordered jobs, worker lanes, makespan,
margin, and cutoff.

At the cutoff, the reducer stops waiting, synthesizes terminal `timed-out`
reports for unfinished scopes, and may persist the incomplete candidate
Snapshot. The UI still acknowledges refresh within 100 ms and discloses slow
Collectors at two seconds
(`_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md:563-570`).
The cutoff is a bounded truth decision, not an impossible claim that every
kernel-blocked child has exited.

### Capture, timeout, and cancellation semantics

The numeric fields are insufficient without one shared process contract:

1. Every potentially blocking Provider command, `/etc` read, and `/proc` walk
   runs as a supervised worker mode of the same `srvls` binary. Workers accept
   typed input and emit one versioned typed result; they never create a second
   daemon or runtime architecture.
2. Before spawn, `CommandRunner` reserves stdout and stderr independently
   against the child, owning scope, and generation ledgers. Reservation order
   is generation, scope, child under one coordinator lock. Insufficient
   aggregate capacity deterministically refuses the later canonical scope or
   truncates only to its remaining reservation and emits a diagnostic; it can
   never borrow from the other stream.
3. Spawn uses argv only, with an Adapter-owned executable policy, environment
   allowlist, working directory, and new process group. Stdout and stderr drain
   concurrently. Bytes beyond a retained reservation are counted and discarded
   while draining so a full pipe cannot deadlock the child.
4. The total result is `SpawnFailed(kind) | Exited(code) |
   Signaled(signal) | TimedOut` plus bounded stdout and stderr, original byte
   counts, independent truncation flags, duration, and redacted argv identity.
   Nonzero exit and signals are values interpreted by the Adapter.
5. Typed normalization consumes the retained raw streams, records lossy decode
   and truncation metadata, and immediately frees raw buffers and releases
   reservations. Invalid or truncated structured Collector stdout reduces to
   `invalid-output`; it can never become complete evidence.
6. At a deadline the parent makes its truth decision without waiting for
   unbounded Host I/O. It requests process-group termination, observes the
   configured graceful interval, sends forced termination, and observes the
   configured forced interval. An exited child is reaped synchronously. A child
   still blocked in Linux uninterruptible I/O is registered with a bounded
   eventual reaper, remains an explicit diagnostic, and cannot later join the
   expired generation. No wall-clock contract promises that such a child has
   exited or been reaped.
7. User navigation, dropped delivery, or a newer refresh suppresses stale
   delivery but is not cancellation. A typed generation or operation owns its
   cancellation capability and truthful terminal record through persistence.

These rules close the gap previously identified in
`_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/reviews/review-version-operations.md:45-64` and implement the feasible portion of
the canonical bounded-refresh requirement
(`_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:710-712`).

### Durable SQLite and crash recovery

One SQLite database below `$XDG_STATE_HOME/srvls`, defaulting to
`~/.local/state/srvls`, is the sole durable truth owner. Its directory is mode
0700 and database, WAL, shared-memory, backup, and lock files are mode 0600.
Every connection enables foreign keys, uses WAL, `synchronous=FULL`, and the
configured busy timeout. Schema changes are embedded forward migrations under
an exclusive state lock with a verified pre-migration backup and integrity
check; no caller coordinates sidecar JSON files.

Repositories use `BEGIN IMMEDIATE` transactions and compare-and-swap revisions
for every current pointer. The atomic write units are:

- Promise lifecycle event plus current Promise projection;
- immutable Snapshot, diagnostics, scope reports, and current-Snapshot CAS;
- Accepted Baseline pointer plus acceptance or override audit event; and
- Operation phase, evidence, and its terminal outcome.

An action writes phases before crossing each irreversible boundary:
`planned -> launch-authorized -> executing -> verifying -> terminal`. Recovery
never auto-replays a Host mutation. `planned` without launch authorization can
close as refused with a recovery reason. Any recovered phase in which launch
may have occurred is conservatively closed as `executed-unverified` unless
fresh correlated evidence proves the canonical terminal outcome. The original
actor, idempotency key, target identity, policy fingerprint, phase times, and
evidence remain queryable.

### Retention and active-truth invariants

Age, per-owner count, global count, and byte limits all apply. Each family is
pruned oldest-first by canonical timestamp then stable ID inside a serialized
repository transaction. The transaction writes an audit watermark with family,
cutoff timestamp and ID, deleted count, bytes reclaimed, and policy
fingerprint. Pruning never races renewal, baseline acceptance, Snapshot commit,
or operation finalization.

The following truth is pinned even when an ordinary age or count limit would
otherwise remove it:

- the current Snapshot and Accepted Baseline plus their compatibility metadata;
- active Promise projections, the lifecycle evidence needed to derive them,
  and their latest Heartbeat;
- the latest closure summary for a closed Promise;
- a closed or expired Promise still required to explain a surviving Observation
  or current Reconciliation Finding;
- any Snapshot, plan, or evidence referenced by a nonterminal operation; and
- a terminal operation until its outcome and required evidence have passed
  every applicable retention bound.

After ordinary pruning, the state adapter enforces the global Promise,
operation, lifecycle-event, and byte ceilings. If pinned truth alone prevents
compliance, it records a capacity diagnostic and refuses new durable growth or
Host mutation before corrupting, deleting, or silently rewriting pinned truth.
Read-only stateless compatibility output remains available. Capacity recovery
and deterministic compaction remain permitted.

Snapshot production is an explicit surface contract:

| Surface | Durable effect |
| --- | --- |
| Eligible bare TUI, `--tui`, or deprecated `--fzf` alias; initial load and `r` refresh | Commit a candidate Snapshot and CAS the current pointer after full reduction. |
| `srvls brief --linear` and its canonical `--json` equivalent | Collect, reconcile, commit a candidate Snapshot, then render that exact Snapshot. |
| TUI `b` or the deterministic `baseline` command | Move only the Accepted Baseline pointer to an eligible existing current Snapshot and write an audit event. |
| Canonical `action execute` verification | Persist the Operation; a fresh targeted Snapshot may replace current truth only if its generation is still latest. |
| Promise lifecycle commands | Persist Promise events and projections, but do not create Snapshots. |
| Canonical inspect, action plan/status, and config validate/explain | Read state or configuration without creating a Snapshot. |
| Legacy table, top-level `--json`, `--prom`, `--md`, legacy inspection, and explicit legacy action verbs | Remain stateless compatibility lanes. |

This keeps the five-minute metrics timer from creating unbounded Snapshot
history while protecting existing automation described at `README.md:108-151`.

### Action bounds and outcome mapping

The action pool admits at most `action.max_concurrency` operations and is
independent of collection. A SQLite partial unique constraint plus an in-memory
exact-target lock permits only one nonterminal operation per Provider identity.
The tuple actor, idempotency key, operation kind, and exact target returns the
original plan, operation, or terminal result on retry. A different submission
for a locked target is refused as `duplicate-operation`; saturation is refused
before Provider launch rather than entering an unbounded queue.

A plan binds its source generation, exact target and birth evidence, operation,
effective policy fingerprint, safety assessment, actor, and expiration. The
five-minute default TTL is shortened by any newer source generation, identity
change, or policy change. Expiry requires replan and reconfirmation. Execution
then performs bounded identity and capability revalidation before persisting
`launch-authorized`; only that phase may cross the Provider launch boundary.

The total decision bound is derived, never independently guessed:

```text
revalidation
+ selected Provider execution
+ verification window
+ graceful termination observation
+ forced termination observation
+ durable finalization
```

The default totals are 143 seconds for systemd, 88 for Docker, 73 for PM2, 53
for direct process, and 163 for a declared Launch Mechanism. Configuration
validation computes the selected formula and `config explain`, action plans,
confirmation, TUI status, linear output, and machine output expose it. A Linux
D-state descendant may outlive this decision bound under the eventual reaper;
the durable operation still reaches one truthful outcome and retains that
diagnostic.

Only evidence sampled after the recorded Provider launch boundary, correlated
to the OperationId, and matched to the exact target may prove verification.
Pre-launch or uncorrelated matching state never counts. Apply FR-40 in its exact
precedence:

1. `verified` when fresh post-action evidence proves the postcondition,
   regardless of command diagnostics;
2. `refused` when no Provider operation launched because confirmation,
   capability, authorization, duplicate-operation, capacity, plan expiry, or
   immediate identity revalidation failed;
3. `timed-out` when execution exceeded its Provider-specific deadline,
   termination was attempted, and the postcondition was not verified within the
   bounded operation;
4. `failed` when invocation could not start or fresh post-action evidence
   disproves the postcondition; otherwise
5. `executed-unverified` when launch occurred but evidence is incomplete or
   ambiguous, verification expires, or a replacement identity is observed.

This is the exact precedence at
`_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:595-605`.
Phase names are durable progress, not extra outcomes
(`_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md:354-374`).

## Rust bootstrap and early-CI implications

### Live toolchain and ABI facts

```text
$ rustc --version --verbose
rustc 1.95.0 (59807616e 2026-04-14)
host: x86_64-unknown-linux-gnu
LLVM version: 22.1.2

$ cargo --version
cargo 1.95.0 (f2d3ce0bd 2026-03-21)

$ print $RUSTUP_TOOLCHAIN
1.95.0

$ rustup run stable rustc --version
rustc 1.95.0 (59807616e 2026-04-14)

$ rustup check
stable-x86_64-unknown-linux-gnu - update available:
1.95.0 (59807616e 2026-04-14) -> 1.97.0 (2d8144b78 2026-07-07)

$ rustup run 1.88.0 rustc --version
error: toolchain '1.88.0-x86_64-unknown-linux-gnu' is not installed
exit 1

$ getconf GNU_LIBC_VERSION
glibc 2.42

$ ldd --version | head -n 1
ldd (Ubuntu GLIBC 2.42-0ubuntu3.1) 2.42
```

A trivial dynamically linked binary compiled by the local Rust 1.95.0
toolchain had maximum imported version `GLIBC_2.34`:

```text
$ print 'fn main() {}' | rustc - -o /tmp/srvls-zigzag-glibc-probe
$ readelf --version-info /tmp/srvls-zigzag-glibc-probe |
    rg -o 'GLIBC_[0-9.]+' | sort -Vu | tail -n 1
GLIBC_2.34
```

This does **not** prove the future dependency-complete release binary's ABI
floor. It proves that Host glibc version and imported-symbol floor are different
facts. AD-12's initial Host claim is confirmed at glibc 2.42, but release CI
must record the full binary's maximum imported `GLIBC_*` symbol and smoke it on
the declared Host baseline rather than infer compatibility from the build image
(`_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:111-115`).

The live crates.io sparse-index record returned:

```json
{"vers":"0.30.2","rust_version":"1.88.0","yanked":false}
```

Thus ratatui 0.30.2 and MSRV 1.88 remain internally consistent. Local Rust 1.95
cannot prove either 1.88 compatibility or the current-stable lane: rustup reports
1.97.0 is available. No 1.88 toolchain, manifest, lockfile, Rust source, or CI
workflow currently exists.

A live crates.io API comparison against the spine's dependency table
(`_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:149-163`)
found every named crate pin still at the registry's maximum stable version except
clap: the spine pins 4.6.1, while crates.io reports 4.6.2. The sparse-index
record for 4.6.2 is non-yanked and declares Rust 1.85:

```json
{"vers":"4.6.2","rust_version":"1.85","yanked":false}
```

Because no manifest or lockfile exists, 4.6.1 is a planning pin rather than a
live resolution. Bootstrap should reselect 4.6.2 or explicitly retain 4.6.1,
then make the committed lockfile the reviewed resolution.

### Required bootstrap slice

The readiness report correctly found that Story 1.2 assumes a Rust crate that
no earlier story creates (`_bmad-output/planning-artifacts/implementation-readiness-report-2026-07-15.md:160-168`;
`_bmad-output/planning-artifacts/epics.md:202-215`). The addendum makes correction mandatory before Provider
implementation (`_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/addendum.md:23-28`).

Insert a bootstrap story after compatibility capture and before any Rust
Collector:

1. Create one Rust 2024 binary crate named `srvls` with
   `package.rust-version = "1.88"`.
2. Create private-by-default `domain`, `application`, `ports`, `adapters`,
   `presentation`, `cli`, `state`, `config`, and composition-root modules.
3. Commit `Cargo.lock` and make every CI build/test command use `--locked`.
4. Add a no-Host test harness, fake Clock/BootIdentity/CommandRunner/StateStore,
   and one composition smoke that performs no Host mutation.
5. Install exact Rust 1.88 in CI and fetch a separate current-stable lane. The
   installed local stable channel is stale at 1.95 and is neither proof.
6. Run formatting, locked clippy on all targets with warnings denied, locked
   tests on all targets, and an architecture-boundary check before merging any
   Provider.
7. Keep release tarball, checksum, `readelf`, install, and rollback checks in
   the release epic, but do not defer MSRV/current/lock/test enforcement there.

Story 4.1 currently owns all those gates after three implementation epics
(`_bmad-output/planning-artifacts/epics.md:676-697`). That sequencing remains unsafe even though the PRD and UX
document-discovery gaps are now closed.

## Readiness-gap implications for the current stories

### The old readiness document is partly superseded

The July 15 report records PRD and UX as missing
(`_bmad-output/planning-artifacts/implementation-readiness-report-2026-07-15.md:9-15`). Those two discovery
blockers are resolved by the finalized July 16 PRD/addendum and UX spine pair.

The current epic artifact has not consumed them. Its frontmatter names only the
Python-era sources and old architecture (`_bmad-output/planning-artifacts/epics.md:1-13`), and it still defines
18 legacy FRs, 10 NFRs, and eight candidate UX-DRs
(`_bmad-output/planning-artifacts/epics.md:21-113`). The canonical product has 43 FRs and 16 NFRs. Runtime
Promise lifecycle, direct processes, reconciliation, Brief/baseline,
configuration, durable state, linear/Agent surfaces, and lifecycle retention
are not merely missing acceptance criteria; they require new epic structure.

Implementation readiness therefore remains **NOT READY** for full Phase 4, but
for a different immediate reason than document absence: architecture and epics
have not been reconciled to the now-final sources.

### Explicit TUI Start interaction

The old gap at
`_bmad-output/planning-artifacts/implementation-readiness-report-2026-07-15.md:170-172` is now canonically
closed:

- `a` opens the contextual Action Menu;
- Start appears on an active Runtime Promise when its Launch Mechanism resolves
  an exact supported target, even with no Observation;
- there is no direct Start shortcut;
- `s`, `R`, and `x` remain accelerators for exact current Observations and enter
  the same plan path;
- safe nondestructive Start can proceed from the plan with Enter unless
  privilege or policy introduces uncertainty.

Evidence is at `_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md:536-556` and `_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md:303-339`. The old architecture
key map (`_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md:147`), Story 3.1's Entry-only planner
(`_bmad-output/planning-artifacts/epics.md:512-536`), and Story 3.5's direct-only acceptance criteria
(`_bmad-output/planning-artifacts/epics.md:616-644`) must be revised to match.

### Story 1.6 is still too broad

Story 1.6 combines:

- process spawn/result semantics;
- stdout/stderr draining and caps;
- deadlines, process-group cancellation, termination, and reaping;
- worker-pool scheduling;
- generation cuts and late-result rejection;
- Collector outcome and Collection Obligation reduction;
- deterministic compatibility merge order; and
- strict-mode exit/presentation policy
  (`_bmad-output/planning-artifacts/epics.md:291-312`).

Split it into at least:

1. **Total bounded CommandRunner:** total `ProcessResult`, stream caps,
   lossy-decoding metadata, process groups, deadline/cancel/kill/reap, fake
   clock/process tests, and the envelope in this report.
2. **Concurrent collection and evidence policy:** eight scope jobs, bounded
   scheduling, per-scope deadlines and obligations, dynamic Promise promotion,
   shared outcome reduction, generation cut, deterministic bucket/ordinal
   assembly, aggregate deadline, and strict-mode mapping.

Configuration schema/provenance and durable Snapshot commit should be their own
bootstrap/state stories rather than being smuggled into either split. The
readiness report's original split recommendation remains valid
(`_bmad-output/planning-artifacts/implementation-readiness-report-2026-07-15.md:174-176`), and canonical
Promise-driven obligations make the orchestration half larger, not smaller.

### Story 3.5 is still too broad and now semantically stale

Story 3.5 currently combines shortcut handling, confirmation, duplicate
suppression, operation identity, refresh races, verification, and outcome
rendering. It also names `Stale` as a terminal outcome and omits `timed-out`
(`_bmad-output/planning-artifacts/epics.md:616-644`), contradicting the canonical five-outcome algebra.

Split it into:

1. **Action discovery, planning, and confirmation:** `a` Action Menu,
   Promise-originated Start, direct accelerators, exact identity/generation,
   Safe-to-stop recalculation, disabled reasons, Cancel-first focus, unknown
   acknowledgement, and one captured plan.
2. **Durable operation execution and shutdown:** idempotent operation ID,
   duplicate suppression, provider-scoped privilege, pre-execution
   revalidation, independent operation lane, phase-specific Ctrl-C/SIGINT/
   SIGTERM handling, bounded termination attempts, eventual-reaper diagnostics,
   and outcome-before-exit persistence.
3. **Verification and outcome presentation:** Provider postconditions,
   bounded verification, race isolation, canonical precedence, TUI/linear/JSON
   rendering, durable `action status` lookup, and no optimistic row mutation.

Provider-specific systemd, Docker, and PM2 stories can continue to own native
argv and postconditions, but the canonical PRD also requires a direct-process
action story and Promise-only Start target resolution. The readiness report's
original concern at
`_bmad-output/planning-artifacts/implementation-readiness-report-2026-07-15.md:178-180` is therefore still
open.

## Architecture amendment checklist

No canonical file was edited in this review. Before implementation readiness is
re-run, the architecture owner should:

- bind the finalized PRD/addendum and UX spines as sources;
- retain the paradigm while replacing Entry-only scope with Promise,
  Observation, collection, reconciliation, baseline, state, config, and
  operation boundaries;
- add StateStore, Clock, BootIdentity, ConfigSource, process Provider, and
  lifecycle/audit ports;
- adopt or explicitly revise every numeric envelope value above;
- replace the Collector outcome/obligation and Action Outcome algebras;
- bind canonical Brief ordering, Action Menu/baseline keys, linear/Agent
  surfaces, configuration provenance, and phase-specific signal behavior;
- enumerate required compatibility-ledger deviations before Rust parser or CLI
  implementation;
- split broad Stories 1.6 and 3.5 and add bootstrap/early-CI work;
- regenerate epics against canonical FR-1 through FR-43 and NFR-1 through
  NFR-16; and
- re-run implementation readiness against the live compatibility corpus,
  revised architecture, revised epics, and finalized UX.

## Final assessment

**Review: COMPLETE. Architecture paradigm: RATIFIED. Canonical operational
build substrate: ADOPTION REQUIRED.**

The live Python utility is healthy enough to capture: syntax and smoke gates
pass, the command and output surfaces are inspectable, and current Host timings
leave headroom for bounded collection. This report now supplies a complete,
internally consistent compatibility oracle and recommended operational
contract, including the Linux boundary that userspace cannot promise a timed
reap from uninterruptible I/O.

The report itself is complete. Implementation remains blocked until the
canonical architecture adopts or explicitly supersedes these defaults,
scheduling and capture invariants, SQLite transactions, retention bounds,
surface effects, and action lanes, and the story set is regenerated against
that amended spine.
