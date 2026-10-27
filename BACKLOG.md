# Backlog

## Adoption on existing code

For a project that has code; the first increment assumes none. Prototype on a
real messy project before writing it into the skills.

- Start from an empty specification; derive `technical.md` from the
  project, reviewed by the human. Never specify the whole code at once:
  an agent cannot tell intended from accidental behavior.
- The specification grows zone by zone, with the increments that touch
  each zone; the rest is "unspecified, as is" (refinement).
- Characterization tests (golden master) protect untouched zones, kept
  visibly apart from tests that express the specification.
- The human states principles that hold; the agent looks for
  counterexamples in code and tests: a bug (backlog), or an exception
  the human specifies or leaves unspecified. Back important rules with
  an executable check (e.g. property-based tests).
