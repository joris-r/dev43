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
````

## `operations.md`

````markdown
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
````

## `ui.md`

````markdown
# UI

## Board page

At `/`.

Shows, top to bottom:
- [banner] the Error banner;
- [columns] the three Columns, side by side, in column order.

## Error banner

Shows, by state:
- [hidden] Page opened: hidden.
- [message] Operation refused or failed: its message.
  - [cleared] Next operation succeeds: hidden.

## Column

Shows, top to bottom:
- [name] its name;
- [add] the Add form, in To do only;
- [cards] its Cards, in board order.

## Add form

Shows:
- [field] a text field, emptied once a card is added.

Actions:
- [add] Enter, or focus leaving the field with text in it: runs
  /operations/add-card with the field's text.
- [cancel] Esc in the field: empties it; nothing is added.

## Card

Shows:
- [title] its title, then a "×" button.

Actions:
- [delete] "×" clicked: runs /operations/delete-card, without
  confirmation.
- [pad] Clicked elsewhere: opens the Move pad on it.

## Move pad

Shows, by state:
- [closed] Page opened: hidden.
- [open] Opened on a card: next to it, four arrows in a cross, "↑"
  above, "↓" below, "←" left, "→" right.
  - [moved] Opened on another card: moves to it.
  - [dismissed] An arrow clicked, Esc, or a click outside: hidden.

Actions:
- [up] "↑": runs /operations/move-card one position up; disabled at
  the top.
- [down] "↓": one position down; disabled at the bottom.
- [left] "←": to the end of the previous column; disabled in To do.
- [right] "→": to the end of the next column; disabled in Done.
````

## `scenarios.md`

````markdown
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
````
