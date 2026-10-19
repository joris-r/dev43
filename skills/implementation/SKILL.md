---
name: implementation
description: Dev-4-3 Implementation phase of an increment. Use when spec/STATE.md says Phase is Implementation. Writes code until the tests pass, never modifying tests, tagging every deviation.
---

# Implementation

Goal: code that makes the tests green and follows the specification,
with every deviation tagged for the human.

## Exploration

1. Read the change spec, the tests, and the code they touch.
2. Flag to the human fragile areas, divergences between code and spec,
   and technical choices that will be needed (libraries, algorithms,
   interfaces). These are important decisions: they are hard to reverse.

End when the human says Exploration is over; then set Step to
Production in STATE.

## Production

Work without interrupting until all tests are green, except disputed
ones.

- Never modify a test. If one seems wrong, leave it, tag it `unsure`,
  and continue. This is a disputed test.
- Tag every interpretation of the specification and every technical
  choice it does not dictate.
- Cite a rule ID in code only where it explains something the reader
  would not otherwise see.
- If a decision calls into question what was agreed, stop and propose a
  return to Exploration (or to Specification).

Stage all changes (`git add -A`) and hand over with: test results, the
disputed tests with your reasoning, and the list of tags.

## Ruling on disputed tests

During Verification, the human rules on each
disputed test: fix the code; or correct the test (return to Tests); or
the test faithfully expresses a wrong decision (return to
Specification). On a return, set Phase to Tests or Specification and
Step to Exploration in STATE. The increment keeps its name; code and
tests already written stay unless the human decides otherwise.

## Verification

Starts when the human declares Production over: set Step to
Verification in STATE.

1. Run the checks below and report the results, with the list of
   remaining tags.
2. The human reviews every produced artifact (`git diff --cached`) and
   rules on each tag or edits the artifacts directly. Apply the rulings,
   remove the tags, and run the checks again.

Checks:

- The full test suite passes, except disputed tests.
- The checks required by the test and quality policy in
  `spec/main/technical.md`, as updated by the change page, pass.
- Test files are unchanged since the Tests phase (`git diff HEAD` on
  the test files shows nothing but tags).

## Exit

Checks pass, no tags remain, the human approves. Next phase:
Integration.

On the human's go, set Phase to Integration and Step to Exploration in
STATE; then stage all changes and
commit them as `dev43: <increment> — Implementation`.
