---
name: clinical-evidence-review
description: Use when reviewing clinical study evidence, efficacy, safety, endpoints, populations, comparators, durability, study quality, benefit-risk, or whether clinical data support a claimed product profile or next development step.
---

# Clinical Evidence Review Skill

## Use When

Assessing whether available human clinical evidence supports the claimed product profile, development plan, and diligence recommendation.

## Review Method

1. Identify each completed and ongoing clinical study by phase, design, population, dose, comparator, geography, and status.
2. Separate primary evidence from summaries, selected charts, abstracts, posters, and company claims.
3. Review study quality: randomization, blinding, control, sample size, baseline balance, follow-up, discontinuations, protocol deviations, and data completeness.
4. Assess efficacy against prespecified endpoints, clinically meaningful thresholds, comparator relevance, durability, subgroup consistency, and standard of care.
5. Assess safety by AE profile, serious AEs, discontinuations, deaths, AESIs, dose relationship, exposure duration, class risks, and monitorability.
6. Identify whether clinical evidence supports the claimed target product profile, proposed patient population, next study, and valuation assumptions.
7. Convert unresolved issues into stage-specific document requests and expert review questions.

## Output Fields

- Clinical claim
- Study or evidence source
- Evidence strength: high / medium / low / not assessable
- Supportive findings
- Limiting findings
- Safety concerns
- Decision implication
- Required follow-up

## Clinical Evidence Rating

- `High`: Supported by primary clinical documents, appropriate design, clinically meaningful endpoints, consistent results, and adequate safety characterization.
- `Medium`: Directionally supportive but limited by sample size, follow-up, comparator, endpoint maturity, or incomplete primary documents.
- `Low`: Based mainly on summaries, selected charts, exploratory analyses, weak design, limited safety exposure, or unverified claims.
- `Not assessable`: Required clinical source documents or key analyses are missing.

## References

- Read `references/stage_requirements.md` when judging whether the clinical package is appropriate for Phase 1, Phase 2, Phase 3, registration, or commercial diligence.
- Read `references/red_flags_and_scoring.md` when writing the workstream conclusion, rating clinical evidence strength, or drafting specific clinical document requests.

## Quality Boundary

Do not treat a company-reported clinical signal as verified unless primary clinical documents support it. Do not collapse statistical robustness, dose rationale, regulatory acceptability, or commercial differentiation into the clinical evidence conclusion; route those to the relevant sub-agent when material.
