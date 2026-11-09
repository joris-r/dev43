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
  what changes: plain lines are added, a line starting with `×` is
  removed (code blocks included), a line ending with `…` is existing
  context that locates a change.
- The future specification is written along parts that can move
  separately.
- A path in `docs_future/<feature>/` points to the feature's section if
  it has one, else to `docs/`.
- A commit that changes a section with a future version in
  `docs_future/` updates that version too.
- `docs_future/<feature>/` settles every decision where the human
  matters; later refinement settles only what an agent can decide.
- Before any increment builds it, fresh agents stress it with
  Specification passes until one finds nothing important.
- An increment that meets a decision needing the human stops and
  escalates.
- Planning picks the part the next increment builds, closed under its
  dependencies, cited or not. Specification
  moves it into `docs/` unchanged in a first commit, then refines it
  in place in a second.
- The retrospective writes what the increment taught about the rest of
  the feature to `docs_future/<feature>/BACKLOG.md`. The next
  Specification takes it into account; a major change gets an
  increment of its own that updates `docs_future/<feature>/`.
- `docs_future/<feature>/` shrinks to what remains, deleted when empty.
- Planning lists the open features. Abandoning one is an increment that
  deletes its folder.

## Supervised increments

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
    each transition as a sub-point;
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
- A scenario is one end-to-end test, cited by its section path; its
  steps carry no tags.
- `design/` and `design.md` have no tags; they are checked by eye at
  review.

## Skill changes

- Skills state goals and limits, and leave the choices to the agent.

### Specification checks

Script:
- [paths] Every path a document cites resolves; `docs/` cites nothing
  in `docs_future/`.
- [names] A concept or operation has the same section name in every
  document.
- [overlap] A commit changing a section of `docs/` that has a future
  version changes that version too.

Agent:
- [invariants] Invariants are only in the model; each operation states
  the conditions that keep them.
- [meaning] Every concept and field states its meaning, unless its name
  makes it obvious.
- [duplicate] Nothing is stated twice or derivable from another line.
- [examples] Every example illustrates a rule ambiguous without it.
- [dependents] An added or changed operation keeps the invariants of
  every domain that depends on its domain.
- [extension] An extension of another domain's operation keeps or
  weakens its precondition, and keeps or strengthens its effects.
- [tags] Every statement of behavior has a tag.
- [silver] Every line passes the silver rule; the agent deletes the
  lines it is sure fail it.
- [why] No line gives a reason; reasons go to the commit body.

### Tests checks

Script:
- [coverage] Every tag and every scenario has a test, or is marked not
  testable; every test path resolves.

Agent, fresh context:
- [faithful] Each new or changed test checks what its rule says.

Human:
- [cases] A summary, one line per test case of each added or changed
  tag, covers what the human meant.

### Retrospective

- Moves into `core`, at the final review, for every increment, direct
  ones included; the integration skill is deleted.
- New topic: what the increment taught about the rest of the feature,
  written to `docs_future/<feature>/BACKLOG.md`.
- Its result goes in the increment's last commit, never in the spec.
