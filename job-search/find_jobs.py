# -*- coding: utf-8 -*-
"""Find new postings for the daily run.

    python3 job-search/find_jobs.py                     # list new candidates from every source
    python3 job-search/find_jobs.py --days 2            # LinkedIn: only postings from the last 2 days
    python3 job-search/find_jobs.py --dry-run           # do not record today's candidates in shown_jobs.txt
    python3 job-search/find_jobs.py show URL            # print one posting's full text
    python3 job-search/find_jobs.py show URL --pdf OUT  # ...and save it as the Job Description PDF

Sources:
  - City of Toronto: every opening on jobs.toronto.ca, not a keyword search.
  - LinkedIn's public job search (no login) for the KEYWORDS below, in Ontario and across Canada.
    Most employers, including Metrolinx, the regions and the consultancies, post there too.

URLs already in seen_jobs.txt, jobs already in the tracker or applications/, and the downgrade
titles that criteria.md lists are dropped. Everything else is printed for judgement: the script
does not decide fit. A candidate is listed in full on the first day it appears (recorded in
shown_jobs.txt) and in one line after that. Any source that fails is reported as UNREADABLE so
it reaches the run summary.
"""

import html
import os
import re
import sys
import time
import urllib.parse
import urllib.request

import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/126.0 Safari/537.36")

KEYWORDS = ["transportation planner", "transportation planning", "transportation engineer",
            "traffic engineer", "transit planner", "transportation analyst", "transportation modeller",
            "rail simulation", "service planner", "mobility planner", "transportation project manager",
            "transit advisor"]
LOCATIONS = [("Ontario, Canada", 3), ("Canada", 2)]   # (location, pages of 10)

# criteria.md, "DO NOT include" — titles only; the work is judged by reading the posting
DOWNGRADE = re.compile(r"\b(assistant|associate|junior|jr\b|entry[- ]level|graduate|intern|internship|co-?op|"
                       r"student|trainee|in[- ]training|eit|technician|technologist)\b"
                       r"|\b(analyst|planner|engineer|specialist)\s+(1|i)\b", re.I)
# City of Toronto lists every division's jobs: only these get their posting read for division and dates
CITY_RELEVANT = re.compile(r"transport|transit|traffic|planner|planning|engineer|project manager|program manager|"
                           r"\bgis\b|spatial|\bdata\b|research|policy|infrastructure|mobility|\broads?\b|"
                           r"right of way|capital|\bmodel", re.I)
# LinkedIn keyword search returns logistics, trades and IT roles too; these titles are never his field
NOISE = re.compile(r"logistic|supply chain|dispatch|carrier|freight|warehouse|truck|driver|delivery|shipping|courier|"
                   r"customs|sales|marketing|\bseo\b|account (director|manager|executive)|nurse|health|patient|\bcare\b|"
                   r"travel (agent|counsellor|consultant|expert)|rental|maintenance|mechanic|repair|pump|crushing|tire|"
                   r"mining|\bmill\b|inventory|relocation|apprentice|submarine|aircraft|propulsion|software|developer|"
                   r"data scientist|network engineer|\brf\b|radio|microwave|telecom|test analyst|\bbim\b|signal+ing|"
                   r"\bocs\b|electrification|structur|systems engineer|systems integration|architect|firmware|electrical|"
                   r"customer|client service|coordinator|scheduler|procurement|buyer|payroll|recruit|human resources|"
                   r"\bhr\b|finance|accountant|legal|teacher|instructor|operator|attendant|clerk|security|superintendent|"
                   r"foreman|estimator|surveyor|designer|draft|\bsap\b|first mile|last mile|warranty", re.I)
# ...and these employers' "transportation" roles are shipping and retail logistics
NOISE_EMPLOYER = re.compile(r"logistic|trucking|freight|courier|\btransport\b(?! canada)|day & ross|loblaw|"
                            r"canadian tire|tjx|amazon|uline|walmart|costco|sobeys|pepsico|accenture|toromont", re.I)
FRENCH = re.compile(r"[éèêàâçôû·]|\b(ingénieur|conseill|chargé|technicien|planificat|coordonnat|analyste|responsable|"
                    r"chef|spécialiste|professionnel)", re.I)


