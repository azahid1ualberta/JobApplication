# -*- coding: utf-8 -*-
"""13 October 2026 catch-up: senior roles the daily runs missed between 13 September and
12 October (the finder had no GIS keywords and no employer sweeps)."""

import content20
from content3 import (NAME, CONTACT, MOTT, UOFA, resume)
from content19 import (OPENTRACK, SLOW, CVT, CLI, DASHBOARD, TOOLS_SENTENCE, city, metrolinx, skills,
                       REVIEW_DEV, BRIEFING, PROJECTS, COORD, SCHED, DATA_KPI, IMPROVE, CAPITAL)
from content20 import (TTS, DEV_STUDIES, REPORTS, AGENCIES, letter, VALIDATED, OT_BUILD)

content20.DATE = "October 13, 2026"

ROW = ("B: Build and maintain the road and right-of-way datasets the division depends on, using GIS and Python, "
       "including a ROW-width dataset covering all city roads, built with QGIS, MapBox and JavaScript.")
STUDIES = ("B: Run assigned studies from scoping through to recommendations, writing the briefing notes that come "
           "out of them and presenting to planners, engineers and managers in other divisions.")
EVIDENCE = ("B: Worked with schedulers, operations staff and engineers on service design decisions and presented "
            "the evidence behind them.")
TOOLS_ALSO = ("I also set up a command line workflow that pre-simulated slow orders in batches, cutting turnaround "
              "on scenario requests from days to hours, and built the Crew Variance Tool, a Python application "
              "that read large JSON operations files and summarised speed profiles and run-time variance across "
              "subdivisions.")
UOFA_GIS = [
    "SUB: Graduate Research Assistant",
    "DATE: University of Alberta  |  January 2020 – August 2022",
    "B: Master's research on how road networks perform during emergency evacuations, using macroscopic (LWR) "
    "and agent-based (MATSim) models.",
    "B: Spatial analysis of large transportation datasets in GIS, turning data into recommendations for safer "
    "wildfire evacuation plans in Alberta communities.",
]


# ================================================ Metrolinx Engineering Lead - GIS

RESUME_MX_GIS = resume(
    "Transportation engineer with a master's degree and four years of GIS and data work across municipal "
    "transportation planning at the City of Toronto and GO rail service planning at Metrolinx. Builds the "
    "spatial datasets a division depends on and turns scattered sources into one validated source people "
    "report from.",
    city(ROW, DASHBOARD, TTS, STUDIES)
    + metrolinx(OPENTRACK, CVT, CLI, EVIDENCE) + MOTT + UOFA_GIS,
    skills=skills("ArcGIS Pro, QGIS and MapBox. Python (Pandas, NumPy), SQL and JavaScript for spatial data "
                  "processing and automation. Data integration, validation and dashboards. OpenTrack, VISSIM, "
                  "Synchro and MATSim. AutoCAD and Civil 3D. Advanced Excel, including large multi-source "
                  "workbooks. Briefing notes and presentations for senior staff."))

COVER_MX_GIS = letter(
    "Talent Acquisition", "Engineering & Safety Division", "Metrolinx, 20 Bay Street, Toronto, ON",
    "Re: Engineering Lead - Geographic Information Systems (GIS)", "Dear Hiring Manager,",
    [
        "I would like to apply for the Engineering Lead, Geographic Information Systems position in the "
        "Engineering and Safety Division. I worked at Metrolinx in 2023 as a Transportation Planner in Service "
        "Design, and since January 2024 I have been an Assistant Planner in Transportation Planning at the City "
        "of Toronto, where much of my work is building and looking after the spatial data the division relies on.",

        "At the City I build and maintain the road and right-of-way datasets Transportation Planning depends "
        "on, using GIS and Python, including a right-of-way width dataset covering all city roads, built with "
        "QGIS, MapBox and JavaScript. I also built the Transportation Data Dashboard, which combined several "
        "years of Transportation Tomorrow Survey data into one validated source the division now reports from. "
        "The posting describes bringing location, condition, performance and project information together so "
        "that decisions rest on one consistent picture of the network. That is the problem I have been "
        "working on, at the scale of one division.",

        "At Metrolinx I saw the railway from the operations side. I ran OpenTrack simulations of GO rail "
        "services to test how infrastructure constraints and speed restrictions changed run times and "
        "reliability, and presented that evidence to schedulers, operations staff and engineers. " + TOOLS_ALSO
        + " My master's thesis used GIS and macro-simulation to assess community "
        "transportation capacity for wildfire evacuation.",

        "I should be straightforward about the gaps. I have not led a GIS program or set geospatial "
        "governance, standards and data models for an organization; my GIS work has been building and "
        "maintaining datasets and tools within one division. I have not worked in asset management or State "
        "of Good Repair planning, integrated GIS with an enterprise asset management system, or led staff, "
        "consultants or vendors, and I do not hold a professional certification. I am applying because the "
        "spatial analysis and data integration at the centre of the role is the work I do now.",

        "Thank you for considering my application.",
    ])
