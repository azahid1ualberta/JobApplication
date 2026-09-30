import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdfbuilder3 import build_pdf
import content16 as C

APPS = "/home/user/JobApplication/applications"
# (job id, folder, role, resume body size, resume side margin)
# With the Crew Variance Tool and command line bullets added, two resumes no
# longer hold one page at 9.4pt. 117225 drops to the original August 9.3pt;
# 117364 keeps 9.3pt with side margins narrowed to 0.55in.
JOBS = [
    ("116752", "Metrolinx-Project-Manager-Program-Delivery-Controls-116752",
     "Project Manager, Program Delivery Controls", 9.4, 0.68),
    ("117364", "Metrolinx-Project-Manager-Traffic-Transportation-Ontario-Line-117364",
     "Project Manager, Traffic & Transportation, Ontario Line", 9.3, 0.55),
    ("117225", "Metrolinx-Senior-Advisor-Commercial-Strategy-Rail-117225",
     "Senior Advisor, Commercial Strategy, Rail", 9.3, 0.68),
]

for jid, folder, role, body, side in JOBS:
    d = os.path.join(APPS, folder)
    os.makedirs(d, exist_ok=True)
    build_pdf(getattr(C, f"RESUME_{jid}"), os.path.join(d, "Abdullah_Al_Zahid_Resume.pdf"),
              body_size=body, leading_mult=1.25, space_after=2.2, margin=side, head_before=9,
              title=f"Abdullah Al Zahid - Resume - {role} ({jid})")
    build_pdf(getattr(C, f"COVER_{jid}"), os.path.join(d, "Abdullah_Al_Zahid_Cover_Letter.pdf"),
              body_size=10, leading_mult=1.36, space_after=8, margin=0.85,
              title=f"Abdullah Al Zahid - Cover Letter - {role} ({jid})")
print("built")
