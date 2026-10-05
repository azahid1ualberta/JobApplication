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

- **Assistant Planner, Transportation Planning, City of Toronto** — Jan 2024–present. Reviews
  development applications and their transportation studies against City standards and
  Official Plan policy; road and right-of-way datasets (GIS, Python); Transportation Data
  Dashboard (several years of data, one validated source); briefing notes, memos; coordination
  with divisions, consultants, applicants, agencies; runs assigned projects end to end.
- **Transportation Planner, Simulation and Modelling, Metrolinx Service Design** — Feb 2023–Jan
  2024. OpenTrack simulation of GO rail; slow-order assessment; run-time variance analysis;
  the two tools above.
- **Graduate Transportation Planner, Mott MacDonald** — Jan–Feb 2023. Ontario Line construction
  staging traffic simulation.
- **Graduate Research Assistant, University of Alberta** — 2020–2022. Evacuation network
  modelling with LWR and MATSim.
- **Education:** MSc Transportation Engineering (UAlberta, 2022); BSc Civil Engineering (BUET,
  2018); BSc Computer Science (UBC, in progress 2025–2027).
- **Does not have:** P.Eng. or EIT (not registered with PEO), Class G licence, PMP, CROR, staff
  supervision, budget management, procurement/contract administration, Power BI, R, VBA,
  AutoCAD/Civil 3D.
