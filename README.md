# Dev43

A specification-driven development process for humans and LLM agents,
packaged as a Claude Code plugin. The process itself is described in
[process_principles.md](docs/process_principles.md), and the
released versions in [CHANGELOG.md](CHANGELOG.md).

## Why Dev43

The hard part of working with AI agents is trusting what they produce.
Dev43 keeps the agent inside a disciplined process: specification first,
then tests, then code.

The specification is made of living documents and comes with traceability
tags (as readable keywords). The test suite is produced before the code
and traces the requirements. Agent skills check soundness and
completeness. Invariants on the data model are checked against the
effects of the operations.

The approach comes from safety-critical software processes, adapted to
agentic development. The internal correctness of the specification is
inspired by the formal B method.

Used in [Gilda](https://github.com/joris-r/gilda), a web service for
association scheduling (Python, Litestar, Datastar and PostgreSQL).

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
each commit message. So never clear the agent's context while work is
uncommitted.

You review the specification and try the software; agents check the
tests and the code.

The first increment sets up the stack with a trivial feature, such as a
health check or "hello world". On existing code, it describes the existing
stack instead.

Then you are in Pause: ask for something and the agent starts
an increment, which can go through these four phases:

1. Planning
2. Specification
3. (writing of) Tests
4. Implementation

Work in each phase happens in these three steps:

1. **Exploration**: you discuss with the agent. When you're ready, say "next".
2. **Production**: the agent does the work in one go.
3. **Verification**: you review the produced work. The agent may place a
   mark where it needs a human decision, which you must rule on.

You won't always go through all the phases and steps, only those needed by
the complexity of the increment. The gates and shape of the increment are
decided during planning.

A large change can be first written ahead, in `docs_future/<feature>/`, with
the outline of the increments that carry it out. Once you have approved
it, `dev43:supervise` can run those increments without you: it relays
only the decisions that need you.

## Examples

[docs/examples/](docs/examples/) holds two simple example specifications:

- [01_todo_cli](docs/examples/01_todo_cli/docs/README.md): a CLI, with
  a feature written ahead in `docs_future/tags/`
- [02_kanban_web](docs/examples/02_kanban_web/docs/README.md): a web
  app, with a page design
- See [Gilda](https://github.com/joris-r/gilda) for a bigger project

## License

MIT, see [LICENSE](LICENSE).
