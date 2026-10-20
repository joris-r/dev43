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

The silver rule is its dual, and limits how much humans are involved: a
statement belongs in the specification only if a competent agent could
reasonably have chosen otherwise and the human would care.

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

The specification is minimal, by the silver rule. Agents are good at
deriving details, so it records only the decisions where the human
matters. Everything else is derived by the agents in the tests and
the code, and brought to the human's attention by tags when they are
unsure. The specification must remain shorter and more abstract than
the tests and the source code, and easy for a human to read.

A decision states what is decided, not why: reasoning goes stale as the
project moves on. The reasons are discussed in Exploration and kept in
the commit message of the phase.

All work starts with the specification. Writing it after the code tends
to describe what the code does rather than what was needed, and bakes in
accidental decisions.

The specification is a living document: it evolves through change
specifications, which are merged into the main specification at Integration.

The specification starts from the data model. It settles many
decisions on its own and defines the vocabulary: everything else refers
to things by their names. It favors examples (a terminal session, a
request and its response, a sample file) over prose, with a few rules
for what the examples do not show, and uses nested lists rather than
tables, which are hard to read, edit and diff.

Tests and code refer to the specification by these names, never by
repeating it. Only a free-text rule that has no natural name, and that a
test or code must cite, gets a short unique ID.

The main specification is a few pages: the data model, the technical
decisions, and one page per feature area. A change specification is a
single page.


### Working with Agents

The Exploration step is a discussion between peers, the human and the
agent: short messages that answer each other, one point at a time, not
a finished survey that the human answers by numbers. The subject is
approached gradually until the important decisions surface. A point
the human does not react to counts as accepted. The step ends when both
consider the subject mature: the agent may propose to end it, the human
has the final say.

Exploration stays coarse. It raises only what the agent cannot settle
with confidence: the human's goals and preferences, real trade-offs,
choices the agent is unsure of. A choice the agent would recommend with
confidence is not asked; it is made in Production, where reviewing it
is cheap. The split between Exploration and Production
exists to reduce the discussion.

In the Production step, the agent works without interruption and tags
each choice it is unsure of, directly on the relevant line of the
specification, tests or source code. Before handing over, it runs the
checks of the phase and fixes what fails, so that the human reviews
only work that passes them. The hand-over moves the phase to
Verification: there is nothing for the human to decide at that point.

A tag draws the human's attention to a doubt and records that they must
act. A choice the agent is confident of is not tagged: tagging it
would cost a ruling for nothing, and the human sees it in the review
anyway. The artifact itself stays complete without the tag; the human
accepts a choice by removing its tag, and rejects it by changing the
content. A choice is tagged once, at its most
authoritative place (specification, then tests, then code).

In the Verification step, the human reviews every produced artifact
once, with particular attention to the tagged choices, and rules on
each tag or edits the artifacts directly. The agent applies the rulings
and runs the checks again. The step is complete when the checks pass,
no tags remain and the human approves. A check is kept only if it is
cheap to run and has an obvious use; some phases have almost none.

Gates between steps and phases cost a human message each. A plain
approval with no change request passes the gate in front of the agent,
which says which gate it passed.

Reviewing afterward, in context, is more efficient than interrupting the
agent, since the main decisions have normally already surfaced during
Exploration. If the agent nevertheless meets a major decision, one that
calls into question what was agreed, it stops and the work returns to
Exploration.


### Version Control

The project is a git repository. Git gives the history and the current
changes for free, so the process relies on it instead of keeping its own
records.

- The index belongs to the human. At the end of Production, the agent
  only marks new files as intended to be added, so that they show in
  `git diff`. During Verification, the human stages each file or hunk
  once read: `git diff --cached` shows what is reviewed and `git diff`
  what remains. The goal of the review is agreement on the content,
  not a record of who wrote what.
- At the end of each phase, on the human's go, the agent commits. Each
  commit holds one phase of one increment, so `git diff HEAD` shows the
  work of the current phase.

Apart from one commit when Dev-4-3 is set up, and the Amendment commit
of the Implementation phase, nothing is committed at any other time.


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
  for whom, how to run it), then a short draft of the technical page
  of the specification with tags: technical choices, project
  conventions including the test and quality policy. Nothing else is
  specified: the data model and the features come with the increments.
  Only what is costly to change later is decided. Then concrete setup:
  repository (ignore rules, lock files), tooling, CI, a minimal
  skeleton that runs with a trivial test.
- **Verification**: the skeleton runs with its trivial test; human
  review.

Exit: the technical page of the main specification exists, the
skeleton runs, and the first increment can start with a small scope.


## Specification Phase

- **Exploration**: frame the topic, explore the web, documents, existing
  code and tests.
- **Production**: a minimal change specification on one page: data
  model first, then behavior with examples, then technical decisions.
  It names what it modifies or removes. Edge cases are left to the
  Tests phase.
- **Verification**: `spec/main/` is unchanged; human review, including
  the size of the increment (possible verdict: too big, split it).


## Tests Phase

- **Exploration**: what to test; edge cases are settled here, by
  tests, and raised to the human only when a test cannot choose; flag
  rules that cannot be tested; propose an update of the test and quality policy
  if the increment brings new needs.
- **Production**: tests, each citing what it checks by its name in the
  specification or by its rule ID.
- **Verification**: every new or modified rule ID has a test or is
  marked not testable; every rule ID cited in tests exists; the new
  tests fail for the right reason. Then the human reviews the test
  suite (does each part of the change have tests, and does each test
  truly express it?). This review deserves
  particular care: checking behavior through tests is more efficient
  than through the code they constrain.

The test and quality policy is a project decision, recorded in the
technical page of the specification: a first version in Initial
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

A small addition to the specification during Implementation (a rule or
an example that one or two new tests can check) does not need a full
return: the agent writes the specification line and its tests together,
checks that the tests fail for the right reason, and the human approves
both in one gate. It is committed as an Amendment. Anything larger goes
back through Specification or Tests.


## Integration Phase

- **Exploration**: retrospective on the process itself (rules, agent
  context, thresholds).
- **Production**: in-place rewrite of the main specification, each
  part of the change in the page it belongs to, then removal of the
  change specification.
- **Verification**: the full test suite passes, no rule ID is defined
  twice in the main specification, every rule ID cited in tests or code
  exists,
  and the change specification is removed; human review.


## Future Work

### Retro-Specification Phase

Adopting Dev-4-3 on a project that already has code is not supported
yet. A Retro-Specification phase would replace Initial Framing: it would
write the main specification from the existing software, telling
intended behavior apart from accidental behavior, so that the
specification describes what is needed, not just what the code does.
