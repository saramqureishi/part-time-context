#!/usr/bin/env python3
"""Sara's general part-time CV (retail, customer service, admin).

Rules: Pythian + Zudio only (no TEQBIT), no em-dashes, simple English,
no First Class, no weekdays in the text.
"""
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
        "North Harrow, London, HA2 7QN &nbsp;|&nbsp; 07760 584657 &nbsp;|&nbsp; "
        "sara.qureishi24@gmail.com", contact_style))

    e.append(Paragraph("PROFESSIONAL SUMMARY", section_style))
    e.append(hr())
    e.append(Paragraph(
        "Friendly, reliable and hard working MSc Artificial Intelligence "
        "student at Brunel University London, with part-time retail "
        "experience and experience working with clients in busy teams. I "
        "enjoy helping customers, keeping a shop tidy and well stocked, and "
        "learning new tasks quickly. I am looking for part-time work in "
        "retail, customer service or administration where I can support the "
        "team and grow.", summary_style))

    e.append(Paragraph("EDUCATION", section_style))
    e.append(hr())
    e.append(Paragraph("BRUNEL UNIVERSITY LONDON", company_style))
    e.append(Paragraph("MSc Artificial Intelligence (ongoing)", body_style))
    e.append(Paragraph("JNTU HYDERABAD, INDIA", company_style))
    e.append(Paragraph("BTech Computer Science and Engineering", body_style))

    e.append(Paragraph("WORK EXPERIENCE", section_style))
    e.append(hr())

    e.append(Paragraph("SALES ASSISTANT (PART-TIME)", company_style))
    e.append(Paragraph("Zudio | Hyderabad, India | 2019 - 2022", jobtitle_style))
    e.append(bullets([
        "Welcomed customers, answered their questions and helped them find "
        "the right products and sizes.",
        "Kept shelves, rails and displays neat, full and in the right place.",
        "Helped with stock and putting out new items.",
        "Supported the till and billing during busy times, working "
        "accurately.",
        "Worked with the team to keep the store clean, tidy and ready for "
        "customers.",
    ]))

    e.append(Paragraph("CONSULTANT", company_style))
    e.append(Paragraph("Pythian | May 2022 - August 2023", jobtitle_style))
    e.append(bullets([
        "Spoke with clients to understand what they needed and kept them "
        "updated clearly.",
        "Handled several tasks at once and met deadlines in a busy team.",
        "Checked work carefully so the results were accurate and could be "
        "trusted.",
        "Promoted within four months for being reliable and quick to learn.",
    ]))

    e.append(Paragraph("VOLUNTEERING", section_style))
    e.append(hr())
    e.append(bullets([
        "Event volunteer at a community meetup of 50+ people, helping with "
        "registration, welcoming guests, parking and prizes.",
    ]))

    e.append(Paragraph("CORE SKILLS", section_style))
    e.append(hr())
    e.append(bullets([
        "<b>Customer service:</b> friendly communication, active listening, "
        "helping and guiding customers.",
        "<b>Retail:</b> stock replenishment, tidy displays, till and billing "
        "support.",
        "<b>Administration:</b> accurate record-keeping, Microsoft Office, "
        "quick to learn new systems.",
        "<b>Soft skills:</b> teamwork, reliability, time management, "
        "adaptability.",
        "<b>Languages:</b> English (fluent).",
    ]))

    e.append(Paragraph("AVAILABILITY", section_style))
    e.append(hr())
    e.append(Paragraph(
        "Available to start immediately. Flexible with shifts, including "
        "mornings, evenings and weekends, within the legal limit of 20 hours "
        "per week during term time.", body_style))

    doc.build(e)
    print("Wrote", path)


if __name__ == "__main__":
    build("/projects/sandbox/part-time-context/CVs/"
          "Sara_Qureishi_CV_PartTime_General.pdf")
