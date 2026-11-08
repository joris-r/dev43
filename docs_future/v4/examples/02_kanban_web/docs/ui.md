# UI

## Board page

The only page, at `/`. Opening it runs /operations/board.

Contains, top to bottom:

- an Error banner;
- the three Columns, side by side, in column order.

Every action updates the page without a reload.

## Error banner

- [show] Shows the message of a refused action, until the next action.
- [hidden] Hidden while there is no message.

## Column

- Header: the column's name.
- An Add form, in To do only.
- Its Cards, in board order.

## Add form

A text field and an "Add" button.

- "Add" runs /operations/add with the field's text.
- [cleared] The field is emptied after a success.

## Card

The card's title, then its buttons:

- "←" runs /operations/move to the previous column.
- "→" runs /operations/move to the next column.
- "×" runs /operations/delete, at once.
- [edges] A card in To do has no "←"; a card in Done has no "→".
