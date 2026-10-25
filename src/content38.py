# -*- coding: utf-8 -*-
"""25 October 2026 daily run: KGS Group Traffic Engineering Lead (4466377894),
Barrick Geospatial Data and GIS Solutions Lead (4473804708)."""

import content20
from content3 import (NAME, CONTACT, MOTT, UOFA, resume)
from content19 import (OPENTRACK, CVT, CLI, DASHBOARD, TOOLS_SENTENCE, city, metrolinx, skills,
                       BRIEFING, PROJECTS, COORD, REVIEW_DEV, DATA_KPI, TOOLING)
from content20 import (TTS, REPORTS, AGENCIES, letter)

content20.DATE = "October 25, 2026"

ROW = ("B: Built and maintain the road and right-of-way datasets Transportation Planning depends on, including "
       "a right-of-way width dataset for all city roads, using QGIS, MapBox, JavaScript and Python to merge "
       "sources that were scattered across the division.")

# ---------------------------------------------------------------- KGS 4466377894
RESUME_4466377894 = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner in Transportation "
    "Planning with the City of Toronto, reviewing development applications and their transportation "
    "studies and analyzing travel survey data. Previously simulated Ontario Line construction staging "
    "in Synchro at Mott MacDonald and assessed rail service effects at Metrolinx.",
    city(REVIEW_DEV, TTS, DASHBOARD, PROJECTS, COORD, BRIEFING)
    + metrolinx(CVT, CLI, OPENTRACK) + MOTT + UOFA,
    skills=skills("Synchro, VISSIM, OpenTrack and MATSim. Transportation planning and development review. "
                  "Travel survey and network data analysis. ArcGIS Pro, QGIS, AutoCAD and Civil 3D. "
                  "Python, SQL and JavaScript. MS Office."))

COVER_4466377894 = letter(
    "Hiring Team", "Transportation Department", "KGS Group",
    "Re: Traffic Engineering Lead (Req Id 565)",
    "Dear Hiring Team,",
    [
        "I would like to be considered for the Traffic Engineering Lead position. I am an Assistant Planner "
        "in Transportation Planning at the City of Toronto, with a master's degree in transportation "
        "engineering from the University of Alberta, and I am interested in consulting work on "
        "transportation master plans, corridor studies and traffic impact studies.",

        "At the City I review development applications and the transportation studies filed with them, "
        "analyze Transportation Tomorrow Survey data to find where capacity is short, and write the briefing "
        "notes that carry findings and options to senior staff. That is the client side of the studies your "
        "team prepares. At Mott MacDonald I simulated Ontario Line construction staging and road closures "
        "in Synchro, and I have also worked in VISSIM, MATSim and OpenTrack. I use GIS, AutoCAD, Python and "
        "SQL day to day.",

        TOOLS_SENTENCE,

        "I should be straightforward about the gaps. The posting asks for ten years and a P.Eng., and I "
        "have about four and a half years of relevant experience and am not registered with Professional "
        "Engineers Ontario, as an EIT or otherwise. I have reviewed traffic impact studies rather than "
        "written them for clients, and I have not led road safety audits, prepared proposals or schedules "
        "for a consulting practice, or supervised or mentored staff. I have not used Sidra or EMME, and I "
        "hold no PTP, PTOE or RSP designation. I am applying because traffic analysis, modelling and "
        "transportation planning is where my experience sits, and I would like to grow into a lead role.",

        "Thank you for considering my application.",
    ])

# ---------------------------------------------------------------- Barrick 4473804708
RESUME_4473804708 = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner with the City of Toronto, "
    "where GIS and Python are the tools behind much of the work. Builds and maintains large spatial datasets, "
    "a validated data dashboard and tooling that automates analysis. Earlier GIS work covered wildfire "
    "evacuation planning in Alberta communities.",
    city(ROW, DASHBOARD, TTS, DATA_KPI, PROJECTS, BRIEFING)
    + metrolinx(CVT, CLI, OPENTRACK) + MOTT + UOFA,
    skills=skills("ArcGIS Pro, QGIS and MapBox. Python, SQL and JavaScript. Spatial analysis, data validation "
                  "and dashboards. Large multi-source datasets. AutoCAD and Civil 3D. "
                  "Synchro, VISSIM, OpenTrack and MATSim. MS Office."))

COVER_4473804708 = letter(
    "Hiring Team", "Exploration", "Barrick Mining Corporation",
    "Re: Canada - Geospatial Data & GIS Solutions Lead",
    "Dear Hiring Team,",
    [
        "I would like to be considered for the Geospatial Data & GIS Solutions Lead position. I am an Assistant "
        "Planner in Transportation Planning at the City of Toronto, with a master's degree in transportation "
        "engineering from the University of Alberta, where my thesis used GIS to study how much traffic a "
        "community's roads could carry in a wildfire evacuation.",

        "At the City, GIS and Python are how I keep the division's data usable. I build and maintain the road "
        "and right-of-way datasets that Transportation Planning depends on, including a right-of-way width "
        "dataset for all city roads, built with QGIS, MapBox and JavaScript from sources that used to be "
        "scattered. I also built the Transportation Data Dashboard, which brought several years of survey data "
        "into one validated source in place of a report rebuilt by hand each quarter. Compiling, checking and "
        "standardizing spatial data from several sources, and automating the repetitive parts with Python and "
        "SQL, is most of what I do.",

        TOOLS_SENTENCE,

        "I should be straightforward about the gaps. My work has been in transportation, not in mining, "
        "geoscience or exploration, and I have not worked with remote sensing or satellite imagery. My "
        "professional GIS experience is shorter than the five years the posting asks for and is mixed in with "
        "other planning work. I have worked mainly in ArcGIS Pro and QGIS, and I have not administered ArcGIS "
        "Enterprise or Web GIS, or supported field teams with them. I have not supervised staff and I do not hold "
        "a GISP or Esri certification. I am applying because the spatial data management and Python automation "
        "is where my experience sits, and I would be glad to learn the geoscience side.",

        "Thank you for considering my application.",
    ])
