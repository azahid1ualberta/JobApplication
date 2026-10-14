# -*- coding: utf-8 -*-
"""14 October 2026 daily run: Ontario MTO Senior Project Manager (Highway Transfer Secretariat),
Toronto Port Authority Project Lead (Airport Comprehensive Plan), Defence Construction Canada
Real Property Spatial Data Requirements Specialist."""

import content20
from content3 import (NAME, CONTACT, MOTT, UOFA, resume)
from content19 import (OPENTRACK, CVT, CLI, DASHBOARD, TOOLS_SENTENCE, city, metrolinx, skills,
                       BRIEFING, PROJECTS, COORD, SCHED, REVIEW_DEV, RESEARCH, DATA_KPI)
from content20 import (TTS, DEV_STUDIES, REPORTS, AGENCIES, letter)

content20.DATE = "October 14, 2026"

ROW = ("B: Build and maintain the road and right-of-way datasets the division depends on, using GIS and Python, "
       "including a ROW-width dataset covering all city roads, built with QGIS, MapBox and JavaScript.")
BYLAW = ("B: Advise on by-laws and regulations that bear on the City's roads and right-of-way.")

# ================================================ MTO Senior Project Manager, Highway Transfer Secretariat

RESUME_MTO = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner with the City of Toronto's "
    "Transportation Planning division. Works with road and right-of-way data, advises on by-laws and "
    "regulations, coordinates across divisions and agencies, and writes the briefing notes that carry issues, "
    "options and recommendations to senior staff.",
    city(BRIEFING, BYLAW, COORD, PROJECTS, RESEARCH)
    + metrolinx(OPENTRACK, CVT, CLI) + MOTT + UOFA,
    skills=skills("Briefing notes, decision documents and presentations. Policy and regulatory research. Project "
                  "planning, scheduling and follow-through. Coordination across divisions, agencies and "
                  "consultants. Road and right-of-way data, ArcGIS, QGIS. Python (Pandas, NumPy), SQL and "
                  "advanced Excel. MS Office."))

COVER_MTO = letter(
    "Hiring Manager", "Highway Transfer Secretariat", "Ministry of Transportation, 777 Bay Street, Toronto, ON",
    "Re: Senior Project Manager, Highway Transfer Secretariat (Competition C-MT-249159/26)", "Dear Hiring Manager,",
    [
        "I would like to apply for the Senior Project Manager position with the Highway Transfer Secretariat. "
        "I am an Assistant Planner in Transportation Planning at the City of Toronto, and the transfer of the "
        "Gardiner Expressway and Don Valley Parkway is the kind of work where municipal and provincial "
        "responsibilities meet, which I see from the City's side of my own work on roads and right-of-way.",

        "The posting asks for advice on priorities, risks and policy implications, and for decision materials "
        "that senior leaders can act on. At the City I write the briefing notes, memos and presentations that "
        "carry issues, options and recommendations to senior staff, advise on by-laws and regulations, and "
        "research how City policy and provincial legislation bear on a question. I coordinate with divisions, "
        "consultants and outside agencies whose priorities conflict, and I run assigned projects from scoping "
        "through to recommendations, holding the schedule and quality myself. I also built and maintain "
        "road and right-of-way datasets, including a right-of-way width dataset covering all city roads.",

        TOOLS_SENTENCE + " Setting up a method once so a team can rely on it is how I tend to approach "
        "project work generally.",

        "I should be straightforward about the gaps. I have not led a portfolio of projects or directed "
        "program staff, and I have not prepared Cabinet or Treasury Board submissions or business cases at the "
        "scale this role handles. I have not worked inside a provincial ministry or helped develop legislation, "
        "and I do not hold a PMP. My project work so far has been at the scale of a planner's assignments "
        "rather than a secretariat's. I am applying because the subject matter is close to what I do each day, "
        "and I would welcome being considered for the position or for a related role on the team.",

        "Thank you for considering my application.",
    ])

# ================================================ Toronto Port Authority Project Lead, Airport Comprehensive Plan

RESUME_TPA = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner with the City of Toronto. "
    "Analyzes travel and network data to establish where capacity falls short, reviews development "
    "applications and their transportation studies, and builds simulation models of road and rail systems, "
    "with reports and briefings that carry the findings to agencies and decision-makers.",
    city(TTS, DEV_STUDIES, PROJECTS, BRIEFING, AGENCIES)
    + metrolinx(OPENTRACK, CVT, CLI) + MOTT + UOFA,
    skills=skills("Transportation capacity and demand analysis. Traffic and rail simulation: VISSIM, Synchro, "
                  "MATSim and OpenTrack. Python (Pandas, NumPy), SQL and advanced Excel. ArcGIS and QGIS. AutoCAD "
                  "and Civil 3D. Technical reports, briefing notes and presentations. MS Office."))