def get(url, tries=2):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-CA,en;q=0.9"})
    for i in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:  # noqa: BLE001 - report every failure, never stop the run
            err = e
            if getattr(e, "code", None) == 429:
                time.sleep(15)
            elif i + 1 < tries:
                time.sleep(3)
    raise err


def text(s):
    s = re.sub(r"<(br|/p|/li|/div|/h\d|/tr)[^>]*>", "\n", s)
    s = re.sub(r"<li[^>]*>", "\n- ", s)
    s = html.unescape(re.sub(r"<[^>]+>", "", s))
    s = re.sub(r"[ \t\xa0]+", " ", s)
    return re.sub(r"\n\s*\n+", "\n\n", s).strip()


def ids_in(url):
    return set(re.findall(r"\d{9,}", url or ""))


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def company_key(s):
    """'WSP in Canada' -> 'wsp', 'York Region (The Regional Municipality of York)' -> 'york region'."""
    s = norm(re.sub(r"\(.*?\)", "", s or ""))
    return " ".join(re.sub(r"\b(in canada|canada|inc|ltd|limited|corporation|corp|group|the)\b", "", s).split())


def iso(d):
    for fmt in ("%b %d, %Y", "%d-%b-%Y", "%a %b %d %H:%M:%S UTC %Y"):
        try:
            return time.strftime("%Y-%m-%d", time.strptime(d.strip(), fmt))
        except ValueError:
            pass
    return d


# ------------------------------------------------------------------ what we already have

def already_have():
    """URLs and job IDs in seen_jobs.txt (built or skipped) and the tracker; titles already built."""
    with open(os.path.join(HERE, "seen_jobs.txt")) as f:
        urls = {l.split()[0] for l in f if l.strip() and not l.startswith("#")}
    ids = set().union(*(ids_in(u) for u in urls)) if urls else set()
    pairs = set()
    ws = openpyxl.load_workbook(os.path.join(HERE, "Job_Tracker.xlsx")).active
    for row in ws.iter_rows(min_row=2, values_only=True):
        title, company, url = row[1], row[2], row[7]
        pairs.add((norm(title), company_key(company)))
        if url:
            urls.add(url)
            ids |= ids_in(url)
    built = [norm(d) for d in os.listdir(os.path.join(HERE, "..", "applications"))]
    return urls, ids, pairs, built


def have(j, urls, ids, pairs, built):
    t, c = norm(j["title"]), company_key(j["company"])
    return (j["url"] in urls or j["id"] in ids or (t, c) in pairs
            or any(t in b and c in b for b in built))


# ------------------------------------------------------------------ sources

def city_of_toronto():
    jobs, start, total = [], 0, None
    while total is None or start < total:
        s = get(f"https://jobs.toronto.ca/jobsatcity/search/?q=&sortColumn=referencedate&sortDirection=desc"
                f"&startrow={start}")
        m = re.search(r"Showing \d+ to \d+ of (\d+) Jobs", s)
        total = int(m.group(1)) if m else 0
        for tile in re.split(r'(?=<li class="job-tile)', s)[1:]:
            link = re.search(r'data-url="(/jobsatcity/job/[^"]+/(\d+)/)"', html.unescape(tile))
            if not link:
                continue
            fields = {k: html.unescape(v) for k, v in re.findall(
                r'section-label[^>]*>\s*(.*?)\s*</span>\s*<div[^>]*-value">\s*(.*?)\s*</div>', tile, re.S)}
            title = re.search(r'class="jobTitle-link[^>]*>\s*(.*?)\s*</a>', tile, re.S)
            jobs.append({"source": "City of Toronto", "id": link.group(2),
                         "url": "https://jobs.toronto.ca" + link.group(1),
                         "title": html.unescape(title.group(1)).strip() if title else "?",
                         "company": "City of Toronto", "location": "Toronto, ON",
                         "posted": iso(fields.get("Posting Date", "")), "stream": fields.get("Job Stream", "")})
        start += 25
        if not m:
            break
    return jobs, total


