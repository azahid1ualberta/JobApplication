# -*- coding: utf-8 -*-
"""Metrolinx, three postings (September 2026):

    116752  Project Manager, Program Delivery Controls, Change and Configuration Management
    117364  Project Manager, Traffic & Transportation, Ontario Line
    117225  Senior Advisor, Commercial Strategy, Rail
"""

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


# ================================================ 116752 Program Delivery Controls

CITY_CONTROLS = CITY_HEAD + [
    "B: Review development applications, engineering submissions and consultant studies against City "
    "standards, test whether their assumptions hold, and recommend conditions where something is missing.",
    "B: Built the Transportation Data Dashboard, reconciling several years of data from separate sources into "
    "one validated source, so the division reports continuously rather than rebuilding a report each quarter.",
    "B: Analyze data for inconsistencies, trends and gaps, and turn the findings into briefing notes and "
    "presentations for management.",
    "B: Coordinate with divisions, consultants and outside agencies whose priorities conflict, and work "
    "issues through to a resolution.",
    "B: Run assigned projects from scoping through to recommendations, holding the schedule and quality myself.",
]

METROLINX_CONTROLS = METROLINX_HEAD + [
    "B: Established what proposed operating and infrastructure changes would do to run times, reliability "
    "and recovery before they were taken forward, using OpenTrack simulation of GO rail services.",
    "B: Worked through large operations datasets across subdivisions and set out where the evidence pointed "
    "for schedulers, operations staff and engineers.",
    "B: Found ways to get scenario analysis through faster and more consistently as the volume of requests grew.",
]

SKILLS_CONTROLS = [
    "H2: Skills",
    "P: Data validation, reconciliation and performance reporting. KPIs and dashboards. Critical review of "
    "technical submissions. Python (Pandas, NumPy), SQL and advanced Excel. Briefing notes, memos and "
    "presentations. OpenTrack, VISSIM, Synchro, ArcGIS and QGIS.",
]

RESUME_116752 = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner with the City of Toronto "
    "and previously with Metrolinx. Reviews technical submissions and data critically, turns multi-source "
    "data into validated reporting and KPIs, and writes the analysis that management decides from.",
    CITY_CONTROLS + METROLINX_CONTROLS + MOTT + UOFA, skills=SKILLS_CONTROLS)

COVER_116752 = letter(
    "Talent Acquisition", "Capital Projects Group — Rapid Transit Program Controls", "Metrolinx, 10 Bay Street",
    "Re: Project Manager, Program Delivery Controls (Job ID 116752)",
    "Dear Hiring Manager,",
    [
        "I would like to be considered for the Project Manager, Program Delivery Controls, Change and "
        "Configuration Management position with the Rapid Transit program. I worked at Metrolinx through 2023 "
        "and am now an Assistant Planner with the City of Toronto, and the part of this role I am most drawn "
        "to is what the posting calls independent, evidence-based challenge.",

        "Much of my current work is that kind of review. I read development applications, engineering "
        "submissions and consultant studies against City standards, check whether their assumptions hold up, "
        "and set out plainly what is missing before anything moves forward. The aim is a better submission "
        "rather than a rejected one, and it depends on keeping a working relationship with applicants and "
        "consultants whose priorities differ from the City's, which is the collaborative side of challenge "
        "the posting describes.",

        "The role also asks for someone to review and validate project data, identify inconsistencies and "
        "emerging trends, and improve program-level KPIs, dashboards and reporting. I built the Transportation "
        "Data Dashboard, which brought several years of data from separate sources into one validated source "
        "the division reports from; most of that work was reconciling sources that did not agree and making "
        "the result reliable enough for management to decide from. At Metrolinx my work was establishing what "
        "proposed operating and infrastructure changes would do to service before they were taken forward, "
        "which is a form of impact assessment.",

        "I should be straightforward about where I fall short. I have not worked in project controls: I have "
        "not managed cost, schedule, risk or contingency baselines, challenged EACs, run change control or "
        "configuration management, or led stage-gate reviews, and I have not used EcoSys, Unifier or Power BI. "
        "The analytical and review side of the role is familiar to me; the controls discipline itself would "
        "be new, and I would expect to learn a good deal from the team.",

        "Thank you for taking the time to consider my application.",
    ])


