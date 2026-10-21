# -*- coding: utf-8 -*-
"""21 October 2026 daily run: TTC Senior Project Engineer (13718), Artelia Team Lead Mobility and ITS (4480740696)."""

import content20
from content3 import (NAME, CONTACT, MOTT, UOFA, resume)
from content19 import (OPENTRACK, CVT, CLI, DASHBOARD, TOOLS_SENTENCE, city, metrolinx, skills,
                       BRIEFING, PROJECTS, COORD, REVIEW_DEV, DATA_KPI, CAPITAL)
from content20 import (TTS, DEV_STUDIES, REPORTS, AGENCIES, letter)

content20.DATE = "October 21, 2026"

# ---------------------------------------------------------------- TTC 13718
RESUME_13718 = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner with the City of Toronto, "
    "where assigned projects run from scoping to recommendations. Coordinates consultants, divisions and "
    "outside agencies, tracks the work against schedule, and writes the briefing notes that carry issues and "
    "options to senior staff. Previously simulated GO rail operations at Metrolinx.",
    city(PROJECTS, COORD, REVIEW_DEV, BRIEFING, DASHBOARD, CAPITAL)
    + metrolinx(OPENTRACK, CVT, CLI) + MOTT + UOFA,
    skills=skills("Project coordination across consultants and divisions. Reports, presentations and briefing "
                  "materials. Python, SQL and advanced Excel. ArcGIS Pro, QGIS, AutoCAD and Civil 3D. Synchro, "
                  "VISSIM and OpenTrack. MS Office."))

COVER_13718 = letter(
    "Hiring Manager", "Major Projects", "Toronto Transit Commission",
    "Re: Senior Project Engineer, Waterfront East Rapid Transit Line (Requisition 13718)",
    "Dear Hiring Manager,",
    [
        "I would like to apply for the Senior Project Engineer position on the Waterfront East Rapid Transit "
        "Line. I am an Assistant Planner in Transportation Planning at the City of Toronto, with a master's "
        "degree in transportation engineering. The part of the posting I can speak to is the coordination: "
        "keeping several parties working from the same information and moving toward the same decision.",

        "At the City I run assigned projects from scoping through to recommendations. I plan the work, hold the "
        "schedule, and report progress to the people relying on it, while working with other divisions, "
        "consultants and outside agencies whose priorities do not always line up. I review development "
        "applications and the studies filed with them, and I write the briefing notes and presentations that "
        "put issues and options in front of senior staff. Earlier, at Metrolinx, I ran OpenTrack simulations "
        "of GO rail services to establish what proposed changes would do to run times and reliability before "
        "they were taken forward, and at Mott MacDonald I worked on Ontario Line construction staging.",

        TOOLS_SENTENCE,

        "I should be straightforward about the gaps. I have not delivered a major capital project from design "
        "through construction, and I have not managed a project budget, a formal risk register or a critical "
        "path schedule. The posting asks for five years of delivering complex infrastructure projects, and my "
        "experience is shorter than that and closer to planning and analysis than to delivery. I do not hold a "
        "P.Eng. I am applying because the coordination, reporting and stakeholder work is close to what I "
        "already do, and a transit expansion on the waterfront is work I would like to contribute to.",

        "Thank you for considering my application.",
    ])

# ---------------------------------------------------------------- Artelia 4480740696
RESUME_4480740696 = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner with the City of Toronto, "
    "reviewing development applications and their transportation studies and analyzing travel and network "
    "data. Previously ran traffic simulations at Mott MacDonald and rail simulations at Metrolinx. Builds the "
    "Python and GIS tools that analysis depends on.",
    city(DEV_STUDIES, TTS, PROJECTS, COORD, DASHBOARD, REPORTS)
    + metrolinx(OPENTRACK, CVT, CLI) + MOTT + UOFA,
    skills=skills("Traffic analysis and simulation in Synchro, VISSIM, OpenTrack and MATSim. Transportation "
                  "studies and technical reporting. Python, SQL and JavaScript. ArcGIS Pro, QGIS, AutoCAD and "
                  "Civil 3D. MS Office."))

COVER_4480740696 = letter(
    "Hiring Manager", "Mobility and Intelligent Transportation Systems", "Artelia Canada, Mississauga",
    "Re: Team Lead, Mobility and ITS",
    "Dear Hiring Manager,",
    [
        "I would like to be considered for the Team Lead position in Mobility and Intelligent Transportation "
        "Systems. I am an Assistant Planner in Transportation Planning at the City of Toronto, with a master's "
        "degree in transportation engineering. My work is on the planning and analysis side of transportation, "
        "and I am writing knowing that this is a senior role and that I am earlier in my career than it asks.",

        "At the City I review development applications and the transportation studies filed with them against "
        "City standards, analyze travel and network data, including the Transportation Tomorrow Survey, and run "
        "assigned projects from scoping to recommendations. At Mott MacDonald I ran traffic simulations in "
        "Synchro to estimate how Ontario Line construction staging would affect surrounding streets, and at "
        "Metrolinx I simulated GO rail operations in OpenTrack. My graduate research modelled evacuation "
        "traffic on road networks.",

        TOOLS_SENTENCE,

        "I should be straightforward about the gaps. The posting asks for ten years in transportation planning "
        "or traffic engineering and I have fewer than four. I have not led a team of engineers and technicians, "
        "managed project budgets, prepared proposals or worked on client business development. I have not done "
        "intelligent transportation systems or highway design work, and I am not a registered professional "
        "engineer. I am applying because the analysis and study work is close to what I do now, and I would "
        "understand if the role needs someone further along.",

        "Thank you for considering my application.",
    ])
