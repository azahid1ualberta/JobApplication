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


# ================================================ Metrolinx - Senior Advisor, Agreements

RESUME_MX_AGREE = resume(
    "Transportation engineer with a master's degree and four years across municipal transportation planning at "
    "the City of Toronto and GO rail service planning at Metrolinx. Works with municipal divisions, agencies, "
    "consultants and applicants whose priorities conflict, reviews development applications against City "
    "standards and Official Plan policy, and writes the briefing notes that carry issues to senior staff.",
    city(AGENCIES, DEV_STUDIES, POLICY_COUNCIL, STUDIES)
    + metrolinx(OPENTRACK, SLOW, CVT, CLI) + MOTT + UOFA,
    skills=skills("Coordination across municipal divisions, agencies, consultants and applicants. Development "
                  "application review against City standards and Official Plan policy. Briefing notes, reports and "
                  "presentations for senior staff. Rail service planning and the effect of construction on an "
                  "operating railway. Python (Pandas, NumPy), SQL, ArcGIS Pro and QGIS. MS Office."))

COVER_MX_AGREE = letter(
    "Talent Acquisition", "Capital Projects Group, Third Party Coordination - Agreements",
    "Metrolinx, 20 Bay Street, Toronto, ON",
    "Re: Senior Advisor, Agreements", "Dear Hiring Manager,",
    [
        "I would like to apply for one of the two Senior Advisor, Agreements positions with the Third Party "
        "Coordination team in the Capital Projects Group. I am an Assistant Planner in Transportation Planning at "
        "the City of Toronto, and before that I was a Transportation Planner at Metrolinx in GO rail service "
        "design, so I know both sides of the table these agreements are negotiated across.",

        "At the City I review development applications and the transportation studies filed with them against "
        "City standards and Official Plan policy, and recommend conditions where something is missing. I advise "
        "applicants and staff on transportation planning and related regulations, and I coordinate with "
        "divisions, consultants, applicants and outside agencies whose priorities conflict, working issues "
        "through to a position everyone can act on. That has taught me which parts of a municipality a request "
        "touches and how its conditions get set.",

        "At Metrolinx I ran OpenTrack simulations of GO rail services and assessed what temporary and permanent "
        "slow orders, the kind of restriction construction on an operating railway imposes, would do to service. "
        + TOOLS_ALSO,

        "I should be straightforward about the gaps. I have not negotiated or drafted agreements, and I have not "
        "worked on P3 financing or procurement. I would also be learning the legislative side of agreements "
        "work, including the Environmental Assessment Act and the Occupational Health and Safety Act. I am "
        "applying because the coordination with municipalities at the centre of the role is work I do every day.",

        "Thank you for considering my application.",
    ])


# ================================================ Metrolinx - Operational Readiness Specialist

RESUME_MX_OPREADY = resume(
    "Transportation engineer with a master's degree and four years across GO rail service planning at Metrolinx "
    "and municipal transportation planning at the City of Toronto. Has assessed what construction restrictions "
    "do to an operating railway, simulated Ontario Line construction staging, and reviews consultant studies "
    "against standards.",
    city(DEV_STUDIES, STUDIES, AGENCIES, DASHBOARD)
    + metrolinx(OPENTRACK, SLOW, EVIDENCE, CVT, CLI) + MOTT + UOFA,
    skills=skills("Operational impact assessment: OpenTrack rail simulation and Synchro traffic simulation of "
                  "construction staging. Review of consultant studies and submissions against standards. AutoCAD "
                  "and Civil 3D. Reports, briefings and presentations. Python (Pandas, NumPy), SQL, ArcGIS Pro and "
                  "QGIS. MS Office."))

COVER_MX_OPREADY = letter(
    "Talent Acquisition", "GO & UP Operational Readiness & Performance", "Metrolinx, Toronto, ON",
    "Re: Operational Readiness Specialist", "Dear Hiring Manager,",
    [
        "I would like to apply for the Operational Readiness Specialist position in the GO & UP Operational "
        "Readiness & Performance division. I worked at Metrolinx in 2023 as a Transportation Planner in Service "
        "Design, and since January 2024 I have been an Assistant Planner in Transportation Planning at the City "
        "of Toronto. Readiness is about knowing what a change will do to the operation before it reaches "
        "service, and that was the purpose of my work in Service Design.",

        "There I ran OpenTrack simulations of GO rail services to establish what proposed operating and "
        "infrastructure changes would do to run times, reliability and recovery before they were taken forward, "
        "and assessed the service effect of temporary and permanent slow orders. I worked with schedulers, "
        "operations staff and engineers on service design decisions and presented the evidence behind them. "
        + TOOLS_ALSO,

        "At Mott MacDonald I ran Synchro traffic simulations to estimate how Ontario Line construction staging "
        "and road closures would affect surrounding streets. At the City I review development applications and "
        "the studies filed with them against standards, recommend conditions where something is missing, and "
        "write the briefing notes and presentations that carry findings to managers in other divisions.",

        "I should be straightforward about the gaps. I have not worked in operational readiness or "
        "commissioning, reviewed commissioning documentation, or given functional leadership to a team of "
        "coordinators. My review work has been of transportation studies and development submissions rather "
        "than detailed construction drawings, though I work in AutoCAD and Civil 3D, and I am not registered "
        "with PEO, which the posting lists as an asset.",

        "Thank you for considering my application.",
    ])


