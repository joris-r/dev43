---
description: Set up Dev43 in the current project (CLAUDE.md, docs/ and docs_future/)
allowed-tools: Bash, Read, Write, Edit, Skill
---

Set up the Dev43 process in the current project. Templates are in
`${CLAUDE_PLUGIN_ROOT}/templates/`.

1. If a commit records the Dev43 state
   (`git log -1 --grep='^Dev43-Next: '`), stop: Dev43 is already set
   up. Show the current state and do nothing else.
2. Look for source code in the project, and tell the human whether you
   found any: it sets the mode (steps 6 and 7).
3. If the project is not a git repository, run `git init`; the
   permission prompt is the human's approval, do not ask separately.
   Dev43 relies on git; do not go on without it.
4. `CLAUDE.md`:
   - absent → copy the template;
   - present → append the template's lines, unchanged, after showing
     them to the human. The Dev43 rules stay in the `dev43:core` skill,
     never in `CLAUDE.md`.
5. Create `docs/` (with a `.gitkeep` file), and
   `docs_future/BACKLOG.md` holding only the title `# Backlog`. If a
   `docs/` folder already holds documents the process does not own,
   ask the human where the specification goes before going on.
6. Stage and commit only the files you created or changed, as
   `[init] Dev43 setup`, so that later phases can diff against it. End
   the message with the state trailers (see `dev43:core`, State):
   `Dev43:` the `version` in
   `${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json`,
   `Dev43-Specification:` `complete` without source code, `partial`
   with it, and `Dev43-Next: Pause`.
7. List what you created, then load `dev43:planning` and propose the
   plan of the first increment, which frames the project (see the
   `dev43:specification` skill, framing): shape `full` without source
   code, `specify-existing` with it, and the Exploration and
   Verification of Specification as gates.
