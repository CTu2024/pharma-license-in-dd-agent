from datetime import date
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf" / "quregenai_quantum_aidd_due_diligence_report.pdf"


def para(text, style):
    return Paragraph(text, style)


def bullets(items, style, bullet_type="bullet"):
    return ListFlowable(
        [ListItem(Paragraph(item, style), leftIndent=12) for item in items],
        bulletType=bullet_type,
        start="circle",
        leftIndent=16,
        bulletFontName="Helvetica",
        bulletFontSize=7,
        bulletOffsetY=1,
    )


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#667085"))
    canvas.drawString(doc.leftMargin, 0.45 * inch, "QureGenAI Quantum AIDD - diligence summary")
    canvas.drawRightString(A4[0] - doc.rightMargin, 0.45 * inch, f"Page {doc.page}")
    canvas.restoreState()


def styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "Title",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=24,
            leading=30,
            textColor=colors.HexColor("#101828"),
            spaceAfter=14,
        ),
        "subtitle": ParagraphStyle(
            "Subtitle",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=10.5,
            leading=15,
            textColor=colors.HexColor("#475467"),
            spaceAfter=16,
        ),
        "h1": ParagraphStyle(
            "H1",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=15,
            leading=19,
            textColor=colors.HexColor("#101828"),
            spaceBefore=12,
            spaceAfter=7,
        ),
        "h2": ParagraphStyle(
            "H2",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=11,
            leading=14,
            textColor=colors.HexColor("#344054"),
            spaceBefore=8,
            spaceAfter=5,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.2,
            leading=13.2,
            textColor=colors.HexColor("#344054"),
            spaceAfter=6,
        ),
        "small": ParagraphStyle(
            "Small",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=7.8,
            leading=10.5,
            textColor=colors.HexColor("#475467"),
            spaceAfter=4,
        ),
        "table_header": ParagraphStyle(
            "TableHeader",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=7.6,
            leading=9.2,
            textColor=colors.white,
        ),
        "table_cell": ParagraphStyle(
            "TableCell",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=7.4,
            leading=9.2,
            textColor=colors.HexColor("#344054"),
        ),
        "callout": ParagraphStyle(
            "Callout",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=10,
            leading=13,
            textColor=colors.HexColor("#101828"),
            backColor=colors.HexColor("#F2F4F7"),
            borderColor=colors.HexColor("#D0D5DD"),
            borderWidth=0.5,
            borderPadding=8,
            spaceBefore=6,
            spaceAfter=10,
        ),
        "right": ParagraphStyle(
            "Right",
            parent=base["BodyText"],
            alignment=TA_RIGHT,
            fontName="Helvetica",
            fontSize=8,
            leading=10,
            textColor=colors.HexColor("#667085"),
        ),
        "label": ParagraphStyle(
            "Label",
            parent=base["BodyText"],
            alignment=TA_LEFT,
            fontName="Helvetica-Bold",
            fontSize=8,
            leading=10,
            textColor=colors.HexColor("#101828"),
        ),
    }


def make_table(rows, col_widths, s):
    data = []
    for ridx, row in enumerate(rows):
        style = s["table_header"] if ridx == 0 else s["table_cell"]
        data.append([Paragraph(cell, style) for cell in row])
    table = Table(data, colWidths=col_widths, hAlign="LEFT", repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#344054")),
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#D0D5DD")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F9FAFB")]),
            ]
        )
    )
    return table


