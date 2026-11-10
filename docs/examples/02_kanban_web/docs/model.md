# Model

## Column

One of three fixed stages of work.

- [stages] `todo`, `doing` or `done`, in that order.

## Card

Something the user has to do.

- `id: integer`, identifies the card.
  - [unique] No two cards share it.
- `title: string`, what to do.
  - [trimmed] Not empty, with no whitespace at its start or end.
- `column: /model/column`, the card's stage.
- `position: integer`, the card's place in its column, 1 at the top.
  - [contiguous] In each column, the positions run from 1 to the
    number of cards in it, each used once.

## Board

The state: everything the application stores.

- `cards: set of /model/card`, all the cards.

Board order: the cards by column, in column order, then by position.
