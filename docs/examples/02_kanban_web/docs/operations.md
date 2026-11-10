# Operations

## General

The page runs every operation on the server. JSON in and out; a card
reads `{"id": 1, "title": "write tests", "column": "todo",
"position": 1}`.

- [malformed] Body not JSON, or an input missing or not of its type:
  refused, 400, `Malformed request.`
- [refused] A refused operation changes nothing and answers
  `{"error": "<message>"}`.

## Initial state

- [empty] The board holds no card.

## Show board

HTTP: `GET /cards`.

- [result] Answers 200 with all cards, in board order.

## Add card

HTTP: `POST /cards` with `{"title": "write tests"}`.

Inputs:
- `title: string`

Cases:
- [accepted] Title not empty once trimmed:
  - a new card is stored: an id no card has, the trimmed title, in
    `todo`, at the position after its last card;
  - answers 201 with the new card.
- [empty] Title empty once trimmed: refused, 400, `Title is empty.`

## Move card

Records the progress or the priority of a card.

HTTP: `PATCH /cards/<id>` with `{"direction": "up"}`.

Inputs:
- `id: integer`
- `direction: one of up, down, left, right`

Cases:
- [up] Known id, `up`, card not at the top of its column:
  - it swaps positions with the card above it;
  - answers 200 with the card.
- [down] Known id, `down`, card not at the bottom of its column:
  - it swaps positions with the card below it;
  - answers 200 with the card.
- [left] Known id, `left`, card not in `todo`:
  - the card is in the previous column, at the position after its
    last card;
  - in the column it left, the cards below it move up one position;
  - answers 200 with the card.
- [right] Known id, `right`, card not in `done`:
  - the card is in the next column, at the position after its last
    card;
  - in the column it left, the cards below it move up one position;
  - answers 200 with the card.
- [edge] Known id, any other move: refused, 400,
  `Cannot move <direction>.`
- [missing] Unknown id: refused, 404, `No card <id>.`

## Delete card

HTTP: `DELETE /cards/<id>`.

Inputs:
- `id: integer`

Cases:
- [removed] Known id:
  - the card is no longer stored;
  - in its column, the cards below it move up one position;
  - answers 204.
- [missing] Unknown id: refused, 404, `No card <id>.`
