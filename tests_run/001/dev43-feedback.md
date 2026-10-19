# Dev-4-3 plugin: corrections to make

Findings from testing the plugin on this project (a CLI to-do list,
Initial Framing phase). Paths are relative to the plugin repository.

## 1. Initial Framing must not write level-1 specification

**Observed.** `skills/initial-framing/SKILL.md` asks for
`spec/main/1-functional/vision.md` with an ID per decision. The agent
gave IDs to the purpose, the users, the main use cases (`add`, `list`,
`done`, `rm`) and the data file location. These are features: the first
Specification phase will specify `add` and `list` again under new IDs,
creating duplicates to remove right after framing.

**Fix.**
- The vision (purpose, users, constraints, out of scope) goes in
  `README.md`, with no IDs. It is context, not verifiable requirements.
- Initial Framing writes no file in `1-functional/` or `2-interfaces/`.
  Its specification output is `3-technical/` only (stack, conventions).
- Level-3 decisions written during framing cannot cite level-1 IDs; they
  quote the constraint in their "because" in plain text.
- Add `README.md` to the deliverables of the skill (it was missing).

## 2. State that Initial Framing is a bootstrap phase

**Observed.** Framing writes specification, code and a test in one
phase: it looks like a whole Specification / Tests / Implementation /
Integration cycle, which contradicts the process. Part of it is
unavoidable: the Tests phase needs test tooling, and Implementation needs
a chosen stack, so the skeleton cannot go through the normal cycle.

**Fix.** Write the exception as a rule in `process_principles.md` and in
the skill, e.g.: "Initial Framing is the only phase that writes to
`spec/main/` directly and the only one where code is not test-first,
because it builds the tooling the cycle depends on. It delivers no
feature." Bound it: the skeleton implements only T- decisions, and its
trivial test checks the tooling, not a behavior.

Check whether Retro-Specification needs the same explicit statement
(the other entry phase, exception the other way round: the code exists,
the specification is written afterwards).

## 3. Say what deserves an ID

