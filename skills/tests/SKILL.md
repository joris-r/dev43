---
name: tests
description: Dev-4-3 Tests phase of an increment. Use when spec/STATE.md says Phase is Tests. Writes tests, each linked to a decision ID, before any implementation.
---

# Tests

Goal: a test suite that faithfully expresses the change specification.
Tests are written before the implementation and will be read-only
during it.

## Exploration

1. Read the change specification and the test and quality policy in
   `spec/main/3-technical/`.
2. Discuss with the human: what to test, at which level, which edge
   cases matter.
3. If the change brings new test or quality needs, propose an update
   of the policy; once the human agrees, write it in the change folder
   under `3-technical/`.
4. Flag decisions that cannot be tested; propose to make them testable
   or to accept them as not testable. Mark each accepted one
   "(not testable)" in the change spec.

End when the human says Exploration is over; then set Step to
Production in STATE.

## Production

Work without interrupting.

- Each test cites the ID(s) it checks, in its name or a comment.
- Every testable decision of the change has at least one test.
- Update or delete existing tests that cite a modified or removed
  decision.
- Tests must fail for the right reason before implementation (missing
  behavior, not syntax or setup errors). Run them to confirm. On a
  return from Implementation, this applies only to new or changed
  tests.
- Write only the minimum non-test code needed for tests to compile
  (stubs, signatures), and tag it `tech` if it fixes an interface.

Tag every choice the spec does not dictate. Hand over for review.

## Verification

Starts when the human declares Production over: set Step to
Verification in STATE.

This review deserves particular care: checking behavior through tests is
cheaper than through code.

Cycle until a round adds no new tags:

1. Spawn a subagent with only the paths of `spec/main/`, the change
   folder and the tests, and this checklist: does each test truly
   express its decision; decisions with no test, unless marked "(not
   testable)"; tests added or changed in this increment with no or
   wrong ID; tests that check implementation details instead of
   behavior; missing edge cases. Tell it to tag each problem in place
   with `@dev43:decision[verify]`, not to fix anything, and to return a
   list.
2. The human reviews the suite and rules on each tag.
3. Repeat.

## Exit

No tags remain and the human approves the suite. Next phase:
Implementation. From now on, tests are read-only.

On the human's go, set Phase to Implementation and Step to
Exploration in STATE.
