# -*- coding: utf-8 -*-
"""22 October 2026 daily run: Strathcona County GIS Specialist II Transportation (4481159005),
Metrolinx Senior Project Manager Hamilton LRT (4481143114)."""

import content20
from content3 import (NAME, CONTACT, MOTT, UOFA, resume)
from content19 import (OPENTRACK, CVT, CLI, DASHBOARD, TOOLS_SENTENCE, city, metrolinx, skills,
                       BRIEFING, PROJECTS, COORD, REVIEW_DEV, DATA_KPI, TOOLING)
from content20 import (TTS, REPORTS, AGENCIES, letter)

content20.DATE = "October 22, 2026"

ROW = ("B: Built and maintain the road and right-of-way datasets Transportation Planning depends on, including "
       "a right-of-way width dataset for all city roads, using QGIS, MapBox, JavaScript and Python to merge "
       "sources that were scattered across the division.")

# ---------------------------------------------------------------- Strathcona 4481159005
RESUME_4481159005 = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner with the City of Toronto, "
    "where GIS and Python are the tools behind much of the work. Builds and maintains road and right-of-way "
    "datasets, a validated data dashboard and spatial analysis for transportation planning. Earlier GIS work "
    "covered wildfire evacuation planning in Alberta communities.",
    city(ROW, DASHBOARD, TTS, DATA_KPI, PROJECTS, BRIEFING)
    + metrolinx(CVT, CLI, OPENTRACK) + MOTT + UOFA,
    skills=skills("ArcGIS Pro, QGIS and MapBox. Python, SQL and JavaScript. Spatial analysis, data validation "
                  "and dashboards. Transportation datasets and network analysis. AutoCAD and Civil 3D. "
                  "Synchro, VISSIM, OpenTrack and MATSim. MS Office."))

COVER_4481159005 = letter(
    "Hiring Manager", "Transportation Engineering and Operations", "Strathcona County",
    "Re: GIS Specialist II, Transportation",
    "Dear Hiring Manager,",
    [
        "I would like to apply for the GIS Specialist II, Transportation position. I am an Assistant Planner in "
        "Transportation Planning at the City of Toronto, with a master's degree in transportation engineering "
        "from the University of Alberta, where my thesis used GIS to study how much traffic a community's "
        "roads could carry in a wildfire evacuation.",

        "At the City, GIS and Python are how I keep the division's data usable. I build and maintain the road "
        "and right-of-way datasets that Transportation Planning depends on, including a right-of-way width "
        "dataset for all city roads, built with QGIS, MapBox and JavaScript from sources that used to be "
        "scattered. I also built the Transportation Data Dashboard, which brought several years of survey data "
        "into one validated source in place of a report rebuilt by hand each quarter. I analyze travel and "
        "network data for trends and gaps and turn the results into recommendations, and I explain them to "
        "planners and engineers who are not GIS users.",

        TOOLS_SENTENCE,

        "I should be straightforward about the gaps. My professional GIS experience is shorter than the five "
        "years the posting asks for, and it is mixed in with other planning work rather than being the whole "
        "of a role. I have not supervised or coached staff, and I do not hold a GISP or Esri certification. "
        "I have worked mainly in ArcGIS Pro and QGIS and have not administered an enterprise geodatabase or "
        "run a GIS service for a whole department. I am applying because the work is transportation data and "
        "spatial analysis, which is where my experience sits, and I would be glad to learn the rest.",

        "Thank you for considering my application.",
    ])

# ---------------------------------------------------------------- Metrolinx 4481143114
RESUME_4481143114 = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner with the City of Toronto, "
    "running assigned projects from scoping to recommendations and coordinating consultants, divisions and "
    "outside agencies. Previously assessed rail service effects at Metrolinx and simulated Ontario Line "
    "construction staging at Mott MacDonald.",
    city(PROJECTS, COORD, REVIEW_DEV, BRIEFING, DASHBOARD)
    + metrolinx(OPENTRACK, CVT, CLI) + MOTT + UOFA,
    skills=skills("Project coordination across consultants and divisions. Reports, presentations and briefing "
                  "materials. Python, SQL and advanced Excel. ArcGIS Pro, QGIS, AutoCAD and Civil 3D. "
                  "OpenTrack, Synchro and VISSIM. MS Office."))

COVER_4481143114 = letter(
    "Hiring Manager", "Capital Project Delivery", "Metrolinx",
    "Re: Senior Project Manager, Hamilton LRT",
    "Dear Hiring Manager,",
    [
        "I would like to be considered for the Senior Project Manager position on the Hamilton LRT Project. "
        "I am an Assistant Planner in Transportation Planning at the City of Toronto, with a master's degree "
        "in transportation engineering, and I worked at Metrolinx in 2023. I am writing knowing that this is a "
        "delivery role at a much more senior level than mine.",

        "At the City I run assigned projects from scoping through to recommendations. I plan the work, hold "
        "the schedule, and report progress to the people relying on it, while coordinating divisions, "
        "consultants and outside agencies whose priorities do not always line up. I review development "
        "applications and the studies filed with them, and I write the briefing notes that carry issues and "
        "options to senior staff. At Mott MacDonald I worked on Ontario Line construction staging and ran "
        "traffic simulations of the road closures it required. At Metrolinx I simulated GO rail operations in "
        "OpenTrack and assessed what construction-related slow orders do to service.",

        TOOLS_SENTENCE,

        "I should be straightforward about the gaps. I have not managed the design, procurement, construction "
        "or commissioning of a transit project. I have not administered contracts, managed contractors or a "
        "project budget, or led a team of project professionals, and I am not familiar enough with the "
        "Occupational Health and Safety Act or the Professional Engineers Act to claim working knowledge of "
        "them. I do not hold a P.Eng. I am applying because the coordination, scheduling and stakeholder work "
        "is close to what I do now, and because I would like to move toward delivering transit rather than "
        "only planning it.",

        "Thank you for considering my application.",
    ])
