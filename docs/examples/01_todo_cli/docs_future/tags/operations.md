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
