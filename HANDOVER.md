# Sara's Part-Time Job Search — Handover Document

**Purpose:** This doc hands over Sara's part-time job hunt to a new AI assistant so it can continue seamlessly. Read this first.

_Last updated: end of session, late October 2026._

---

## 1. Who Sara is (candidate profile)

- **Name:** Sara Qureishi (full: Sara Muzaffar Qureishi)
- **Phone:** 07760 584657
- **Email:** sara.qureishi24@gmail.com (also uses sara.mqureishi@gmail.com — she emailed EACS from the mqureishi one; pick the one she asks for, otherwise default to sara.qureishi24@gmail.com)
- **Address:** 34 The Ridgeway, North Harrow, HA2 7QN
- **Status:** International student, eligible to work in the UK **up to 20 hours/week during term time** (student visa). This 20-hour cap is a HARD limit — never suggest or write anything above it.
- **Date of birth:** 24 April 2000

### Education
- **MSc Artificial Intelligence**, Brunel University London — ongoing (approx Jan 2026 to Apr 2027; confirm exact dates with her)
- **BTech Computer Science and Engineering**, JNTU Hyderabad, India — **First Class** (2018–2022, CGPA 6.73, officially "First Class" on consolidated transcript)
- **Secondary (Class 12 / Higher Secondary Certificate)** — Page Junior College, Hyderabad (finished 2018); Class 10 at Niraj Public School, Hyderabad. Treat as **equivalent to UK GCSEs/A-Levels**.

### Work experience (IMPORTANT — see note below)
- **Pythian** — Consultant / "Analytics Consultant", Data Practice. **May 2022 – August 2023.** Real work: supported SAP HANA Cloud migration (600+ calculation views/database objects), ETL processes (reduced processing time 28%), data validation/testing, client interaction/requirements gathering. **Promoted within 4 months.** Reason for leaving: asked to relocate, which was not possible at the time.
- **TEQBIT** — Technical Consultant. **August 2023 – January 2026.** DevOps/Kubernetes/Alibaba; led a client demo (SCCC Alibaba); multi-cluster/GitOps.

### Other involvement (useful for CVs)
- **Event volunteer** — community/PostgreSQL meetup, 50+ attendees (registration, welcoming, parking, prizes). Sponsored by Pythian.
- **Acknowledged contributor** — Artificial Intelligence Review (Springer, 2026), credited for validating empirical testing on a research paper.
- Attended Brunel CS PhD Symposium 2026.

---

## 2. CRITICAL rules & preferences (follow these exactly)