def city_details(j):
    """Division, salary, closing date and City job ID, from the posting itself."""
    t = show(j["url"])
    f = lambda k: (re.search(k + r":\s*(.+)", t) or [None, ""])[1].strip()
    period = re.search(r"Posting Period:\s*\S+\s+to\s+(\S+)", t)
    j["closes"] = iso(period.group(1)) if period else ""
    pay = re.search(r"\$[\d,. ]+\s*-\s*\$[\d,.]+", f("Salary") or f("Hourly Rate"))
    pay = pay.group(0).rstrip(", ") + ("/hr" if f("Hourly Rate") else "") if pay else ""
    j["location"] = f"{f('Division & Section')}; {pay}"
    j["city_id"] = f("Job ID")


def linkedin(days):
    jobs, requests, failures = {}, 0, []
    for kw in KEYWORDS:
        for loc, pages in LOCATIONS:
            for page in range(pages):
                q = urllib.parse.urlencode({"keywords": kw, "location": loc, "f_TPR": f"r{days * 86400}",
                                            "start": page * 10})
                try:
                    s = get("https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?" + q)
                except Exception as e:  # noqa: BLE001
                    failures.append(f"{kw} / {loc} / page {page + 1}: {e}")
                    break
                finally:
                    requests += 1
                    time.sleep(1.2)
                cards = re.findall(r"<li>(.*?)</li>", s, re.S)
                for c in cards:
                    url = re.search(r'href="(https://[a-z]+\.linkedin\.com/jobs/view/[^"?]+)', c)
                    if not url:
                        continue
                    jid = re.search(r"(\d{9,})$", url.group(1)).group(1)
                    g = lambda p: (lambda m: html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip() if m else "")(
                        re.search(p, c, re.S))
                    jobs.setdefault(jid, {"source": "LinkedIn", "id": jid,
                                          "url": "https://ca.linkedin.com/jobs/view/" + jid,
                                          "title": g(r'base-search-card__title">(.*?)</h3>'),
                                          "company": g(r'base-search-card__subtitle">(.*?)</h4>'),
                                          "location": g(r'job-search-card__location">(.*?)</span>'),
                                          "posted": (re.search(r'datetime="([^"]+)"', c) or [None, ""])[1]})
                if len(cards) < 10:
                    break
    return list(jobs.values()), requests, failures


# ------------------------------------------------------------------ one posting

def show(url):
    jid = (re.findall(r"\d{9,}", url) or [""])[-1]
    if "linkedin.com" in url:
        s = get("https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/" + jid)
        g = lambda p: (lambda m: text(m.group(1)) if m else "")(re.search(p, s, re.S))
        head = [("Title", g(r"<h2[^>]*top-card-layout__title[^>]*>(.*?)</h2>")),
                ("Company", g(r"topcard__org-name-link[^>]*>(.*?)</a>")),
                ("Location", g(r'topcard__flavor--bullet">(.*?)</span>')),
                ("Posted", g(r"posted-time-ago__text[^>]*>(.*?)</span>")),
                ("Salary", g(r'compensation__salary[^>]*>(.*?)</div>'))]
        crit = re.findall(r'description__job-criteria-subheader">(.*?)</h3>\s*<span[^>]*>(.*?)</span>', s, re.S)
        head += [(text(a), text(b)) for a, b in crit]
        body = g(r'show-more-less-html__markup[^>]*>(.*?)</div>')
    else:
        s = get(url)
        title = re.search(r'itemprop="title"[^>]*>\s*(.*?)\s*<', s, re.S)
        posted = re.search(r'datePosted"[^>]*content="([^"]+)"', s)
        head = [("Title", text(title.group(1)) if title else ""), ("Posted", posted.group(1) if posted else "")]
        i = s.find('class="jobdescription"')
        body = text(s[s.find(">", i) + 1:i + 80000].split("Apply now")[0]) if i >= 0 else text(s)
    head = [(k, v) for k, v in head if v]
    return "\n".join(f"{k}: {v}" for k, v in head) + f"\nURL: {url}\n\n{body}\n"


def save_pdf(posting, path):
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
    style = getSampleStyleSheet()["BodyText"]
    style.fontSize, style.leading = 9.5, 12.5
    story = []
    for para in posting.split("\n"):
        story.append(Paragraph(html.escape(para), style) if para.strip() else Spacer(1, 4))
    SimpleDocTemplate(path, pagesize=letter, leftMargin=54, rightMargin=54, topMargin=54,
                      bottomMargin=54).build(story)


