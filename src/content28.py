# -*- coding: utf-8 -*-
"""13 October 2026 catch-up: senior roles the daily runs missed between 13 September and
12 October (the finder had no GIS keywords and no employer sweeps)."""

import content20
from content3 import (NAME, CONTACT, MOTT, UOFA, resume)
from content19 import (OPENTRACK, SLOW, CVT, CLI, DASHBOARD, TOOLS_SENTENCE, city, metrolinx, skills,
                       REVIEW_DEV, BRIEFING, PROJECTS, COORD, SCHED, DATA_KPI, IMPROVE, CAPITAL)
from content20 import (TTS, DEV_STUDIES, REPORTS, AGENCIES, letter, VALIDATED, OT_BUILD)

content20.DATE = "October 13, 2026"

ROW = ("B: Build and maintain the road and right-of-way datasets the division depends on, using GIS and Python, "
       "including a ROW-width dataset covering all city roads, built with QGIS, MapBox and JavaScript.")
STUDIES = ("B: Run assigned studies from scoping through to recommendations, writing the briefing notes that come "
           "out of them and presenting to planners, engineers and managers in other divisions.")
EVIDENCE = ("B: Worked with schedulers, operations staff and engineers on service design decisions and presented "
            "the evidence behind them.")
TOOLS_ALSO = ("I also set up a command line workflow that pre-simulated slow orders in batches, cutting turnaround "
              "on scenario requests from days to hours, and built the Crew Variance Tool, a Python application "
              "that read large JSON operations files and summarised speed profiles and run-time variance across "
              "subdivisions.")
UOFA_GIS = [
    "SUB: Graduate Research Assistant",
    "DATE: University of Alberta  |  January 2020 – August 2022",
    "B: Master's research on how road networks perform during emergency evacuations, using macroscopic (LWR) "
    "and agent-based (MATSim) models.",
    "B: Spatial analysis of large transportation datasets in GIS, turning data into recommendations for safer "
    "wildfire evacuation plans in Alberta communities.",
]


# ================================================ Metrolinx Engineering Lead - GIS

RESUME_MX_GIS = resume(
    "Transportation engineer with a master's degree and four years of GIS and data work across municipal "
    "transportation planning at the City of Toronto and GO rail service planning at Metrolinx. Builds the "
    "spatial datasets a division depends on and turns scattered sources into one validated source people "
    "report from.",
    city(ROW, DASHBOARD, TTS, STUDIES)
    + metrolinx(OPENTRACK, CVT, CLI, EVIDENCE) + MOTT + UOFA_GIS,
    skills=skills("ArcGIS Pro, QGIS and MapBox. Python (Pandas, NumPy), SQL and JavaScript for spatial data "
                  "processing and automation. Data integration, validation and dashboards. OpenTrack, VISSIM, "
                  "Synchro and MATSim. AutoCAD and Civil 3D. Advanced Excel, including large multi-source "
                  "workbooks. Briefing notes and presentations for senior staff."))

COVER_MX_GIS = letter(
    "Talent Acquisition", "Engineering & Safety Division", "Metrolinx, 20 Bay Street, Toronto, ON",
    "Re: Engineering Lead - Geographic Information Systems (GIS)", "Dear Hiring Manager,",
    [
        "I would like to apply for the Engineering Lead, Geographic Information Systems position in the "
        "Engineering and Safety Division. I worked at Metrolinx in 2023 as a Transportation Planner in Service "
        "Design, and since January 2024 I have been an Assistant Planner in Transportation Planning at the City "
        "of Toronto, where much of my work is building and looking after the spatial data the division relies on.",

        "At the City I build and maintain the road and right-of-way datasets Transportation Planning depends "
        "on, using GIS and Python, including a right-of-way width dataset covering all city roads, built with "
        "QGIS, MapBox and JavaScript. I also built the Transportation Data Dashboard, which combined several "
        "years of Transportation Tomorrow Survey data into one validated source the division now reports from. "
        "The posting describes bringing location, condition, performance and project information together so "
        "that decisions rest on one consistent picture of the network. That is the problem I have been "
        "working on, at the scale of one division.",

        "At Metrolinx I saw the railway from the operations side. I ran OpenTrack simulations of GO rail "
        "services to test how infrastructure constraints and speed restrictions changed run times and "
        "reliability, and presented that evidence to schedulers, operations staff and engineers. " + TOOLS_ALSO
        + " My master's thesis used GIS and macro-simulation to assess community "
        "transportation capacity for wildfire evacuation.",

        "I should be straightforward about the gaps. I have not led a GIS program or set geospatial "
        "governance, standards and data models for an organization; my GIS work has been building and "
        "maintaining datasets and tools within one division. I have not worked in asset management or State "
        "of Good Repair planning, integrated GIS with an enterprise asset management system, or led staff, "
        "consultants or vendors, and I do not hold a professional certification. I am applying because the "
        "spatial analysis and data integration at the centre of the role is the work I do now.",

        "Thank you for considering my application.",
    ])


