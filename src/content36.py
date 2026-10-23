# -*- coding: utf-8 -*-
"""23 October 2026 daily run: City of Hamilton Senior Project Manager, Mobility Planning (4482702306)."""

import content20
from content3 import (NAME, CONTACT, MOTT, UOFA, resume)
from content19 import (OPENTRACK, CVT, CLI, DASHBOARD, TOOLS_SENTENCE, city, metrolinx, skills,
                       BRIEFING, PROJECTS, COORD, REVIEW_DEV, DATA_KPI, TOOLING)
from content20 import (TTS, REPORTS, AGENCIES, letter)

content20.DATE = "October 23, 2026"

RESUME_4482702306 = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner in Transportation "
    "Planning with the City of Toronto, reviewing development applications and their transportation "
    "studies, analyzing travel survey data and writing briefing notes. Previously assessed rail service "
    "effects at Metrolinx and simulated Ontario Line construction staging at Mott MacDonald.",
    city(REVIEW_DEV, TTS, DASHBOARD, PROJECTS, COORD, BRIEFING)
    + metrolinx(CVT, CLI, OPENTRACK) + MOTT + UOFA,
    skills=skills("Transportation planning and development review. Travel survey and network data analysis. "
                  "Python, SQL and JavaScript. ArcGIS Pro, QGIS, AutoCAD and Civil 3D. "
                  "Synchro, VISSIM, OpenTrack and MATSim. MS Office."))

COVER_4482702306 = letter(
    "Hiring Manager", "Transportation Planning Section, Planning and Economic Development",
    "City of Hamilton",
    "Re: Job ID #32289, Senior Project Manager, Mobility Planning",
    "Dear Hiring Manager,",
    [
        "I would like to apply for the Senior Project Manager, Mobility Planning position. I am an Assistant "
        "Planner in Transportation Planning at the City of Toronto, with a master's degree in transportation "
        "engineering from the University of Alberta, and the work in this posting is close to what I do now.",

        "At the City I review development applications and the transportation studies filed with them, "
        "analyze Transportation Tomorrow Survey data, and write the briefing notes that carry issues and "
        "options to senior staff. I run assigned projects from scoping through to recommendations, "
        "coordinating divisions, consultants and outside agencies whose priorities do not always line up. "
        "I also built the Transportation Data Dashboard, which brought several survey years into one "
        "validated source. Earlier, at Metrolinx, I simulated GO rail operations in OpenTrack, and at Mott "
        "MacDonald I worked on Ontario Line construction staging, so I have seen regional transit planning "
        "from the provincial side.",

        TOOLS_SENTENCE,

        "I should be straightforward about the gaps. I have not supervised or directed a team of project "
        "managers, and I have not managed a section budget, written RFPs or administered consultant "
        "contracts. I have not run public engagement to IAP2 standards, and my work on Environmental "
        "Assessments and Complete Streets guidelines has been limited. I do not hold an MCIP, RPP, C.E.T. "
        "or P.Eng. designation, and I do not have a Class G licence. I am applying because the "
        "transportation planning, development review and data work is where my experience sits.",

        "Thank you for considering my application.",
    ])
