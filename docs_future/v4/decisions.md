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
  the sections the feature adds or changes, each in its full future
  version. Its README lists what the feature removes.
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
- Planning picks the part the next increment builds: whole sections,
  closed under their dependencies. Specification
  moves it into `docs/` unchanged in a first commit, then refines it
  in place in a second.
- The retrospective writes what the increment taught about the rest of
  the feature to `docs_future/<feature>/BACKLOG.md`. The next
  Specification takes it into account; a major change gets an
  increment of its own that updates `docs_future/<feature>/`.
- `docs_future/<feature>/` shrinks to what remains, deleted when empty.
- Planning lists the open features. Abandoning one is an increment that
  deletes its folder.

## Layout

- Documents, each only when needed: README, overview, technical,
  design, model, operations, ui, scenarios. Top level spans domains;
  a domain folder holds what is specific to it.
- `operations.md`: the actions on `model.md` data, queries included.
  `ui.md` refers to them, adding only trigger and display.
- One `##` section per concept or operation, same name across
  documents.
- Web `ui.md`: one `##` section per page or component; `design.md`
  uses the same names.

## Traceability

- Tag: a short name in brackets starting a line, unique in its
  section, on every statement of behavior (something the software
  could be seen to break): `- [empty] Add an empty text: refused.`
- Path: `/<file>/<section>/<tag>` or `/<file>/<section>`, prefixed by
  `/<domain>` if any. Segments: lowercase, spaces to hyphens,
  punctuation dropped.
- Tests cite paths in a comment; documents cite them as plain text.

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
- [coverage] Every tag has a test or is marked not testable; every
  test path resolves.

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

## Examples

- Work from examples, not rules. `examples/01_todo_cli/`: a short
  terminal to-do list.

## Migration from v3

- `spec/main/` becomes `docs/`; `spec/changes/` becomes `docs_future/`.
- Rule IDs (`R5`) become tags, cited by path.
