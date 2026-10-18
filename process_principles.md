# Dev-4-3: A Software Development Process

## Context and Goal

Dev-4-3 is a software development methodology for human and LLM agents based on
the specification driven development (SDD) ideas.

There are four main phases:

1. Specification
2. Tests (writing of)
3. Implementation
4. Integration

They are repeated for each increment. Two special phases may come first:

- Initial Framing (new project)
- Retro-Specification (existing project)

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

The specification records only the decisions an agent could not guess,
together with their rationale. It must remain shorter and more abstract
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

In the Production and Verification steps, the agent works without
interruption and tags each place where it made a decision, directly on
the relevant line of the specification, tests or source code. At the end
of the step, the human reviews every produced artifact, with particular
attention to the tagged decisions. The step is complete only when no tags
remain.

The Verification step starts with an agent in a fresh context, so that it
judges the artifacts on their own rather than through the reasoning that
produced them. Verification is cyclic: after each human review, the agent
verifies again, until no new tags appear.

Reviewing afterward, in context, is more efficient than interrupting the
agent, since the main decisions have normally already surfaced during
Exploration. If the agent nevertheless meets a major decision, one that
calls into question what was agreed, it stops and the work returns to
Exploration.


## Initial Framing Phase

This phase sets up a new project before the first increment: the
overall vision, the technical stack, the conventions and a minimal
running skeleton. It delivers no feature.

- **Exploration**: peer-to-peer discussion of the overall scope (what
  the software is for, for whom, technical, legal and platform
  constraints, out of scope). The agent compares structuring stacks and
  libraries, with throwaway prototypes if useful.
- **Production**: a short draft with decision tags: overall vision
  (functional and UX), technical choices with their "because," project
  conventions. Only what is costly to change later is decided.
- **Verification**: fresh-context review until convergence, then
  concrete setup: repository, tooling, CI, a minimal skeleton that runs
  with a trivial test.

Exit: the main specification exists, the skeleton runs, and the
first increment can start with a small scope.


## Retro-Specification Phase

This phase replaces Initial Framing when the project already has code.
It writes the main specification from the existing software. The main
task is to tell intended behavior apart from accidental behavior, so that
the specification describes what is needed, not just what the code does.

- **Exploration**: read the existing code, tests and documentation;
  discuss with the human what the software is for and which behaviors
  are known to be intended, accidental or wrong.
- **Production**: a draft main specification derived from the code,
  with decision tags on every behavior whose intent is uncertain.
- **Verification**: fresh-context review until convergence; the human
  rules on each tagged behavior (keep, change in a later increment, or
  drop); existing tests are linked to unique IDs where possible.

Exit: the main specification exists, known gaps between the code and
the specification are listed, and the first increment can start with a
small scope.


## Specification Phase

- **Exploration**: frame the topic, explore the web, documents, existing
  code and tests.
- **Production**: a short change specification that cites the unique
  IDs of the modified decisions.
- **Verification**: consistency, repetition, vagueness, decisions
  without a "because"; size of the increment (possible verdict: too big,
  split it).


## Tests Phase

- **Exploration**: what to test, which edge cases; flag decisions that
  cannot be tested.
- **Production**: tests each linked to a decision by its unique ID.
- **Verification**: the human reviews the test suite (does each test
  truly express the decision?); coverage and decision-to-test links
  checked. This review deserves particular care: checking behavior
  through tests is more efficient than through the code they constrain.

Test types, coverage threshold and use of mutation testing are
project decisions, recorded in the project's specification.


## Implementation Phase

- **Exploration**: read the existing code, flag fragile areas and
  divergences.
- **Production**: autonomous coding until tests are green, deviations
  tagged.
- **Verification**: tests, lint, typing, static analysis; the human
  handles the tags and reviews the produced code.

Technical choices (stack, libraries, algorithms, communication
interfaces) are important decisions like any other, because they are
hard to reverse.

Tests are never modified during Implementation. If the agent believes a
test is wrong, it leaves it unchanged, tags it as disputed with its
reasoning, and continues. At review, the human rules: either the code is
fixed, or the test is corrected in a return to the Tests phase, or, if
the test faithfully expresses a wrong decision, the work returns to the
Specification phase.

In code, at least three kinds of deviation are distinguished, so review
can go by severity: disputed test, interpreted specification decision,
important technical decision.


## Integration Phase

- **Exploration**: gaps between what was planned and what was delivered,
  decisions that moved; retrospective on the process itself (rules,
  agent context, thresholds).
- **Production**: in-place rewrite of the main specification.
- **Verification**: global fresh-context review, condensation, removal
  of the change specification, resolution of ID conflicts.
