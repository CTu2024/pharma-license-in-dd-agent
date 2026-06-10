# Evaluation Test Cases

Use these cases to test whether the agent system produces disciplined diligence outputs.

## Case 1: Summary-Only Package

Input:

- Investor deck
- Phase 1b synopsis
- CMC summary
- Company-written regulatory interaction summary

Expected behavior:

- Recommendation should usually be `Request More Data` or `Pause`.
- Agent should not treat company summaries as equivalent to primary documents.
- Agent should request CSR, protocol, SAP, original agency correspondence, and CMC validation materials.

## Case 2: Strong Clinical Signal, Weak CMC

Input:

- Full clinical package with promising efficacy
- Limited manufacturing history
- No long-term stability data
- Unclear scale-up plan

Expected behavior:

- Agent should preserve the positive clinical view while escalating CMC risk.
- Recommendation may be `Pursue` with conditions or `Renegotiate`, depending on severity.
- Risk matrix should separate clinical confidence from manufacturing readiness.

## Case 3: Mechanism Plausible But Human Validation Weak

Input:

- Strong animal data
- Limited human target validation
- Early biomarker changes
- No clear clinical endpoint movement

Expected behavior:

- Agent should label target biology confidence as limited.
- Agent should avoid overstating proof of mechanism.
- Follow-up questions should request translational evidence and biomarker assay validation.

