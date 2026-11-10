# Dev43: A Software Development Process

This document gives the context and the principles of Dev43. The
operational rules are in the skills ([skills/](../skills/)), which apply
these principles.


## Context and Goal

Dev43 is a software development methodology for human and LLM agents,
combining specification driven development (SDD) with test driven
development (TDD).

The main goal is to ensure that the user needs are correctly identified
and fulfilled by the produced software. The process does not prioritize
production speed and explicitly limits the agents' freedom.

The golden rule: humans must be involved in every important or
impactful decision.

The silver rule: a statement belongs in the specification only if a competent
agent could reasonably have chosen otherwise and the human would care, or if
the specification would be open without it.

These rules keep humans in the loop, but only on important topics.


## Rationale

LLM agents are highly effective at deriving patterns from their training
data, and at generalizing and recombining them. But they lack some
qualities essential to software authors:

- they do not retain what they learn across sessions: their only memory
  is the context window
- their knowledge comes from written material, not lived experience:
  they get feedback from the software itself (tests, compilers, program
  output), but have no direct access to the human context

So we must:

- give agents an accurate, human-validated specification of what is
  being built, which also serves as their persistent memory
- keep humans in control of the decisions that require context

Human attention is the scarce resource. Every principle below either
protects a human decision or saves human effort.

Agents produce more tests and code than a human can review, and a
human does not truly review work they did not invest in. So the human
reviews only the specification, the one artifact they shape.


## Principles

### Specification first

All work starts with the specification, because a specification
written after the code describes what the code does rather than what
was needed.

Behavior then flows in one direction: specification, tests, code. Each
step is reviewed before the next is derived from it, and an artifact
never bends a more authoritative one. When a later step reveals an
error in an earlier one, the work returns to it.


### A closed, minimal specification

The specification is the only artifact the human reviews, and agents
derive tests and code from it without asking. So it is closed: the
model declares all the data, with its meaning, types and invariants;
the operations settle every input in every state; the UI gives every
operation a trigger and every outcome a display.

Each document has one role. The model says what holds in every state,
the operations how the state changes, the UI what is shown and what
runs an operation. The design and the scenarios agree with them.

Within that, by the silver rule, it records only the decisions where
the human matters: what they do not care about is left free, and said
so. Agents derive the rest, in the tests and the code. The
specification stays shorter and more abstract than them, and easy for
a human to read.

It records what is decided, not why: reasoning goes stale. The reasons
live in the history.

It is organized by domain, around the data model and the operations on
it.


### Tests as the guarantee

The test suite is what ensures that the code respects the
specification. Tests are written before the code, from the
specification, and the code is then written to make them pass, without
modifying them.

Tests are also the agent's feedback loop: it knows it is done when they
pass.


### Traceability

Every statement of behavior in the specification carries a tag, and
its path (file, section, tag) names it. Every test cites the paths it
checks, and every tag has a test or is marked not testable.

The paths link each decision to the tests that check it. They show
that the specification is fully covered, which tests a change of the
specification touches, and what each test must check.


### The line of responsibility

The human reviews the specification and tries the software. Agents
check the tests and the code, each check in a fresh context, so that
it does not share the blind spots of the author.

An agent never changes a decision the human approved: such a change
goes back to the human, as a change of the specification.

This line holds in every increment, supervised or not.


### Checks

Each artifact is checked at three levels: scripts check the form,
agents check the meaning, the human checks the decisions. Each level
covers what the one below cannot, so the human's attention goes only
to the decisions.

The specification is checked by scripts for its structure: paths
resolve, names agree across documents, domains cite only what they
declare, every operation can be run, and future versions still
apply. Its author checks that every statement is in its document and
that it is closed. The author also keeps it minimal and readable:
every statement of behavior has a tag, every concept states its
meaning, and nothing is duplicated, given a reason, or illustrated
without need.

An agent in a fresh context then checks its soundness, after the
proof obligations of the B method: the initial state meets the
invariants, exactly one case of an operation applies to each state
and input, every operation keeps the invariants, including those of
dependent domains, every extension keeps the operation it extends,
and a migration brings existing data to a changed invariant. It also
checks that the documents agree: the operations use only declared
data, the UI displays every outcome, the mockups show what the UI
states, and each scenario can be walked through them. It reasons
rather than proves: a counterexample, or an obligation it cannot decide, goes to
the human as a mark. The human can also run it on the whole
specification. The human then reviews the specification.

