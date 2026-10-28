# -*- coding: utf-8 -*-
"""28 October 2026 daily run:

    4483683186  Metrolinx, Senior Advisor, GO Market Development
    56338       City of Edmonton, Safe Mobility Analyst (closes Nov 10, 2026, 11:59 PM ABT)
    88758       Government of Alberta (Transportation and Economic Corridors), Senior Policy Advisor (closes Nov 10)
    4484251767  Urban Systems, GIS Analyst (Kamloops)
    4483671842  Coast Mountain Bus Company, Senior Advisor, Zero Emissions
    4483679321  Metrolinx, Project Manager, Permit, Licenses & Approvals
    4484288755  Dillon Consulting, Strategic Lead - Transportation Planning & Strategy (Toronto listing)
"""

import content20
from content3 import (MOTT, UOFA, resume)
from content19 import (OPENTRACK, SLOW, CVT, CLI, DASHBOARD, city, metrolinx, skills, PROJECTS, BRIEFING,
                       COORD, REVIEW_DEV, DATA_KPI, RESEARCH, SCHED)
from content20 import (TTS, AGENCIES, DEV_STUDIES, REPORTS, letter)
from content28 import (ROW, POLICY_COUNCIL, TOOLS_ALSO, UOFA_GIS, STUDIES, EVIDENCE)

content20.DATE = "October 28, 2026"

# ================================================ Metrolinx Senior Advisor, GO Market Development

RESUME_GOMKT = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner in Transportation Planning "
    "with the City of Toronto, and formerly a Transportation Planner in Service Design at Metrolinx. Brings "
    "several years of Transportation Tomorrow Survey data together into one validated source, assesses the "
    "transportation implications of development, and writes the briefing notes that carry findings to senior staff.",
    city(DASHBOARD, TTS, DEV_STUDIES, BRIEFING)
    + metrolinx(OPENTRACK, SLOW, CVT, CLI) + MOTT + UOFA_GIS,
    skills=skills("Travel demand and survey data analysis (TTS). Data integration and validation across sources. "
                  "Dashboards. ArcGIS Pro, QGIS and MapBox. Python (Pandas, NumPy), SQL and JavaScript. "
                  "OpenTrack, VISSIM, Synchro and MATSim. Briefing notes and presentations for senior staff."))

COVER_GOMKT = letter(
    "Hiring Manager", "GO Market Development", "Metrolinx",
    "Re: Senior Advisor, GO Market Development", "Dear Hiring Manager,",
    [
        "I would like to apply for the Senior Advisor position in GO Market Development. I worked at Metrolinx in "
        "2023 as a Transportation Planner in Service Design, and since January 2024 I have been an Assistant "
        "Planner in Transportation Planning at the City of Toronto.",

        "The posting asks for someone who can bring large datasets from several sources together to see where "
        "travel demand is heading. That is close to what I do at the City. I built the Transportation Data "
        "Dashboard, which brought the 2006, 2011 and 2016 Transportation Tomorrow Survey data into one validated "
        "source the division now reports from, and I analyze travel and network data to show where capacity falls "
        "short and what that means for investment. I review development applications and the transportation "
        "studies filed with them, so I am used to asking what growth in a given place means for the network. I "
        "also build and maintain the division's road and right-of-way datasets in GIS, and I write the briefing "
        "notes that carry findings to senior staff.",

        "At Metrolinx I ran OpenTrack simulations of GO rail services and assessed what slow orders would do to "
        "service, so I know the network from the operating side. " + TOOLS_ALSO,

        "I should be straightforward about the gaps. I have not done market or consumer analytics, ridership "
        "forecasting, or work with mobility and cell phone data, and I have not led technical studies as the "
        "senior person on them or managed a stakeholder relationship at this level. I have not used Tableau or "
        "Power BI. What I can offer is a sound grounding in the survey data and the GGH network, and I would "
        "need to learn the market side of the work.",

        "Thank you for considering my application.",
    ])

# ================================================ City of Edmonton Safe Mobility Analyst (56338)

RESUME_56338 = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner in Transportation Planning "
    "with the City of Toronto. Builds the datasets and dashboards that turn travel data into evidence for "
    "decisions, and writes the reports and briefing notes that carry it to senior staff.",
    city(DASHBOARD, TTS, ROW, BRIEFING)
    + metrolinx(OPENTRACK, SLOW, CVT, CLI) + MOTT + UOFA_GIS,
    skills=skills("Spatial and statistical analysis of transportation data. Data validation and dashboards. "
                  "ArcGIS Pro, QGIS and MapBox. Python (Pandas, NumPy), SQL and JavaScript. Synchro, VISSIM, "
                  "OpenTrack and MATSim. Technical reports and briefing notes."))

