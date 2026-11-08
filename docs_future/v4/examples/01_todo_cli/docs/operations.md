# Operations

## Add

Adds a task with the given text at the end of the list.

- [first] Empty list, add "buy milk": the list holds task 1, "buy milk", not
  done.
- [empty] Add an empty text: refused, nothing changes.

## List

Returns all tasks, in list order.

## Done

Marks a task as done.

- [open] Task 2 open, done 2: task 2 is done.
- [again] Task 2 already done, done 2: nothing changes, not an error.
- [missing] No task 7, done 7: refused.

## Remove

Removes a task, done or not. The tasks after it move up one number.

- [shift] Tasks 1 "buy milk", 2 "call Ann", remove 1: "call Ann" is now task 1.
- [missing] No task 7, remove 7: refused.