# ================================================ 117364 Traffic & Transportation, Ontario Line

CITY_TRAFFIC = CITY_HEAD + [
    "B: Review development applications and the transportation studies filed with them against City "
    "standards and Official Plan policy, and recommend conditions where something is missing.",
    "B: Build and maintain the road and right-of-way datasets Transportation Planning depends on, using GIS "
    "and Python to merge sources that were scattered across the division.",
    "B: Analyze how the limited space in the right-of-way is being used, and what competing demands on it "
    "mean for capacity.",
    "B: Coordinate with divisions, consultants, applicants and outside agencies whose priorities conflict, and "
    "write the memos and briefing notes that settle them.",
    "B: Built the Transportation Data Dashboard, combining several years of data into one validated source "
    "the division reports from.",
]

METROLINX_TRAFFIC = METROLINX_HEAD + [
    "B: Ran OpenTrack simulations of GO rail services to establish what infrastructure constraints and speed "
    "restrictions would do to run times and reliability.",
    "B: Assessed the service effect of temporary and permanent slow orders, the kind of restriction that "
    "construction on an operating railway imposes.",
    "B: Worked with schedulers, operations staff and engineers to settle the variables a service plan had to "
    "be built on.",
]

SKILLS_TRAFFIC = [
    "H2: Skills",
    "P: Traffic modelling and simulation: VISSIM, Synchro, MATSim and OpenTrack. Review of transportation "
    "and traffic impact studies. Road and right-of-way data, ArcGIS and QGIS. Stakeholder coordination "
    "across municipal divisions and agencies. Python (Pandas, NumPy) and SQL. Memos, briefing notes and "
    "presentations.",
]

RESUME_117364 = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner with the City of Toronto. "
    "Reviews development applications and the transportation studies filed with them, maintains the road and "
    "right-of-way data the division relies on, and brings traffic simulation experience from Ontario Line "
    "construction staging work and GO rail operations.",
    CITY_TRAFFIC + METROLINX_TRAFFIC + MOTT + UOFA, skills=SKILLS_TRAFFIC)

COVER_117364 = letter(
    "Talent Acquisition", "Capital Projects Group — Ontario Line, Traffic and Transportation",
    "Metrolinx, 10 Bay Street",
    "Re: Project Manager, Traffic & Transportation, Ontario Line (Job ID 117364)", "Dear Hiring Manager,",
    [
        "I would like to be considered for one of the Project Manager, Traffic and Transportation positions "
        "with the Ontario Line team. I am an Assistant Planner with the City of Toronto, so I work on the "
        "municipal side of the relationship this role manages, and I spent a short placement with Mott "
        "MacDonald on the Ontario Line itself.",

        "The posting asks for knowledge of traffic modelling, traffic impact studies and traffic operations "
        "analysis, preferably in transit delivery. At Mott MacDonald I ran traffic simulations to estimate how "
        "Ontario Line construction staging would affect the surrounding streets, which is the question that "
        "sits behind a Traffic Management Plan. At the City I review development applications and the "
        "transportation studies filed with them against City standards, and I build and maintain the road and "
        "right-of-way datasets the division depends on, so what a project does to the limited space in the "
        "right-of-way is a question I work on routinely.",

        "The role is also about third parties, and here the municipal perspective may be useful. I coordinate "
        "with divisions, consultants, applicants and outside agencies whose priorities conflict, and I write "
        "the memos and briefing notes that carry those issues to management. Working inside the City's "
        "transportation division means I understand the priorities a municipal road authority brings to these "
        "discussions, even though permits are not my own area. At Metrolinx in 2023 I saw the same question "
        "from the railway's side, assessing what speed restrictions on an operating network would do to service.",

        "I should be straightforward about the gaps. I have not obtained road occupancy or construction permits, "
        "prepared or reviewed Traffic Management Plans, or worked on a transit project through construction, "
        "and I have no experience with P3, Progressive Design-Build or Alliance models. I do not hold a P.Eng. "
        "The Planning Act I work with through development review; the Highway Traffic Act and the Ontario "
        "Traffic Manual I know in general terms rather than as someone who applies them daily.",

        "Thank you for taking the time to consider my application. I would welcome the chance to discuss the "
        "role.",
    ])


