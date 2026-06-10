# Dry Run: Mock XYZ-204 v0.2

## Purpose

This dry run tests the expanded agent system on a broader Phase 2 regional license-in case.

## Input

- `examples/mock_opportunity_xyz204.md`

## Agents Expected To Activate

- Primary Diligence Agent
- Clinical Evidence Sub-agent
- Biostatistics Sub-agent
- CMC / Regulatory Readiness Sub-agent
- Regulatory Pathway Sub-agent
- Competitive Landscape Sub-agent
- Market Access / HEOR Sub-agent
- Pricing Sub-agent
- IP Triage Sub-agent
- Legal And Contract Sub-agent
- Financial Valuation Sub-agent
- Deal Structure Sub-agent

## Skills Expected To Activate

Shared skills:

- Evidence Traceability
- Data Room Gap Review
- Risk Matrix Writing
- Diligence Question Drafting

Specialist skills:

- Biostatistical Robustness
- Regulatory Precedent Analysis
- Market Access / HEOR Gap
- Pricing Analog Review
- IP Triage Review
- Contract Issue Spotting
- rNPV Assumption Review
- Deal Structure Review

## Outputs

- `decision_memo.md`
- `workstream_reports/`
- `requirement_check.csv`
- `risk_matrix.csv`
- `question_log.csv`
- `source_register.csv`

## Workstream Reports

- `workstream_reports/clinical_evidence_report.md`
- `workstream_reports/biostatistics_report.md`
- `workstream_reports/cmc_regulatory_readiness_report.md`
- `workstream_reports/regulatory_pathway_report.md`
- `workstream_reports/ip_legal_report.md`
- `workstream_reports/market_access_pricing_report.md`
- `workstream_reports/valuation_deal_structure_report.md`

## Review Checklist

- Did the output distinguish promising clinical signal from incomplete evidence?
- Did each activated discipline produce its own conclusion, risks, gaps, assumptions, and escalation view?
- Did the requirement check reflect Phase 2-to-Phase 3 expectations?
- Did CMC scale-up and stability gaps affect timeline and economics?
- Did IP and contract gaps prevent clean term-sheet movement?
- Did pricing/access assumptions flow into valuation and deal-structure implications?
- Did the recommendation integrate tradeoffs rather than simply list risks?
