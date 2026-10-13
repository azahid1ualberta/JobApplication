import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content28 as C
from generate19 import fit, RESUME_STEPS, LETTER_STEPS

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "applications")
JOBS = [("MX_GIS", "Metrolinx-Engineering-Lead-GIS-4476855569", "Engineering Lead - GIS"),
        ("OPS_GOLRT", "Ontario-Public-Service-Manager-GO-LRT-4471948021", "Manager, GO-LRT"),
        ("MISS_TRAFFIC", "City-of-Mississauga-Supervisor-Traffic-Planning-28597", "Supervisor, Traffic Planning"),
        ("DURHAM", "Region-of-Durham-Senior-Planner-24244", "Senior Planner"),
        ("SYSTRA_GIS", "SYSTRA-GIS-Manager-GO-Expansion-4467587249", "GIS Manager"),
        ("PEARSON", "Toronto-Pearson-Senior-Capacity-Planning-Analyst-4471907925", "Senior Capacity Planning Analyst"),
        ("MX_SPONSOR", "Metrolinx-Sponsor-Officer-GO-Expansion-4473808230", "Sponsor Officer, GO Expansion"),
        ("MX_AGREE", "Metrolinx-Senior-Advisor-Agreements-4474218523", "Senior Advisor, Agreements"),
        ("MX_OPREADY", "Metrolinx-Operational-Readiness-Specialist-4475495932", "Operational Readiness Specialist"),
        ("MX_SSE", "Metrolinx-Senior-Advisor-SSE-4476864368", "Senior Advisor, SSE"),
        ("MX_PM", "Metrolinx-Project-Manager-Union-Station-Enhancement-4475743512", "Project Manager"),
        ("MX_GXO", "Metrolinx-Senior-Manager-GO-Expansion-Operations-4473399545", "Senior Manager, GO Expansion Operations"),
        ("MM_ADV", "Mott-MacDonald-Advisory-Consultant-4472048640", "Advisory Consultant"),
        ("MM_OR", "Mott-MacDonald-Senior-Advisory-Consultant-Operational-Readiness-4470639693",
         "Senior Advisory Consultant, Operational Readiness"),
        ("MM_PM", "Mott-MacDonald-Project-Manager-4450679013", "Project Manager"),
        ("DIL", "Dillon-Transportation-Planner-Engineer-Toronto-4454867596", "Transportation Planner-Engineer"),
        ("DIL_SR", "Dillon-Senior-Transportation-Planner-Engineer-4338753958", "Senior Transportation Planner-Engineer"),
        ("GHD", "GHD-Senior-Transportation-Planner-Traffic-Engineer-4474284635",
         "Senior Transportation Planner - Traffic Engineer"),
        ("EGIS", "Egis-Project-Manager-Rail-Transit-4467784730", "Project Manager, Rail & Transit"),
        ("CNV_GIS", "City-of-North-Vancouver-Manager-GIS-4475965890", "Manager, GIS"),
        ("SKY_GIS", "Skyline-Recruitment-GIS-Manager-4476799886", "GIS Manager"),
        ("WSP_AVN", "WSP-Aviation-Planner-4429033181", "Aviation Planner"),
        ("BINNIE", "Binnie-Project-Manager-Transportation-Major-Projects-4462349430", "Project Manager"),
        ("AECON", "Aecon-Traffic-Lead-4452988953", "Traffic Lead"),
        ("COT_SPATIAL", "City-of-Toronto-Spatial-Specialist-66074", "Spatial Specialist")]
only = sys.argv[1:]
for k, f, role in JOBS:
    if only and k not in only:
        continue
    d = os.path.join(A, f)
    os.makedirs(d, exist_ok=True)
    r = fit(getattr(C, "RESUME_" + k), d + "/Abdullah_Al_Zahid_Resume.pdf", RESUME_STEPS,
            leading_mult=1.25, space_after=2.2, head_before=9, title=f"Abdullah Al Zahid - Resume - {role}")
    c = fit(getattr(C, "COVER_" + k), d + "/Abdullah_Al_Zahid_Cover_Letter.pdf", LETTER_STEPS,
            leading_mult=1.36, space_after=8, title=f"Abdullah Al Zahid - Cover Letter - {role}")
    print(k, f"resume {r} | letter {c}")
