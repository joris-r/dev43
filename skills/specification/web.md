# Form: a web application

The specification of a small kanban web application, in `docs/`. Match its form and level of detail, not its content. Its `design/board-page.html` is a static HTML page with one frame per set of states, its values as CSS variables at the top, and real content in every state.

## `README.md`

````markdown
# Kanban documentation

- [overview.md](overview.md): what the app is for.
- [technical.md](technical.md): stack and architecture.
- [design/](design/): mockups of the look, checked by eye.
- [model.md](model.md): what is stored, sets the vocabulary.
- [operations.md](operations.md): what each action does to it, and
  its HTTP interface.
- [ui.md](ui.md): the page and its actions.
- [scenarios.md](scenarios.md): typical use.
````

## `overview.md`

````markdown
# Overview

A kanban to-do board, as a local web application. A didactic project,
for a single user on their own machine: cards move from To do to Done.

## Non-goals

- No accounts, sharing or remote access.
- No custom columns.
````

## `technical.md`

````markdown
# Technical

- A local server and a single web page.
- Server: Python 3.12, Flask, SQLite in `kanban.db` in the working
  directory. Listens on `127.0.0.1:8000`.
- Page: plain HTML, CSS and JavaScript, served by the same server.
  It updates without a reload.
````

## `model.md`

````markdown
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
````

## `operations.md`

````markdown
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
````

## `ui.md`

````markdown
# UI

## General

- [current] The page shows the board as stored: it runs
  /operations/show-board when opened, and follows each operation it
  runs.

## Board page

At `/`.

Shows, top to bottom:
- [banner] the Error banner;
- [columns] the three Columns, side by side, in column order.

## Error banner

Shows, by state:
- [hidden] Page opened, or an operation succeeds: hidden.
- [message] An operation is refused: its message.
- [unreachable] An operation gets no answer: `Server unreachable.`

## Column

Shows, top to bottom:
- [name] its name: "To do" for `todo`, "Doing" for `doing`, "Done"
  for `done`;
- [add] the Add form, in To do only;
- [cards] its Cards, in board order.

## Add form

Shows:
- [field] a text field, empty when the page opens, with the
  placeholder `New card`.

Actions:
- [add] Enter, or focus leaving the field, with text in it: runs
  /operations/add-card with the text as title; once it succeeds, the
  field is empty.
- [cancel] Esc in the field: the field is empty; nothing runs.

## Card

Shows:
- [title] its title, then a "×" button.

Actions:
- [delete] "×" clicked: runs /operations/delete-card with its id,
  without confirmation.
- [pad] Clicked elsewhere: opens the Move pad on it.

## Move pad

Shows, by state:
- [closed] Page opened: hidden.
- [open] Opened on a card, also when open on another: next to that
  card, four arrows in a cross, "↑" above, "↓" below, "←" left, "→"
  right; an arrow is disabled when its move would be refused.
- [dismissed] An arrow clicked, Esc, its card deleted, or a click
  outside the pad and the cards: hidden.

Actions:
- [move] An arrow clicked: runs /operations/move-card with the card's
  id and the arrow's direction: `up` for "↑", `down` for "↓", `left`
  for "←", `right` for "→".
````

## `scenarios.md`

````markdown
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
````
