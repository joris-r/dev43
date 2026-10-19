# Dev-4-3: A Software Development Process

## Context and Goal

Dev-4-3 is a software development methodology for human and LLM agents based on
the specification driven development (SDD) ideas.

There are four main phases:

1. Specification
2. Tests (writing of)
3. Implementation
4. Integration

They are repeated for each increment. A special phase, Initial Framing,
comes first in a new project.

Each phase, main or special, follows three steps:

1. Exploration
2. Production
3. Verification

The golden rule of Dev-4-3 is: humans must be involved in every
important or impactful decision.

The main goal is to ensure that the user needs are correctly identified
and fulfilled by the produced software.

This process does not prioritize the production speed and explicitly
limits the AI agents' freedom.


## Rationale

LLM agents are highly effective at deriving patterns from their training
data. They can also generalize and recombine these patterns, which gives
them a form of logical inference.

However, they lack some qualities essential to software authors:

- they cannot retain what they learn across sessions
  - at the time of writing, their only memory is the context window of
    the current session
- their knowledge comes from written training material, not lived experience
  - in an agentic setting, they can get feedback from the software itself
    (tests, compiler errors, program output)
  - but they have no direct access to the human context

This means we must:

- give agents an accurate, human-validated specification of what is being built
  - which also serves as their persistent memory
- keep humans in control of decisions that require context


## Principles

### Incremental Development

The software is developed incrementally, in change sets of manageable size
and complexity. Small increments let humans review each change properly and
let agents hold the whole change within their context window.

Each increment's changes are described in a dedicated change specification,
separate from the main specification. The main specification remains
untouched during the increment, so it always describes the software as it
currently exists.

In the Integration phase, the change specification is merged into the main
documents, and the next increment can start.


### Specification

The specification records only the decisions an agent could not guess.
A decision states what is decided, not why: reasoning goes stale as the
project moves on. The reasons are discussed in Exploration and kept in
the commit message of the phase. The specification must remain shorter and more abstract
than the tests and the source code, and easy for a human to read.

All work starts with the specification. Writing it after the code tends
to describe what the code does rather than what was needed, and bakes in
accidental decisions.

The specification is a living document: it evolves through change
specifications, which are merged into the main specification at Integration.

Requirements and decisions are identified by unique IDs and are
cross-referenced, never repeated, between the specification, the tests
and the source code. This lets Verification check that every requirement
is tested and implemented.

Specification documents are split first by level, then by domain.


### Working with Agents

The Exploration step is a discussion between peers, the human and the
agent. The subject is approached gradually until the important decisions
surface. The step ends when both consider the subject mature; the human
has the final say.

In the Production step, the agent works without interruption and tags
each place where it made a choice, directly on the relevant line of
the specification, tests or source code. Then it hands over.

A tag draws the human's attention and records that they must act. It
carries only the agent's confidence: sure (a quick look is enough) or
unsure (look closely). The artifact itself stays complete without the
tag; the human accepts a choice by removing its tag, and rejects it by
changing the content.

In the Verification step, the agent first runs the checks of the phase.
A check is kept only if it is cheap to run and has an obvious use; some
phases have almost none. Then the human reviews every produced artifact
once, with particular attention to the tagged choices, and rules on
each tag or edits the artifacts directly. The agent applies the rulings
and runs the checks again. The step is complete when the checks pass,
no tags remain and the human approves.

Reviewing afterward, in context, is more efficient than interrupting the
agent, since the main decisions have normally already surfaced during
Exploration. If the agent nevertheless meets a major decision, one that
calls into question what was agreed, it stops and the work returns to
Exploration.


### Version Control

The project is a git repository. Git gives the history and the current
changes for free, so the process relies on it instead of keeping its own
records.

- At the end of Production, the agent stages all changes. During
  Verification, `git diff --cached` shows what the agent produced and
  `git diff` what changed during the review.
