import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdfbuilder3 import build_pdf
import content15 as C

d = "/home/user/JobApplication/applications/Metrolinx-Manager-Rapid-Transit-Program-Delivery-117264"
os.makedirs(d, exist_ok=True)

build_pdf(C.RESUME_117264, os.path.join(d, "Abdullah_Al_Zahid_Resume.pdf"),
          body_size=9.4, leading_mult=1.25, space_after=2.2, margin=0.68, head_before=9,
          title="Abdullah Al Zahid - Resume - Manager, Rapid Transit Program Delivery (117264)")
build_pdf(C.COVER_117264, os.path.join(d, "Abdullah_Al_Zahid_Cover_Letter.pdf"),
          body_size=10, leading_mult=1.36, space_after=8, margin=0.85,
          title="Abdullah Al Zahid - Cover Letter - Manager, Rapid Transit Program Delivery (117264)")
print("built")
