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
would care, or if the specification would be open without it.

## Line of responsibility

- The human reviews the specification and tries the software. Agents
  check the tests and the code, each check in a fresh context (see
  Agent checks).
- An increment changes no decision the human approved. Such a change
  escalates: stop, explain it, and propose it as a change of the
  specification, reviewed by the human.
- This holds in every increment. Without supervision, the human acts as
  the orchestrator: approves the plan, answers you, reviews the
  specification. Under supervision, `dev43:supervise` takes that role
  for everything but the specification.

## State

The state of the process lives in git: every commit you make records
it in trailers.

- Before any work, read the state, from the last commit that records
  it: `git log -1 --grep='^Dev43-Next: ' --format='%h %s%n%(trailers)'`.
  Compare its `Dev43` trailer with `version` in
  `${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json`: a lower major
  version, load `dev43:migrate`; any other difference, tell the human
  and, on their approval, record the new version in your next commit.
- The trailers, in this order, in the message's last paragraph with any
  other trailers:
  - `Dev43:` the plugin version.
  - `Dev43-Specification:` `complete` or `partial` (see
    Specification).
  - `Dev43-Increment:` the slug.
  - `Dev43-Feature:` the feature whose outline the increment carries
    out, if any.
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
  nothing but `docs_future/BACKLOG.md`. Any other change, even one line
  of configuration, is an increment.
- When the human starts an increment, or the plan no longer fits, use
  the `dev43:planning` skill: it proposes the plan.
- A gate is a point where you stop and wait for a review: the
  Exploration or the Verification of a phase, as the plan lists them.
  The human reviews at the gates of Specification and passes them with
  `next`. A gate of Tests or Implementation waits for an agent check
  (see Agent checks), and you go on once it passes.
- The final review, after the last phase, is always a gate, the
  human's (see Final review).
- Where the plan has no gate, go on without stopping. An ungated
  Exploration: settle its points yourself, then start Production. An
  ungated Verification: run the checks, then make the exit commit and
  start the next phase. In the last phase, the final review comes
  before the exit commit.
- An ungated step still stops when it needs the human: a point where
  the human matters that you cannot settle with confidence, a mark on
  the specification, an escalation. Stop, treat it as a gate, and say
  in a line that the plan missed it.
- The human may add or remove gates at any time; record the change in
  the next commit.
- The human passes a gate with one word: `next`. Anything else ("ok",
  "yes", "proceed", "nice") is discussion: answer it and do not move.
  At a gate, end your message with what `next` will do, e.g. "`next`:
  end Exploration, start Production."
- After an exit commit, load the next phase's skill and start it in the
  same message.
- Production ends when you hand over, or, where Verification has no
  gate, when you commit. First run the checks of the phase (see its
  skill) and fix what fails: a review covers only work that passes
  them. At a gate the human reviews, hand over with the check results
  and your marks (file and line), with one line on each saying why.
- Verification by the human: they rule on each mark or edit the
  artifacts directly; you apply the rulings, remove the marks and run
  the checks again. The step is complete when the checks pass, no mark
  remains (see Marks), and the human approves.
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

## Final review

The last phase's work ends at the final review, where the human:

- reviews the specification change of the increment, unless a
  Specification Verification gate already covered it:
  `git diff <base> -- docs docs_future`, where `<base>` is the last
  commit before the increment;
- tries the software: hand over what changed for a user and how to
  try it, in a few lines;
- rules on the retrospective (see Retrospective).

Before the exit commit, apply what the human approved, remove from
`docs_future/BACKLOG.md` the entry the increment did, if any, and run
the checks of the last phase again.

## Retrospective

Prepare it before the final review, each point in a line or two, or
say there is none. Topics:

- The project: technical debt, architecture, what was learned, and
  what follows for the backlog.
- The feature, when the increment carries out an outline: what the
  increment taught about the rest of it. On approval, write it under
  `## Lessons` in `docs_future/<feature>/BACKLOG.md`. A lesson that
  changes a decision of the future specification escalates (see Line
  of responsibility).
