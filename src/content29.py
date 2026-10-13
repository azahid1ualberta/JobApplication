# -*- coding: utf-8 -*-
"""13 October 2026 daily run."""

import content20
from content3 import (NAME, CONTACT, MOTT, UOFA, resume)
from content19 import (OPENTRACK, SLOW, CVT, CLI, DASHBOARD, TOOLS_SENTENCE, city, metrolinx, skills)
from content20 import (TTS, letter)
from content28 import ROW, STUDIES, TOOLS_ALSO, UOFA_GIS

content20.DATE = "October 13, 2026"

RESUME_CONSOR = resume(
    "Transportation engineer with a master's degree and four years of GIS and data work across municipal "
    "transportation planning at the City of Toronto and GO rail service planning at Metrolinx. Builds spatial "
    "datasets, web maps and tools in ArcGIS Pro, QGIS, MapBox and Python, and writes up the analysis for "
    "planners and engineers who use it.",
    city(ROW, DASHBOARD, TTS, STUDIES)
    + metrolinx(OPENTRACK, CVT, CLI) + MOTT + UOFA_GIS,
    skills=skills("ArcGIS Pro, QGIS and MapBox. Python (Pandas, NumPy), SQL and JavaScript for spatial data "
                  "processing and automation. Data integration, validation and dashboards. AutoCAD and Civil 3D. "
                  "OpenTrack, VISSIM, Synchro and MATSim. Advanced Excel. Reports and presentations for "
                  "technical and non-technical readers."))

COVER_CONSOR = letter(
    "Hiring Manager", "", "Consor Canada, Toronto, ON",
    "Re: Environmental GIS Analyst", "Dear Hiring Manager,",
    [
        "I would like to apply for the Environmental GIS Analyst position in Toronto. Since January 2024 I have "
        "been an Assistant Planner in Transportation Planning at the City of Toronto, where much of my work is "
        "building and looking after spatial data. Before that I was a Transportation Planner at Metrolinx, and "
        "my master's research at the University of Alberta used GIS to assess wildfire evacuation plans.",

        "At the City I build and maintain the road and right-of-way datasets the division depends on, using GIS "
        "and Python, including a right-of-way width dataset covering all city roads, built with QGIS, MapBox and "
        "JavaScript. I also built the Transportation Data Dashboard, which brought three Transportation "
        "Tomorrow Survey years into one validated source people now report from. I work in ArcGIS Pro, QGIS and "
        "SQL daily, and use Python to automate the repetitive parts. " + TOOLS_ALSO,

        "I should be straightforward about the gaps. My GIS work has been in transportation planning, not "
        "environmental consulting, and I have not mapped natural heritage, habitat, archaeology, hydrology or "
        "hydrogeology, or worked with the regulatory approval processes behind them. I have not processed "
        "LiDAR, drone or satellite imagery, run field data collection workflows, or built web maps and story "
        "maps in ArcGIS Online. My GIS experience is about four years rather than five, and I do not hold a GIS "
        "certification. I am applying because the core of the role, building clean spatial data and turning it "
        "into maps and analysis that others can use, is what I do now, and I would like to learn the environmental "
        "side from a team that works in it.",

        "Thank you for considering my application.",
    ])
