# -*- coding: utf-8 -*-
"""Metrolinx — Senior Advisor, Strategy, Planning & Partnerships, found 7 October 2026."""

import content20
from content3 import (NAME, CONTACT, MOTT, UOFA, resume)
from content19 import (OPENTRACK, SLOW, CVT, CLI, DASHBOARD, TOOLS_SENTENCE, city, metrolinx, skills)
from content20 import (TTS, DEV_STUDIES, REPORTS, AGENCIES, letter)

content20.DATE = "October 7, 2026"

RESUME_MX_SPP = resume(
    "Transportation engineer with a master's degree and four years across GO rail service planning at "
    "Metrolinx and municipal transportation planning at the City of Toronto. Analyzes travel and network data "
    "to show where capacity falls short, builds the Python and GIS tooling behind the analysis, and writes the "
    "briefing notes and presentations that carry findings to decision-makers.",
    city(TTS, DASHBOARD, REPORTS, DEV_STUDIES, AGENCIES)
    + metrolinx(OPENTRACK, SLOW, CVT, CLI) + MOTT + UOFA,
    skills=skills("Python (Pandas, NumPy) and SQL for analysis and automation. OpenTrack, Synchro, VISSIM and MATSim. "
                  "ArcGIS Pro, QGIS and MapBox. Advanced Excel, including large multi-source workbooks. "
                  "Adobe Photoshop and Illustrator. Briefing notes, technical reports and presentations."))

COVER_MX_SPP = letter(
    "Talent Acquisition", "Strategy, Planning & Partnerships", "Metrolinx, 97 Front Street West, Toronto, ON",
    "Re: Senior Advisor, Strategy, Planning & Partnerships", "Dear Hiring Manager,",
    [
        "I would like to apply for the Senior Advisor, Strategy, Planning & Partnerships position. I worked at "
        "Metrolinx for a year as a Transportation Planner in Simulation and Modelling, and I would like to be "
        "considered for a role closer to the investment questions that sit behind that work.",

        "The posting describes technical analysis of the trade-offs and benefits of transit investments, and "
        "deliverables that senior management can read quickly. At Metrolinx I ran OpenTrack simulations of GO "
        "rail services to test how infrastructure constraints and speed restrictions changed run times and "
        "schedule reliability, and I presented that evidence to schedulers, operations staff and engineers. At "
        "the City of Toronto I analyze travel and network data, including several years of the Transportation "
        "Tomorrow Survey, to work out where capacity is short and what that means for future investment, and I "
        "write the briefing notes that come out of it.",

        TOOLS_SENTENCE + " I work in Python, SQL, ArcGIS Pro and QGIS, and Excel, and I have built the "
        "dashboards and datasets that my division reports from.",

        "I should be straightforward about the gaps. I have not built investment-grade business cases or "
        "ridership forecasts, and I have not done formal cost-benefit analysis; my work has been on the "
        "operations, network-data and review side. I have not used EMME, TransCAD or VISUM, or R, STATA or SAS. "
        "I would be glad to be considered on the strength of the analytical work above and my master's degree "
        "in transportation engineering.",

        "Thank you for considering my application.",
    ])
