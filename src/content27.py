# -*- coding: utf-8 -*-
"""10 October 2026 run: HDR Transportation Planner (Toronto), York Region Service Planner,
Metrolinx Project Manager, Adjacent Construction Review."""

import content20
from content3 import (NAME, CONTACT, MOTT, UOFA, resume)
from content19 import (OPENTRACK, SLOW, CVT, CLI, DASHBOARD, TOOLS_SENTENCE, city, metrolinx, skills,
                       REVIEW_DEV, BRIEFING, PROJECTS, COORD, SCHED, DATA_KPI)
from content20 import (TTS, DEV_STUDIES, REPORTS, AGENCIES, letter, VALIDATED)

content20.DATE = "October 10, 2026"

# ---------------------------------------------------------------- HDR
RESUME_HDR = resume(
    "Transportation engineer with a master's degree and four years of work across municipal transportation "
    "planning at the City of Toronto and rail service simulation at Metrolinx. Reviews the transportation "
    "studies behind development applications, analyzes travel data and builds the Python and GIS tooling "
    "behind the analysis.",
    city(TTS, DEV_STUDIES, DASHBOARD, REPORTS, AGENCIES)
    + metrolinx(OPENTRACK, SLOW, CVT, CLI) + MOTT + UOFA,
    skills=skills("Synchro, VISSIM, OpenTrack and MATSim. ArcGIS Pro, QGIS and MapBox. Python (Pandas, NumPy) "
                  "and SQL. AutoCAD and Civil 3D. Advanced Excel. Travel data analysis and visualization; "
                  "technical reports and presentations."))

COVER_HDR = letter(
    "Talent Acquisition", "Transportation", "HDR, Toronto, ON",
    "Re: Transportation Planner (Toronto)", "Dear Hiring Manager,",
    [
        "I would like to apply for the Transportation Planner position in Toronto. I am an Assistant Planner "
        "in Transportation Planning with the City of Toronto, and before that I was a Transportation Planner "
        "at Metrolinx, where I worked on GO rail service simulation. I hold a master's degree in "
        "Transportation Engineering.",

        "At the City I review the transportation studies filed with development applications and analyze "
        "travel data, including several years of the Transportation Tomorrow Survey, then write up what I find "
        "for planners and engineers in other divisions. I have run traffic simulations in Synchro, and I work "
        "in ArcGIS Pro, QGIS and Python. " + TOOLS_SENTENCE,

        "I should be straightforward about the gaps. My consulting experience is limited to a short period at "
        "Mott MacDonald in early 2023, where I did traffic simulation of Ontario Line construction staging. "
        "I have not worked on Municipal Class Environmental Assessments or Transit Project Assessment Process "
        "studies, and I have not used EMME, VISUM or Aimsun. I have no experience writing proposals or "
        "attending public meetings for a consultant's client. I am not registered with PEO, so I am not an EIT "
        "or a P.Eng. today.",

        "Thank you for considering my application.",
    ])

# ---------------------------------------------------------------- York Region
RESUME_YORK = resume(
    "Transportation engineer with a master's degree and four years across GO rail service planning at "
    "Metrolinx and municipal transportation planning at the City of Toronto. Analyzes travel data to see "
    "where service falls short, reviews development applications for what they mean for "
    "transportation, and writes the memos that carry recommendations to decision-makers.",
    city(TTS, DEV_STUDIES, DATA_KPI, REPORTS, DASHBOARD)
    + metrolinx(OPENTRACK, VALIDATED, SCHED, CVT, CLI) + MOTT + UOFA,
    skills=skills("OpenTrack, TrainPlan, Synchro, VISSIM and MATSim. ArcGIS Pro, QGIS and MapBox. Python "
                  "(Pandas, NumPy) and SQL. Advanced Excel. Service and network analysis; development "
                  "application review; memos and presentations."))

COVER_YORK = letter(
    "Human Resources", "", "The Regional Municipality of York, Richmond Hill, ON",
    "Re: Service Planner, Transit Planning", "Dear Hiring Manager,",
    [
        "I would like to apply for the Service Planner position with Transit Planning. I am an Assistant "
        "Planner in Transportation Planning with the City of Toronto, and before that I was a Transportation "
        "Planner at Metrolinx, where I planned and simulated GO rail services.",

        "At Metrolinx I ran OpenTrack simulations to establish what proposed operating changes would do to "
        "run times and reliability, and worked with schedulers and operations staff to settle the variables a "
        "service plan rested on. At the City I review development applications and the transportation studies "
        "filed with them, analyze travel data including the Transportation Tomorrow Survey, and write the "
        "memos that carry comments and recommendations to other divisions, which is close to the memo and "
        "development review work in the posting. " + TOOLS_SENTENCE,

        "I should be straightforward about the gaps. My service planning has been on rail, not bus: I have "
        "not designed bus routes, set running and recovery times for a bus network, or used transit scheduling "
        "software such as Hastus. I have not worked with ridership data such as passenger loads and on-off "
        "counts, and I have not run public information sessions on annual transit plans. My direct service planning "
        "experience is about a year at Metrolinx, short of the posting's two-year minimum; the rest of my four "
        "and a half years is transportation planning at the City.",

        "Thank you for considering my application.",
    ])

# ---------------------------------------------------------------- Metrolinx ACR
RESUME_ACR = resume(
    "Transportation engineer with a master's degree and four years across rail planning at Metrolinx and "
    "municipal transportation planning at the City of Toronto, where the daily work is reviewing "
    "development applications and the studies filed with them. Coordinates divisions, consultants and "
    "outside agencies toward a position everyone can act on.",
    city(DEV_STUDIES, AGENCIES, PROJECTS, BRIEFING, TTS)
    + metrolinx(OPENTRACK, SLOW, CVT, CLI) + MOTT + UOFA,
    skills=skills("Review of development applications and transportation studies; coordination of "
                  "multi-party technical review; briefing notes and presentations. OpenTrack, Synchro and "
                  "VISSIM. ArcGIS Pro, QGIS and MapBox. Python and SQL. AutoCAD and Civil 3D. Advanced Excel."))

COVER_ACR = letter(
    "Talent Acquisition", "Integrated Delivery Division", "Metrolinx, 20 Bay Street, Toronto, ON",
    "Re: Project Manager, Adjacent Construction Review - Adjacent Development", "Dear Hiring Manager,",
    [
        "I would like to be considered for the Project Manager, Adjacent Construction Review position. I am "
        "an Assistant Planner in Transportation Planning with the City of Toronto, and from February 2023 to "
        "January 2024 I was a Transportation Planner at Metrolinx, so I know the operating railway the "
        "corridor protection work is meant to safeguard.",

        "At the City, much of my work is reviewing development applications and the transportation studies "
        "filed with them, recommending conditions where something is missing, and working issues through "
        "with divisions, consultants, applicants and outside agencies whose priorities conflict. At Metrolinx "
        "I assessed the effect of temporary and permanent slow orders, which are what construction beside an "
        "operating railway imposes. " + TOOLS_SENTENCE,

        "I should be straightforward about the gaps. I am not a Registered Professional Planner and I do not "
        "hold a PMP. I have not managed third-party agreements or construction agreements, supervised staff, "
        "or written terms of reference or tender documents for consultants. I do not have a Class G licence, "
        "and I have not taken the Canadian Rail Operating Rules course. My review experience is on the "
        "municipal side of the Planning Act process, not the transit-agency side, and I have not enforced "
        "permit conditions on site.",

        "Thank you for considering my application.",
    ])
