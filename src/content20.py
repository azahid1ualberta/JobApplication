# -*- coding: utf-8 -*-
"""Consulting firms, four postings (September 2026):

    WSP     Senior Passenger Modelling Specialist (94275)
    Stantec Senior Aviation Planner - Airports (Toronto and Markham listings, same posting)
    Stantec Aviation Planner - Airports (Markham)
    CIMA+   Senior Aviation Planner (REF3026P)
"""

from content3 import (NAME, CONTACT, CITY_HEAD, METROLINX_HEAD, MOTT, UOFA, resume)
from content19 import (OPENTRACK, CVT, CLI, SCHED, DASHBOARD, TOOLS_SENTENCE, city, metrolinx, skills)

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


TTS = ("B: Analyze travel and network data, including several years of the Transportation Tomorrow Survey, to "
       "establish where capacity falls short and what that means for future service and investment.")
DEV_STUDIES = ("B: Review development applications and the transportation studies filed with them against City "
               "standards and Official Plan policy, and recommend conditions where something is missing.")
REPORTS = ("B: Write the technical reports, briefing notes and presentations that carry findings to planners, "
           "engineers and managers across divisions.")
AGENCIES = ("B: Coordinate with divisions, consultants, applicants and outside agencies whose priorities "
            "conflict, and work issues through to a position everyone can act on.")
OT_BUILD = ("B: Ran OpenTrack simulations of GO rail services to build and test timetables against "
            "infrastructure constraints, speed restrictions and corridor conditions.")
VALIDATED = ("B: Validated proposed operating changes by establishing what they would do to run times, schedule "
             "reliability and recovery before anyone committed to them.")


# ================================================ WSP Senior Passenger Modelling Specialist

RESUME_WSP = resume(
    "Transportation engineer with a master's degree whose work has centred on simulation: agent-based "
    "(MATSim) and macroscopic network models in graduate research, traffic simulation of Ontario Line "
    "construction staging, and OpenTrack rail simulation of GO services at Metrolinx. Builds the Python "
    "tooling behind the analysis and turns model output into clear reports for decision-makers.",
    city(TTS, DASHBOARD, DEV_STUDIES, REPORTS)
    + metrolinx(OT_BUILD, VALIDATED, CVT, CLI, SCHED) + MOTT + UOFA,
    skills=skills("Agent-based and microscopic simulation: MATSim, VISSIM, Synchro and OpenTrack. Python "
                  "(Pandas, NumPy) and SQL for analysis and automation. Model testing and data visualization. "
                  "Advanced Excel. ArcGIS and QGIS. Technical reports and presentations."))

COVER_WSP = letter(
    "Talent Acquisition", "Rail & Transit", "WSP Canada, Toronto, ON",
    "Re: Senior Passenger Modelling Specialist (Job ID 94275)", "Dear Hiring Manager,",
    [
        "I would like to apply for the Senior Passenger Modelling Specialist position with the Rail & Transit "
        "team, based in Toronto. Simulation has been the common thread through my work so far, and passenger "
        "modelling is where I would like to take it.",

        "The posting asks for experience in agent-based simulation within transportation. My master's research "
        "at the University of Alberta used MATSim, an agent-based model, alongside macroscopic LWR models to "
        "study how road networks perform during emergency evacuations: how many people move, which paths they "
        "take, where queues form and whether the system holds up under stress. Those are close to the questions "
        "behind passenger flow modelling, though at network rather than station scale. Since then I have run "
        "traffic simulations of Ontario Line construction staging at Mott MacDonald, and OpenTrack simulations "
        "of GO rail services at Metrolinx, building and testing scenarios against infrastructure constraints "
        "before anyone committed to them.",

        "The posting also asks for strong Python and Excel for analysis and automation. " + TOOLS_SENTENCE +
        " At the City of Toronto I built the Transportation Data Dashboard, bringing several years of data into "
        "one validated source, and I write the technical reports and presentations that turn analysis into "
        "something decision-makers can act on.",

        "I should be straightforward about the gaps. I have not used LEGION, Viswalk, MassMotion or CAST, "
        "modelled a transit station, or developed a Crowd Control Plan, and I have not used VBA or R. The "
        "posting asks for eight or more years of experience; I have closer to four years of professional work "
        "plus my graduate research. I am applying because the modelling foundation is genuinely mine, and if "
        "the team has an intermediate passenger modelling role, I would welcome being considered for it.",

        "Thank you for considering my application.",
    ])


# ================================================ Aviation planner resume (shared by all three)

RESUME_AVIATION = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner with the City of Toronto. "
    "Analyzes transportation data to establish where capacity falls short, reviews development proposals and "
    "their transportation studies, and builds simulation models of road and rail systems, with reports and "
    "presentations that carry the findings to agencies and decision-makers.",
    city(TTS, DEV_STUDIES, REPORTS, AGENCIES, DASHBOARD)
    + metrolinx(OPENTRACK, CVT, CLI, SCHED) + MOTT + UOFA,
    skills=skills("Transportation capacity and demand analysis. Traffic and rail simulation: VISSIM, Synchro, "
                  "MATSim and OpenTrack. Python (Pandas, NumPy), SQL and advanced Excel. ArcGIS and QGIS. AutoCAD and "
                  "Civil 3D. "
                  "Dashboards and data visualization. Technical reports, memoranda and presentations. MS Office."))

