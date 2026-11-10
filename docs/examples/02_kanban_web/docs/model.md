# Model

## Column

One of three fixed stages.

- [stages] `todo` (shown "To do"), `doing` ("Doing"), `done`
  ("Done"), in that order.

## Card

Something the user has to do.

- `id: integer`, identifies the card.
  - [unique] No two cards share it.
- `title: string`, what to do.
  - [nonempty] Trimmed and not empty.
- `column: /model/column`, the card's stage.
- `position: integer`, the card's place in its column.
  - [top] 1 at the top.
  - [contiguous] In each column, positions run from 1 to the number
    of cards in it.

## Board

All cards, grouped by column in column order, each column ordered by
position: the board order.
