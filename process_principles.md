# Dev43: A Software Development Process

This document gives the context and the principles of Dev43. The
operational rules are in the skills ([skills/](skills/)), which apply
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
agent could reasonably have chosen otherwise and the human would care.

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


### A minimal specification

By the silver rule, the specification records only the decisions where
the human matters. Agents derive the rest, in the tests and the code.
The specification stays shorter and more abstract than them, and easy
for a human to read.

It records what is decided, not why: reasoning goes stale. The reasons
live in the history.

It is organized by domain, around the data model and the operations on
it. Each operation states one case per condition, so that gaps and
overlaps show.


### Tests as the guarantee

The test suite is what ensures that the code respects the
specification. Tests are written before the code, from the
specification, and the code is then written to make them pass, without
modifying them.

Every statement of behavior in the specification carries a tag. Every
test cites the tags it checks, and every tag has a test or is marked
not testable. This traceability shows that the specification is fully
covered.

Tests are also the agent's feedback loop: it knows it is done when they
pass.


### The line of responsibility

The human reviews the specification and tries the software. Agents
check the tests and the code, each check in a fresh context, so that
it does not share the blind spots of the author.

An agent never changes a decision the human approved: such a change
goes back to the human, as a change of the specification.

This line holds in every increment, supervised or not.


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
   each choice it is unsure of with a tag on the artifact.
3. **Verification**: the reviewer, the human for the specification,
   rules on the tags and approves.

The steps regulate the interaction between human and agent: important
topics are discussed first, then the agent works unsupervised, and its
tags keep the human aware and involved at Verification.


### Gates follow the impact

The agent stops only where the change can do harm. At the start of
an increment, the agent analyzes the potential impact of the change and
proposes the gates: the steps where it waits for review, by the human
for the specification, by an agent for tests and code. Elsewhere it
goes on alone, and its work is reviewed at the end of the increment,
which is always a gate: the human reviews the specification change
and tries the software. The size of a change does
not set its gates: a large refactoring under unchanged tests may need
fewer than a one-line change of a rule.

An agent unsure of a choice stops anyway, gate or not: the plan sets
the minimum of attention, never the maximum.


### Supervised increments

Without supervision, the human acts as the orchestrator: approves the
plan, answers the agent, and reviews the specification. Once the human has approved a future specification that settles every
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
without truly checking it. Only the human review catches it.


## Future Work

See [BACKLOG.md](BACKLOG.md).
