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


### Tests as the guarantee

The test suite is what ensures that the code respects the
specification. Tests are written before the code, from the
specification, and the code is then written to make them pass, without
modifying them.

Every test cites what it checks in the specification, and every
specified rule has a test or is marked not testable. This downward
traceability lets the human check that the specification is fully
covered.

Tests are also the agent's feedback loop: it knows it is done when they
pass.

Tests deserve the most careful review: they make explicit the cases
that code leaves implicit, and checking behavior through them is
cheaper than through the code.


### Small increments

The software grows in increments small enough for a human to review
properly and for an agent to hold in its context.

Each increment is described by a change specification, separate from the
main one, so the main specification always describes the software as it
exists. The change is merged at the end of the increment.


### Four phases

An increment goes through four phases, each producing one artifact:

1. **Specification**: the change specification.
2. **Tests**: tests that express it.
3. **Implementation**: code that makes the tests pass.
4. **Integration**: the change merged into the main specification, and
   a retrospective.

An increment goes through only the phases whose artifact changes: a
refactoring needs no new tests, a tooling update needs no specification.


### Discuss, then produce, then review

Each phase follows three steps:

1. **Exploration**: a discussion between peers, one point at a time,
   raising only what the agent cannot settle with confidence.
2. **Production**: the agent works without interruption, and marks
   each choice it is unsure of with a tag on the artifact.
3. **Verification**: the human reviews the result, rules on the tags,
   and approves.

The steps regulate the interaction between human and agent: important
topics are discussed first, then the agent works unsupervised, and its
tags keep the human aware and involved at Verification.


### Version control as the record

The project is a git repository, and the process relies on it instead
of keeping its own records. Each phase ends in one commit, and the
commit bodies are the decision record: what was decided and why. An
abandoned increment is reverted, not erased, so its reasons stay in the
history.


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
  of behavior updates the main specification at its end
- the specification is minimal, so there is little to go stale
- traceability makes drift visible: a test that no longer matches the
  code fails, and a rule without a test, or a test citing a missing
  rule, is caught

What remains is drift in meaning, such as a test that cites a rule
without truly checking it. Only the human review catches it.


## Future Work

See [BACKLOG.md](BACKLOG.md).
