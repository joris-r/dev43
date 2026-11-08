# Operations

## Board

Returns the board.

## Add

Adds a card with the given title.

- [first] Empty board, add "write tests": the board holds one card,
  "write tests", in To do.
- [empty] Add an empty title: refused, nothing changes.

## Move

Puts a card in the given column.

- [forward] "write tests" in To do, move to Doing: it is in Doing.
- [any] A card can move to any column, backward included.
- [missing] Unknown card: refused.

## Delete

Removes a card.

- [gone] Delete "write tests": it is no longer on the board.
- [missing] Unknown card: refused.
