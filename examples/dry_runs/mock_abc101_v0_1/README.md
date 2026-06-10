# Dry Run: Mock ABC-101 v0.1

## How This Run Was Performed

Input:

- `examples/mock_opportunity_brief.md`

Workflow:

- `workflows/initial_triage_workflow.md`

Outputs:

- `decision_memo.md`
- `requirement_check.csv`
- `risk_matrix.csv`
- `question_log.csv`
- `source_register.csv`

## Review Checklist

- Did the memo make one clear recommendation?
- Did the gap review compare the package against evidence that should normally be available for the asset's current phase?
- Did each critical gap identify the unmet requirement and the specific company request?
- Did it avoid treating company summaries as primary evidence?
- Did every material claim have a source, assumption, inference, or open question label?
- Did every high-severity risk have a next action?
- Did every critical gap become a document request or follow-up question?

## Result

The run recommends `Request More Data`, mainly because the current package is summary-heavy and lacks the primary documents needed to verify clinical, CMC, and regulatory claims.
