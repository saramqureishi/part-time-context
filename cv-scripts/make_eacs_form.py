#!/usr/bin/env python3
"""Fill the EACS Database & Payments Administrator application form as a PDF."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
)

NAVY = HexColor("#1F3A66")
DARK = HexColor("#1A1A1A")
GREY = HexColor("#555555")

styles = getSampleStyleSheet()
title_style = ParagraphStyle("T", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=15, textColor=NAVY, alignment=1, spaceAfter=2, leading=18)
sub_style = ParagraphStyle("Sub", parent=styles["Normal"], fontSize=9.5,
    alignment=1, textColor=GREY, spaceAfter=8, leading=12)
sec_style = ParagraphStyle("Sec", parent=styles["Heading2"], fontName="Helvetica-Bold",
    fontSize=11.5, textColor=NAVY, spaceBefore=9, spaceAfter=2, leading=14)
lbl_style = ParagraphStyle("Lbl", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=9.5, textColor=DARK, leading=13)
val_style = ParagraphStyle("Val", parent=styles["Normal"], fontSize=9.5,
    textColor=DARK, leading=13)
body_style = ParagraphStyle("Body", parent=styles["Normal"], fontSize=9.5,
    leading=13.5, textColor=DARK, spaceAfter=3, alignment=TA_LEFT)
note_style = ParagraphStyle("Note", parent=styles["Normal"], fontSize=8.5,
    textColor=HexColor("#B00000"), leading=11, spaceAfter=2)


def hr():
    return HRFlowable(width="100%", thickness=0.8, color=NAVY,
                      spaceBefore=1, spaceAfter=4)


def kv(rows, widths):
    t = Table(rows, colWidths=widths, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t


def grid(rows, widths):
    t = Table(rows, colWidths=widths, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#BBBBBB")),
        ("BACKGROUND", (0, 0), (-1, 0), HexColor("#EEF2F7")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.8),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t


def P(t, s=val_style):
    return Paragraph(t, s)


def build(path):
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=16 * mm,
        rightMargin=16 * mm, topMargin=14 * mm, bottomMargin=14 * mm)
    e = []
    e.append(Paragraph("Ealing Abbey Counselling Service &mdash; Application Form", title_style))
    e.append(Paragraph("Post applied for: Database &amp; Payments Administrator", sub_style))

    # Section 1
    e.append(Paragraph("Section 1 &ndash; Personal Details", sec_style))
    e.append(hr())
    e.append(kv([
        [P("Title:", lbl_style), P("Ms"), P("First Name:", lbl_style), P("Sara")],
        [P("Surname:", lbl_style), P("Qureishi"), P("", lbl_style), P("")],
        [P("Address:", lbl_style), P("34 The Ridgeway, North Harrow"), P("Postcode:", lbl_style), P("HA2 7QN")],
        [P("Telephone (Day):", lbl_style), P("07760 584657"), P("Telephone (Eve):", lbl_style), P("07760 584657")],
        [P("Mobile:", lbl_style), P("07760 584657"), P("Email:", lbl_style), P("sara.mqureishi@gmail.com")],
    ], [68, 150, 70, 140]))

    # Section 2
    e.append(Paragraph("Section 2 &ndash; Present or Most Recent Employment", sec_style))
    e.append(hr())
    e.append(kv([
        [P("Name &amp; Address of Employer:", lbl_style),
         P("Pythian &mdash; [employer address / city, India]")],
        [P("Position Held:", lbl_style), P("Consultant")],
        [P("Date of Appointment:", lbl_style), P("May 2022")],
        [P("Notice Required:", lbl_style), P("None (role has ended)")],
    ], [160, 320]))
    e.append(Spacer(1, 3))
    e.append(Paragraph("Main Duties and Responsibilities:", lbl_style))
    e.append(Paragraph(
        "Provided client-facing and administrative support, working with data, "
        "systems and detailed records. Entered and checked information "
        "accurately, used databases and spreadsheets to record, monitor and "
        "retrieve key information, and identified and resolved discrepancies. "
        "Managed multiple tasks and deadlines methodically, working "
        "independently and as part of a supportive team. Promoted within four "
        "months for reliability, accuracy and work ethic.", body_style))

    # Section 2a
    e.append(Paragraph("Section 2a &ndash; Employment History", sec_style))
    e.append(hr())
    e.append(grid([
        ["Employer Name &amp; Address", "Position / Main Duties", "From", "To", "Reason for Leaving"],
        ["Pythian\n[address / city, India]",
         "Consultant &ndash; administrative and data support; records, databases and spreadsheets.",
         "2022 / 05", "2023 / 08",
         "I was asked to relocate, which was not possible for me at that time."],
    ], [110, 150, 45, 45, 130]))

    # Section 3
    e.append(Paragraph("Section 3 &ndash; Educational History and Qualifications", sec_style))
    e.append(hr())
    e.append(grid([
        ["College / University etc.", "Dates Attended", "Qualifications"],
        ["Brunel University London", "Jan 2026 &ndash; Apr 2027", "MSc Artificial Intelligence (ongoing)"],
        ["JNTU Hyderabad, India", "2018 &ndash; 2022", "BTech Computer Science &amp; Engineering &mdash; First Class"],
        ["Page Junior College, Hyderabad, India", "[2016] &ndash; 2018",
         "Higher Secondary Certificate (Class 12, equivalent to UK A-Levels)"],
    ], [170, 90, 220]))
    e.append(Paragraph("Other Relevant Courses: &mdash;", val_style))

    # Section 4
    e.append(Paragraph("Section 4 &ndash; Accreditation / Registration (if applicable)", sec_style))
    e.append(hr())
    e.append(Paragraph("Not applicable (this is an administrative role).", val_style))

    # Section 5
    e.append(Paragraph("Section 5 &ndash; Skills, Knowledge and Experience", sec_style))
    e.append(hr())
    for para in [
        "I am applying for the Database &amp; Payments Administrator role "
        "because it matches my skills well and because I would value "
        "contributing to a service that makes an important difference to the "
        "local community.",
        "I have excellent attention to detail, particularly when entering and "
        "checking data, and I take real care to keep records accurate. At "
        "Pythian I worked extensively with databases and spreadsheets to "
        "record, monitor and retrieve key information, and I regularly "
        "identified and followed up on discrepancies to make sure records were "
        "complete and correct &mdash; experience that fits closely with "
        "reconciling payments and maintaining accurate attendance and payment "
        "records at EACS.",
        "I am numerate and work to a high level of accuracy, and I am confident "
        "using Microsoft Excel, Word and Outlook. As a current MSc Artificial "
        "Intelligence student with a First Class degree in Computer Science, I "
        "am very comfortable learning new systems quickly, so I would get to "
        "grips with CORE Net and SumUp reconciliation without difficulty.",
        "I am methodical and organised, able to prioritise my workload and stay "
        "effective under pressure, and I communicate clearly and sensitively "
        "&mdash; which I would bring to liaising with volunteer counsellors to "
        "resolve queries. I work well independently and on my own initiative, "
        "while also enjoying being part of a small, supportive team. I fully "
        "understand the importance of confidentiality, especially where records "
        "relate to people's care.",
        "While I do not yet have direct experience in counselling services, I "
        "have a genuine interest in the voluntary and charitable sector and in "
        "supporting services that improve people's wellbeing. I would be proud "
        "to help EACS run smoothly behind the scenes.",
    ]:
        e.append(Paragraph(para, body_style))

    # Section 6 - Disclosure
    e.append(Paragraph("Section 6 &ndash; Disclosure", sec_style))
    e.append(hr())
    e.append(Paragraph(
        "Have you ever, or are you currently, the subject of any criminal, "
        "civil investigatory or disciplinary proceedings, enquiries or "
        "cautions? &nbsp;&nbsp; <b>No</b>", val_style))
    e.append(Paragraph(
        "Have you ever been refused / expelled from membership of any "
        "professional body / register or training course? &nbsp;&nbsp; "
        "<b>No</b>", val_style))

    # Section 6 - References
    e.append(Paragraph("Section 6 &ndash; References", sec_style))
    e.append(hr())
    e.append(grid([
        ["", "First Referee", "Second Referee"],
        ["Name", "Dr Fotios Spyridonis", "Dr Matloob [surname]"],
        ["Address", "Brunel University London,\nKingston Lane, Uxbridge, UB8 3PH",
         "Brunel University London,\nKingston Lane, Uxbridge, UB8 3PH"],
        ["Job Title", "Senior Lecturer in Computer Science",
         "[Lecturer / role at Brunel]"],
        ["Capacity in which\nyou know referee", "Course Tutor", "Lecturer / Tutor"],
        ["Tel No", "[ ]", "[ ]"],
        ["Email Address", "[fotios.spyridonis@brunel.ac.uk &ndash; confirm]",
         "[matloob....@brunel.ac.uk &ndash; confirm]"],
    ], [90, 180, 180]))

    # Section 7 - Availability
    e.append(Paragraph("Section 7 &ndash; Availability", sec_style))
    e.append(hr())
    e.append(Paragraph(
        "The position is for 12 hours per week, within EACS's core office "
        "hours of 9am&ndash;4pm, Monday to Thursday. I am available on "
        "<b>Mondays and Tuesdays</b> and happy to agree a consistent weekly "
        "pattern within these hours. Please note I am <b>unable to work "
        "Wednesdays and Thursdays due to university classes</b>; I am flexible "
        "around this and can discuss the best arrangement.", body_style))

    # Section 8 - Declaration
    e.append(Paragraph("Section 8 &ndash; Declaration", sec_style))
    e.append(hr())
    e.append(Paragraph(
        "I hereby certify that all the information given by me on this form is "
        "correct to the best of my knowledge, that all the questions relating "
        "to me have been accurately and fully answered, and that I possess all "
        "the qualifications which I claim to hold.", body_style))
    e.append(Spacer(1, 6))
    e.append(kv([
        [P("Signature:", lbl_style), P("Sara Qureishi"),
         P("Date:", lbl_style), P("[date of sending]")],
    ], [70, 200, 50, 150]))

    doc.build(e)
    print("Wrote", path)


if __name__ == "__main__":
    build("/projects/sandbox/job-search/Sara_Qureishi_EACS_Application_Form.pdf")
