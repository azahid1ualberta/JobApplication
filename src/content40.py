# -*- coding: utf-8 -*-
"""26 October 2026, sent in chat: four City of Toronto internal postings.

    67098  Project Lead, Transportation Services (Transportation Electrical Construction & Maintenance)
    67403  Engineer, Toronto Water, WIM Policy Development
    67513  Project Manager, Transportation Services (Operations Maintenance, CDDI Area 2)
    65654  Engineer, Toronto Water, Process Innovation & Energy
"""

import content20
from content3 import (MOTT, UOFA, resume)
from content19 import (OPENTRACK, SLOW, CVT, CLI, DASHBOARD, TOOLS_SENTENCE, city, metrolinx, skills,
                       BRIEFING, PROJECTS)
from content20 import (TTS, DEV_STUDIES, AGENCIES, letter)
from content28 import (ROW, STUDIES, POLICY_COUNCIL, EVIDENCE, TOOLS_ALSO)

content20.DATE = "October 26, 2026"


# ================================================ 67098 Project Lead, Transportation Services

RESUME_67098 = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner in Transportation Planning "
    "with the City of Toronto. Runs assigned projects from scoping to recommendations, coordinates with "
    "divisions, agencies and consultants, maintains the road and right-of-way datasets the division depends "
    "on, and writes the briefing notes and reports that carry issues to senior staff.",
    city(PROJECTS, AGENCIES, ROW, POLICY_COUNCIL)
    + metrolinx(OPENTRACK, SLOW, CVT, CLI) + MOTT + UOFA,
    skills=skills("Project planning, scheduling and follow-through. Coordination across City divisions, agencies "
                  "and consultants. Briefing notes, reports and presentations for senior staff. Synchro and "
                  "VISSIM. AutoCAD and Civil 3D; ArcGIS Pro, QGIS and MapBox. Python and SQL. MS Office."))

COVER_67098 = letter(
    "Sherwin de Castro", "Human Resources", "Transportation Services, City of Toronto",
    "Re: Project Lead, Transportation Services (Job ID 67098)", "Dear Sherwin de Castro,",
    [
        "I would like to be considered for one of the two Project Lead, Transportation Services positions in the "
        "Transportation Electrical Construction & Maintenance unit. I am an Assistant Planner in Transportation "
        "Planning at the City, and before that I worked in GO rail service design at Metrolinx and on Ontario "
        "Line traffic simulation at Mott MacDonald.",

        "Much of the role is project coordination and reporting in a complex municipal environment: managing "
        "projects from inception to completion, working across divisions, agencies and consultants, and "
        "preparing briefing materials and staff reports for senior management and Council. That is the shape "
        "of my work now. I run assigned projects from scoping through to recommendations, planning the work and "
        "holding the schedule myself, and I coordinate with divisions, consultants, applicants and outside "
        "agencies whose priorities conflict. I write the briefing notes, memos and presentations that carry "
        "issues to senior staff, and with policy staff I recommend and report to Council on new transportation "
        "regulations and guidelines.",

        "On the technical side, I build and maintain the road and right-of-way datasets the division depends "
        "on, using GIS and Python. At Mott MacDonald I ran Synchro traffic simulations to estimate how Ontario "
        "Line construction staging and road closures would affect the surrounding streets, and at Metrolinx I "
        "ran OpenTrack simulations of GO rail services. " + TOOLS_ALSO,

        "I should be straightforward about the gaps. The posting asks for considerable experience in traffic "
        "signals, ITS or streetlighting, and I have not worked on the design, construction or maintenance of "
        "any of them. I have not managed capital construction projects or project budgets, led a procurement "
        "process or managed contractors, and I have not given work direction to staff. I do not hold a P.Eng. "
        "or PMP, which the posting lists as assets, and I do not currently hold a Class G licence, which the "
        "posting requires, so I would need to resolve that.",

        "Thank you for considering my application.",
    ])


# ================================================ 67403 Engineer, Toronto Water, WIM Policy Development

