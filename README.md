# Dev43

A specification-driven development process for humans and LLM agents,
packaged as a Claude Code plugin. The process itself is described in
[process_principles.md](process_principles.md).


## Install

From a Claude Code panel in VSCode:

- open the "/" menu
- go to "Manage plugins" (Customize section)
- in the "Marketplaces" tab:
  - paste `joris-r/dev43`
  - click "Add"
- in the "Plugins" tab:
  - dev43 should show up
  - click "Install"
  - choose "Install for you" (or any other option)
  - "dev43@dev43" should appear with a green dot


## Usage

In a new or existing project, run:

```
/dev43:init
```

This creates and commits:

- `CLAUDE.md`, telling the agent to use Dev43 (add your own directives below)
- `spec/BACKLOG.md`, for future work
- `spec/STATE.md`, where the agent records the current phase, step and topic

Work happens in phases, each with three steps:

1. **Exploration**: you discuss with the agent. When you're ready, say "next".
2. **Production**: the agent does the work in one go. It tags any important
   choice that you didn't discuss together.
3. **Verification**: you review the work and stage the reviewed files with git.
   Remove a tag if you agree with the choice, or discuss it with the agent.
   When everything is staged and no tags remain, say "next".

The first increment sets up the stack with a trivial feature, such as a
health check. On existing code, it describes the existing stack instead,
and you then specify the software zone by zone, as you need to change it.
Then you are in Pause: ask for something and the agent starts
an increment, which can go through these phases:

1. Specification
2. Tests
3. Implementation
4. Integration

The agent proposes to skip phases or steps that add nothing, and there are
shorter paths for bug fixes, refactoring and tool updates.


## License

MIT, see [LICENSE](LICENSE).
