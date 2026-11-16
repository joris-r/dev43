# Changelog

Every released version of the Dev43 plugin, newest first. A major
version changes what a project following Dev43 looks like; the
versions under it refine the rules. The commit of each release holds
the details.

## 4: a closed specification, checked by agents

Impact: the specification moves from `spec/` to `docs/`, organized by
domain into model, operations, UI, design, contents and scenarios;
every statement carries a tag, every test cites paths. Agents check
each phase in a fresh context; the human reviews the specification.
Projects on Dev43 3 migrate with `dev43:migrate`.

### 4.7: agent checks before each exit commit, test levels

- 4.7.1 (2026-11-16): an increment of an outline that changes no
  specified behavior gives its shape and its work instead of
  sections, and [outline] checks it.
- 4.7.0 (2026-11-16): every phase runs its agent checks before its
  exit commit, and a gate is the human's review only; lessons and
  points for the human take one line and leave once used; the Tests
  phase finds the tests to update by the changed text too; a
  statement is tested once, at the cheapest level that observes it,
  and `technical.md` names the levels.

### 4.6: sent texts, migration between minor versions

- 4.6.0 (2026-11-15): a text an operation sends has its own section
  of `contents.md`, cited by its case; projects on an earlier minor
  version of Dev43 4 migrate with `dev43:migrate`; check.py reads
  Extends, the outline's citations and the French section names.

### 4.5: ordered cases and Then:

- 4.5.0 (2026-11-14): under `Cases:`, a numbered list means ordered
  cases; `Then:` holds the statements after given cases or after no
  refusal; `## General` applies before the cases.

### 4.4: contents and mockups

- 4.4.1 (2026-11-14): check.py reads tags on numbered items.
- 4.4.0 (2026-11-13): one subject per increment; `contents.md` holds
  the authored text; one mockup per UI element; tags in the project's
  language.

### 4.3: a closed specification

- 4.3.4 (2026-11-10): existing code, migrate and supervise follow the
  closed specification; an open case is stated as `unspecified`.
- 4.3.3 (2026-11-10): the Specification agent check runs before its
  exit commit, gate or not; [outline] check; planning covers stored
  data and its migration.
- 4.3.2 (2026-11-10): an agent checks that the code handles every
  state and input of each case, not only the values its tests use. An
  Amendment made during Implementation passes the Specification
  checks, soundness included.
- 4.3.1 (2026-11-10): what a test establishes, by kind of statement; a
  test checks nothing the specification leaves free.
- 4.3.0 (2026-11-10): the specification is closed: all the data, every
  input settled in every state, every outcome displayed. Inputs,
  Cases, Initial state, Trigger; soundness obligations [initial],
  [partition], [determined], [migration] and the coherence checks.

### 4.2: soundness

- 4.2.3 (2026-11-10): the model states what holds; how a value comes
  is an operation.
- 4.2.2 (2026-11-10): the final review comes before the last exit
  commit.
- 4.2.1 (2026-11-10): the CLAUDE.md template links the plugin
  repository.
- 4.2.0 (2026-11-10): `dev43:soundness`, after the proof obligations
  of the B method, in a fresh context.

### 4.1: fixes from the first migration

- 4.1.4 (2026-11-10): [placement] check; principles on checks and
  traceability.
- 4.1.3 (2026-11-10): the human reviews a change of behavior before
  tests and code build on it.
- 4.1.2 (2026-11-10): paths transliterate accents.
- 4.1.1 (2026-11-10): an agent check ends: a finding is fixed or
  disputed, and after three rounds the human decides.
- 4.1.0 (2026-11-09): fixes from the first migration; refusal messages
  specified only when `technical.md` says so.

### 4.0: docs/ layout and traceability

- 4.0.0 (2026-11-09): `docs/` layout and traceability, future
  specifications with outlines, marks, agent checks, the line of
  responsibility, supervised increments, `dev43:migrate`, check.py.
  Integration phase removed.

## 3: gates follow the impact

Impact: each increment starts with a plan from an impact analysis, which
sets its gates; the agent commits the other phases itself. The process
state lives in commit trailers, no longer in `spec/STATE.md`, and the
history is never rewritten.

- 3.0.0 (2026-11-02): `dev43:planning`; gates follow the impact;
  `Dev43-*` trailers; wip commits replace the stash; small changes
  edit `spec/main/` in place.

## 2: existing code

Impact: Dev43 applies to existing code, with a partial specification
that grows zone by zone, and the first increment frames the project
through a trivial feature instead of a separate Initial Framing.

- 2.1.0 (2026-11-02): the direct shape covers small code changes
  outside the specification; tests are found by entry point; the
  principles reduced to context and principles.
- 2.0.0 (2026-10-27): partial specification and the specify-existing
  shape; framed first increment.

## 1: the process as a plugin

Impact: the four phases, Exploration, Production and Verification,
traceability from rules to tests, and git as the record, packaged as
Claude Code skills and refined from test runs and project retros.

- 1.6.0 (2026-10-27): narrower dependency tags; retro notes file
  dropped; README for newcomers.
- 1.5.0 (2026-10-26): the refactoring shape becomes code-only.
- 1.4.0 (2026-10-25): the rules move from the project's CLAUDE.md to
  `dev43:core`; increment shapes and Pause; citations match names
  ignoring case; Integration test run dropped.
- 1.3.0 (2026-10-24): behavior rules are observable outcomes; folded
  gates; "going further" in the retrospective.
- 1.2.0 (2026-10-23): refactoring increments, retrospective, abandoned
  increments.
- 1.1.0 (2026-10-21): Next in STATE, stash on return, backlog, Idle;
  MIT license.
- 1.0.0 (2026-10-20): first release, renamed from Dev-4-3.
