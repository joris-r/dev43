---
name: migrate
description: Dev43 migration of a project from Dev43 3 to Dev43 4. Loaded by dev43:core when the major version of the project's Dev43 trailer is 3. Rewrites spec/ into docs/ and the tests' citations into paths, without changing any decision.
---

# Migration from Dev43 3

Load `dev43:core` first if it is not loaded.

Goal: the v3 specification rewritten in the v4 form, every decision
kept, and the tests citing paths. It changes the form, never a
decision, except the deletions the human approves.

## Start

- The migration starts in Pause. If an increment is in progress,
  finish it under the v3 rules first, then migrate.
- Propose it as one increment, `migrate`, whatever the size, with
  phases Specification and Tests, then Implementation only if a new
  test fails. Its gates: Specification Verification, where the human
  reviews the whole new specification.
- On `next`, the commits of the increment record `Dev43:` the new
  plugin version.

## Specification

Rewrite `spec/main/` into `docs/`, in the form of the
`dev43:specification` skill:

- `data-model.md` becomes `model.md`; `technical.md` stays; each
  feature-area page splits into the operations, UI and scenarios it
  holds, at top level or in a domain folder. Agree on the domains with
  the human when the split is not obvious.
- Every statement of behavior gets a tag. Rule IDs disappear: list,
  in the commit body, each rule ID with the path that replaces it.
- A statement v4 requires and v3 left open (e.g. a refused case, a
  message) states the current behavior of the code, marked
  `@dev43:unsure` for the human.
- Run the agent checks of the specification. Apply the deletions of
  [duplicate] and [why]; propose those of [silver] and [examples] to
  the human, as marks.
- Move `spec/BACKLOG.md` to `docs_future/BACKLOG.md`, and delete
  `spec/`. Files the process does not own stay as they are.
- List the rules of the project's `CLAUDE.md` that name a removed
  phase or step (Integration, a change page, a human review of tests
  or code); the human rewords them at the review.
- An agent checks, in a fresh context, that every v3 statement maps to
  a v4 line, and that v4 adds only marked lines. The mapping goes in
  the commit body.

The human reviews the whole of `docs/` at the Verification gate.

## Tests

- Existing tests change only their citations: each name or rule ID
  becomes the paths of what the test checks.
- Each tag without a test gets one, written as in the Tests skill. It
  checks the current behavior: one that fails is a counterexample, to
  raise to the human.
- Run the script check [coverage].
- An agent checks, in a fresh context, that each new citation matches
  what its test checks.

## Implementation

Only if a new test fails and the human decides the code is wrong: fix
the code, as in the Implementation skill.

## Exit

The final review, as in `dev43:core`. Then Pause, under the v4 rules.
