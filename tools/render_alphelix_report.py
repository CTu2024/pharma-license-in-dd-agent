from pathlib import Path
import html
import re

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


BASE = Path("/Users/chengbj/Documents/Due Diligence")
MD_PATH = BASE / "outputs" / "alphelix_gpcr_asset_generation_report.md"
HTML_PATH = BASE / "outputs" / "alphelix_gpcr_asset_generation_report.html"
PDF_PATH = BASE / "outputs" / "alphelix_gpcr_asset_generation_report.pdf"


def inline_html(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    return text


def inline_pdf(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    return text


def render_html(lines: list[str]) -> None:
    out = [
        "<!doctype html>",
        '<html><head><meta charset="utf-8">',
        "<title>Alphelix GPCR Asset Generation Capability Report</title>",
        """<style>
:root{color-scheme:light;}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif;line-height:1.55;color:#1f2933;max-width:980px;margin:40px auto;padding:0 28px;background:#fff;}
h1{font-size:30px;line-height:1.2;margin:0 0 12px;color:#0f2a43;}
h2{font-size:21px;margin-top:34px;border-bottom:1px solid #d9e2ec;padding-bottom:7px;color:#173a5e;}
h3{font-size:17px;margin-top:24px;color:#243b53;}
p{margin:10px 0;}
ul{padding-left:24px;}
li{margin:5px 0;}
table{border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;}
th,td{border:1px solid #cbd5e1;padding:8px 10px;vertical-align:top;}
th{background:#eef2f7;text-align:left;}
code{background:#f1f5f9;padding:1px 4px;border-radius:4px;}
.meta{color:#52606d;margin-bottom:26px;}
a{color:#1267b3;}
</style></head><body>""",
    ]
    in_ul = False
    in_table = False
    row_count = 0

    for line in lines:
        stripped = line.strip()
        if not stripped:
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if in_table:
                out.append("</table>")
                in_table = False
            continue

        if stripped.startswith("|") and stripped.endswith("|"):
            if in_ul:
                out.append("</ul>")
                in_ul = False
            cells = [cell.strip() for cell in stripped.strip("|").split("|")]
            if all(set(cell) <= set("-: ") for cell in cells):
                continue
            if not in_table:
                out.append("<table>")
                in_table = True
                row_count = 0
            tag = "th" if row_count == 0 else "td"
            out.append(
                "<tr>"
                + "".join(f"<{tag}>{inline_html(cell)}</{tag}>" for cell in cells)
                + "</tr>"
            )
            row_count += 1
            continue

        if in_table:
            out.append("</table>")
            in_table = False
        if stripped.startswith("- "):
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline_html(stripped[2:])}</li>")
            continue

        if in_ul:
            out.append("</ul>")
            in_ul = False

        level = len(stripped) - len(stripped.lstrip("#"))
        if 1 <= level <= 3 and stripped[level : level + 1] == " ":
            out.append(f"<h{level}>{inline_html(stripped[level + 1:])}</h{level}>")
        elif stripped.startswith("Date:"):
            out.append(f'<p class="meta">{inline_html(stripped)}</p>')
        else:
            out.append(f"<p>{inline_html(stripped)}</p>")

    if in_ul:
        out.append("</ul>")
    if in_table:
        out.append("</table>")
    out.append("</body></html>")
    HTML_PATH.write_text("\n".join(out), encoding="utf-8")


def render_pdf(lines: list[str]) -> None:
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="ReportTitle",
            parent=styles["Title"],
            fontSize=20,
            leading=24,
            spaceAfter=12,
            textColor=colors.HexColor("#0f2a43"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="H2x",
            parent=styles["Heading2"],
            fontSize=14,
            leading=18,
            spaceBefore=16,
            spaceAfter=7,
            textColor=colors.HexColor("#173a5e"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="H3x",
            parent=styles["Heading3"],
            fontSize=11.5,
            leading=15,
            spaceBefore=10,
            spaceAfter=5,
            textColor=colors.HexColor("#243b53"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="Bodyx",
            parent=styles["BodyText"],
            fontSize=9.2,
            leading=12.2,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Smallx",
            parent=styles["BodyText"],
            fontSize=8.2,
            leading=10.5,
            spaceAfter=4,
            textColor=colors.HexColor("#52606d"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="Bulletx",
            parent=styles["BodyText"],
            fontSize=9.2,
            leading=12.2,
            leftIndent=10,
        )
    )

    story = []
    bullets: list[str] = []
    table_rows: list[list[str]] = []

    def flush_bullets() -> None:
        nonlocal bullets
        if not bullets:
            return
        story.append(
            ListFlowable(
                [ListItem(Paragraph(inline_pdf(item), styles["Bulletx"])) for item in bullets],
                bulletType="bullet",
                leftIndent=16,
            )
        )
        story.append(Spacer(1, 4))
        bullets = []

    def flush_table() -> None:
        nonlocal table_rows
        if not table_rows:
            return
        data = [
            [Paragraph(inline_pdf(cell), styles["Smallx"]) for cell in row]
            for row in table_rows
        ]
        table = Table(data, repeatRows=1, hAlign="LEFT")
        table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eef2f7")),
                    ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#cbd5e1")),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 5),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                    ("TOPPADDING", (0, 0), (-1, -1), 4),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ]
            )
        )
        story.append(table)
        story.append(Spacer(1, 8))
        table_rows = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            flush_bullets()
            flush_table()
            continue

        if stripped.startswith("|") and stripped.endswith("|"):
            flush_bullets()
            cells = [cell.strip() for cell in stripped.strip("|").split("|")]
            if all(set(cell) <= set("-: ") for cell in cells):
                continue
            table_rows.append(cells)
            continue

        flush_table()
        if stripped.startswith("- "):
            bullets.append(stripped[2:])
            continue

        flush_bullets()
        level = len(stripped) - len(stripped.lstrip("#"))
        if level == 1 and stripped[level : level + 1] == " ":
            story.append(Paragraph(inline_pdf(stripped[level + 1 :]), styles["ReportTitle"]))
        elif level == 2 and stripped[level : level + 1] == " ":
            story.append(Paragraph(inline_pdf(stripped[level + 1 :]), styles["H2x"]))
        elif level == 3 and stripped[level : level + 1] == " ":
            story.append(Paragraph(inline_pdf(stripped[level + 1 :]), styles["H3x"]))
        elif stripped.startswith("Date:"):
            story.append(Paragraph(inline_pdf(stripped), styles["Smallx"]))
            story.append(Spacer(1, 8))
        else:
            story.append(Paragraph(inline_pdf(stripped), styles["Bodyx"]))

    flush_bullets()
    flush_table()
    doc = SimpleDocTemplate(
        str(PDF_PATH),
        pagesize=letter,
        rightMargin=0.7 * inch,
        leftMargin=0.7 * inch,
        topMargin=0.65 * inch,
        bottomMargin=0.65 * inch,
        title="Alphelix GPCR Asset Generation Capability Report",
    )
    doc.build(story)


def main() -> None:
    lines = MD_PATH.read_text(encoding="utf-8").splitlines()
    render_html(lines)
    render_pdf(lines)
    print(HTML_PATH)
    print(PDF_PATH)


if __name__ == "__main__":
    main()
