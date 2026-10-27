# -*- coding: utf-8 -*-
"""27 October 2026 daily run: City of Edmonton, General Supervisor, Program Management (ID 56127).

Safe Mobility section (Vision Zero). Closes Nov 5, 2026, 11:59 PM ABT. Leads Program Management and
Planning & Monitoring teams (about 40 staff).
"""

import content20
from content3 import (MOTT, UOFA, resume)
from content19 import (OPENTRACK, SLOW, CVT, CLI, DASHBOARD, city, metrolinx, skills, PROJECTS)
from content20 import (TTS, AGENCIES, letter)
from content28 import (ROW, POLICY_COUNCIL, TOOLS_ALSO)

content20.DATE = "October 27, 2026"

RESUME_56127 = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner in Transportation Planning "
    "with the City of Toronto. Builds the datasets and dashboards that turn travel data into evidence for "
    "decisions, and runs assigned projects from scoping to recommendations.",
    city(DASHBOARD, PROJECTS, AGENCIES, ROW, POLICY_COUNCIL)
    + metrolinx(OPENTRACK, SLOW, CVT, CLI) + MOTT + UOFA,
    skills=skills("Mobility data analysis and validation. Project planning and follow-through. Briefing notes and "
                  "reports for senior staff. Synchro and VISSIM. ArcGIS Pro, QGIS and MapBox. Python and SQL."))

COVER_56127 = letter(
    "Hiring Manager", "General Supervisor, Program Management (ID 56127)", "Safe Mobility, City of Edmonton",
    "Re: General Supervisor, Program Management (ID 56127)", "Dear Hiring Manager,",
    [
        "I would like to be considered for the General Supervisor, Program Management position in Safe "
        "Mobility. I am an Assistant Planner in Transportation Planning at the City of Toronto. I did my master's "
        "degree in transportation engineering at the University of Alberta, and I note that the section works "
        "closely with the University on research.",

        "The part of the role that connects evidence to action is the part closest to my work. At the City I "
        "built the Transportation Data Dashboard, which brings several years of the Transportation Tomorrow "
        "Survey into one validated source, and I analyze travel and network data to show where capacity falls "
        "short and what that means for investment. I also maintain the road and right-of-way datasets the "
        "division depends on. I run assigned projects from scoping through to recommendations, holding the "
        "schedule myself and coordinating with divisions, consultants and agencies whose priorities conflict, "
        "and I write the briefing notes that carry the findings to senior staff and, with policy staff, report to "
        "Council on new transportation regulations.",

        "At Metrolinx I ran OpenTrack simulations of GO rail services and assessed what temporary and permanent "
        "slow orders would do to service. " + TOOLS_ALSO + " Earlier, at the University of Alberta, I modelled "
        "evacuation traffic for wildfire emergencies.",

        "I should be straightforward about the gaps. This is a leadership role over about forty people, including "
        "people leaders, and I have never supervised staff, let alone led leaders. I have not managed a "
        "capital or operating budget, or run multi-year portfolio forecasting and governance. I have not worked "
        "on Vision Zero, road safety engineering, traffic calming or traffic signals, and I have not worked in "
        "Edmonton's municipal environment. I do not hold a P.Eng. or PMP, which the posting lists as assets. What "
        "I can offer is a sound grounding in transportation data and project work, and I would need to learn "
        "the rest.",

        "Thank you for considering my application.",
    ])
