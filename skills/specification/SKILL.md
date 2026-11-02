---
name: specification
description: Dev43 Specification phase, the first phase of each increment. Use when the plan of the increment reaches the Specification phase. Produces the change of the specification, in place in spec/main/ or on a change page in spec/changes/.
---

# Specification

Load `dev43:core` first if it is not loaded.

Goal: a minimal change of the specification for one increment: in
place in `spec/main/`, or on one change page when the plan has an
Integration phase.

## Exploration

1. The plan set the scope. On a return from a later phase, keep the
   slug and amend the existing change. If the plan no longer fits,
   propose another (see `dev43:planning`).
2. Read the relevant parts of `spec/main/`, the code and tests, and
   the earlier decisions on the topic (`git log --grep=<keyword>`).
   Search the web or documents when the topic needs it.
3. Approach the subject gradually: the data model first (which
   entities and fields the change adds or modifies), then the behavior
   with examples, then technical decisions if any.
4. Surface decisions; flag early if the scope looks too big.
5. If the change needs a new feature-area page in `spec/main/`, agree
   on its name with the human.

When `spec/main/` is empty, or the increment changes the project's
purpose, stack or conventions, read [framing.md](framing.md), next to
this skill, and follow it too. When the Shape is `specify-existing`,
read [existing.md](existing.md) and follow it too.

One point per message; raise only what you cannot settle with
confidence, and settle the rest yourself in Production (see
`dev43:core`, Working with the human).

When you have nothing left to raise, propose to end Exploration.

## Production

Work without interrupting.

In place: edit `spec/main/` directly. Rewrite the affected passages so
they read as one document, and keep it minimal.

With a change page: leave `spec/main/` untouched, and write
`spec/changes/<slug>.md`: a title with the scope in one sentence, then
only what changes, in the order of the main specification: data model
first, then behavior, then technical.

- New content: write it as it will read in `spec/main/`.
- Modified content: write its new version and name what it replaces
  (by name or rule ID).
- Removed content: list it under a `Removed` heading, by name or rule
  ID.

In both cases, state behavior as what a client observes at the
interface (a response, a screen, a file), never as internal state; an
absence only when a test can observe it.

Follow the specification rules of `dev43:core`: write the minimum,
examples first, lists not tables, rule IDs only where needed, no
reasons. Leave edge cases to the Tests phase. Tag the choices you
are unsure of.

[example.md](example.md), next to this skill, is a change page of the
target shape: an early increment of a small HTTP link shortener. Match
its length and level of detail, not its content.

Run the Verification checks and fix what fails. Then hand over with the
check results and the list of tags, with one line on each saying why;
or, where Verification has no gate, make the exit commit.

## Verification

Starts at your hand-over, once the checks below pass.

1. The human reviews the changes (`git diff`), staging each file or
   hunk once read, and rules on each tag or edits the artifacts
   directly.
2. Apply the rulings, remove the tags, and run the checks again. The
   review is done when all changes are staged, new files included.

Checks:

- With a change page: `spec/main/` is unchanged:
  `git diff HEAD -- spec/main` and
  `git ls-files -o --exclude-standard spec/main` print nothing.
- In place: no rule ID is defined twice in `spec/main/`.

The human also judges the size of the increment. If they decide to
split it, return to Exploration and narrow the scope, recorded in the
next commit; the rest becomes a later increment.

## Exit

No tags remain and the human approves, or the checks pass where
Verification has no gate. Next phase: the next one of the plan.

Commit as `[<increment>] Specification` (see `dev43:core`, Git).
