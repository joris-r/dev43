# Threat model

`docs/security.md` answers four questions:

- Assets: what the project protects.
- Actors: whom it defends against.
- Boundaries: where input comes from someone less trusted, and the
  actors at each.
- Threats: one tagged entry each, pointing to its mitigation, or
  accepted by the human.

It is always present; for software with nothing to defend, a few
lines say so. Empty, it is not written yet.

The silver rule applies: only the threats where another choice would
matter to the human. A threat comes from an asset and a boundary of
the project; the catalogs are for the agent to search with, never to
copy.

A mitigation is stated where its behavior lives (e.g. a case of
`operations.md`), and the threat points to it. Tests cite the
mitigation like any other behavior.

An operation reachable from a less-trusted actor states who may run
it and refuses the others, in a tagged case. A rule under General in
`operations.md` covers several operations at once (e.g. `[owner] Only
the owner of a board runs its operations.`).

The agent brings the expertise (STRIDE, OWASP) and derives the
threats from the model and the operations. The human decides what is
sensitive, whom to defend against, and which risks to accept.

An abuse scenario has an attacker of `security.md` as its actor, names
the threat it plays, and ends on the refusal or limit a mitigation
states.

The form examples get a `security.md`:

- `cli.md`: one local user, who owns the data; nothing to defend.
- `web.md`, still single-user and local: a hostile page in the same
  browser calls the API (`[foreign-page]`); the server listens on
  `127.0.0.1` (`technical.md`) and refuses a foreign `Host` or
  `Origin` (General of `operations.md`); an abuse scenario shows it.
