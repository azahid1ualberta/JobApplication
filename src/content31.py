# -*- coding: utf-8 -*-
"""16 October 2026 daily run: City of Toronto Project Manager, Transportation Services (Job ID 67209)."""

import content20
from content3 import (NAME, CONTACT, MOTT, UOFA, resume)
from content19 import (OPENTRACK, CVT, CLI, DASHBOARD, TOOLS_SENTENCE, city, metrolinx, skills,
                       BRIEFING, PROJECTS, COORD, REVIEW_DEV, RESEARCH, DATA_KPI)
from content20 import (TTS, DEV_STUDIES, REPORTS, AGENCIES, letter)

content20.DATE = "October 16, 2026"

BYLAW = ("B: Advise on by-laws and regulations that bear on the City's roads and right-of-way.")

RESUME_67209 = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner with the City of Toronto's "
    "Transportation Planning division. Analyzes travel and network data, reviews development applications and "
    "their transportation studies, advises on by-laws and regulations, and writes the briefing notes and "
    "reports that carry findings to senior staff.",
    city(TTS, DEV_STUDIES, PROJECTS, BRIEFING, BYLAW, AGENCIES)
    + metrolinx(OPENTRACK, CVT, CLI) + MOTT + UOFA,
    skills=skills("Transportation planning analysis, TTS and travel data. Traffic and rail simulation: VISSIM, "
                  "Synchro, MATSim and OpenTrack. Python (Pandas, NumPy), SQL and advanced Excel. ArcGIS Pro, QGIS, "
                  "AutoCAD. Briefing notes, reports and presentations. MS Office."))

COVER_67209 = letter(
    "Hiring Manager", "Vision Zero Strategy, Transportation Services", "City of Toronto",
    "Re: Project Manager, Transportation Services (Job ID 67209)", "Dear Hiring Manager,",
    [
        "I would like to be considered for the Project Manager, Transportation Services position in the Vision "
        "Zero Strategy unit. I am an Assistant Planner in Transportation Planning at the City, and the parts of "
        "this role that match my experience are the transportation data analysis, the work with other divisions "
        "and consultants, and the reporting to senior staff.",

        "At the City I analyze travel and network data, including several years of the Transportation Tomorrow "
        "Survey, and I review development applications and the transportation studies filed with them against "
        "City standards. I advise on by-laws and regulations that bear on the street network, and I write the "
        "briefing notes and reports that carry findings to senior staff. I coordinate with divisions, "
        "consultants and outside agencies whose priorities conflict, and I run assigned projects from scoping "
        "through to recommendations. Before that, at Metrolinx, I assessed rail operating changes in OpenTrack, "
        "and at Mott MacDonald I modelled road closures in Synchro.",

        TOOLS_SENTENCE,

        "I should be straightforward about the gaps. I have not worked in road safety, so I know Vision Zero and "
        "Safe System principles from reading rather than from practice, and I have not analyzed collision data. "
        "I have not procured or administered consultant contracts or been accountable for a project budget, "
        "and I have not supervised staff. I do not hold a P.Eng. or RPP designation. I am applying because "
        "the analysis, coordination and writing underneath the role are what I do each day, and I would like to "
        "grow into project leadership in this field.",

        "Thank you for considering my application.",
    ])