LANDSIDE = (
    "The posting covers ground transportation facilities and commercial land development at airports as well "
    "as airside and terminal work, and the landside is where my experience applies. At the City of Toronto I "
    "analyze travel and network data to establish where capacity falls short, review development applications "
    "and the transportation studies filed with them, and write the reports and presentations that carry "
    "findings to managers and outside agencies. The operational side of facility planning, testing whether a "
    "design will cope with the demand placed on it, is what I have done with simulation: traffic simulation of "
    "Ontario Line construction staging at Mott MacDonald, OpenTrack simulation of GO rail services at "
    "Metrolinx, and agent-based MATSim models in my master's research.")


# ================================================ Stantec Senior Aviation Planner

COVER_STANTEC_SENIOR = letter(
    "Talent Acquisition", "Airport Planning and Design", "Stantec Consulting Ltd., Toronto, ON",
    "Re: Senior Aviation Planner - Airports", "Dear Hiring Manager,",
    [
        "I would like to apply for the Senior Aviation Planner position with the Airport Planning and Design "
        "team. I come to it from transportation planning rather than aviation, so I want to be clear about both "
        "what I would bring and where I fall short.",

        LANDSIDE,

        TOOLS_SENTENCE + " Building tools like these is how I approach analysis generally: set up the method "
        "once, then spend the time on what the results mean.",

        "The gaps are real. I have no airport planning experience: I have not prepared airport master plans or "
        "airfield and terminal concept plans, and I have not used Aviplan, though I have worked in AutoCAD and "
        "Civil 3D. I have not "
        "managed consulting projects or supported pursuits. A senior role expects aviation experience I do not "
        "yet have, so I would also welcome being considered for the Aviation Planner position the team has "
        "posted, where I could build that experience.",

        "Thank you for considering my application.",
    ])


# ================================================ Stantec Aviation Planner

COVER_STANTEC = letter(
    "Talent Acquisition", "Airport Planning and Design", "Stantec Consulting Ltd., Markham, ON",
    "Re: Aviation Planner - Airports", "Dear Hiring Manager,",
    [
        "I would like to apply for the Aviation Planner position with the Airport Planning and Design team. I "
        "come to it from transportation planning, and airport planning is a field I would like to grow into.",

        LANDSIDE,

        TOOLS_SENTENCE + " I am comfortable learning new software quickly, which I expect would matter here.",

        "I should be straightforward about the gaps. I have no airport planning experience and have not "
        "prepared development or concept plans for airfields or terminals. I have worked in AutoCAD, Civil 3D "
        "and Adobe Photoshop and Illustrator, but not in Aviplan or Bluebeam Revu, and I would be learning the applicable aviation standards and "
        "regulations. What I would bring from the start is the transportation analysis, the simulation "
        "background and the report writing.",

        "Thank you for considering my application.",
    ])


# ================================================ CIMA+ Senior Aviation Planner

COVER_CIMA = letter(
    "Talent Acquisition", "Aviation", "CIMA+, 5935 Airport Road, Mississauga, ON",
    "Re: Senior Aviation Planner (Reference REF3026P)", "Dear Hiring Manager,",
    [
        "I would like to apply for the Senior Aviation Planner position with the Aviation team. I come to it "
        "from transportation planning rather than aviation, and I want to be clear about both what I would bring "
        "and where I fall short.",

        "Several of the listed responsibilities are close to my current work. The first is reviewing and "
        "interpreting transportation data to support capacity planning and operational decisions: at the City of "
        "Toronto I analyze travel and network data to establish where capacity falls short and what that means "
        "for future investment. Land use concepts and zoning frameworks are familiar from reviewing development "
        "applications against the Official Plan. Construction phasing and operations planning connect to my "
        "Mott MacDonald work simulating Ontario Line construction staging, and to assessing what slow orders "
        "would do to GO rail service at Metrolinx.",

        "The posting also mentions familiarity with simulation and modelling software. I have worked with "
        "VISSIM, Synchro, MATSim and OpenTrack. " + TOOLS_SENTENCE + " I write technical memoranda, reports and "
        "presentations, and I have built a dashboard the division reports from, though I have not used Power BI.",

        "The gaps are significant. The posting strongly prefers twelve or more years of airport planning "
        "experience, and I have none: I have not prepared airport master plans, airfield or terminal "
        "configurations, aeronautical impact evaluations or air service studies, and I have not used CAST or "
        "AviPlan, though I have worked in AutoCAD and Civil 3D. If the team has an intermediate planning role, I would welcome being "
        "considered for it.",

        "Thank you for considering my application.",
    ])
