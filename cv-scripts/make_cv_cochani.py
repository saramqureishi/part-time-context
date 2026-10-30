#!/usr/bin/env python3
"""Sara's CV for Cochani (perfume shop) Sales Assistant. Lively, simple English, no em-dashes."""
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
        "Warm, friendly and well-presented Brunel University London student "
        "(MSc Artificial Intelligence) who loves working with people and "
        "giving a great shopping experience. I enjoy making customers feel "
        "welcome, taking the time to understand what they are looking for, and "
        "helping them find the perfect scent or gift. Positive, reliable and "
        "quick to learn, I would love to join the Cochani team as a part-time "
        "Sales Assistant.", summary_style))

    e.append(Paragraph("WHY I'M A GREAT FIT", section_style))
    e.append(hr())
    e.append(bullets([
        "Warm and welcoming, with a real love of helping customers",
        "Great at listening and finding the right product or gift for each person",
        "Confident and well presented, happy to represent a premium brand",
        "Keen to learn about fragrances and share that knowledge with customers",
        "Reliable, punctual and flexible with shifts",
        "Friendly team player, confident on the tills and keeping the store "
        "looking beautiful",
    ]))

    e.append(Paragraph("EXPERIENCE", section_style))
    e.append(hr())
    e.append(Paragraph("TEQBIT", company_style))
    e.append(Paragraph("Technical Consultant | August 2023 - January 2026",
                       jobtitle_style))
    e.append(bullets([
        "Worked accurately and efficiently in busy, fast-paced, high-pressure "
        "environments.",
        "Kept records and tasks well organised with strong attention to detail.",
        "Reliable and trusted to work independently and support the wider team.",
        "Followed procedures carefully and maintained high standards.",
    ]))
    e.append(Paragraph("PYTHIAN", company_style))
    e.append(Paragraph("Consultant | May 2022 - August 2023", jobtitle_style))
    e.append(bullets([
        "Managed multiple tasks during peak workloads while meeting deadlines.",
        "Worked accurately and reliably, and happily helped the team wherever "
        "needed.",
        "Promoted within 4 months for reliability, work ethic and quick "
        "learning.",
    ]))

    e.append(Paragraph("EDUCATION", section_style))
    e.append(hr())
    e.append(bullets([
        "MSc Artificial Intelligence, Brunel University London (ongoing)",
        "BTech Computer Science and Engineering, JNTU Hyderabad, India",
    ]))

    e.append(Paragraph("AVAILABILITY", section_style))
    e.append(hr())
    e.append(bullets([
        "Part-time, up to 20 hours a week",
        "Available Fridays, Saturdays, Sundays, Mondays and Tuesdays",
        "Not available Wednesdays or Thursdays (university classes)",
        "Flexible with mornings, afternoons, evenings and weekends; reliable "
        "and punctual",
    ]))

    doc.build(e)
    print("Wrote", path)


if __name__ == "__main__":
    build("/projects/sandbox/job-search/Sara_Qureishi_CV_Cochani.pdf")
