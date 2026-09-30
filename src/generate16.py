import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdfbuilder3 import build_pdf
import content16 as C

APPS = "/home/user/JobApplication/applications"
JOBS = [
    ("116752", "Metrolinx-Project-Manager-Program-Delivery-Controls-116752",
     "Project Manager, Program Delivery Controls"),
    ("117364", "Metrolinx-Project-Manager-Traffic-Transportation-Ontario-Line-117364",
     "Project Manager, Traffic & Transportation, Ontario Line"),
    ("117225", "Metrolinx-Senior-Advisor-Commercial-Strategy-Rail-117225",
     "Senior Advisor, Commercial Strategy, Rail"),
]

# Same settings as 117317 and 117264.
for jid, folder, role in JOBS:
    d = os.path.join(APPS, folder)
    os.makedirs(d, exist_ok=True)
    build_pdf(getattr(C, f"RESUME_{jid}"), os.path.join(d, "Abdullah_Al_Zahid_Resume.pdf"),
              body_size=9.4, leading_mult=1.25, space_after=2.2, margin=0.68, head_before=9,
              title=f"Abdullah Al Zahid - Resume - {role} ({jid})")
    build_pdf(getattr(C, f"COVER_{jid}"), os.path.join(d, "Abdullah_Al_Zahid_Cover_Letter.pdf"),
              body_size=10, leading_mult=1.36, space_after=8, margin=0.85,
              title=f"Abdullah Al Zahid - Cover Letter - {role} ({jid})")
print("built")