RESUME_67403 = resume(
    "Civil engineer with a master's degree in transportation engineering, currently an Assistant Planner with "
    "the City of Toronto. Works with policy staff on transportation regulations and guidelines reported to "
    "Council, reviews development applications against City standards and Official Plan policy, and writes the "
    "briefing notes and reports that carry findings to senior staff.",
    city(POLICY_COUNCIL, DEV_STUDIES, STUDIES, AGENCIES, DASHBOARD)
    + metrolinx(OPENTRACK, SLOW, CVT, CLI) + MOTT + UOFA,
    skills=skills("Regulations and guidelines developed with policy staff and reported to Council. Development "
                  "application review against City standards and Official Plan policy. Technical reports, "
                  "briefing notes and presentations. Coordination across divisions, agencies and consultants. "
                  "Python (Pandas, NumPy), SQL, ArcGIS Pro and QGIS. AutoCAD and Civil 3D. MS Office."))

COVER_67403 = letter(
    "Lina Truong", "Human Resources", "Toronto Water, City of Toronto",
    "Re: Engineer, Water Infrastructure Management, Policy Development (Job ID 67403)", "Dear Lina Truong,",
    [
        "I would like to apply for the Engineer position with the Policy Development team in Toronto Water's "
        "Water Infrastructure Management section. I should say at the outset that I come to it from "
        "transportation planning rather than stormwater, and I have tried to be clear below about both what I "
        "would bring and where I fall short.",

        "Much of the posting is policy work: developing strategies, policies and guidelines, accounting for "
        "legislation and initiatives by other orders of government, and writing reports to Committees and "
        "Council. That is the part of my current job I would bring. In Transportation Planning I advise "
        "applicants and staff on transportation planning, by-laws and related regulations, monitor the effect "
        "of zoning regulations, and with policy staff recommend and report to Council on new transportation "
        "regulations and guidelines. I review development applications against City standards and Official "
        "Plan policy, and I write the briefing notes and presentations that carry findings to senior staff.",

        "I also run assigned studies from scoping through to recommendations, coordinate with divisions, "
        "consultants and outside agencies, and built the Transportation Data Dashboard, which brought several "
        "years of survey data into one validated source the division reports from. " + TOOLS_SENTENCE,

        "The gaps are substantial. The posting's first qualification is registration as a P.Eng. with PEO, and "
        "I am not registered. I do not have the three years of experience in the planning, design or "
        "construction of storm drainage and stormwater management infrastructure that the posting asks for, "
        "and I have not worked under the Ontario Water Resources Act or the Environmental Protection Act, or "
        "prepared business cases and bid documents. I am applying because the policy and reporting side of the "
        "role is familiar, and because the Qualified List covers permanent and temporary positions.",

        "Thank you for considering my application.",
    ])


# ================================================ 67513 Project Manager, Transportation Services (CDDI Area 2)

RESUME_67513 = resume(
    "Transportation engineer with a master's degree, currently an Assistant Planner with the City of Toronto. "
    "Runs assigned projects to schedule, coordinates across divisions, agencies and consultants, built the "
    "dashboard a division reports from, and prepares reports and presentations for senior staff.",
    city(PROJECTS, AGENCIES, DASHBOARD, BRIEFING, ROW)
    + metrolinx(OPENTRACK, SLOW, CVT, CLI) + MOTT + UOFA,
    skills=skills("Project planning, scheduling and follow-through. Data analysis, dashboards and reporting. "
                  "Coordination across City divisions, agencies and consultants. Reports and presentations for "
                  "senior management. Python (Pandas, NumPy), SQL and advanced Excel. ArcGIS Pro, QGIS and "
                  "MapBox. MS Office."))

