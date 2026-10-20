# -*- coding: utf-8 -*-
"""20 October 2026 daily run: Infrastructure Ontario Senior Planning Advisor (4480256435)."""

import content20
from content3 import (NAME, CONTACT, MOTT, UOFA, resume)
from content19 import (OPENTRACK, CVT, CLI, DASHBOARD, TOOLS_SENTENCE, city, metrolinx, skills,
                       BRIEFING, PROJECTS, COORD, REVIEW_DEV, DATA_KPI, CAPITAL)
from content20 import (TTS, DEV_STUDIES, REPORTS, AGENCIES, letter)

content20.DATE = "October 20, 2026"

# ---------------------------------------------------------------- Infrastructure Ontario 4480256435
RESUME_4480256435 = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner with the City of Toronto, "
    "where assigned projects run from scoping to recommendations. Builds validated data sources and dashboards "
    "that management reports from, coordinates consultants and other divisions, and writes the briefing notes "
    "that carry issues and options to senior staff.",
    city(PROJECTS, DASHBOARD, CAPITAL, DATA_KPI, COORD, BRIEFING)
    + metrolinx(OPENTRACK, CVT, CLI) + MOTT + UOFA,
    skills=skills("Project scoping and coordination. Dashboards and reporting from validated data. Briefing "
                  "notes, reports and presentations. Python, SQL and advanced Excel. ArcGIS Pro, QGIS, MapBox. "
                  "Synchro, VISSIM and OpenTrack. MS Office."))

COVER_4480256435 = letter(
    "Hiring Manager", "Capital Investments", "Infrastructure Ontario, 1 Dundas Street West",
    "Re: Senior Planning Advisor",
    "Dear Hiring Manager,",
    [
        "I would like to apply for the Senior Planning Advisor position in Capital Investments. I am an "
        "Assistant Planner in Transportation Planning at the City of Toronto, with a master's degree in "
        "transportation engineering. The part of the posting I can speak to most directly is turning project "
        "and network information into reports, dashboards and briefing material that people making decisions "
        "can rely on.",

        "At the City I run assigned projects from scoping through to recommendations, working with other "
        "divisions and consultants whose priorities do not always line up. I analyze network data to work out "
        "where capacity is short and what that means for maintenance and capital spending, and I built the "
        "Transportation Data Dashboard, which replaced a report rebuilt by hand each quarter with one validated "
        "source. I write the briefing notes and presentations that put issues and options in front of senior "
        "staff. Earlier, at Metrolinx, I assessed proposed operating changes in OpenTrack before they were "
        "taken forward.",

        TOOLS_SENTENCE,

        "I should be straightforward about the gaps. I have not worked in capital project intake or portfolio "
        "management, and I have not done project cost estimation or managed a budget. I have not used Power BI; "
        "my dashboard and reporting work has been in Python, GIS tools and Excel. I know stage-gate and "
        "complexity-assessment frameworks from reading rather than from practice, and I do not hold a PMP or a "
        "P.Eng. I am applying because the planning, data and reporting work is close to what I already do, and "
        "I would like to apply it to a broader capital portfolio.",

        "Thank you for considering my application.",
    ])
