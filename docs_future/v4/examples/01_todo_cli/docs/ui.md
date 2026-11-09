# UI

## General

One command, `todo`, with a subcommand per operation.

- [errors] Operation refused: its message on stderr, exit code 1.
- [success] Operation succeeded: exit code 0.
- [usage] No subcommand, or an unknown one: prints the usage, exit
  code 1.

## Add task

Command: `todo add <text>` runs /operations/add-task; the text is the
rest of the line, words joined by spaces.

Prints:
- [added] `Added <number>: <text>`

## List tasks

Command: `todo list` runs /operations/list-tasks.

Prints, by outcome:
- [lines] Some tasks: one line per task, `<number>  [<mark>] <text>`,
  the mark `x` when done, a space otherwise.
- [empty] No task: `Nothing to do.`

## Mark done

Command: `todo done <number>` runs /operations/mark-done.

Prints:
- [done] `Done <number>: <text>`, also when it was already done.

## Remove task

Command: `todo rm <number>` runs /operations/remove-task.

Prints:
- [removed] `Removed <number>: <text>`
