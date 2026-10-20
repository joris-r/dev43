---
description: Set up Dev43 in the current project (CLAUDE.md, spec/ tree, STATE.md)
allowed-tools: Bash, Read, Write, Edit, Skill
---

Set up the Dev43 process in the current project. Templates are in
`${CLAUDE_PLUGIN_ROOT}/templates/`.

1. If `spec/STATE.md` already exists, stop: Dev43 is already set up.
   Show the current state and do nothing else.
2. Look for source code in the project. If there is any, stop: adopting
   Dev43 on existing code (Retro-Specification) is not supported yet.
   Tell the human and do nothing else.
3. If the project is not a git repository, run `git init`; the
   permission prompt is the human's approval, do not ask separately.
   Dev43 relies on git; do not go on without it.
4. `CLAUDE.md`:
   - absent → copy the template;
   - present → never overwrite it. Show the human a merge proposal
     (template rules appended under a `# Dev43 rules` section) and apply
     it only on approval.
5. Create `spec/main/` and `spec/changes/` (with `.gitkeep` files).
6. Copy the STATE template to `spec/STATE.md` and fill it in:
   increment `framing`, phase Initial Framing, step Exploration, and
   scope "Set the stack, conventions and a running skeleton. No feature
   is delivered."
7. Stage and commit only the files you created or changed, as
   `[init] Dev43 setup`, so that later phases can diff against it.
8. List what you created, then start Exploration with the
   `dev43:initial-framing` skill.
