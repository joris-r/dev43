# Dev-4-3 plugin feedback — test run 002

A run through one complete cycle on an empty project: `init` → Initial
Framing (`framing`) → first increment `add-list` (Specification → Tests →
Implementation, with one return loop) → start of Integration. Product: a
Python CLI todo list (argparse, JSON file, uv/pytest/ruff/mypy).

Commits produced:

```
c9383c3 dev43: add-list — Implementation
0b6c6df dev43: add-list — Tests            (return loop)
d0f9cb4 dev43: add-list — Specification    (return loop)
a87d2ca dev43: add-list — Tests
d6c1e73 dev43: add-list — Specification
6e64b52 dev43: framing — Initial Framing
5938969 dev43: init
```

## What worked well

- Recording decisions as they were made (the commit body carries the
  reasons) kept the spec pages short and free of justification.
- The Tests check "fail for the right reason" caught real issues: two
  tests passed before any implementation because argparse already rejects
  an unknown subcommand with exit 2. One was strengthened.
- The return loop worked as designed: the increment kept its name, code
  and tests stayed, and the spec stayed the single source of truth.
- Tags kept the review focused: the human ruled on 15 tags in total,
  mostly by deleting them in the editor.

## Friction and proposals

### 0. Exploration is not a discussion (CLAUDE.md, every skill's Exploration)

Remark from the human. A natural discussion is an exchange of short
messages that answer each other. Instead, the agent thought through the
whole topic, then posted a wall of text with numbered points, options
and a recommendation for each, and the human answered by numbers. That
defeats the idea of Exploration: the human reacts to a finished survey
instead of thinking with the agent, and decisions are taken in bulk.

Proposal:

- In Exploration, one point per message, a few sentences at most, then
  wait for the answer. Ask a question or make one proposal; let the
  answer decide what comes next.
- No numbered lists of decisions, no option surveys up front. Bring
  alternatives only when the human asks or when a trade-off really
  needs them.
- The skills' topic lists (e.g. Initial Framing's five topics) are an
  agenda for the agent, not a message template.
- Write this in CLAUDE.md, "Working with the human", and repeat it in
  each skill's Exploration section.

Second remark from the human, on what Exploration is for. A "sure"
recommendation means the agent could do the work without the human.
The split between Exploration (chat) and Production (tags) exists to
reduce chat: Exploration should stay coarse, and the detailed choices
should reach the human as tags in Production, where reviewing them is
cheap. In this run most Exploration questions were the agent's own
"sure" recommendations, asked one by one (e.g. ruff, mypy, layout,
JSON style, atomic write): they should have been tags.

Proposal:

- In Exploration, raise only what the agent cannot settle with
  confidence: the human's goals and preferences, real trade-offs, and
  choices the agent would tag `unsure`.
- Everything the agent would tag `sure` goes straight to Production,
  tagged; it is not asked in Exploration.
- Rule of thumb for the agent: "If you would recommend it with
  confidence, don't ask; tag it."

The test case may have been too simple to show this well: with a small
CLI almost every choice is a confident one, so a coarse Exploration
would have been a few messages long.

### 1. Gate round trips (CLAUDE.md or all skills)

Every phase needs about four human messages: end Exploration, end
Production, approve review, go for exit. In practice the human answered
"agree", "proceed", "reviewed", "ok", and the agent had to guess which
gate(s) that closed, for example whether "agree" on the last Exploration
topic also meant "Exploration is over".

Proposal: state explicitly that when the human approves a step's work
with no change request, the agent may take it as approval to pass the
remaining gates of the phase up to its exit, and must say so in its
reply. Alternatively, give the human a fixed vocabulary (`next`, `go`)
and have the agent always end with the exact word expected.

### 2. One choice tagged in several artifacts (CLAUDE.md, Tags)

The same choice (e.g. the `-f` short option, the ruff rule sets) was
tagged both in `technical.md` and in code. The human removed only the
spec tag; the agent had to decide whether that ruled on the code tag too.

Proposal: "Removing one tag of a choice rules on every tag of that same
choice." Or: "Tag a choice once, at its most authoritative place (spec
before test before code)."

### 3. Removing tags breaks formatting (CLAUDE.md or Verification)

Removing a trailing `# @dev43\:...` comment let `ruff format` join wrapped
lines, so the formatting check failed after the rulings.

Proposal: in every Verification, "after applying rulings, run the
project's formatter, then the checks". Or advise putting code tags on
their own line above the statement, which formatters leave alone.

### 4. Return loop too heavy for a one-line amendment (implementation skill)

During Implementation Exploration the human wanted one extra rule ("a
command is required"). Doing it by the book took Specification
(Exploration, Production, Verification, commit) → Tests (same, commit) →
Implementation: about six gates and two extra commits for one spec line
and one five-line test.

Proposal: a "small amendment" path inside Implementation Exploration: the
agent proposes the spec line and the test together; the human approves
both in one gate; one commit `dev43: <increment> — Amendment`. The test
must still fail for the right reason before code is written.

### 5. Implementation Exploration after a return (implementation skill)

Exit of Tests says "set Phase to Implementation and Step to
Exploration". After a return loop, Implementation Exploration had
already been completed; the agent went straight to Production. The skill
should say whether Exploration must be redone after a return, or may be
skipped when nothing in it is affected.

### 6. Repeated commit subjects (all skills)

The return loop produced a second `dev43: add-list — Specification` and
`— Tests`. `git log` becomes ambiguous. Proposal: suffix returns, e.g.
`dev43: add-list — Specification (amendment)`.

### 7. Ambiguous agreed-vs-tagged choices

The rule "tag every choice the human did not make" is unclear when the
agent proposed a list in Exploration and the human answered only on some
items then said "exploration over" (Implementation, points 1–7). The
agent tagged the items the human did not explicitly address. A rule
would help: "Items of an Exploration proposal the human did not object
to count as decided" or the opposite.

### 8. Let the human use the index to track the review (CLAUDE.md, Git)

Remark from the human. Today the agent stages everything at the end of
Production (`git add -A`), so the index means "what the agent produced".
The human would rather use the index for their own review: stage each
file or hunk once read, so `git diff --cached` shows what is reviewed and
`git diff` what remains to read.

Proposal:

- At the end of Production, the agent does not stage. It runs
  `git add -N` (intent-to-add) on new files, so they show in `git diff`
  and the human can stage them hunk by hunk.
- The step is reviewed when `git diff` is empty (everything staged).
- The tag checks still work: they use `git diff HEAD` and untracked files.
- The agent's output and the human's edits are no longer told apart.
  That is intended: the goal of the review is agreement on the content,
  not a record of who wrote what.
- Update the Git section of CLAUDE.md accordingly (it currently defines
  `git diff --cached` as the agent's output and `git diff` as review
  changes) and the "Stage all changes" line of every skill's Production.

### 9. Minor

- `init`: STATE template has no hint for the framing increment's scope;
  the agent wrote "Set the stack, conventions and a running skeleton. No
  feature is delivered." Consider filling it from the template.
- `init`: `git init` approval was asked with a question prompt; fine, but
  the skill could say the permission prompt itself is enough.
- Tests skill, step 4: a rule partly testable (R1: error paths testable,
  interrupted write not) does not fit "(not testable)" well. The run wrote
  "An interrupted write is not covered by tests (not testable)." Allow
  partial marking explicitly.
- Every message starts with `[Phase · Step]`; on a message that crosses a
  gate the prefix is ambiguous (old or new state). Suggest: the state at
  the end of the message.
- Integration: the retrospective proposals mix project rules (CLAUDE.md)
  and plugin changes; the skill could ask the agent to label each
  proposal with its target.
