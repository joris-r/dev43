# Form: a future specification

A large change is written ahead in `docs_future/<feature>/`, one
`future` increment per subject (see `dev43:planning`, Scope). It
mirrors the layout of `docs/` and holds only what changes:

- a plain line is added, right after the line above it;
- a line starting with `×` is removed (code blocks included);
- a line ending with `…` stands for the existing line that starts
  with the same text, as context;
- a heading that exists in `docs/` is context; a new section goes
  after the section above it, or at the end of the file.

A path in `docs_future/<feature>/` resolves against `docs/` with the
feature applied.

`docs_future/<feature>/BACKLOG.md` is the only file outside the
mirror:

- the feature's description, in a few lines;
- `## Outline`: the increments that build the feature, in order, each
  with the sections it integrates. Every section is in one increment,
  and `docs/` is closed after each of them;
- `## Lessons`: what the increments taught about the rest of the
  feature;
- `## For the human`: under supervision, the retrospective points on
  the project and the process, kept for the human.

Below, the feature `tags` of the CLI in [cli.md](cli.md). Match its
form, not its content.

## `BACKLOG.md`

````markdown
# Tags

Tasks get tags, and the list can be filtered by one.

## Outline

1. Tagging: /overview/non-goals, /model/task, /model/tag,
   /operations/general, /operations/add-task, /operations/tag-task,
   /operations/untag-task, /operations/migrate, /ui/tag-task,
   /ui/untag-task.
2. Filtering: /operations/list-tasks, /ui/list-tasks,
   /scenarios/shopping.

## Lessons
````

## `overview.md`

````markdown
# Overview

## Non-goals

× - No due dates, priorities or tags.
- No due dates or priorities.
````

## `model.md`

````markdown
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
````

## `operations.md`

````markdown
# Operations

## General

- [refused] A refused operation changes nothing …
- [lowercase] A tag input is lowercased first; it is valid when the
  result is a /model/tag.

## Add task

× - [stored] Text not empty:
- [stored] Text not empty, without `#`:
×   - a new task with the text, not done, is at the end of the list;
  - a new task with the text, not done, without tags, is at the end
    of the list;
- [empty] Empty text: refused, `Text is empty.` …
- [hash] Text with a `#`: refused, `No "#" in a task.`

## List tasks

Inputs:
- `tag: optional string`

Cases:
× - [result] Returns the list.
- [result] No tag: returns the list.
- [filter] Valid tag: returns the tasks with it, in list order, each
  with its number.
- [invalid] Tag not valid: refused, `Not a tag: <tag>.`

## Tag task

Inputs:
- `number: integer`
- `tag: string`

Cases:
- [tagged] Number of a task, valid tag: the task has the tag; returns
  the tag, lowercased.
- [invalid] Number of a task, tag not valid: refused,
  `Not a tag: <tag>.`
- [missing] Any other number: refused, `No task <number>.`

## Untag task

Inputs:
- `number: integer`
- `tag: string`

Cases:
- [untagged] Number of a task, valid tag: the task does not have the
  tag; returns the tag, lowercased.
- [invalid] Number of a task, tag not valid: refused,
  `Not a tag: <tag>.`
- [missing] Any other number: refused, `No task <number>.`

## Migrate

Trigger: the first read of a list stored before tags existed.

- [cleaned] Every `#` is removed from the texts, then every task with
  an empty text is removed from the list; no task has a tag.
````

## `ui.md`

````markdown
# UI

## List tasks

× Command: `todo list` runs /operations/list-tasks.
Command: `todo list [<tag>]` runs /operations/list-tasks.

× - [lines] Some tasks: one line per task, `<number>  [<mark>] <text>`,
×   the mark `x` when done, a space otherwise.
- [lines] Some tasks: one line per task,
  `<number>  [<mark>] <text>  <tags>`, the mark `x` when done, a space
  otherwise; `  <tags>` only when the task has tags, in alphabetical
  order, each as `#<tag>`, separated by a space.
× - [empty] No task: `Nothing to do.`
- [empty] No tag given, no task: `Nothing to do.`
- [nomatch] Valid tag given, no task has it: `No task tagged <tag>.`

## Tag task

Command: `todo tag <number> <tag>` runs /operations/tag-task.

Prints:
- [tagged] `Tagged <number>: <tag>`, the tag as returned.

## Untag task

Command: `todo untag <number> <tag>` runs /operations/untag-task.

Prints:
- [untagged] `Untagged <number>: <tag>`, the tag as returned.
````

## `scenarios.md`

````markdown
# Scenarios

## Shopping

The list holds 1 "buy milk", 2 "call Ann" and 3 "fix bike".

- The user tags 1 and 3 shop.
- They list shop: "buy milk" and "fix bike", as 1 and 3.
- At the shop they buy milk and run `todo done 1`.
````
