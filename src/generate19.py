import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pymupdf
from pdfbuilder3 import build_pdf
import content19 as C

APPS = "/home/user/JobApplication/applications"
JOBS = [
    ("65977", "City-of-Toronto-Project-Manager-Priority-Development-Review-65977",
     "Project Manager, Priority Development Review"),
    ("64483", "City-of-Toronto-Project-Manager-Business-Transformation-Parks-and-Recreation-64483",
     "Project Manager Business Transformation"),
    ("66777", "City-of-Toronto-Project-Manager-TW-Capital-Planning-Implementation-66777",
     "Project Manager TW"),
    ("67150", "City-of-Toronto-Project-Manager-Fleet-Safety-Operations-67150",
     "Project Manager, Fleet Safety Operations & Continuous Improvement"),
    ("64397", "City-of-Toronto-Senior-Project-Manager-TW-Water-Treatment-64397",
     "Senior Project Manager TW"),
]

# Largest type first; the first setting that holds one page is used. 9.4 and
# 9.3 at 0.68in are the August look; 0.55in side margins as on 117364.
RESUME_STEPS = [(9.4, 0.68), (9.3, 0.68), (9.3, 0.62), (9.3, 0.55), (9.2, 0.55)]
LETTER_STEPS = [(10.0, 0.85), (9.8, 0.85), (9.8, 0.8)]


def fit(lines, path, steps, **kw):
    for body, side in steps:
        build_pdf(lines, path, body_size=body, margin=side, **kw)
        if len(pymupdf.open(path)) == 1:
            return body, side
    raise RuntimeError(f"{path} does not fit one page")


for jid, folder, role in JOBS:
    d = os.path.join(APPS, folder)
    os.makedirs(d, exist_ok=True)
    r = fit(getattr(C, f"RESUME_{jid}"), os.path.join(d, "Abdullah_Al_Zahid_Resume.pdf"), RESUME_STEPS,
            leading_mult=1.25, space_after=2.2, head_before=9,
            title=f"Abdullah Al Zahid - Resume - {role} ({jid})")
    c = fit(getattr(C, f"COVER_{jid}"), os.path.join(d, "Abdullah_Al_Zahid_Cover_Letter.pdf"), LETTER_STEPS,
            leading_mult=1.36, space_after=8,
            title=f"Abdullah Al Zahid - Cover Letter - {role} ({jid})")
    print(f"{jid}: resume {r[0]}pt @ {r[1]}in | letter {c[0]}pt @ {c[1]}in")
