# -*- coding: utf-8 -*-
"""Stantec — Transportation Planner (Markham / Toronto), found 5 October 2026."""

import content20
from content3 import (NAME, CONTACT, MOTT, UOFA, resume)
from content19 import (OPENTRACK, SLOW, CVT, CLI, DASHBOARD, TOOLS_SENTENCE, city, metrolinx, skills)
from content20 import (TTS, DEV_STUDIES, REPORTS, AGENCIES, letter)

content20.DATE = "October 5, 2026"

RESUME_STANTEC_TP = resume(
    "Transportation engineer with a master's degree and experience on the public side of the "
    "consultant relationship: currently an Assistant Planner with the City of Toronto reviewing development "
    "applications and their transportation studies, previously with Metrolinx and Mott MacDonald. Works in "
    "Synchro, VISSIM, MATSim, OpenTrack, ArcGIS and Python, and writes technical reports that turn model "
    "results into recommendations.",
    city(DEV_STUDIES, TTS, REPORTS, AGENCIES, DASHBOARD)
    + metrolinx(OPENTRACK, SLOW, CVT, CLI) + MOTT + UOFA,
    skills=skills("Synchro, VISSIM, MATSim and OpenTrack. ArcGIS and QGIS. AutoCAD and Civil 3D. Python (Pandas, NumPy) and SQL. "
                  "Review of traffic impact and transportation studies against Ontario municipal standards. "
                  "Technical reports, memoranda and presentations. MS Office (Word, Excel, PowerPoint, Teams)."))

COVER_STANTEC_TP = letter(
    "Talent Acquisition", "Transportation Planning & Traffic Engineering", "Stantec Consulting Ltd., Markham, ON",
    "Re: Transportation Planner (Markham / Toronto)", "Dear Hiring Manager,",
    [
        "I would like to apply for the Transportation Planner position in Markham or Toronto. My work so far has "
        "been on the public side of transportation planning, and consulting is where I would like to take it.",

        "The posting describes multimodal transportation analysis, safety assessments and traffic and "
        "transportation planning projects for public and private clients across Ontario. At the City of Toronto I "
        "review development applications and the transportation studies filed with them against City standards, "
        "so I know what a municipal reviewer looks for and where submissions tend to fall short. At Mott "
        "MacDonald I ran traffic simulations in Synchro to estimate how Ontario Line construction staging would "
        "affect the surrounding streets, and at Metrolinx I ran OpenTrack simulations of GO rail services.",

        "Of the software the posting names, I have worked with Synchro, VISSIM and ArcGIS, as well as MATSim and "
        "OpenTrack. " + TOOLS_SENTENCE + " I write the technical reports, memos and presentations that carry "
        "findings to decision-makers.",

        "I should be straightforward about the gaps. The posting asks for five or more years of relevant "
        "technical experience, and I have closer to four. I have not used Aimsun or SimTraffic, I have not "
        "managed consulting projects or budgets, and I do not hold a P.Eng., PTOE, RPP or RSP designation, "
        "which the posting lists as beneficial. I would be glad to be considered on the strength of the work "
        "above and my master's degree in transportation engineering.",

        "Thank you for considering my application.",
    ])
