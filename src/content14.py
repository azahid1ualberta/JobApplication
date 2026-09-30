# -*- coding: utf-8 -*-
"""Metrolinx — Rail Simulation Specialist, Operations (117317)."""

from content3 import (NAME, CONTACT, CITY_HEAD, METROLINX_HEAD, MOTT, UOFA, resume)

DATE = "September 29, 2026"


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


METROLINX_SIM = METROLINX_HEAD + [
    "B: Ran OpenTrack simulations of GO rail services, building and testing network scenarios against "
    "infrastructure constraints, speed restrictions and corridor conditions.",
    "B: Established what proposed operating and infrastructure changes would do to run times, schedule "
    "reliability and recovery before they were taken forward.",
    "B: Assessed the network effect of temporary and permanent slow orders, including how far a speed "
    "restriction carried beyond the subdivision it sat on.",
    "B: Analysed run-time and speed profile patterns across subdivisions to find where schedules were most "
    "exposed to variance, working from the operations data directly where the volumes ruled out doing it "
    "by hand.",
    "B: Worked with schedulers, operations staff and engineers to pin down the technical and operational "
    "variables a service plan had to be built on.",
]

CITY_SIM = CITY_HEAD + [
    "B: Analyze travel and network data to establish where capacity falls short and what that means for "
    "future service and investment.",
    "B: Review development applications and engineering studies for their effect on existing and planned "
    "infrastructure, and recommend conditions where capacity is at risk.",
    "B: Built the Transportation Data Dashboard, combining several years of data from separate operational "
    "sources into one validated source the division reports from.",
    "B: Run assigned studies from scoping through to recommendations, and write the technical reports and "
    "briefing notes that carry them to planners, engineers and managers across divisions.",
]

SKILLS_SIM = [
    "H2: Skills",
    "P: OpenTrack rail simulation and network modelling. Python (Pandas, NumPy), SQL and JavaScript. "
    "Operations data handling, pipelines and validation. VISSIM, Synchro and MATSim. ArcGIS and QGIS. "
    "Technical reporting and performance dashboards. MS Office, including large multi-source Excel workbooks.",
]

RESUME_117317 = resume(
    "Transportation engineer with a master's degree and a year in the Metrolinx Service Design office, where "
    "the work was rail network simulation and modelling in OpenTrack. Currently an Assistant Planner with the "
    "City of Toronto. Builds the simulation and analysis that turns proposed service and infrastructure "
    "changes into defensible operating requirements.",
    CITY_SIM + METROLINX_SIM + MOTT + UOFA, skills=SKILLS_SIM)

COVER_117317 = letter(
    "Talent Acquisition", "Operations", "Metrolinx, 130 Adelaide Street West",
    "Re: Rail Simulation Specialist (Job ID 117317)", "Dear Hiring Manager,",
    [
        "I would like to be considered for the Rail Simulation Specialist position. I spent 2023 in the "
        "Metrolinx Service Design office as a Transportation Planner in simulation and modelling, and rail "
        "network simulation in OpenTrack was the substance of that year, so the posting reads closely to work "
        "I already know.",

        "The role is described as modelling and simulating rail network utilization scenarios, conducting "
        "network analyses and studies, and validating service level increases using OpenTrack. That was the "
        "shape of my work at Metrolinx. I built and tested network scenarios against infrastructure "
        "constraints, speed restrictions and corridor conditions, and much of my time went into establishing "
        "what a proposed operating or infrastructure change would do to run times, schedule reliability and "
        "recovery before it was taken forward. Looking at run-time patterns across subdivisions to see where "
        "schedules were likely to come under pressure was part of that.",

        "One line in the posting I would pick out is construction activity that reduces capacity, and "
        "recommending solutions for high-risk areas. A good deal of my Metrolinx work sat there: assessing "
        "what temporary and permanent slow orders would do to run times, connections and recovery, and how "
        "far the effect carried beyond the subdivision it sat on. Before that I spent a short placement with "
        "Mott MacDonald on Ontario Line work, simulating how construction staging would affect the "
        "surrounding network, which is the same question asked from the road side.",

        "Since January 2024 I have been an Assistant Planner with the City of Toronto. I analyse network "
        "capacity, review development applications and engineering studies for their effect on planned "
        "infrastructure, and write the technical reports and briefing notes that carry findings to colleagues "
        "in other divisions. Working with municipalities, consultants and agencies whose priorities do not "
        "line up is routine there rather than exceptional.",

        "Two things I should be straightforward about. My direct rail simulation experience is one year, and "
        "it is commuter rail rather than the wider mix of passenger and freight networks the posting asks "
        "for. And while I am comfortable in OpenTrack, I have not used Rail Traffic Controller, and my "
        "knowledge of the applicable standards and regulations is general rather than detailed.",

        "Thank you for taking the time to consider my application. I would welcome the chance to discuss the "
        "role.",
    ])