POLICY_COUNCIL = ("B: Advise applicants and staff on transportation planning, by-laws and related regulations, and with "
                  "policy staff recommend and report to Council on new transportation regulations and guidelines.")


# ================================================ Ontario Public Service - Manager, GO/LRT

RESUME_OPS_GOLRT = resume(
    "Transportation engineer with a master's degree and four years across municipal transportation planning at "
    "the City of Toronto and GO rail service planning at Metrolinx. Reviews development applications against "
    "Official Plan policy, coordinates across divisions, agencies and applicants whose priorities conflict, and "
    "writes the briefing notes that carry issues and options to senior staff.",
    city(DEV_STUDIES, POLICY_COUNCIL, AGENCIES, STUDIES, TTS)
    + metrolinx(OPENTRACK, SLOW, CVT, CLI) + MOTT + UOFA,
    skills=skills("Development application review against City standards and Official Plan policy. Transit and "
                  "rail service planning. Briefing notes, reports and presentations for senior staff. Coordination "
                  "across divisions, agencies, consultants and applicants. Python (Pandas, NumPy), SQL, ArcGIS Pro "
                  "and QGIS. OpenTrack, VISSIM, Synchro and MATSim. MS Office."))

COVER_OPS_GOLRT = letter(
    "Avril Bundale", "Director, Transit Oriented Communities Policy and Delivery Branch",
    "Ontario Public Service, Toronto, ON",
    "Re: Manager, GO/LRT", "Dear Avril Bundale,",
    [
        "I would like to apply for the Manager, GO/LRT position in the Transit Oriented Communities Policy and "
        "Delivery Branch. I am an Assistant Planner in Transportation Planning at the City of Toronto, and before "
        "that I was a Transportation Planner at Metrolinx, in GO rail service design. The branch works where "
        "transit investment meets land use and development, and that is where my work has been.",

        "At the City I review development applications and the transportation studies filed with them against "
        "City standards and Official Plan policy, and recommend conditions where something is missing. I advise "
        "applicants and staff on transportation planning and related regulations, and with policy staff I "
        "recommend and report to Council on new transportation regulations and guidelines. I coordinate with "
        "divisions, consultants, applicants and outside agencies whose priorities often conflict, and I write the "
        "briefing notes and presentations that carry issues and options to managers in other divisions.",

        "At Metrolinx I ran OpenTrack simulations of GO rail services to test how infrastructure constraints and "
        "speed restrictions changed run times and reliability, and worked with schedulers, operations staff and "
        "engineers on service design decisions. " + TOOLS_ALSO,

        "I should be straightforward about the gaps. This is a people leadership role, and I have not supervised "
        "staff. I have not led transit-oriented community projects, land transactions or government approvals "
        "such as Treasury Board submissions, and I have not worked in municipal finance. I am applying because "
        "the land use, development and partner side of the role is the work I do every day, from the municipal "
        "side of the table, and I would welcome the chance to bring it to the Province's side.",

        "Thank you for considering my application.",
    ])


# ================================================ City of Mississauga - Supervisor, Traffic Planning

