# -*- coding: utf-8 -*-
"""15 October 2026 daily run: City of Mississauga Project Leader, Transportation (Req 28672);
CMHC Specialist, Geographic Information Systems (Req 12565)."""

import content20
from content3 import (NAME, CONTACT, MOTT, UOFA, resume)
from content19 import (OPENTRACK, CVT, CLI, DASHBOARD, TOOLS_SENTENCE, city, metrolinx, skills,
                       BRIEFING, PROJECTS, COORD, SCHED, REVIEW_DEV, RESEARCH, DATA_KPI)
from content20 import (TTS, DEV_STUDIES, REPORTS, AGENCIES, letter)

content20.DATE = "October 15, 2026"

ROW = ("B: Build and maintain the road and right-of-way datasets the division depends on, using GIS and Python, "
       "including a ROW-width dataset covering all city roads, built with QGIS, MapBox and JavaScript.")
BYLAW = ("B: Advise on by-laws and regulations that bear on the City's roads and right-of-way.")

# ================================================ Mississauga Project Leader, Transportation

RESUME_MSG = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner with the City of Toronto's "
    "Transportation Planning division. Analyzes travel and network data, reviews development applications and "
    "their transportation studies, advises on by-laws and regulations, and writes the briefing notes and "
    "reports that carry transportation findings to senior staff.",
    city(TTS, DEV_STUDIES, BRIEFING, BYLAW, AGENCIES)
    + metrolinx(OPENTRACK, CVT, CLI) + MOTT + UOFA,
    skills=skills("Transportation planning analysis, TTS and travel data. Traffic and rail simulation: VISSIM, "
                  "Synchro, MATSim and OpenTrack. Python (Pandas, NumPy), SQL and advanced Excel. ArcGIS Pro, QGIS. "
                  "Briefing notes, corporate-style reports and presentations. MS Office."))

COVER_MSG = letter(
    "Hiring Manager", "Transportation Planning", "City of Mississauga, Transportation and Works Department",
    "Re: Project Leader, Transportation (Req ID 28672)", "Dear Hiring Manager,",
    [
        "I would like to apply for the Project Leader, Transportation position in Transportation Planning. I am "
        "an Assistant Planner in Transportation Planning at the City of Toronto, and the work you describe, "
        "studies and policy that support a multi-modal transportation plan, is the work I do now at a smaller "
        "scale.",

        "At the City I analyze travel and network data, including several years of the Transportation Tomorrow "
        "Survey, to show where capacity falls short. I review development applications and the transportation "
        "studies filed with them against City standards and Official Plan policy, advise on by-laws and "
        "regulations, and write the briefing notes and reports that carry findings to senior staff. I "
        "coordinate with divisions, consultants and outside agencies whose priorities conflict, and I run "
        "assigned projects from scoping through to recommendations. Before that, at Metrolinx, I used OpenTrack "
        "to assess rail operating changes, and at Mott MacDonald I modelled road closures for Ontario Line "
        "construction staging in Synchro.",

        TOOLS_SENTENCE,

        "I should be straightforward about the gaps. I have about four and a half years of experience, "
        "counting my graduate research, which is short of the five the posting asks for. I am not a registered professional "
        "engineer or a member of the Ontario Professional Planners Institute. I have not led a Transportation "
        "Master Plan or a Development Charges background study, I have not worked on the Class Environmental "
        "Assessment process. I am applying because the "
        "analysis and writing underneath the role are what I do each day, and I would welcome the chance to "
        "take on the project leadership.",

        "Thank you for considering my application.",
    ])

# ================================================ CMHC Specialist, Geographic Information Systems

RESUME_CMHC = resume(
    "Transportation engineer with a master's degree and part way through a computer science degree, currently "
    "an Assistant Planner with the City of Toronto. Builds and maintains spatial datasets and the tooling "
    "around them using GIS and Python, brings several sources into one validated dataset, and documents the "
    "result for the analysts who rely on it.",
    city(ROW, DASHBOARD, "B: Build and maintain the datasets and tooling Transportation Planning depends on, "
         "using Python and GIS.", TTS, BRIEFING)
    + metrolinx(CVT, CLI, OPENTRACK, SCHED) + MOTT + UOFA,
    skills=skills("Spatial data and GIS: ArcGIS Pro, QGIS, MapBox. Python (Pandas, NumPy), SQL and JavaScript. "
                  "Dataset validation and documentation. Dashboards and data visualization. Advanced Excel. "
                  "Reports, briefing notes and presentations. MS Office."))

COVER_CMHC = letter(
    "Hiring Manager", "Survey Data Processing", "Canada Mortgage and Housing Corporation, Ottawa, ON",
    "Re: Specialist, Geographic Information Systems (Requisition 12565)", "Dear Hiring Manager,",
    [
        "I would like to apply for the Specialist, Geographic Information Systems position on the Survey Data "
        "Processing team. My background is in transportation planning, and the part of it that overlaps with "
        "your role is geospatial data: building it, checking it and making it usable for analysts.",

        "At the City of Toronto I build and maintain the road and right-of-way datasets that Transportation "
        "Planning depends on, including a right-of-way width dataset covering all city roads, built with QGIS, "
        "MapBox and JavaScript. I also built the Transportation Data Dashboard, which brought several years of "
        "survey data into one validated source the division reports from. I work in ArcGIS Pro and QGIS and "
        "write Python and SQL for the data work. I explain data to the people who use it through briefing "
        "notes and presentations.",

        TOOLS_SENTENCE,

        "I should be straightforward about the gaps. I have not administered enterprise GIS licensing or "
        "ArcGIS Enterprise, and I have not worked with SAS or R. I have not managed vendors, set a data "
        "quality audit methodology, or estimated resources for a large project, and I have no experience with "
        "housing or market survey data. My experience is about four and a half years. The role would be in "
        "Ottawa and I am in Toronto, which I raise only so you have the full picture. I am applying because "
        "geospatial data work is the part of my experience I would most like to grow.",

        "Thank you for considering my application.",
    ])
