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

Add a row to `README.md` for each application. When he sends postings in chat, deliver a
**zip** with `SendUserFile`. The **daily run** delivers to Google Drive and pushes to GitHub
(both approved by him on 5 October 2026).

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

## Daily job search — runs every day at ~11 AM Toronto time

Approved by him on 5 October 2026: cost OK, results to Google Drive as dated folders, push to
GitHub. Each run is a fresh session; this file is the whole procedure.

**Drive (Google Drive connector; folder owned by packplug.review@gmail.com, writable):**

| What | Drive ID |
|---|---|
| `Applications` folder — create one subfolder per run named `YYYY-MM-DD` | `1noa0PTUzD__Gc0BN2JN60cD-GmlzX6SE` |
| `Job Tracker.xlsx` — **update this file in place** each run | `1dnINTddvyJzyCT15cS0EnhWJoxl5IiLR` |
| `criteria.md` — **download fresh each run**; he edits it in Drive | `13dQfEXijktFf8tHnTW0tkgJlrpJPQPsb` |
| `seen_jobs.txt` — update in place each run | `1OFPc9dUbkXHMliWCAP02O7amQkg09hu8` |
| `Resume_Content.md` — his facts; download fresh each run | `124FiwrAmVrkeNAcDGCWYIf3FIlPsPbaJ` |

Public download also works without the connector:
`https://drive.google.com/uc?export=download&id=<ID>`.

**Procedure:**

1. Setup: `pip install reportlab fonttools pymupdf openpyxl`; `python src/fetch_fonts.py` if
   `src/fonts/` is empty. Download `criteria.md` and `Resume_Content.md` from Drive into
   `job-search/` (Drive is the source of truth — he edits them there).
2. Search per `criteria.md`: priority employers first (City of Toronto `jobs.toronto.ca`,
   TTC, Peel, York, Durham, Mississauga, Brampton, Metrolinx, the consultancies), then
   WebSearch. Metrolinx's portal and Indeed/WSP block automated reads — use mirrors (Glassdoor,
   LinkedIn public pages, aggregators) and say so. **Never** log in anywhere.
3. Skip anything whose URL is already seen (`python job-search/tracker.py seen URL`), anything
   expired or unverifiable, and every title the criteria list as a downgrade. Aim for the
   strongest 10–15. Never fabricate a posting.
4. For each job: save the posting text as `Job Description - <Company> - <Role>.pdf`; write
   `src/content<N>.py` following the existing ones; build resume + letter with `fit()`; write
   `APPLICATION-NOTES.md`. All writing rules above apply — gaps paragraph, no invented facts,
   Crew Variance Tool and command line workflow (except his old Metrolinx team).
5. Check every PDF is one page and render a sample to PNG to eyeball it.
6. Tracker: add one row per job with `python job-search/tracker.py add row.json` (14 columns;
   Status `New`; "Why It Matches" = 2–4 plain sentences ending with honest flags). This also
   appends to `seen_jobs.txt`.
7. Drive: create folder `YYYY-MM-DD` under `Applications`; upload per job
   `Resume - <Company> - <Role>.pdf`, `Cover Letter - <Company> - <Role>.pdf`,
   `Job Description - <Company> - <Role>.pdf`, `Notes - <Company> - <Role>.md`
   (`disableConversionToGoogleType: true` for all). Update `Job Tracker.xlsx` and
   `seen_jobs.txt` in place. Add `Run Summary - YYYY-MM-DD.md`: jobs found (title, company,
   closing date, verdict), and **every source that could not be read** — an unreadable source
   is a finding, never a silence.
8. GitHub: `git add -A`, commit, push to `claude/tailored-resume-cover-letters-t2n8vx`.
9. If nothing qualifies, still write the run summary saying so and which sources were checked.
