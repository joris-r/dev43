# Security

## Assets

- The cards, which only the user reads and changes.

## Actors

- A foreign page: a page of another site, open in the user's browser.
- A local program: any other program on the user's machine.

## Boundaries

- The HTTP interface: the user's page, foreign pages and local
  programs.

## Threats

- [foreign-page] A foreign page reads or changes the cards through the
  HTTP interface: mitigated by /technical and
  /operations/general/origin.
- [local-program] A local program reads or changes the cards: accepted.