# ================================================ Metrolinx - Senior Advisor, SSE

RESUME_MX_SSE = resume(
    "Transportation engineer with a master's degree and four years across municipal transportation planning at "
    "the City of Toronto and GO rail service planning at Metrolinx. Writes the briefing notes, memos and "
    "presentations that carry issues and options to senior staff, coordinates across divisions and agencies, "
    "and runs assigned studies to schedule.",
    city(BRIEFING, PROJECTS, AGENCIES, POLICY_COUNCIL, DEV_STUDIES)
    + metrolinx(OPENTRACK, SLOW, CVT, CLI) + MOTT + UOFA,
    skills=skills("Briefing notes, memos, reports and slide decks for senior staff. Issues analysis and "
                  "recommendations. Coordination across divisions, agencies, consultants and applicants. Project "
                  "planning and follow-through. OpenTrack, VISSIM, Synchro and MATSim. Python, SQL, ArcGIS Pro "
                  "and QGIS. MS Office."))

COVER_MX_SSE = letter(
    "Talent Acquisition", "Scarborough Subway Extension, Vice President's Office",
    "Metrolinx, 100 Consilium Place, Toronto, ON",
    "Re: Senior Advisor, SSE", "Dear Hiring Manager,",
    [
        "I would like to apply for the Senior Advisor position in the Scarborough Subway Extension Vice "
        "President's Office. I am an Assistant Planner in Transportation Planning at the City of Toronto, and "
        "before that I was a Transportation Planner at Metrolinx. Much of this role is preparing the memos, "
        "reports, briefing notes and slide decks that move a project's issues to the people who decide them, "
        "and that is a large part of what I do now.",

        "At the City I write the briefing notes, memos and presentations that carry issues, options and "
        "recommendations to senior staff across divisions. I run assigned projects from scoping through to "
        "recommendations, planning the work and holding the schedule myself, and I coordinate with divisions, "
        "consultants, applicants and outside agencies whose priorities conflict. With policy staff I recommend "
        "and report to Council on new transportation regulations and guidelines.",

        "At Metrolinx I ran OpenTrack simulations of GO rail services and assessed what temporary and permanent "
        "slow orders, the kind of restriction construction on an operating railway imposes, would do to service. "
        + TOOLS_ALSO,

        "I should be straightforward about the gaps. I have not prepared Board, Cabinet or Treasury Board "
        "submissions, and I have not worked on the delivery team of a major capital project or on contract "
        "issues. My project management has been of studies rather than construction. I am applying because the "
        "reporting, issues analysis and coordination at the centre of the role is the work I do now.",

        "Thank you for considering my application.",
    ])


# ================================================ Metrolinx - Project Manager, Union Station Enhancement

RESUME_MX_PM = resume(
    "Transportation engineer with a master's degree and four years across municipal transportation planning at "
    "the City of Toronto and GO rail service planning at Metrolinx. Runs assigned projects from scoping to "
    "recommendations, reviews consultant studies against standards, coordinates consultants, agencies and "
    "divisions, and has worked on what construction does to a railway and to city streets.",
    city(PROJECTS, DEV_STUDIES, AGENCIES, BRIEFING)
    + metrolinx(OPENTRACK, SLOW, CVT, CLI) + MOTT + UOFA,
    skills=skills("Project planning, scheduling and follow-through. Review of consultant studies and submissions "
                  "against standards. Coordination across consultants, agencies and divisions. Briefing materials "
                  "for senior management. AutoCAD and Civil 3D. Python (Pandas, NumPy), SQL and ArcGIS Pro. MS "
                  "Office."))

