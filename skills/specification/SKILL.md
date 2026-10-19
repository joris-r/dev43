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
make. Stage all changes (`git add -A`) and hand over with the list of tags.

## Verification

Starts when the human declares Production over: set Step to
Verification in STATE.

1. Run the checks below and report the results, with the list of
   remaining tags.
2. The human reviews every produced artifact (`git diff --cached`) and
   rules on each tag or edits the artifacts directly. Apply the rulings,
   remove the tags, and run the checks again.

Checks:

- `spec/main/` is unchanged (`git diff HEAD -- spec/main` is empty).

The human also judges the size of the increment. If they decide to
split it, return to Exploration and narrow the Scope in STATE; the rest
becomes a later increment.

## Exit

No tags remain and the human approves. Next phase: Tests.

On the human's go, set Phase to Tests and Step to Exploration in
STATE; then stage all changes and
commit them as `dev43: <increment> — Specification`.
