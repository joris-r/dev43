---
name: integration
description: Dev-4-3 Integration phase, the last phase of each increment. Use when spec/STATE.md says Phase is Integration. Merges the change specification into the main specification and runs a retrospective.
---

# Integration

Goal: `spec/main/` describes the software as it now exists, the change
page is gone, and the process itself has been reviewed.

## Exploration

Retrospective with the human on the process itself: rules in
`CLAUDE.md`, agent context, thresholds, skill instructions. Propose
concrete changes, one per message; the human decides. Label each with
its target: the project (e.g. `CLAUDE.md`) or the Dev-4-3 plugin.

When you have nothing left to raise, propose to end Exploration. It
ends when the human agrees; then set Step to Production in STATE.

## Production

Work without interrupting. Rewrite `spec/main/` in place:

- Put each part of the change page in the page it belongs to: the data
  model in `data-model.md`, technical decisions in `technical.md`,
  behavior in its feature-area page. Apply modifications and removals.
- Rewrite affected passages so they read as one document, not as a
  history of changes. Keep it minimal: merging is not a reason to add
  detail.
- Apply the approved process changes to the project (e.g. `CLAUDE.md`).
  Record approved skill changes for the plugin maintainer; never edit
  the plugin's skills.

Then delete `spec/changes/<slug>.md`. Tag the choices you are
unsure of. Run the Verification checks and fix what fails. Then mark
new files (`git add -N .`), set Step to Verification in STATE, and
hand over with the check results and the list of tags, with one line
on each saying why.

## Verification

Starts at your hand-over, once the checks below pass.

1. The human reviews the changes (`git diff`), staging each file or
   hunk once read, and rules on each tag or edits the artifacts
   directly.
2. Apply the rulings, remove the tags, and run the checks again. The
   review is done when `git diff` is empty.

Checks:

- The full test suite passes.
- No rule ID is defined twice in `spec/main/`.
- Every rule ID cited in tests or code exists in `spec/main/`.
- `spec/changes/<slug>.md` no longer exists.

## Exit

Checks pass, no tags remain, the human approves. Next phase:
Specification.

On the human's go, set Phase to Specification and Step to Exploration in
STATE, and clear Increment and Scope; then stage all changes and
commit them as `dev43: <increment> — Integration`, where
`<increment>` is the increment that just ended.