COVER_MX_PM = letter(
    "Talent Acquisition", "Capital Projects Group, Union Station Enhancement Project Office",
    "Metrolinx, 130 Adelaide Street West, Toronto, ON",
    "Re: Project Manager, Union Station Enhancement Project Office", "Dear Hiring Manager,",
    [
        "I would like to apply for the Project Manager position in the Union Station Enhancement Project Office. "
        "I am an Assistant Planner in Transportation Planning at the City of Toronto, and before that I was a "
        "Transportation Planner at Metrolinx in GO rail service design, working on the network that Union "
        "Station serves.",

        "At the City I run assigned projects from scoping through to recommendations, planning the work, holding "
        "the schedule and quality myself, and reporting progress to the people relying on it. I review the "
        "studies consultants and applicants submit against City standards and recommend conditions where "
        "something is missing, coordinate with divisions, consultants and outside agencies, and write the "
        "briefing notes and presentations that carry issues and options to senior staff.",

        "At Metrolinx I ran OpenTrack simulations of GO rail services and assessed what temporary and permanent "
        "slow orders would do to service. " + TOOLS_ALSO + " At Mott MacDonald I ran Synchro traffic simulations "
        "of Ontario Line construction staging and road closures.",

        "I should be straightforward about the gaps. I have not managed a capital infrastructure project through "
        "design, procurement, construction and commissioning, or run project controls, budgets, procurement, "
        "contract administration or commercial issues. I do not hold a PMP, C.E.T. or P.Eng., or a Class G "
        "licence, all of which the posting lists as assets. I am applying because the coordination, review and "
        "reporting parts of the role are what I do now.",

        "Thank you for considering my application.",
    ])


# ================================================ Metrolinx - Senior Manager, GO Expansion Operations
# His old area (GO Expansion Operations): leave out the Crew Variance Tool and command line workflow.

RESUME_MX_GXO = resume(
    "Transportation engineer with a master's degree and four years across GO rail service planning at Metrolinx "
    "and municipal transportation planning at the City of Toronto. Tested GO service changes in simulation "
    "against infrastructure constraints and construction restrictions, and works across divisions, agencies and "
    "consultants to move issues to a decision.",
    city(STUDIES, AGENCIES, TTS, DASHBOARD)
    + metrolinx(OPENTRACK, SLOW, EVIDENCE) + MOTT + UOFA,
    skills=skills("Rail service design and simulation: OpenTrack and TrainPlan. Operational effect of "
                  "construction and speed restrictions. Briefing notes, reports and presentations for senior "
                  "staff. Coordination across operations, engineering and project teams. Python (Pandas, NumPy), "
                  "SQL and ArcGIS Pro. MS Office."))

COVER_MX_GXO = letter(
    "Talent Acquisition", "GO Expansion Operations", "Metrolinx, Toronto, ON",
    "Re: Senior Manager, GO Expansion Operations", "Dear Hiring Manager,",
    [
        "I would like to apply for the Senior Manager, GO Expansion Operations position. I worked at Metrolinx in "
        "2023 as a Transportation Planner, Simulation and Modelling, in Service Design, and since January 2024 I "
        "have been an Assistant Planner in Transportation Planning at the City of Toronto.",

        "At Metrolinx I ran OpenTrack simulations of GO rail services to establish what proposed operating and "
        "infrastructure changes would do to run times, reliability and recovery before they were taken forward. "
        "I assessed the service effect of temporary and permanent slow orders, the kind of restriction that "
        "construction on an operating railway imposes, and worked with schedulers, operations staff and engineers "
        "on service design decisions, presenting the evidence behind them. Reviewing corridor projects through an "
        "operations lens is close to that work.",

        "At the City I run assigned studies from scoping through to recommendations, write the briefing notes "
        "that come out of them, and present to planners, engineers and managers in other divisions. I coordinate "
        "with divisions, consultants and outside agencies whose priorities conflict, and work issues through to "
        "a position everyone can act on.",

        "I should be straightforward about the gaps, which are large for a role at this level. The posting asks "
        "for ten years of progressively senior experience in railway operations, corridor engineering and "
        "contract management; I have about four and a half years in total, one of them in rail. I have not "
        "managed staff, applied collective agreement provisions, or managed vendors or capital budgets, and I do "
        "not hold CROR certification or a P.Eng. If the team has a role closer to my level, I would welcome "
        "being considered for it.",

        "Thank you for considering my application.",
    ])


# ================================================ Mott MacDonald - Advisory Consultant

RESUME_MM_ADV = resume(
    "Transportation engineer with a master's degree and four years across municipal transportation planning, GO "
    "rail service planning and consulting. Runs studies from scoping to recommendations, analyzes data and "
    "options, and writes the reports, briefing notes and presentations that turn analysis into decisions.",
    city(STUDIES, TTS, AGENCIES, DASHBOARD)
    + metrolinx(OPENTRACK, EVIDENCE, CVT, CLI) + MOTT + UOFA,
    skills=skills("Options analysis and evidence-based recommendations. Reports, briefing notes and presentations "
                  "for senior decision-makers. Research and data analysis: Python (Pandas, NumPy), SQL and advanced "
                  "Excel. ArcGIS Pro and QGIS. OpenTrack, VISSIM, Synchro and MATSim. Word, Excel and PowerPoint."))