1. **Experience to show:** Sara decided to **use Pythian ONLY** on most CVs (≈1 year). **Do NOT write "3 years" / "3+ years"** anywhere — that was an early mistake, now fixed. The ONLY exception: the **Cochani** CV, where she asked to ADD TEQBIT back.
2. **Job criteria:** part-time (~20 hrs/week max), **communication-based**. She prefers **no heavy labour, no serving/waiting, no alcohol venues**. Some light physical retail (stock, shelves) is OK — she confirmed "some physical work is fine" but asked things not be too heavy to lift.
3. **Availability:** available Fri, Sat, Sun, Mon, Tue. **NOT available Wednesdays or Thursdays (university classes).** Flexible mornings/afternoons/evenings/weekends.
4. **Writing style for CVs & letters:** **simple, medium-level English** (not too fancy, not too basic). **NO em-dashes (—)** anywhere. Keep it warm and genuine.
5. **Honesty:** only put things that are TRUE and provable. She's careful about this (e.g. corrected the GCSE issue, the 30-day challenge, etc.). Never invent experience or grades.
6. **NI number:** she was asked for her National Insurance number by a shop. **Advised NOT to share it** until there's a formal job offer/onboarding. Keep this stance.
7. **"First Class" on BTech:** keep it on most CVs (it's a strength). She asked to REMOVE it on **Miniso** and **Cochani** only.
8. **CV format:** clean one-page PDF — centred navy name, centred contact line, centred section headings with a horizontal rule, dated job titles, bullet points. Built with Python + reportlab (scripts in repo).

---

## 3. How the CVs are built (technical)

- Each CV is a Python script `make_cv_<name>.py` using **reportlab** (`pip install "reportlab<4.1"` — the sandbox runs Python 3.9, and reportlab 4.1+ needs 3.10+, so pin `<4.1`).
- Run: `python3 make_cv_<name>.py` → outputs `Sara_Qureishi_CV_<Name>.pdf`.
- The sandbox resets between sessions, so reportlab must be reinstalled each time.
- A new AI can just edit the `.py` and re-run, or write fresh ones in the same style.

---

## 4. Applications status (as of handover)

| Employer | Role | Location | Status / Notes |
|----------|------|----------|----------------|
| **Miniso** | Sales Assistant | (local) | ✅ **Interview DONE.** Awaiting outcome. |
| **EACS (Ealing Abbey Counselling Service)** | Database & Payments Administrator | Ealing W5 | Application form + CV + cover letter prepared. Submit to **martine@eacs.org.uk** by **9am Thu 5 Nov**. Needs: 2 referees (Dr Fotios Spyridonis + Dr Matloob, both Brunel), Pythian address, sign/date. 12 hrs/wk, Mon–Thu 9–4. |
| **Pandora** | Seasonal Sales & Operations Assistant | Brent Cross / Westfield | CV done. Applied (she was filling the form). £14.55/hr. |
| **HRUC (Harrow/Richmond/Uxbridge College)** | Administrator, Creative Arts | Uxbridge | CV + selection-criteria answers done. 17 hrs/wk term-time, Tue+Fri required (fits her). Closes ~12 Oct (may be gone now). |
| **Cochani** (perfume shop, The Pavilions, Uxbridge) | Sales Assistant (December part-time) | Uxbridge | CV done (TEQBIT included). Met a manager in person; sent WhatsApp + CV; he said he'd let her know for December. |
| **CSA (airport travel retail)** | Sales Consultant (part-time) | Heathrow | CV + emails done. Met **Michael Odish** (Michael.Odish@csatr.uk) at careers fair. Applied to info@csatr.uk + emailing Michael separately. |
| **GAP (NEXT group)** | Sales Associate | Wembley Outlet | CV done. Shifts Sun/Mon/Fri = 12.5 hrs, no Wed/Thu (great fit). Apply before 30 Oct. |
| **Parkview Surgery** | Receptionist/Administrator | Uxbridge UB8 | CV + essential/desirable criteria answers + qualification answers + Pythian "key tasks" done. Needs their **application form** too. Closes **5 Nov**, interviews **10 Nov**. 16.5 hrs/wk. EMIS Web/Docman desirable. |
| **Penshurst Gardens Surgery** | Administrator/Receptionist | Edgware HA8 | CV done. £12.21/hr, 15–25 hrs. Some Wed/Fri shifts (flag Wed). Closes **30 Nov**. |
| **Connected Kerb** | Customer Service Support Coordinator | Soho (hybrid) | CV done. 3 days/wk, patterns Mon–Wed or Wed–Fri (both include Wed — flag her Wed clash). Strong fit otherwise. |
| **Mercedes-Benz Temple Fortune (Sytner)** | Receptionist/Host | Temple Fortune NW11 | CV done. Part-time patterns available. |
| Card Factory, OFFICE, WHSmith, Inditex (Zara group), Smyths Toys | Sales Assistant roles | various (Uxbridge/Wembley/Watford/Brent Cross) | CVs done, tailored. Smyths & Inditex are more physical (warehouse/stock) — she's OK with some of that. |

### Roles deliberately SKIPPED (against her rules — don't suggest these)
- **ETM Group Head Host** — bar/hospitality, full-time, serving/alcohol.
- **Cinemas (Vue/Cineworld/Odeon)** — involve food/drink serving + cleaning.
- **Wembley Stadium / OVO Arena stewarding** — labour/security, event-only.
- **Gym Personal Trainer** — needs qualifications.
- **Apprentice retail roles (e.g. some Superdrug)** — require NOT being in education.

---

## 5. CVs available in this repo (all tailored, all PDF)

Master (all-purpose, for careers fairs/walk-ins), Pandora, HRUC Admin, EACS, Card Factory, OFFICE, WHSmith, Inditex, Smyths, GAP, CSA, Miniso, Cochani, Connected Kerb, Mercedes, Parkview, Penshurst, Sherlock (Sherlock Holmes Museum visitor assistant).

Plus: EACS application form (PDF), EACS cover letter (PDF + md), and several dated job-search lists (`*_2026-10-*.md`).

---

## 6. Honest job-search method used (keep doing this)

- **Searching:** used live web search to pull Indeed/employer result pages. Be honest with Sara: we return search *pages*, not a guaranteed "posted in last 24 hours" feed. The reliable trick is telling her to click **"Date posted → Last 24 hours"** on Indeed.
- **Best sources:** official store careers pages, Indeed (filtered to her areas), Google Jobs alerts, Heathrow/airport careers, GP surgery NHS jobs.
- **Her target areas:** Harrow, Wembley, Uxbridge, Ruislip, Greenford, Watford, Brent Cross, central London.
- She wanted an easy way to get job lists daily — the honest answer is job alerts (she sets them up), and the AI pulls fresh filtered search links on request.

---

## 7. What the new AI should do next

1. Keep applying to communication-based part-time roles in her areas (≤20 hrs/wk, no serving/alcohol/heavy-labour).
2. For each new role: build/tailor a CV in the same style (simple English, no em-dashes, Pythian-only unless she says otherwise), and help with application questions/cover letters.
3. Chase outstanding ones: **EACS form (by 5 Nov)**, **Parkview form (by 5 Nov)**, **GAP (by 30 Oct)**, **Penshurst (by 30 Nov)**, follow up **Cochani** and **CSA/Michael**.
4. Remind her to line up **2 referees** (Dr Fotios Spyridonis + Dr Matloob at Brunel — she needs their Brunel emails; ask them first).
5. Always keep her **20-hour visa limit** and **no Wed/Thu** in mind.

---

*Built with help from Kiro across multiple sessions. All CVs/letters are drawn from Sara's real, verifiable background.*
