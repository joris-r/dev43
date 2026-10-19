---
name: integration
description: Dev-4-3 Integration phase, the last phase of each increment. Use when spec/STATE.md says Phase is Integration. Merges the change specification into the main specification and runs a retrospective.
---

# Integration

Goal: `spec/main/` describes the software as it now exists, the change
folder is gone, and the process itself has been reviewed.

## Exploration

Retrospective with the human on the process itself: rules in
`CLAUDE.md`, agent context, thresholds, skill instructions. Propose
concrete changes; the human decides.

End when the human says Exploration is over; then set Step to
Production in STATE.

## Production

Work without interrupting. Rewrite `spec/main/` in place:

- Apply new, modified and removed decisions from the change spec.
- Rewrite affected passages so they read as one document, not as a
  history of changes.
- If a new ID of the change already exists in `spec/main/`, renumber the
  new one and update its citations in the spec, tests and code. Change
  only the citations, never test or code logic.
- Apply the approved process changes to the project (e.g. `CLAUDE.md`).
  Record approved skill changes for the plugin maintainer; never edit
  the plugin's skills.

Tag every choice not dictated by the change spec. Hand over for review.

## Verification

Starts when the human declares Production over: set Step to
Verification in STATE.

Cycle until a round adds no new tags:

1. Spawn a subagent with only the `spec/main/` paths, the change folder
   and the test and source trees, and this checklist: every change
   merged; condensation (repetition, outdated text); ID conflicts or
   duplicates; IDs cited in tests/code that no longer exist. Tell it to
   tag each problem in place with `@dev43:decision[verify]`, not to fix
   anything, and to return a list.
2. The human rules on each tag.
3. Repeat.

Once converged and approved, delete `spec/changes/<slug>/`.

## Exit

Main spec updated, change folder removed, no tags remain, the human
approves. Next phase: Specification.

On the human's go, set Phase to Specification and Step to Exploration in
STATE, and clear Increment and Scope.