COVER_MM_ADV = letter(
    "Talent Acquisition", "Advisory", "Mott MacDonald, Toronto, ON",
    "Re: Advisory Consultant", "Dear Hiring Manager,",
    [
        "I would like to apply for the Advisory Consultant position in Toronto. I worked at Mott MacDonald "
        "briefly in early 2023, on Ontario Line traffic simulation, before joining Metrolinx in Service Design, "
        "and I am now an Assistant Planner in Transportation Planning at the City of Toronto. I would like to come "
        "back to consulting, on the advisory side.",

        "The posting asks for options analysis, research, and clear, defensible recommendations for senior "
        "decision-makers. At the City I run assigned studies from scoping through to recommendations, analyze "
        "travel and network data including several years of the Transportation Tomorrow Survey, and write the "
        "briefing notes and presentations that carry the findings to planners, engineers and managers in other "
        "divisions. I built the Transportation Data Dashboard, bringing several years of survey data into one "
        "validated source the division reports from.",

        "At Metrolinx I ran OpenTrack simulations of GO rail services to establish what proposed operating and "
        "infrastructure changes would do to run times and reliability before they were taken forward, and "
        "presented that evidence to schedulers, operations staff and engineers. " + TOOLS_ALSO,

        "I should be straightforward about the gaps. The posting asks for eight years of advisory or consulting "
        "experience; I have about four and a half years in total, most of it in the public sector. I have not "
        "prepared business cases, economic analysis or procurement and commercial strategies, and I have not "
        "worked on P3 or other alternative delivery models, commercial management or business development. I do "
        "not hold a project management or professional designation.",

        "Thank you for considering my application.",
    ])


# ================================================ Mott MacDonald - Senior Advisory Consultant, Operational Readiness

RESUME_MM_OR = RESUME_MX_OPREADY

COVER_MM_OR = letter(
    "Talent Acquisition", "Advisory", "Mott MacDonald, Toronto, ON",
    "Re: Senior Advisory Consultant, Operational Readiness", "Dear Hiring Manager,",
    [
        "I would like to apply for the Senior Advisory Consultant, Operational Readiness position. I worked at "
        "Mott MacDonald briefly in early 2023 before joining Metrolinx in Service Design, and I am now an "
        "Assistant Planner in Transportation Planning at the City of Toronto. Operational readiness is about "
        "knowing what a change will do to an operation before it reaches service, and that has been the thread "
        "of my work.",

        "At Metrolinx I ran OpenTrack simulations of GO rail services to establish what proposed operating and "
        "infrastructure changes would do to run times, reliability and recovery before they were taken forward, "
        "and assessed the service effect of temporary and permanent slow orders. I worked with schedulers, "
        "operations staff and engineers on service design decisions and presented the evidence behind them. "
        + TOOLS_ALSO,

        "At Mott MacDonald I ran Synchro traffic simulations of Ontario Line construction staging and road "
        "closures. At the City I built the Transportation Data Dashboard, which brought several years of survey "
        "data into one validated source the division reports from, and I write the briefing notes and "
        "presentations that carry findings to managers in other divisions.",

        "I should be straightforward about the gaps, which are significant at this level. The posting asks for "
        "ten years on major infrastructure programs; I have about four and a half. I have not led operational "
        "readiness, activation or transition work, handover and acceptance, change management or operational "
        "trials, and I have not led commercial management, business development or junior staff. If the practice "
        "has a role closer to my level in operational readiness, I would welcome being considered for it.",

        "Thank you for considering my application.",
    ])


# ================================================ Mott MacDonald - Project Manager

RESUME_MM_PM = RESUME_MX_PM

COVER_MM_PM = letter(
    "Talent Acquisition", "", "Mott MacDonald, Toronto, ON",
    "Re: Project Manager", "Dear Hiring Manager,",
    [
        "I would like to apply for the Project Manager position in Toronto. I worked at Mott MacDonald briefly in "
        "early 2023, where I ran Synchro traffic simulations of Ontario Line construction staging and road "
        "closures and prepared the supporting material for the project team. Since then I have worked in GO "
        "rail service design at Metrolinx and, since January 2024, as an Assistant Planner in Transportation "
        "Planning at the City of Toronto.",

        "At the City I run assigned projects from scoping through to recommendations, planning the work, holding "
        "the schedule and quality myself, and reporting progress to the people relying on it. I coordinate with "
        "divisions, consultants, applicants and outside agencies whose priorities conflict, and I write the "
        "briefing notes and presentations that carry issues and options to senior staff.",

        "At Metrolinx I ran OpenTrack simulations of GO rail services and assessed what temporary and permanent "
        "slow orders, the kind of restriction construction on an operating railway imposes, would do to service. "
        + TOOLS_ALSO,

        "I should be straightforward about the gaps. The posting asks for five to ten years of project "
        "management on infrastructure projects. My project management has been of studies, not delivery: I have "
        "not managed an infrastructure project's schedule and commercial objectives, change control or project "
        "controls, and I have not led or managed staff. I am not a member of PMI and do not hold a PMP.",

        "Thank you for considering my application.",
    ])


