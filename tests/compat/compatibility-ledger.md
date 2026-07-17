# Legacy compatibility ledger

## COMPAT-0001 — Initial frozen Python oracle

- **Status:** frozen
- **Effective date:** 2026-07-17
- **Legacy behavior version:** Python baseline v1
- **Frozen parent:**
  `598eb0ccd0ad37a9432a2132a14d75aeea0f9f47`
- **Source origin:**
  `63757c542176e37d89eb3a2a8eef18e9fb2785e1`
  (`feat: establish srvls baseline`, 2026-07-14)
- **Git blob:** `aebb996d1341fc44afe513126ca6553815faa904`
- **Source SHA-256:**
  `06a7e312fba5f2ca03e99181cc208d7abd9ac4688f26ea0f8c89ee19eb9e8b62`
- **Rationale:** create the missing immutable AD-9 oracle before the Rust
  implementation exists, so independently built presenters cannot bless their
  own output.
- **Version impact:** none. This entry records existing Python behavior and does
  not approve a new top-level legacy output.
- **Replacement assertion:** the five fixed `golden/*.oracle.json` files and
  their `SHA256SUMS` entries replace Host recapture as compatibility evidence.

### Frozen behavior notes

- Provider merge order is cron, system systemd, user systemd, Docker, then PM2.
  Encounter order survives in table, JSON, and fzf-lines. Markdown alone sorts
  by type and then name. Prometheus aggregate keys sort by type/state.
- Output flag priority is membership-based and independent of argv order:
  JSON, Prometheus, Markdown, fzf-lines, fzf, then table. `--help` and unknown
  arguments are not special; without a known output flag they render a table.
- Unknown inspection succeeds with no output. Bad action arity exits 1 and puts
  usage on stderr. Cron and unknown action refusals put text on stdout and exit
  1. Child action output inherits stdout/stderr.
- Missing, denied, and timed-out commands collapse to successful-empty Provider
  input through the Python `run()` helper. Malformed systemd/PM2 JSON also
  collapses to empty. Wrong-shaped decoded objects can escape as an exception.
  A denied `/etc/crontab` open also escapes; denied `/etc/cron.d/*` entries are
  skipped.
- Missing Docker is silent. Absent PM2 is detected with `which` and silent.
  Missing fzf exits 1 with `fzf not installed` on stderr.
- Docker inspection always prints its recent-log separator. Docker log stderr
  is appended after stdout and lines are truncated to 200 columns. Other
  inspection stderr is dropped; systemd/PM2 output is limited to 30 lines.
- Hostile identifiers remain one typed argv element, preventing shell
  evaluation. Legacy table, Markdown, fzf-lines, and Prometheus surfaces retain
  their historical escaping defects; the oracle records the bytes rather than
  silently repairing them.
- Empty fzf-lines and unknown inspection are exact zero-byte stdout cases.
- Direct-process Observations have no Python Provider and remain excluded from
  all legacy presenters until a future ledgered decision says otherwise.

All clock, local-time rendering, load, identity/path, tool-result, source-path,
and traceback substitutions are exhaustive in `manifest.json`. No other value
was normalized.

### Consumer disposition

| Consumer | Frozen surface | Disposition |
| --- | --- | --- |
| `srvls-metrics.service` | `--prom` | Preserve `output.prometheus`; the currently broken forwarding path is deployment state, not permission to change metrics bytes. |
| `srvls-snapshot.service` | `--md` | Preserve `output.markdown`; only the declared UTC-now substitution replaces the capture timestamp. |
| Legacy fzf preview | `inspect` | Preserve exact typed preview argv, successful-empty behavior, line/column truncation, and Docker stderr merge. |
| Legacy fzf actions | `stop`, `restart`, `disable` | Preserve exact typed argv and Docker/PM2 disable translation. |
| Human CLI users | table, help, errors | Preserve ordering, summary bytes, unknown/help fallback, arity channels, and return codes. |
| Script consumers | `--json`, `--fzf-lines` | Preserve flat `EntryV1` order, keys, JSON formatting, and exact empty output. |

### Coverage evidence

| AD-9 edge | Fixture |
| --- | --- |
| Provider success/malformed/unavailable/denied/timeout | `fixtures/provider-matrix.json` |
| Wrong-shaped structured data | `fixtures/provider-matrix.json` |
| Table/JSON/Prometheus/Markdown/fzf-lines, order, escaping | `fixtures/output-matrix.json` |
| Flag precedence, help, unknown argv, arity, absent fzf | `fixtures/cli-matrix.json` |
| Empty inspection and stdout/stderr placement | `fixtures/cli-matrix.json` |
| Inspection argv, truncation, missing tools, Docker log merge | `fixtures/inspect-matrix.json` |
| Every action/type argv and hostile target identity | `fixtures/action-matrix.json` |

## Required fields for a future entry

Every change must state rationale, old and new behavior versions, affected
fixture/golden hashes, replacement assertion, migration or compatibility
window, and disposition for each named consumer above. A candidate generated
by the implementation under test is never acceptable evidence.
