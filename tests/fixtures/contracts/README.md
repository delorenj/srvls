# Frozen architecture contract oracles

This directory is immutable input evidence for the architecture contracts at
parent commit `598eb0ccd0ad37a9432a2132a14d75aeea0f9f47`. It is intentionally
independent of the future Rust implementation and must never be refreshed from
an encoder under test.

The byte fixtures were transcribed from AD-10, AD-13, AD-24, and AD-25 and
cross-checked with Python 3 standard-library primitives plus `sha256sum`.
`canonical_json_v1.py` is the shared normative implementation of AD-24: it
rejects short control escapes, floats and non-finite numbers, non-NFC strings,
surrogate or alternate Unicode escapes, null, duplicate keys, representation
whitespace/BOMs, and noncanonical uppercase-percent spellings. Both contract
validators execute its positive and negative vectors. Raw
logical inputs, complete expected bytes, canonical JSON preimages, domain
separators, and final hashes are all checked in. `manifest.sha256` pins every
non-release oracle and validator file except itself; the release-transaction
subcorpus is closed independently by its own `SHA256SUMS`.

Canonical JSON `*.json` files use one repository LF as a text-file terminator;
that terminator is not part of CanonicalJsonV1. The validator removes exactly
one LF before byte comparison and hashing, rejects CRLF or multiple trailing
LFs, and checks the stored presentation file itself through `manifest.sha256`.

Corpus ownership:

- `policy-snapshot-v1/` freezes the complete default PolicySnapshotV1.
- `collection-plan-v1/` freezes the original minimal plan, the distinct
  generation-0 plan that produced the prior SnapshotV1, and the complete
  generation-2 baseline/history/promotion plan that accepts that Snapshot.
- `observation-id-v1/` starts from raw cron, PM2, and process hash inputs and
  freezes all five Provider identities.
- `provider-scope-input-v1/` freezes a nonempty nested binary assignment for
  every Provider, including empty and non-UTF-8 raw values.
- `ipc-v1/complete-exchange/` freezes all four frame schemas and every Provider
  detail variant.
- `ipc-v1/preallocation-timeout/` freezes the constructible no-child timeout
  whose request ID is tagged absent.
- `release-transaction-v1/` independently closes its own inventory and freezes
  byte-complete, size-checked managed-consumer content for distinct target and
  prior generations; complete install/upgrade forward, owner-replay,
  FirstInstall-recovery, installed-prior recovery, and explicit-rollback
  predecessor chains; both admission and KnownGood variants; directional FD4
  request/result roles plus both forward result branches; the official
  stable-toolchain identity; both
  deployed brownfield consumer pairs and their directional source/candidate
  mapping; immutable installed rollback bundles; and temp-free live record-lock
  plus ActionExecutor handoff proofs.

Run `python3 tests/fixtures/contracts/validate.py`. Validation is read-only: it
does not rewrite, recapture, or accept updated goldens.
