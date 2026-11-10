# Model

## Task

Something the user has to do.

- `text: string`, what to do.
  - [nonempty] Not empty.
- `done: boolean`, whether the user has ticked it off.

## List

The state: everything the tool stores.

- `tasks: list of /model/task`, all the tasks.

A task's number: its position in the list, starting at 1.
