# Operations

## General

- [refused] A refused operation changes nothing and gives a message.

## Add task

- [stored] Text not empty:
  - a new task with the text is stored, at the end of the list;
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
