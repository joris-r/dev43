# Form: a future specification

A large change is written ahead in `docs_future/<feature>/`. It
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
  with the sections it integrates, closed under its dependencies,
  cited or not;
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
   /operations/add-task, /operations/tag-task,
   /operations/untag-task, /ui/tag-task, /ui/untag-task, /technical.
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

## `technical.md`

````markdown
# Technical

- [migrate] A file written before tags has every `#` removed from its
  texts on first read; a task left with an empty text is removed.
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

A word the user puts on tasks to group them.

- [word] One word: no space, no `#`.
- [lower] Stored in lowercase: `Shop` and `shop` are the same tag.
````

## `operations.md`

````markdown
# Operations

## Add task

× - [stored] Text not empty:
- [stored] Text not empty, without `#`:
- [empty] Empty text: refused, `Text is empty.` …
- [hash] Text containing `#`: refused, `No "#" in a task.`

## List tasks

× - [result] Returns the list.
- [result] No tag given: returns the list.
- [filter] Valid tag given: returns only the tasks with it, keeping
  their numbers: tasks 1 and 3 tagged shop, 2 tagged work, list shop:
  tasks 1 and 3.
- [invalid] Not a valid /model/tag: refused, `Not a tag: <tag>.`

## Tag task

- [tagged] Known number, valid tag, task without it: the task has the
  tag; returns the tag, as stored: tag 1 Shop: task 1 has shop.
- [again] Known number, valid tag, task already has it: nothing
  changes, not an error; returns the tag, as stored.
- [invalid] Known number, not a valid /model/tag: refused,
  `Not a tag: <tag>.`
- [missing] Unknown number: refused, `No task <number>.`

## Untag task

- [untagged] Known number, valid tag, task has it: it no longer has
  it; returns the tag, as stored.
- [absent] Known number, valid tag, task without it: nothing changes,
  not an error; returns the tag, as stored.
- [invalid] Known number, not a valid /model/tag: refused,
  `Not a tag: <tag>.`
- [missing] Unknown number: refused, `No task <number>.`
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
- [tagged] `Tagged <number>: <tag>`, the tag as stored, also when the
  task already had it.

## Untag task

Command: `todo untag <number> <tag>` runs /operations/untag-task.

Prints:
- [untagged] `Untagged <number>: <tag>`, the tag as stored, also when the task did not
  have it.
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
