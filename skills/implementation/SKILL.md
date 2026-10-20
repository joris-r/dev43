---
name: implementation
description: Dev43 Implementation phase of an increment. Use when spec/STATE.md says Phase is Implementation. Writes code until the tests pass, never modifying tests, tagging every deviation.
---

# Implementation

Goal: code that makes the tests green and follows the specification,
with every deviation tagged for the human.

## Exploration

1. Read the change spec, the tests, and the code they touch.
2. Flag to the human fragile areas, divergences between code and spec,
   and technical choices that will be needed (libraries, algorithms,
   interfaces). These are important decisions: they are hard to reverse.

One point per message; raise only what you cannot settle with
confidence, and settle the rest yourself in Production (see
`CLAUDE.md`, Working with the human).

After a return from Tests or Specification, raise only what the return
changed; if nothing, say so and move on at the human's approval.

When you have nothing left to raise, propose to end Exploration. It
ends when the human agrees; then set Step to Production in STATE.

## Amendment

When the human wants a small addition to the specification during
Implementation (a rule or an example that one or two new tests can
check), skip the return loop:

1. Write the addition in the change page and its new tests, tagged as
   usual. Existing tests stay unchanged.
2. Run the new tests: they must fail for the right reason.
3. Hand over both together; the human reviews them in one gate.
4. On approval, commit only the change page and the new tests as
   `[<increment>] Amendment`. Phase and Step stay as they were.

Anything larger, or a change to an existing rule or test, goes through
a return to Specification or Tests.

## Production

Work without interrupting until all tests are green, except disputed
ones.

- Never modify a test. If one seems wrong, leave it, tag it `unsure`,
  and continue. This is a disputed test.
- Tag the interpretations of the specification and the technical
  choices you are unsure of.
- Cite a rule ID in code only where it explains something the reader
  would not otherwise see.
- If a decision calls into question what was agreed, stop and propose a
  return to Exploration (or to Specification).

Run the Verification checks and fix what fails, except disputed
tests. Then mark new files (`git add -N .`), set Step to Verification
in STATE, and hand over with: the check results, the
disputed tests with your reasoning, and the list of tags.

## Ruling on disputed tests

During Verification, the human rules on each
disputed test: fix the code; or correct the test (return to Tests); or
the test faithfully expresses a wrong decision (return to
Specification). On a return, set Phase to Tests or Specification and
Step to Exploration in STATE. The increment keeps its name; code and
tests already written stay unless the human decides otherwise. The
commits of the phases done again end with ` (return)`.

## Verification

Starts at your hand-over, once the checks below pass.

1. The human reviews the changes (`git diff`), staging each file or
   hunk once read, and rules on each tag or edits the artifacts
   directly.
2. Apply the rulings, remove the tags, and run the checks again. The
   review is done when `git diff` is empty.

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
commit them as `[<increment>] Implementation`.
