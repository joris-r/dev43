# Dev43

A specification-driven development process for humans and LLM agents,
packaged as a Claude Code plugin. The process itself is described in
[process_principles.md](docs/process_principles.md).


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
- `docs/`, for the specification
- `docs_future/BACKLOG.md`, for future work

The agent records where the process stands in trailers at the end of
each commit message. So never clear the agent's
context while work is uncommitted.

You review the specification and try the software; agents check the
tests and the code. Work happens in phases, each with three steps:

1. **Exploration**: you discuss with the agent. When you're ready, say "next".
2. **Production**: the agent does the work in one go. It marks any choice
   it is unsure of.
3. **Verification**: you review the specification and stage the reviewed
   files with git. Remove a mark if you agree with the choice, or discuss
   it with the agent. When everything is staged and no marks remain, say
   "next".

You only meet the steps the plan of the increment stops at (see below).

The first increment sets up the stack with a trivial feature, such as a
health check. On existing code, it describes the existing stack instead,
and you then specify the software zone by zone, as you need to change it.
Then you are in Pause: ask for something and the agent starts
an increment, which can go through these phases:

1. Specification
2. Tests
3. Implementation

Each increment starts with a plan: the agent analyzes the potential impact
of the change and proposes its phases and its gates, the points where it
stops for a review. A change of appearance may need only your review at the
end; a new rule, a discussion before it is specified. The agent goes through
the other steps alone, committing each phase. At the end, you review the
specification change, try the software, and go through a short
retrospective. It still stops whenever it is unsure.

A large change is first written ahead, in `docs_future/<feature>/`, with
the outline of the increments that carry it out. Once you have approved
it, `dev43:supervise` can run those increments without you: it relays
only the decisions that need you, and at the end you try the software,
guided by its scenarios.

Projects set up with Dev43 3 are migrated by the agent at the first
session, with your review of the new specification.


## Examples

[docs/examples/](docs/examples/) holds two example specifications:

- [01_todo_cli](docs/examples/01_todo_cli/docs/README.md): a CLI, with
  a feature written ahead in `docs_future/tags/`
- [02_kanban_web](docs/examples/02_kanban_web/docs/README.md): a web
  app, with a page design


## License

MIT, see [LICENSE](LICENSE).
