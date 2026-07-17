# Provenance

- Frozen parent: `598eb0ccd0ad37a9432a2132a14d75aeea0f9f47`
- Parent architecture SHA-256:
  `5907c2f7da67378c6da60de0ed6374b9393d30b7945d271e6e261467ebce9392`
- Capture date: 2026-07-17
- Authoring method: hand-authored independent architecture oracle with
  synthetic, non-secret IDs, paths, timestamps, hashes, process identities,
  unit names, and D-Bus names
- Product encoder used: none
- Mutable Host capture used: none
- Volatile substitutions: none; every synthetic value is literal

Primary semantics were reality-checked against:

- Linux man-pages 6.18 `fcntl_locking(2)`: traditional process-associated
  `F_SETLK`/`F_SETLKW` locks, `[0,1)` byte range semantics, automatic release
  on owner termination, non-inheritance across `fork`, and owner-side close
  hazards.
- Linux man-pages 6.18 `fork(2)`: process-associated locks are not inherited;
  OFD and `flock` locks are inherited.
- systemd v257 `org.freedesktop.systemd1` XML: Manager `Subscribe()` enables
  most signals and JobNew/JobRemoved require subscription by at least one
  client.

The fixed SHA-256 domains are the literal ASCII token, one zero byte, then the
declared CanonicalJsonV1 preimage. `SHA256SUMS` covers repository file bytes,
including the single terminal line feed. The validator recalculates both
layers independently.
