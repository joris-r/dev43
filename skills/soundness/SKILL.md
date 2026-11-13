---
name: soundness
description: Dev43 soundness check of the specification, after the proof obligations of the B method. Run by a sub-agent at the Verification of Specification when the change touches the model, the operations, the UI, the design, the contents or the scenarios; the human may also call it on the whole of docs/. Checks that every operation keeps the invariants, that every extension keeps the operation it extends, and that the documents agree.
---

# Soundness

Load `dev43:core` first if it is not loaded.

Goal: find where the specification is unsound, open or incoherent: a
case of an operation that can break an invariant, as the proof
obligations of the B method would, a state or an input no case
settles, and a document that contradicts another. It is reasoning,
not proof: it reports counterexamples and undecided obligations, never
that the specification is proved.

## Scope

- Called at the Verification of Specification, in a fresh context
  (see `dev43:core`, Agent checks): the operations the change adds or
  changes, the operations whose effects touch an invariant it adds or
  changes, their extensions, and the UI elements, mockups and
  scenarios that the change touches or that use those operations.
  `check.py spec` lists the changed operations with their dependent
  domains and extensions. For a future version, check `docs/` with the
  feature applied.
- Called by the human: all of `docs/`, or the part they name.

## Obligations

The state after a case is what the case states, the rest unchanged.

In scope:

- [initial] The initial state meets every invariant.
- [partition] In every state meeting the invariants, exactly one case
  applies to each input of its type. A case stated as `unspecified`
  counts here and carries no other obligation.
- [invariants] Under the invariants and the case's condition, the
  state after a case meets every invariant of its domain.
- [dependents] It also meets the invariants of every domain that
  depends on its domain.
- [determined] A case fixes the state after it and its result, but
  for the values it leaves free.
- [extension] An extension keeps or weakens the precondition of the
  operation it extends, keeps or strengthens its effects, and the two
  together keep the invariants.
- [migration] For a future version that adds or strengthens an
  invariant: its migration takes every state meeting the invariants
  of `docs/` to a state meeting the new ones.

## Coherence

- [state] Every value an operation reads or changes is declared in
  the model, and every field gets its value from the initial state or
  an operation.
- [display] Every outcome of an operation the UI runs has a display;
  every input of a trigger has a source; every value shown is a
  field, a definition or a result; the UI changes only what is on
  display.
- [design] A mockup shows every element and state of its `ui.md`
  section, and nothing the section lacks.
- [contents] Every section of `contents.md` is cited by a `ui.md`
  element, and every element that carries authored text cites one.
- [scenarios] Walk each scenario from its starting state: each action
  is a trigger of `ui.md`, available at that step, and each thing
  seen is what the operations and the UI give.

## Report

- A counterexample: the case path, the invariant path, and a state
  meeting the invariants and the condition that the case leads out
  of them. For a coherence finding: the two paths that disagree, or
  the path and what it lacks.
- An undecided obligation: the case, the invariant, and what leaves it
  open, e.g. a vague effect or an unstated meaning.
- Otherwise: "no counterexample found", with the obligations checked.

Each finding is a decision for the human: a missing condition, a
changed effect, a wrong invariant, or which document is right. At
Verification, the author marks each one where it applies for the
human. On a call by the human, report them; a fix is an increment.
