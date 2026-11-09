# v4 decisions

## Purpose

1. A better specification structure.
2. A large specification change written ahead, then carried out over
   several increments.
3. Increments carried out by an agent supervised by an agent, once the
   human has approved the future specification.

## Phases

- Planning, Specification, Tests, Implementation; each runs the three
  steps. Integration is removed.
- Planning has no commit of its own; the plan goes in the trailers of
  the increment's first commit.
- Every increment ends with a retrospective.

## Future specification

- A large change is written ahead in `docs_future/<feature>/`, by
  increments of its own.
- `docs_future/<feature>/` mirrors the layout of `docs/` and holds only
  what changes:
  - a plain line is added, right after the line above it;
  - a line starting with `×` is removed (code blocks included);
  - a line ending with `…` stands for the existing line that starts
    with the same text, as context;
  - a heading that exists in `docs/` is context; a new section goes
    after the section above it, or at the end of the file.
- `docs_future/<feature>/BACKLOG.md` is the only file outside the
  mirror. It holds the feature's description, its outline and its
  lessons.
- `docs_future/<feature>/BACKLOG.md` outlines the increments that
  build the feature, in order, each with the sections it integrates
  and closed under its dependencies, cited or not. It is part of the
  feature's design, reviewed by the human.
- A path in `docs_future/<feature>/` resolves against `docs/` with the
  feature applied.
- Every future version stays applicable to `docs/`: a commit that
  changes `docs/` updates the future versions it breaks.
- Supervised work starts only once `docs_future/<feature>/` settles
  every decision where the human matters.
- Work that raises a decision needing the human pauses the supervised
  work.
- Planning takes the next increment of the outline. Specification
  only integrates its sections into `docs/`, in one commit.
- The retrospective writes what the increment taught about the rest of
  the feature to `docs_future/<feature>/BACKLOG.md`. The next Planning
  takes it into account; an important lesson pauses the supervised
  work, and an increment of its own updates `docs_future/<feature>/`.
- `docs_future/<feature>/` shrinks to what remains. The last increment
  of the outline deletes it, moving any open lesson to the project
  backlog.
- Planning lists the open features. Abandoning one is an increment that
  deletes its folder.
- The project backlog is `docs_future/BACKLOG.md`.

## Supervised increments

- Dev43 draws the line of responsibility between human and agent: the
  human reviews only the specification, and tries the software.
- Tests and code are checked by agents only, each check in a fresh
  context.
- The line of responsibility holds in every increment; without
  supervision, the human acts as the orchestrator.
- A gate on Tests or Implementation waits for an agent check; the
  human sees only the tags touching a decision they approved.
- The final review of an unsupervised increment covers the
  specification change, a try of the software and the retrospective.
- An increment changes no decision the human approved; such a change
  escalates and goes into `docs_future/<feature>/`, reviewed by the
  human.
- The orchestrator waits only for escalations, never for a review of
  tests or code.
- At the end of a feature, the human tries the software, guided by
  its scenarios.
- An orchestrator runs one sub-agent at a time, one per increment.
- The orchestrator plans each increment from the future
  specification, answers what an agent can decide, relays to the
  human only the decisions where the human matters, and reviews at
  the gates.
- It reads its state from the commits and
  `docs_future/<feature>/BACKLOG.md`, so it can restart at any point.

## Layout

- Documents, each only when needed: README, overview, technical,
  design, design/, model, operations, ui, scenarios. Top level spans
  domains; a domain folder holds what is specific to it.
- A domain's `README.md` declares the domains it depends on:
  `Depends on: /tasks, /users.`
- An operation extending another domain's operation starts with
  `Extends <path>.`
- `operations.md`: the actions on `model.md` data, queries included.
  `ui.md` refers to them, adding only trigger and display.
- An operation: purpose only if the name and cases leave it unclear,
  API binding if any, then one tagged case per condition, errors
  included, each with all its outcomes. A refused case states its
  message.
- One `##` section per concept or operation, same name across
  documents.
- `ui.md`: one `##` section per element the user meets (page,
  component, command), its binding first, then:
  - what it shows, in order; one tagged case per state or outcome,
    each transition as a tagged sub-point;
  - what the user can do: each trigger, the operation it runs, and
    when it is unavailable.
