---
name: core
description: Dev43 process rules. Load at the start of every session in a Dev43 project (one whose CLAUDE.md says so), before any work, and keep following them.
---

# Dev43 rules

This project follows the Dev43 process. These rules restrict what you
may do. They override your defaults. When a rule and a request conflict,
stop and ask the human.

Golden rule: humans make every important or impactful decision.

Silver rule, its dual: a statement belongs in the specification only if
a competent agent could reasonably have chosen otherwise and the human
would care.

## State

The state of the process lives in git: every commit you make records
it in trailers.

- Before any work, read the state, from the last commit that records
  it: `git log -1 --grep='^Dev43-Next: ' --format='%h %s%n%(trailers)'`.
  If its `Dev43` trailer differs from `version` in
  `${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json`, tell the human;
  on their approval, record the new version in your next commit. If
  `spec/STATE.md` exists, see Migration first.
- The trailers, in this order, in the message's last paragraph with any
  other trailers:
  - `Dev43:` the plugin version.
  - `Dev43-Specification:` `complete` or `partial` (see
    Specification).
  - `Dev43-Increment:` the slug.
  - `Dev43-Scope:` the scope, in one sentence.
  - `Dev43-Shape:` the shape.
  - `Dev43-Phases:` the phases of the plan, in order, e.g.
    `Specification, Tests, Implementation`.
  - `Dev43-Gates:` the gates of the plan besides the final review, e.g.
    `Specification Exploration`, or `none`.
  - `Dev43-Next:` the phase that starts after this commit, or `Pause`.
  In Pause, only `Dev43`, `Dev43-Specification` and `Dev43-Next`.
  Copy unchanged values from the previous state.
- The step within a phase is not recorded: it lives in the
  conversation. The human never clears your context while work is
  uncommitted. If a session starts with uncommitted changes
  (`git status`), tell the human and ask which step you are at; never
  guess.
- Start every message with `[<Phase> · <Step>]`, the phase and step
  you are in once the message's changes are made.

## Plan and gates

- Between increments, Phase is Pause and no step applies; your
  messages start with `[Pause]`. Pause is a free discussion: change
  nothing but `spec/BACKLOG.md`. Any other change, even one line of
  configuration, is an increment.
- When the human starts an increment, or the plan no longer fits, use
  the `dev43:planning` skill: it proposes the plan (scope, shape,
  phases, gates).
- A gate is a point where you stop and wait for the human's `next`:
  the Exploration or the Verification of a phase, as the plan lists
  them. The last phase's Verification is always a gate: the final
  review.
- Where the plan has no gate, go on without stopping. An ungated
  Exploration: read what its skill says, settle its points yourself,
  then start Production. An ungated Verification: run the checks, then
  make the exit commit and start the next phase.
- An ungated step still stops when it needs the human: a point you
  cannot settle with confidence, a tag, a major decision. Stop, treat
  it as a gate, and say in a line that the plan missed it. A tag always
  stops you before a commit.
- The human may add or remove gates at any time; record the change in
  the next commit.
- The human passes a gate with one word: `next`. Anything else ("ok",
  "yes", "proceed", "nice") is discussion: answer it and do not move.
  At a gate, end your message with what `next` will do, e.g. "`next`:
  end Exploration, start Production." or "`next`: make the exit commit,
  then run Implementation up to the final review."
- After an exit commit, load the next phase's skill and start it in the
  same message.
- Production ends when you hand over, or, where Verification has no
  gate, when you commit. First run the checks of the phase (see its
  skill) and fix what fails: the human reviews only work that passes
  them. At a gated Verification, hand over with the check results and
  your tags (file and line), with one line on each saying why.
- Verification: the human reviews. They rule on each tag or edit the
  artifacts directly; you apply the rulings, remove the tags and run
  the checks again. The step is complete when the checks pass, no tag
  remains (see Tags), and the human approves.
- Final review: the human also reviews the increment's commits that no
  gate reviewed, in order. Name them in your hand-over, with the
  command to read them: `git log -p --reverse <first>^..HEAD`. When the
  plan has no Integration phase, the hand-over also holds the
  retrospective (see the Integration skill), each point in a line or
  two, or says there is none. Before the exit commit, apply what the
  human approved of it, remove from `spec/BACKLOG.md` the entry the
  increment did, if any, and run the checks of Integration that apply.
