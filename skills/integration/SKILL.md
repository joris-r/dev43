---
name: integration
description: Dev43 Integration phase, the last phase of each increment. Use when spec/STATE.md says Phase is Integration. Merges the change specification into the main specification and runs a retrospective.
---

# Integration

Goal: `spec/main/` describes the software as it now exists, the change
page is gone, and the increment has been looked back on.

## Exploration

Retrospective with the human, on two topics:

- The project, at every increment: technical debt, architecture, what
  was learned, and what follows for the backlog.
- The process, only if something went wrong during the increment:
  rules in `CLAUDE.md`, agent context, thresholds, skill instructions.
  Label each change with its target: the project (e.g. `CLAUDE.md`)
  or the Dev43 plugin.

Propose concrete changes, one per message; the human decides. Keep
each short: what happened, in a sentence or two, and the change.

When you have nothing left to raise, propose to end Exploration. It
ends on `next`; then set Step to Production in STATE.

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

Then delete `spec/changes/<slug>.md`, remove from `spec/BACKLOG.md`
the entry the increment did, if any, and add the approved entries. Tag the choices you are
unsure of. Run the Verification checks and fix what fails. Then set Step to Verification in STATE, and
hand over with the check results and the list of tags, with one line
on each saying why.

## Verification

Starts at your hand-over, once the checks below pass.

1. The human reviews the changes (`git diff`), staging each file or
   hunk once read, and rules on each tag or edits the artifacts
   directly.
2. Apply the rulings, remove the tags, and run the checks again. The
   review is done when all changes are staged, new files included.

Checks:

- The full test suite passes.
- No rule ID is defined twice in `spec/main/`.
- Every rule ID cited in tests or code exists in `spec/main/`.
- `spec/changes/<slug>.md` no longer exists.

## Exit

Checks pass, no tags remain, the human approves. Next: Idle, until the
human starts an increment.

On `next`, set Phase to Idle in STATE, and clear Step, Increment and
Scope; then stage all changes and
commit them as `[<increment>] Integration`, where
`<increment>` is the increment that just ended.
