---
name: supervise
description: Dev43 supervised increments. Use when the human asks to carry out the outline of a feature of docs_future/ without them. Orchestrates one sub-agent per increment, answers what an agent can decide, and relays to the human only the decisions where the human matters.
---

# Supervise

Load `dev43:core` first if it is not loaded.

Goal: the increments of a feature's outline carried out one at a time,
each by a sub-agent, with the human involved only where they matter.
You are the orchestrator: you hold the role the human holds in an
unsupervised increment, for everything but the specification.

## Start

- Supervised work starts in Pause, on a feature whose
  `docs_future/<feature>/` the human has approved and which settles
  every decision where the human matters. If one remains open, raise
  it first: it is a `future` increment. So is a finding of the script
  checks of the specification: run them before the first increment.
- Tell the human the increments of the outline you will run, and start
  on their `next`.
- Your messages start with `[Supervise · <feature>]`.

## State

Read it from the commits (see `dev43:core`, State) and
`docs_future/<feature>/BACKLOG.md`: the next increment is the first of
the outline. You can restart at any point. An increment left
uncommitted by an interrupted sub-agent: tell the human.

## Each increment

1. Plan it, as in `dev43:planning`, from the outline and the lessons.
   You approve the plan; its gates are for you and the agent checks.
2. Start one sub-agent for it, with a fresh context. Give it the plan,
   and tell it that it runs under supervision: it loads `dev43:core`,
   addresses you instead of the human, and stops at each gate and each
   point it cannot settle, ending its message with what it needs.
3. Answer what an agent can decide. Pass its gates with `next` once
   their checks pass. Run each agent check in a fresh context of its
   own.
4. A decision where the human matters (a mark on the specification, an
   Amendment, an escalation, a return to Specification) pauses the
   supervised work:
   relay it to the human in a few lines, wait, and pass on the answer.
5. At its final review, check that its specification change only moves
   sections of `docs_future/<feature>/` into `docs/`, and that the
   script checks pass. Rule on its retrospective: the lessons go under
   `## Lessons` in `docs_future/<feature>/BACKLOG.md`, the project and
   process points under `## For the human`, both in the increment's
   last commit. An important lesson pauses the supervised work: it
   needs a `future` increment.
6. Wait for the increment's last commit before the next one.

## End

When the last increment has deleted `docs_future/<feature>/`, hand
over to the human:

- what the feature changed for a user, and its scenarios, to try the
  software by them;
- the points of `## For the human`, which the last increment moved to
  `docs_future/BACKLOG.md`, each in a line or two. They rule on each;
  the rejected ones leave the backlog.

On their approval, Pause. A problem they find is a new increment.
