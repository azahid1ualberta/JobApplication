# -*- coding: utf-8 -*-
"""26 October 2026 daily run: Dillon Consulting Senior Project Manager, Transportation/Traffic
Engineering & Roadway Safety (4483555546 Toronto; same ad at eight other Ontario offices)."""

import content20
from content3 import (NAME, CONTACT, MOTT, UOFA, resume)
from content19 import (OPENTRACK, CVT, CLI, DASHBOARD, TOOLS_SENTENCE, city, metrolinx, skills,
                       BRIEFING, PROJECTS, COORD, REVIEW_DEV, DATA_KPI, TOOLING)
from content20 import (TTS, REPORTS, AGENCIES, letter)

content20.DATE = "October 26, 2026"

RESUME_4483555546 = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner in Transportation "
    "Planning with the City of Toronto, reviewing development applications and their transportation "
    "studies and analyzing travel survey data. Previously simulated Ontario Line construction staging "
    "in Synchro at Mott MacDonald and assessed rail service effects at Metrolinx.",
    city(REVIEW_DEV, TTS, DASHBOARD, PROJECTS, COORD, BRIEFING)
    + metrolinx(CVT, CLI, OPENTRACK) + MOTT + UOFA,
    skills=skills("Synchro, VISSIM, OpenTrack and MATSim. Transportation planning and development review. "
                  "Travel survey and network data analysis. ArcGIS Pro, QGIS, AutoCAD and Civil 3D. "
                  "Python, SQL and JavaScript. MS Office."))

COVER_4483555546 = letter(
    "Hiring Team", "Integrated Mobility", "Dillon Consulting Limited",
    "Re: Senior Project Manager - Transportation/Traffic Engineering & Roadway Safety (Toronto)",
    "Dear Hiring Team,",
    [
        "I would like to be considered for the Senior Project Manager position in Traffic Engineering and "
        "Roadway Safety. I am an Assistant Planner in Transportation Planning at the City of Toronto, with "
        "a master's degree in transportation engineering from the University of Alberta, and I am "
        "interested in consulting work on traffic, corridor and transportation master plan studies.",

        "At the City I review development applications and the transportation studies filed with them, "
        "analyze Transportation Tomorrow Survey data, and write the briefing notes that carry findings "
        "and options to senior staff. I also advise on right-of-way questions, and I built the city-wide "
        "right-of-way width dataset. At Mott MacDonald I simulated Ontario Line construction staging and "
        "road closures in Synchro, and I have also worked in VISSIM, MATSim and OpenTrack. I use GIS, "
        "AutoCAD, Python and SQL day to day.",

        TOOLS_SENTENCE,

        "I should be straightforward about the gaps. The posting asks for ten years of experience, a P.Eng. "
        "or eligibility for registration, and business development and leadership capability. I have about "
        "four and a half years of relevant experience and am not registered with Professional Engineers "
        "Ontario, as an EIT or otherwise. I have reviewed traffic impact studies rather than written them for "
        "clients, and I have not led road safety audits, parking studies or Vision Zero programs, written "
        "proposals, managed project budgets, supervised staff, or worked in business development. I am "
        "applying because traffic analysis, modelling and transportation planning is where my experience "
        "sits, and I would like to grow toward a lead role.",

        "Thank you for considering my application.",
    ])
