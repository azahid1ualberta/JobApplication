import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content22 as C
from generate19 import fit, RESUME_STEPS, LETTER_STEPS

APPS = "/home/user/JobApplication/applications"
JOBS = [
    ("Dillon-Airport-Design-Engineer", "Airport Design Engineer", C.COVER_DILLON),
    ("WSP-Civil-Project-Engineer-Aviation-85226", "Civil Project Engineer - Aviation", C.COVER_WSP_AVIATION),
]
if __name__ == "__main__":
    for folder, role, cov in JOBS:
        d = os.path.join(APPS, folder)
        os.makedirs(d, exist_ok=True)
        r = fit(C.RESUME_CIVIL, os.path.join(d, "Abdullah_Al_Zahid_Resume.pdf"), RESUME_STEPS,
                leading_mult=1.25, space_after=2.2, head_before=9, title=f"Abdullah Al Zahid - Resume - {role}")
        c = fit(cov, os.path.join(d, "Abdullah_Al_Zahid_Cover_Letter.pdf"), LETTER_STEPS,
                leading_mult=1.36, space_after=8, title=f"Abdullah Al Zahid - Cover Letter - {role}")
        print(f"{folder}: resume {r[0]}pt @ {r[1]}in | letter {c[0]}pt @ {c[1]}in")
