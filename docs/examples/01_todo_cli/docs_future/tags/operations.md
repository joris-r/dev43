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
