# -*- coding: utf-8 -*-
"""Metrolinx — Manager, Rapid Transit Program Delivery, Capital Projects Group (117264)."""

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


CITY_RT = CITY_HEAD + [
    "B: Review development applications, engineering submissions and consultant drawings for their effect on "
    "existing and planned infrastructure, and recommend conditions where something is missing.",
    "B: Coordinate with divisions, consultants, applicants and outside agencies whose priorities conflict, and "
    "work issues through to a position everyone can act on.",
    "B: Write the memos, briefing notes and presentations that carry plans, issues and recommendations to "
    "management across divisions.",
    "B: Built the Transportation Data Dashboard, replacing reports rebuilt by hand each quarter with one "
    "validated source the division reports from, and saw the change through to adoption.",
    "B: Run assigned projects from scoping through to recommendations, holding the schedule and quality myself.",
]

METROLINX_RT = METROLINX_HEAD + [
    "B: Ran OpenTrack simulations of GO rail services to establish what proposed operating and infrastructure "
    "changes would do to run times, reliability and recovery before they were taken forward.",
    "B: Assessed the service effect of temporary and permanent slow orders, the kind of restriction that work "
    "on an operating railway imposes, including how far the effect carried beyond the affected subdivision.",
    "B: Put the evidence in front of schedulers, operations staff and engineers, and worked with them to "
    "settle the variables a service plan had to be built on.",
]

SKILLS_RT = [
    "H2: Skills",
    "P: Stakeholder coordination and consensus building across agencies. Development review and "
    "infrastructure impact assessment. Memos, briefing notes and presentations for management. Project "
    "scoping and follow-through. OpenTrack, VISSIM, Synchro and MATSim. Python (Pandas, NumPy), SQL, ArcGIS "
    "and QGIS. Dashboards and performance reporting.",
]

RESUME_117264 = resume(
    "Transportation engineer with a master's degree and experience across the City of Toronto, Metrolinx and "
    "Mott MacDonald. Reviews development proposals for their effect on existing and planned infrastructure, "
    "coordinates across agencies whose priorities conflict, and writes the memos and briefing notes that "
    "carry issues and recommendations to management.",
    CITY_RT + METROLINX_RT + MOTT + UOFA, skills=SKILLS_RT)

COVER_117264 = letter(
    "Talent Acquisition", "Capital Projects Group — Rapid Transit Program Delivery", "Metrolinx, 10 Bay Street",
    "Re: Manager, Rapid Transit Program Delivery (Job ID 117264)", "Dear Hiring Manager,",
    [
        "I would like to be considered for the Manager, Rapid Transit Program Delivery position with the "
        "Capital Projects Group. I worked at Metrolinx through 2023 in the Service Design office, and my "
        "current work with the City of Toronto sits at the point where new development meets existing and "
        "planned infrastructure, which is much of what the Transit Oriented Community side of this role is "
        "about.",

        "That is the part of the posting I recognise most closely: making sure a developer's proposal accounts "
        "for the infrastructure around and beneath it, and that the owner's requirements are written into what "
        "gets built. As an Assistant Planner I review development applications, engineering submissions and "
        "consultant drawings for their effect on existing and planned infrastructure, and recommend conditions "
        "where something is missing. I have not prepared a Metrolinx Asset Protection Package, but reading a "
        "submission against what has to be protected, and setting out plainly what needs to change, is the "
        "everyday substance of my work.",

        "The posting also asks for someone who can work with partners on sensitive issues and report clearly "
        "to management. At the City I coordinate with divisions, consultants, applicants and outside agencies "
        "whose priorities often conflict, and I write the memos and briefing notes that carry those issues "
        "upward. At Metrolinx my work was establishing what slow orders and other operating changes would do "
        "to service before they were taken forward, and a short placement with Mott MacDonald on Ontario Line "
        "work involved simulating how construction staging would affect the surrounding streets.",

        "I should be straightforward about the gaps. The posting asks for at least eight years of relevant "
        "experience and I have closer to four. I have not supervised staff, held a project budget, taken a "
        "project through a system safety review, or negotiated agreements with the TTC, and I do not hold a "
        "P.Eng. or PMP. I am applying because the development interface work is familiar to me, and because "
        "the posting invites people who do not meet every requirement. If this role is a step too far, I "
        "would welcome being considered for a project-level position within the Rapid Transit program.",

        "Thank you for taking the time to consider my application.",
    ])
