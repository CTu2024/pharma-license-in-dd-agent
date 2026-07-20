# Primary Diligence Engagement Workflow

## Entry

Use this workflow when the user explicitly requests diligence and supplies confidential, primary, data-room, or discipline-level material requiring source registration, package-gap assessment, specialist review, or integration.

Do not require a prior scouting review. A CDA or prior scouting decision may explain how the opportunity arrived, but the operational trigger is the user's diligence request plus substantive diligence material.

If the supplied confidential package is sparse, continue with intake and gap assessment; do not send the engagement back to Scouting.

## Owner

Use `agents/primary_diligence_agent.md` with the relevant shared and specialist skills.

## Process

1. **Set decision context**
   - Capture the asset, indication, modality, stage, geography, licensor, transaction scope, next decision, and deadline.
   - Define the stage-appropriate evidence standard for that decision.

2. **Register sources**
   - Assign a source ID to every supplied item.
   - Record document type, date, owner, confidentiality, source quality, and limitations.
   - Treat any prior scouting memo as context unless its underlying sources are available and traceable.

3. **Assess package completeness**
   - Compare supplied evidence with stage-appropriate requirements.
   - Mark each requirement `Met`, `Partially Met`, `Not Met`, or `Not Assessable`.
   - Convert material gaps into prioritized document requests or questions.

4. **Route material workstreams**
   - Activate only specialist workstreams that can change the diligence decision.
   - Record why each workstream is activated or waived.

5. **Produce workstream reports**
   - Use `templates/workstream_report.md` for each activated discipline.
   - Require a conclusion, evidence reviewed, requirement check, risks, gaps, assumptions, and human escalation needs.
   - Use one conclusion: `Supportive`, `Supportive With Conditions`, `Mixed`, `Not Supportive`, or `Not Assessable`.

6. **Integrate**
   - Merge workstream findings into the risk matrix and decision memo.
   - Identify dependencies, conflicting conclusions, deal-critical risks, and unresolved decision issues.
   - Do not substitute integrated prose for missing workstream analysis unless the workstream is explicitly waived.

7. **Recommend and end**
   - Choose exactly one: `Pursue`, `Pause`, `Renegotiate`, `Reject`, or `Request More Data`.
   - State the rationale, confidence, assumptions, human escalations, and conditions that would change the recommendation.
   - Deliver the outputs and end the engagement.

## Outputs

- `templates/decision_memo.md`
- `templates/workstream_report.md` for each activated discipline
- Stage-appropriate requirement check
- `templates/risk_matrix.csv`
- `templates/question_log.csv`
- `templates/source_register.csv`

## Quality Gate

- No material claim lacks a source, assumption label, or open-question label.
- Critical gaps are tied to stage-specific requirements.
- Every high-severity risk has a mitigation, owner, and next action.
- Every critical gap becomes a question or document request.
- Activated workstream reports exist or are explicitly waived before integration.
- The recommendation is understandable to a cross-functional governance group.