COVER_67513 = letter(
    "Gera Mulira", "Human Resources", "Transportation Services, City of Toronto",
    "Re: Project Manager, Transportation Services (Job ID 67513)", "Dear Gera Mulira,",
    [
        "I would like to be considered for the Project Manager, Transportation Services position supporting the "
        "Manager, Contract Development, Delivery and Inspections, Area 2. I should say at the outset that this "
        "is an operations role and my background is in transportation planning, so I have tried to be clear "
        "below about both what I would bring and where I fall short.",

        "Parts of the role are close to my current work: developing plans and recommending policies and "
        "practices, preparing reports for senior management, presenting programs, and providing technical "
        "support across divisional lines. In Transportation Planning I run assigned projects from scoping "
        "through to recommendations, holding the schedule and quality myself, coordinate with divisions, "
        "consultants and outside agencies, and write the briefing notes, memos and presentations that carry "
        "issues to senior staff.",

        "The posting also places weight on systems that monitor productivity and performance. I built the "
        "Transportation Data Dashboard, which combined several years of survey data into one validated source "
        "the division reports from. " + TOOLS_SENTENCE,

        "The gaps are substantial. I have no experience in winter operations or summer maintenance contracts, "
        "and I have not supervised staff, handled labour relations or grievances under a collective agreement, "
        "or prepared operating and capital budgets. I have not used EWMS, SAP or GPS/AVL systems. I do not "
        "currently hold a Class G licence, which the posting requires along with a City Operator's Licence, "
        "so I would need to resolve that. I am applying because the planning and reporting side of the role is "
        "familiar, and because the Qualified List covers permanent and temporary positions.",

        "Thank you for considering my application.",
    ])


# ================================================ 65654 Engineer, Toronto Water, Process Innovation & Energy

RESUME_65654 = resume(
    "Civil engineer with a master's degree in transportation engineering, currently an Assistant Planner with "
    "the City of Toronto. Analyzes large datasets and develops recommendations from them, builds the Python "
    "tooling and dashboards behind that analysis, and writes the technical reports and briefing notes that "
    "carry findings to senior staff.",
    city(TTS, DASHBOARD, ROW, STUDIES)
    + metrolinx(CVT, CLI, OPENTRACK, EVIDENCE) + MOTT + UOFA,
    skills=skills("Data analysis, interpretation and recommendations: Python (Pandas, NumPy), SQL and advanced "
                  "Excel. Dashboards and validated reporting. Simulation: OpenTrack, VISSIM, Synchro and MATSim. "
                  "ArcGIS Pro and QGIS. AutoCAD and Civil 3D. Technical reports, briefing notes and "
                  "presentations. MS Office."))

COVER_65654 = letter(
    "Sarah Persadsingh", "Human Resources", "Toronto Water, City of Toronto",
    "Re: Engineer, Process Innovation & Energy (Job ID 65654)", "Dear Sarah Persadsingh,",
    [
        "I would like to apply for one of the two Engineer positions in Toronto Water's Process, Innovation & "
        "Energy unit. I should say at the outset that I come to it from transportation rather than water and "
        "wastewater process engineering, and I have tried to be clear below about both what I would bring and "
        "where I fall short.",

        "The part of the role I would bring is data analysis and the development of recommendations from it, "
        "which the posting lists among its qualifications. " + TOOLS_SENTENCE + " At the City I built the "
        "Transportation Data Dashboard, which combined several years of survey data into one validated source "
        "the division reports from, and I analyze travel and network data to work out where capacity is short.",

        "I write technical memoranda, briefing notes and presentations, run assigned studies from scoping "
        "through to recommendations, and coordinate with divisions, consultants and outside agencies. My "
        "master's research modelled how road networks perform during emergency evacuations.",

        "The gaps are substantial. The posting requires registration as a P.Eng. with PEO and a valid Class G "
        "licence, and I hold neither. I have no experience in wastewater or stormwater treatment, drinking "
        "water, biosolids or energy management, treatment process assessment and optimization, or bench and "
        "pilot trials, and I have not worked under the Safe Drinking Water Act, the Ontario Water Resources Act "
        "or the Environmental Protection Act. I am applying because the data analysis side of the role is "
        "familiar, and because the Qualified List covers permanent and temporary positions.",

        "Thank you for considering my application.",
    ])
