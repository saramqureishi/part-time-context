#!/usr/bin/env python3
"""Sara's Home Bargains part-time Sales Assistant CV.

Follows the handover rules: Pythian only, no em-dashes, simple English,
First Class kept on the BTech, availability Fri to Tue (not Wed/Thu).
"""
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

    # Summary
    e.append(Paragraph(
        "Friendly, reliable and hard working Brunel University London student "
        "(MSc Artificial Intelligence) looking for a part-time Sales Assistant "
        "role at Home Bargains. I enjoy helping customers, keeping a shop "
        "tidy and well stocked, and working as part of a busy team. I am "
        "available on Friday, Saturday, Sunday, Monday and Tuesday, including "
        "mornings, evenings and weekends. I am not available on Wednesday or "
        "Thursday due to university classes.",
        summary_style))

    # Why I'm a great fit
    e.append(Paragraph("WHY I'M A GREAT FIT", section_style))
    e.append(hr())
    e.append(bullets([
        "Friendly and confident with customers, always happy to help them find "
        "what they need.",
        "Happy to do shop floor tasks such as filling shelves, keeping "
        "aisles tidy and putting products in the right place.",
        "Comfortable working on the till and handling payments carefully and "
        "accurately.",
        "A strong team player who supports colleagues in a busy shop.",
        "Reliable, punctual and quick to learn new tasks and systems.",
        "Flexible across my available days (Friday to Tuesday), including "
        "mornings, evenings and weekends.",
    ]))

    # Experience
    e.append(Paragraph("EXPERIENCE", section_style))
    e.append(hr())

    e.append(Paragraph("PYTHIAN", company_style))
    e.append(Paragraph("Analytics Consultant | May 2022 - August 2023",
                       jobtitle_style))
    e.append(bullets([
        "Worked in a busy, fast-paced team and spoke with clients to "
        "understand what they needed and keep them updated clearly.",
        "Stayed organised and accurate while handling several tasks at once "
        "and meeting deadlines.",
        "Promoted within four months for being reliable, hard working and "
        "quick to learn.",
        "Checked and validated work carefully so the results were correct and "
        "could be trusted.",
    ]))

    # University & Community Involvement
    e.append(Paragraph("UNIVERSITY & COMMUNITY INVOLVEMENT", section_style))
    e.append(hr())
    e.append(bullets([
        "Event volunteer at a community meetup of 50+ people, handling "
        "registration, welcoming guests, parking and prizes as part of a team.",
        "Acknowledged contributor in Artificial Intelligence Review (Springer, "
        "2026), credited for careful and reliable testing work.",
    ]))

    # Education
    e.append(Paragraph("EDUCATION", section_style))
    e.append(hr())
    e.append(bullets([
        "MSc Artificial Intelligence - Brunel University London (ongoing).",
        "BTech Computer Science and Engineering - JNTU Hyderabad, India "
        "(First Class).",
    ]))

    doc.build(e)
    print("Wrote", path)


if __name__ == "__main__":
    build("/projects/sandbox/part-time-context/CVs/Sara_Qureishi_CV_HomeBargains.pdf")
