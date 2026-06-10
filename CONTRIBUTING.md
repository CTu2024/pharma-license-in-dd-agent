# Contributing

Thanks for helping improve this pharma license-in diligence agent system.

## Contribution Principles

Good contributions should make the workflow more useful, more evidence-disciplined, or easier to audit.

Prefer changes that:

- clarify agent or sub-agent ownership
- improve source traceability
- make stage-specific requirements more precise
- improve risk and gap writing
- add realistic mock cases
- strengthen evaluation criteria
- reduce unsupported or overconfident conclusions

## Repository Conventions

Agent charters live in `agents/`.

Skill instructions live in `skills/<skill_name>/SKILL.md` and should include:

- YAML frontmatter with `name` and `description`
- when to use the skill
- a concise review method
- expected output fields
- quality or refusal boundaries

Templates live in `templates/`.

Mock opportunity inputs and dry-run outputs live in `examples/`.

Evaluation cases live in `evals/`.

## Adding A Sub-Agent

When adding a sub-agent:

1. Create `agents/<name>_subagent.md`.
2. Define outcome owned, review questions, inputs, outputs, and refusal boundaries.
3. Add it to `agents/README.md`.
4. Add routing guidance to `agents/primary_diligence_agent.md`.
5. Update the workflow if the sub-agent changes the operating sequence.

## Adding A Skill

When adding a skill:

1. Create `skills/<skill_name>/SKILL.md`.
2. Keep the body concise and operational.
3. Add the skill to `skills/README.md`.
4. Map it to relevant sub-agents in `agents/primary_diligence_agent.md` if appropriate.
5. Add or update a mock dry run that demonstrates the skill.

## Adding A Dry Run

When adding a dry run:

1. Create a synthetic or sanitized input in `examples/`.
2. Create `examples/dry_runs/<case_name>/`.
3. Include at least:
   - `README.md`
   - `decision_memo.md`
   - `requirement_check.csv`
   - `risk_matrix.csv`
   - `question_log.csv`
   - `source_register.csv`
4. Add `workstream_reports/` when more than one discipline is activated.
5. Avoid confidential, proprietary, patient-level, or non-public information.

## Safety And Confidentiality

Do not contribute confidential data, patient data, proprietary company materials, unpublished transaction materials, or non-public regulatory correspondence.

Synthetic examples are preferred.

