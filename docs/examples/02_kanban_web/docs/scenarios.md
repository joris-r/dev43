# Scenarios

## First card

The board is empty.

- The user types "write tests" and presses Enter.
- The card appears in To do, and the field is empty again.
- They click the card, then "→", twice: the card is in Done.
- They click the card: its Move pad has only "←" enabled.

## Clearing done work

The board holds "write tests" in Done.

- The user clicks "×" on it.
- The board is empty.
- They reload the page: the board is still empty.

## Prioritizing

To do holds "write tests", then "fix bug".

- The user clicks "fix bug", then "↑".
- To do shows "fix bug", then "write tests".
- They reload the page: the order is kept.

## Foreign page

Plays /security/threats/foreign-page. The board holds "write tests" in
To do.

- A foreign page sends `POST /cards` with `{"title": "spam"}` as plain
  text.
- It is refused, 403.
- The user reloads the page: the board holds only "write tests".
