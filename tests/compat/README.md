# Frozen Python compatibility oracle

This directory is the executable AD-9 legacy oracle. It freezes observable
behavior from the Python `srvls` source at parent commit
`598eb0ccd0ad37a9432a2132a14d75aeea0f9f47`.

The source authority is the Git blob
`aebb996d1341fc44afe513126ca6553815faa904`, whose 13,388 bytes have SHA-256
`06a7e312fba5f2ca03e99181cc208d7abd9ac4688f26ea0f8c89ee19eb9e8b62`.
Replay reads that blob directly from Git. It never imports the working-tree
script or invokes a replacement implementation.

## Evidence layout

- `fixtures/*.json` specify virtual files, clocks, identities, tool presence,
  subprocess outcomes, CLI arguments, and direct legacy function calls.
- `golden/*.oracle.json` are fixed captured assertions. Each embeds the source
  pin, fixture hash, exact stdout/stderr, termination, return value, tool lookup,
  and child argv/outcome sequence.
- `manifest.json` records provenance, every volatile substitution, the five
  matrices, coverage, exclusions, named deployed consumers, and the exhaustive
  inherited-versus-approved-deviation disposition of all 94 cases.
- `compatibility-ledger.md` records version impact and consumer disposition.
- `SHA256SUMS` freezes every intentional oracle file except the hash list itself.
- `replay_oracle.py` renders the frozen reference and validates byte equality.
- `capture-baseline.sh` creates candidates only outside the repository.
- `validate.sh` performs offline, read-only validation.

The corpus covers Provider success, malformed input, unavailability, denial,
and timeout wherever the Python surface exposes the condition. It also covers
wrong-shaped structured data, merge/order behavior, table/JSON/Prometheus/
Markdown/fzf-lines bytes, flag precedence, help, unknown argv, bad arity,
successful-empty inspection, stdout/stderr placement, missing Docker, absent
PM2/fzf, inspection truncation and Docker log stderr merging, hostile
identifiers, exact fzf bindings, and every action/type argv mapping.

Direct-process collection is intentionally absent: the frozen Python program
has no such Provider and AD-9 keeps direct-process Observations off legacy
presenters. The manifest records this as an explicit unsupported legacy case.

The two named host-managed user-systemd consumers retain separate authorities:
this corpus owns their inherited `--prom` and `--md` output bytes, while
`release-transaction-v1/brownfield-consumer-pairs.json` owns their exact
normalized service/timer definitions, candidate rewrites, and rollback
direction. `replay_oracle.py` requires both anchors for metrics and Snapshot;
an output-only deployed-consumer row is invalid.

## Validation

Run:

```bash
bash tests/compat/validate.sh
```

Validation does four things without network or Host mutation:

1. resolves the frozen parent path to the pinned Git blob and checks its size
   and SHA-256;
2. checks every path in `SHA256SUMS` and rejects unhashed fixture/golden files;
3. replays every fixture in memory against only the frozen Python blob; and
4. compares the complete rendered bytes with the checked-in goldens.

A future Rust compatibility test consumes fixture inputs and assertions as
independent evidence. For the 90 `inherited` cases it compares against the
historical golden bytes. For the four `approved-deviation` cases it preserves
those historical bytes as provenance but applies the exact replacement
assertion in `manifest.json`. It must not call `capture-baseline.sh`, derive
expected values from its own presenters, or rewrite these files.

Those four replacement assertions are byte-total: COMPAT-0002 freezes exact
uppercase-percent stdout and stderr plus one numeric exit status. Predicate-only
help, diagnostic-token, generic nonempty, and generic nonzero assertions fail.

## Capture and change control

`capture-baseline.sh` refuses any output path inside the repository. It creates
an external candidate directory for deliberate review:

```bash
bash tests/compat/capture-baseline.sh /tmp/srvls-oracle-candidate-v2
```

Changing an assertion requires all of the following:

1. a manually reviewed reason for changing legacy behavior;
2. a new compatibility-ledger entry naming version impact, replacement
   assertion, and disposition for every affected consumer;
3. updated immutable provenance and file hashes; and
4. review of candidate bytes independently from the encoder under test.

Ordinary validation never captures, refreshes, or writes an assertion.
