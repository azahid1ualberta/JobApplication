# -*- coding: utf-8 -*-
"""26 October 2026, sent in chat: four Metrolinx postings from the Metrolinx careers site.

    117600  Manager, Project Delivery (Union+, Capital Projects Group)
    117614  Data Scientist II (6-month term, Marketing Customer Analytics Office)
    117642  Senior Business Intelligence Performance Analyst (Strategy & Centres of Excellence)
    116406  Project Manager, Union Station Rail Corridor (contract up to 12 months)

The fifth posting he sent, Senior Project Manager, Hamilton LRT (116522), was already built by the
22 October run (content35); it is rebuilt there with the new education block.
"""

import content20
from content3 import (MOTT, UOFA, resume)
from content19 import (OPENTRACK, SLOW, CVT, CLI, DASHBOARD, city, metrolinx, skills)
from content20 import (TTS, AGENCIES, letter)
from content28 import (ROW, STUDIES, EVIDENCE, TOOLS_ALSO, RESUME_MX_PM)

content20.DATE = "October 26, 2026"
MX = "Metrolinx, Toronto, ON"


# ================================================ 117600 Manager, Project Delivery (Union+)

RESUME_117600 = RESUME_MX_PM

COVER_117600 = letter(
    "Talent Acquisition", "Capital Projects Group (GO & UP), Union+", "Metrolinx, 130 Adelaide Street West, Toronto, ON",
    "Re: Manager, Project Delivery (Job ID 117600)", "Dear Hiring Manager,",
    [
        "I would like to apply for the Manager, Project Delivery position with the Union+ team in the Capital "
        "Projects Group. I should say at the outset that this is a design and construction delivery role at a "
        "level above my experience, and I have tried to be clear below about both what I would bring and where "
        "I fall short.",

        "From my time in Service Design at Metrolinx I know the GO network that runs through the Union Station "
        "Rail Corridor from the operating side. I ran OpenTrack simulations of GO rail services and assessed "
        "the service effect of temporary and permanent slow orders, the kind of restriction construction on an "
        "operating railway imposes. " + TOOLS_ALSO,

        "Since January 2024 I have been an Assistant Planner in Transportation Planning at the City of Toronto. "
        "I run assigned projects from scoping through to recommendations, holding the schedule and quality "
        "myself, review the studies consultants and applicants submit against City standards, and coordinate "
        "with divisions, consultants and outside agencies whose priorities conflict. At Mott MacDonald I ran "
        "Synchro traffic simulations of Ontario Line construction staging and road closures.",

        "The gaps are substantial. The posting asks for experience managing construction projects from start "
        "to completion, working directly with contractors, and leading a team of technical project "
        "professionals. I have not managed design or construction, overseen contractors or Alliance partners, "
        "managed budgets or risk, or supervised staff, and I have not worked on access planning or track "
        "protection in a live corridor. If the Union+ team has a project coordinator or project manager role "
        "closer to my level, I would welcome being considered for it.",

        "Thank you for considering my application.",
    ])


# ================================================ 117614 Data Scientist II (6-month term)

RESUME_117614 = resume(
    "Transportation engineer with a master's degree whose work has centred on data and models: Python tooling "
    "that summarised large GO operations files at Metrolinx, simulation of GO service changes, and travel data "
    "analysis and dashboards at the City of Toronto. Turns analysis into clear recommendations for "
    "decision-makers.",
    city(TTS, DASHBOARD, ROW, STUDIES)
    + metrolinx(CVT, CLI, OPENTRACK, EVIDENCE) + MOTT + UOFA,
    skills=skills("Python (Pandas, NumPy) and SQL for data extraction, analysis and automation. Simulation and "
                  "modelling: OpenTrack, MATSim, VISSIM and Synchro. Advanced Excel, including large multi-source "
                  "workbooks. Dashboards and data validation. ArcGIS Pro and QGIS; JavaScript. Reports and "
                  "presentations for senior staff. MS Office."))

COVER_117614 = letter(
    "Talent Acquisition", "Marketing Customer Analytics Office", "Metrolinx, 10 Bay Street, Toronto, ON",
    "Re: Data Scientist II, 6-Month Term (Job ID 117614)", "Dear Hiring Manager,",
    [
        "I would like to apply for the Data Scientist II position with the Marketing Customer Analytics Office. "
        "I worked at Metrolinx in 2023 as a Transportation Planner in Service Design, and I am now an Assistant "
        "Planner in Transportation Planning at the City of Toronto. The posting's central question, what a "
        "change in GO and UP service levels does to ridership and revenue, sits next to the one I worked on: "
        "what a change does to the service itself.",

        "At Metrolinx I ran OpenTrack simulations of GO rail services to establish what proposed operating and "
        "infrastructure changes would do to run times, reliability and recovery before they were taken forward, "
        "and presented that evidence to schedulers, operations staff and engineers. " + TOOLS_ALSO,

        "At the City I analyze travel and network data, including several years of the Transportation Tomorrow "
        "Survey, and I built the Transportation Data Dashboard, which combined several years of survey data into "
        "one validated source the division reports from. I work in Python and SQL, and I write up results for "
        "readers without a modelling background. My master's research used agent-based (MATSim) and "
        "macroscopic models.",

        "I should be straightforward about the gaps. I have not trained machine learning models or built "
        "ridership and revenue forecasts, and I have not used PySpark, Power BI, Microsoft Azure or Databricks, "
        "or run A/B tests. I am applying because the modelling and data work behind the role is familiar, and I "
        "know the GO service it would be forecasting.",

        "Thank you for considering my application.",
    ])


