# -*- coding: utf-8 -*-
"""Metrolinx — Timetabling Specialist, GO Expansion Operations (117073).

Posting closed 7 September 2026. Kept because the documents are reusable and
because this is the tone Abdullah approved: modest register, and no naming of
the Crew Variance Tool or the command line workflow, since the audience is a
team that already lived through that work.
"""

from content3 import (NAME, CONTACT, CITY_HEAD, METROLINX_HEAD, MOTT, UOFA, resume)

DATE = "August 26, 2026"


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


METROLINX_TT = METROLINX_HEAD + [
    "B: Ran OpenTrack simulations of GO rail services to build and test timetables against infrastructure "
    "constraints, speed restrictions and corridor conditions.",
    "B: Validated proposed operating changes by establishing what they would do to run times, schedule "
    "reliability and recovery before anyone committed to them.",
    "B: Assessed the timetable effect of temporary and permanent slow orders, including how far a speed "
    "restriction carried beyond the subdivision it sat on, and turned scenario requests around in volume.",
    "B: Analysed run-time and speed profile patterns across subdivisions to find where schedules were most "
    "exposed to variance, working from the operations data directly where the volumes ruled out doing it "
    "by hand.",
    "B: Worked with schedulers, operations staff and engineers to pin down the technical and operational "
    "variables that had to go into a service plan.",
]

CITY_TT = CITY_HEAD + [
    "B: Analyze travel and network data to establish where capacity falls short and what it means for future "
    "service and investment.",
    "B: Built the Transportation Data Dashboard, combining several years of data from separate operational "
    "sources into one validated source the division reports from.",
    "B: Review development applications and engineering studies against City standards, and run assigned "
    "studies from scoping through to recommendations.",
    "B: Write the briefing notes that carry findings to planners, engineers and managers across divisions.",
]

SKILLS_TT = [
    "H2: Skills",
    "P: OpenTrack rail simulation and timetabling. Python (Pandas, NumPy), SQL and JavaScript. Operations "
    "data handling, pipelines and validation. VISSIM, Synchro and MATSim. ArcGIS and QGIS. Dashboards and "
    "performance reporting. MS Office, including large multi-source Excel workbooks.",
]

RESUME_117073 = resume(
    "Transportation engineer with a master's degree and a year in the Metrolinx Service Design office, where "
    "the work was rail timetabling and validating operating changes in OpenTrack. Currently an Assistant "
    "Planner with the City of Toronto. Builds the modelling and analysis that turns proposed service and "
    "infrastructure changes into defensible operating specifications.",
    CITY_TT + METROLINX_TT + MOTT + UOFA, skills=SKILLS_TT)

COVER_117073 = letter(
    "Talent Acquisition", "GO Expansion Operations", "Metrolinx, 130 Adelaide Street West",
    "Re: Timetabling Specialist (Job ID 117073)", "Dear Hiring Manager,",
    [
        "I would like to be considered for the Timetabling Specialist position with the GO Expansion "
        "Operations team. I spent 2023 in the Metrolinx Service Design office, where much of my work involved "
        "rail timetabling in OpenTrack, and I would welcome the chance to return to that side of the "
        "business.",

        "The posting describes using specialized scheduling and modelling tools to analyze rail operations "
        "and translate future-state plans into operating specifications, planning assumptions and service "
        "requirements. That was the shape of my work at Metrolinx. I used OpenTrack to build and test "
        "timetables against infrastructure constraints, speed restrictions and corridor conditions, and a "
        "good deal of my time went into understanding what a proposed change would mean for run times, "
        "reliability and recovery before it was taken forward. Working across timetabling, crewing, cycling "
        "and consist length was part of that, as was looking at run-time patterns across subdivisions to see "
        "where schedules were likely to come under pressure.",

        "A good deal of that work was slow order assessment, working out what a temporary or permanent speed "
        "restriction would do to run times, connections and recovery, and how far the effect carried beyond "
        "the subdivision it sat on. When the volume of scenarios grew I found ways to get through them more "
        "quickly and more consistently, though the part I valued most was the conversation with schedulers "
        "and operations staff about what the results actually meant for the schedule. Since January 2024 I "
        "have been an Assistant Planner with the City of Toronto, working on network capacity analysis, "
        "divisional reporting and briefing notes for colleagues across divisions.",

        "I should mention two things honestly. I do not hold CROR certification, which I note is listed as "
        "preferred, and my familiarity with Transport Canada and TAC requirements is general rather than "
        "detailed. I have also not supervised staff directly, though I have coordinated technical work that "
        "others depended on and would be glad to grow into that part of the role.",

        "Thank you for taking the time to consider my application. I would very much welcome the opportunity "
        "to discuss the position.",
    ])
