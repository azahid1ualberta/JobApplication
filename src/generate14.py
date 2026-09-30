import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdfbuilder3 import build_pdf
import content14 as C

d = "/home/user/JobApplication/applications/Metrolinx-Rail-Simulation-Specialist-117317"
os.makedirs(d, exist_ok=True)

# Same settings as the August originals, with the resume body at 9.4pt rather
# than 9.3 -- the largest size that still holds one page with this content.
build_pdf(C.RESUME_117317, os.path.join(d, "Abdullah_Al_Zahid_Resume.pdf"),
          body_size=9.4, leading_mult=1.25, space_after=2.2, margin=0.68, head_before=9,
          title="Abdullah Al Zahid - Resume - Rail Simulation Specialist (117317)")
build_pdf(C.COVER_117317, os.path.join(d, "Abdullah_Al_Zahid_Cover_Letter.pdf"),
          body_size=10, leading_mult=1.36, space_after=8, margin=0.85,
          title="Abdullah Al Zahid - Cover Letter - Rail Simulation Specialist (117317)")
print("built")
