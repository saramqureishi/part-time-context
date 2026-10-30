#!/usr/bin/env python3
"""Sara's CV for Penshurst Gardens Surgery Administrator/Receptionist. Simple English, no em-dashes."""
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
name_style = ParagraphStyle("Name", parent=styles["Title"],
    fontName="Helvetica-Bold", fontSize=22, textColor=NAVY,
    alignment=TA_CENTER, spaceAfter=4, leading=25)
contact_style = ParagraphStyle("Contact", parent=styles["Normal"],
    fontSize=9.5, alignment=TA_CENTER, textColor=DARK, spaceAfter=10, leading=13)
summary_style = ParagraphStyle("Summary", parent=styles["Normal"],
    fontSize=10, leading=14.5, alignment=TA_JUSTIFY, spaceAfter=4, textColor=DARK)
section_style = ParagraphStyle("Section", parent=styles["Heading2"],
    fontName="Helvetica-Bold", fontSize=12, textColor=NAVY,
    alignment=TA_CENTER, spaceBefore=10, spaceAfter=3, leading=15)
company_style = ParagraphStyle("Company", parent=styles["Normal"],
    fontName="Helvetica-Bold", fontSize=10.5, textColor=NAVY,
    spaceBefore=6, spaceAfter=0, leading=13)
jobtitle_style = ParagraphStyle("JobTitle", parent=styles["Normal"],
    fontName="Helvetica-Bold", fontSize=10, textColor=DARK,
    spaceBefore=1, spaceAfter=2, leading=13)
bullet_style = ParagraphStyle("Bullet", parent=styles["Normal"], fontSize=10,
    leading=13.5, spaceAfter=1.5, textColor=DARK)


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
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=20 * mm,
        rightMargin=20 * mm, topMargin=16 * mm, bottomMargin=16 * mm)
    e = []
    e.append(Paragraph("Sara Qureishi", name_style))
    e.append(Paragraph(
        "North Harrow, London &nbsp;|&nbsp; 07760 584657 &nbsp;|&nbsp; "
        "sara.qureishi24@gmail.com", contact_style))

    e.append(Paragraph(
        "Friendly, reliable and well-organised Brunel University London "
        "student (MSc Artificial Intelligence) with customer service and "
        "administrative experience in busy, fast-paced settings. I give a "
        "polite and professional service in person and on the telephone, "
        "communicate clearly with everyone, and take pride in keeping work "
        "accurate and confidential. Calm under pressure, adaptable and good "
        "with computers, I would be glad to join the team at Penshurst "
        "Gardens Surgery as an Administrator and Receptionist.", summary_style))

    e.append(Paragraph("WHY I'M A GREAT FIT", section_style))
    e.append(hr())
    e.append(bullets([
        "Excellent communication skills with a polite, professional telephone "
        "manner",
        "Experienced in giving high levels of customer service, in person and "
        "by phone",
        "Good keyboard, computer and Microsoft Office skills, and quick to "
        "learn systems such as EMIS Web",
        "Well organised with good attention to detail, able to prioritise and "
        "work to deadlines",
        "Calm and polite under pressure, able to use initiative and help "
        "resolve concerns",
        "Understands the importance of confidentiality, and works well both "
        "independently and in a team",
    ]))

    e.append(Paragraph("EXPERIENCE", section_style))
    e.append(hr())
    e.append(Paragraph("PYTHIAN", company_style))
    e.append(Paragraph("Consultant | May 2022 - August 2023", jobtitle_style))
    e.append(bullets([
        "Dealt with clients face to face, by phone and by email, giving a "
        "polite and efficient service.",
        "Worked in a busy, pressurised environment while staying calm, "
        "accurate and organised.",
        "Entered and managed data and records carefully, keeping information "
        "confidential.",
        "Worked well as part of a team and promoted within 4 months for "
        "reliability and work ethic.",
    ]))

    e.append(Paragraph("EDUCATION", section_style))
    e.append(hr())
    e.append(bullets([
        "MSc Artificial Intelligence, Brunel University London (ongoing)",
        "BTech Computer Science and Engineering, JNTU Hyderabad, India "
        "(First Class)",
        "Secondary education to GCSE/A-Level standard (equivalent), Hyderabad, "
        "India",
    ]))

    doc.build(e)
    print("Wrote", path)


if __name__ == "__main__":
    build("/projects/sandbox/job-search/Sara_Qureishi_CV_Penshurst.pdf")
