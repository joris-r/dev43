---
description: Set up Dev-4-3 in the current project (CLAUDE.md, spec/ tree, STATE.md)
argument-hint: "[new|existing]"
allowed-tools: Bash, Read, Write, Edit, Skill
---

Set up the Dev-4-3 process in the current project. Templates are in
`${CLAUDE_PLUGIN_ROOT}/templates/`.

1. If `spec/STATE.md` already exists, stop: Dev-4-3 is already set up.
   Show the current state and do nothing else.
2. Decide the starting phase. Use `$ARGUMENTS` if it is `new` or
   `existing`. Otherwise look for source code in the project and propose
   one: no code → Initial Framing; code → Retro-Specification. Ask the
   human to confirm.
3. `CLAUDE.md`:
   - absent → copy the template;
   - present → never overwrite it. Show the human a merge proposal
     (template rules appended under a `# Dev-4-3 rules` section) and apply
     it only on approval.
4. Create `spec/main/1-functional/`, `spec/main/2-interfaces/`,
   `spec/main/3-technical/` and `spec/changes/` (with `.gitkeep` files).
5. Copy the STATE template to `spec/STATE.md` and fill it in:
   increment `framing` or `retro`, the confirmed phase, step
   Exploration.
6. List what you created, then start Exploration with the
   `dev43:initial-framing` or `dev43:retro-specification` skill.

Do not commit.
