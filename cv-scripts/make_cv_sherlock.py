#!/usr/bin/env python3
"""Sara's CV for Sherlock Holmes Museum Visitor Services Assistant. Simple English, no em-dashes."""
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
        "Friendly, enthusiastic and well-presented Brunel University London "
        "student (MSc Artificial Intelligence) who loves meeting people and "
        "giving them a great experience. I enjoy welcoming visitors from all "
        "walks of life, helping them and making their visit memorable. I am a "
        "confident communicator, happy to talk to groups, stay calm when it "
        "is busy, and help out in the shop. I would love to join the Sherlock "
        "Holmes Museum as a Visitor Services Assistant.", summary_style))

    e.append(Paragraph("WHY I'M A GREAT FIT", section_style))
    e.append(hr())
    e.append(bullets([
        "Strong customer service skills, focused on creating positive visitor "
        "experiences",
        "Warm, friendly manner and enjoy meeting people from all backgrounds",
        "Confident speaking to individuals and groups, happy to give short "
        "guided tours and talks",
        "Calm under pressure in a busy, lively, visitor-facing setting",
        "Happy to help in the shop, sell products and keep the floor tidy "
        "and well presented",
        "Proactive team player who adapts quickly, and comfortable wearing "
        "period costume to engage with visitors",
    ]))

    e.append(Paragraph("EXPERIENCE", section_style))
    e.append(hr())
    e.append(Paragraph("PYTHIAN", company_style))
    e.append(Paragraph("Consultant | May 2022 - August 2023", jobtitle_style))
    e.append(bullets([
        "Spoke with clients every day, welcomed them warmly and explained "
        "things clearly and confidently.",
        "Worked reliably in a busy, fast-paced environment, staying calm and "
        "positive under pressure.",
        "Happily helped the wider team and took on different tasks to keep "
        "things running smoothly.",
        "Promoted within 4 months for my work and reliability.",
    ]))
    e.append(Paragraph("COMMUNITY INVOLVEMENT", company_style))
    e.append(Paragraph("Event volunteer", jobtitle_style))
    e.append(bullets([
        "Volunteered at a community event with 50+ attendees, welcoming and "
        "checking in guests, directing people and helping the event run "
        "smoothly.",
    ]))

    e.append(Paragraph("EDUCATION", section_style))
    e.append(hr())
    e.append(bullets([
        "MSc Artificial Intelligence, Brunel University London (ongoing)",
        "BTech Computer Science and Engineering, JNTU Hyderabad, India",
    ]))

    doc.build(e)
    print("Wrote", path)


if __name__ == "__main__":
    build("/projects/sandbox/job-search/Sara_Qureishi_CV_Sherlock.pdf")