# ================================================ Dillon - Transportation Planner/Engineer (Toronto)

RESUME_DIL = resume(
    "Transportation engineer with a master's degree and four years across municipal transportation planning at "
    "the City of Toronto, GO rail service planning at Metrolinx and a consulting placement at Mott MacDonald. "
    "Reviews traffic and transportation studies, runs traffic and rail simulation, and builds the Python and GIS "
    "tooling behind the analysis.",
    city(DEV_STUDIES, TTS, ROW, DASHBOARD)
    + metrolinx(OPENTRACK, SLOW, CVT, CLI) + MOTT + UOFA,
    skills=skills("Synchro and VISSIM; OpenTrack and MATSim. Python (Pandas, NumPy), SQL and advanced Excel. "
                  "ArcGIS Pro, QGIS and MapBox. AutoCAD and Civil 3D. Travel data analysis, including the "
                  "Transportation Tomorrow Survey. Technical reports and presentations."))

COVER_DIL = letter(
    "Talent Acquisition", "Integrated Mobility", "Dillon Consulting Limited, Toronto, ON",
    "Re: Transportation Planner/Engineer", "Dear Hiring Manager,",
    [
        "I would like to apply for the Transportation Planner/Engineer position with the Integrated Mobility "
        "team in Toronto. I am an Assistant Planner in Transportation Planning at the City of Toronto, and before "
        "that I worked in GO rail service design at Metrolinx and briefly at Mott MacDonald. I hold a master's "
        "degree in Transportation Engineering.",

        "The posting lists traffic impact assessments, traffic operations studies and transit planning among the "
        "team's work. At the City I review development applications and the transportation studies filed with "
        "them against City standards and Official Plan policy, so I know what a municipal reviewer looks for in a "
        "traffic impact assessment. I analyze travel and network data, including several years of the "
        "Transportation Tomorrow Survey, and I built the Transportation Data Dashboard, which combined several "
        "years of survey data into one validated source the division reports from.",

        "The posting lists Python as an asset, along with GIS and traffic modelling software. I work in Python, "
        "SQL, ArcGIS Pro and QGIS, and I have used Synchro to simulate Ontario Line construction staging at Mott "
        "MacDonald and OpenTrack for GO rail services at Metrolinx. " + TOOLS_ALSO,

        "I should be straightforward about the gaps. My consulting experience is limited to a short placement at "
        "Mott MacDonald in early 2023, and I have not written proposals. I have not prepared transit ridership "
        "forecasts, on-demand transit studies or signal designs, or used SimTraffic, and I am not registered "
        "with PEO.",

        "Thank you for considering my application.",
    ])


# ================================================ Dillon - Senior Transportation Planner/Engineer

RESUME_DIL_SR = RESUME_DIL

COVER_DIL_SR = letter(
    "Talent Acquisition", "Integrated Mobility", "Dillon Consulting Limited, Toronto, ON",
    "Re: Senior Transportation Planner/Engineer", "Dear Hiring Manager,",
    [
        "I would like to apply for the Senior Transportation Planner/Engineer position with the Integrated "
        "Mobility discipline in the GTHA. I am an Assistant Planner in Transportation Planning at the City of "
        "Toronto, and before that I worked in GO rail service design at Metrolinx and briefly at Mott MacDonald.",

        "At the City I review development applications and the transportation studies filed with them against "
        "City standards and Official Plan policy, run assigned studies from scoping through to recommendations, "
        "and present to planners, engineers and managers in other divisions. I coordinate with divisions, "
        "consultants, applicants and outside agencies whose priorities conflict. That is the client side of the "
        "GTHA market the posting describes.",

        "At Mott MacDonald I ran Synchro traffic simulations of Ontario Line construction staging and road "
        "closures, and at Metrolinx I ran OpenTrack simulations of GO rail services. " + TOOLS_ALSO,

        "I should be straightforward about the gaps, which are large for this level. The posting asks for ten "
        "years of progressive experience, six of them in project management; I have about four and a half. I "
        "have not led Municipal Class Environmental Assessments or functional design studies, managed people, "
        "budgets or consultation programs, or led business development and proposals. If the team is also "
        "hiring at the planner or engineer level, I would welcome being considered for that role.",

        "Thank you for considering my application.",
    ])


# ================================================ GHD - Senior Transportation Planner / Traffic Engineer

