# Model

## Task

- `text: string` …
  - [nonempty] Not empty. …
  - [hash] Contains no `#`.
- `tags: set of /model/tag`, the tags given to it.

## Tag

A word the user puts on tasks to group them: a `string`.

- [word] Not empty, with no whitespace and no `#`.
- [lower] In lowercase.
