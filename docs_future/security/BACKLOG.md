# Security

The specification states the project's threat model, the scenarios
show abuse paths, and every increment takes part in security.

## Outline

1. Threat model: a new `docs/security.md` (assets, actors, trust
   boundaries, threats, the mitigations they require), cited by tests
   like the other documents.
2. Folders: `docs/design/` becomes `docs/_design/`; the scenarios live
   in `scenarios.md` or in `_scenarios/`, one file each, as the
   project needs, abuse paths beside the nominal ones.
3. Security check: a new agent check at the Verification of every
   increment, against `security.md` and the diff.
4. Skills: security considerations in the existing skills (framing,
   specification, tests, implementation, soundness, retrospective).
5. Migration, a minor version: a `dev43:migrate` step renames
   `design/`, creates an empty `security.md` and adds the backlog
   entry "write the threat model". That increment, planned by the
   human, brings the changes to the existing specification; code that
   breaks them becomes bug entries. Until then, the security check
   runs on what `security.md` holds.