**Observed.** Nothing in `templates/CLAUDE.md` or the skills says what
gets an ID, so the agent gave one to everything, including the
out-of-scope list (a non-requirement). An ID is only useful when
something cites it: a test, code, a tag, or a change specification that
modifies it. After framing, 12 of the 21 level-3 IDs were cited nowhere
and never will be ("Linux only", "pytest", "ruff", "no coverage
threshold"…). Several of the citations that do exist are decorative,
e.g. `# T-MAIN-020` at the top of `.gitignore` or `# T-MAIN-002` next to
`requires-python`: they add nothing the reader does not already see.
Meanwhile IDs cost numbering, global uniqueness, no reuse, and noise.

IDs pay off at level 1 (behavior checked by tests) and level 2
(interface contracts), where the spec → test → code loop is real. Most
level-3 decisions are tooling choices with no consumer; a section
heading is enough for a later change specification to refer to them.

**Fix.**
- Add a rule to `templates/CLAUDE.md`, e.g.: "Give an ID only to a
  requirement a test can check or a decision an artifact must cite. No ID
  for context, rationale, tooling choices or out of scope."
- Level 3 is written in prose: sections without IDs, one decision per
  paragraph with its "because". An ID only for a checkable rule (e.g.
  "every test uses a temporary data file").
- Forbid decorative citations: cite an ID in code only where it explains
  something the reader would not otherwise see.

## 4. Do not ask for content that was not discussed

**Observed.** The skill asks for "UX principles" in `vision.md`, but the
Exploration topic list has no such topic. The agent had to invent two
principles (and tag them).

**Fix.** Either add the topic to Exploration or drop it from the
Production deliverables.

## 5. Repository hygiene is missing from Exploration

**Observed.** The human had to ask for a `.gitignore` themselves. A
`README.md` was not planned at all.

**Fix.** In the Exploration "Conventions" topic, list `README.md`,
`.gitignore` and lock-file policy explicitly.

## 6. `init` does not check for a git repository

**Observed.** `templates/CLAUDE.md` relies on `git grep` to check that
no tag remains, but `commands/init.md` neither checks for a repository
nor proposes `git init`. In this test the folder was not a repository
when `init` ran.

**Fix.** In `commands/init.md`, if the project is not a git repository,
propose `git init` to the human (without committing).

## 7. Verification subagent: model and cost not controlled

**Observed.** The skill says "spawn a subagent" without saying which. The
main agent used `general-purpose`, which inherits the session model
(Opus here): about 49,000 tokens for one pass over a dozen small files,
mostly start-up context. Applying a closed checklist does not need the
largest model.

**Fix.** Ship a dedicated agent in the plugin, e.g.
`agents/dev43-verifier.md`, with `model: sonnet` in its frontmatter,
restricted tools (Read, Edit, Bash), and the verification rules built in
(only add `verify` tags, no fix, no STATE change). Make the phase skills
spawn that agent by name.

## 8. The downward-link rule is ambiguous about same-level citations

**Observed.** `templates/CLAUDE.md` says "level 3 cites 1 or 2". The
verification subagent read it as forbidding level 3 from citing level 3,
and tagged `T-MAIN-012` for citing `T-MAIN-004`. The intent is to forbid
upward links only.

**Fix.** Reword, e.g.: "Links never point upward: a level may cite its
own level or lower levels (level 1 cites only level 1)."

## 9. An accepted `tech` tag loses its decision when removed

**Observed.** The agent tagged the build backend `uv_build` as `tech`; the
human accepted it and removed the tag. The decision then existed
nowhere: the next verification pass flagged `uv_build` as an untagged,
unspecified dependency.

**Fix.** In `templates/CLAUDE.md`: "When the human accepts a `tech` or
`spec` tag, write the decision into the specification (new ID or
existing one) before removing the tag." Say who does it: the agent,
applying the ruling.

## 10. Verification is noisy and does not converge

**Observed.** The framing only set up a standard stack, yet two
verification passes raised 14 tags. In the second pass, 4 of 6 tags
challenged decisions the human had made explicitly in Exploration
("cheap to change, could be dropped"): the subagent starts without the
conversation, so it cannot tell a human decision from an agent choice.
Since every pass re-reads everything, each pass finds new subjective
remarks, and "cycle until a round raises nothing new" may never end.

**Fix.**
- Only the first pass reviews all artifacts. Each later pass reviews
  only what changed since the previous pass (the edits that applied the
  rulings), plus the consistency of those changes with the rest. The
  skill gives the subagent that diff, e.g. saved by the main agent
  before applying the rulings (`git diff` to a file, or `git stash
  create` as a reference, since nothing is committed).
- Raise the bar for a tag: only problems that would mislead a later
  phase (contradiction, ambiguity, broken link, skeleton not matching
  the spec). Drop "cheap to change, could be dropped" from the
  checklist, or apply it only to decisions with no "because".
- Optionally mark human-made decisions in the spec (e.g. `(human)`) so
  the verifier does not re-open them.

## 11. Do not record the "because" of decisions

**Observed.** `templates/CLAUDE.md` says "Give a decision a 'because'
when its reason is not obvious, or when it is a trade-off someone might
later want to reverse", and the Specification verification checklist
flags "decisions missing a 'because'". The agent therefore attaches a
justification to many decisions, e.g. in the first increment's change
specification: "F-MAIN-002 — … Because it is simpler than a fixed
identifier; numbers shift when a task is removed, which is accepted."
This is analysis, not a decision. It adds noise to the specification,
and analysis quickly becomes irrelevant as the project moves on: the
specification ends up carrying outdated reasoning.

**Fix.**
- Remove the "because" rule from `templates/CLAUDE.md` and from the
  skills: a decision states what is decided, not why.
- Remove "decisions missing a 'because'" from the Specification
  verification checklist.
- Align items 1, 3 and 10 above, which assume a "because" (level-3
  decisions quoting constraints in their "because", "one decision per
  paragraph with its 'because'", "decisions with no 'because'").

## 12. Tags are too verbose and their status is unclear

**Observed.** The intent of a tag is only to mark agent-written content
where the human's attention is required. In practice the agent writes
the choice itself inside the tag, e.g. in the first increment's change
specification:
`<!-- @dev43\:decision[spec] F-MAIN-008 — an empty TODO_FILE is treated as unset. -->`
with nothing in the decision text saying so. The human cannot tell
whether the tag content is part of the decision (to be copied into the
specification when accepted) or only an explanation for the review.
Removing an accepted tag then deletes the decision (same root cause as
item 9).

**Fix.**
- The agent writes its choice in the artifact itself (specification
  text, test or code), like any other content.
- The tag only marks that content for review: kind, ID and at most a
  few words saying what to look at, e.g.
  `<!-- @dev43\:decision[spec] F-MAIN-008 empty TODO_FILE -->`.
  Any longer explanation goes in the agent's hand-over message, not in
  the artifact.
- Accepting a tag then means only removing it; rejecting it means
  changing the content it marks. This also solves item 9.

**Why it matters.** Because the tag holds the decision, the human has to
go through the agent to apply each ruling. The review turns into
answering the agent's recommendations ("agreed on all") instead of
reading the artifacts and forming an opinion of one's own. The intent is
the opposite: the human reviews everything that was produced anyway,
actively, and edits the artifacts directly if needed. The agent applies
the solution it thinks is right; the tag only draws attention to it.
The human can remove a tag by hand without asking the agent.

## 13. The tag check matches tag examples in documentation

**Observed.** The `git grep` check of `templates/CLAUDE.md`
also matches tags quoted as examples in other Markdown files (here this
feedback file), so a step can never be "complete". The examples above
are escaped (`@dev43\:decision`) to avoid it.

**Fix.** Exclude documentation of the process from the check, or match
only real tags (e.g. a tag must start a comment: `<!-- @dev43:` or
`# @dev43:` / `// @dev43:`).

## 14. A cheaper model does not make verification cheap

**Observed.** In the first increment (`add-list`), the verification
subagent ran on Sonnet, as item 7 suggests. Each pass still used about
40,000 tokens, even the second one, which reviewed only a diff of a few
lines. Most of the cost is the subagent's start-up context, not the
amount reviewed. The first pass also returned an empty report (the text
`placeholder`); its findings had to be recovered from the tags it left
in the files.

**Fix.** A dedicated agent with a minimal context (item 7) matters more
than the model. Make the skill check the returned list against
`git grep` instead of trusting the report.

## 15. Verification pushes test-level detail into the specification

**Observed.** In `add-list`, the first pass raised 5 tags and the second
pass 5 more, each on the edge cases of the rulings applied after the
previous pass: whether `todo add "milk\n"` is accepted, whether `1.0` or
`true` is a valid `version`, which error wins when both the text and
the file are invalid. Each answer creates new edge cases, so the cycle
does not converge (see item 10). The human stopped it after two passes.
The checklist items "vagueness" and "untestable decisions" drive this:
any decision can be made more precise.

**Fix.** Edge cases are the Tests phase's job, where a test settles
them. Remove "vagueness" and "untestable" from the Specification
checklist, or limit them to a decision a test writer could not start
from at all.

## 16. Overall: the specification is not readable

**Conclusion of the human, ending the experiment after the first
increment's Specification phase.** The first goal was a specification
that is easy to read. The result has far too much noise: too much
detail, no structure (a flat list of numbered decisions), "because"
analysis (item 11), verbose tags (item 12). Verification does not help:
it only adds more noise (items 10, 15).

## 17. Target shape of a specification: examples, few rules, IDs per feature

**Observed.** `dev43-spec-draft.md`, at the project root, rewrites the
`add-list` change specification by hand as a target. It covers the same
behavior in about the same length (74 lines against 71) but reads much
better: 6 IDs instead of 13, no "because", no tags, one page instead of
three files. The edge cases the verification passes had added to the
specification (`1.0` versus `1`, `"milk\n"`, error precedence,
`--file ''`, `~` expansion, `XDG_DATA_HOME`) are left out.

**Fix.**
- A specification is mostly examples (a terminal session, a request
  and its response, a sample file), plus a few rules for what the
  examples do not show. Use tables for enumerations, such as errors and
  exit codes.
- One ID per feature or contract, on a section heading, not one per
  sentence. Tests cite that ID.
- One page per increment rather than one file per level; the level is
  in the ID prefix (F, I, T).
- Edge cases are settled in the Tests phase by a test. They are raised
  to the human only when a test cannot choose.
- Derive the rules of `templates/CLAUDE.md` and the skills from a
  hand-written target like this one, not the other way round.
