# Model

## Task

- `text: string` …
  - [hash] Contains no `#`.
- `tags: set of /model/tag`, the tags given to it.

## Tag

A word the user puts on tasks to group them.

- [word] One word: no space, no `#`.
- [lower] Stored in lowercase: `Shop` and `shop` are the same tag.
