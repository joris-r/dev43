# Specifying existing code

Topics for a `specify-existing` increment: it specifies a zone of
existing behavior without changing it. They add to the Specification
skill.

## Exploration

1. Agree on the zone with the human: it becomes a feature-area page of
   `spec/main/`, or extends `data-model.md` or `technical.md`.
2. The human states claims about the zone: entities, rules, examples.
   Do not draft them from the code: it shows what the software does,
   not what was intended. Help with questions.
3. Look for counterexamples to each claim in the code and tests, and
   raise them one per message. The human rules on each:
   - a bug: propose a backlog entry to fix it;
   - an exception: specified, or left unspecified;
   - a wrong claim: refined.
4. Point out behavior of the zone the claims leave out only if the
   human would likely care (silver rule); they decide.

## Production

The change page holds the claims, as refined. What it does not state
stays unspecified. No code changes.
