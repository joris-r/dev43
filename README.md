# Dev-4-3

A specification-driven development process for humans and LLM agents,
packaged as a Claude Code plugin. The process itself is described in
[process_principles.md](process_principles.md).

## Contents

- `templates/CLAUDE.md`: the rules agents must follow in a Dev-4-3 project
  (step gates, decision tags, spec layout, test protection).
- `templates/STATE.md`: tracks the current increment, phase and step.
- `commands/init.md`: `/dev43:init`, sets up a project.
- `skills/`: one skill per phase: `initial-framing`, `specification`,
  `tests`, `implementation`, `integration`.

## Install

From a terminal, with the Claude Code CLI:

```sh
claude plugin marketplace add /path/to/dev-4-3
claude plugin install dev43@dev43
```

The plugin is installed for your user, so it is also available in the
VS Code extension (which shares `~/.claude/`). Reload the VS Code window
afterwards.

If `claude` is not on your PATH, the VS Code extension ships its own copy:
`~/.vscode/extensions/anthropic.claude-code-<version>/resources/native-binary/claude`.
The `/plugin` slash command is not available inside the VS Code extension.

To try the plugin without installing it:

```sh
claude --plugin-dir /path/to/dev-4-3
```

## Usage

In a project, run:

```
/dev43:init
```

Only new projects are supported for now: adopting Dev-4-3 on existing
code (Retro-Specification) is future work.

This copies `CLAUDE.md` (or proposes a merge if one exists), creates the
`spec/` tree and `spec/STATE.md`, and starts the first Exploration. From
then on, the agent follows the skill of the current phase, and only you
move the work to the next step or phase.
