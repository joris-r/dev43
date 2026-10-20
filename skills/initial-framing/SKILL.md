---
name: initial-framing
description: Dev-4-3 Initial Framing phase for a new project with no code yet. Use when spec/STATE.md says Phase is Initial Framing, or when the human starts a new project with Dev-4-3. Sets the stack, conventions and a running skeleton; delivers no feature.
---

# Initial Framing

Goal: `spec/main/technical.md` exists, a minimal skeleton runs with one
trivial test, and the first increment can start with a small scope.
Decide only what is costly to change later.

This is a bootstrap phase: the only one that writes `spec/main/`
directly, and the only one whose code is not test-first, because it
builds the tooling the cycle depends on. Keep it bounded: the skeleton
implements only technical decisions, and its trivial test checks the
tooling, not a behavior.

## Setup (first use only)

If the project has no `spec/STATE.md`, ask the human to run
`/dev43:init` first.

## Exploration

Peer discussion with the human. Your agenda, not a message template:

1. Purpose: what the software is for, for whom, the main use cases.
2. Constraints: technical, legal, platform, budget, hosting.
3. Out of scope: what it will explicitly not do.
4. Stack: the structuring choices (language, framework, database).
   Raise a real trade-off when there is one; build throwaway
   prototypes (outside the repo or in a scratch folder) if a choice
   needs evidence.
5. Conventions: repo layout, naming, the test and quality policy, and
   repository files. Most are choices you can make with confidence:
   make them in Production rather than asking.

One point per message; raise only what you cannot settle with
confidence, and settle the rest yourself in Production (see
`CLAUDE.md`, Working with the human).

When you have nothing left to raise, propose to end Exploration. It
ends when the human agrees; then set Step to Production in STATE.

## Production

Work without interrupting.

Write `README.md`: a few lines on what the software is for and for
whom, and how to run it and its tests. It is context, not
specification: no IDs.

Write a short `spec/main/technical.md`: the stack, the conventions, and
the test and quality policy. Write nothing else in `spec/main/`: the
data model and the features come with the increments, starting with
the first one.

Then set up the repository (`.gitignore`, lock files as agreed),
tooling, CI, and a minimal skeleton that runs with one trivial test,
following `technical.md`.

In both, tag the choices you are unsure of.

Run the Verification checks and fix what fails. Then mark new files
(`git add -N .`), set Step to Verification in STATE, and hand over
with the check results and the list of tags, with one line on each
saying why.

## Verification

Starts at your hand-over, once the checks below pass.

1. The human reviews the changes (`git diff`), staging each file or
   hunk once read, and rules on each tag or edits the artifacts
   directly.
2. Apply the rulings, remove the tags, and run the checks again. The
   review is done when `git diff` is empty.

Checks:

- The skeleton runs and its trivial test passes.

## Exit

Spec exists, skeleton runs, no tags remain, the human approves. Next
phase: Specification.

On the human's go, set Phase to Specification and Step to Exploration in
STATE, and clear Increment and Scope; then stage all changes and
commit them as `[<increment>] Initial Framing`, where
`<increment>` is the increment that just ended.
