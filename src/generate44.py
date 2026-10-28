import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content44 as C
from generate19 import fit, RESUME_STEPS, LETTER_STEPS

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "applications")
JOBS = [
    ("GOMKT", "Metrolinx-Senior-Advisor-GO-Market-Development-4483683186", "Senior Advisor, GO Market Development"),
    ("56338", "Edmonton-Safe-Mobility-Analyst-56338", "Safe Mobility Analyst"),
    ("88758", "Alberta-TEC-Senior-Policy-Advisor-88758", "Senior Policy Advisor"),
    ("USGIS", "UrbanSystems-GIS-Analyst-Kamloops-4484251767", "GIS Analyst"),
    ("CMBC", "CMBC-Senior-Advisor-Zero-Emissions-4483671842", "Senior Advisor, Zero Emissions"),
    ("PLA", "Metrolinx-Project-Manager-Permits-Licenses-Approvals-4483679321", "Project Manager, Permit, Licenses & Approvals"),
    ("DILLON", "Dillon-Strategic-Lead-Transportation-Planning-4484288755", "Strategic Lead, Transportation Planning & Strategy"),
]
only = sys.argv[1:]
for k, f, role in JOBS:
    if only and k not in only:
        continue
    d = os.path.join(A, f)
    os.makedirs(d, exist_ok=True)
    r = fit(getattr(C, "RESUME_" + k), d + "/Abdullah_Al_Zahid_Resume.pdf", RESUME_STEPS,
            leading_mult=1.25, space_after=2.2, head_before=9, title=f"Abdullah Al Zahid - Resume - {role}")
    c = fit(getattr(C, "COVER_" + k), d + "/Abdullah_Al_Zahid_Cover_Letter.pdf", LETTER_STEPS,
            leading_mult=1.36, space_after=8, title=f"Abdullah Al Zahid - Cover Letter - {role}")
    print(k, f"resume {r} | letter {c}")
