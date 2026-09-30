# -*- coding: utf-8 -*-
"""Metrolinx — Manager, System Risk Modeling & Intelligence, Engineering & Safety (117339)."""

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


CITY_RISK = CITY_HEAD + [
    "B: Built the Transportation Data Dashboard, combining several years of data from separate operational "
    "sources into one validated source the division reports from, so performance is tracked continuously "
    "rather than rebuilt each quarter.",
    "B: Analyze travel and network data for trends and emerging issues, and establish where capacity falls "
    "short and what that means for future service and investment.",
    "B: Write the briefing notes and presentations that carry findings to planners, engineers and managers "
    "across divisions.",
    "B: Coordinate with divisions, consultants and outside agencies whose priorities conflict, and work issues "
    "through to a resolution.",
    "B: Run assigned projects from scoping through to recommendations, holding the schedule and quality myself.",
]

METROLINX_RISK = METROLINX_HEAD + [
    "B: Ran OpenTrack simulations of GO rail services to establish what proposed operating and infrastructure "
    "changes would do to run times, schedule reliability and recovery before they were taken forward.",
    "B: Built the Crew Variance Tool, a Python application that read large JSON operations files and produced "
    "summaries of speed profiles and run-time variance across subdivisions.",
    "B: Analysed run-time and speed profile patterns across subdivisions to find where schedules were most "
    "exposed to variance.",
    "B: Set up a command line workflow so temporary and permanent slow orders could be pre-simulated in "
    "batches, cutting turnaround on scenario requests from days to hours.",
    "B: Worked with schedulers, operations staff and engineers to settle the variables a service plan had to "
    "be built on.",
]

SKILLS_RISK = [
    "H2: Skills",
    "P: Performance analytics, KPIs and reliability reporting. Python (Pandas, NumPy), SQL and large "
    "operations datasets. OpenTrack rail simulation, VISSIM, Synchro and MATSim. Dashboards and "
    "single-source reporting. Briefing notes and presentations for senior audiences. MS Office, including "
    "large multi-source Excel workbooks.",
]

RESUME_117339 = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner with the City of Toronto "
    "and previously in the Metrolinx Service Design office. Builds single-source performance data from "
    "operational sources that do not agree, analyses run-time and reliability patterns across a rail network, "
    "and turns the findings into reporting senior staff decide from.",
    CITY_RISK + METROLINX_RISK + MOTT + UOFA, skills=SKILLS_RISK)

COVER_117339 = letter(
    "Talent Acquisition", "Engineering and Safety — System Safety and Engineering Management Office",
    "Metrolinx, 20 Bay Street",
    "Re: Manager, System Risk Modeling & Intelligence (Job ID 117339)", "Dear Hiring Manager,",
    [
        "I would like to be considered for the Manager, System Risk Modeling and Intelligence position with "
        "the System Safety and Engineering Management Office. I spent 2023 in the Metrolinx Service Design "
        "office running OpenTrack simulations of GO rail service, and one line in this posting describes that "
        "work from the other side: giving service design and operational planning the data that goes into "
        "their service planning simulation tools.",

        "That is the part of the role I understand best. At Metrolinx I tested what proposed operating and "
        "infrastructure changes would do to run times, schedule reliability and recovery, and much of the value "
        "depended on the quality of the operations data behind the simulation. I built the Crew Variance Tool, "
        "a Python application that read large JSON operations files and summarised speed profiles and run-time "
        "variance across subdivisions, and set up a command line workflow that pre-simulated slow orders in "
        "batches, cutting turnaround on scenario requests from days to hours. Finding where schedules were most "
        "exposed to variance was, in effect, reliability analysis at the level of the timetable.",

        "The posting also asks for a single source of data for senior leaders and timely deep dives on emerging "
        "issues. At the City of Toronto I built the Transportation Data Dashboard, which combined several years "
        "of data from separate operational sources into one validated source the division reports from; most "
        "of that work was reconciling sources that did not agree. I also write the briefing notes and "
        "presentations that carry findings to managers across divisions.",

        "I should be straightforward about the gaps, because this is a manager's role. I have not led a team or "
        "managed staff, which the posting asks for directly. I have not worked with RAMS or EN 50126, with "
        "commercial mechanisms such as liquidated damages, or with formal Lean and Plan-Do-Check-Act programmes, "
        "and I have not been responsible for expense allocation or cost management. I do not hold a P.Eng. The "
        "analytical core of the role is familiar to me; the leadership and the RAMS regime would be new. If the "
        "office has an advisor-level position, I would welcome being considered for that as well.",

        "Thank you for taking the time to consider my application.",
    ])
