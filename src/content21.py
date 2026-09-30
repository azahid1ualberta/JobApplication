# -*- coding: utf-8 -*-
"""Stantec — Project Manager, Transportation Engineering & Planning (Req 1007868)."""

from content3 import (NAME, CONTACT, MOTT, UOFA, resume)
from content19 import (OPENTRACK, SLOW, CVT, CLI, DASHBOARD, TOOLS_SENTENCE, city, metrolinx, skills)
from content20 import (TTS, DEV_STUDIES, REPORTS, AGENCIES, letter)

RESUME_1007868 = resume(
    "Transportation engineer with a master's degree and experience on the public side of the "
    "consultant relationship: currently an Assistant Planner with the City of Toronto reviewing development "
    "applications and their transportation studies, previously with Metrolinx and Mott MacDonald. Works in "
    "Synchro, VISSIM, MATSim, OpenTrack, ArcGIS and Python, and writes technical reports that turn model "
    "results into recommendations.",
    city(DEV_STUDIES, TTS, REPORTS, AGENCIES, DASHBOARD)
    + metrolinx(OPENTRACK, SLOW, CVT, CLI) + MOTT + UOFA,
    skills=skills("Synchro, VISSIM, MATSim and OpenTrack. ArcGIS and QGIS. Python (Pandas, NumPy) and SQL. "
                  "Review of traffic impact and transportation studies against Ontario municipal standards. "
                  "Technical reports, memoranda and presentations. MS Office (Word, Excel, PowerPoint, Teams)."))

COVER_1007868 = letter(
    "Talent Acquisition", "Transportation Planning & Traffic Engineering", "Stantec Consulting Ltd., Markham, ON",
    "Re: Project Manager - Transportation Engineering & Planning (Req ID 1007868)", "Dear Hiring Manager,",
    [
        "I would like to apply for the Project Manager, Transportation Engineering and Planning position with "
        "the Transportation Planning and Traffic Engineering team in Markham or Toronto. My work so far has been "
        "on the public side of transportation planning, and consulting is where I would like to take it.",

        "The posting lists traffic impact studies, construction staging plans, and surface transit lines and "
        "stations among the team's work. At the City of Toronto I review development applications and the "
        "transportation studies filed with them against City standards, so I know what a municipal reviewer "
        "looks for in a traffic impact study and where submissions tend to fall short. At Mott MacDonald I ran "
        "traffic simulations to estimate how Ontario Line construction staging would affect the surrounding "
        "streets, and at Metrolinx I ran OpenTrack simulations of GO rail services and assessed what "
        "temporary and permanent speed restrictions would do to service.",

        "Of the software the posting names, I have worked with Synchro, VISSIM, ArcGIS and Python, as well as "
        "MATSim and OpenTrack. " + TOOLS_SENTENCE + " I write the technical reports, memos and presentations "
        "that carry findings to decision-makers, and I coordinate with agencies, consultants and applicants "
        "whose priorities often conflict.",

        "I should be straightforward about the gaps. The posting asks for eight or more years of transportation "
        "experience, including five or more in project management, business development and proposal "
        "preparation. I have closer to four years, and I have not managed consulting projects, prepared "
        "proposals, or handled project budgets and invoicing. I have not used Aimsun, EMME, TransCAD, VISUM or "
        "HCS, and I do not hold a P.Eng. If the team is also hiring at the transportation planner or engineer "
        "level, I would welcome being considered for that role.",

        "Thank you for considering my application.",
    ])
