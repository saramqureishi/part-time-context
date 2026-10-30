#!/usr/bin/env python3
"""Sara's CV for OFFICE Sales Assistant (seasonal). Reference layout; Pythian only."""
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
        "London, UK &nbsp;|&nbsp; 07760 584657 &nbsp;|&nbsp; "
        "sara.qureishi24@gmail.com", contact_style))

    e.append(Paragraph(
        "Enthusiastic, friendly Brunel University London student (MSc "
        "Artificial Intelligence) with customer-facing "
        "experience in busy, fast-paced environments. I enjoy engaging with "
        "customers, making them feel welcome and helping them find exactly "
        "what they are looking for. Positive, reliable and a strong team "
        "player, I thrive when things get busy and would love to join the "
        "OFFICE store team as a Sales Assistant during the peak trading "
        "period.", summary_style))

    e.append(Paragraph("WHY I'M A GREAT FIT", section_style))
    e.append(hr())
    e.append(bullets([
        "Confident, friendly communicator who enjoys engaging with customers "
        "and driving sales",
        "Puts customers first &mdash; making every shopper feel welcome and "
        "well looked after",
        "Thrives in a fast-paced environment and stays calm and positive when "
        "it gets busy",
        "Reliable team player with a passion for great service and a "
        "willingness to learn",
        "Flexible and dependable &mdash; happy to work evenings, weekends and "
        "extra shifts during peak periods",
        "Quick to learn products and confident recommending the right item to "
        "each customer",
    ]))

    e.append(Paragraph("EXPERIENCE", section_style))
    e.append(hr())
    e.append(Paragraph("PYTHIAN", company_style))
    e.append(Paragraph("Consultant | May 2022 - August 2023", jobtitle_style))
    e.append(bullets([
        "Engaged with customers and colleagues in a friendly, helpful way, "
        "communicating clearly and building good relationships.",
        "Worked accurately and reliably in a busy, fast-paced environment, "
        "staying positive under pressure.",
        "Supported the wider team and took on a range of tasks to keep things "
        "running smoothly.",
        "Promoted within 4 months for reliability, work ethic and quick "
        "learning.",
    ]))

    e.append(Paragraph("EDUCATION", section_style))
    e.append(hr())
    e.append(bullets([
        "MSc Artificial Intelligence - Brunel University London (Ongoing)",
        "BTech Computer Science &amp; Engineering - JNTU Hyderabad, India - "
        "First Class",
    ]))

    doc.build(e)
    print("Wrote", path)


if __name__ == "__main__":
    build("/projects/sandbox/job-search/Sara_Qureishi_CV_OFFICE.pdf")
