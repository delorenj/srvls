# Frozen architecture contract oracles

This directory is immutable input evidence for the architecture contracts at
parent commit `598eb0ccd0ad37a9432a2132a14d75aeea0f9f47`. It is intentionally
independent of the future Rust implementation and must never be refreshed from
an encoder under test.

The byte fixtures were transcribed from AD-10, AD-13, AD-24, and AD-25 and
cross-checked with Python 3 standard-library primitives plus `sha256sum`. Raw
logical inputs, complete expected bytes, canonical JSON preimages, domain
separators, and final hashes are all checked in. `manifest.sha256` pins every
oracle and validator file except itself.

Canonical JSON `*.json` files use one repository LF as a text-file terminator;
that terminator is not part of CanonicalJsonV1. The validator removes exactly
one LF before byte comparison and hashing, rejects CRLF or multiple trailing
LFs, and checks the stored presentation file itself through `manifest.sha256`.

Corpus ownership:

- `policy-snapshot-v1/` freezes the complete default PolicySnapshotV1.
- `collection-plan-v1/` freezes both the original minimal plan and a complete
  nonempty baseline/history/promotion plan plus its prior SnapshotV1.
- `observation-id-v1/` starts from raw cron, PM2, and process hash inputs and
  freezes all five Provider identities.
- `provider-scope-input-v1/` freezes a nonempty nested binary assignment for
  every Provider, including empty and non-UTF-8 raw values.
- `ipc-v1/complete-exchange/` freezes all four frame schemas and every Provider
  detail variant.
- `ipc-v1/preallocation-timeout/` freezes the constructible no-child timeout
  whose request ID is tagged absent.

Run `python3 tests/fixtures/contracts/validate.py`. Validation is read-only: it
does not rewrite, recapture, or accept updated goldens.