- At the end of each phase, on the human's go, the agent commits. Each
  commit holds one phase of one increment, so `git diff HEAD` shows the
  work of the current phase.

Apart from one commit when Dev-4-3 is set up, nothing is staged or
committed at any other time.


## Initial Framing Phase

This phase sets up a new project before the first increment: a short
README, the technical stack, the conventions and a minimal running
skeleton. It delivers no feature, and specifies none.

It is a bootstrap phase, and the only exception to two rules: it writes
the main specification directly, and its code is not written test-first.
The normal cycle needs a stack and test tooling, so they cannot go
through it. The exception is bounded: the skeleton implements only
technical decisions, and its trivial test checks the tooling, not a
behavior.

- **Exploration**: peer-to-peer discussion of the overall scope (what
  the software is for, for whom, technical, legal and platform
  constraints, out of scope). The agent compares structuring stacks and
  libraries, with throwaway prototypes if useful.
- **Production**: a README of a few lines (what the software is for,
  for whom, how to run it), then a short draft of the technical level
  of the specification with tags: technical choices, project
  conventions including the test and quality
  policy. Nothing is written at the functional or interface level.
  Only what is costly to change later is decided. Then concrete setup:
  repository (ignore rules, lock files), tooling, CI, a minimal
  skeleton that runs with a trivial test.
- **Verification**: the skeleton runs with its trivial test; human
  review.

Exit: the technical level of the main specification exists, the
skeleton runs, and the first increment can start with a small scope.


## Specification Phase

- **Exploration**: frame the topic, explore the web, documents, existing
  code and tests.
- **Production**: a short change specification that cites the unique
  IDs of the modified decisions.
- **Verification**: `spec/main/` is unchanged; human review, including
  the size of the increment (possible verdict: too big, split it).


## Tests Phase

- **Exploration**: what to test, which edge cases; flag decisions that
  cannot be tested; propose an update of the test and quality policy
  if the increment brings new needs.
- **Production**: tests each linked to a decision by its unique ID.
- **Verification**: every new or modified decision has a test or is
  marked not testable; every test cites an existing ID; the new tests
  fail for the right reason. Then the human reviews the test suite
  (does each test truly express the decision?). This review deserves
  particular care: checking behavior through tests is more efficient
  than through the code they constrain.

The test and quality policy is a project decision, recorded in the
technical level of the specification: a first version in Initial
Framing, updated in the Tests phase when an
increment brings new needs.


## Implementation Phase

- **Exploration**: read the existing code, flag fragile areas and
  divergences.
- **Production**: autonomous coding until tests are green, deviations
  tagged.
- **Verification**: the full test suite passes, the checks required by
  the test and quality policy pass, and the test files are unchanged
  since the Tests phase (`git diff HEAD`); the human handles the tags
  and reviews the produced code.

Technical choices (stack, libraries, algorithms, communication
interfaces) are important decisions like any other, because they are
hard to reverse.

Tests are never modified during Implementation. If the agent believes a
test is wrong, it leaves it unchanged, tags it unsure with its
reasoning in the hand-over, and continues. At review, the human rules: either the code is
fixed, or the test is corrected in a return to the Tests phase, or, if
the test faithfully expresses a wrong decision, the work returns to the
Specification phase.

A disputed test is always tagged unsure: it contradicts a suite the
human approved.


## Integration Phase

- **Exploration**: retrospective on the process itself (rules, agent
  context, thresholds).
- **Production**: in-place rewrite of the main specification,
  resolving ID conflicts, then removal of the change specification.
- **Verification**: the full test suite passes, no ID is defined twice
  in the main specification, every ID cited in tests or code exists,
  and the change specification is removed; human review.


## Future Work

### Retro-Specification Phase

Adopting Dev-4-3 on a project that already has code is not supported
yet. A Retro-Specification phase would replace Initial Framing: it would
write the main specification from the existing software, telling
intended behavior apart from accidental behavior, so that the
specification describes what is needed, not just what the code does.