- An exact text the user sees is written with placeholders:
  `No task <number>.`
- `design/`: mockups, one per page, named after its `ui.md` section,
  showing every state, values included. `design.md` holds the look
  rules they cannot show.
- The form for each kind of UI (web, CLI) is an example in a separate
  file, loaded by the skill on demand.

## Traceability

- Tag: a short name in brackets starting a line, unique in its
  section, on every statement of behavior (something the software
  could be seen to break): `- [empty] Add an empty text: refused.`
- Path: `/<file>/<section>/<tag>` or `/<file>/<section>`, prefixed by
  `/<domain>` if any. Segments: lowercase, spaces to hyphens,
  punctuation dropped.
- Bindings (route, command, HTTP) carry no tag.
- Tests cite paths in a comment; documents cite them as plain text.
- A statement no test can check ends with `(not testable)`.
- A scenario is one end-to-end test, cited by its section path; its
  steps carry no tags.
- `design/` and `design.md` have no tags; they are checked by eye at
  review.

## Migration from v3

- The migration changes the form of the specification, never a
  decision, except the deletions the human approves.
- The agent applies the deletions of [duplicate] and [why], and
  proposes those of [silver] and [examples] to the human.
- A statement v4 requires and v3 left open states the current
  behavior of the code, tagged `@dev43:unsure` for the human.
- An agent checks, in a fresh context, that every v3 statement maps
  to a v4 line and that v4 adds only the tagged lines. The mapping
  goes in the commit body.
- The human reviews the whole new specification.
- The migration starts in Pause, and is one increment whatever the
  size: Specification, Tests, and Implementation only if a new test
  fails.
- Tests phase: existing tests change only their citations, to paths;
  each tag without a test gets one. An agent checks, in a fresh
  context, that each new citation matches what its test checks.
- A `migrate` skill, loaded by `core` when the major version of the
  `Dev43` trailer is below the plugin's. It migrates from v3 only;
  the v2 migration is removed from `core`.
- `spec/BACKLOG.md` moves to `docs_future/BACKLOG.md`. Files the
  process does not own stay as they are.
- The skill lists the CLAUDE.md project rules naming a removed phase
  or step; the human rewords them at the Specification review.

## Skill changes

- Skills state goals and limits, and leave the choices to the agent.

### Specification checks

Script:
- [paths] Every path a document cites resolves; `docs/` cites nothing
  in `docs_future/`.
- [names] A concept or operation has the same section name in every
  document.
- [overlap] Every future version applies to `docs/`: each `×` and `…`
  line matches an existing line.
- [depends] A domain cites only itself, top level and the domains it
  declares; dependencies have no cycle; each `Extends` path is an
  operation of a declared domain. The script lists, for each changed
  operation, its dependent domains and its extensions.

Agent:
- [invariants] Invariants are only in the model; each operation states
  the conditions that keep them.
- [meaning] Every concept and field states its meaning, unless its name
  makes it obvious.
- [duplicate] Nothing is stated twice or derivable from another line.
- [examples] Every example illustrates a rule ambiguous without it.
- [dependents] An added or changed operation keeps the invariants of
  every domain that depends on its domain.
- [complete] The cases of an operation do not overlap and cover every
  input.
- [extension] An extension of another domain's operation keeps or
  weakens its precondition, and keeps or strengthens its effects.
- [tags] Every statement of behavior has a tag.
- [silver] Every line passes the silver rule; the agent deletes the
  lines it is sure fail it.
- [why] No line gives a reason; reasons go to the commit body.

### Tests checks

Script:
- [coverage] Every tag and every scenario has a test, or is marked
  `(not testable)`; every test path resolves.

Agent, fresh context:
- [faithful] Each new or changed test checks what its rule says.
- [cases] The test cases of each added or changed tag cover what it
  says.

### Retrospective

- Moves into `core`, at the final review; the integration skill is
  deleted.
- New topic: what the increment taught about the rest of the feature,
  written to `docs_future/<feature>/BACKLOG.md`.
- Its result goes in the increment's last commit, never in the spec.
