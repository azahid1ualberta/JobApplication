import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content27 as C
from generate19 import fit, RESUME_STEPS, LETTER_STEPS

A = "/home/user/JobApplication/applications/"
JOBS = [("HDR", "HDR-Transportation-Planner-Toronto-4476228723", "Transportation Planner"),
        ("YORK", "York-Region-Service-Planner-4476289029", "Service Planner"),
        ("ACR", "Metrolinx-Project-Manager-Adjacent-Construction-Review-4475706583",
         "Project Manager, Adjacent Construction Review")]
for k, f, role in JOBS:
    d = A + f
    os.makedirs(d, exist_ok=True)
    r = fit(getattr(C, "RESUME_" + k), d + "/Abdullah_Al_Zahid_Resume.pdf", RESUME_STEPS,
            leading_mult=1.25, space_after=2.2, head_before=9, title=f"Abdullah Al Zahid - Resume - {role}")
    c = fit(getattr(C, "COVER_" + k), d + "/Abdullah_Al_Zahid_Cover_Letter.pdf", LETTER_STEPS,
            leading_mult=1.36, space_after=8, title=f"Abdullah Al Zahid - Cover Letter - {role}")
    print(k, f"resume {r}pt | letter {c}")
