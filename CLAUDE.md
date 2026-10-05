# Job applications for Abdullah Al Zahid — how to work in this repo

Read this before producing any resume, cover letter or notes. The person has approved this
exact format and voice; do not drift from it.

## What a finished application is

One folder per job under `applications/<Org>-<Role>-<JobID>/` with:

- `Abdullah_Al_Zahid_Resume.pdf` — **one page**
- `Abdullah_Al_Zahid_Cover_Letter.pdf` — **one page**
- `APPLICATION-NOTES.md` — for him, not the employer: posting facts table (division, location,
  type, pay, posted, closes), an honest verdict, a qualifications table ("where you stand"),
  what the documents do, before-you-apply tips, priority

Add a row to `README.md` for each application. Deliver as a **zip** with `SendUserFile`.
Do not push to GitHub unless he asks (he asked for zips instead, October 2026).

## How to build the PDFs

- Content lives in `src/content<N>.py` as tagged lines (`NAME:`, `CONTACT:`, `H2:`, `SUB:`,
  `DATE:`, `P:`, `PLT:`, `B:`, `SIGN:`, `SPACE:`). Shared blocks are in `src/content3.py`;
  reusable bullets in `src/content19.py`; the `letter()` helper in `src/content20.py`.
- Render with `src/pdfbuilder3.py`. Use `fit()` from `src/generate19.py`, which tries
  resume sizes 9.4pt @ 0.68in, 9.3 @ 0.68, 9.3 @ 0.62, 9.3 @ 0.55, 9.2 @ 0.55 and letters at
  10pt @ 0.85in, keeping the first that holds one page. See `src/generate21.py` for a template.
- Fonts: `python src/fetch_fonts.py` once after cloning (Comfortaa, Nunito, Style Script).
- The spacing constants in `pdfbuilder3.py` are calibrated to his approved August documents.
  **Do not change them.** If a resume will not fit at 9.3pt, trim *new* content you wrote,
  never content he approved, and never go below 9.2pt — he said 9.2 reads too small.
- Render to PNG and look at both pages before delivering.

## Writing rules

- **Never invent experience.** Everything comes from his real record (below). If unsure, leave it out.
- **Every cover letter has a gaps paragraph** that names plainly what he does not have
  ("I should be straightforward about the gaps..."). No qualification-mapping lists — he
  rejected those as AI-sounding.
- **Modest, natural register.** "I would like to apply / be considered for", "that was the
  shape of my work". No hype, no buzzwords.
- **Crew Variance Tool and command line workflow:** include them for every employer *except*
  Metrolinx GO Expansion Operations / Service Design (his old team), where he asked to leave
  them out. Do not remove other content to make room.
- **Exact wording of those two items:** "Built the Crew Variance Tool, a Python application
  that read large JSON operations files and produced summaries of speed profiles and run-time
  variance across subdivisions." / "Set up a command line workflow so temporary and permanent
  slow orders could be pre-simulated in batches, cutting turnaround on scenario requests from
  days to hours."
- City of Toronto letters go to the named HR contact: "Dear <Full Name>," — do not guess Mr./Ms.
- Dates: postings saying "12:00 AM" on day X effectively close at the end of day X-1. Say so.
- Do not state he would relocate; that is his decision.

## His facts (do not go beyond these)

**Master source: `job-search/Resume_Content.md`** (carried over from the previous automation,
built from his own April 2026 resume). Nothing outside that file may appear on a resume or
letter. Key points:

- **Assistant Planner, Transportation Planning, City of Toronto** — Jan 2024–present.
  Development applications and their transportation studies; TTS analysis; Transportation Data
  Dashboard (2006/2011/2016 TTS, one validated source); road and right-of-way datasets incl. a
  ROW-width dataset for all city roads (QGIS, MapBox, JavaScript); briefing notes; advising on
  by-laws and regulations.
- **Transportation Planner, Simulation and Modelling, Metrolinx Service Design** — Feb 2023–Jan
  2024. OpenTrack; slow-order assessment; the two tools above.
- **Graduate Transportation Planner, Mott MacDonald** — Jan–Feb 2023. Ontario Line construction
  staging and road-closure traffic simulation **in Synchro**.
- **Graduate Research Assistant, University of Alberta** — 2020–2022. Evacuation modelling
  (LWR, MATSim); GIS analysis for wildfire evacuation plans.
- **Education:** MSc Transportation Engineering (UAlberta, 2022, CGPA 4.0/4.0); BSc Civil
  Engineering (BUET, 2018, CGPA 3.69/4.0); BSc Computer Science (UBC, part-time, 2025–2027).
- **Tools he has:** OpenTrack, TrainPlan, VISSIM, Synchro, MATSim; Python, SQL, JavaScript;
  ArcGIS Pro, QGIS, MapBox; **AutoCAD, Civil 3D**; Excel; Adobe Photoshop/Illustrator, Blender.
  (An earlier version of this file wrongly listed AutoCAD/Civil 3D as gaps — corrected Oct 2026.)
- **Awards and publications** are in `Resume_Content.md`; include only when there is room.
- **Does not have:** P.Eng. or EIT (not registered with PEO), Class G licence, PMP, CROR, staff
  supervision, budget management, procurement/contract administration, Power BI, R, VBA.

## Daily job search (carried over from the previous automation)

- Search rules: `job-search/criteria.md` — Planner grade is the **floor**; skip Assistant,
  Junior, EIT, Technician, "Analyst 1" titles; judge the work, not the title.
- De-duplicate against `job-search/seen_jobs.txt`; append each new posting URL.
- Tracker: `job-search/Job_Tracker.xlsx`, same 14 columns as the old one.
