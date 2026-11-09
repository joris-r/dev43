# UI

## List tasks

× Command: `todo list` runs /operations/list-tasks.
Command: `todo list [<tag>]` runs /operations/list-tasks.

× - [lines] Some tasks: one line per task, `<number>  [<mark>] <text>`,
×   the mark `x` when done, a space otherwise.
- [lines] Some tasks: one line per task,
  `<number>  [<mark>] <text>  <tags>`, the mark `x` when done, a space
  otherwise, the tags in alphabetical order, each as `#<tag>`,
  separated by a space.
× - [empty] No task: `Nothing to do.`
- [empty] No tag given, no task: `Nothing to do.`
- [nomatch] Tag given, no task has it: `No task tagged <tag>.`

## Tag task

Command: `todo tag <number> <tag>` runs /operations/tag-task.

Prints:
- [tagged] `Tagged <number>: <tag>`, the tag as stored, also when the
  task already had it.

## Untag task

Command: `todo untag <number> <tag>` runs /operations/untag-task.

Prints:
- [untagged] `Untagged <number>: <tag>`, also when the task did not
  have it.
