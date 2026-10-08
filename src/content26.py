# -*- coding: utf-8 -*-
"""Halton Region — Project Manager II, Transportation Planning (Posting 5507), found 8 October 2026."""

import content20
from content3 import (NAME, CONTACT, MOTT, UOFA, resume)
from content19 import (OPENTRACK, SLOW, CVT, CLI, DASHBOARD, TOOLS_SENTENCE, city, metrolinx, skills,
                       REVIEW_DEV, BRIEFING, PROJECTS, COORD)
from content20 import (TTS, DEV_STUDIES, REPORTS, AGENCIES, letter)

content20.DATE = "October 8, 2026"

RESUME_HALTON = resume(
    "Transportation engineer with a master's degree and four years across GO rail service planning at "
    "Metrolinx and municipal transportation planning at the City of Toronto. Reviews the transportation "
    "studies behind development applications, analyzes network data to show where capacity falls short, "
    "and writes the briefing notes that carry findings to decision-makers.",
    city(TTS, DEV_STUDIES, PROJECTS, BRIEFING, DASHBOARD)
    + metrolinx(OPENTRACK, SLOW, CVT, CLI) + MOTT + UOFA,
    skills=skills("Synchro, VISSIM, OpenTrack and MATSim. ArcGIS Pro, QGIS and MapBox. Python (Pandas, NumPy) "
                  "and SQL. AutoCAD and Civil 3D. Advanced Excel. Network and corridor analysis; review of "
                  "transportation studies; briefing notes and presentations."))

COVER_HALTON = letter(
    "Human Resources", "", "Regional Municipality of Halton, 1151 Bronte Road, Oakville, ON",
    "Re: Project Manager II, Transportation Planning (Posting 5507)", "Dear Hiring Manager,",
    [
        "I would like to apply for the Project Manager II, Transportation Planning position. I am an "
        "Assistant Planner in Transportation Planning with the City of Toronto, and before that I was a "
        "Transportation Planner at Metrolinx, one of the agencies the posting says this role works with.",

        "At the City I review development applications and the transportation studies filed with them, and "
        "I analyze travel and network data, including several years of the Transportation Tomorrow Survey, to "
        "work out where capacity is short. I write the briefing notes that come out of that work and present "
        "to planners and engineers in other divisions. I have run Synchro traffic simulations and "
        "OpenTrack rail simulations, and I work in ArcGIS Pro and QGIS. " + TOOLS_SENTENCE,

        "I should be straightforward about the gaps. The posting asks for seven years of experience and a "
        "P.Eng. or C.E.T.; I have about four and a half years, and I am not registered with PEO. I have not led "
        "a Municipal Class Environmental Assessment or a region-wide corridor study, I have not used EMME, and "
        "I do not hold a PMP. I "
        "do not hold a Class G licence, which the posting requires by the first day. I am applying because the posting says "
        "equivalent combinations of education and experience will be considered, and because the work, "
        "multi-modal studies and technical review across municipal and provincial partners, is close to what "
        "I do now.",

        "Thank you for considering my application.",
    ])