# ------------------------------------------------------------------ main

def main():
    args = sys.argv[1:]
    if args[:1] == ["show"]:
        posting = show(args[1])
        print(posting)
        if "--pdf" in args:
            save_pdf(posting, args[args.index("--pdf") + 1])
        return
    days = int(args[args.index("--days") + 1]) if "--days" in args else 7
    urls, ids, pairs, built = already_have()

    found, report = [], []
    try:
        city, total = city_of_toronto()
        found += city
        report.append(f"City of Toronto: read all {total} openings.")
    except Exception as e:  # noqa: BLE001
        report.append(f"City of Toronto: UNREADABLE ({e}).")
    try:
        li, n, failures = linkedin(days)
        found += li
        report.append(f"LinkedIn public search: {len(li)} postings from the last {days} days, {n} requests"
                      + (f"; UNREADABLE for {len(failures)} queries: " + "; ".join(failures[:5]) if failures else "."))
    except Exception as e:  # noqa: BLE001
        report.append(f"LinkedIn public search: UNREADABLE ({e}).")

    new, seen, downgrade, other_city, noise, french = [], 0, [], [], [], []
    for j in found:
        city = j["source"] == "City of Toronto"
        if have(j, urls, ids, pairs, built):
            seen += 1
        elif DOWNGRADE.search(j["title"]):
            downgrade.append(j)
        elif city and not CITY_RELEVANT.search(j["title"] + " " + j["stream"]):
            other_city.append(j)
        elif not city and FRENCH.search(j["title"]):
            french.append(j)
        elif not city and (NOISE.search(j["title"]) or NOISE_EMPLOYER.search(j["company"])):
            noise.append(j)
        else:
            new.append(j)
    for j in new:
        if j["source"] == "City of Toronto":
            try:
                city_details(j)
                if j["city_id"] and any(b.endswith(" " + j["city_id"]) for b in built):
                    j["built"] = True
            except Exception as e:  # noqa: BLE001
                j["location"] = f"posting unreadable: {e}"
            time.sleep(0.5)
    seen += sum(1 for j in new if j.get("built"))
    new = [j for j in new if not j.get("built")]

    today = time.strftime("%Y-%m-%d")
    shown_path = os.path.join(HERE, "shown_jobs.txt")
    shown = {}
    if os.path.exists(shown_path):
        for line in open(shown_path):
            if line.strip() and not line.startswith("#"):
                shown[line.split()[0]] = line.split()[-1]
    earlier = [j for j in new if shown.get(j["url"], today) < today]
    new = [j for j in new if j not in earlier]
    if "--dry-run" not in args:
        with open(shown_path, "a") as f:
            f.writelines(f"{j['url']}  # first shown {today}\n" for j in new if j["url"] not in shown)

    print("## Sources\n")
    for r in report:
        print("- " + r)
    print(f"\n## New candidates ({len(new)}) — read each before deciding\n")
    print("| Posted | Closes | Title | Company | Location / division | URL |\n|---|---|---|---|---|---|")
    for j in sorted(new, key=lambda j: (j["source"] != "City of Toronto", j["posted"]), reverse=True):
        print(f"| {j['posted']} | {j.get('closes', '')} | {j['title']} | {j['company']} | {j['location']} | {j['url']} |")
    print(f"\n## Dropped as downgrade titles per criteria.md ({len(downgrade)})\n")
    print("; ".join(sorted({f"{j['title']} ({j['company']})" for j in downgrade})) or "none")
    print(f"\n## Other City of Toronto openings, outside his field ({len(other_city)})\n")
    print("; ".join(j["title"].title() for j in other_city) or "none")
    print(f"\n## Dropped from LinkedIn as outside his field ({len(noise)}) or French-language ({len(french)})\n")
    print("; ".join(sorted({j["title"] for j in noise})) or "none")
    print(f"\n## Shown on an earlier day and not built ({len(earlier)}): judged then; revisit only if asked\n")
    print("; ".join(sorted({f"{j['title']} ({j['company']})" for j in earlier})) or "none")
    print(f"\nAlready seen, skipped before, in the tracker or already built: {seen}")


if __name__ == "__main__":
    main()
