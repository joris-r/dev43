# Security check

- [security] is an agent check of Implementation and of the Direct
  phase, on the code changed by the increment, in the same sub-agent
  as the other checks. Soundness covers the specification.
- It flags an entry point, boundary, asset or dependency that
  `security.md` does not cover, and the common flaws of the stack
  (injection, secrets in code or logs, path traversal, unsafe
  deserialization, weak cryptography or randomness, data shown to an
  actor who may not see it). `[general]` covers the mitigations.
- A flaw is fixed or disputed, as any finding. Uncovered surface is
  marked; at the final review the human returns to Specification, or
  accepts it with a backlog entry to update `security.md`.
- The dependency audit is a tool of the stack, in the test and
  quality policy of `technical.md`; framing adds it when the software
  is exposed.
