# Scouting Engagement Workflow

## Entry

Use this workflow only when the user supplies public or explicitly non-confidential information and asks whether an early pharma license-in opportunity merits another BD step.

If confidentiality status is unclear, clarify it before reviewing the material.

## Owner

Use `agents/scouting_triage_agent.md` with `skills/scouting_triage/SKILL.md`.

## Process

1. Confirm the Scouting entry conditions and immediate BD decision.
2. Run the Scouting Triage skill against the supplied sources.
3. Obtain targeted specialist input only if a narrow question is essential to the scouting recommendation.
4. Produce `templates/scouting_memo.md` and `templates/scouting_scorecard.csv`.
5. Present exactly one recommendation and end the engagement.

## Exit

- `Pass` → close the opportunity unless a human later reopens it with new information.
- `Monitor` → record the reassessment trigger and timing; end the current engagement.
- `Intro Call` → provide the agenda and questions; end the current engagement.
- `Request Non-Confidential Follow-Up` → provide prioritized requests; end the current engagement.
- `Recommend CDA / Confidential Diligence` → present the recommendation for human decision; end the current engagement.

Do not execute a CDA, activate the Primary Diligence Agent, or continue automatically into confidential diligence.

## Later Diligence

If a CDA is subsequently executed and a user starts a new request with confidential, primary, data-room, or discipline-level material, use `workflows/primary_diligence_workflow.md`. That is a separate engagement, not the next step of this workflow.