# ================================================ 117225 Senior Advisor, Commercial Strategy, Rail

CITY_COMMERCIAL = CITY_HEAD + [
    "B: Write the briefing notes, memos and presentations that carry findings and recommendations to managers "
    "across divisions.",
    "B: Built the Transportation Data Dashboard, replacing a report rebuilt by hand with one validated source "
    "that tracks divisional performance continuously.",
    "B: Coordinate with divisions, consultants, applicants and outside agencies whose priorities conflict, and "
    "put positions in writing that hold up with each of them.",
    "B: Review development applications and engineering submissions against City standards, and flag where "
    "they fall short.",
    "B: Run assigned projects from scoping through to recommendations, holding the schedule and quality myself.",
]

METROLINX_COMMERCIAL = METROLINX_HEAD + [
    "B: Substantiated the effect of proposed operating changes on run times, equipment and schedule, using "
    "OpenTrack simulation of GO rail services.",
    "B: Put the evidence in front of schedulers, operations staff and engineers, and worked with them to "
    "settle what a service plan had to be built on.",
    "B: Analysed run-time and speed profile patterns across subdivisions to find where schedules were most "
    "exposed to variance.",
]

SKILLS_COMMERCIAL = [
    "H2: Skills",
    "P: Briefing notes, memos and presentations for senior audiences. KPIs, dashboards and performance "
    "reporting. MS Office, including large multi-source Excel workbooks. Python (Pandas, NumPy) and SQL. "
    "Stakeholder coordination and consensus building. OpenTrack rail simulation.",
]

RESUME_117225 = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner with the City of Toronto "
    "and previously in rail operations planning at Metrolinx. Writes the briefing notes, memos and "
    "presentations senior staff decide from, builds KPI reporting, and coordinates across stakeholders whose "
    "interests conflict.",
    CITY_COMMERCIAL + METROLINX_COMMERCIAL + MOTT + UOFA, skills=SKILLS_COMMERCIAL)

COVER_117225 = letter(
    "Talent Acquisition", "Integrated Delivery — Commercial Management, Fleet Strategy",
    "Metrolinx, 20 Bay Street",
    "Re: Senior Advisor, Commercial Strategy, Rail (Job ID 117225)", "Dear Hiring Manager,",
    [
        "I would like to be considered for the Senior Advisor, Commercial Strategy, Rail position with the "
        "Fleet Strategy team. I worked at Metrolinx in 2023 on the rail operations side, and I am now an "
        "Assistant Planner with the City of Toronto, where much of my work is the analysis and communication "
        "this role describes.",

        "A large part of the posting is about preparing presentations and briefing materials for senior "
        "management, drafting and reviewing memos and briefing notes, and keeping information flowing between "
        "a business unit and its stakeholders. That is a daily part of my current job. I write the briefing "
        "notes, memos and presentations that carry findings to managers across divisions, and I coordinate "
        "with consultants, applicants and outside agencies whose interests do not always line up, which often "
        "means putting a position in writing that has to hold up with more than one audience.",

        "The posting also asks for experience with key performance indicators and for improving processes "
        "that are not working. I built the Transportation Data Dashboard, which brought several years of data "
        "from separate sources into one validated source the division reports from and replaced a report that "
        "was rebuilt by hand. At Metrolinx my work meant establishing what proposed operating changes would do "
        "to run times, equipment and schedule, which gave me some sense of how the fleet and operating sides "
        "of a railway depend on each other.",

        "I should be clear about the commercial side. I have not administered commercial contracts, monitored "
        "contractor compliance, managed claims or developed negotiation mandates, and my knowledge of contract "
        "law is general. I have not managed a budget, and I have not used Oracle or Unifier. The analytical, "
        "reporting and communication parts of the role I would bring from the start; the contract discipline "
        "I would be learning.",

        "Thank you for taking the time to consider my application.",
    ])
