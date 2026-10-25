---
name: specification
description: Dev43 Specification phase, the first phase of each increment. Use when spec/STATE.md says Phase is Specification, or when the human starts a new increment. Produces a short change specification in spec/changes/.
---

# Specification

Goal: a minimal change specification for one increment, on one page.
`spec/main/` stays untouched.

## Exploration

1. Agree with the human on the increment's scope; record it in STATE
   with a short slug once they approve. You may propose a scope from
   `spec/BACKLOG.md`. On a return from a later phase,
   keep the slug and amend the existing change page.
   If the Shape in STATE no longer fits, propose another (see
   `CLAUDE.md`, State and gates); update it once the human agrees.
2. Read the relevant parts of `spec/main/`, the code and tests, and
   the earlier decisions on the topic (`git log --grep=<keyword>`).
   Search the web or documents when the topic needs it.
3. Approach the subject gradually: the data model first (which
   entities and fields the change adds or modifies), then the behavior
   with examples, then technical decisions if any.
4. Surface decisions; flag early if the scope looks too big.
5. If the change needs a new feature-area page in `spec/main/`, agree
   on its name with the human.

One point per message; raise only what you cannot settle with
confidence, and settle the rest yourself in Production (see
`CLAUDE.md`, Working with the human).

When you have nothing left to raise, propose to end Exploration. It
ends on `next`; then set Step to Production in STATE.

## Production

Work without interrupting. Write `spec/changes/<slug>.md`: a title
with the scope in one sentence, then only what changes, in the order of
the main specification: data model first, then behavior, then
technical.

- New content: write it as it will read in `spec/main/`.
- Modified content: write its new version and name what it replaces
  (by name or rule ID).
- Removed content: list it under a `Removed` heading, by name or rule
  ID.
- State behavior as what a client observes at the interface (a
  response, a screen, a file), never as internal state.

Follow the specification rules of `CLAUDE.md`: write the minimum,
examples first, lists not tables, rule IDs only where needed, no
reasons. Leave edge cases to the Tests phase. Tag the choices you
are unsure of.

[example.md](example.md), next to this skill, is a change page of the
target shape: the first increment of a small HTTP link shortener. Match
its length and level of detail, not its content.

Run the Verification checks and fix what fails. Then set Step to Verification in STATE, and hand over
with the check results and the list of tags, with one line on each
saying why.

## Verification

Starts at your hand-over, once the checks below pass.

1. The human reviews the changes (`git diff`), staging each file or
   hunk once read, and rules on each tag or edits the artifacts
   directly.
2. Apply the rulings, remove the tags, and run the checks again. The
   review is done when all changes are staged, new files included.

Checks:

- `spec/main/` is unchanged (`git diff HEAD -- spec/main` is empty).

The human also judges the size of the increment. If they decide to
split it, return to Exploration and narrow the Scope in STATE; the rest
becomes a later increment.

## Exit

No tags remain and the human approves. Next phase: the next one of
the Shape.

On `next`, set Phase to the next phase and Step to Exploration in
STATE; then stage all changes and
commit them as `[<increment>] Specification`.
