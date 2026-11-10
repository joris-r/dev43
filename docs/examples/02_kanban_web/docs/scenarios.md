# Scenarios

## First card

The board is empty.

- The user types "write tests" and presses Enter.
- The card appears in To do, and the field is empty again.
- They move it right twice, through the Move pad: the card is in
  Done, and its Move pad has "→" disabled.

## Clearing done work

The board holds "write tests" in Done.

- The user clicks "×" on it.
- The board is empty.
- They reload the page: the board is still empty.

## Prioritizing

To do holds "write tests", then "fix bug".

- The user opens the Move pad on "fix bug" and clicks "↑".
- To do shows "fix bug", then "write tests"; the Move pad
  on "fix bug" has "↑" disabled.
- They reload the page: the order is kept.
