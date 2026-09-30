import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content23 as C
from generate19 import fit, RESUME_STEPS, LETTER_STEPS

d = "/home/user/JobApplication/applications/Stantec-Aviation-Project-Manager-1006666"
if __name__ == "__main__":
    os.makedirs(d, exist_ok=True)
    r = fit(C.RESUME_1006666, os.path.join(d, "Abdullah_Al_Zahid_Resume.pdf"), RESUME_STEPS,
            leading_mult=1.25, space_after=2.2, head_before=9,
            title="Abdullah Al Zahid - Resume - Aviation Project Manager")
    c = fit(C.COVER_1006666, os.path.join(d, "Abdullah_Al_Zahid_Cover_Letter.pdf"), LETTER_STEPS,
            leading_mult=1.36, space_after=8, title="Abdullah Al Zahid - Cover Letter - Aviation Project Manager")
    print(f"resume {r[0]}pt @ {r[1]}in | letter {c[0]}pt @ {c[1]}in")