COVER_56338 = letter(
    "Hiring Manager", "", "Mobility Data Analysis, City of Edmonton",
    "Re: Safe Mobility Analyst (ID 56338)", "Dear Hiring Manager,",
    [
        "I would like to apply for the Safe Mobility Analyst position. I am an Assistant Planner in "
        "Transportation Planning at the City of Toronto. I did my master's degree in transportation engineering "
        "at the University of Alberta, so Edmonton is a city I know.",

        "The role is about turning transportation data into evidence people can act on, and that is the part of my "
        "work I do most. At the City I built the Transportation Data Dashboard, which brings several years of the "
        "Transportation Tomorrow Survey into one validated source, and I analyze travel and network data for "
        "trends, gaps and emerging issues. I maintain the division's road and right-of-way datasets in GIS and "
        "Python, including a right-of-way width dataset for all city roads, and I write the briefing notes and "
        "reports that carry findings to senior staff. My master's research used GIS and simulation to study how "
        "road networks perform under stress, and I took a graduate course in GIS as part of the program. "
        + TOOLS_ALSO,

        "I should be straightforward about the gaps. I have not worked with collision, near-miss or conflict data, "
        "or on Vision Zero programs, and I have not done predictive risk modelling or evaluated the effect of "
        "safety countermeasures. I have not used SPSS, R, Tableau or Google BigQuery, and my university degrees "
        "are in engineering rather than statistics. I would count the road safety side as what I need to learn, "
        "and the posting's four years of analytical experience is a little more than I have in a municipal "
        "setting.",

        "Thank you for considering my application.",
    ])

# ================================================ Government of Alberta Senior Policy Advisor (88758)

RESUME_88758 = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner in Transportation Planning "
    "with the City of Toronto. Researches policy questions, advises on by-laws and regulations, and writes the "
    "briefing notes and reports that carry issues, options and recommendations to senior staff.",
    city(POLICY_COUNCIL, BRIEFING, RESEARCH, AGENCIES, DASHBOARD)
    + metrolinx(OPENTRACK, SLOW, CVT, CLI) + MOTT + UOFA,
    skills=skills("Policy research and analysis. Briefing notes, reports and presentations for senior staff. "
                  "Coordination across divisions, agencies and consultants. Transportation data analysis. "
                  "ArcGIS Pro and QGIS. Python and SQL."))

COVER_88758 = letter(
    "Hiring Manager", "", "Strategic Policy, Transportation and Economic Corridors, Government of Alberta",
    "Re: Senior Policy Advisor (Requisition 88758)", "Dear Hiring Manager,",
    [
        "I would like to be considered for the Senior Policy Advisor position in Strategic Policy. I am an "
        "Assistant Planner in Transportation Planning at the City of Toronto, and I did my master's degree in "
        "transportation engineering at the University of Alberta.",

        "The posting describes policy research, options analysis and briefing materials for senior officials, "
        "and that is the kind of writing I do. At the City I research policy questions as they come up, looking at "
        "how City policy, provincial legislation and the work of other levels of government bear on them, and I "
        "write the briefing notes and memos that carry issues, options and recommendations to senior staff. I "
        "advise on by-laws and regulations, and with policy staff I have helped report to Council on new "
        "transportation regulations. I coordinate with divisions, consultants and outside agencies whose "
        "priorities conflict, and I run assigned projects from scoping through to recommendations.",

        "I also bring a technical grounding that policy staff do not always have. At Metrolinx I ran OpenTrack "
        "simulations of GO rail services, and at the City I built the Transportation Data Dashboard, which brings "
        "several years of travel survey data into one validated source. " + TOOLS_ALSO,

        "I should be straightforward about the gaps. I have not worked on provincial legislation or Cabinet "
        "materials, or done Gender-Based Analysis Plus. I have not prepared requests for proposals or "
        "managed contractors through an evaluation, and I have not led stakeholder engagement with Indigenous "
        "communities or other ministries. My degrees are in engineering rather than public administration or "
        "political science, though the posting names a related field and I have worked in policy support for "
        "about three years. I have not worked in Alberta's government, and I would need to learn its processes.",

        "Thank you for considering my application.",
    ])

# ================================================ Urban Systems GIS Analyst

RESUME_USGIS = resume(
    "Transportation engineer with a master's degree and four years of GIS and data work across municipal "
    "transportation planning at the City of Toronto and rail service planning at Metrolinx. Builds the "
    "spatial datasets a division depends on, and the Python tooling that automates the processing.",
    city(ROW, DASHBOARD, TTS, STUDIES)
    + metrolinx(OPENTRACK, CVT, CLI, EVIDENCE) + MOTT + UOFA_GIS,
    skills=skills("ArcGIS Pro, QGIS and MapBox. Python (Pandas, NumPy), SQL and JavaScript for spatial data "
                  "processing and automation. Data integration, validation and dashboards. AutoCAD and "
                  "Civil 3D. OpenTrack, VISSIM, Synchro and MATSim. Maps, reports and presentations."))
