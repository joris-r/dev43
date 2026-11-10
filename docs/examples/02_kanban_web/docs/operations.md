# Operations

## General

The page runs every operation on the server. JSON in and out; a card
reads `{"id": 1, "title": "write tests", "column": "todo",
"position": 1}`.

- [refused] A refused operation changes nothing and answers
  `{"error": "<message>"}`.
- [malformed] Body not JSON, missing a field or with a value of the
  wrong type: refused, 400, `Malformed request.`

## Show board

HTTP: `GET /cards`.

- [result] Answers 200 with all cards, in board order.

## Add card

HTTP: `POST /cards` with `{"title": "write tests"}`.

- [accepted] Trimmed title not empty:
  - a new card with the trimmed title is stored, at the end of To do,
    its id one above the highest ever assigned;
  - answers 201 with the new card.
- [empty] Trimmed title empty: refused, 400, `Title is empty.`

## Move card

Records the progress or the priority of a card.

HTTP: `PATCH /cards/<id>` with `{"column": "doing", "position": 1}`.

- [moved] Known id, position from 1 to the number of cards in the
  column, the moved card included:
  - the card is at that position in that column;
  - the other cards keep their order: To do holds "a", "b", "c";
    move "c" to To do, position 1: To do holds "c", "a", "b";
  - answers 200 with the card.
- [position] Known id, any other position: refused, 400,
  `Position out of range.`
- [missing] Unknown id: refused, 404, `No card <id>.`

## Delete card

HTTP: `DELETE /cards/<id>`.

- [removed] Known id:
  - the card is no longer stored;
  - answers 204.
- [missing] Unknown id: refused, 404, `No card <id>.`
