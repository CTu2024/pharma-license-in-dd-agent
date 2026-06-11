# Pharma License-In Due Diligence Agent

An open, modular agent workflow system for pharma license-in due diligence.

This repository provides agent charters, sub-agent roles, reusable skills, workflow instructions, templates, and mock dry runs for structured pharmaceutical business development diligence. It is designed to help teams turn a license-in opportunity package into source-backed workstream reports, risk matrices, follow-up questions, and an integrated decision memo.

## What This Is

This is a reusable diligence operating model. It helps an AI agent or human team:

- route diligence work across specialist sub-agents
- compare provided materials against stage-specific evidence requirements
- separate facts, assumptions, inferences, and open questions
- produce discipline-level workstream analysis reports
- integrate risks across clinical, CMC, regulatory, IP, market access, valuation, and deal structure
- generate precise company follow-up requests
- produce a decision-ready executive memo

## What This Is Not

This repository does not provide medical, legal, regulatory, financial, tax, investment, or professional advice. It is a workflow and template system. Outputs should be reviewed by qualified experts before being used in real transaction decisions.

See [DISCLAIMER.md](DISCLAIMER.md).

## Current Scope

The first version focuses on early-to-mid diligence triage for a pharma license-in opportunity.

Typical inputs:

- opportunity brief
- data room document index
- target or product overview
- clinical summary or study report excerpt
- CMC, regulatory, quality, or development summary
- patent, contract, pricing, forecast, or deal-term summary when available

Typical outputs:

- executive decision memo
- discipline-level workstream analysis reports
- stage-specific requirement check
- integrated risk matrix
- missing information log
- seller follow-up question log
- source register

## Repository Map

- [agents/](agents/README.md): Primary agent and specialist sub-agent charters.
- [skills/](skills/README.md): Shared and specialist skill instructions.
- [SKILL_COVERAGE.md](SKILL_COVERAGE.md): Sub-agent to specialist skill coverage matrix.
- [workflows/](workflows/initial_triage_workflow.md): End-to-end diligence workflow.
- [templates/](templates/): Standard memo, workstream report, risk, question, requirement, and source templates.
- [examples/](examples/): Mock opportunity packages and dry runs.
- [evals/](evals/test_cases.md): Lightweight cases for testing output quality.
- [ROADMAP.md](ROADMAP.md): Planned expansion path.

## Architecture

The operating model has three layers:

1. **Primary Diligence Agent**
   - Owns the integrated recommendation.
   - Routes workstreams.
   - Consolidates discipline outputs.

2. **Sub-Agents**
   - Own discipline-level judgments.
   - Produce workstream analysis reports.
   - Refuse conclusions outside their scope.

3. **Skills**
   - Shared skills enforce evidence traceability, stage-aware gap review, risk writing, and diligence question drafting.
   - Specialist skills guide discipline-specific analysis such as biostatistics, regulatory precedent, IP triage, market access, pricing, valuation, and deal structure.

## Quick Start

Review the main workflow:

[workflows/initial_triage_workflow.md](workflows/initial_triage_workflow.md)

Then inspect the richer mock dry run:

[examples/dry_runs/mock_xyz204_v0_2/README.md](examples/dry_runs/mock_xyz204_v0_2/README.md)

Key outputs from that dry run:

- [decision_memo.md](examples/dry_runs/mock_xyz204_v0_2/decision_memo.md)
- [workstream_reports/](examples/dry_runs/mock_xyz204_v0_2/workstream_reports/)
- [requirement_check.csv](examples/dry_runs/mock_xyz204_v0_2/requirement_check.csv)
- [risk_matrix.csv](examples/dry_runs/mock_xyz204_v0_2/risk_matrix.csv)
- [question_log.csv](examples/dry_runs/mock_xyz204_v0_2/question_log.csv)
- [source_register.csv](examples/dry_runs/mock_xyz204_v0_2/source_register.csv)

## How To Run A Dry Run

1. Choose an input package from `examples/` or create a sanitized opportunity brief.
2. Use `workflows/initial_triage_workflow.md`.
3. Activate only the sub-agents relevant to the asset and decision question.
4. Apply the four shared skills in every run:
   - Evidence Traceability
   - Data Room Gap Review
   - Risk Matrix Writing
   - Diligence Question Drafting
5. Add specialist skills where needed.
6. Produce workstream reports before writing the integrated decision memo.
7. Review the output against the checklist in the dry-run README.

## Recommendation Labels

The primary agent should choose one integrated recommendation:

- `Pursue`
- `Pause`
- `Renegotiate`
- `Reject`
- `Request More Data`

Every recommendation should state the rationale, key assumptions, conditions that would change the recommendation, and human expert escalations.

## Development Status

This is an early scaffold intended for iteration. The current repo is useful for structured thinking, mock dry runs, and prompt/workflow development. It is not yet a production application or automated diligence platform.

## Contributing

Contributions are welcome. Good contributions usually improve one of four things:

- sharper sub-agent boundaries
- better specialist skill instructions
- more realistic mock diligence cases
- stronger evaluation criteria

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).
