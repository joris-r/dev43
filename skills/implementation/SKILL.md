---
name: implementation
description: Dev43 Implementation phase of an increment. Use when the plan of the increment reaches the Implementation phase. Writes code until the tests pass, never modifying tests, marking every deviation.
---

# Implementation

Load `dev43:core` first if it is not loaded.

Goal: code that makes the tests pass and follows the specification,
with every deviation marked.

## Exploration

When Implementation resumes after a return, its wip commit is in the
history (see `dev43:core`, Returns): build on it. Where it disagrees
with what the return phases committed, they win (tests are read-only).

1. Read the change, the tests, and the code they touch.
2. Find the fragile areas, the divergences between code and
   specification, and the technical choices the change needs
   (libraries, algorithms, interfaces). A choice the human would care
   about (silver rule) is a change of `docs/technical.md` (see
   `dev43:core`, Specification); settle the others yourself.

## Amendment

A small addition to the specification found during Implementation (a
statement that one or two new tests can check) skips the return loop:

1. Write the addition in `docs/` and its new tests, marked as usual.
   Existing tests stay unchanged.
2. Run the checks of the Specification phase on the addition (see
   its skill, Verification), [soundness] included.
3. Run the new tests: they must fail for the right reason.
4. The human reviews the addition, and an agent check covers the new
   tests (see the Tests skill, Checks).
5. Commit only the specification and the new tests as
   `[<increment>] Amendment`, with the state trailers; Next stays
   Implementation.

Anything larger, or a change to an existing statement or test, goes
through a return to Specification or Tests.

## Production

Work without interrupting until all tests pass, except disputed ones.

- Never modify a test written in a Tests phase. If one seems wrong,
  leave it, mark it, and continue: it is a disputed test. In a
  `code-only` increment, you may edit a test without changing what it
  checks (e.g. a moved import); mark each such edit. Tests that the
  test and quality policy leaves to Implementation are code.
- Mark the technical choices you are unsure of.
- A doubt on what the specification means, which the tests do not
  settle, is an opening in the specification: an Amendment, or a
  return to Specification.
- In the first increment, also set up the repository (a `.gitignore`
  that keeps out secrets and build output, lock files) and, if any, CI,
  as `docs/technical.md` says.
- Cite a path in code only where it explains something the reader
  would not otherwise see.

Run the checks and fix what fails, except disputed tests. Then run the
agent checks of this phase and of the earlier ones that have not run
theirs. Give the checking agent the disputed tests with your
reasoning, and the routine libraries added. Then hand over for the
final review.

## Disputed tests

The checking agent rules on each disputed test: fix the code, or
correct the test (a return to Tests). A test that faithfully expresses
a wrong decision goes to the human, as a return to Specification. A
return follows `dev43:core`, Returns: the marks of the disputed tests
are removed, as the return is the ruling, and the implementation work
goes into the wip commit. The increment keeps its name, and
Implementation resumes on that commit.

## Checks

Run:

- The full test suite passes, except disputed tests.
- The checks required by the test and quality policy in
  `docs/technical.md` pass.
- Tests written in a Tests phase are unchanged since the last Tests
  commit (`git diff <that commit>` on them shows nothing but marks).
  In a `code-only` increment, it shows only marked edits that leave
  what each test checks unchanged.

Agent checks, in a fresh context (see `dev43:core`, Agent checks), on
the code changed by the increment:

- [general] The code implements each statement of the change for
  every state and input of its case, beyond the values of its tests.
- [technical] The code follows `docs/technical.md`.
- [choices] Every dependency, service or interface the specification
  does not name is marked, or is a routine library of the stack.

## Exit

Checks pass, no marks remain, and the human approves at the final
review (see `dev43:core`, Final review). Next: `Pause`.

Commit as `[<increment>] Implementation` (see `dev43:core`, Git).
