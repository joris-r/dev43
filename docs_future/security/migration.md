# Migration: to 4.8

- Every `design/` becomes `_design/`, in domain folders and in
  `docs_future/<feature>/` too; what refers to the old path (the
  README index, sometimes a build file) follows. `docs/security.md` is
  created empty, and `docs_future/BACKLOG.md` gets "write the threat
  model". A Specification phase alone, its Verification the one gate.
- "Write the threat model" is a `specify-existing` increment, the
  specification complete or not, its Exploration a gate. Code that
  breaks a claim is a bug entry.
- While `security.md` is empty, `[security]` checks only the common
  flaws; planning proposes "write the threat model" first when an
  increment adds an entry point.
