---
name: tests
description: Dev43 Tests phase of an increment. Use when the plan of the increment reaches the Tests phase. Writes tests, each citing the paths it checks in the specification, before any implementation.
---

# Tests

Load `dev43:core` first if it is not loaded.

Goal: a test suite that faithfully expresses the change of the
specification (see `dev43:core`, Specification). Tests are written
before the implementation and are read-only during it.

## Exploration

1. Read the change and the test and quality policy in
   `docs/technical.md`.
2. Decide what to test, and at which level. Edge cases are settled
   here, by tests.
3. Raise to the human only what the specification must settle: an
   edge case no test can choose, a statement that cannot be tested, a
   new test or quality need for the policy. Each one is a change of
   the specification (see `dev43:core`, Specification); a statement
   accepted as not testable ends with `(not testable)`.

## Production

Work without interrupting.

- Each test cites, in a comment, the paths it checks. A scenario has
  one end-to-end test, citing its section path.
- Every tag and scenario added or changed by the change has a test.
- Update or delete the existing tests that check something the change
  modifies or removes; find them by the paths they cite, and by the
  entry points whose behavior changes (e.g. a command, a route).
- New tests fail for the right reason before implementation (missing
  behavior, not syntax or setup errors). Run them to confirm. On a
  return from Implementation, this applies only to new or changed
  tests, and the wip code is in place: one may already pass because
  of it; name it in your hand-over.
- A new test that already passes is not vacuous (e.g. a loop over
  elements that do not exist yet): it is a negative check, or behavior
  the existing code already meets. Name each in your hand-over and say
  why it passes.
- In the `specify-existing` shape, instead of the two points above:
  every new test passes on the current code. A test that fails reveals
  a counterexample: tell the human. On a bug, the statement leaves the
  change, its test is deleted, and you propose an entry in
  `docs_future/BACKLOG.md` to fix it.
- Write only the minimum non-test code the tests need to compile
  (stubs, signatures); mark it if it fixes an interface. If the project
  has no code yet, also set up the project and the test tooling, as
  `docs/technical.md` says.

Mark the choices you are unsure of. Run the checks and fix what fails.
Then make the exit commit, after the agent checks where Verification
has a gate or a mark remains.

## Checks

Script: `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/check.py" tests`.

- [coverage] Every tag and every scenario has a test, or is marked
  `(not testable)`; every test path resolves.

Run:

- The new tests fail for the right reason, or already pass and are
  named in the hand-over. In the `tests-only` and `specify-existing`
  shapes, instead: the full test suite and the checks of the test and
  quality policy pass.

Agent checks, in a fresh context (see `dev43:core`, Agent checks), on
the tests added or changed by the increment:

- [faithful] Each new or changed test checks what its statement says.
- [cases] The test cases of each added or changed tag cover what it
  says.

## Exit

Checks pass and no marks remain. Next phase: the next one of the plan.
In the last phase, the human also approves at the final review (see
`dev43:core`, Final review); Next is `Pause`.
From now on, tests are read-only.

Commit as `[<increment>] Tests` (see `dev43:core`, Git).
