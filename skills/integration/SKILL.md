---
name: integration
description: Dev43 Integration phase, the last phase of each increment. Use when spec/STATE.md says Phase is Integration. Merges the change specification into the main specification and runs a retrospective.
---

# Integration

Load `dev43:core` first if it is not loaded.

Goal: `spec/main/` describes the software as it now exists, the change
page is gone, and the increment has been looked back on.

## Exploration

Retrospective with the human, on three topics:

- The project, at every increment: technical debt, architecture, what
  was learned, and what follows for the backlog. If nothing is worth
  raising, say so; the topic is then done.
- The process, only if something went wrong during the increment:
  rules, agent context, thresholds, skill instructions. Label each
  change with its target: the project (e.g. its `CLAUDE.md`) or the
  Dev43 plugin.
- Going further: up to three leads drawn from the increment's actual
  work, never generic, or none if no real one: a concept or pattern at
  play (e.g. Data Mapper vs Active Record), or a quality or security
  point worth examining. The human picks one or none; nothing is
  committed and the gate does not depend on it.

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
  Never edit the plugin's skills, and write no file for approved plugin
  changes.

Then delete `spec/changes/<slug>.md`, remove from `spec/BACKLOG.md`
the entry the increment did, if any, and add the approved entries. Tag the choices you are
unsure of. Run the Verification checks and fix what fails. Then set Step to Verification in STATE, and
hand over with the check results, the list of tags with one line on
each saying why, and where each item of the change page landed (a
page of `spec/main/`, or removed). If plugin changes were approved,
invite the human to send them to Dev43
(https://github.com/joris-r/dev43/issues), with the text ready to
send: the project, the increment, the Dev43 version, and each change in
a sentence or two.

## Verification

Starts at your hand-over, once the checks below pass.

1. The human reviews the changes (`git diff`), staging each file or
   hunk once read, and rules on each tag or edits the artifacts
   directly.
2. Apply the rulings, remove the tags, and run the checks again. The
   review is done when all changes are staged, new files included.

Checks:

- No rule ID is defined twice in `spec/main/`.
- Every rule ID cited in tests or code exists in `spec/main/`.
- `spec/changes/<slug>.md` no longer exists.

## Exit

Checks pass, no tags remain, the human approves. Next: Pause, until
the human starts an increment.

On `next`, set Phase to Pause in STATE, and clear the other fields and
Scope; then stage all changes and
commit them as `[<increment>] Integration`, where
`<increment>` is the increment that just ended.
