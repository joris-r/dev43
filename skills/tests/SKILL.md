---
name: tests
description: Dev43 Tests phase of an increment. Use when spec/STATE.md says Phase is Tests. Writes tests, each citing what it checks in the specification, before any implementation.
---

# Tests

Load `dev43:core` first if it is not loaded.

Goal: a test suite that faithfully expresses the change specification.
Tests are written before the implementation and will be read-only
during it.

## Exploration

1. Read the change specification and the test and quality policy in
   `spec/main/technical.md`.
2. Discuss with the human: what to test, at which level. Edge cases are
   settled here, by tests: raise one only when a test cannot choose.
3. If the change brings new test or quality needs, propose an update
   of the policy; once the human agrees, write it in the change page.
4. Flag rules that cannot be tested; propose to make them testable
   or to accept them as not testable. Mark each accepted one
   "(not testable)" in the change page. If only part of a rule is not
   testable, name that part, e.g. "(interrupted write not testable)".

One point per message; raise only what you cannot settle with
confidence, and settle the rest yourself in Production (see
`dev43:core`, Working with the human).

When you have nothing left to raise, propose to end Exploration. It
ends on `next`; then set Step to Production in STATE.

## Production

Work without interrupting.

- Each test cites what it checks: a name from the specification (in
  the test name or its grouping) or a rule ID.
- Every example and every testable rule of the change has at least one
  test.
- Update or delete existing tests that check something the change
  modifies or removes; find them by searching the tests for the names
  and rule IDs it modifies or removes.
- Tests must fail for the right reason before implementation (missing
  behavior, not syntax or setup errors). Run them to confirm. On a
  return from Implementation, this applies only to new or changed
  tests.
- A new test that already passes must not be vacuous (e.g. a loop
  over elements that do not exist yet): it is a negative check (e.g.
  "does not show X"), or behavior the existing code already meets.
  Name each in your hand-over and say why it passes.
- Write only the minimum non-test code needed for tests to compile
  (stubs, signatures), and tag it if it fixes an interface. If the
  project has no code yet, also set up the project and the test
  tooling, as the technical part of the change page says.

Tag the choices you are unsure of. Run the Verification checks and
fix what fails. Then set Step to Verification in STATE, and hand over with the check results and the
list of tags, with one line on each saying why.

## Verification

Starts at your hand-over, once the checks below pass.

1. The human reviews the changes (`git diff`), staging each file or
   hunk once read, and rules on each tag or edits the artifacts
   directly.
2. Apply the rulings, remove the tags, and run the checks again. The
   review is done when all changes are staged, new files included.

Checks:

- Every new or modified rule ID of the change is cited by a test,
  unless marked "(not testable)" (search ignoring case and separators).
- Every rule ID cited in tests exists in `spec/main/` or the change
  page.
- The new tests fail for the right reason (missing behavior, not syntax
  or setup errors), or already pass and are named in the hand-over.
  In the `tests-only` shape, instead: the full test suite and the
  checks of the test and quality policy pass.

The human's review deserves particular care: checking behavior through
tests is cheaper than through code. Does each part of the change have
tests, and does each test truly express it?

## Exit

Checks pass, no tags remain and the human approves the suite. Next
phase: the next one of the Shape. From now on, tests are read-only.

On `next`, set Phase to the next phase and Step to
Exploration in STATE; then stage all changes and
commit them as `[<increment>] Tests`.
