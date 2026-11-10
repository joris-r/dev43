# Operations

## General

- [refused] A refused operation changes nothing and gives a message.

## Initial state

- [empty] The list holds no task.

## Add task

Inputs:
- `text: string`

Cases:
- [stored] Text not empty:
  - a new task with the text, not done, is at the end of the list;
  - returns the new task.
- [empty] Empty text: refused, `Text is empty.`

## List tasks

- [result] Returns the list.

## Mark done

Inputs:
- `number: integer`

Cases:
- [done] Number of an open task: the task is done; returns it.
- [again] Number of a done task: nothing changes; returns it.
- [missing] Any other number: refused, `No task <number>.`

## Remove task

Inputs:
- `number: integer`

Cases:
- [removed] Number of a task:
  - the task is removed from the list;
  - returns the removed task.
- [missing] Any other number: refused, `No task <number>.`