RESUME_USGIS = [l.replace("fully funded by the university.", "fully funded by the university; graduate course in GIS.")
                for l in RESUME_USGIS]

COVER_USGIS = letter(
    "Hiring Manager", "", "Urban Systems, Kamloops Office",
    "Re: GIS Analyst, Kamloops", "Dear Hiring Manager,",
    [
        "I would like to apply for the GIS Analyst position in the Kamloops office. I am an Assistant Planner in "
        "Transportation Planning at the City of Toronto, where much of my work is building and looking after the "
        "spatial data the division relies on.",

        "I build and maintain the road and right-of-way datasets Transportation Planning depends on, using ArcGIS "
        "Pro, QGIS, Python and SQL, including a right-of-way width dataset covering all city roads, built with "
        "QGIS, MapBox and JavaScript. I also built the Transportation Data Dashboard, which brought several years "
        "of travel survey data into one validated source. The posting asks for someone who sees where integration "
        "and automation can help, and " + TOOLS_ALSO[0].lower() + TOOLS_ALSO[1:]
        + " My master's thesis used GIS and simulation to assess community capacity for wildfire evacuation, "
        "and I took a graduate course in GIS as part of that program. I also use AutoCAD and Civil 3D.",

        "I should be straightforward about the gaps. I do not hold a GIS degree, diploma or certificate; my "
        "training is a graduate course in GIS and my work. I have not worked with ArcGIS Online in a consulting "
        "setting, digitized as-built drawings, maintained infrastructure asset inventories for a utility, or "
        "worked with reality capture, geomatics or remote sensing. I have not worked in British Columbia, and "
        "my GIS work has been in transportation rather than civil infrastructure.",

        "Thank you for considering my application.",
    ])

# ================================================ Coast Mountain Bus Company Senior Advisor, Zero Emissions

RESUME_CMBC = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner in Transportation Planning "
    "with the City of Toronto, and formerly a Transportation Planner in Service Design at Metrolinx. Builds "
    "the datasets, dashboards and Python tools that turn operations data into evidence for decisions.",
    city(DASHBOARD, TTS, DATA_KPI, BRIEFING)
    + metrolinx(OPENTRACK, SLOW, CVT, CLI) + MOTT + UOFA,
    skills=skills("Analysis of transit operations and service data. Python (Pandas, NumPy), SQL and JavaScript. "
                  "Dashboards and performance reporting. OpenTrack, VISSIM, Synchro and MATSim. ArcGIS Pro and "
                  "QGIS. Technical reports and presentations for senior staff."))

COVER_CMBC = letter(
    "Hiring Manager", "", "Low Carbon Fleet Programs, Coast Mountain Bus Company",
    "Re: Senior Advisor, Zero Emissions", "Dear Hiring Manager,",
    [
        "I would like to be considered for the Senior Advisor, Zero Emissions position. I am an Assistant "
        "Planner in Transportation Planning at the City of Toronto, and in 2023 I worked at Metrolinx as a "
        "Transportation Planner in Service Design, simulating GO rail services.",

        "The posting asks for analytical frameworks, dashboards and models that support decisions on how a "
        "transit fleet is operated. That is the kind of work I have done. At Metrolinx I ran OpenTrack "
        "simulations of GO services to establish what proposed changes would do to run times and reliability "
        "before anyone committed to them. " + TOOLS_ALSO + " At the City I built the Transportation Data "
        "Dashboard, which brings several years of travel survey data into one validated source, and I write the "
        "technical reports and briefing notes that carry findings to senior staff.",

        "I should be straightforward about the gaps. I have no experience with zero-emission buses, charging "
        "infrastructure, energy modelling or greenhouse gas reporting, and I have not worked with Fabric, Power BI "
        "or machine learning. The posting asks for seven years of analysis experience and I have closer to four. "
        "It also includes managing staff and overseeing consultants, and I have done neither. I would be coming to "
        "the subject as a learner, with the data and simulation skills to build on.",

        "Thank you for considering my application.",
    ])

# ================================================ Metrolinx Project Manager, Permit, Licenses & Approvals