RESUME_MISS_TRAFFIC = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner with the City of Toronto, "
    "where reviewing development applications and the transportation studies filed with them is a core part of "
    "the job. Has run traffic simulation of Ontario Line construction staging and rail simulation of GO services, "
    "and writes the reports and briefing notes that carry findings to decision-makers.",
    city(DEV_STUDIES, POLICY_COUNCIL, STUDIES, AGENCIES, TTS)
    + metrolinx(OPENTRACK, SLOW, CVT, CLI) + MOTT + UOFA,
    skills=skills("Review of development applications and transportation studies against City standards and "
                  "Official Plan policy. Synchro and VISSIM; OpenTrack and MATSim. ArcGIS Pro, QGIS and MapBox. "
                  "Python (Pandas, NumPy) and SQL. AutoCAD and Civil 3D. Reports, briefing notes and presentations "
                  "for senior staff. MS Office."))

COVER_MISS_TRAFFIC = letter(
    "Human Resources", "Planning & Building Department", "City of Mississauga, Mississauga, ON",
    "Re: Supervisor, Traffic Planning (Req ID 28597)", "Dear Hiring Manager,",
    [
        "I would like to apply for the Supervisor, Traffic Planning position in the Development Engineering & "
        "Construction section. I am an Assistant Planner in Transportation Planning at the City of Toronto, and "
        "reviewing development applications from a transportation perspective is the core of what I do.",

        "At the City I review development applications and the transportation studies filed with them against "
        "City standards and Official Plan policy, and recommend conditions where something is missing. I advise "
        "applicants and staff on transportation planning, by-laws and related regulations, monitor the effect of "
        "zoning regulations, and with policy staff recommend and report to Council on new transportation "
        "regulations and guidelines. I run assigned studies from scoping through to recommendations and present "
        "to planners, engineers and managers in other divisions.",

        "At Mott MacDonald I ran Synchro traffic simulations to estimate how Ontario Line construction staging and "
        "road closures would affect the surrounding streets, and at Metrolinx I ran OpenTrack simulations of GO "
        "rail services. " + TOOLS_ALSO,

        "I should be straightforward about the gaps. The posting asks for eight years of related experience, "
        "including three in a leadership role. I have about four and a half years, and I have not supervised "
        "staff, set work plans for a team, or procured and managed consultants. I am not registered with "
        "Professional Engineers Ontario, which the posting lists as preferred, and I do not hold a Class G "
        "licence, so I would reach meetings and sites by other means. I am applying because the review work your "
        "team does is the work I do now.",

        "Thank you for considering my application.",
    ])


# ================================================ Region of Durham - Senior Planner (24244)

RESUME_DURHAM = resume(
    "Transportation engineer with a master's degree and four years across municipal transportation planning at "
    "the City of Toronto and GO rail service planning at Metrolinx. Analyzes travel and network data including "
    "the Transportation Tomorrow Survey, builds the datasets and dashboards a division reports from, and reviews "
    "development applications against Official Plan policy.",
    city(TTS, DASHBOARD, ROW, DEV_STUDIES)
    + metrolinx(OPENTRACK, CVT, CLI, EVIDENCE) + MOTT + UOFA_GIS,
    skills=skills("Transportation and growth data analysis, including the Transportation Tomorrow Survey. ArcGIS "
                  "Pro, QGIS and MapBox. Python (Pandas, NumPy), SQL and JavaScript; datasets, dashboards and data "
                  "validation. Development application review against Official Plan policy. Reports, briefing "
                  "notes and presentations. OpenTrack, VISSIM, Synchro and MATSim. MS Office."))

