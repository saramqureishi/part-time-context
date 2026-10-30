#!/usr/bin/env python3
"""Sara's Pandora Seasonal Sales & Operations Assistant CV — styled to match the
Primark reference layout (centered navy name, centered summary, centered section
headings with rules, dated roles)."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, HRFlowable, ListFlowable, ListItem, Spacer
)

NAVY = HexColor("#1F3A66")
DARK = HexColor("#222222")

styles = getSampleStyleSheet()

name_style = ParagraphStyle(
    "Name", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=22, textColor=NAVY, alignment=TA_CENTER, spaceAfter=4, leading=25)
contact_style = ParagraphStyle(
    "Contact", parent=styles["Normal"], fontSize=9.5, alignment=TA_CENTER,
    textColor=DARK, spaceAfter=10, leading=13)
summary_style = ParagraphStyle(
    "Summary", parent=styles["Normal"], fontSize=10, leading=14.5,
    alignment=TA_JUSTIFY, spaceAfter=4, textColor=DARK)
section_style = ParagraphStyle(
    "Section", parent=styles["Heading2"], fontName="Helvetica-Bold",
    fontSize=12, textColor=NAVY, alignment=TA_CENTER,
    spaceBefore=10, spaceAfter=3, leading=15)
company_style = ParagraphStyle(
    "Company", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=10.5, textColor=NAVY, spaceBefore=6, spaceAfter=0, leading=13)
jobtitle_style = ParagraphStyle(
    "JobTitle", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=10, textColor=DARK, spaceBefore=1, spaceAfter=2, leading=13)
body_style = ParagraphStyle(
    "Body", parent=styles["Normal"], fontSize=10, leading=14,
    alignment=TA_LEFT, spaceAfter=2, textColor=DARK)
bullet_style = ParagraphStyle(
    "Bullet", parent=styles["Normal"], fontSize=10, leading=13.5,
    spaceAfter=1.5, textColor=DARK)


def hr():
    return HRFlowable(width="100%", thickness=1, color=HexColor("#2E2E2E"),
                      spaceBefore=0, spaceAfter=5)


def bullets(items):
    return ListFlowable(
        [ListItem(Paragraph(t, bullet_style), leftIndent=10, value="\u2022")
         for t in items],
        bulletType="bullet", start="\u2022", leftIndent=14, bulletFontSize=8,
        spaceBefore=2, spaceAfter=2)


def build(path):
    doc = SimpleDocTemplate(
        path, pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm,
        topMargin=16 * mm, bottomMargin=16 * mm)
    e = []

    # Header
    e.append(Paragraph("Sara Qureishi", name_style))
    e.append(Paragraph(
        "London, UK &nbsp;|&nbsp; 07760 584657 &nbsp;|&nbsp; "
        "sara.qureishi24@gmail.com", contact_style))

    # Summary (centered-style paragraph, like the reference)
    e.append(Paragraph(
        "Warm, friendly and customer-focused Brunel University London student "
        "(MSc Artificial Intelligence) with experience in "
        "busy, fast-paced, client-facing environments. I love meeting new "
        "people, building genuine connections and helping customers find "
        "exactly what they are looking for &mdash; especially meaningful gifts "
        "for the people they care about. Positive, reliable and sales-minded, "
        "I enjoy working as part of an upbeat team and would be proud to "
        "represent Pandora as a Seasonal Sales &amp; Operations Assistant and "
        "help make the festive season sparkle.", summary_style))

    # Why I'm a great fit
    e.append(Paragraph("WHY I'M A GREAT FIT", section_style))
    e.append(hr())
    e.append(bullets([
        "Warm and confident at connecting with customers, listening to their "
        "stories and adapting to their needs",
        "Sales-minded &mdash; motivated to meet and surpass targets through "
        "genuine, helpful conversations",
        "Fast learner who enjoys building product knowledge to deliver "
        "memorable customer experiences",
        "Calm, accurate and organised in a busy environment &mdash; ideal for "
        "the festive rush",
        "Honest, reliable team player with a positive attitude and willingness "
        "to learn",
        "Happy to support behind-the-scenes operations when the store needs it",
    ]))

    # Experience
    e.append(Paragraph("EXPERIENCE", section_style))
    e.append(hr())

    e.append(Paragraph("TEQBIT", company_style))
    e.append(Paragraph("Technical Consultant | August 2023 - January 2026",
                       jobtitle_style))
    e.append(bullets([
        "Built rapport with customers and explained information clearly, "
        "patiently and in a friendly, approachable way.",
        "Represented the business in a live customer-facing demonstration, "
        "confidently presenting and answering questions.",
        "Worked accurately and efficiently in busy, fast-paced, high-pressure "
        "environments.",
        "Reliable and trusted to work independently and support the wider team.",
    ]))

    e.append(Paragraph("PYTHIAN", company_style))
    e.append(Paragraph("Consultant | May 2022 - August 2023", jobtitle_style))
    e.append(bullets([
        "Managed multiple tasks during peak workloads while meeting deadlines "
        "and keeping work well organised.",
        "Promoted within 4 months for reliability, work ethic and quick "
        "learning.",
    ]))

    # Education
    e.append(Paragraph("EDUCATION", section_style))
    e.append(hr())
    e.append(bullets([
        "MSc Artificial Intelligence - Brunel University London (Ongoing)",
    ]))

    doc.build(e)
    print("Wrote", path)


if __name__ == "__main__":
    build("/projects/sandbox/job-search/Sara_Qureishi_CV_Pandora.pdf")
