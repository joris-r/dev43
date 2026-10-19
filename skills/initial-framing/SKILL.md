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
5. Conventions: repo layout, naming, the test and quality policy, and
   repository files: what `README.md` covers, what `.gitignore`
   excludes, whether lock files are committed.
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

Then set up the repository (`README.md`, `.gitignore`, lock files as
agreed), tooling, CI, and a minimal skeleton that runs with one trivial
test, following `stack.md` and `conventions.md`.
Tag every choice they do not dictate.

Stage all changes (`git add -A`) and hand over with the list of tags,
with one line on each `unsure` tag saying why.

## Verification

Starts when the human declares Production over: set Step to
Verification in STATE.

1. Run the checks below and report the results, with the list of
   remaining tags.
2. The human reviews every produced artifact (`git diff --cached`) and
   rules on each tag or edits the artifacts directly. Apply the rulings,
   remove the tags, and run the checks again.

Checks:

- The skeleton runs and its trivial test passes.

## Exit

Spec exists, skeleton runs, no tags remain, the human approves. Next
phase: Specification.

On the human's go, set Phase to Specification and Step to Exploration in
STATE, and clear Increment and Scope; then stage all changes and
commit them as `dev43: <increment> — Initial Framing`, where
`<increment>` is the increment that just ended.
