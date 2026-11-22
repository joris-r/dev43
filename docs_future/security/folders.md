# Folders

A folder of one kind of document starts with `_`; a domain folder
does not.

- `design/` becomes `_design/`, in the skills, the web example and
  the README. A `dev43:migrate` step moves it and fixes the links;
  the earlier steps keep `design/`.
- The scenarios are in `scenarios.md` or in `_scenarios/`, never
  both: several files, grouped as the project likes, one `##` section
  per scenario. The path drops the `_`: `/scenarios/checkout/<scenario>`.
  The skills say "the scenarios". Switching forms is a `direct`
  increment of the project, not a `dev43:migrate` step.
