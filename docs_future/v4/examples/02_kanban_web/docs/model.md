# Model

## Column

One of three fixed stages: `todo` (shown "To do"), `doing` ("Doing"),
`done` ("Done"), in that order.

## Card

Something the user has to do.

- `id: integer`, identifies the card.
  - [unique] Assigned at creation, one above the highest ever assigned.
- `title: string`, what to do.
  - [nonempty] Not empty.
- `column: Column`, the card's stage.
  - [fresh] `todo` at creation.

## Board

All cards, grouped by column, oldest first within each.