RESUME_GHD = RESUME_DIL

COVER_GHD = letter(
    "Talent Acquisition", "Transportation Planning and Traffic Engineering", "GHD, Toronto, ON",
    "Re: Senior Transportation Planner / Traffic Engineer", "Dear Hiring Manager,",
    [
        "I would like to apply for the Senior Transportation Planner / Traffic Engineer position with the "
        "Transportation Planning and Traffic Engineering team in Toronto. I am an Assistant Planner in "
        "Transportation Planning at the City of Toronto, and before that I worked in GO rail service design at "
        "Metrolinx and briefly at Mott MacDonald.",

        "The posting includes research and analysis of land use and travel data, the transportation impact of "
        "proposed developments, and microsimulation. At the City I review development applications and the "
        "transportation studies filed with them against City standards and Official Plan policy, and recommend "
        "conditions where something is missing. I analyze travel and network data, including several years of "
        "the Transportation Tomorrow Survey, and write the memos, reports and presentations that carry findings "
        "to planners, engineers and managers.",

        "At Mott MacDonald I ran Synchro traffic simulations of Ontario Line construction staging and road "
        "closures, and at Metrolinx I ran OpenTrack simulations of GO rail services. " + TOOLS_ALSO + " I also "
        "work in VISSIM, AutoCAD and Civil 3D, and GIS.",

        "I should be straightforward about the gaps. The posting asks for eight to ten years of experience and "
        "registration with PEO as a P.Eng. or Engineer-in-Training; I have about four and a half years and I am "
        "not registered with PEO. I have not done safety audits or collision analysis, used Sidra, prepared "
        "parking justification or loading studies, or led proposals and fee preparation. If the team is also "
        "hiring at the planner level, I would welcome being considered for that role.",

        "Thank you for considering my application.",
    ])


# ================================================ Egis - Project Manager, Rail & Transit

RESUME_EGIS = RESUME_MX_PM

COVER_EGIS = letter(
    "Talent Acquisition", "Rail & Transit", "Egis Canada, Toronto, ON",
    "Re: Project Manager, Rail & Transit", "Dear Hiring Manager,",
    [
        "I would like to apply for the Project Manager, Rail & Transit position in Toronto. I am an Assistant "
        "Planner in Transportation Planning at the City of Toronto, and before that I was a Transportation "
        "Planner at Metrolinx in GO rail service design.",

        "At the City I run assigned projects from scoping through to recommendations, planning the work, holding "
        "the schedule and quality myself, and reporting progress to the people relying on it. I review the "
        "studies consultants and applicants submit against City standards, coordinate with divisions, "
        "consultants and outside agencies, and write the briefing notes and presentations that carry issues and "
        "options to senior staff.",

        "At Metrolinx I ran OpenTrack simulations of GO rail services and assessed what temporary and permanent "
        "slow orders would do to service. " + TOOLS_ALSO + " At Mott MacDonald I ran Synchro traffic "
        "simulations of Ontario Line construction staging.",

        "I should be straightforward about the gaps. The posting asks for more than ten years in rail, transit "
        "or transportation infrastructure and experience managing complex multidisciplinary delivery; I have "
        "about four and a half years, and I have not managed design, procurement or construction, budgets, "
        "invoicing or change orders, or led business development. I do not hold a P.Eng. or PMP. If the team is "
        "hiring at a coordinator or project engineer level in rail and transit, I would welcome being considered.",

        "Thank you for considering my application.",
    ])


# ================================================ City of North Vancouver - Manager, GIS

RESUME_CNV_GIS = RESUME_MX_GIS

COVER_CNV_GIS = letter(
    "Human Resources", "Office of the Chief Administrative Officer", "City of North Vancouver, North Vancouver, BC",
    "Re: Manager, Geographic Information Systems (GIS)", "Dear Hiring Manager,",
    [
        "I would like to apply for the Manager, Geographic Information Systems position in the Office of the "
        "Chief Administrative Officer. I am a transportation engineer and an Assistant Planner in Transportation "
        "Planning at the City of Toronto, where much of my work is building and maintaining the spatial data the "
        "section relies on.",

        "I build and maintain the road and right-of-way datasets Transportation Planning depends on, using GIS "
        "and Python, including a right-of-way width dataset covering all city roads, built with QGIS, MapBox and "
        "JavaScript. I also built the Transportation Data Dashboard, which combined several years of survey data "
        "into one validated source the division reports from. The posting describes a working manager who "
        "contributes directly to technical delivery, and hands-on technical work is where I am strongest.",

        "My master's thesis used GIS and macro-simulation to assess community transportation capacity for "
        "wildfire evacuation. At Metrolinx I set up a command line workflow that pre-simulated slow orders in "
        "batches, cutting turnaround on scenario requests from days to hours, and built the Crew Variance Tool, a "
        "Python application that read large JSON operations files and summarised speed profiles and run-time "
        "variance across subdivisions.",

        "I should be straightforward about the gaps. I have not led a GIS team or supervised GIS specialists and "
        "technicians, and I have not administered ArcGIS Enterprise, ArcGIS Online or field data collection "
        "tools, or used FME. My master's degree is in transportation engineering rather than GIS or geography, "
        "though my thesis was GIS-based. I am applying because the spatial data and automation at the centre of "
        "the role is the work I do now.",

        "Thank you for considering my application.",
    ])


