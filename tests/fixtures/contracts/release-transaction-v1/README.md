# Release transaction v1 oracle

This directory is the independent fixed oracle for the AD-23 release authority.
It is assertion input, not output from a Rust or Python `srvls` encoder.

The seven `*.manifest.json` files are complete `UpgradeTransactionV1`
envelopes at these crash cuts:

- recovery-owner takeover with candidate validation pending;
- first-install prior absence with consumer removal pending;
- irreversible commit decision complete;
- KnownGood publication pending and complete;
- ready admission pending; and
- explicit rollback with restored ready admission pending.

`rollback-unavailable.result.json` freezes the no-transaction
FirstInstallAbsentV1 result. `admission-record-lock.trace.json` freezes shared
and exclusive stopped-child takeover. `manager-subscription.trace.json` freezes
the user-bus owner/match/Subscribe/baseline/trigger order and loss behavior.

Each JSON file is its exact canonical object plus one repository line feed.
The line feed is not part of CanonicalJsonV1 or any domain-separated checksum;
it is included in `SHA256SUMS`. The validator rejects any other whitespace,
key order, duplicate key, checksum, crash-cut state, trace order, or file hash.

Run:

```sh
python3 tests/fixtures/contracts/release-transaction-v1/validate_oracles.py
```

The validator uses only the Python standard library and imports no product
code. Do not refresh these fixtures from an implementation. A contract change
requires a reviewed new schema version and new immutable oracle set.
