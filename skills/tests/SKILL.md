---
name: tests
description: Dev-4-3 Tests phase of an increment. Use when spec/STATE.md says Phase is Tests. Writes tests, each citing what it checks in the specification, before any implementation.
---

# Tests

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
   "(not testable)" in the change page.

End when the human says Exploration is over; then set Step to
Production in STATE.

## Production

Work without interrupting.

- Each test cites what it checks: a name from the specification (in
  the test name or its grouping) or a rule ID.
- Every example and every testable rule of the change has at least one
  test.
- Update or delete existing tests that check something the change
  modifies or removes.
- Tests must fail for the right reason before implementation (missing
  behavior, not syntax or setup errors). Run them to confirm. On a
  return from Implementation, this applies only to new or changed
  tests.
- Write only the minimum non-test code needed for tests to compile
  (stubs, signatures), and tag it if it fixes an interface.

Tag every choice the spec does not dictate. Stage all changes
(`git add -A`) and hand over with the list of tags,
with one line on each `unsure` tag saying why.

## Verification

Starts when the human declares Production over: set Step to
Verification in STATE.

1. Run the checks below and report the results, with the list of
   remaining tags.
2. The human reviews every produced artifact (`git diff --cached`) and
   rules on each tag or edits the artifacts directly. Apply the rulings,
   remove the tags, and run the checks again.

Checks:

- Every new or modified rule ID of the change is cited by a test,
  unless marked "(not testable)".
- Every rule ID cited in tests exists in `spec/main/` or the change
  page.
- The new tests fail for the right reason (missing behavior, not syntax
  or setup errors).

The human's review deserves particular care: checking behavior through
tests is cheaper than through code. Does each part of the change have
tests, and does each test truly express it?

## Exit

Checks pass, no tags remain and the human approves the suite. Next
phase: Implementation. From now on, tests are read-only.

On the human's go, set Phase to Implementation and Step to
Exploration in STATE; then stage all changes and
commit them as `dev43: <increment> — Tests`.
