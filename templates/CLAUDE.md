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
  and list your tags (file and line), with one line on each `unsure`
  tag saying why.
- Verification: run the checks of the phase (see its skill) and report
  the results, then the human reviews. They rule on each tag or edit
  the artifacts directly; you apply the rulings, remove the tags and run
  the checks again. The step is complete when the checks pass,
  no tag remains (see Tags), and the human approves.
- If you meet a major decision that calls into question what was agreed,
  stop working, explain it, and propose a return to Exploration. Never
  work around it. If the human agrees, set Step to Exploration in STATE.

## Tags

A tag draws the human's attention to something you chose, and records
that they must act on it. It says only how confident you are.

- Tag every choice that neither the specification nor the human
  dictated, on the line where it applies (spec, test or code):
  - `@dev43:sure`: you are confident; a quick look is enough.
  - `@dev43:unsure`: you are not confident; the human must look closely.
    A test you believe is wrong is always `unsure`.
- Write the choice itself as normal content: the artifact must read
  correctly once the tag is removed. Put nothing else in the tag, no
  kind, ID or explanation; explanations go in your hand-over message.
- In Markdown, put the tag in an HTML comment: `<!-- @dev43:unsure -->`.
  In code, use the language's comment syntax.
- If unsure whether something is a choice, tag it.
- The human accepts a tag by removing it, and rejects it by changing
  the content (or asking you to). Never remove a tag yourself unless
  the human has ruled on it.
- No tag remains when both commands print nothing:
  `git diff HEAD | grep '^+.*@dev43:'` and
  `git ls-files -o --exclude-standard -z | xargs -0 -r grep -Hn '@dev43:'`.
  Committed content never holds a real tag, so tags quoted in committed
  documents do not count. To quote a tag in a new document, write
  `@dev43\:`.

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
  tag it `unsure`, explain why in your hand-over, and continue. Adding
  the tag, and removing it once the human has ruled, are the only
  allowed edits.
- Add no dependency, library, service or interface unless the
  specification names it or you tag it.

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
