# UI

## Board page

At `/`.

Shows, top to bottom:
- [banner] the Error banner;
- [columns] the three Columns, side by side, in column order.

## Error banner

Shows, by state:
- [hidden] Page opened: hidden.
- [message] Operation refused or failed: its message.
  - Next operation succeeds: hidden.

## Column

Shows, top to bottom:
- [name] its name;
- [add] the Add form, in To do only;
- [cards] its Cards, in board order.

## Add form

Shows:
- [field] a text field, emptied once a card is added.

Actions:
- [add] Enter, or focus leaving the field with text in it: runs
  /operations/add-card with the field's text.
- [cancel] Esc in the field: empties it; nothing is added.

## Card

Shows:
- [title] its title, then a "×" button.

Actions:
- [delete] "×" clicked: runs /operations/delete-card, without
  confirmation.
- [pad] Clicked elsewhere: opens the Move pad on it.

## Move pad

Shows, by state:
- [closed] Page opened: hidden.
- [open] Opened on a card: next to it, four arrows in a cross, "↑"
  above, "↓" below, "←" left, "→" right.
  - Opened on another card: moves to it.
  - An arrow clicked, Esc, or a click outside: hidden.

Actions:
- [up] "↑": runs /operations/move-card one position up; disabled at
  the top.
- [down] "↓": one position down; disabled at the bottom.
- [left] "←": to the end of the previous column; disabled in To do.
- [right] "→": to the end of the next column; disabled in Done.
