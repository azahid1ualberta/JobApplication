# -*- coding: utf-8 -*-
"""26 October 2026, sent in chat: three more Metrolinx postings.

    117344  Engineering Lead - GIS: already built on 13 October from LinkedIn (content28, MX_GIS);
            rebuilt with today's date, the job ID and the new education block. Closes 26 Oct, 11:59 PM.
    116577  Project Manager, Union Station Rail Corridor (temporary assignment up to 7 months)
    117601  Project Manager, Union Station Rail Corridor (permanent)

The USRC postings share the duties of 116406 (content41), so their letters follow it.
"""

import content20
from content3 import resume
from content20 import letter
from content28 import (TOOLS_ALSO, RESUME_MX_PM, RESUME_MX_GIS, COVER_MX_GIS)

content20.DATE = "October 26, 2026"


# ================================================ 117344 Engineering Lead - GIS (rebuild)

RESUME_117344 = RESUME_MX_GIS
COVER_117344 = [l.replace("PLT: October 13, 2026", "PLT: October 26, 2026")
                 .replace("PLT: **Re: Engineering Lead - Geographic Information Systems (GIS)**",
                          "PLT: **Re: Engineering Lead - Geographic Information Systems (GIS), Job ID 117344**")
                for l in COVER_MX_GIS]


# ================================================ USRC Project Manager letters

def usrc_letter(job_id, kind, extra_gap):
    return letter(
        "Talent Acquisition", "Capital Projects Group (GO & UP), GO Expansion - USRC",
        "Metrolinx, 130 Adelaide Street West, Toronto, ON",
        f"Re: Project Manager, Union Station Rail Corridor{kind} (Job ID {job_id})", "Dear Hiring Manager,",
        [
            "I would like to apply for the Project Manager, Union Station Rail Corridor position with the GO "
            "Expansion USRC project. I am an Assistant Planner in Transportation Planning at the City of Toronto, "
            "and before that I was a Transportation Planner at Metrolinx in GO rail service design.",

            "Much of the role is keeping a project moving: tracking day-to-day tasks, reporting to management, and "
            "working with municipalities, transit authorities, agencies and property owners to resolve issues. At "
            "the City I run assigned projects from scoping through to recommendations, holding the schedule and "
            "quality myself and reporting progress to the people relying on it, and I coordinate with divisions, "
            "consultants, applicants and outside agencies whose priorities conflict.",

            "At Metrolinx I ran OpenTrack simulations of GO rail services and assessed what temporary and permanent "
            "slow orders, the kind of restriction construction on an operating railway imposes, would do to "
            "service. " + TOOLS_ALSO + " At Mott MacDonald I ran Synchro traffic simulations of Ontario Line "
            "construction staging.",

            "I should be straightforward about the gaps. I have not managed the planning, design, construction or "
            "commissioning of rail infrastructure, coordinated cost estimates, or supervised staff, and my "
            "knowledge of construction in an operating railway comes from assessing what slow orders do to "
            "service. " + extra_gap,

            "Thank you for considering my application.",
        ])


RESUME_116577 = RESUME_MX_PM
COVER_116577 = usrc_letter("116577", ", Temporary Assignment",
                           "I do not hold a PMP, P.Eng. or Class G licence, which the posting lists as assets.")

RESUME_117601 = RESUME_MX_PM
COVER_117601 = usrc_letter("117601", "",
                           "I do not hold a PMP or P.Eng., which the posting lists as assets, and I do not currently "
                           "hold a Class G licence, so the driver's abstract the posting requires is something I "
                           "would need to resolve.")