def build():
    s = styles()
    doc = BaseDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=0.65 * inch,
        rightMargin=0.65 * inch,
        topMargin=0.68 * inch,
        bottomMargin=0.72 * inch,
        title="QureGenAI Quantum AIDD Due Diligence Report",
        author="OpenAI Codex",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=footer)])

    story = []
    story.append(Paragraph("QureGenAI Quantum AIDD Due Diligence Report", s["title"]))
    story.append(
        Paragraph(
            f"Prepared {date.today().isoformat()} from company decks, extracted PDF text, subagent diligence review, and limited external source checks.",
            s["subtitle"],
        )
    )
    story.append(
        Paragraph(
            "Executive conclusion: technically plausible and strategically differentiated, but not yet validated as a superior drug discovery platform. The next step should be non-confidential follow-up focused on benchmark proof, primary data, quantum contribution, customer traction, and IP.",
            s["callout"],
        )
    )

    story.append(Paragraph("1. Executive View", s["h1"]))
    story.append(
        Paragraph(
            "QureGenAI's strongest claim is not simply that AI finds molecules better. The differentiated thesis is that quantum computational chemistry can add first-principles electronic-structure signal where conventional AIDD is data-limited or physically approximate.",
            s["body"],
        )
    )
    story.append(
        bullets(
            [
                "<b>Strategic interest:</b> credible wedge for mechanistic, electronic-structure-heavy discovery problems.",
                "<b>Main diligence risk:</b> platform may be an integrated workflow of public AIDD tools plus early quantum demos, without proven proprietary lift.",
                "<b>Evidence maturity:</b> early-stage and assertion-heavy; current materials lack primary validation packages and prospective benchmarks.",
                "<b>Recommended action:</b> request non-confidential follow-up before CDA unless internal strategic appetite is already high.",
            ],
            s["body"],
        )
    )

    story.append(Paragraph("2. Why Quantum Chemistry Could Matter", s["h1"]))
    rows = [
        ["Dimension", "Conventional AIDD / CADD Limitation", "Potential Quantum Chemistry Advantage", "Diligence Caveat"],
        [
            "Data dependency",
            "ML performance depends on dataset quality, relevance, and leakage controls.",
            "First-principles calculations can in principle generate signal for novel chemotypes or sparse target classes.",
            "Must show prospective lift versus strong classical baselines.",
        ],
        [
            "Electronic effects",
            "Docking, QSAR, and force fields often simplify charge transfer, polarization, covalency, metal centers, and water networks.",
            "Electronic-structure modeling may better capture bond breaking/forming, reaction barriers, protonation, tautomerism, and active-site chemistry.",
            "Near-term quantum hardware is noisy and limited to small active spaces.",
        ],
        [
            "Mechanistic explainability",
            "Black-box AI scores often do not expose why a compound should work.",
            "Quantum/QM outputs can be tied to energy terms, Hamiltonians, active spaces, and QM/MM regions.",
            "Explainability is useful only if predictions correlate with experimental outcomes.",
        ],
        [
            "Experiment efficiency",
            "Large virtual screens can still produce modest enrichment and many false positives.",
            "If accurate, mechanistic calculations could prioritize fewer, higher-information wet-lab tests.",
            "The company has not provided cohort-level hit-rate or conversion data.",
        ],
    ]
    story.append(make_table(rows, [0.95 * inch, 1.6 * inch, 1.7 * inch, 1.35 * inch], s))

    story.append(Paragraph("3. Company And Platform Snapshot", s["h1"]))
    story.append(
        bullets(
            [
                "QureGenAI is presented as an AI + quantum drug discovery engine from Yitu Biotech / QureGenAI, with web, API, and MCP-style access.",
                "The deck describes integration of 20+ tools including RFDiffusion3, Protenix, AutoDock, DiffDock/PocketVina, ProteinMPNN, Foldseek2, PocketXMol, Boltz2/PSICHIC, MolMap, and TyxonQ.",
                "TyxonQ is positioned as the quantum engine connected to real superconducting quantum hardware and quantum chemistry workflows.",
                "The company claims Suzhou HQ, Xi'an quantum computing center, Beijing gene center, Nanjing medicinal chemistry lab, 9 FIC pipelines, 20+ enterprise/hospital customers, and 20+ platform-driven pipelines.",
            ],
            s["body"],
        )
    )

    story.append(Paragraph("4. Evidence Assessment", s["h1"]))
    rows = [
        ["Claim Area", "Deck Evidence", "Assessment", "What Must Be Verified"],
        [
            "Quantum hardware access",
            "TyxonQ connected to real superconducting quantum computers and active-space workflows.",
            "Partially supported externally by TyxonQ site and GitHub repo, but platform maturity is not proven.",
            "Hardware specs, uptime, queue reliability, circuit depth, qubits, fidelity, error mitigation, and task logs.",
        ],
        [
            "Better drug design",
            "Decks claim higher physical fidelity, lower data dependency, and very high FIC success.",
            "Scientifically plausible for narrow problem classes, but broad superiority is unproven.",
            "Prospective head-to-head benchmarks against CADD, MD, FEP, QM/MM, docking, and ML.",
        ],
        [
            "Pipeline validation",
            "QGB-02 AGA, QGCPU-03 anemia/CKD, ASO/siRNA examples with claimed wet-lab evidence.",
            "Interesting but primary data are absent; some pipeline/stage labels are inconsistent.",
            "Protocols, controls, raw data, stats, PK/PD, tox, formulation, regulatory status, and replication.",
        ],
        [
            "Commercial traction",
            "Claims of 20+ customers and 20+ R&D pipelines.",
            "Unsubstantiated from provided materials.",
            "Named references, paid vs pilot split, contract values, retention, usage metrics.",
        ],
        [
            "IP / moat",
            "Claims of PCT authorization and 5+ patents; heavy use of known tools.",
            "Moat is unclear; public-tool integration is not enough.",
            "Patent list, claim scope, ownership, FTO, proprietary datasets, and algorithmic lift.",
        ],
    ]
    story.append(make_table(rows, [1.0 * inch, 1.45 * inch, 1.6 * inch, 1.55 * inch], s))

    story.append(PageBreak())
    story.append(Paragraph("5. Key Red Flags", s["h1"]))
    story.append(
        bullets(
            [
                "<b>Overclaiming:</b> statements implying 95% FIC success or drug discovery success approaching 100% are extraordinary and unsupported by the package.",
                "<b>Pipeline inconsistency:</b> QGB-02 is described as a biologic in one table and an AGA small molecule in a case slide.",
                "<b>Stage inconsistency:</b> QGB-02 is described as clinical ready, volunteer-tested, and preparing to enter preclinical work.",
                "<b>Quantum contribution unclear:</b> it is not shown that quantum calculations changed candidate selection or improved outcomes versus conventional methods.",
                "<b>Public-tool dependency:</b> many platform components appear to be known external or open-source tools; proprietary differentiation needs isolation.",
                "<b>Regulatory ambiguity:</b> drug/cosmetic dual-track AGA registration needs jurisdiction, product class, endpoint, and claims-path clarification.",
            ],
            s["body"],
        )
    )

    story.append(Paragraph("6. Diligence Questions", s["h1"]))
    rows = [
        ["Priority", "Question / Request", "Why It Matters"],
        [
            "1",
            "Provide prospective benchmark studies showing QureGenAI incremental performance versus standard AIDD/CADD/QM/MM on the same tasks.",
            "This is the central proof of platform validity.",
        ],
        [
            "2",
            "Provide a quantum contribution memo: exact workflow, QPU usage, active-space definition, runtime/cost, and decisions changed.",
            "Separates quantum-enabled discovery from branding.",
        ],
        [
            "3",
            "Provide raw packages for QGB-02 and QGCPU-03: protocols, controls, stats, PK/PD, tox, formulation, and replication.",
            "Determines whether pipeline claims support asset value.",
        ],
        [
            "4",
            "Provide customer proof: named references, paid contract details, renewal/retention, and platform usage metrics.",
            "Validates market pull and willingness to pay.",
        ],
        [
            "5",
            "Provide patent numbers, claim charts, ownership, FTO, and relation to public tools.",
            "Determines whether the platform and assets are defensible.",
        ],
    ]
    story.append(make_table(rows, [0.7 * inch, 3.25 * inch, 1.65 * inch], s))

    story.append(Paragraph("7. Decision Recommendation", s["h1"]))
    story.append(
        Paragraph(
            "Recommended next action: <b>Request non-confidential follow-up before CDA</b>. Proceed to confidential diligence only if the company can produce a credible data inventory, primary study packages, customer proof, and a clear quantum contribution case.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "Walk-away signal: QureGenAI cannot show at least one case where Quantum AIDD made a materially better decision than best-in-class classical AI/CADD/HPC and that decision translated into wet-lab or asset value.",
            s["callout"],
        )
    )

    story.append(Paragraph("8. Source Register", s["h1"]))
    sources = [
        ["S1", "Company deck", "/Users/chengbj/Downloads/[Chinese] TyxonQ quantum computational chemistry final external deck.pdf", "82 pages; quantum chemistry and TyxonQ platform claims."],
        ["S2", "Company deck", "/Users/chengbj/Downloads/Yitu Biotech company introduction 20260130 V8 Chinese.pdf", "21 pages; company, pipeline, team, and platform claims."],
        ["S3", "Company deck", "/Users/chengbj/Downloads/[Final] QureGenAI drug design platform introduction.pdf", "23 pages; product features and workflow claims."],
        ["S4", "External", "https://www.tyxonq.com/", "TyxonQ device status and hardware summary as accessed during review."],
        ["S5", "External", "https://github.com/QureGenAI-Biotech/TyxonQ", "Open-source TyxonQ software repository and README claims."],
        ["S6", "External publication", "https://arxiv.org/abs/2401.03759", "Hybrid quantum computing pipeline for real-world drug discovery."],
    ]
    story.append(make_table([["ID", "Type", "Source", "Use"]] + sources, [0.45 * inch, 0.85 * inch, 2.45 * inch, 1.85 * inch], s))
    story.append(Spacer(1, 0.15 * inch))
    story.append(
        Paragraph(
            "Evidence note: Company deck statements are treated as company-provided claims, not independently verified facts. External links were used only to corroborate existence and scope of TyxonQ and the cited quantum-drug-discovery publication.",
            s["small"],
        )
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc.build(story)


if __name__ == "__main__":
    build()
    print(OUT)
