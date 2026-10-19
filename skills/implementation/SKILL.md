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

- Never modify a test. If one seems wrong, leave it, tag it
  `disputed-test` with your reasoning, and continue.
- Tag deviations by kind: `disputed-test`, `spec` (interpreted
  decision) or `tech` (important technical decision).
- Cite the implemented ID in non-trivial code.
- If a decision calls into question what was agreed, stop and propose a
  return to Exploration (or to Specification).

Hand over with: test results, and the list of tags grouped by kind.

## Ruling on disputed tests

At the end of Production or Verification, the human rules on each
`disputed-test`: fix the code; or correct the test (return to Tests); or
the test faithfully expresses a wrong decision (return to
Specification). On a return, set Phase to Tests or Specification and
Step to Exploration in STATE. The increment keeps its name; code and
tests already written stay unless the human decides otherwise.

## Verification

Starts when the human declares Production over: set Step to
Verification in STATE.

Cycle until a round adds no new tags:

1. Run the tests and the checks required by the test and quality
   policy in `spec/main/3-technical/`, as updated by the change folder.
   Report results.
2. Spawn a subagent with only the paths of `spec/main/`, the change
   folder, the tests and the sources, and this checklist, limited to
   code added or changed in this increment: code matches spec; code not
   traceable to an ID; dead or speculative code; new dependencies. Tell
   it to tag each problem in place with `@dev43:decision[verify]`, not
   to fix anything, and to return a list.
3. The human handles the tags and reviews the code.
4. Repeat.

## Exit

Tests green, checks pass, no tags remain, the human approves. Next
phase: Integration.

On the human's go, set Phase to Integration and Step to Exploration in
STATE.
