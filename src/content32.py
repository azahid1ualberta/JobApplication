# -*- coding: utf-8 -*-
"""17 October 2026 daily run: Metrolinx Senior Project Manager, Third-Party Coordination (4479640432);
Arcadis Traffic Analysis Engineer, Calgary (4477770650; the Vancouver posting 4477766809 is the same text)."""

import content20
from content3 import (NAME, CONTACT, MOTT, UOFA, resume)
from content19 import (OPENTRACK, CVT, CLI, DASHBOARD, TOOLS_SENTENCE, city, metrolinx, skills,
                       BRIEFING, PROJECTS, COORD, REVIEW_DEV, RESEARCH, DATA_KPI)
from content20 import (TTS, DEV_STUDIES, REPORTS, AGENCIES, letter)

content20.DATE = "October 17, 2026"

BYLAW = ("B: Advise on by-laws and regulations that bear on the City's roads and right-of-way.")

# ---------------------------------------------------------------- Metrolinx 4479640432
RESUME_4479640432 = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner with the City of Toronto "
    "and previously a planner at Metrolinx. Coordinates divisions, consultants and outside agencies whose "
    "priorities differ, reviews development and engineering submissions, and writes the briefing notes that "
    "carry issues and options to senior staff.",
    city(DEV_STUDIES, COORD, PROJECTS, BRIEFING, BYLAW)
    + metrolinx(OPENTRACK, CVT, CLI) + MOTT + UOFA,
    skills=skills("Stakeholder and agency coordination. Review of technical submissions. Briefing notes, reports "
                  "and presentations. Traffic and rail simulation: Synchro, VISSIM and OpenTrack. Python, SQL and "
                  "advanced Excel. ArcGIS Pro, QGIS, AutoCAD, Civil 3D. MS Office."))

COVER_4479640432 = letter(
    "Hiring Manager", "Capital Projects Group, Eglinton Crosstown West Extension", "Metrolinx, 5090 Explorer Drive",
    "Re: Senior Project Manager, Third-Party Coordination",
    "Dear Hiring Manager,",
    [
        "I would like to apply for the Senior Project Manager, Third-Party Coordination position on the "
        "Eglinton Crosstown West Extension. I worked at Metrolinx through 2023 and am now an Assistant Planner "
        "in Transportation Planning at the City of Toronto, one of the authorities a project like this has to "
        "bring along. The part of the role I can speak to is the coordination between a project team and the "
        "agencies and divisions it depends on.",

        "At the City I review development applications and the transportation studies filed with them against "
        "City standards, and I work with divisions, consultants and outside agencies whose priorities conflict, "
        "taking an issue through to a resolution that each side can accept. I advise on by-laws and "
        "regulations that bear on the right-of-way, I run assigned projects from scoping to recommendations, "
        "and I write the briefing notes that put issues and options in front of senior staff. At Metrolinx I "
        "assessed operating and infrastructure changes in OpenTrack before they were taken forward, and I built "
        "the Crew Variance Tool, a Python application that read large JSON operations files and produced "
        "summaries of speed profiles and run-time variance across subdivisions.",

        TOOLS_SENTENCE,

        "I should be straightforward about the gaps. This is a senior role leading a team of specialists, and "
        "I have not supervised staff. I have not worked on property acquisition, utility relocation or permit "
        "approvals, I have not managed a project budget or administered a construction contract, and I know "
        "design-build delivery and the Building Transit Faster Act from reading rather than from practice. I "
        "do not hold a PMP or a P.Eng., and I do not have the Ontario Class G licence the posting requires for site travel. I am applying because the coordination and negotiation underneath the "
        "role are work I already do from the City's side of the table, and I would like to move into project "
        "leadership on transit.",

        "Thank you for considering my application.",
    ])

# ---------------------------------------------------------------- Arcadis 4477770650
RESUME_4477770650 = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner with the City of Toronto's "
    "Transportation Planning division, where reviewing the transportation studies filed with development "
    "applications is a core part of the work. Has modelled road closures and staging in Synchro and rail "
    "operations in OpenTrack, and analyzes travel data in Python and SQL.",
    city(DEV_STUDIES, TTS, DATA_KPI, PROJECTS, BRIEFING, BYLAW)
    + metrolinx(OPENTRACK, CVT, CLI) + MOTT + UOFA,
    skills=skills("Traffic simulation: Synchro and VISSIM; MATSim and OpenTrack. Review of traffic and "
                  "transportation studies. Python (Pandas, NumPy), SQL and advanced Excel. AutoCAD, Civil 3D, "
                  "ArcGIS Pro, QGIS. Technical reports and presentations. MS Office."))

COVER_4477770650 = letter(
    "Hiring Manager", "Transportation", "Arcadis",
    "Re: Traffic Analysis Engineer (Calgary and Vancouver postings)",
    "Dear Hiring Manager,",
    [
        "I would like to be considered for the Traffic Analysis Engineer position. I am a transportation "
        "engineer with a master's degree and nearly four years of professional experience, and I am an "
        "Assistant Planner in Transportation Planning at the City of Toronto. The posting describes work I "
        "see from the reviewing side every day: site plans, land development and corridor studies, and the "
        "traffic analysis that supports them.",

        "At the City I review the transportation studies filed with development applications against City "
        "standards, check whether their assumptions and results hold up, and write up what is missing. I "
        "analyze travel data, including several years of the Transportation Tomorrow Survey, and I write the "
        "briefing notes and reports that carry the findings to senior staff. At Mott MacDonald I modelled "
        "road closures and construction staging for the Ontario Line in Synchro, and my graduate work "
        "used MATSim and traffic flow modelling for evacuation. I use AutoCAD and Civil 3D, and I work in "
        "Python and SQL.",

        TOOLS_SENTENCE,

        "I should be straightforward about the gaps. I have not written traffic impact studies as a "
        "consultant, so I know what a good one contains from reviewing them rather than from producing them. "
        "I have not used Vistro, Sidra or Aimsun, and I do not know the Alberta Transportation, BC MoTT or "
        "TAC guidelines well. I have not run field data collection, and I have not written proposals. I am "
        "not registered as a P.Eng. or EIT. I am applying because the analysis and reporting are close to "
        "my own work, and I would like to move into project delivery in a consulting team.",

        "Thank you for considering my application.",
    ])