COVER_DURHAM = letter(
    "Human Resources", "Community Growth and Economic Development Department",
    "Regional Municipality of Durham, Whitby, ON",
    "Re: Senior Planner (Job ID 24244)", "Dear Hiring Manager,",
    [
        "I would like to apply for the Senior Planner position, and in particular for the opening in the "
        "Transportation Planning section. I am an Assistant Planner in Transportation Planning at the City of "
        "Toronto, and before that I was a Transportation Planner at Metrolinx. I hold a master's degree in "
        "Transportation Engineering.",

        "The posting puts weight on transportation and growth monitoring, planning data, and the technology "
        "behind it. At the City I analyze travel and network data, including several years of the Transportation "
        "Tomorrow Survey, to work out where capacity is short and what that means for future investment. I built "
        "the Transportation Data Dashboard, which combined the 2006, 2011 and 2016 surveys into one validated "
        "source the division reports from, and I build and maintain the road and right-of-way datasets the "
        "division depends on, using GIS and Python.",

        "I also review development applications and the transportation studies filed with them against City "
        "standards and Official Plan policy, run assigned studies from scoping through to recommendations, and "
        "present to planners, engineers and managers in other divisions. At Metrolinx I ran OpenTrack "
        "simulations of GO rail services. " + TOOLS_ALSO,

        "I should be straightforward about the gaps. My degrees are in civil and transportation engineering "
        "rather than planning or geography, and I am not a member of CIP or OPPI; I would need to confirm whether "
        "my experience makes me eligible for the RPP designation. I have not presented evidence at the Ontario "
        "Land Tribunal, and my policy work has supported policy staff rather than led the formulation of "
        "provincial or regional policy.",

        "Thank you for considering my application.",
    ])


# ================================================ SYSTRA - GIS Manager, GO Expansion Program

RESUME_SYSTRA_GIS = RESUME_MX_GIS

COVER_SYSTRA_GIS = letter(
    "Talent Acquisition", "", "SYSTRA Canada, Toronto, ON",
    "Re: GIS Manager, GO Expansion Program", "Dear Hiring Manager,",
    [
        "I would like to apply for one of the two GIS Manager positions supporting the GO Expansion Program. I "
        "worked at Metrolinx in 2023 as a Transportation Planner in Service Design, on the GO network the program "
        "is expanding, and since January 2024 I have been an Assistant Planner in Transportation Planning at the "
        "City of Toronto, where much of my work is building and maintaining the spatial data the division relies on.",

        "At the City I build and maintain the road and right-of-way datasets Transportation Planning depends on, "
        "using GIS and Python, including a right-of-way width dataset covering all city roads, built with QGIS, "
        "MapBox and JavaScript. I also built the Transportation Data Dashboard, which combined several years of "
        "Transportation Tomorrow Survey data into one validated source the division now reports from. Looking for "
        "the places where automation and better data could replace manual work is how I approach a dataset.",

        "At Metrolinx I ran OpenTrack simulations of GO rail services to test how infrastructure constraints and "
        "speed restrictions changed run times and reliability, and presented that evidence to schedulers, "
        "operations staff and engineers. " + TOOLS_ALSO,

        "I should be straightforward about the gaps. I have not administered ArcGIS Enterprise, or set an "
        "enterprise GIS roadmap, governance framework or data standards, and I have not managed GIS staff, "
        "budgets or vendors. Of the tools listed, I work in ArcGIS Pro, Python and SQL, but I have not used FME, "
        "Arcade, Field Maps, Survey123, Jira or Power BI. I am applying because the data integration and "
        "automation at the centre of the role is the work I do now, and I know the network it serves.",

        "Thank you for considering my application.",
    ])


# ================================================ Toronto Pearson - Senior Capacity Planning Analyst

RESUME_PEARSON = resume(
    "Transportation engineer with a master's degree whose work has centred on capacity, modelling and data: "
    "OpenTrack rail simulation at Metrolinx, agent-based (MATSim) and macroscopic network models in graduate "
    "research, and travel and network data analysis at the City of Toronto. Builds the Python tooling and "
    "datasets behind the analysis and presents results to the people who act on them.",
    city(TTS, DASHBOARD, ROW, STUDIES)
    + metrolinx(OPENTRACK, CVT, CLI, EVIDENCE) + MOTT + UOFA,
    skills=skills("Simulation: OpenTrack, VISSIM, Synchro and MATSim. Python (Pandas, NumPy) and SQL for analysis "
                  "and automation. Advanced Excel, including large multi-source workbooks. ArcGIS Pro and QGIS. "
                  "Dashboards, reports and presentations for technical and non-technical audiences."))