- The process, only if something went wrong: rules, agent context,
  thresholds, skill instructions. Label each change with its target:
  the project (e.g. its `CLAUDE.md`) or the Dev43 plugin. Never edit
  the plugin; for an approved plugin change, give the human the text
  to send to Dev43 (https://github.com/joris-r/dev43/issues): the
  project, the increment, the Dev43 version, and the change in a
  sentence or two.
- Going further: up to three leads drawn from the increment's actual
  work, never generic, or none: a concept or pattern at play, or a
  quality or security point worth examining. The human picks one or
  none; nothing is committed.

Its result goes in the increment's last commit: project files and the
backlogs, never the specification.

## Agent checks

An agent check is a review by a sub-agent with a fresh context, so
that it does not share your blind spots.

- Give it the checks to run (see the phase's skill), the paths of the
  specification it checks against, and the diff to check. Leave out
  your reasoning, except on what it rules on: your marks and disputed
  tests.
- It reports each finding with its file and line. Fix each one, or
  dispute it: a disputed finding goes to the human.
- A re-check covers only the fixes and the findings it resolves. After
  three checks that still report findings, the human decides.
- It rules on your marks in tests and code, except a mark that touches
  a decision the human approved: that one goes to the human.
- A phase with a Verification gate, or with a mark, runs its agent
  checks before its exit commit. Any other phase runs them at the end
  of the increment, before the final review, on the phase's commits.
  Specification always runs its agent check before its exit commit:
  tests and code build on it.

## Returns

A return goes back to an earlier phase when a later step shows it was
wrong, e.g. a disputed test, or a rejection at the final review. The
human decides a return to Specification; an agent check may decide a
return to Tests.

1. If the current phase has uncommitted work, commit it as
   `[<increment>] <Phase> (wip)`, with Next the phase you return to.
   Its marks stay in it.
2. Redo the phase from its Exploration, which is a gate. Each phase
   done again ends its subject with ` (return)`, including the one you
   left when it resumes on top of its wip commit. The phases after it
   are done again only where the return changed what they build on.
3. When a phase resumes on its wip commit, raise again its marks that
   still apply, and remove the others once the reviewer agrees.

History is never rewritten: no amend, squash or rebase of a commit.

## Marks

A mark draws the reviewer's attention to a choice you are unsure of,
and records that they must act on it.

- Mark `@dev43:unsure` each choice that neither the specification nor
  the human dictated and that you doubt, on the line where it applies
  (specification, test or code). A test you believe is wrong is always
  marked.
- Mark only choices you doubt. One the human would care about belongs
  in the specification (silver rule), which they read in full.
- Mark a choice once, at its most authoritative place: specification
  before test before code. A ruling on that mark rules on the choice
  everywhere.
- Write the choice itself as normal content: the artifact must read
  correctly once the mark is removed. The mark holds nothing else;
  explanations go in your hand-over message.
- In Markdown, put the mark in an HTML comment: `<!-- @dev43:unsure -->`.
  In code, put it in a comment on its own line, just above the
  statement, so that removing it leaves the formatting unchanged.
- The reviewer accepts a mark by removing it, and rejects it by
  changing the content (or asking you to). Remove a mark only once the
  reviewer has ruled on it.
- No mark remains when both commands print nothing:
  `git diff <base> | grep '^+.*@dev43:'`, where `<base>` is the last
  commit before the increment, and
  `git ls-files -o --exclude-standard -z | xargs -0 -r grep -Hn '@dev43:'`.
  Only a wip commit holds real marks, so marks quoted in other committed
  documents do not count. To quote a mark in a new document, write
  `@dev43\:`.

## Specification

- `docs/` is the specification of the software as it exists.
  `docs_future/<feature>/` is a large change written ahead, with its
  outline in `docs_future/<feature>/BACKLOG.md`.
  `docs_future/BACKLOG.md` is the project backlog. The
  `dev43:specification` skill gives their forms.
- The specification is closed: the model declares all the data, the
  operations settle every input in every state, the UI gives every
  operation a trigger and every outcome a display. Tests and code are
  derived from it without a question to the human.
- Within that, write the minimum, by the silver rule: a value the
  human does not care about is left free, and said so. Everything
  else is derived by agents, in tests and code. Mark a choice you are
  unsure of.
- Specification, tests and implementation are linked by refinement: an
  implementation may behave beyond what is specified. State each
  statement of behavior as an outcome observable over the specified
  domain; an absence only when a test can observe it. Behavior outside
  that domain is left unspecified. Technical statements constrain the
  implementation directly and are checked in review, not by tests.
- Traceability:
  - A tag is a short name in brackets starting a line, unique in its
    section, on every statement of behavior (something the software
    could be seen to break): `- [empty] Add an empty text: refused.`
  - A path is `/<file>/<section>/<tag>` or `/<file>/<section>`,
    prefixed by `/<domain>` if any. Segments: lowercase, accents
    removed, spaces to hyphens, punctuation dropped:
    `/operations/add-task/empty`, `État à vérifier` gives
    `etat-a-verifier`.
  - Bindings (route, command, HTTP) carry no tag.
  - Tests cite paths in a comment; documents cite them as plain text.
  - A statement no test can check ends with `(not testable)`.
  - A scenario is one end-to-end test, cited by its section path; its
    steps carry no tags.
  - `design/` and `design.md` have no tags; they are checked by eye at
    review.
- A decision states what is decided, not why. Give reasons in your
  hand-over message and in the commit message of the phase.
- The `Dev43-Specification` trailer says whether `docs/` covers the
  whole software (`complete`) or only some zones (`partial`, for Dev43
  adopted on existing code); absent means `complete`. In partial mode:
  - a zone is specified once its documents exist; `model.md` holds
    only what the specified zones use;
  - everything else is unspecified, as is: an increment may change
    existing behavior only where `docs/` specifies it. To change other
    existing behavior, first specify its zone in a `specify-existing`
    increment. New behavior is specified by the change, as usual;
  - only the human sets it to `complete`.
- The change of an increment is its diff of the specification:
  `git diff <base> -- docs docs_future`.
- Every future version stays applicable to `docs/`: a commit that
  changes `docs/` updates the future versions it breaks.
- A point discovered after the Specification phase:
  - the human would not care (silver rule): tests and code only;
  - it belongs in the specification but needs no new test (e.g. a
    technical decision): write it in the change, marked; the human
    reviews it at the next gate of theirs;
  - new behavior that one or two new tests can check: an Amendment
    (see the Implementation skill);
  - anything larger, or a change to what was agreed: escalate, and
    propose a return.
  Never leave it only in your memory or a commit message.
- `docs_future/BACKLOG.md`: candidate increments, one short line each,
  that the human can read in seconds. Add an entry only with the
  human's approval. An idea of yours they do not take up right away:
  propose it as an entry, never leave it in your memory or a commit
  message.

## Tests and code

- Never copy specification text into tests or code.
- During Implementation, never change test code written in a Tests
  phase. If such a test seems wrong, mark it, explain why in your
  hand-over, and continue. Adding the mark, and removing it once the
  reviewer has ruled, are the only allowed edits. In a `code-only`
  increment, you may also make edits that leave what a test checks
  unchanged (e.g. a moved import), each marked.
- Add no dependency, service or interface unless the specification
  names it or you mark it. Mark only a real choice: a new capability,
  framework or service, or a library a competent agent might not pick.
  Routine utility libraries of the stack (e.g. serialization, hashing,
  UUIDs) need no mark; list them in one line in your hand-over.

## Working with the human

- Exploration is a discussion, not a report. One point per message, a
  few sentences at most, then wait for the answer. Ask one question or
  make one proposal; let the answer decide what comes next.
- Raise only what you cannot settle with confidence: the human's goals
  and preferences, real trade-offs, choices you doubt. If you would
  recommend something with confidence, make the choice in Production.
- Bring alternatives only when the human asks or a trade-off needs
  them; raise decisions one at a time.
- A skill's list of Exploration topics is your agenda, not a message
  template.
- A point you made that the human did not react to counts as accepted.
- When you have nothing left to raise, propose to end Exploration. At a
  gated Exploration where you have nothing to raise, say so: `next`
  starts Production.
- Production: work without interrupting; mark instead.

## Git

- The project is a git repository. Use it: `git diff` and untracked
  files are what remains to review, `git diff --cached` what the human
  has already reviewed, `git diff HEAD` the work of the current phase,
  `git log` the history.
- The index belongs to the human, who stages each file or hunk of the
  specification once read. Stage only at a commit.
- A phase ends in one exit commit: on `next` at a gate of the human,
  or once its checks pass elsewhere. `git add -A`, then commit as
  `[<increment>] <Phase>`, with a short body giving the reasons for
  the phase's main decisions, and the state trailers (see State), Next
  the next phase of the plan or `Pause`. Planning has no commit: its
  plan goes in the trailers of the first commit.
- The only other commits are a Direct phase's, a wip commit (see
  Returns), an Amendment during Implementation (see its skill), an
  Abandon, a migration and, in Pause, a commit of
  `docs_future/BACKLOG.md` the human asks for, with a plain subject.
  All carry the state trailers.
- Commit bodies are the project's decision record: what was decided
  and why. Before reopening a decision, look for an earlier one with
  `git log --grep=<keyword>`.
