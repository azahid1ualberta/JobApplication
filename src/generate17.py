import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdfbuilder3 import build_pdf
import content17 as C

d = "/home/user/JobApplication/applications/Metrolinx-Manager-System-Risk-Modeling-Intelligence-117339"
os.makedirs(d, exist_ok=True)

# The original August settings: 9.3pt resume body holds one page with all six
# Metrolinx bullets, including the Crew Variance Tool and command line workflow.
build_pdf(C.RESUME_117339, os.path.join(d, "Abdullah_Al_Zahid_Resume.pdf"),
          body_size=9.3, leading_mult=1.25, space_after=2.2, margin=0.68, head_before=9,
          title="Abdullah Al Zahid - Resume - Manager, System Risk Modeling & Intelligence (117339)")
build_pdf(C.COVER_117339, os.path.join(d, "Abdullah_Al_Zahid_Cover_Letter.pdf"),
          body_size=10, leading_mult=1.36, space_after=8, margin=0.85,
          title="Abdullah Al Zahid - Cover Letter - Manager, System Risk Modeling & Intelligence (117339)")
print("built")
