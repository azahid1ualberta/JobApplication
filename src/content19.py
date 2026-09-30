# -*- coding: utf-8 -*-
"""City of Toronto, five postings (September 2026):

    65977  Project Manager, Development Review (Priority Development Review)
    64483  Project Manager Business Transformation, Parks & Recreation CPDD
    66777  Project Manager TW, Toronto Water Capital Planning & Implementation
    67150  Project Manager, Fleet Safety Operations & Continuous Improvement
    64397  Senior Project Manager TW, Toronto Water Wastewater Treatment
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


# ------------------------------------------------------------ shared bullets

REVIEW_DEV = ("B: Review development applications and the studies filed with them against City standards and "
              "Official Plan policy, and recommend conditions where something is missing.")
REVIEW_ENG = ("B: Review engineering submissions, consultant studies and drawings against City standards, and "
              "recommend conditions where something is missing.")
COORD = ("B: Coordinate with divisions, consultants, applicants and outside agencies whose priorities conflict, "
         "and work issues through to a position everyone can act on.")
PROJECTS = ("B: Run assigned projects from scoping through to recommendations, planning the work, holding the "
            "schedule and quality myself, and reporting progress to the people relying on it.")
BRIEFING = ("B: Write the briefing notes, memos and presentations that carry issues, options and "
            "recommendations to senior staff across divisions.")
RESEARCH = ("B: Research policy questions as they come up, looking at how City policy, provincial legislation "
            "and work by other levels of government bear on them.")
DASHBOARD = ("B: Built the Transportation Data Dashboard, replacing a report rebuilt by hand each quarter with "
             "one validated source the division reports from, and saw the change through to adoption.")
DATA_KPI = ("B: Analyze large volumes of travel and network data for trends, gaps and emerging issues, and turn "
            "them into KPIs and data-driven recommendations.")
IMPROVE = ("B: Identify where a process is not working, coordinate the people needed to change it, and see the "
           "change through to adoption.")
TOOLING = ("B: Build and maintain the datasets and tooling Transportation Planning depends on, using Python and "
           "GIS.")
CAPITAL = ("B: Analyze network data to work out where capacity is short, and what that means for maintenance "
           "and capital spending.")

OPENTRACK = ("B: Ran OpenTrack simulations of GO rail services to establish what proposed operating and "
             "infrastructure changes would do to run times, reliability and recovery before they were taken "
             "forward.")
SLOW = ("B: Assessed the service effect of temporary and permanent slow orders, the kind of restriction that "
        "construction on an operating railway imposes.")
CVT = ("B: Built the Crew Variance Tool, a Python application that read large JSON operations files and "
       "produced summaries of speed profiles and run-time variance across subdivisions.")
CLI = ("B: Set up a command line workflow so temporary and permanent slow orders could be pre-simulated in "
       "batches, cutting turnaround on scenario requests from days to hours.")
SCHED = ("B: Worked with schedulers, operations staff and engineers to settle the variables a service plan had "
         "to be built on.")

TOOLS_SENTENCE = ("At Metrolinx I set up a command line workflow that pre-simulated slow orders in batches, "
                  "cutting turnaround on scenario requests from days to hours, and built the Crew Variance Tool, "
                  "a Python application that read large JSON operations files and summarised speed profiles and "
                  "run-time variance across subdivisions.")


def city(*bullets):
    return CITY_HEAD + list(bullets)


def metrolinx(*bullets):
    return METROLINX_HEAD + list(bullets)


def skills(text):
    return ["H2: Skills", f"P: {text}"]


# ================================================ 65977 Project Manager, Development Review

RESUME_65977 = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner with the City of Toronto, "
    "where reviewing development applications against City standards and Official Plan policy is a core part "
    "of the job. Coordinates across divisions, agencies and applicants whose priorities conflict, and writes "
    "the briefing notes that carry issues and options to senior staff.",
    city(REVIEW_DEV, COORD, PROJECTS, BRIEFING, RESEARCH)
    + metrolinx(OPENTRACK, CLI, CVT, SCHED) + MOTT + UOFA,
    skills=skills("Development application review against City standards and Official Plan policy. Project "
                  "planning, scheduling and follow-through. Coordination across divisions, agencies and applicants. "
                  "Briefing notes, memos and presentations for senior staff. Policy research. Python (Pandas, "
                  "NumPy), SQL, ArcGIS and QGIS. MS Office."))

COVER_65977 = letter(
    "Nikki Kang", "Human Resources", "Development Review Division, City of Toronto",
    "Re: Project Manager, Priority Development Review (Job ID 65977)", "Dear Nikki Kang,",
    [
        "I would like to apply for the Project Manager position with the Priority Development Review Service. I "
        "am an Assistant Planner in Transportation Planning with the City, and reviewing development "
        "applications as they move through the City's process is a large part of my job.",

        "I see that process from the commenting side. I review development applications and the studies filed "
        "with them against City standards and Official Plan policy, and recommend conditions where something is "
        "missing. From there I can see where an application tends to stall: a condition that is unclear, a study "
        "that answers a different question from the one being asked, or two divisions each waiting on the other. "
        "Coordinating the review so that technical experts keep responsibility for their advice while the file "
        "keeps moving is the part of this role I believe I would do well.",

        "I coordinate with divisions, consultants, applicants and outside agencies whose priorities conflict, "
        "and I write the briefing notes and memos that carry issues and options to senior staff. I run assigned "
        "projects from scoping through to recommendations, planning the work and holding the schedule myself. "
        + TOOLS_SENTENCE + " Making a process faster and more predictable for the people who depend on it is "
        "the same instinct this role asks for.",

        "I should be clear about where I fall short. I have not led a portfolio of development applications, "
        "led a project team, retained and managed consultants, or controlled project expenditures, and I have "
        "not briefed elected officials directly. My knowledge of Zoning By-law Amendment and Site Plan Control "
        "applications comes from reviewing them rather than steering them through approval. I am applying "
        "because the substance of the role is close to my daily work, and because the Qualified List covers "
        "both permanent and temporary positions.",

        "Thank you for considering my application. I would welcome the chance to discuss the role.",
    ])


# ================================================ 64483 Project Manager Business Transformation, P&R CPDD

RESUME_64483 = resume(
    "Transportation engineer with a master's degree and part way through a computer science degree, currently "
    "an Assistant Planner with the City of Toronto. Replaces manual processes with automation and validated "
    "data, gets the people who rely on the output to adopt the change, and reports the results to management.",
    city(DASHBOARD, IMPROVE, TOOLING, BRIEFING, COORD)
    + metrolinx(CLI, CVT, OPENTRACK, SCHED) + MOTT + UOFA,
    skills=skills("Process automation with Python (Pandas, NumPy) and SQL. Dashboards, KPIs and performance "
                  "measurement. Data analysis and data-driven recommendations. Advanced Excel and MS Office. "
                  "Briefing notes, memos and presentations. Stakeholder coordination across divisions and agencies."))

COVER_64483 = letter(
    "Heather Thompson", "Human Resources", "Parks & Recreation, City of Toronto",
    "Re: Project Manager Business Transformation (Job ID 64483)", "Dear Heather Thompson,",
    [
        "I would like to apply for the Project Manager Business Transformation position with the CPDD "
        "Transformation Unit. I am an Assistant Planner with the City and part way through a computer science "
        "degree, and the part of this role I am most drawn to is using automation to reduce manual workloads.",

        "That is work I have done in two organizations. At Metrolinx, scenario requests were being run case by "
        "case, so I set up a command line workflow that pre-simulated slow orders in batches, cutting turnaround "
        "from days to hours, and built the Crew Variance Tool, a Python application that read large JSON "
        "operations files and produced summaries of speed profiles and run-time variance that had been put "
        "together by hand. At the City I built the Transportation Data Dashboard, replacing a report rebuilt "
        "each quarter with one validated source the division reports from. In each case the harder part was not "
        "the code but getting the people who relied on the output to trust it and change how they worked, which "
        "is the people side of adoption the posting describes.",

        "I also coordinate with divisions, consultants and outside agencies whose priorities conflict, and I "
        "write the briefing notes, memos and presentations that carry findings and recommendations to "
        "management. Working inside the City gives me a practical sense of how a change has to move through a "
        "division before it sticks.",

        "I should be straightforward about the gaps. I have not led an enterprise-wide transformation, I am not "
        "trained in Prosci or Lean Six Sigma and hold no change management accreditation, and I have not led "
        "staff, administered a project budget or designed training programmes. I have not used Power BI, "
        "Tableau or VBA. I am applying because automation and adoption are the parts of this work I have "
        "actually done, and because the Qualified List covers permanent and temporary positions.",

        "Thank you for considering my application.",
    ])


# ================================================ 66777 Project Manager TW, Capital Planning & Implementation

RESUME_66777 = resume(
    "Civil engineer with a master's degree in transportation engineering, currently an Assistant Planner with "
    "the City of Toronto. Reviews engineering submissions, consultant studies and drawings against City "
    "standards, runs assigned projects from scoping to recommendations, and explains technical work to the "
    "people making decisions on it.",
    city(REVIEW_ENG, PROJECTS, CAPITAL, COORD, BRIEFING)
    + metrolinx(OPENTRACK, SLOW, CLI, CVT) + MOTT + UOFA,
    skills=skills("Review of engineering submissions, drawings and specifications. Project planning, scheduling "
                  "and follow-through. Communicating technical work to non-technical audiences. Coordination with "
                  "divisions, consultants and agencies. Python (Pandas, NumPy), SQL, ArcGIS and QGIS. MS Office."))

COVER_66777 = letter(
    "Lina Truong", "Human Resources", "Toronto Water, City of Toronto",
    "Re: Project Manager TW, Capital Planning & Implementation (Job ID 66777)", "Dear Lina Truong,",
    [
        "I would like to apply for one of the Project Manager TW positions with Toronto Water's Capital Planning "
        "and Implementation section. I am a civil engineer and an Assistant Planner with the City, and I would "
        "welcome the chance to move closer to the delivery of municipal infrastructure.",

        "The posting asks for someone to lead the review of drawings, purchasing documents and specifications "
        "prepared by staff, contractors and consultants. At the City I review engineering submissions, "
        "consultant studies and drawings against City standards and recommend conditions where something is "
        "missing, and I run assigned projects from scoping through to recommendations while holding the "
        "schedule and quality myself. I also analyze network data to work out where capacity is short and what "
        "that means for maintenance and capital spending.",

        "The posting places weight on communicating technical information to non-technical audiences and on "
        "working in an operational environment. Much of my job is explaining technical findings to managers in "
        "other divisions through briefing notes and memos. At Metrolinx I worked on an operating railway, "
        "assessing what construction-related speed restrictions would do to service. "
        + TOOLS_SENTENCE,

        "I should be straightforward about the gaps. I do not currently hold a Class G licence, which the "
        "posting lists as a requirement, so I would need to resolve that. I have not managed municipal "
        "infrastructure design and construction, administered contracts and payments, or directed staff, and "
        "my knowledge of the Occupational Health and Safety Act is general. I do not hold a PMP or P.Eng. I am "
        "applying because the review and project coordination parts of the role are familiar, and because the "
        "Qualified List covers permanent and temporary positions.",

        "Thank you for considering my application.",
    ])


# ================================================ 67150 Project Manager, Fleet Safety Operations & CI

RESUME_67150 = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner with the City of Toronto "
    "and previously in operations analysis at Metrolinx. Analyzes large volumes of operational data, builds "
    "KPIs and reporting, improves processes that are not working, and presents data-driven recommendations to "
    "management.",
    city(DATA_KPI, DASHBOARD, IMPROVE, BRIEFING, COORD, PROJECTS)
    + metrolinx(CVT, CLI, OPENTRACK, SCHED) + MOTT + UOFA,
    skills=skills("Analysis of large operational datasets. KPIs, dashboards and performance reporting. Continuous "
                  "improvement of processes. Python (Pandas, NumPy), SQL and advanced Excel. Reports, briefing "
                  "materials and presentations for senior management. Knowledge of City of Toronto structure and "
                  "decision-making. MS Office."))

COVER_67150 = letter(
    "Heather Anne Thompson", "Human Resources", "Fleet Services, City of Toronto",
    "Re: Project Manager, Fleet Safety Operations & Continuous Improvement (Job ID 67150)",
    "Dear Heather Anne Thompson,",
    [
        "I would like to apply for the Project Manager, Fleet Safety Operations and Continuous Improvement "
        "position with Fleet Services. I am an Assistant Planner with the City, and the parts of this role that "
        "match my experience are the data analysis, the performance measures and the continuous improvement.",

        "Qualification eight asks for experience analyzing large volumes of safety or operational data, "
        "developing key performance indicators and preparing data-driven recommendations. " + TOOLS_SENTENCE +
        " At the City I built the Transportation Data Dashboard, which combines several years of data from "
        "separate sources into one validated source and tracks divisional performance continuously rather than "
        "in a report rebuilt by hand.",

        "On continuous improvement and communication, I identify where a process is not working, coordinate the "
        "people needed to change it and see the change through to adoption, and I write the reports, briefing "
        "materials and presentations that carry recommendations to senior management. As a City employee I work "
        "within the City's structure and decision-making processes every day.",

        "I should be straightforward about the gaps, because several are central to the role. I have not worked "
        "in fleet safety or collision management, administered CVOR compliance, or used fleet telematics, and I "
        "have not directed professional, technical or administrative staff. My knowledge of the Highway Traffic "
        "Act, the Occupational Health and Safety Act and the CVOR program is general rather than practical. I do "
        "not currently hold a Class G licence. I am applying because the analytical and improvement side of the "
        "role is work I do now, and because the Qualified List covers permanent and temporary positions.",

        "Thank you for considering my application.",
    ])


# ================================================ 64397 Senior Project Manager TW, Wastewater Treatment

RESUME_64397 = resume(
    "Civil engineer with a master's degree in transportation engineering, currently an Assistant Planner with "
    "the City of Toronto. Reviews engineering submissions and drawings against City standards, analyzes "
    "operational data to find where performance can improve, and coordinates across municipal divisions and "
    "agencies.",
    city(REVIEW_ENG, DATA_KPI, PROJECTS, COORD, RESEARCH, BRIEFING)
    + metrolinx(OPENTRACK, CVT, CLI, SCHED) + MOTT + UOFA,
    skills=skills("Review of engineering submissions, drawings and specifications. Operational data analysis and "
                  "continuous improvement. Project planning and follow-through. Coordination with municipal "
                  "divisions and agencies. Python (Pandas, NumPy), SQL, ArcGIS and QGIS. MS Office."))

COVER_64397 = letter(
    "Sheena Ramcharan", "Human Resources", "Toronto Water, City of Toronto",
    "Re: Senior Project Manager TW, Water Treatment and Supply (Job ID 64397)", "Dear Sheena Ramcharan,",
    [
        "I would like to apply for the Senior Project Manager TW position with the Water Treatment and Supply "
        "section of Toronto Water. I should say at the outset that I come to it from transportation rather than "
        "water treatment, and I have tried to be clear below about both what I would bring and where I fall "
        "short.",

        "I am a civil engineer and an Assistant Planner with the City. I review engineering submissions, "
        "consultant studies and drawings against City standards, and I run assigned projects from scoping "
        "through to recommendations. The posting also asks for someone who analyzes data from operating systems "
        "to identify opportunities for improvement. " + TOOLS_SENTENCE + " At the City I built the "
        "Transportation Data Dashboard, which brought several years of operational data into one validated "
        "source the division reports from.",

        "The gaps are substantial. I have no experience in municipal water treatment, its unit processes, "
        "residuals management, pumping or storage, and I have not worked under the Safe Drinking Water Act or "
        "the Ontario Water Resources Act. I have not supervised engineers or technical staff, prepared capital "
        "and operating budgets, or prepared RFPs and tender documents. I am applying because the Qualified List "
        "covers permanent and temporary positions, and if a more junior engineering role in Water Treatment and "
        "Supply would suit my background better, I would welcome being considered for it.",

        "Thank you for considering my application.",
    ])