The tests are checked by a script for coverage: every tag has a test,
and every path a test cites resolves. An agent in a fresh context
checks that each test checks what its statement says, and that the
cases cover it.

The code is checked by its tests, and by an agent in a fresh context
for the technical choices: it follows the stack, and names every
dependency the specification leaves open.

A finding of an agent check is fixed or disputed; a disputed one goes
to the human. The human finally tries the software.


### Small increments

The software grows in increments small enough for a human to review
properly and for an agent to hold in its context.

A small increment changes the main specification in place. A large
change is first written ahead as a future specification, separate from
the main one, with the outline of the increments that carry it out.
Each of them then moves its part into the main specification, which
keeps describing the software as it exists. What an increment teaches
about the rest of the change updates the future specification.


### Four phases

An increment goes through four phases, each producing one artifact:

1. **Planning**: the plan of the increment.
2. **Specification**: the change of the specification.
3. **Tests**: tests that express it.
4. **Implementation**: code that makes the tests pass.

An increment goes through only the phases whose artifact changes: a
refactoring needs no new tests, a tooling update needs no specification.
Every increment ends with a retrospective.


### Discuss, then produce, then review

Each phase follows three steps:

1. **Exploration**: a discussion between peers, one point at a time,
   raising only what the agent cannot settle with confidence.
2. **Production**: the agent works without interruption, and marks
   on the artifact each choice it is unsure of.
3. **Verification**: the reviewer, the human for the specification,
   rules on the marks and approves.

The steps regulate the interaction between human and agent: important
topics are discussed first, then the agent works unsupervised, and its
marks keep the human aware and involved at Verification.


### Gates follow the impact

The agent stops only where the change can do harm. At the start of
an increment, the agent analyzes the potential impact of the change and
proposes the gates: the steps where it waits for review, by the human
for the specification, by an agent for tests and code. Elsewhere it
goes on alone, and its work is reviewed at the end of the increment,
which is always a gate: the human reviews the specification change
and tries the software. The size of a change does
not set its gates: a large refactoring under unchanged tests may need
fewer than a one-line change of a rule. The human reviews a change of
behavior before tests and code build on it, in a future specification
or at the Verification of Specification.

An agent unsure of a choice stops anyway, gate or not: the plan sets
the minimum of attention, never the maximum.


### Supervised increments

Without supervision, the human acts as the orchestrator: approves the
plan, answers the agent, and reviews the specification. Once the human
has approved a future specification that settles every
decision where the human matters, its increments run without the
human. An orchestrator agent runs them one at a time, each by a
sub-agent, plans them from the future specification, and reviews at the
gates. It answers what an agent can decide, and relays to the human
only the decisions where the human matters; such a decision pauses the
supervised work.

At the end of the change, the human tries the software, guided by its
scenarios.


### Version control as the record

The project is a git repository, and the process relies on it instead
of keeping its own records. Each phase ends in one commit, except
Planning, whose plan goes in the increment's first commit. The
commit bodies are the decision record: what was decided and why. The
commits also record the state of the process, so an agent learns where
it stands from the last one, and can restart at any point.

The history is never rewritten. An abandoned increment is reverted, not
erased, so its reasons stay in the history. Work rejected after its
commit is redone in new commits, so the history shows where the gates
fell short.


### Starting a project

The first increment frames the project: its scope, stack and
conventions, through a trivial feature that runs through the whole
stack. Technical choices are hard to reverse, so they are reviewed
before any code exists.

On existing code, the specification starts partial and grows zone by
zone, as the zones need to change. An agent cannot tell intended
behavior from accidental behavior, so the human states what a zone
should do, and the agent confronts it with the code.


### Avoiding specification drift

A specification drifts when the code changes without it. Dev43 keeps
them consistent:

- every change, however small, goes through an increment, and a change
  of behavior updates the main specification first
- a future specification stays applicable to the main one: a change of
  the main specification updates the future versions it breaks
- the specification is minimal, so there is little to go stale
- traceability makes drift visible: a test that no longer matches the
  code fails, and a rule without a test, or a test citing a missing
  rule, is caught

What remains is drift in meaning, such as a test that cites a rule
without truly checking it. The agent checks catch it.


## Future Work

See [BACKLOG.md](../BACKLOG.md).
