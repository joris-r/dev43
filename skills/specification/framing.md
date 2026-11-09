# Framing

Topics for an increment that sets or changes the project's purpose,
stack or conventions. They add to the Specification skill.

## Exploration

Discuss first, before the scope:

1. Purpose: what the software is for, for whom, the main use cases.
2. Constraints: technical, legal, platform, budget, hosting.
3. Out of scope: what it will explicitly not do.
4. Stack: the structuring choices (language, framework, database).
   Raise a real trade-off when there is one; build a throwaway preview
   (see the Specification skill) if a choice needs evidence.
5. Conventions: repo layout, naming, the test and quality policy,
   whether the specification states the messages the user sees, and
   repository files. Most are choices you can make with confidence:
   make them in Production rather than asking.

On a project already framed, raise only the topics the change touches.

When `docs/` is empty, propose as scope a trivial feature that
runs through the whole stack, such as a hello world or a health check.
The real features come in later increments.

On existing code (`Dev43-Specification: partial`), the stack and
conventions already exist: read them from the project and propose
them, rather than comparing options. Raise only what the code cannot
tell (e.g. a convention it breaks often). The scope is `technical.md` alone,
with no feature; a change to the stack or conventions is a
later increment.

## Production

- When `docs/technical.md` does not exist, the change writes it in
  full: the stack, the conventions, and the
  test and quality policy. Decide only what is costly to change later.
  On existing code, it describes them as they are.
- Write `docs/overview.md`: what the software is for, for whom, and
  its non-goals.
- Write or update the project's `README.md`: a few lines on what the
  software is for, and how to run it and its tests. It is context, not
  specification: no tags.
