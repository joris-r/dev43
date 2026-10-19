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

Then delete `spec/changes/<slug>/`. Tag every choice not dictated by
the change spec. Stage all changes (`git add -A`) and hand over with
the list of tags.

## Verification

Starts when the human declares Production over: set Step to
Verification in STATE.

1. Run the checks below and report the results, with the list of
   remaining tags.
2. The human reviews every produced artifact (`git diff --cached`) and
   rules on each tag or edits the artifacts directly. Apply the rulings,
   remove the tags, and run the checks again.

Checks:

- The full test suite passes.
- No ID is defined twice in `spec/main/`.
- Every ID cited in tests or code exists in `spec/main/`.
- `spec/changes/<slug>/` no longer exists.

## Exit

Checks pass, no tags remain, the human approves. Next phase:
Specification.

On the human's go, set Phase to Specification and Step to Exploration in
STATE, and clear Increment and Scope; then stage all changes and
commit them as `dev43: <increment> — Integration`, where
`<increment>` is the increment that just ended.