RESUME_PLA = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner in Transportation Planning "
    "with the City of Toronto, where reviewing development applications and advising on by-laws and regulations "
    "is part of the job. Formerly a Transportation Planner at Metrolinx. Coordinates across divisions, agencies "
    "and applicants whose priorities conflict.",
    city(REVIEW_DEV, AGENCIES, PROJECTS, POLICY_COUNCIL)
    + metrolinx(OPENTRACK, SLOW, CVT, CLI) + MOTT + UOFA,
    skills=skills("Development application review against City standards and Official Plan policy. Knowledge "
                  "of municipal by-laws and regulations. Project planning, tracking and follow-through. "
                  "Coordination across divisions, agencies and applicants. Briefing notes and presentations. "
                  "Synchro, AutoCAD and Civil 3D. Python, SQL, ArcGIS Pro and QGIS."))

COVER_PLA = letter(
    "Hiring Manager", "Operational Planning & Interface Management, Capital Projects Group", "Metrolinx",
    "Re: Project Manager, Permit, Licenses & Approvals", "Dear Hiring Manager,",
    [
        "I would like to apply for the Project Manager, Permit, Licenses & Approvals position. I worked at "
        "Metrolinx in 2023 as a Transportation Planner in Service Design, and since January 2024 I have been an "
        "Assistant Planner in Transportation Planning at the City of Toronto.",

        "At the City I sit on the approval-authority side of the process the posting describes. I review "
        "development applications and the transportation studies filed with them against City standards and "
        "Official Plan policy, recommend conditions where something is missing, and advise on by-laws and "
        "regulations. I coordinate with divisions, consultants, applicants and outside agencies whose priorities "
        "conflict, and work issues through to a position everyone can act on. I run assigned projects from "
        "scoping through to recommendations, holding the schedule myself, and I know the Planning Act "
        "process from the City's side. At Mott MacDonald I worked on road-closure traffic simulation for Ontario "
        "Line construction staging, so I have seen what a construction schedule has to get past before a "
        "road can be closed. " + TOOLS_ALSO,

        "I should be straightforward about the gaps. I have not prepared or tracked permit applications for a "
        "construction project, or dealt with the Environmental Assessment Act and O. Reg. 231/08, the Ontario "
        "Water Resources Act or heritage approvals. I have not worked with design-build delivery or contract "
        "administration, and I have not negotiated with approval authorities on a project's behalf. My experience "
        "is with the municipal side of review, and I would need to learn the construction side.",

        "Thank you for considering my application.",
    ])

# ================================================ Dillon Strategic Lead - Transportation Planning & Strategy

RESUME_DILLON = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner in Transportation Planning "
    "with the City of Toronto, and formerly a Transportation Planner at Metrolinx and a Graduate Transportation "
    "Planner at Mott MacDonald. Reviews development applications and their transportation studies, analyzes "
    "travel data, and writes the briefing notes that carry findings to senior staff.",
    city(DEV_STUDIES, TTS, DASHBOARD, AGENCIES, POLICY_COUNCIL)
    + metrolinx(OPENTRACK, SLOW, CVT, CLI) + MOTT + UOFA,
    skills=skills("Transportation planning and travel data analysis. Development review. Synchro, VISSIM, "
                  "OpenTrack and MATSim simulation. Python, SQL, ArcGIS Pro and QGIS. Technical reports, "
                  "briefing notes and presentations."))

COVER_DILLON = letter(
    "Hiring Manager", "Integrated Mobility", "Dillon Consulting Limited",
    "Re: Strategic Lead, Transportation Planning & Strategy (Toronto)", "Dear Hiring Manager,",
    [
        "I would like to be considered for the Strategic Lead, Transportation Planning & Strategy position. I "
        "am an Assistant Planner in Transportation Planning at the City of Toronto, and I am writing knowing "
        "that this is a senior role for which I am early in my career.",

        "The technical work the posting lists is work I have done at a smaller scale. At the City I review "
        "development applications and the transportation studies filed with them, analyze travel and network "
        "data, and coordinate with divisions, consultants, applicants and outside agencies whose priorities "
        "conflict. At Mott MacDonald I did traffic simulation in Synchro for Ontario Line construction staging, "
        "and at Metrolinx I ran OpenTrack simulations of GO rail services. My master's research at the "
        "University of Alberta used macroscopic and agent-based simulation. " + TOOLS_ALSO,

        "I should be plain about the gaps, because they are large. The posting asks for twelve years of "
        "experience and six in project management; I have about four years of professional work. I have not led "
        "project teams or staff, managed budgets, developed business for a firm, or led proposals. I have not "
        "worked on Municipal Class Environmental Assessments, functional design of corridors, or master plans. I "
        "do not hold a P.Eng. I understand if the role is out of reach, and I would be glad to be considered "
        "for a transportation planner position if the team has one.",

        "Thank you for considering my application.",
    ])
