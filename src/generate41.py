import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content41 as C
from generate19 import fit, RESUME_STEPS, LETTER_STEPS

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "applications")
JOBS = [("117600", "Metrolinx-Manager-Project-Delivery-Union-Plus-117600", "Manager, Project Delivery"),
        ("117614", "Metrolinx-Data-Scientist-II-117614", "Data Scientist II"),
        ("117642", "Metrolinx-Senior-BI-Performance-Analyst-117642", "Senior Business Intelligence Performance Analyst"),
        ("116406", "Metrolinx-Project-Manager-USRC-116406", "Project Manager, Union Station Rail Corridor")]
for k, f, role in JOBS:
    d = os.path.join(A, f)
    os.makedirs(d, exist_ok=True)
    r = fit(getattr(C, "RESUME_" + k), d + "/Abdullah_Al_Zahid_Resume.pdf", RESUME_STEPS,
            leading_mult=1.25, space_after=2.2, head_before=9, title=f"Abdullah Al Zahid - Resume - {role}")
    c = fit(getattr(C, "COVER_" + k), d + "/Abdullah_Al_Zahid_Cover_Letter.pdf", LETTER_STEPS,
            leading_mult=1.36, space_after=8, title=f"Abdullah Al Zahid - Cover Letter - {role}")
    print(k, f"resume {r} | letter {c}")
