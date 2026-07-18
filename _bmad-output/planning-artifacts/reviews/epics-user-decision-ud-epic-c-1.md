---
decisionId: UD-EPIC-C-1
date: 2026-07-17
status: accepted
authority: user-checkpoint
artifact: _bmad-output/planning-artifacts/epics.md
---

# UD-EPIC-C-1: Canonical backlog seam closure

At the create-epics-and-stories requirements checkpoint, the user selected
option `C` and stated: “requirements confirmed complete and correct. Continue
through the remaining sequential workflow checkpoints under the explicit
authorization in the mission prompt.”

The mission prompt required the canonical backlog to close Runtime Promise,
Lease, reconciliation, abandoned-runtime, Safe-to-stop, and action seams rather
than leave implementation alternatives. The accepted consequence is:

1. Persistent intent missing either Durable Ownership or an inspectable Launch
   Mechanism is rejected with no write (`lease_prerequisite_missing`, exit 2).
2. Duplicate truth is an unordered member set plus excess cardinality. It never
   selects an “excess instance” or grants Safe-to-stop from membership alone.

This record preserves the post-source decision used by Contract C-15 and C-17.
It does not alter the general PRD/addendum/UX/architecture precedence chain.

## Source pins

- Architecture integration base: `ac298ad`.
- Batch-5 reviewed canonical predecessor digest:
  `7d749899972903b90c76df2825bfbfaf0055e0f83544cd72cb7d648af8ad645c`.
- User checkpoint date and repository timezone: 2026-07-17,
  America/New_York.
