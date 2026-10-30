#!/usr/bin/env python3
"""Sara's CV for EACS Database & Payments Administrator (Ealing, 12 hrs/wk).
Same clean layout as the reference. Pythian only (no TEQBIT, per Sara's choice)."""
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
body_style = ParagraphStyle("Body", parent=styles["Normal"], fontSize=10,
    leading=14, alignment=TA_LEFT, spaceAfter=2, textColor=DARK)
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
        "London, UK &nbsp;|&nbsp; 07760 584657 &nbsp;|&nbsp; "
        "sara.qureishi24@gmail.com", contact_style))

    e.append(Paragraph(
        "Organised and careful Brunel University London student (MSc "
        "Artificial Intelligence) with a First Class degree in Computer "
        "Science and work experience in data and systems. I am good with "
        "numbers and pay close attention to detail when entering and checking "
        "data. I am confident using Microsoft Excel, Word and Outlook, "
        "communicate clearly and politely, and understand the importance of "
        "keeping information confidential. Reliable, well organised and calm "
        "under pressure, I would be glad to support the team at Ealing Abbey "
        "Counselling Service as Database and Payments Administrator.",
        summary_style))

    e.append(Paragraph("WHY I'M A GREAT FIT", section_style))
    e.append(hr())
    e.append(bullets([
        "Good attention to detail when entering and checking data",
        "Good with numbers and a high level of accuracy",
        "Experience using databases, and confident with Microsoft Excel, "
        "Word and Outlook",
        "Well organised and able to manage my time and meet deadlines",
        "Able to work on my own and stay effective under pressure",
        "Clear, polite communicator and a good team player who respects "
        "confidentiality",
    ]))

    e.append(Paragraph("EXPERIENCE", section_style))
    e.append(hr())
    e.append(Paragraph("PYTHIAN (Data Practice)", company_style))
    e.append(Paragraph("Consultant | May 2022 - August 2023", jobtitle_style))
    e.append(bullets([
        "Helped move over 600 records and database objects to a new system "
        "(SAP HANA Cloud), making sure the data stayed accurate and "
        "consistent.",
        "Checked and tested data carefully after the move and sorted out any "
        "errors I found.",
        "Improved data processes, reducing processing time by 28%.",
        "Spoke with clients regularly, understood what they needed and "
        "explained things clearly.",
        "Promoted within 4 months for my work and reliability.",
    ]))

    e.append(Paragraph("EDUCATION", section_style))
    e.append(hr())
    e.append(bullets([
        "MSc Artificial Intelligence, Brunel University London (ongoing)",
        "BTech Computer Science and Engineering, JNTU Hyderabad, India "
        "(First Class)",
        "Higher Secondary Certificate (Class 12, equivalent to A-Levels), "
        "Hyderabad, India",
    ]))

    doc.build(e)
    print("Wrote", path)


if __name__ == "__main__":
    build("/projects/sandbox/job-search/Sara_Qureishi_CV_EACS.pdf")
