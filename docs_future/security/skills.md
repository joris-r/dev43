# Security in the skills

- `init` creates `docs/security.md` with its title alone; the framing
  fills it. On existing code it stays empty, with the backlog entry
  "write the threat model".
- `specify-existing`: the agent lists the entry points of the zone
  from the code; the human claims who may run each operation and what
  is sensitive. A counterexample is a bug entry. On existing code,
  "write the threat model" is a `specify-existing` increment.
- Planning: a change that adds an asset, actor, entry point or
  boundary has `security.md` in its scope, takes `full` or
  `specify-existing`, and the Exploration of Specification as a gate.
- Supervision: accepting a threat or uncovered surface goes to the
  human; a mitigation the future specification states is the
  supervisor's. The final hand-over lists the threats the feature
  added and how each was ruled.
