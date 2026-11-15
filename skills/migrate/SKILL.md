---
name: migrate
description: Dev43 migration of a project to the current form, from Dev43 3 or from an earlier minor version of Dev43 4. Loaded by dev43:core when the major or minor version of the project's Dev43 trailer is lower than the plugin's. Rewrites the specification and the tests' citations, without changing any decision.
---

# Migration

Load `dev43:core` first if it is not loaded.

Goal: the specification in the current form, every decision kept, and
the tests citing it. A migration changes the form, never a decision,
except the deletions the human approves. A statement the current form
requires and the old one left open states the current behavior of the
code, marked `@dev43:unsure` for the human. A line that only gives the
form (inputs, types, the state concept) needs no mark.

## Start

- The migration starts in Pause. If an increment is in progress,
  finish it under the old rules first, then migrate.
- Propose it as one increment, `migrate`, whatever the size, with
  phases Specification and Tests, then Implementation only if a new
  test fails. Its gates: Specification Verification, where the human
  reviews the whole changed specification; Specification Exploration
  too when the migration closes the specification (to 4.3), which
  raises decisions.
- From Dev43 3: the rewrite of [From Dev43 3](#from-dev43-3), in the
  current form. From Dev43 4: the [minor steps](#minor-steps) after the
  project's version, in order, in the same increment.
- On `next`, the commits of the increment record `Dev43:` the new
  plugin version.

## From Dev43 3

Rewrite `spec/main/` into `docs/`, in the form of the
`dev43:specification` skill:

- `data-model.md` becomes `model.md`; `technical.md` stays; each
  feature-area page splits into the operations, UI and scenarios it
  holds, at top level or in a domain folder. Agree on the domains with
  the human when the split is not obvious.
- Every statement of behavior gets a tag. Rule IDs disappear: list,
  in the commit body, each rule ID with the path that replaces it.
- Run the agent checks of the specification. Apply the deletions of
  [duplicate] and [why]; propose those of [silver] and [examples] to
  the human, as marks.
- Move `spec/BACKLOG.md` to `docs_future/BACKLOG.md`, and delete
  `spec/`. Files the process does not own stay as they are.
- List the rules of the project's `CLAUDE.md` that name a removed
  phase or step (Integration, a change page, a human review of tests
  or code); the human rewords them at the review.
- An agent checks, in a fresh context, that every v3 statement maps to
  a v4 line, and that v4 adds only marked lines and lines of form.
  The mapping goes in the commit body.

The human reviews the whole of `docs/` at the Verification gate. The
hand-over lists the deletions, the marks and the `CLAUDE.md` rules to
reword; the mappings stay in the commit body.

## Minor steps

Each step brings `docs/` and `docs_future/` to the form of the
`dev43:specification` skill on one point. A rule the step does not
name is unchanged. Changes of the process alone (gates, the scope of
an increment, the checks) need no step.

### To 4.3: the specification is closed

1. Run `dev43:soundness` on the whole of `docs/`, in a fresh context:
   its findings are the open points.
2. `model.md` declares all the data: the state concept, a type on
   every field, the invariants. How a value is obtained or changed
   moves to an operation.
3. Every operation has `Inputs:` and `Cases:`, one case per state and
   input, errors included; `## Initial state` exists; an operation no
   `ui.md` runs has a `Trigger:` line.
4. `ui.md` gives every operation a trigger and every outcome a
   display. A condition on the model or a computed input moves to the
   operation.
5. A refused case states its message only if `technical.md` says the
   project specifies messages. If it does not, ask the human in
   Exploration whether to add that line or to drop the messages.

The open cases are the decisions of Exploration: the human settles
them, or the code's behavior stands, marked.

### To 4.4: contents and mockups

- The authored text (pages, help, emails, notices) moves from `ui.md`
  and `design/` to `contents.md`, untagged. A test that cited a moved
  tag cites the `ui.md` element instead; one that checked only the
  wording is proposed for deletion.
- `design/` has one mockup per element of `ui.md` with a look of its
  own, components included; a page's mockup shows a component once, in
  place.
- Tags not in the project's language: propose the renaming to the
  human; on approval, the citations follow.

### To 4.5: ordered cases and Then:

Rewrite where it shortens an operation: statements repeated in several
cases become `Then:` statements, saying after which cases; cases whose
conditions read in order ("otherwise", "if none refused") become a
numbered list; statements on every operation go to `## General`.
Bulleted cases keep their meaning as they are.

### To 4.6: the texts an operation sends

A text an operation sends (an email, a notice) gets its own section
of `contents.md`, cited by the case that sends it; the `ui.md`
element that cited it for that operation drops the citation.

## Tests

- Existing tests change only their citations: each name, rule ID or
  moved path becomes the paths of what the test checks.
- Each tag without a test gets one, written as in the Tests skill. It
  checks the current behavior: one that fails is a counterexample, to
  raise to the human.
- Run the script check [coverage].
- An agent checks, in a fresh context, that each new citation matches
  what its test checks. The checks [faithful] and [cases] apply only
  to the new tests; a gap it finds in the coverage of existing tests
  is proposed as an entry in `docs_future/BACKLOG.md`.

## Implementation

Only if a new test fails and the human decides the code is wrong: fix
the code, as in the Implementation skill.

## Exit

The final review, as in `dev43:core`. Then Pause, under the current
rules.
