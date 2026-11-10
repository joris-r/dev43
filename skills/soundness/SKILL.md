---
name: soundness
description: Dev43 soundness check of the specification, after the proof obligations of the B method. Run by a sub-agent at the Verification of Specification when the change adds or changes an operation or an invariant; the human may also call it on the whole of docs/. Checks that every operation keeps the invariants, and that every extension keeps the operation it extends.
---

# Soundness

Load `dev43:core` first if it is not loaded.

Goal: find each case of an operation that can break an invariant, as
the proof obligations of the B method would. It is reasoning, not
proof: it reports counterexamples and undecided obligations, never
that the specification is proved.

## Scope

- Called at the Verification of Specification, in a fresh context
  (see `dev43:core`, Agent checks): the operations the change adds or
  changes, the operations whose effects touch an invariant it adds or
  changes, and their extensions. `check.py spec` lists the changed
  operations with their dependent domains and extensions. For a future
  version, check `docs/` with the feature applied.
- Called by the human: every operation of `docs/`, or the part they
  name.

## Obligations

For each case of an operation in scope:

- [invariants] Under the invariants and the case's condition, its
  effects keep every invariant of its domain they touch.
- [dependents] They also keep the invariants of every domain that
  depends on its domain.
- [extension] An extension keeps or weakens the precondition of the
  operation it extends, keeps or strengthens its effects, and the two
  together keep the invariants.

## Report

- A counterexample: the case path, the invariant path, and a state
  meeting the invariants and the condition that the effects lead out
  of them.
- An undecided obligation: the case, the invariant, and what leaves it
  open, e.g. a vague effect or an unstated meaning.
- Otherwise: "no counterexample found", with the obligations checked.

Each finding is a decision for the human: a missing condition, a
changed effect, or a wrong invariant. At Verification, the author
marks each one on its case for the human. On a call by the human,
report them; a fix is an increment.
