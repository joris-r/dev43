# Dev-4-3 plugin feedback

Feedback from a test run of the plugin on this project (a didactic
kanban web app), gathered at the Integration retrospective of the first
increment, `create-and-view`, on 2026-10-20.

## 1. Spec notes: record spec updates during later phases (from the human)

### Observation

During Implementation the agent added a `created_at` field to the
models: a technical, non-functional field absent from the data model.
The human saw it in the review and approved it. The process worked,
but there was no formal place to note that the specification needed
updating. The change page is frozen after Specification, and an
Amendment requires new tests, which this did not need. The agent fell
back on its private memory and the commit message, neither of which
the Integration skill reads.

### Proposal

A `## Spec notes` section in `spec/STATE.md`, to be filled by the agent
or the human in any phase after Specification, and consumed by
Integration.

- Each note is one line: what the specification should gain or change,
  e.g. `- Data model: Board, Column, Card have a created_at, not exposed
  by the API.`
- At Integration, each note is either:
  - merged into `spec/main/`, marked "(not tested)" if it states
    behavior that no test checks (distinct from "(not testable)");
  - or, if it needs new tests or changes behavior, turned into the
    scope of a later increment instead of being merged.
- Integration then empties the section.

### Changes needed in the plugin

- `templates/STATE.md`: add an empty `## Spec notes` section after
  `## Scope of the current increment`.
- `templates/CLAUDE.md`:
  - under "State and gates" or "Specification": "A needed change to the
    specification found after the Specification phase is not written
    in the change page: add it as a one-line note under `## Spec notes`
    in STATE, and mention it in your hand-over."
  - under "Specification": define the "(not tested)" marker next to
    "(not testable)", and the check that every "(not tested)" item was
    approved by the human.
- Tests and Implementation skills: in Production, tell the agent to
  record spec notes rather than tagging or silently deviating, when
  the deviation is approved or obviously harmless.
- Integration skill:
  - Production: "Process each note under `## Spec notes` in STATE:
    merge it into `spec/main/` (marked "(not tested)" where it applies),
    or, if it needs tests, propose it as a later increment. Then empty
    the section."
  - Exploration: review the spec notes with the human first, deciding
    for each one between merging it and scheduling it.
  - Verification checks: "`## Spec notes` in STATE is empty."
- `init` skill: nothing beyond the new STATE template.

### Applied in this project

The `created_at` note was merged by hand into `spec/main/data-model.md`
and marked "(not tested)". `CLAUDE.md` and `STATE.md` were left as
generated, at the human's request.

## 2. Tests that already pass before implementation (agent observation, not discussed with the human)

The Tests phase checks that new tests "fail for the right reason", but
says nothing about tests that pass before any implementation exists.
Some are legitimate, such as negative checks ("does not show X") and
404 tests on routes that do not exist yet. Others pass vacuously: a
loop over buttons that asserts each has no text passes when there are
no buttons. The agent caught one such test only by chance.

Proposal for the Tests skill: in Production, list the new tests that
pass before implementation and check that each one is a legitimate
negative check, not a vacuous one. In the hand-over, name them with
one line each.

## 3. Validate tests against a throwaway implementation (agent observation, not discussed with the human)

Tests become read-only at Implementation, so a test that cannot be
satisfied, or that over-constrains the code, costs a return to Tests.
In this run, the agent wrote a quick throwaway frontend implementation
in a scratch folder outside the repo and ran the new suite against it.
All tests passed, confirming the suite could be met as written. The
trickier tests included focus handling, Enter then blur sending exactly
one request, and finding the right column's button.

Proposal for the Tests skill: suggest, for non-trivial suites, a
throwaway implementation outside the repository to confirm the tests
can pass, deleted afterwards and never committed.

## 4. Commit subject format (from the human)

The `dev43:` prefix in commit subjects is noise, and the em dash `—`
is undesirable (hard to type, and odd in a one-line log). The human
prefers the increment in brackets, then the phase:

```
[create-and-view] Tests
[create-and-view] Implementation (return)
[create-and-view] Amendment
```

Changes needed in the plugin, wherever the format appears:

- `templates/CLAUDE.md`, section "Git": `[<increment>] <phase>`.
- The exit sections of every phase skill, and the Amendment of the
  Implementation skill.
- `init` skill: a subject for the init commit in the same style, e.g.
  `[init] Dev-4-3 setup`.
