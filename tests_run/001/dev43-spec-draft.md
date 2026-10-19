DOMAIN = MAIN

# Increment add-list: add and list tasks

A task is a text and a done/not-done status. Tasks keep the order in
which they were added, and are numbered by their position, from 1.

## F-MAIN-001 — Add a task

```console
$ todo add buy some milk
Added 1: buy some milk
$ todo add "call   Bob"
Added 2: call   Bob
```

The words are joined with spaces and the text is trimmed. A new task is
not done. Duplicates are allowed. An empty text or a text containing a
newline is refused.

## F-MAIN-002 — List tasks

```console
$ todo list
1. [ ] buy some milk
2. [ ] call   Bob
$ todo
1. [ ] buy some milk
2. [ ] call   Bob
```

`todo` alone is `todo list`. An empty list prints nothing.

## F-MAIN-003 — Errors

| Situation                          | Exit |
|------------------------------------|------|
| Wrong command or option            | 2    |
| Empty text or text with a newline  | 1    |
| Data file unreadable or invalid    | 1    |
| Data file cannot be written        | 1    |

Messages go to standard error, prefixed with `todo: error:`. On error,
the data file is left unchanged.

## F-MAIN-004 — Data file location

First match wins:

1. `todo --file PATH ...` (the option comes before the sub-command);
2. the `TODO_FILE` environment variable, if not empty;
3. `$HOME/.local/share/todo/tasks.json`.

A missing file is an empty list. `add` creates it, with its directories;
`list` never does.

## I-MAIN-001 — Data file format

```json
{
  "version": 1,
  "tasks": [
    {"text": "buy some milk", "done": false}
  ]
}
```

UTF-8, accents kept as is, indented by 2 spaces. Any other shape, an
unknown key, or a text that `add` would refuse makes the file invalid.

## T-MAIN-022 — Safe write

The file is written to a temporary file in the same directory, then
renamed over the old one.
