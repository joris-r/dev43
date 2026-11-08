# API

## General

JSON in and out. A card reads `{"id": 1, "title": "write tests",
"column": "todo"}`.

- [errors] A refused operation answers `{"error": "<message>"}`: 400
  for invalid input, 404 for an unknown card.

## Board

`GET /cards` runs /operations/board. Answers 200 with the cards, in
board order.

## Add

`POST /cards` with `{"title": "write tests"}` runs /operations/add.
Answers 201 with the new card.

## Move

`PATCH /cards/<id>` with `{"column": "doing"}` runs /operations/move.
Answers 200 with the card.

## Delete

`DELETE /cards/<id>` runs /operations/delete. Answers 204.
