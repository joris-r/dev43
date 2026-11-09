# Operations

## Add

- [hash] Add a text containing `#`: refused, nothing changes.

## List

× Returns all tasks, in list order.
Returns all tasks, or only those with a given tag, in list order.

- [filter] Tasks 1 and 3 tagged shop, 2 tagged work, list shop: tasks 1
  and 3, keeping their numbers.

## Tag

Gives a tag to a task.

- [first] Task 1 untagged, tag 1 Shop: task 1 has shop.
- [again] Task 1 has shop, tag 1 shop: nothing changes, not an error.
- [invalid] Tag 1 "big shop": refused.
- [missing] No task 7, tag 7 shop: refused.

## Untag

Takes a tag off a task.

- [has] Task 1 has shop, untag 1 shop: task 1 has no tag.
- [absent] Task 1 without urgent, untag 1 urgent: nothing changes, not
  an error.
- [missing] No task 7, untag 7 shop: refused.
