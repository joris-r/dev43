# Framing

Topics for an increment that sets or changes the project's purpose,
stack or conventions. They add to the Specification skill.

## Exploration

Discuss first, before the scope:

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

On a project already framed, raise only the topics the change touches.

When `spec/main/` is empty, propose as scope a trivial feature that
runs through the whole stack, such as a hello world or a health check.
The real features come in later increments.

## Production

- When `spec/main/technical.md` does not exist, the technical part of
  the change page holds all of it: the stack, the conventions, and the
  test and quality policy. Decide only what is costly to change later.
- Write or update `README.md`: a few lines on what the software is for
  and for whom, and how to run it and its tests. It is context, not
  specification: no IDs.