- If you meet a major decision that calls into question what was agreed,
  stop working, explain it, and propose a return. Never work around it.
- Direct phase: no specification, no retrospective. Make the change,
  run the checks of the test and quality policy, and hand over as
  usual. On `next`, commit as `[<increment>] <Kind>`, where `<Kind>`
  names the work in one word, e.g. Tooling, Config, Dependencies, Fix;
  Next is `Pause`.
- Abandon: only the human decides to abandon an increment, from any
  phase. Then:
  1. List what to keep from the increment (e.g. backlog edits) and
     wait for the human's answer.
  2. Discard the uncommitted work. If the increment has commits, undo
     them in one go: `git revert --no-commit <first>^..HEAD`, where
     `<first>` is its first commit. Re-apply what is kept.
  3. Rewrite the backlog entry the increment came from as the need it
     served, or remove it if the need is gone. Record no rejected idea.
  4. Commit everything as `[<increment>] Abandon`, the body saying why;
     Next is `Pause`.

## Returns

A return goes back to an earlier phase when a later step shows it was
wrong, e.g. a disputed test, or a rejection at the final review. Only
the human decides one.

1. If the current phase has uncommitted work, commit it as
   `[<increment>] <Phase> (wip)`, with Next the phase you return to.
   Its tags stay in it.
2. Redo the phase from its Exploration, which is a gate. Each phase
   done again ends its subject with ` (return)`, including the one you
   left when it resumes on top of its wip commit. The phases after it
   are done again only where the return changed what they build on.
3. When a phase resumes on its wip commit, raise again its tags that
   still apply, and remove the others once the human agrees.

History is never rewritten: no amend, squash or rebase of a commit.

## Migration

`spec/STATE.md` exists in projects set up before Dev43 3. Propose to
migrate; on `next`, delete it and commit as `[migrate] Dev43 3`, with
the trailers taken from its fields; Next is its Phase. If its Phase is
not Pause, the gates are every Exploration and Verification left in the
increment, as before Dev43 3, and the increment keeps its change page.
If its Stash is set, apply the stash first, and commit it as a wip of
Implementation (see Returns).

## Tags

A tag draws the human's attention to a choice you are unsure of, and
records that they must act on it.

- Tag `@dev43:unsure` each choice that neither the specification nor
  the human dictated and that you doubt, on the line where it applies
  (spec, test or code). A test you believe is wrong is always tagged.
- Do not tag choices you are confident of: the human sees them in the
  review. One the human would care about belongs in the specification
  (silver rule), which they read in full.
- Tag a choice once, at its most authoritative place: spec before test
  before code. A ruling on that tag rules on the choice everywhere.
- Write the choice itself as normal content: the artifact must read
  correctly once the tag is removed. Put nothing else in the tag, no
  kind, ID or explanation; explanations go in your hand-over message.
- In Markdown, put the tag in an HTML comment: `<!-- @dev43:unsure -->`.
  In code, put it in a comment on its own line, just above the
  statement, so that removing it leaves the formatting unchanged.
- The human accepts a tag by removing it, and rejects it by changing
  the content (or asking you to). Never remove a tag yourself unless
  the human has ruled on it.
- No tag remains when both commands print nothing:
  `git diff <base> | grep '^+.*@dev43:'`, where `<base>` is the last
  commit before the increment, and
  `git ls-files -o --exclude-standard -z | xargs -0 -r grep -Hn '@dev43:'`.
  Only a wip commit holds real tags, so tags quoted in other committed
  documents do not count. To quote a tag in a new document, write
  `@dev43\:`.

## Specification

- Write the minimum, by the silver rule. Everything else is derived by
  agents, in tests and code. Tag what you are unsure of instead of
  specifying it.
- Specification, tests and implementation are linked by refinement: an
  implementation may behave beyond what is specified. State each
  behavior rule as an outcome observable over the specified domain; an
  absence only when a test can observe it. Behavior outside that
  domain is left unspecified. Technical rules constrain the
  implementation directly and are checked in review, not by tests.