# ================================================ Skyline Recruitment (for a consulting firm) - GIS Manager

RESUME_SKY_GIS = RESUME_MX_GIS

COVER_SKY_GIS = letter(
    "Recruitment Team", "", "Skyline Recruitment Ltd., Toronto, ON",
    "Re: GIS Manager (multidisciplinary consulting firm)", "Dear Hiring Manager,",
    [
        "I would like to apply for the GIS Manager position you are recruiting for on behalf of a "
        "multidisciplinary consulting firm in Toronto. I am a transportation engineer and an Assistant Planner in "
        "Transportation Planning at the City of Toronto, where much of my work is building and maintaining the "
        "spatial data the section relies on.",

        "I build and maintain the road and right-of-way datasets Transportation Planning depends on, using GIS "
        "and Python, including a right-of-way width dataset covering all city roads, built with QGIS, MapBox and "
        "JavaScript. I also built the Transportation Data Dashboard, which combined several years of survey data "
        "into one validated source the division reports from. Keeping data consistent enough that other people "
        "can rely on it is most of that work. I also work in AutoCAD and Civil 3D.",

        "My master's research included spatial analysis of large transportation datasets in GIS for wildfire "
        "evacuation planning. At Metrolinx I set up a command line workflow that pre-simulated slow orders in "
        "batches, cutting turnaround on scenario requests from days to hours, and built the Crew Variance Tool, a "
        "Python application that read large JSON operations files and summarised speed profiles and run-time "
        "variance across subdivisions.",

        "I should be straightforward about the gaps. I have not led or supervised GIS staff, and my GIS work has "
        "been in transportation rather than environmental, geotechnical or hydrogeological projects. I have not "
        "set company-wide GIS standards or managed field-data systems.",

        "Thank you for considering my application.",
    ])


# ================================================ WSP - (Intermediate) Aviation Planner

from content20 import RESUME_AVIATION
RESUME_WSP_AVN = RESUME_AVIATION

COVER_WSP_AVN = letter(
    "Talent Acquisition", "Aviation", "WSP Canada, Ontario",
    "Re: Aviation Planner", "Dear Hiring Manager,",
    [
        "I would like to apply for the Aviation Planner position. I come to it from transportation planning "
        "rather than aviation, so I want to be clear about both what I would bring and where I fall short.",

        "The posting starts with capacity, demand forecasting and operational improvements, and those are the "
        "questions my work has been about. At the City of Toronto I analyze travel and network data, including "
        "several years of the Transportation Tomorrow Survey, to work out where capacity is short and what that "
        "means for future investment. At Metrolinx I ran OpenTrack simulations of GO rail services to test how "
        "infrastructure constraints and construction restrictions changed run times and reliability, and at Mott "
        "MacDonald I simulated Ontario Line construction staging, which is close to the construction operation "
        "planning the posting mentions.",

        TOOLS_SENTENCE + " I work in AutoCAD and Civil 3D, and I write the technical reports and presentations "
        "that carry findings to decision-makers.",

        "I should be straightforward about the gaps. I have no aviation planning experience, and the posting "
        "asks for seven to ten years. I have not prepared airport master plans or terminal and airside layouts, "
        "carried out aeronautical impact assessments, or applied CARs, TP312, TP1247 or ICAO standards, and I "
        "have not used CAST or AviPlan.",

        "Thank you for considering my application.",
    ])


# ================================================ Binnie - Project Manager, Transportation Major Projects

RESUME_BINNIE = RESUME_MX_PM

