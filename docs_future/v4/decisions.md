# v4 decisions

## Layout

- Documents: README, overview, technical, design, model, operations,
  ui, scenarios. Each added only when needed; top level for what spans
  domains, a domain folder for what is specific to it.
- `operations.md` defines the actions on the data of `model.md`,
  queries included; `ui.md` offers them and refers to them, adding only
  how they are triggered and shown.
- Each concept or operation has its own `##` section, named the same
  across documents (`## Add` in operations and api).
- A web `ui.md` follows the UI's structure: one `##` section per page
  or component, listing what it contains; each action refers to its
  operation. `design.md` uses the same component names.

## Traceability

- A tag is a short name in brackets at the start of a line:
  `- [empty] Add an empty text: refused.`
- Tag only what a test checks on its own.
- A tag is unique within its section only.
- A reference is a path: `/<file>/<section>/<tag>`, or
  `/<file>/<section>` for a whole section. With domains:
  `/<domain>/<file>/...`.
- Heading to path segment: lowercase, spaces to hyphens, punctuation
  dropped (`First day` → `first-day`).
- A test cites the exact path in a comment, and may cite several.
- Documents cite a path as plain text:
  `` `todo add` runs /operations/add. ``

## Examples

- Work from examples, not rules. `examples/01_todo_cli/`: a short
  terminal to-do list.

## Migration from v3

- `spec/main/` becomes `docs/`; `spec/changes/` becomes `docs_future/`.
- Rule IDs (`R5`) become tags, cited by path.
