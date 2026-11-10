---
name: specification
description: Dev43 Specification phase, the first phase of each increment. Use when the plan of the increment reaches the Specification phase. Produces the change of the specification, in docs/ or in docs_future/<feature>/.
---

# Specification

Load `dev43:core` first if it is not loaded.

Goal: a minimal change of the specification for one increment,
approved by the human: in `docs/`, or in `docs_future/<feature>/` for
the `future` shape.

## Exploration

1. The plan set the scope. On a return from a later phase, keep the
   slug and amend the existing change. If the plan no longer fits,
   propose another (see `dev43:planning`).
2. Read the relevant parts of `docs/` and `docs_future/`, the code and
   tests, and the earlier decisions on the topic
   (`git log --grep=<keyword>`). Search the web or documents when the
   topic needs it.
3. Approach the subject gradually: the model first, then the
   operations, then the UI, then technical decisions if any.
4. Surface decisions; flag early if the scope looks too big.
5. Agree with the human on the name of a new domain, document or
   concept.
6. If a point needs evidence, or the human wants to see something
   first, build a throwaway preview outside the repo (e.g. in a
   `git worktree`). Delete it when Exploration ends: it never enters a
   commit, and the real code comes in its phase.

An increment of a feature has its decisions settled by the future
specification: raise only what moving it into `docs/` reveals.

When `docs/` is empty, or the increment changes the project's purpose,
stack or conventions, read [framing.md](framing.md), next to this
skill, and follow it too. When the Shape is `specify-existing`, read
[existing.md](existing.md) and follow it too.

One point per message; raise only what you cannot settle with
confidence, and settle the rest yourself in Production (see
`dev43:core`, Working with the human).

When you have nothing left to raise, propose to end Exploration.

## Production

Work without interrupting. By shape:

- Most shapes: edit `docs/` in place. Rewrite the affected passages so
  they read as one document, and keep it minimal. Update the future
  versions the change breaks.
- An increment of a feature: move its sections from
  `docs_future/<feature>/` into `docs/`, as they read with the
  feature applied, and remove them, with the increment, from the
  feature. The last increment deletes `docs_future/<feature>/`,
  moving any open lesson and the points kept for the human to
  `docs_future/BACKLOG.md`.
- `future`: write or update `docs_future/<feature>/`, in the form of
  [future.md](future.md); or delete it, for an abandoned feature.

Follow the specification rules of `dev43:core`: write the minimum, no
reasons, a tag on every statement of behavior. Leave edge cases to the
Tests phase. Mark the choices you are unsure of.

Run the Verification checks and fix what fails. Then hand over with
the check results and the list of marks, with one line on each saying
why; or, where Verification has no gate, make the exit commit.

## Layout

- Documents, each only when needed:
  - `README.md`: the index of the documents;
  - `overview.md`: what the software is for, its non-goals. A
    capability the software lacks is a non-goal, untagged;
  - `technical.md`: stack, conventions, test and quality policy;
  - `design.md`, `design/`: the look;
  - `model.md`: the data, which sets the vocabulary;
  - `operations.md`: the actions on that data, queries included;
  - `ui.md`: what the user meets;
  - `scenarios.md`: typical use, end to end.
- The top level spans domains. A domain folder holds what is specific
  to it; its `README.md` declares the domains it depends on:
  `Depends on: /tasks, /users.`
- One `##` section per concept or operation, with the same name
  across documents.
- `model.md`: each concept states its meaning, then its fields
  (`name: type`, its meaning), then its invariants, each tagged.
  Invariants are only in the model.
- `operations.md`: an operation states its purpose only if the name
  and cases leave it unclear, its API binding if any, then one tagged
  case per condition, errors included, each with all its outcomes. A
  refused case states its message only when `technical.md` says the
  project specifies messages. An operation extending another
  domain's operation starts with `Extends <path>.`
- `ui.md`: one section per element the user meets (page, component,
  command), its binding first, then:
  - what it shows, in order; one tagged case per state or outcome,
    each transition as a tagged sub-point;
  - what the user can do: each trigger, the operation it runs, and
    when it is unavailable.
  It refers to the operations, adding only trigger and display.
- An exact text the user sees is written with placeholders:
  `No task <number>.`
- `design/`: mockups, one per page, named after its `ui.md` section,
  showing every state, values included. `design.md` holds the look
  rules they cannot show.
- A scenario: its starting state, then its steps, each a user action
  or what they see.
- Use nested lists, never tables. An example only where a statement is
  ambiguous without it.

For the form of a whole specification, read the one matching the
project's UI, next to this skill: [cli.md](cli.md) for a command line,
[web.md](web.md) for a web application.

## Verification

Starts at your hand-over, once the checks below pass.

1. The human reviews the changes (`git diff`), staging each file or
   hunk once read, and rules on each mark or edits the artifacts
   directly.
2. Apply the rulings, remove the marks, and run the checks again. The
   review is done when all changes are staged, new files included.

The human also judges the size of the increment. If they decide to
split it, return to Exploration and narrow the scope, recorded in the
next commit; the rest becomes a later increment.

Script checks: `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/check.py" spec`.

- [paths] Every path a document cites resolves; `docs/` cites nothing
  in `docs_future/`.
- [names] A concept or operation has the same section name in every
  document.
- [overlap] Every future version applies to `docs/`: each `×` and `…`
  line matches an existing line.
- [depends] A domain cites only itself, the top level and the domains
  it declares; dependencies have no cycle; each `Extends` path is an
  operation of a declared domain. The script also lists, for each
  changed operation, its dependent domains and its extensions: they
  are the input of [dependents] and [extension].

Agent checks, by you, on the change:

- [placement] Every statement is in its document: invariants in the
  model, conditions and effects in the operations; `ui.md` adds only
  triggers and display.
- [invariants] Each operation states the conditions that keep the
  invariants.
- [meaning] Every concept and field states its meaning, unless its name
  makes it obvious.
- [duplicate] Nothing is stated twice or derivable from another line.
- [examples] Every example illustrates a statement ambiguous without
  it.
- [dependents] An added or changed operation keeps the invariants of
  every domain that depends on its domain.
- [complete] The cases of an operation do not overlap and cover every
  input.
- [extension] An extension of another domain's operation keeps or
  weakens its precondition, and keeps or strengthens its effects.
- [tags] Every statement of behavior has a tag.
- [silver] Every line passes the silver rule; delete the lines you are
  sure fail it.
- [why] No line gives a reason; reasons go to the commit body.

## Exit

No marks remain and the human approves, or the checks pass where
Verification has no gate. Next phase: the next one of the plan.

Commit as `[<increment>] Specification` (see `dev43:core`, Git).
