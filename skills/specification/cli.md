# Form: a CLI

The specification of a small to-do CLI, in `docs/`. Match its form and level of detail, not its content.

## `README.md`

````markdown
# Todo documentation

- [overview.md](overview.md): what the tool is for.
- [technical.md](technical.md): stack and storage.
- [model.md](model.md): what is stored, sets the vocabulary.
- [operations.md](operations.md): what each action does to it.
- [ui.md](ui.md): the commands and their output.
- [scenarios.md](scenarios.md): typical use.
````

## `overview.md`

````markdown
# Overview

A personal to-do list for the terminal. One user, one machine: add a
task, see what is left, tick it off.

## Non-goals

- No sync, sharing or accounts.
- No due dates, priorities or tags.
````

## `technical.md`

````markdown
# Technical

- Python 3.12, standard library only.
- Installed as a `todo` command.
- Tasks are stored in one JSON file, `~/.todo.json`, created on first
  write.
````

## `model.md`

````markdown
# Model

## Task

Something the user has to do.

- `text: string`, what to do.
  - [nonempty] Not empty.
- `done: boolean`, whether the user has ticked it off.

## List

The ordered sequence of all tasks.

- [order] Oldest first.
- [number] A task's number is its position in the list, starting at 1.
````

## `operations.md`

````markdown
# Operations

## General

- [refused] A refused operation changes nothing and gives a message.

## Add task

- [stored] Text not empty:
  - a new task with the text, not done, is stored, at the end of the
    list;
  - returns the new task.
- [empty] Empty text: refused, `Text is empty.`

## List tasks

- [result] Returns the list.

## Mark done

- [done] Open task: it is done; returns it.
- [again] Task already done: nothing changes, not an error; returns
  it.
- [missing] Unknown number: refused, `No task <number>.`

## Remove task

- [removed] Known number:
  - the task is removed, done or not;
  - the tasks after it move up one number: tasks 1 "buy milk", 2
    "call Ann", remove 1: "call Ann" is now task 1;
  - returns the removed task.
- [missing] Unknown number: refused, `No task <number>.`
````

## `ui.md`

````markdown
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
````

## `scenarios.md`

````markdown
# Scenarios

## First day

The user has never used the tool.

- They add "buy milk", then "call Ann".
- They list: both appear, as 1 and 2, not done.
- They call Ann and run `todo done 2`.
- They list again: "call Ann" is marked done.

## Cleaning up

The list holds 1 "buy milk" (done) and 2 "call Ann".

- The user removes 1.
- They list: "call Ann" is now task 1.
````
