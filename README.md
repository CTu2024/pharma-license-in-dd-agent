# Pharma License-In Due Diligence Agent

An open, modular operating model for pharma license-in scouting and due diligence.

The repository supports two independent operational modes:

1. **Scouting** — evaluate public or explicitly non-confidential information, recommend the next BD step, and end the engagement.
2. **Primary Diligence** — evaluate confidential, primary, data-room, or discipline-level material, coordinate specialist workstreams, produce an integrated recommendation, and end the engagement.

A human-controlled CDA and transaction process may occur between the modes, but the system does not execute that process or transition automatically.

## What This Is

This repository provides agent charters, reusable skills, engagement workflows, templates, and sanitized examples for structured pharmaceutical business-development review. It helps an AI agent or human team:

- screen early opportunities from non-confidential material;
- distinguish scouting hypotheses from diligence conclusions;
- register and trace confidential diligence sources;
- compare a package with stage-appropriate evidence requirements;
- route decision-material specialist workstreams;
- integrate risks, gaps, questions, and workstream conclusions; and
- produce a decision-ready scouting or diligence recommendation.

## What This Is Not

This repository does not provide medical, legal, regulatory, financial, tax, investment, or other professional advice. It does not sign or approve CDAs, authorize transactions, or automate human governance. Outputs require review by accountable qualified experts.

See [DISCLAIMER.md](DISCLAIMER.md).

## Choose One Mode

| User request and supplied material | Mode | Owner | Engagement output |
|---|---|---|---|
| Public or explicitly non-confidential material; decide whether the opportunity merits another BD step | Scouting | [Scouting Triage Agent](agents/scouting_triage_agent.md) | Scouting memo, scorecard, and one next-step recommendation |
| Confidential, primary, data-room, or discipline-level material; perform diligence, assess gaps, or integrate workstreams | Primary Diligence | [Primary Diligence Agent](agents/primary_diligence_agent.md) | Workstream reports, source register, risk matrix, questions, and integrated decision memo |
| Confidentiality status or requested decision is unclear | Neither yet | User clarification required | Clarified mode and permitted source scope |

### Mode 1: Scouting

Entry:

- public or explicitly non-confidential information; and
- a request to choose the next BD step.

Recommendations:

- `Pass`
- `Monitor`
- `Intro Call`
- `Request Non-Confidential Follow-Up`
- `Recommend CDA / Confidential Diligence`

Every recommendation ends the Scouting engagement. If the recommendation concerns CDA, an authorized human decides what happens next. The system does not activate Primary Diligence automatically.

Start with [workflows/scouting_triage_workflow.md](workflows/scouting_triage_workflow.md).

### Mode 2: Primary Diligence

Entry:

- an explicit diligence request; and
- confidential, primary, data-room, or discipline-level material.

Recommendations:

- `Pursue`
- `Pause`
- `Renegotiate`
- `Reject`
- `Request More Data`

A previous scouting review is optional. A sparse confidential package remains a Primary Diligence intake and gap-review problem; it does not revert to Scouting.

Start with [workflows/primary_diligence_workflow.md](workflows/primary_diligence_workflow.md).

## Architecture

```text
Agent     = owns one engagement and its authority boundaries
Skill     = supplies a reusable analytical method
Workflow  = defines entry, sequence, exit, and handoff boundaries
Template  = defines the deliverable structure
```

- [agents/](agents/README.md): Scouting, Primary Diligence, and specialist agent charters.
- [skills/](skills/README.md): Shared and specialist analytical methods.
- [SKILL_COVERAGE.md](SKILL_COVERAGE.md): Agent-to-skill coverage matrix.
- [workflows/](workflows/): The two independent engagement workflows.
- [templates/](templates/): Standard scouting, workstream, risk, question, source, and decision outputs.
- [examples/](examples/): Sanitized prompts, mock packages, and dry runs.
- [share/scouting_triage_chat/](share/scouting_triage_chat/): Portable Scouting package for chat-only LLM users.
- [evals/](evals/test_cases.md): Lightweight behavior and boundary cases.

## Scouting Quick Start

1. Confirm all supplied material is public or explicitly non-confidential.
2. Use `agents/scouting_triage_agent.md` and `skills/scouting_triage/SKILL.md`.
3. Follow `workflows/scouting_triage_workflow.md`.
4. Produce `templates/scouting_memo.md` and `templates/scouting_scorecard.csv`.
5. Present one recommendation and end the engagement.

For a chat-only user, use [SCOUTING_TRIAGE_CHAT_PROMPT.md](share/scouting_triage_chat/SCOUTING_TRIAGE_CHAT_PROMPT.md).

## Primary Diligence Quick Start

1. Confirm the user explicitly requests diligence and is authorized to provide the supplied confidential or primary material.
2. Use `agents/primary_diligence_agent.md`.
3. Follow `workflows/primary_diligence_workflow.md`.
4. Activate only decision-material specialist workstreams.
5. Apply Evidence Traceability, Data Room Gap Review, Risk Matrix Writing, and Diligence Question Drafting.
6. Produce workstream reports before integration unless explicitly waived.
7. Deliver one integrated recommendation and end the engagement.

See the richer mock run at [examples/dry_runs/mock_xyz204_v0_2/README.md](examples/dry_runs/mock_xyz204_v0_2/README.md).

## Development Status

This is an early scaffold for structured thinking, sanitized dry runs, and prompt/workflow development. It is not a production application or an automated diligence platform.

## Contributing

Contributions should improve agent boundaries, analytical skills, sanitized examples, or evaluation criteria without adding confidential or proprietary information. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).