COVER_PEARSON = letter(
    "Talent Acquisition", "Airport Operations", "Greater Toronto Airports Authority, Toronto, ON",
    "Re: Senior Capacity Planning Analyst", "Dear Hiring Manager,",
    [
        "I would like to apply for the Senior Capacity Planning Analyst position with the Capacity Allocation "
        "team. I am a transportation engineer with a master's degree, and much of my work has been about "
        "capacity: how much a network can carry, where it falls short, and what a change would do to it.",

        "At Metrolinx I ran OpenTrack simulations of GO rail services to test how infrastructure constraints and "
        "speed restrictions changed run times, reliability and recovery, and presented that evidence to "
        "schedulers, operations staff and engineers. " + TOOLS_ALSO + " My master's research modelled how road "
        "networks perform during emergency evacuations, using macroscopic (LWR) and agent-based (MATSim) models.",

        "At the City of Toronto I analyze travel and network data, including several years of the Transportation "
        "Tomorrow Survey, to work out where capacity is short and what that means for future investment. I built "
        "the Transportation Data Dashboard, which brought several years of survey data into one validated source "
        "the division reports from, and I write up results for readers without a modelling background.",

        "I should be straightforward about the gaps. I have not worked at an airport or with airport data, so "
        "gating, towing, slot and schedule analysis would be new to me, as would airport simulation tools. I have "
        "not used Power BI, Visual Basic, Access, Oracle or Microsoft Fabric. The posting prefers eight years of "
        "professional experience; I have about four and a half, plus my graduate research.",

        "Thank you for considering my application.",
    ])


# ================================================ Metrolinx - Sponsor Officer, GO Expansion

RESUME_MX_SPONSOR = resume(
    "Transportation engineer with a master's degree and four years across GO rail service planning at Metrolinx "
    "and municipal transportation planning at the City of Toronto. Takes problems from scoping to "
    "recommendations, builds the evidence behind them, and writes the briefing notes and presentations that carry "
    "issues and options to decision-makers.",
    city(STUDIES, AGENCIES, TTS, DASHBOARD)
    + metrolinx(OPENTRACK, EVIDENCE, CVT, CLI) + MOTT + UOFA,
    skills=skills("Briefing notes, reports and presentations for senior staff. Evidence-based analysis of options "
                  "and trade-offs. Coordination across divisions, agencies and consultants. OpenTrack, VISSIM, "
                  "Synchro and MATSim. Python (Pandas, NumPy), SQL, ArcGIS Pro and QGIS. Advanced Excel. MS Office."))

COVER_MX_SPONSOR = letter(
    "Talent Acquisition", "Integrated Delivery", "Metrolinx, 97 Front Street West, Toronto, ON",
    "Re: Sponsor Officer, GO Expansion", "Dear Hiring Manager,",
    [
        "I would like to apply for the Sponsor Officer, GO Expansion position in the Integrated Delivery "
        "division. I worked at Metrolinx in 2023 as a Transportation Planner in Service Design, testing GO service "
        "plans in simulation, and since January 2024 I have been an Assistant Planner in Transportation Planning "
        "at the City of Toronto.",

        "The role is about taking unclear issues through to a decision: working out the key questions, building "
        "the evidence, and writing it up so that senior management can act. That is the shape of my work at the "
        "City. I run assigned studies from scoping through to recommendations, write the briefing notes that come "
        "out of them, and present to planners, engineers and managers in other divisions. I coordinate with "
        "divisions, consultants, applicants and outside agencies whose priorities conflict, and work issues "
        "through to a position everyone can act on.",

        "At Metrolinx I ran OpenTrack simulations of GO rail services to establish what proposed operating and "
        "infrastructure changes would do to run times, reliability and recovery before they were taken forward, "
        "and worked with schedulers, operations staff and engineers on service design decisions. " + TOOLS_ALSO
        + " So I know the GO network, and the questions a service increase raises, from the operating side.",

        "I should be straightforward about the gaps. I have not worked in a sponsor or benefits-realization role, "
        "managed against a business case, or taken items through governance approvals, and I have not managed a "
        "portfolio of initiatives. I do not hold a P.Eng., RPP or PMP, which the posting lists as assets.",

        "Thank you for considering my application.",
    ])
