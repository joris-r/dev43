# Security

The specification states the project's threat model, the scenarios
show abuse paths, and every increment takes part in security.
[process.md](process.md) gives the whole in the process, and
[principle.md](principle.md) its principle.

## Outline

1. Threat model: a new `docs/security.md`, always present, and the
   abuse scenarios, in the form examples too; see
   [threat_model.md](threat_model.md).
2. Folders: `design/` becomes `_design/`; the scenarios live in
   `scenarios.md` or in `_scenarios/`; see [folders.md](folders.md).
3. Security check: `[security]`, an agent check of Implementation and
   Direct; see [check.md](check.md).
4. Skills: init, specify-existing, planning and supervision; see
   [skills.md](skills.md).
5. Migration, a minor version: a `dev43:migrate` step and the
   increment "write the threat model"; see
   [migration.md](migration.md).
