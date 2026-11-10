# UI

## General

- [current] The page shows the board as stored: it runs
  /operations/show-board when opened, and follows each operation it
  runs.

## Board page

At `/`.

Shows, top to bottom:
- [banner] the Error banner;
- [columns] the three Columns, side by side, in column order.

## Error banner

Shows, by state:
- [hidden] Page opened, or an operation succeeds: hidden.
- [message] An operation is refused: its message.
- [unreachable] An operation gets no answer: `Server unreachable.`

## Column

Shows, top to bottom:
- [name] its name: "To do" for `todo`, "Doing" for `doing`, "Done"
  for `done`;
- [add] the Add form, in To do only;
- [cards] its Cards, in board order.

## Add form

Shows:
- [field] a text field, empty when the page opens, with the
  placeholder `New card`.

Actions:
- [add] Enter, or focus leaving the field, with text in it: runs
  /operations/add-card with the text as title; once it succeeds, the
  field is empty.
- [cancel] Esc in the field: the field is empty; nothing runs.

## Card

Shows:
- [title] its title, then a "×" button.

Actions:
- [delete] "×" clicked: runs /operations/delete-card with its id,
  without confirmation.
- [pad] Clicked elsewhere: opens the Move pad on it.

## Move pad

Shows, by state:
- [closed] Page opened: hidden.
- [open] Opened on a card, also when open on another: next to that
  card, four arrows in a cross, "↑" above, "↓" below, "←" left, "→"
  right; an arrow is disabled when its move would be refused.
- [dismissed] An arrow clicked, Esc, its card deleted, or a click
  outside the pad and the cards: hidden.

Actions:
- [move] An arrow clicked: runs /operations/move-card with the card's
  id and the arrow's direction: `up` for "↑", `down` for "↓", `left`
  for "←", `right` for "→".
