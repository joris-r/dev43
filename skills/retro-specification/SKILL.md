---
name: retro-specification
description: Dev-4-3 Retro-Specification phase for a project that already has code. Use when spec/STATE.md says Phase is Retro-Specification, or when the human adopts Dev-4-3 on an existing codebase. Writes the main specification from the existing software, separating intended from accidental behavior.
---

# Retro-Specification

Goal: a main specification that describes what is needed, not merely
what the code does, plus a list of known gaps between code and spec.

## Setup (first use only)

If the project has no `spec/STATE.md`, ask the human to run
`/dev43:init` first.

## Exploration

1. Read the code, tests, docs, commit history and issues. Map the
   domains, the existing stack and the existing test and quality
   practices.
2. Discuss with the human: what the software is for, for whom, which
   behaviors are known to be intended, accidental or wrong.
3. Propose a split into domains, each with a short `DOMAIN` code; the
   human decides.
4. List behaviors whose intent you cannot infer. Ask about the important
   ones; the rest will be tagged.

End when the human says Exploration is over; then set Step to
Production in STATE.

## Production

Work without interrupting. Write the draft in `spec/main/` using the
three levels (`1-functional`, `2-interfaces`, `3-technical`), split by
domain, each file starting with its `DOMAIN = <CODE>` line, each
decision with an ID (and a "because" when not obvious).

- Tag `spec` every behavior whose intent is uncertain. The human rules
  on each: keep (in the spec), change in a later increment (add it to
  the list of differences), or leave out of the spec (accidental or
  irrelevant; the code stays as is).
- Do not describe code mechanics; describe the decision behind them.
- Write the test and quality policy in `3-technical/`, as practiced today.
- List the known differences between code and spec, in a place the
  human chooses.
- Link existing tests to IDs (comment citing the ID) where possible.
  Never change test logic in this phase.

Hand over for human review, tags first.

## Verification

Starts when the human declares Production over: set Step to
Verification in STATE.

Cycle until a round adds no new tags:

1. Spawn a subagent with only the spec paths, the source tree and the
   tests, with this checklist: does each decision match the code;
   behaviors in the code missing from the spec; spec text that just
   paraphrases code; vagueness, repetition; tests linked to the wrong
   ID. Tell it to tag each problem in place with
   `@dev43:decision[verify]`, not to fix anything, and to return a list.
2. The human rules on each tag; a tagged behavior gets the same options
   as in Production.
3. Repeat.

## Exit

Spec exists, gaps listed, no tags remain, the human approves. Next
phase: Specification.

On the human's go, set Phase to Specification and Step to Exploration in
STATE, and clear Increment and Scope.
