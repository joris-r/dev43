# Security in the process

- Framing: the security context, i.e. the exposure, the sensitive
  data, the legal constraints. It sets the depth of the threat model.
- Exploration of every increment: the agent compares the change with
  `security.md`; a new asset, entry point or boundary brings proposed
  threats, and the human rules on each: mitigated or accepted. The
  question states what an attacker gains, how likely it is, and what
  the mitigation costs, in plain words; `security.md` keeps only the
  decision.
- Tests: the mitigations are tested, and abuse scenarios test them
  end to end.
- Soundness: every threat has an existing mitigation or is accepted;
  every operation reachable across a boundary states who may run it,
  in its cases or by a General rule.
- Security check at Verification: a sub-agent reviews the diff
  against `security.md` and the common flaws (injection, secrets).