COVER_BINNIE = letter(
    "Talent Acquisition", "Transportation Major Projects", "Binnie, Burnaby, BC",
    "Re: Project Manager (Transportation Major Projects)", "Dear Hiring Manager,",
    [
        "I would like to apply for the Project Manager position in the Transportation Major Projects division. I "
        "am an Assistant Planner in Transportation Planning at the City of Toronto, and before that I worked in "
        "GO rail service design at Metrolinx and briefly at Mott MacDonald.",

        "The division works on the owner's side of major projects, and that is the side I work on now. At the "
        "City I review the studies consultants and applicants submit against City standards and recommend "
        "conditions where something is missing. I run assigned projects from scoping through to "
        "recommendations, holding the schedule and quality myself, and I present to planners, engineers and "
        "managers in other divisions.",

        "At Mott MacDonald I ran Synchro traffic simulations of Ontario Line construction staging and road "
        "closures, and at Metrolinx I ran OpenTrack simulations of GO rail services. " + TOOLS_ALSO,

        "I should be straightforward about the gaps. I have not managed major infrastructure projects through "
        "procurement and delivery, directed staff and subconsultants, or done business development and "
        "proposals, and I am not registered as a P.Eng. The posting asks for a Class 5 licence and a personal "
        "vehicle, which I do not have. I am based in Toronto.",

        "Thank you for considering my application.",
    ])


# ================================================ Aecon - Traffic Lead

RESUME_AECON = resume(
    "Transportation engineer with a master's degree who has simulated how Ontario Line construction staging and "
    "road closures affect surrounding streets, assessed what construction restrictions do to GO rail service, and "
    "reviews transportation studies for the City of Toronto.",
    city(DEV_STUDIES, AGENCIES, ROW, STUDIES)
    + metrolinx(OPENTRACK, SLOW, CVT, CLI) + MOTT + UOFA,
    skills=skills("Traffic simulation of construction staging and road closures (Synchro); VISSIM. Review of "
                  "transportation studies and submissions against City standards. Coordination with City "
                  "divisions, agencies and consultants. AutoCAD and Civil 3D. ArcGIS Pro and QGIS. Python and SQL. "
                  "Reports and presentations."))

COVER_AECON = letter(
    "Talent Acquisition", "Aecon Civil", "Aecon Group Inc., Toronto, ON",
    "Re: Traffic Lead", "Dear Hiring Manager,",
    [
        "I would like to apply for the Traffic Lead position with Aecon Civil. I am an Assistant Planner in "
        "Transportation Planning at the City of Toronto, and before that I worked in GO rail service design at "
        "Metrolinx and at Mott MacDonald, where I worked on Ontario Line construction staging.",

        "At Mott MacDonald I ran Synchro traffic simulations to estimate how Ontario Line construction staging and "
        "road closures would affect surrounding streets, and prepared the supporting material for the project "
        "team. At Metrolinx I assessed the service effect of temporary and permanent slow orders, the kind of "
        "restriction construction on an operating railway imposes. " + TOOLS_ALSO,

        "At the City I review development applications and the transportation studies filed with them against "
        "City standards, and I coordinate with divisions, consultants, applicants and outside agencies whose "
        "priorities conflict. The posting asks for experience with the City of Toronto and Metrolinx, and I have "
        "worked for both.",

        "I should be straightforward about the gaps. The posting asks for eight years in urban traffic "
        "operations; I have about four and a half years in transportation planning, and my traffic work has been "
        "simulation and review rather than operations in the field. I have not prepared traffic control plans to "
        "OTM Book 7, Traffic and Transit Management Plans or lane closure reports, or recommended signal timing "
        "changes, and I do not hold a Class G licence, which the posting requires.",

        "Thank you for considering my application.",
    ])


# ================================================ City of Toronto - Spatial Specialist (66074)

RESUME_COT_SPATIAL = RESUME_MX_GIS

COVER_COT_SPATIAL = letter(
    "Hiring Manager", "Technology Services, Enterprise Services & Operations", "City of Toronto, Toronto, ON",
    "Re: Spatial Specialist (Productivity and Automation Specialist), Job ID 66074", "Dear Hiring Manager,",
    [
        "I would like to apply for the Spatial Specialist (Productivity and Automation Specialist) position in "
        "Technology Services. I am an Assistant Planner in Transportation Planning at the City, where much of my "
        "work is building and maintaining the spatial data the section relies on, so I would come to the "
        "enterprise geospatial team as one of its users.",

        "I build and maintain the road and right-of-way datasets Transportation Planning depends on, using GIS "
        "and Python, including a right-of-way width dataset covering all city roads, built with QGIS, MapBox and "
        "JavaScript. I also built the Transportation Data Dashboard, which combined several years of survey data "
        "into one validated source the division reports from. Automating the routine parts of a geospatial "
        "workflow is how I approach a dataset.",

        TOOLS_SENTENCE + " My master's thesis used GIS and macro-simulation to assess community transportation "
        "capacity for wildfire evacuation.",

        "I should be straightforward about the gaps. I have not administered ArcGIS Enterprise, written Arcade "
        "expressions, or used FME or Apache Airflow, and I have not prepared formal test plans for geospatial "
        "applications. My background is in transportation engineering rather than computer science or geomatics, "
        "though I am completing a part-time BSc in Computer Science at UBC.",

        "Thank you for considering my application.",
    ])
