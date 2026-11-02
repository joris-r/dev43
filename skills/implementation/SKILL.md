---
name: implementation
description: Dev43 Implementation phase of an increment. Use when the plan of the increment reaches the Implementation phase. Writes code until the tests pass, never modifying tests, tagging every deviation.
---

# Implementation

Load `dev43:core` first if it is not loaded.

Goal: code that makes the tests green and follows the specification,
with every deviation tagged for the human.

## Exploration

When Implementation resumes after a return, its wip commit is in the
history (see `dev43:core`, Returns): build on it. Where it disagrees
with what the return phases committed, they win (tests are read-only).

1. Read the change, the tests, and the code they touch.
2. Flag to the human fragile areas, divergences between code and spec,
   and technical choices that will be needed (libraries, algorithms,
   interfaces). These are important decisions: they are hard to reverse.

One point per message; raise only what you cannot settle with
confidence, and settle the rest yourself in Production (see
`dev43:core`, Working with the human).

After a return from Tests or Specification, raise only what the return
changed, and the tags of the wip commit that still apply; if
nothing, say so and move on at `next`.

When you have nothing left to raise, propose to end Exploration.

## Amendment

When the human wants a small addition to the specification during
Implementation (a rule or an example that one or two new tests can
check), skip the return loop:

1. Write the addition in the change and its new tests, tagged as
   usual. Existing tests stay unchanged.
2. Run the new tests: they must fail for the right reason.
3. Hand over both together; the human reviews them in one gate.
4. On `next`, commit only the specification and the new tests as
   `[<increment>] Amendment`, with the state trailers; Next stays
   Implementation.

Anything larger, or a change to an existing rule or test, goes through
a return to Specification or Tests.

## Production

Work without interrupting until all tests are green, except disputed
ones.

- Never modify a test written in a Tests phase. If one seems wrong,
  leave it, tag it `unsure`, and continue. This is a disputed test.
  In a `code-only` increment, you may edit a test without changing
  what it checks (e.g. a moved import); tag each such edit. Tests that the
  test and quality policy leaves to Implementation are code.
- Tag the interpretations of the specification and the technical
  choices you are unsure of.
- In the first increment, also set up the repository (a `.gitignore`
  that keeps out secrets and build output, lock files) and, if any, CI,
  as the technical part of the change says.
- Cite a rule ID in code only where it explains something the reader
  would not otherwise see.
- If a decision calls into question what was agreed, stop and propose a
  return to Exploration (or to Specification).

Run the Verification checks and fix what fails, except disputed
tests. Then hand over with: the check results, the disputed tests with
your reasoning, the list of tags, and the routine libraries added, in
one line. A disputed test is a tag: it always stops you.

## Ruling on disputed tests

During Verification, the human rules on each
disputed test: fix the code; or correct the test (return to Tests); or
the test faithfully expresses a wrong decision (return to
Specification). A return follows `dev43:core`, Returns: the tags of the
disputed tests are removed, as the return is the ruling, and the
implementation work goes into the wip commit. The increment keeps its
name, and Implementation resumes on that commit, unless the human
decides otherwise.

## Verification

Starts at your hand-over, once the checks below pass.

1. The human reviews the changes (`git diff`), staging each file or
   hunk once read, and rules on each tag or edits the artifacts
   directly.
2. Apply the rulings, remove the tags, and run the checks again. The
   review is done when all changes are staged, new files included.

Checks:

- The full test suite passes, except disputed tests.
- The checks required by the test and quality policy in
  `spec/main/technical.md`, as updated by the change, pass.
- Tests written in a Tests phase are unchanged since the last Tests
  commit (`git diff <that commit>` on them shows nothing but tags). In a `code-only` increment, it shows
  only tagged edits that leave what each test checks unchanged.

## Exit

Checks pass, no tags remain, the human approves, or the checks pass
where Verification has no gate. Next phase: the next one of the plan,
Integration when the increment has a change page.

Commit as `[<increment>] Implementation` (see `dev43:core`, Git).
