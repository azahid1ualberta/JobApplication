# -*- coding: utf-8 -*-
"""24 October 2026 daily run: Mosaic Mobility Group Transportation Engineer (4482304673)."""

import content20
from content3 import (NAME, CONTACT, MOTT, UOFA, resume)
from content19 import (OPENTRACK, CVT, CLI, DASHBOARD, TOOLS_SENTENCE, city, metrolinx, skills,
                       BRIEFING, PROJECTS, COORD, REVIEW_DEV, DATA_KPI, TOOLING)
from content20 import (TTS, REPORTS, AGENCIES, letter)

content20.DATE = "October 24, 2026"

RESUME_4482304673 = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner in Transportation "
    "Planning with the City of Toronto, reviewing development applications and their transportation "
    "studies and analyzing travel survey data. Previously simulated Ontario Line construction staging "
    "in Synchro at Mott MacDonald and assessed rail service effects at Metrolinx.",
    city(REVIEW_DEV, TTS, DASHBOARD, PROJECTS, COORD, BRIEFING)
    + metrolinx(CVT, CLI, OPENTRACK) + MOTT + UOFA,
    skills=skills("Transportation planning and development review. Travel survey and network data analysis. "
                  "Synchro, VISSIM, OpenTrack and MATSim. Python, SQL and JavaScript. "
                  "ArcGIS Pro, QGIS, AutoCAD and Civil 3D. MS Office."))

COVER_4482304673 = letter(
    "Hiring Team", "", "Mosaic Mobility Group",
    "Re: Transportation Engineer",
    "Dear Hiring Team,",
    [
        "I would like to apply for the Transportation Engineer position. I am an Assistant Planner in "
        "Transportation Planning at the City of Toronto, with a master's degree in transportation "
        "engineering from the University of Alberta, and I am interested in consulting work for "
        "municipal and private-sector clients across Ontario.",

        "At the City I review development applications and the transportation studies filed with them, "
        "analyze Transportation Tomorrow Survey data, and write the briefing notes that carry findings "
        "and options to senior staff. That is the client side of the transportation impact studies your "
        "team prepares, and it has given me a close look at what a reviewer wants to see in one. At Mott "
        "MacDonald I simulated Ontario Line construction staging and road closures in Synchro, and at "
        "Metrolinx I worked in OpenTrack on rail service questions.",

        TOOLS_SENTENCE,

        "I should be straightforward about the gaps. I am not registered with Professional Engineers "
        "Ontario as an EIT or a P.Eng. I have not worked in a consulting firm on client deliverables, and "
        "I have not done parking demand studies, traffic signal warrant analyses or collision analyses in "
        "my own work, nor have I used Arcady. I do not have a Class G licence. I am applying because the "
        "development transportation review, traffic modelling and data work is where my experience sits, "
        "and I would like to build on it in consulting.",

        "Thank you for considering my application.",
    ])
