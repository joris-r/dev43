---
name: planning
description: Dev43 planning of an increment. Use when the human starts an increment, in Pause, or when the plan of the current increment no longer fits. Analyzes the potential impact of the change and proposes its plan: scope, shape, phases and gates.
---

# Planning

Load `dev43:core` first if it is not loaded.

Goal: a plan the human approves, which spends their attention where the
change can do harm.

Planning settles the plan, not the solution, and produces no file. If
the solution needs discussing or showing first (a screen design, a
preview), plan a Specification phase with its Exploration as a gate,
and do it there.

## Open features

Each folder of `docs_future/` other than its `BACKLOG.md` is an open
feature. When the human starts an increment without naming its work,
list the open features, each with the next increment of its outline,
and the project backlog.

An increment of a feature takes the first increment of its outline,
with the lessons of `docs_future/<feature>/BACKLOG.md`. If a lesson
calls the outline into question, propose a `future` increment first.

## Impact analysis

Read the relevant parts of `docs/` and `docs_future/`, the tests and
the code, and the earlier decisions on the topic
(`git log --grep=<keyword>`). Find what the change touches: statements
of behavior, the model, the domains that depend on them (their
`README.md`), tests, code, tooling; and what it could break, open
features included.

A change too large for one increment (a new domain, a reshaped model,
statements spread over several documents) is first written ahead, in
a `future` increment.

## The plan

Propose it in one message: a slug, the feature if any, the scope in
one sentence, the shape, the phases, and the gates, with a few words
on why for each gate. If something in the impact cannot be settled
from the project, raise it first, one point per message.

Approving the plan is the first gate: on `next`, start the first phase
with its skill. The plan is recorded in the trailers of the first
commit (see `dev43:core`, State).

### Shape

- `full`: Specification, Tests, Implementation. The change alters
  behavior.
- `code-only`: Specification, Implementation. The specified behavior
  does not change; the code does, including a new implementation of an
  existing specification. The existing suites must pass unmodified.
  When existing code changes, show a short before/after excerpt in the
  plan.
- `tests-only`: Specification, Tests. Only tests or their tooling
  change; the Tests phase runs the full check.
- `specify-existing`: Specification, Tests. Specifies a zone of
  existing behavior without changing it; no code changes. No Tests
  phase when the change specifies no behavior (e.g. only
  `technical.md`).
- `future`: Specification. Writes, updates or deletes
  `docs_future/<feature>/`: a new feature, an important lesson, or an
  abandoned feature. `docs/` does not change.
- `direct`: one Direct phase, starting at Production. Tooling,
  configuration, dependencies, `CLAUDE.md` or `docs/technical.md`
  change, or a small code change outside the specification
  (appearance, assets, unspecified wording); specified behavior and
  tests do not. A structural change (a new framework, a new repo
  layout) or a refactoring takes `full` or `code-only` instead.

An increment of a feature usually takes `full`; its Specification
only moves the increment's sections from `docs_future/<feature>/` into
`docs/`.

### Gates

The final review is always a gate; do not list it. The other gates:

- Specification Exploration: the human discusses before the change is
  written;
- Specification Verification: the human reviews the change before
  tests and code build on it;
- Tests Verification, Implementation Verification: an agent check
  before the next phase builds on it.

Choose the gates from the potential impact of the change, not from its
size:

- no specified behavior changes: the final review alone;
- behavior changes, but the plan or the future specification already
  settles what: no Specification gate;
- the change holds a decision the human may not share (a statement
  open to debate, a new concept, a choice hard to reverse):
  Specification Exploration;
- the change is what later work builds on and would be costly to redo
  (the model, the stack, a new interface): Specification Verification;
- the tests or the code are where the change can do harm (a delicate
  migration, a subtle invariant, a security point): their
  Verification.

Follow the project's `CLAUDE.md` where it says more.

## Changing the plan

When the plan no longer fits (a point the plan missed, a scope that
grows), propose a new one in the same way. Once the human agrees,
record it in the next commit. The phases already committed stay as
they are.
