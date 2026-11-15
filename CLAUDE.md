# Dev43 plugin

Start by reading [process_principles.md](docs/process_principles.md).

This repository is the Dev43 process, packaged as a Claude Code plugin.
The operational rules live in [skills/](skills/).

[process_principles.md](docs/process_principles.md) holds only the context and
the principles. Amend it only for an important topic, such as a new or
changed principle. Never copy skill details into it.

## Commits

- Propose a commit once your changes are complete and coherent.
- Commit only when the human says so and confirms they reviewed the changes.
- Leave pushing to the human.

## Releases

Release only when the human asks. A release:

- sets `version` in [plugin.json](.claude-plugin/plugin.json);
- adds the version to [CHANGELOG.md](CHANGELOG.md), with its date and
  its changes in one or two lines; a new minor version also gets its
  subsection, a new major version its section and its impact;
- is the commit `vX.Y.Z: <summary>`, its body listing the changes,
  tagged `vX.Y.Z`.

Numbering, by the impact on a project following Dev43:

- major: an incompatible change of the documents or the process; the
  project migrates before any work, with `dev43:migrate`.
- minor: a new or improved rule; the project needs some updates to
  follow it, given by a step of `dev43:migrate` when the documents or
  the tests change.
- patch: a fix or clarification of a rule or a script; the project
  works as it is.
