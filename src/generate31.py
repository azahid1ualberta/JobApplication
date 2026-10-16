import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content31 as C
from generate19 import fit, RESUME_STEPS, LETTER_STEPS

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "applications")
JOBS = [("67209", "City-of-Toronto-Project-Manager-Transportation-Services-Vision-Zero-67209",
         "Project Manager, Transportation Services")]
for k, f, role in JOBS:
    d = os.path.join(A, f)
    os.makedirs(d, exist_ok=True)
    r = fit(getattr(C, "RESUME_" + k), d + "/Abdullah_Al_Zahid_Resume.pdf", RESUME_STEPS,
            leading_mult=1.25, space_after=2.2, head_before=9, title=f"Abdullah Al Zahid - Resume - {role}")
    c = fit(getattr(C, "COVER_" + k), d + "/Abdullah_Al_Zahid_Cover_Letter.pdf", LETTER_STEPS,
            leading_mult=1.36, space_after=8, title=f"Abdullah Al Zahid - Cover Letter - {role}")
    print(k, f"resume {r} | letter {c}")
