# -*- coding: utf-8 -*-
"""Metrolinx — Project Manager, Lakeshore West Existing Stations Rehabilitation (117202)."""

from content3 import (NAME, CONTACT, CITY_HEAD, METROLINX_HEAD, MOTT, UOFA, resume)

DATE = "September 30, 2026"


def letter(to_name, to_title, to_org, subject, salutation, paras):
    out = [f"NAME: {NAME}", f"CONTACT: {CONTACT}", "SPACE:", f"PLT: {DATE}", "SPACE:",
           f"PLT: **{to_name}**"]
    if to_title:
        out.append(f"PLT: {to_title}")
    out += [f"PLT: {to_org}", "SPACE:", f"PLT: **{subject}**", "SPACE:",
            f"PLT: {salutation}", "SPACE:"]
    out += [f"P: {p}" for p in paras]
    out += ["SPACE:", "PLT: Sincerely,", f"SIGN: {NAME}", f"PLT: {NAME}"]
    return out


CITY_PM = CITY_HEAD + [
    "B: Review engineering submissions, consultant studies and drawings against City standards and policy, "
    "and recommend conditions where something is missing.",
    "B: Run assigned projects from scoping through to recommendations, holding the schedule and quality myself "
    "and reporting progress to the people relying on it.",
    "B: Coordinate with divisions, consultants, applicants and outside agencies whose priorities conflict, and "
    "work issues through to a resolution.",
    "B: Write the memos, briefing notes and presentations that carry plans, issues and recommendations to "
    "management.",
    "B: Built the Transportation Data Dashboard, combining several years of data from separate sources into "
    "one validated source the division reports from.",
]

METROLINX_PM = METROLINX_HEAD + [
    "B: Ran OpenTrack simulations of GO rail services to establish what infrastructure constraints and speed "
    "restrictions would do to run times and reliability.",
    "B: Assessed the service effect of temporary and permanent slow orders, the kind of restriction that "
    "construction on an operating railway imposes.",
    "B: Set up a command line workflow so temporary and permanent slow orders could be pre-simulated in "
    "batches, cutting turnaround on scenario requests from days to hours.",
    "B: Built the Crew Variance Tool, a Python application that read large JSON operations files and produced "
    "summaries of speed profiles and run-time variance across subdivisions.",
    "B: Worked with schedulers, operations staff and engineers to settle the variables a service plan had to "
    "be built on.",
]

SKILLS_PM = [
    "H2: Skills",
    "P: Review of engineering submissions, consultant studies and drawings. Project scoping, scheduling and "
    "follow-through. Stakeholder coordination with municipal divisions, agencies and consultants. OpenTrack "
    "rail simulation, VISSIM and Synchro. Python (Pandas, NumPy), SQL, ArcGIS and QGIS. Memos, briefing notes "
    "and presentations. MS Office.",
]

RESUME_117202 = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner with the City of Toronto "
    "and previously with Metrolinx on the GO rail network. Reviews consultant studies, engineering submissions "
    "and drawings against standards, runs assigned projects from scoping to recommendations, and coordinates "
    "with municipal, agency and consultant stakeholders.",
    CITY_PM + METROLINX_PM + MOTT + UOFA, skills=SKILLS_PM)

COVER_117202 = letter(
    "Talent Acquisition", "Capital Projects Group (GO & UP) — Lakeshore West Existing Stations Rehabilitation",
    "Metrolinx, 130 Adelaide Street West",
    "Re: Project Manager (Job ID 117202)", "Dear Hiring Manager,",
    [
        "I would like to be considered for the Project Manager position with the Lakeshore West Existing "
        "Stations Rehabilitation team. I worked on the GO rail network at Metrolinx in 2023 and am now an "
        "Assistant Planner with the City of Toronto, where much of my work is reviewing technical submissions "
        "and coordinating the people who have a stake in them.",

        "The part of the posting I recognise most is facilitating the review of consultant studies, reports, "
        "design proposals and specifications for compliance with standards, and liaising with municipal "
        "authorities, agencies and consultants on timelines and issues. At the City I review engineering "
        "submissions, consultant studies and drawings against City standards and recommend conditions where "
        "something is missing, and I run assigned projects from scoping to recommendations while holding the "
        "schedule and quality myself. I coordinate with divisions, consultants and outside agencies whose "
        "priorities conflict, and write the memos and briefing notes that carry issues to management.",

        "Station rehabilitation happens around a live railway, and that is the part of my Metrolinx experience "
        "most relevant here. I assessed what temporary and permanent slow orders, the kind of restriction "
        "construction work imposes, would do to GO service, and set up a command line workflow that "
        "pre-simulated them in batches, cutting turnaround on scenario requests from days to hours. I also built "
        "the Crew Variance Tool, a Python application that summarised speed profiles and run-time variance "
        "across subdivisions from large operations files.",

        "I should be straightforward about the gaps. I have not managed construction projects through design, "
        "tender, construction and commissioning, supervised staff, managed a budget, or administered "
        "procurement, change orders and consultant agreements. My knowledge of contract law, the Construction "
        "Act and the Occupational Health and Safety Act is general, and I do not hold a PMP or P.Eng. I am "
        "applying because the review and coordination parts of the role are familiar, the railway context is "
        "one I know, and the posting invites people who do not meet every requirement.",

        "Thank you for taking the time to consider my application.",
    ])
