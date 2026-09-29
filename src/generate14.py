import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdfbuilder3 import build_pdf
import content14 as C

d = "/home/user/JobApplication/applications/Metrolinx-Rail-Simulation-Specialist-117317"
os.makedirs(d, exist_ok=True)

# Both documents are set to the loosest spacing that still holds one page.
# The resume is the tighter of the two because it carries four jobs; the gaps
# below are all proportional to the body size, so the rhythm stays even.
build_pdf(C.RESUME_117317, os.path.join(d, "Abdullah_Al_Zahid_Resume.pdf"),
          body=9.2, lead_mult=1.36,
          para_gap=6.0, bullet_gap=3.9, entry_gap=8.7, head_gap=11.5,
          line_gap=2.8, margin=0.68, name_size=19,
          title="Abdullah Al Zahid - Resume - Rail Simulation Specialist (117317)")

build_pdf(C.COVER_117317, os.path.join(d, "Abdullah_Al_Zahid_Cover_Letter.pdf"),
          body=9.4, lead_mult=1.42,
          para_gap=11.0, line_gap=3.0, margin=0.9, name_size=19,
          title="Abdullah Al Zahid - Cover Letter - Rail Simulation Specialist (117317)")
print("built")
