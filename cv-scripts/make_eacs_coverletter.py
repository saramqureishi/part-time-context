#!/usr/bin/env python3
"""EACS cover letter as a clean PDF - short, simple, medium-level English, no em-dashes."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

NAVY = HexColor("#1F3A66")
DARK = HexColor("#1A1A1A")

styles = getSampleStyleSheet()
name_style = ParagraphStyle("N", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=16, textColor=NAVY, alignment=0, spaceAfter=1, leading=19)
contact_style = ParagraphStyle("C", parent=styles["Normal"], fontSize=9.5,
    textColor=DARK, spaceAfter=10, leading=13)
body = ParagraphStyle("B", parent=styles["Normal"], fontSize=10.5, leading=15,
    alignment=TA_JUSTIFY, spaceAfter=8, textColor=DARK)
plain = ParagraphStyle("P", parent=styles["Normal"], fontSize=10.5, leading=15,
    alignment=TA_LEFT, spaceAfter=3, textColor=DARK)


def build(path):
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=22 * mm,
        rightMargin=22 * mm, topMargin=18 * mm, bottomMargin=18 * mm)
    e = []
    e.append(Paragraph("Sara Qureishi", name_style))
    e.append(Paragraph(
        "34 The Ridgeway, North Harrow, HA2 7QN<br/>"
        "07760 584657 &nbsp;|&nbsp; sara.mqureishi@gmail.com", contact_style))

    e.append(Paragraph("13 October 2026", plain))
    e.append(Spacer(1, 4))
    e.append(Paragraph(
        "Martine McLean<br/>Ealing Abbey Counselling Service<br/>"
        "1A Montpelier Avenue, London W5 2XP", plain))
    e.append(Spacer(1, 8))
    e.append(Paragraph("Dear Martine,", plain))
    e.append(Paragraph("<b>Re: Database and Payments Administrator</b>", plain))
    e.append(Spacer(1, 4))

    for p in [
        "I am writing to apply for the Database and Payments Administrator role "
        "at Ealing Abbey Counselling Service. I am an organised and careful "
        "person who is good with numbers and data, and I would really like to "
        "support a small team doing important work in the community.",

        "I think this role suits me well. In my job at Pythian, I worked on a "
        "large data project where I helped move over 600 records and database "
        "objects to a new system, making sure the data stayed accurate and "
        "consistent. I also checked and tested the data carefully and sorted "
        "out any errors I found. This is similar to checking payments and "
        "keeping attendance and payment records correct at EACS. I am confident "
        "using Microsoft Excel, Word and Outlook, and as a Computer Science "
        "graduate and current MSc student, I learn new systems quickly, so I "
        "would soon be comfortable with CORE Net and SumUp.",

        "I also enjoy working with people. In my previous role I spoke with "
        "clients regularly and explained things clearly, so I would be happy "
        "to follow up with your volunteer counsellors in a friendly and polite "
        "way. I am reliable, good at managing my time, and able to work well "
        "both on my own and as part of a team. I also understand how important "
        "it is to keep information confidential.",

        "I do not have direct experience in counselling services, but I am "
        "genuinely interested in the charity sector and in supporting services "
        "that help people. The hours and the Ealing location suit me well, and "
        "I would be glad to discuss my application further.",

        "Thank you for considering my application.",
    ]:
        e.append(Paragraph(p, body))

    e.append(Spacer(1, 6))
    e.append(Paragraph("Yours sincerely,", plain))
    e.append(Paragraph("Sara Qureishi", plain))

    doc.build(e)
    print("Wrote", path)


if __name__ == "__main__":
    build("/projects/sandbox/job-search/Sara_Qureishi_EACS_Cover_Letter.pdf")
