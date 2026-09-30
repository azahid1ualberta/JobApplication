# -*- coding: utf-8 -*-
"""Airport civil design roles (September 2026):

    Dillon  Airport Design Engineer (Oakville, hybrid)
    WSP     Civil Project Engineer - Aviation (85226)
"""

from content3 import (MOTT, UOFA, resume)
from content19 import (REVIEW_ENG, PROJECTS, COORD, BRIEFING, CAPITAL, DASHBOARD,
                       OPENTRACK, SLOW, CVT, CLI, TOOLS_SENTENCE, city, metrolinx, skills)
from content20 import letter

RESUME_CIVIL = resume(
    "Civil engineer with a master's degree in transportation engineering, currently an Assistant Planner with "
    "the City of Toronto. Reviews engineering submissions, consultant drawings and studies against standards, "
    "coordinates schedules and deliverables across consultants and agencies, and brings modelling and Python "
    "automation to technical analysis.",
    city(REVIEW_ENG, PROJECTS, COORD, CAPITAL, BRIEFING, DASHBOARD)
    + metrolinx(OPENTRACK, SLOW, CVT, CLI) + MOTT + UOFA,
    skills=skills("Review of engineering submissions, drawings and specifications. Project coordination, "
                  "scheduling and follow-through. Traffic and rail modelling: VISSIM, Synchro, MATSim and "
                  "OpenTrack. Python (Pandas, NumPy) and SQL. ArcGIS and QGIS. Technical reports and "
                  "presentations. MS Office."))


# ================================================ Dillon Airport Design Engineer

COVER_DILLON = letter(
    "Talent Acquisition", "Airports", "Dillon Consulting Limited, Oakville, ON",
    "Re: Airport Design Engineer", "Dear Hiring Manager,",
    [
        "I would like to apply for the Airport Design Engineer position, based in Oakville or another Dillon "
        "office. I am a civil engineer and an Assistant Planner with the City of Toronto, and I want to be clear "
        "from the start that I come to this from transportation planning and analysis rather than airside "
        "design.",

        "Some of the project management side of the role is familiar. The posting describes tracking open items "
        "with consultants and coordinating scope, schedule and technical inputs across teams. At the City I "
        "review engineering submissions, consultant drawings and studies against City standards, recommend "
        "conditions where something is missing, and run assigned projects from scoping through to "
        "recommendations while holding the schedule myself. I coordinate with divisions, consultants and outside "
        "agencies whose priorities conflict, and I write the reports and briefing notes that carry decisions "
        "upward.",

        "The posting also says Dillon wants its teams to automate the routine so they can focus on "
        "problem-solving. That is how I work. " + TOOLS_SENTENCE,

        "The gaps are significant. I am not a licensed Professional Engineer and have not registered with PEO. "
        "I do not have five years in airport engineering, civil design or site development; I have not done "
        "airside design or airfield pavement work, applied ICAO or FAA standards, or used AutoCAD, MicroStation, "
        "AviPLAN, SkySafe or AutoTURN; and I have not managed budgets or taken infrastructure through "
        "construction. If Dillon's airport team has a junior or intermediate role where I could build that "
        "experience, I would welcome being considered for it.",

        "Thank you for considering my application.",
    ])


# ================================================ WSP Civil Project Engineer - Aviation

COVER_WSP_AVIATION = letter(
    "Talent Acquisition", "Aviation", "WSP Canada, Ontario",
    "Re: Civil Project Engineer - Aviation (Job ID 85226)", "Dear Hiring Manager,",
    [
        "I would like to apply for the Civil Project Engineer position with the Aviation team in Ontario. I am "
        "a civil engineer and an Assistant Planner with the City of Toronto, and I come to airport work from "
        "transportation planning, so I want to be clear about both what I would bring and where I fall short.",

        "Several of the listed responsibilities connect to my current work. I review engineering submissions, "
        "specifications, consultant drawings and studies against City standards, and recommend conditions where "
        "something is missing. I prepare technical reports and presentation materials, liaise with consultants, "
        "applicants and agencies to resolve issues, and run assigned projects to schedule. The posting lists "
        "experience with modelling tools as an advantage: I have worked with VISSIM, Synchro, MATSim and "
        "OpenTrack.",

        TOOLS_SENTENCE + " At the City I built the Transportation Data Dashboard, bringing several years of data "
        "into one validated source the division reports from.",

        "The gaps are real. I am not a licensed Professional Engineer and have not registered with PEO. I have "
        "closer to four years of engineering experience in Canada than five, none of it in aviation. I have not "
        "designed airport infrastructure, worked to TP312, ICAO or FAA standards, prepared quantity take-offs or "
        "cost estimates, carried out construction field reviews, or used AutoCAD or Civil 3D. I am applying "
        "because the review and coordination side of the role is familiar, and I would welcome being considered "
        "at a more junior level if that would suit the team better.",

        "Thank you for considering my application.",
    ])
