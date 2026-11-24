# Security

## Assets

- The cards, which only the user reads and changes.

## Actors

- A foreign page: a page of another site, open in the user's browser.
- A local program: any other program on the user's machine.

## Boundaries

- The HTTP interface: the user's page, foreign pages and local
  programs.
- The database, `kanban.db`: local programs.

## Threats

### The HTTP interface

- [foreign-page] A foreign page reads or changes the cards.
  - Mitigated: /technical, /operations/general/origin.
- [local-request] A local program reads or changes the cards through
  the HTTP interface.
  - Accepted.

### The database

- [local-db] A local program reads or changes `kanban.db`.
  - Accepted.
