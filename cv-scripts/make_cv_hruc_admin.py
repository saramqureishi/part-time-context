#!/usr/bin/env python3
"""Sara's CV for HRUC Administrator - Creative Arts (Uxbridge, term-time, 17 hrs/wk).
Same clean layout as the reference: centered navy name, centered summary,
centered section headings with rules, dated roles."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, HRFlowable, ListFlowable, ListItem
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

    e.append(Paragraph("Sara Qureishi", name_style))
    e.append(Paragraph(
        "London, UK &nbsp;|&nbsp; 07760 584657 &nbsp;|&nbsp; "
        "sara.qureishi24@gmail.com", contact_style))

    e.append(Paragraph(
        "Well organised, flexible and proactive Brunel University London "
        "student (MSc Artificial Intelligence) with administrative and "
        "client-facing experience in busy, fast-paced environments. "
        "Experienced in providing administrative support &mdash; producing "
        "correspondence, managing information, handling queries and "
        "communicating effectively with a wide range of people. Confident "
        "with Microsoft Office and IT systems/databases, with excellent "
        "customer service and interpersonal skills. A reliable team player "
        "who works well on my own initiative, keen to join HRUC as an "
        "Administrator supporting the Creative Arts curriculum team at "
        "Uxbridge.", summary_style))

    e.append(Paragraph("WHY I'M A GREAT FIT", section_style))
    e.append(hr())
    e.append(bullets([
        "Administrative experience in a busy, fast-paced environment",
        "Excellent customer service, interpersonal and communication skills "
        "with students, staff and clients",
        "Confident producing correspondence and reports, managing diaries and "
        "handling queries efficiently",
        "Good working knowledge of Microsoft Office and experience using IT "
        "systems and databases",
        "Well organised with strong attention to detail and the ability to "
        "juggle multiple priorities",
        "A flexible team player, able to work on my own initiative and support "
        "colleagues wherever needed",
    ]))

    e.append(Paragraph("EXPERIENCE", section_style))
    e.append(hr())

    e.append(Paragraph("PYTHIAN", company_style))
    e.append(Paragraph("Consultant | May 2022 - August 2023", jobtitle_style))
    e.append(bullets([
        "Provided administrative and coordination support, keeping records "
        "and information well organised with strong attention to detail.",
        "Handled queries and communicated clearly and professionally with "
        "colleagues and clients.",
        "Used Microsoft Office and IT systems/databases to input, manage and "
        "retrieve information accurately.",
        "Managed multiple tasks and competing deadlines during peak "
        "workloads, staying organised and accurate under pressure.",
        "Promoted within 4 months for reliability, work ethic and quick "
        "learning.",
    ]))

    e.append(Paragraph("EDUCATION", section_style))
    e.append(hr())
    e.append(bullets([
        "MSc Artificial Intelligence - Brunel University London (Ongoing)",
    ]))

    doc.build(e)
    print("Wrote", path)


if __name__ == "__main__":
    build("/projects/sandbox/job-search/Sara_Qureishi_CV_HRUC_Admin.pdf")
