---
name: planning
description: Dev43 planning of an increment. Use when the human starts an increment, in Pause, or when the plan of the current increment no longer fits. Analyzes the potential impact of the change and proposes its plan: scope, shape, phases and gates.
---

# Planning

Load `dev43:core` first if it is not loaded.

Goal: a plan the human approves, which spends their attention where the
change can do harm.

## Impact analysis

Read the relevant parts of `spec/main/`, the tests and the code, and
the earlier decisions on the topic (`git log --grep=<keyword>`). Find
what the change touches: specified behavior, the data model, tests,
code, tooling; and what it could break.

## The plan

Propose it in one message: a slug, the scope in one sentence, the
shape, the phases, and the gates, with a few words on why for each
gate. If something in the impact cannot be settled from the project,
raise it first, one point per message.

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
- `direct`: one Direct phase, starting at Production. Tooling,
  configuration, dependencies, `CLAUDE.md` or `spec/main/technical.md`
  change, or a small code change outside the specification
  (appearance, assets, unspecified wording); specified behavior and
  tests do not. A structural change (a new framework, a new repo
  layout) or a refactoring takes `full` or `code-only` instead.

### Change page

The specification changes in place, in `spec/main/`, unless the change
is large (a new feature area, a reshaped data model, rules spread over
several pages): then it gets a change page, and the plan ends with an
Integration phase that merges it.

### Gates

Each phase has two possible gates: its Exploration (discuss before
producing) and its Verification (review before its commit). The last
phase's Verification is always a gate, the final review; do not list
it.

Choose the gates from the potential impact of the change, not from its
size:

- no specified behavior changes: the final review alone;
- behavior changes, but the plan already settles what: the final
  review alone, which then covers the specification, the tests and the
  code;
- a phase holds a decision the human may not share (a rule open to
  debate, a new entity, a choice hard to reverse): that phase's
  Exploration;
- a phase produces what later work builds on and would be costly to
  redo (the data model, the stack, a new interface): that phase's
  Verification.

Follow the project's `CLAUDE.md` where it says more.

## Changing the plan

When the plan no longer fits (a point the plan missed, a scope that
grows), propose a new one in the same way. Once the human agrees,
record it in the next commit. The phases already committed stay as
they are.
