# Dev-4-3 rules

This project follows the Dev-4-3 process. These rules restrict what you
may do. They override your defaults. When a rule and a request conflict,
stop and ask the human.

Golden rule: humans make every important or impactful decision.

## State and gates

- Before any work, read `spec/STATE.md`. Start every message with
  `[<Phase> · <Step>]` as recorded there.
- Do only the work of the current phase and step. Use the matching
  `dev43:<phase>` skill.
- Never advance the step or phase yourself. You may say a step looks
  complete; only the human decides.
- Production cannot start until the human has declared Exploration over.
- Production ends when you hand over: stage all changes (`git add -A`)
  and list your tags.
- Verification: run the checks of the phase (see its skill) and report
  the results, then the human reviews. They rule on each tag or edit
  the artifacts directly; you apply the rulings, remove the tags and run
  the checks again. The step is complete when the checks pass,
  `git grep -n --untracked "@dev43:decision" -- ':!CLAUDE.md'` returns
  nothing, and the human approves.
- If you meet a major decision that calls into question what was agreed,
  stop working, explain it, and propose a return to Exploration. Never
  work around it. If the human agrees, set Step to Exploration in STATE.

## Decision tags

- Tag every choice that the specification does not dictate, on the line
  where it applies (spec, test or code):
  `@dev43:decision[<kind>] <ID> — <what you chose and why>`
  - `spec`: interpreted a specification decision
  - `tech`: made a technical decision (library, algorithm, structure, interface)
  - `disputed-test`: you believe a test is wrong (Implementation only)
  - `<ID>` is the related decision ID, or `none`.
- In Markdown, put the tag in an HTML comment: `<!-- @dev43:decision[...] ... -->`.
  In code, use the language's comment syntax.
- If unsure whether something is a decision, tag it.
- Never remove a tag unless the human has ruled on it.

## Specification

- Layout: `spec/main/<level>/<domain>.md` and
  `spec/changes/<slug>/<level>/<domain>.md`. Levels:
  `1-functional` (needs, rules, UI), `2-interfaces` (API, data model,
  integrations), `3-technical` (stack, architecture, conventions, test
  and quality policy).
- IDs: `F-<DOMAIN>-<NNN>`, `I-<DOMAIN>-<NNN>`, `T-<DOMAIN>-<NNN>`.
  Each domain file declares its code on its first line:
  `DOMAIN = <CODE>` (upper case, chosen by the human). Several files may
  share a code. Every ID is unique across the whole spec: take the next
  free `<NNN>` for its `F-<DOMAIN>`, `I-<DOMAIN>` or `T-<DOMAIN>` prefix.
  Never reuse the number of a removed ID.
  IDs are created only in the specification. Never invent one elsewhere.
- Cite IDs; never copy decision text into tests or code.
- Links point downward only: level 2 cites level 1, level 3 cites 1 or 2.
- Give a decision a "because" when its reason is not obvious, or when it
  is a trade-off someone might later want to reverse.

## Tests and code

- Every test cites the ID(s) it checks. Non-trivial code cites the ID it
  implements.
- During Implementation, never change test code. If a test seems wrong,
  tag it `disputed-test` with your reasoning and continue. Adding the
  tag, and removing it once the human has ruled, are the only allowed
  edits.
- Add no dependency, library, service or interface unless the
  specification names it or you tag it `tech`.

## Working with the human

- Exploration: discuss as a peer. Ask, challenge, surface decisions.
  The human has the final say.
- Production: work without interrupting; tag instead.

## Git

- The project is a git repository. Use it: `git diff --cached` is what
  you produced in this step, `git diff` what changed during the review,
  `git diff HEAD` the work of the current phase, `git log` the history.
- Stage only at the end of Production. Commit only at the end of a
  phase, on the human's go, after updating STATE:
  `dev43: <increment> — <phase>`. Never commit at any other time.
