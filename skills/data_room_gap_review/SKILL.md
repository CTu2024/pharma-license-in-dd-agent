---
name: data-room-gap-review
description: Use when reviewing pharma license-in data room completeness, missing documents, inconsistent claims, outdated materials, or follow-up information requests.
---

# Data Room Gap Review Skill

Use this skill to turn a document package or data room index into a stage-aware gap log.

## Review Steps

1. Identify the decision context: asset stage, modality, indication, geography, and next milestone.
2. Define what evidence should normally be available at that stage and for that next milestone.
3. List available company-provided documents by workstream.
4. Compare provided materials against the stage-specific requirement set.
5. Flag missing, outdated, inconsistent, draft, redacted, summary-only, or non-primary materials.
6. Convert each gap into a specific company requirement and document request.

## Stage-Aware Requirement Check

Before writing gaps, create a requirement check table.

Required fields:

- Requirement ID
- Stage or milestone
- Workstream
- Expected evidence or document
- Company-provided evidence
- Status: `Met / Partially met / Not met / Not assessable`
- Gap consequence
- Specific company request

## Starter Expected Evidence By Stage

Use this starter checklist as a default, then adjust for modality, indication, geography, and transaction question.

### Preclinical / IND-Enabling

- Target validation and disease rationale package.
- Nonclinical pharmacology and proof-of-concept package.
- DMPK / ADME data.
- Exploratory and GLP toxicology plan or reports.
- Candidate selection rationale.
- CMC process description, analytical methods, formulation, and stability plan.
- IND-enabling development plan and regulatory interaction history, if any.

### Phase 1 / Phase 1b

- Protocols, amendments, statistical analysis plans, and clinical study reports or synopses for completed studies.
- Safety tables, adverse event listings, dose escalation decisions, dose-limiting toxicity review, and exposure data.
- PK, PD, target engagement, biomarker, and dose rationale data.
- Investigator brochure and current development safety update, if available.
- CMC batch records or batch summary, specifications, analytical method status, formulation, and stability data supporting clinical supply.
- Regulatory correspondence, meeting minutes, briefing books, and agency written responses.

### Phase 2

- Full CSRs, protocols, SAPs, datasets or listings, and endpoint analyses for completed Phase 1 and Phase 2 studies.
- Benefit-risk summary by dose, population, subgroup, and endpoint.
- Exposure-response and dose selection rationale for Phase 3.
- Safety database summary, AESI review, discontinuation analysis, and class-risk assessment.
- CMC process history, comparability, analytical validation status, stability, control strategy, and scale-up plan.
- Regulatory advice on Phase 3 design, endpoints, patient population, and filing path.
- Competitive landscape and target product profile assumptions.

### Phase 3 / Registration-Ready

- Full pivotal study package, SAPs, datasets or listings, integrated efficacy and safety summaries.
- Label strategy, benefit-risk assessment, and regulatory filing plan.
- Complete CMC control strategy, validation plan, stability package, specifications, comparability, and inspection readiness evidence.
- Pediatric, special population, DDI, renal/hepatic impairment, and other required clinical pharmacology plans or results.
- Market access evidence plan, HEOR package, and launch supply assumptions.

### Approved / Commercial

- Approval letters, labels, risk management plans, post-marketing commitments, and safety updates.
- Commercial supply, quality history, deviations, recalls, complaints, and inspection history.
- Real-world safety, effectiveness, access, pricing, and competitive performance.
- IP, contracts, licenses, encumbrances, and change-of-control implications.

## Gap Severity

- `Critical`: Could change pursue/reject decision or valuation materially.
- `Major`: Could affect deal terms, development plan, timeline, or risk mitigation.
- `Moderate`: Important for diligence completeness but unlikely alone to stop the deal.
- `Minor`: Useful cleanup or clarification.

## Output Fields

- Gap ID
- Workstream
- Stage or milestone requirement
- Missing or problematic item
- Company-provided evidence
- Requirement status
- Why it matters
- Severity
- Requested document or answer
- Owner
- Status
