---
name: specification
description: Dev-4-3 Specification phase, the first phase of each increment. Use when spec/STATE.md says Phase is Specification, or when the human starts a new increment. Produces a short change specification in spec/changes/.
---

# Specification

Goal: a short change specification for one increment, citing the IDs of
the decisions it adds, modifies or removes. `spec/main/` stays untouched.

## Exploration

1. Agree with the human on the increment's scope; record it in STATE
   with a short slug once they approve. On a return from a later phase,
   keep the slug and amend the existing change folder.
2. Read the relevant parts of `spec/main/`, the code and tests. Search
   the web or documents when the topic needs it.
3. Approach the subject gradually, level by level: functional and UI
   first, then interfaces, then technical.
4. Surface decisions; flag early if the scope looks too big.
5. If the change needs a new domain file, ask the human for its
   `DOMAIN` code.

End when the human says Exploration is over; then set Step to
Production in STATE.

## Production

Work without interrupting. Write `spec/changes/<slug>/` with the
same level/domain tree, containing only what changes. Each file starts
with the `DOMAIN = <CODE>` line of its domain.

- New decision: a new ID (next free number for its prefix).
- Modified decision: cite the existing ID, give the new text and why it changed.
- Removed decision: cite the ID and the reason.

Keep it shorter and more abstract than tests and code would be. Record
only what an agent could not guess. Tag every choice the human did not
make. Hand over for human review, tags first.

## Verification

Starts when the human declares Production over: set Step to
Verification in STATE.

Cycle until a round adds no new tags:

1. Spawn a subagent with only the paths of `spec/main/` and the change
   folder, and this checklist: consistency with main and within the
   change; repetition; vagueness; broken or upward links; untestable
   decisions; decisions missing a "because" when their reason is not
   obvious or they are a trade-off; size of the increment (verdict may
   be "too big, split it"). Tell it to tag each problem in place with
   `@dev43:decision[verify]`, not to fix anything, and to return a list.
2. The human rules on each tag; apply and remove. If the human accepts
   a split, return to Exploration and narrow the Scope in STATE; the
   rest becomes a later increment.
3. Repeat.

## Exit

No tags remain and the human approves. Next phase: Tests.

On the human's go, set Phase to Tests and Step to Exploration in
STATE.