- The `Dev43-Specification` trailer says whether `spec/main/` covers
  the whole software (`complete`) or only some zones (`partial`, for
  Dev43 adopted on existing code); absent means `complete`. In
  partial mode:
  - a zone is specified once its feature-area page exists;
    `data-model.md` holds only the entities that specified zones use;
  - everything else is unspecified, as is: an increment may change
    existing behavior only where `spec/main/` specifies it. To change
    other existing behavior, first specify its zone in a
    `specify-existing` increment. New behavior is specified by the
    change, as usual;
  - only the human sets it to `complete`.
- The change of an increment is its change page, when it has one;
  otherwise its diff of `spec/`: `git diff <base> -- spec/`, where
  `<base>` is the last commit before the increment.
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
- A point discovered after the Specification phase:
  - the human would not care (silver rule): code only;
  - it belongs in the specification but needs no new test (e.g. a
    technical decision): write it in the change, tagged; it is
    reviewed and committed with the current phase;
  - new behavior that one or two new tests can check: an Amendment
    (see the Implementation skill);
  - anything larger, or a change to what was agreed: propose a return.
  Never leave it only in your memory or a commit message.
- Layout:
  - `spec/main/`: the main specification. `data-model.md`,
    `technical.md` (stack, conventions, test and quality policy), and
    one page per feature area, named with the human.
  - `spec/changes/<slug>.md`: the change page of the current
    increment, when it has one.
  - `spec/BACKLOG.md`: candidate increments, one short line each, that
    the human can read in seconds, e.g. "Backend: Litestar SQLAlchemy
    repositories would shrink the hand-written queries." Add an entry
    only with the human's approval. An idea of yours they do not take
    up right away: propose it as an entry, never leave it in your
    memory or a commit message.

## Tests and code

- Tests cite what they check: a name from the specification (in the
  test name or its grouping) or a rule ID, written as the specification
  writes it; case and separators may follow the language's conventions
  (`test_r5`, `TestR5`). Search citations ignoring both.
- Code cites a rule ID only where it explains something the reader
  would not otherwise see.
- Never copy specification text into tests or code.
- During Implementation, never change test code written in a Tests
  phase. If such a test seems wrong,
  tag it `unsure`, explain why in your hand-over, and continue. Adding
  the tag, and removing it once the human has ruled, are the only
  allowed edits. In a `code-only` increment, you
  may also make edits that leave what a test checks unchanged (e.g. a
  moved import), each tagged.
- Add no dependency, service or interface unless the specification
  names it or you tag it. Tag only a real choice: a new capability,
  framework or service, or a library a competent agent might not pick.
  Routine utility libraries of the stack (e.g. serialization, hashing,
  UUIDs) need no tag; list them in one line in your hand-over.

## Working with the human

- Exploration is a discussion, not a report. One point per message, a
  few sentences at most, then wait for the answer. Ask one question or
  make one proposal; let the answer decide what comes next.
- Raise only what you cannot settle with confidence: the human's goals
  and preferences, real trade-offs, choices you doubt. If you would
  recommend something with confidence, don't ask; make the choice in
  Production.
- No numbered lists of decisions, no option surveys up front. Bring
  alternatives only when the human asks or a trade-off needs them.
- A skill's list of Exploration topics is your agenda, not a message
  template.
- A point you made that the human did not react to counts as accepted.
- When you have nothing left to raise, propose to end Exploration. At a
  gated Exploration where you have nothing to raise, say so: `next`
  starts Production.
- Production: work without interrupting; tag instead.

## Git

- The project is a git repository. Use it: `git diff` and untracked
  files are what remains to review, `git diff --cached` what the human
  has already reviewed, `git diff HEAD` the work of the current phase,
  `git log` the history.
- The index belongs to the human, who stages each file or hunk once
  read. Never stage, except at a commit.
- A phase ends in one exit commit: on `next` at its Verification gate,
  or once its checks pass where it has none. `git add -A`, then commit
  as `[<increment>] <Phase>`, with a short body giving the reasons for
  the phase's main decisions, and the state trailers (see State), Next
  the next phase of the plan or `Pause`.
- The only other commits are a Direct phase's (see Plan and gates), a
  wip commit (see Returns), an Amendment during Implementation (see its
  skill), an Abandon, a migration and, in Pause, a commit of
  `spec/BACKLOG.md` the human asks for, with a plain subject. All carry
  the state trailers. Never commit at any other time.
- Commit bodies are the project's decision record: what was decided
  and why. Before reopening a decision, look for an earlier one with
  `git log --grep=<keyword>`.
