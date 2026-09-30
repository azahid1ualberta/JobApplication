# -*- coding: utf-8 -*-
"""Shared building blocks for the tailored resumes and cover letters.

No qualification-mapping section. Conventional order: summary, experience,
skills, education. Cover letters run four or five paragraphs and read like a
person wrote them.
"""

NAME = "Abdullah Al Zahid"
CONTACT = "Toronto, ON  |  (780) 982-3680  |  azahid1@ualberta.ca  |  linkedin.com/in/abdullah-al-zahid"

# ------------------------------------------------------------------ building blocks

CITY_HEAD = ["SUB: Assistant Planner, Transportation Planning",
             "DATE: City of Toronto  |  January 2024 – present"]

CITY_INFRA = CITY_HEAD + [
    "B: Build and maintain the road and right-of-way datasets Transportation Planning depends on, using GIS "
    "and Python to merge sources that were scattered across the division.",
    "B: Built the Transportation Data Dashboard, combining several years of survey data and checking it for "
    "consistency before it reaches management reporting.",
    "B: Review development applications and the studies filed with them against City standards and Official "
    "Plan policy, and recommend conditions where something is missing.",
    "B: Analyze travel and network data to work out where capacity is short, and what that means for "
    "maintenance and capital spending.",
    "B: Run assigned projects from scoping through to recommendations, writing the briefing notes and memos "
    "that come out of them and presenting to planners, engineers and managers in other divisions.",
]

CITY_POLICY = CITY_HEAD + [
    "B: Research policy questions as they come up, looking at how City policy, provincial legislation and work "
    "by other levels of government bear on them, and set out options for the division.",
    "B: Write briefing notes, memos and presentations that senior staff use to make decisions or to put the "
    "division's position in cross-divisional discussions.",
    "B: Built the Transportation Data Dashboard, pulling several years of survey data into one validated "
    "source so performance reporting is continuous rather than rebuilt from scratch each time.",
    "B: Review development applications and consultant studies for consistency with Official Plan policy, and "
    "recommend changes to process where the same problem keeps recurring.",
    "B: Run assigned projects on my own from scoping through to recommendations, working with divisions, "
    "consultants and outside agencies whose priorities do not always line up.",
]

CITY_TECH = CITY_HEAD + [
    "B: Build and maintain the datasets and tooling Transportation Planning depends on, using Python and GIS, "
    "with the validation and documentation that access-controlled municipal data requires.",
    "B: Built the Transportation Data Dashboard, integrating several years of survey data from multiple "
    "sources into a single reporting product used across the division.",
    "B: Run assigned technical projects on my own, from working out what is actually needed through to "
    "delivery and handover.",
    "B: Work with divisions, consultants and outside agencies to reconcile competing requirements and explain "
    "technical work to people making decisions on it.",
]

METROLINX_HEAD = ["SUB: Transportation Planner, Simulation and Modelling",
                  "DATE: Metrolinx, Service Design  |  February 2023 – January 2024"]

METROLINX = METROLINX_HEAD + [
    "B: Ran OpenTrack simulations of GO rail services to test how infrastructure constraints and speed "
    "restrictions affected run times and schedule reliability.",
    "B: Established what proposed operating changes would do to run times, equipment and schedule, and put "
    "the evidence in front of schedulers, operations staff and engineers.",
    "B: Built the data handling behind that analysis in Python, replacing a manual process for summarising "
    "operations data across subdivisions.",
    "B: Worked with schedulers, operations staff and engineers to pin down the technical and operational "
    "variables that had to go into a service plan.",
]

MOTT = [
    "SUB: Graduate Transportation Planner",
    "DATE: Mott MacDonald  |  January – February 2023",
    "B: Short consulting placement on Ontario Line work. Ran traffic simulations to estimate how construction "
    "staging would affect surrounding streets, and prepared the supporting material for the project team.",
]

UOFA = [
    "SUB: Graduate Research Assistant",
    "DATE: University of Alberta  |  January 2020 – August 2022",
    "B: Master's research on how road networks perform during emergency evacuations, using macroscopic (LWR) "
    "and agent-based (MATSim) models.",
    "B: Worked with large travel datasets and wrote up results for readers without a modelling background.",
]

SKILLS = [
    "H2: Skills",
    "P: Python (Pandas, NumPy), SQL and JavaScript. ArcGIS, QGIS and geospatial analysis. OpenTrack rail "
    "simulation, VISSIM, Synchro and MATSim. Data handling, pipelines and validation. Dashboards and "
    "performance reporting. MS Office, including large multi-source Excel workbooks.",
]

EDU = [
    "H2: Education",
    "P: **MSc, Transportation Engineering** — University of Alberta, 2022",
    "P: **BSc, Civil Engineering** — Bangladesh University of Engineering and Technology, 2018",
    "P: **BSc, Computer Science** — University of British Columbia, in progress (2025–2027)",
]


def resume(summary, experience, skills=None):
    return ([f"NAME: {NAME}", f"CONTACT: {CONTACT}", "H2: Summary", f"P: {summary}",
             "H2: Experience"] + experience + (skills or SKILLS) + EDU)
