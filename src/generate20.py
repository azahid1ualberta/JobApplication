import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content20 as C
from generate19 import fit, RESUME_STEPS, LETTER_STEPS

APPS = "/home/user/JobApplication/applications"
JOBS = [
    ("WSP-Senior-Passenger-Modelling-Specialist-94275", "Senior Passenger Modelling Specialist",
     C.RESUME_WSP, C.COVER_WSP),
    ("Stantec-Senior-Aviation-Planner-Airports", "Senior Aviation Planner",
     C.RESUME_AVIATION, C.COVER_STANTEC_SENIOR),
    ("Stantec-Aviation-Planner-Airports", "Aviation Planner",
     C.RESUME_AVIATION, C.COVER_STANTEC),
    ("CIMA-Senior-Aviation-Planner-REF3026P", "Senior Aviation Planner",
     C.RESUME_AVIATION, C.COVER_CIMA),
]

for folder, role, res, cov in JOBS:
    d = os.path.join(APPS, folder)
    os.makedirs(d, exist_ok=True)
    r = fit(res, os.path.join(d, "Abdullah_Al_Zahid_Resume.pdf"), RESUME_STEPS,
            leading_mult=1.25, space_after=2.2, head_before=9,
            title=f"Abdullah Al Zahid - Resume - {role}")
    c = fit(cov, os.path.join(d, "Abdullah_Al_Zahid_Cover_Letter.pdf"), LETTER_STEPS,
            leading_mult=1.36, space_after=8,
            title=f"Abdullah Al Zahid - Cover Letter - {role}")
    print(f"{folder}: resume {r[0]}pt @ {r[1]}in | letter {c[0]}pt @ {c[1]}in")
