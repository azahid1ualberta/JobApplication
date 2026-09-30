import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdfbuilder3 import build_pdf
import content18 as C

d = "/home/user/JobApplication/applications/Metrolinx-Project-Manager-Lakeshore-West-Stations-Rehabilitation-117202"
os.makedirs(d, exist_ok=True)

# 9.3pt with 0.55in side margins, as for 117364: the extra Metrolinx bullets
# do not hold one page at the standard 0.68in.
build_pdf(C.RESUME_117202, os.path.join(d, "Abdullah_Al_Zahid_Resume.pdf"),
          body_size=9.3, leading_mult=1.25, space_after=2.2, margin=0.55, head_before=9,
          title="Abdullah Al Zahid - Resume - Project Manager, Lakeshore West ESR (117202)")
build_pdf(C.COVER_117202, os.path.join(d, "Abdullah_Al_Zahid_Cover_Letter.pdf"),
          body_size=10, leading_mult=1.36, space_after=8, margin=0.85,
          title="Abdullah Al Zahid - Cover Letter - Project Manager, Lakeshore West ESR (117202)")
print("built")