# ================================================ 117642 Senior Business Intelligence Performance Analyst

RESUME_117642 = resume(
    "Transportation engineer with a master's degree and four years across GO rail service planning at Metrolinx "
    "and municipal transportation planning at the City of Toronto. Builds dashboards and the Python tooling that "
    "replaces manual reporting, brings data from several sources into one validated source, and presents "
    "findings to senior staff.",
    city(DASHBOARD, ROW, TTS, STUDIES)
    + metrolinx(CVT, CLI, OPENTRACK, EVIDENCE) + MOTT + UOFA,
    skills=skills("Dashboards, automated reporting and data validation. Python (Pandas, NumPy) and SQL. Advanced "
                  "Excel, including large multi-source workbooks. ArcGIS Pro, QGIS and MapBox; JavaScript. "
                  "Analysis of travel and operations data. Reports and presentations for senior staff. Word, "
                  "Excel and PowerPoint."))

COVER_117642 = letter(
    "Talent Acquisition", "Strategy, Planning & Partnerships, Strategy & Centres of Excellence", MX,
    "Re: Senior Business Intelligence Performance Analyst (Job ID 117642)", "Dear Hiring Manager,",
    [
        "I would like to apply for the Senior Business Intelligence Performance Analyst position with the "
        "Strategy & Centres of Excellence team. I worked at Metrolinx in 2023 as a Transportation Planner in "
        "Service Design, and since January 2024 I have been an Assistant Planner in Transportation Planning at "
        "the City of Toronto.",

        "The posting asks for automated dashboards and reporting tools, less manual reporting, and stronger data "
        "validation. That is what the Transportation Data Dashboard did at the City: it replaced a report rebuilt "
        "by hand each quarter with one validated source, combining several years of survey data, and the "
        "division now reports from it. I also build and maintain the road and right-of-way datasets the "
        "division depends on, using GIS and Python.",

        "At Metrolinx I ran OpenTrack simulations of GO rail services and presented the evidence to schedulers, "
        "operations staff and engineers. " + TOOLS_ALSO,

        "I should be straightforward about the gaps. Of the tools the posting names, I work in SQL, Python and "
        "Excel, but I have not used Power BI, Tableau, Qlik Sense or R, and I have not built reporting in an "
        "enterprise BI platform or worked with financial data. My analysis has been of travel and operations "
        "data rather than regression and time-series forecasting.",

        "Thank you for considering my application.",
    ])


# ================================================ 116406 Project Manager, Union Station Rail Corridor (contract)

RESUME_116406 = RESUME_MX_PM

COVER_116406 = letter(
    "Talent Acquisition", "Capital Projects Group (GO & UP), GO Expansion - USRC", "Metrolinx, 130 Adelaide Street West, Toronto, ON",
    "Re: Project Manager, Union Station Rail Corridor, Contract (Job ID 116406)", "Dear Hiring Manager,",
    [
        "I would like to apply for the Project Manager, Union Station Rail Corridor contract position with the "
        "GO Expansion USRC project. I am an Assistant Planner in Transportation Planning at the City of Toronto, "
        "and before that I was a Transportation Planner at Metrolinx in GO rail service design.",

        "Much of the role is keeping a project moving: tracking day-to-day tasks, reporting to management, and "
        "working with municipalities, transit authorities, agencies and property owners to resolve issues. At "
        "the City I run assigned projects from scoping through to recommendations, holding the schedule and "
        "quality myself and reporting progress to the people relying on it, and I coordinate with divisions, "
        "consultants, applicants and outside agencies whose priorities conflict.",

        "At Metrolinx I ran OpenTrack simulations of GO rail services and assessed what temporary and permanent "
        "slow orders, the kind of restriction construction on an operating railway imposes, would do to service. "
        + TOOLS_ALSO + " At Mott MacDonald I ran Synchro traffic simulations of Ontario Line construction staging.",

        "I should be straightforward about the gaps. I have not managed the planning, design, construction or "
        "commissioning of rail infrastructure, coordinated cost estimates, or supervised staff, and my knowledge "
        "of construction in an operating railway comes from assessing what slow orders do to service. I do not "
        "hold a PMP, P.Eng. or Class G licence, which the posting lists as assets.",

        "Thank you for considering my application.",
    ])
