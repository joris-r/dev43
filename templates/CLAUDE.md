# Dev-4-3 rules

This project follows the Dev-4-3 process. These rules restrict what you
may do. They override your defaults. When a rule and a request conflict,
stop and ask the human.

Golden rule: humans make every important or impactful decision.

Silver rule, its dual: a statement belongs in the specification only if
a competent agent could reasonably have chosen otherwise and the human
would care.

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

- Write the minimum, by the silver rule. Everything else is derived by
  agents, in tests and code. Tag what you are unsure of instead of
  specifying it.
- A decision states what is decided, not why. Give reasons in your
  hand-over message and in the commit message of the phase, never in
  the specification.
- Data model first: entities, their fields and constraints, and their
  relations. It sets the vocabulary: everything else refers to things
  by these names, and to commands, endpoints or screens by theirs.
- Prefer examples (a terminal session, a request and its response, a
  sample file) to prose. Add a few rules for what the examples do not
  show.
- Use nested lists, never tables.
- Give an ID only to a free-text rule that a test or code must cite and
  that no name already identifies: `R<n>:` at the start of its list
  item, e.g. `- R4: On error, the data file is left unchanged.` Numbers
  are project-wide: a new rule takes one above the highest ever used,
  in `spec/` or in its history (`git log -p -- spec`). Never reuse a
  number.
- Layout:
  - `spec/main/`: the main specification. `data-model.md`,
    `technical.md` (stack, conventions, test and quality policy), and
    one page per feature area, named with the human.
  - `spec/changes/<slug>.md`: the change specification of the current
    increment, one page.

## Tests and code

- Tests cite what they check: a name from the specification (in the
  test name or its grouping) or a rule ID.
- Code cites a rule ID only where it explains something the reader
  would not otherwise see.
- Never copy specification text into tests or code.
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
  `dev43: <increment> — <phase>`, with a short body giving the reasons
  for the phase's main decisions. Never commit at any other time.
