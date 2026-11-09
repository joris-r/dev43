# Operations

## Add task

× - [stored] Text not empty:
- [stored] Text not empty, without `#`:
- [hash] Text containing `#`: refused, `No "#" in a task.`

## List tasks

× - [result] Returns the list.
- [result] No tag given: returns the list.
- [filter] Tag given: returns only the tasks with it, keeping their
  numbers: tasks 1 and 3 tagged shop, 2 tagged work, list shop: tasks
  1 and 3.

## Tag task

- [tagged] Known number, valid tag: the task has the tag; returns the
  tag, as stored: tag 1 Shop: task 1 has shop.
- [again] Task already has the tag: nothing changes, not an error;
  returns the tag.
- [invalid] Not a valid /model/tag: refused, `Not a tag: <tag>.`
- [missing] Unknown number: refused, `No task <number>.`

## Untag task

- [untagged] Task has the tag: it no longer has it; returns the tag.
- [absent] Task without the tag: nothing changes, not an error;
  returns the tag.
- [missing] Unknown number: refused, `No task <number>.`
