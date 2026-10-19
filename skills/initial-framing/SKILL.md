---
name: initial-framing
description: Dev-4-3 Initial Framing phase for a new project with no code yet. Use when spec/STATE.md says Phase is Initial Framing, or when the human starts a new project with Dev-4-3. Sets vision, stack, conventions and a running skeleton; delivers no feature.
---

# Initial Framing

Goal: the main specification exists, a minimal skeleton runs with one
trivial test, and the first increment can start with a small scope.
Decide only what is costly to change later.

## Setup (first use only)

If the project has no `spec/STATE.md`, ask the human to run
`/dev43:init` first.

## Exploration

Peer discussion with the human. Cover, one topic at a time:

1. Purpose: what the software is for, for whom, the main use cases.
2. Constraints: technical, legal, platform, budget, hosting.
3. Out of scope: what it will explicitly not do.
4. Stack: compare candidate languages, frameworks, databases and key
   libraries. Give trade-offs and a recommendation. Build throwaway
   prototypes (outside the repo or in a scratch folder) if a choice
   needs evidence.
5. Conventions: repo layout, naming, and the test and quality policy.
6. Domain code: propose `MAIN` by default, since no specific domain is
   in play yet; the human decides.

Surface decisions; don't settle them alone. End when the human says
Exploration is over; then set Step to Production in STATE.

## Production

Work without interrupting. Write a short draft in `spec/main/`:

- `1-functional/vision.md`: purpose, users, main use cases, UX
  principles, out of scope.
- `3-technical/stack.md`: each technical choice with its "because".
- `3-technical/conventions.md`: layout, naming, test and quality policy.
- `2-interfaces/` only if an interface decision is already costly to change.

Start each file with the agreed `DOMAIN` line. Give each decision an
ID. Tag every choice the human did not explicitly make.

Then set up the repository, tooling, CI, and a minimal skeleton that
runs with one trivial test, following `stack.md` and `conventions.md`.
Tag every choice they do not dictate.

Hand over for human review of every file, tags first.

## Verification

Starts when the human declares Production over: set Step to
Verification in STATE.

Cycle until a round adds no new tags:

1. Spawn a subagent with only the paths of the spec files and the
   skeleton, and this checklist: consistency, repetition, vagueness,
   decisions that are cheap to change and could be dropped, missing ID
   or broken downward links; skeleton matches the spec and runs with
   its trivial test. Tell it to tag each problem in place with
   `@dev43:decision[verify]`, not to fix anything, and to return a list.
2. The human rules on each tag; apply the rulings and remove those tags.
3. Repeat.

## Exit

Spec exists, skeleton runs, no tags remain, the human approves. Next
phase: Specification.

On the human's go, set Phase to Specification and Step to Exploration in
STATE, and clear Increment and Scope.
