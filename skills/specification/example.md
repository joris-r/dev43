# add-list: add and list tasks

A to-do list on the command line: add tasks and list them.

## Data model

- Task
  - text: one line, not empty
  - done: false when added
- Tasks keep the order in which they were added; a task's number is its
  position, from 1.
- Stored as JSON:
  ```json
  {"version": 1, "tasks": [{"text": "buy some milk", "done": false}]}
  ```

## todo add

```console
$ todo add buy some milk
Added 1: buy some milk
```

## todo list

```console
$ todo list
1. [ ] buy some milk
```

- `todo` alone is `todo list`.

## Errors

- Messages go to standard error, prefixed with `todo: error:`.
- R1: On error, the data file is left unchanged.
- Exit 2: wrong command or option.
- Exit 1: any other error.

## Data file location

- First match wins:
  1. `--file PATH`
  2. `TODO_FILE`
  3. `$HOME/.local/share/todo/tasks.json`

## Technical

- R2: Write the data file to a temporary file in the same directory,
  then rename it.
