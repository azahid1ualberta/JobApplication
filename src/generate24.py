import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content24 as C
from generate19 import fit, RESUME_STEPS, LETTER_STEPS

d = "/home/user/JobApplication/applications/Stantec-Transportation-Planner-Markham-2026-10"
os.makedirs(d, exist_ok=True)
r = fit(C.RESUME_STANTEC_TP, os.path.join(d, "Abdullah_Al_Zahid_Resume.pdf"), RESUME_STEPS,
        leading_mult=1.25, space_after=2.2, head_before=9,
        title="Abdullah Al Zahid - Resume - Transportation Planner")
c = fit(C.COVER_STANTEC_TP, os.path.join(d, "Abdullah_Al_Zahid_Cover_Letter.pdf"), LETTER_STEPS,
        leading_mult=1.36, space_after=8,
        title="Abdullah Al Zahid - Cover Letter - Transportation Planner")
print(f"resume {r[0]}pt @ {r[1]}in | letter {c[0]}pt @ {c[1]}in")