COVER_TPA = letter(
    "Human Resources", "", "Toronto Port Authority, Billy Bishop Toronto City Airport",
    "Re: Project Lead, Airport Comprehensive Plan (18-month contract)", "Dear Hiring Manager,",
    [
        "I would like to be considered for the Project Lead position on the Airport Comprehensive Plan. I come "
        "to it from transportation planning rather than airport work, so I want to be clear about what I would "
        "bring and where I fall short.",

        "The plan sits in the Infrastructure, Planning and Environment team and draws on transportation, land "
        "use and stakeholder input. At the City of Toronto I analyze travel and network data to establish where "
        "capacity falls short, review development applications and the transportation studies filed with them, "
        "and write the briefing notes and presentations that carry findings to senior staff and outside "
        "agencies. I coordinate with divisions, consultants and agencies whose priorities conflict, and I run "
        "assigned projects from scoping through to recommendations, holding the schedule myself. Testing "
        "whether a design will cope with the demand placed on it is what I have done with simulation, at Mott "
        "MacDonald on Ontario Line construction staging and at Metrolinx on GO rail services.",

        TOOLS_SENTENCE + " I have also worked in AutoCAD and Civil 3D.",

        "The gaps are significant. The posting asks for ten to twelve years of experience on airport projects, "
        "and I have none; my professional experience is closer to four and a half years. I have not "
        "managed a project budget, overseen consultants under a procurement process, or led consultation with "
        "Indigenous communities or the public, and I have not worked on Environmental or Impact Assessments. "
        "I am not bilingual in French. I am applying because the planning and analysis underneath the role "
        "is work I do now, and in case the team would consider someone who is still building airport "
        "experience.",

        "Thank you for considering my application.",
    ])

# ================================================ DCC Real Property Spatial Data Requirements Specialist

RESUME_DCC = resume(
    "Transportation engineer with a master's degree and part way through a computer science degree, currently "
    "an Assistant Planner with the City of Toronto. Builds and maintains spatial datasets and the tooling "
    "around them using GIS, CAD and Python, brings several sources into one validated dataset, and documents "
    "the result for the people who rely on it.",
    city(ROW, DASHBOARD, "B: Build and maintain the datasets and tooling Transportation Planning depends on, "
         "using Python and GIS.", BRIEFING, COORD)
    + metrolinx(CVT, CLI, OPENTRACK, SCHED) + MOTT + UOFA,
    skills=skills("Spatial data and GIS: ArcGIS Pro, QGIS, MapBox. AutoCAD and Civil 3D. Python (Pandas, NumPy), "
                  "SQL and JavaScript. Dataset validation and documentation. Dashboards and data visualization. "
                  "Advanced Excel. Reports, briefing notes and presentations. MS Office."))

COVER_DCC = letter(
    "Human Resources", "", "Defence Construction Canada, Ottawa, ON",
    "Re: Technical Specialist, Real Property Management (Real Property Spatial Data Requirements Specialist)",
    "Dear Hiring Manager,",
    [
        "I would like to apply for the Real Property Spatial Data Requirements Specialist position with the "
        "Spatial Data Services Program. My background is in transportation planning, and the part of it that "
        "overlaps with this role is spatial data: building it, validating it and making it usable.",

        "At the City of Toronto I build and maintain the road and right-of-way datasets that Transportation "
        "Planning depends on, including a right-of-way width dataset covering all city roads, built with QGIS, "
        "MapBox and JavaScript. I also built the Transportation Data Dashboard, which brought several years of "
        "data into one validated source the division reports from. I work in ArcGIS Pro, QGIS, AutoCAD and "
        "Civil 3D, and in Python and SQL. I write the briefing notes and presentations that explain data to "
        "the people who use it, and I coordinate with divisions and consultants whose needs differ.",

        TOOLS_SENTENCE,

        "I should be straightforward about the gaps. I have no experience in real property or facilities "
        "data, and I have not used Building Information Modelling software. I have not written statements of "
        "operational requirements or business cases, or worked as a business analyst, and I have not led data "
        "management projects or dealt with Department of National Defence systems. I am not bilingual in "
        "French, which the posting prefers. I am applying because spatial data work is the part of my "
        "experience I would most like to grow, and I would learn the real property side.",

        "Thank you for considering my application.",
    ])
