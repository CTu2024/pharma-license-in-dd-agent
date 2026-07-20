# Initial Triage Workflow

## Purpose

Produce a source-backed first-pass diligence view for an early pharma license-in opportunity.

## Inputs

- Opportunity brief
- Data room document index
- Target or product overview
- Clinical summary if available
- CMC, quality, regulatory, or development summaries if available

## Steps

1. **Set context**
   - Capture asset name, modality, indication, stage, geography, licensor, and proposed deal scope.
   - Identify the next decision milestone.
   - Define the phase-specific diligence standard: what evidence should reasonably be available at the asset's current stage and before the next decision.

2. **Build source register**
   - Assign a source ID to every input.
   - Note document type, date, owner, and source quality.

3. **Build requirement check**
   - For each workstream, list stage-appropriate expected documents and evidence.
   - Record what the company actually provided.
   - Mark each requirement as met, partially met, not met, or not assessable.
   - Convert unmet requirements into specific company requests.

4. **Route workstreams**
   - Target Biology Sub-agent reviews mechanism and validation.
   - Clinical Evidence Sub-agent reviews clinical evidence and gaps.
   - CMC / Regulatory Readiness Sub-agent reviews CMC, quality, regulatory, and next-milestone readiness.
   - Regulatory Pathway Sub-agent reviews agency history, approval path, required studies, and regional considerations when regulatory risk is material.
   - IP Triage Sub-agent reviews patent, exclusivity, ownership, FTO, and encumbrance flags when transaction rights or exclusivity are material.
   - Financial Valuation Sub-agent reviews assumptions, scenarios, risk adjustment, and deal-term implications when valuation or negotiation decisions are in scope.
   - Competitive Landscape Sub-agent reviews standard of care, approved competitors, pipeline threats, and differentiation when commercial attractiveness is material.
   - DMPK / ADME Sub-agent reviews exposure, ADME, DDI, metabolism, clearance, and species translation when pharmacokinetics or translation risk is material.
   - Toxicology Sub-agent reviews tox package completeness, target organ findings, and safety margins when nonclinical safety is material.
   - Clinical Pharmacology Sub-agent reviews dose rationale, PK/PD, exposure-response, bridging, DDI, and special population evidence when dose or exposure risk is material.
   - Biostatistics Sub-agent reviews powering, endpoints, multiplicity, missing data, subgroup validity, and statistical robustness when evidence reliability is material.
   - Market Access / HEOR Sub-agent reviews payer evidence, HTA risk, outcomes evidence, and access barriers when reimbursement affects value.
   - Pricing Sub-agent reviews analogs, net price assumptions, regional pressure, and pricing sensitivity when price affects valuation.
   - Legal And Contract Sub-agent reviews rights, obligations, sublicensing, change-of-control, termination, and encumbrance constraints when transaction terms are material.
   - Deal Structure Sub-agent reviews license, option, co-development, milestone, royalty, and risk-sharing options when deal design is in scope.
   - Alliance Management Sub-agent reviews governance, decision rights, escalation, reporting, and operating model risks when partnership execution is material.
   - Integration / Transition Sub-agent reviews data, know-how, vendors, CMC, systems, people, and transfer readiness when post-deal handoff is material.

5. **Apply shared skills**
   - Use Evidence Traceability for every material claim.
   - Use Data Room Gap Review to compare provided materials against stage-specific requirements.
   - Use Risk Matrix Writing to standardize risks.
   - Use Diligence Question Drafting to create seller and internal questions.

6. **Produce workstream reports**
   - Each activated sub-agent produces a workstream analysis report using `templates/workstream_report.md`.
   - Each report must include a workstream conclusion, evidence reviewed, requirement check, risks, gaps, assumptions, and escalation needs.
   - Workstream conclusions must be one of: supportive, supportive with conditions, mixed, not supportive, or not assessable.
   - The primary agent may not write the integrated memo until activated workstream reports exist or are explicitly waived.

7. **Integrate**
   - Merge workstream outputs into an integrated risk matrix.
   - Identify cross-workstream dependencies.
   - Separate deal-critical risks from ordinary diligence work.
   - Resolve conflicting workstream conclusions or list them as unresolved decision issues.

8. **Recommend**
   - Choose one recommendation: pursue, pause, renegotiate, reject, or request more data.
   - State the rationale, key assumptions, and conditions for changing the recommendation.

## Standard Outputs

- `templates/decision_memo.md`
- `templates/workstream_report.md` for each activated discipline
- Requirement check table embedded in the decision memo or saved separately
- `templates/risk_matrix.csv`
- `templates/question_log.csv`
- `templates/source_register.csv`

## Quality Bar

- No material claim without a source, assumption label, or open question label.
- Critical gaps must be tied to stage-specific requirements, not generic missing-document observations.
- The integrated memo must summarize discipline conclusions; it must not replace discipline-level analysis reports.
- Every high-severity risk has a mitigation, owner, and next action.
- Every critical gap becomes a follow-up question or document request.
- The recommendation must be understandable to a cross-functional governance group.
