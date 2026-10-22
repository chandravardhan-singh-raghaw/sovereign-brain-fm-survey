# export_openreview_v4.py  --  paste as ONE cell in Google Colab and run.
# Exports OpenReview search results (ICLR, NeurIPS, ICML; papers only) to CSV
# for screened.csv / search_log.csv. No login, no extra packages needed.
#
# Changes from v1:
#  * stops at OpenReview's pagination cap (offset 10,000) instead of erroring
#  * the API matches loosely, so results are filtered here to papers whose
#    title+abstract contain the exact phrase "foundation model" AND the
#    modality word (brain / EEG / fMRI / MRI), mirroring the website's results
#  * no openreview-py fallback
#  * v3: authors can arrive as strings OR dicts -> handled; UTC warning silenced
#  * v4: handles HTTP 429 (rate limit) with wait-and-retry, slower pacing,
#        and writes partial CSVs after every query so nothing is lost

import csv, datetime, time, re, requests
from google.colab import files   # remove this line if not on Colab

QUERIES = {'"foundation model" brain': ["brain"],
           '"foundation model" EEG':   ["eeg", "electroencephalogra"],
           '"foundation model" fMRI':  ["fmri"],
           '"foundation model" MRI':   ["mri", "magnetic resonance"]}
VENUES   = ["ICLR.cc", "NeurIPS.cc", "ICML.cc"]
MIN_YEAR = 2021
TODAY    = datetime.date.today().isoformat()
API      = "https://api2.openreview.net/notes/search"
MAX_OFFSET = 10000          # OpenReview hard cap
PAGE       = 1000

def get_with_retry(params, tries=8):
    """GET with exponential backoff on 429/5xx. Returns the response, or None on 400."""
    wait = 20
    for attempt in range(tries):
        r = requests.get(API, params=params, timeout=90)
        if r.status_code == 400:
            return None
        if r.status_code in (429, 500, 502, 503, 504):
            retry_after = r.headers.get("Retry-After")
            pause = int(retry_after) if retry_after and retry_after.isdigit() else wait
            print(f"   rate-limited ({r.status_code}); waiting {pause}s ...")
            time.sleep(pause)
            wait = min(wait * 2, 300)
            continue
        r.raise_for_status()
        return r
    raise RuntimeError("OpenReview kept rate-limiting after several retries; re-run later, finished queries are saved.")

def fetch(term, group):
    notes, offset = [], 0
    while offset < MAX_OFFSET:
        r = get_with_retry({"term": term, "group": group, "content": "all",
                            "source": "forum", "limit": PAGE, "offset": offset})
        if r is None:                      # hit the cap -> stop quietly
            break
        batch = r.json().get("notes", [])
        notes += batch
        if len(batch) < PAGE:
            break
        offset += PAGE
        time.sleep(1.5)
    return notes

def save(rows, hits):
    seen, unique = set(), []
    for r in rows:
        if r["doi_or_arxiv"] in seen:
            continue
        seen.add(r["doi_or_arxiv"]); unique.append(r)
    cols = ["record_id","bibkey","title","year","venue","venue_type","source_database",
            "doi_or_arxiv","query","url","authors","abstract"]
    with open("openreview_results.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(unique)
    with open("openreview_hits.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["database","query","date","hits"]); w.writeheader(); w.writerows(hits)
    return unique

def val(note, name):
    v = note.get("content", {}).get(name)
    return v.get("value") if isinstance(v, dict) else v

def year_of(note):
    for k in ("pdate", "cdate", "tcdate"):
        if note.get(k):
            return datetime.datetime.fromtimestamp(note[k] / 1000, datetime.timezone.utc).year
    return ""

def author_str(a):
    """authors may be a list of strings, a list of dicts, a dict, or a string."""
    if a is None:
        return ""
    if isinstance(a, dict):
        a = a.get("value", a.get("fullname", a.get("name", "")))
    if isinstance(a, str):
        return a
    out = []
    for x in a if isinstance(a, (list, tuple)) else [a]:
        if isinstance(x, dict):
            x = x.get("fullname") or x.get("name") or x.get("value") or x.get("id") or ""
        out.append(str(x))
    return "; ".join(o for o in out if o)

def matches(note, modality_words):
    text = f"{val(note,'title') or ''} {val(note,'abstract') or ''}".lower()
    return "foundation model" in text and any(w in text for w in modality_words)

rows, hits = [], []
for venue in VENUES:
    for q, words in QUERIES.items():
        raw = fetch(q, venue)
        kept = []
        for n in raw:
            y = year_of(n)
            if (y and y < MIN_YEAR) or not matches(n, words):
                continue
            kept.append(n)
            authors = val(n, "authors")
            venue_str = str(val(n, "venue") or val(n, "venueid") or venue)
            rows.append({
                "record_id": "", "bibkey": "",
                "title": val(n, "title") or "",
                "year": y,
                "venue": venue_str,
                "venue_type": "preprint" if ("Submission" in venue_str or "Rejected" in venue_str
                                             or "Withdrawn" in venue_str) else "conference",
                "source_database": f"OpenReview ({venue.split('.')[0]})",
                "doi_or_arxiv": f"openreview:{n.get('id','')}",
                "query": q,
                "url": f"https://openreview.net/forum?id={n.get('id','')}",
                "authors": author_str(authors),
                "abstract": re.sub(r"\s+", " ", val(n, "abstract") or ""),
            })
        hits.append({"database": "OpenReview", "query": f"{q} [{venue}]", "date": TODAY, "hits": len(kept)})
        print(f"{venue:11s} {q:28s} raw {len(raw):5d} -> matching {len(kept):4d}")
        save(rows, hits)                   # partial save: safe to interrupt
        time.sleep(5)

unique = save(rows, hits)

print(f"\n{len(rows)} matching hits across queries, {len(unique)} unique papers")
print("Files: openreview_results.csv (append to screened.csv), openreview_hits.csv (append to search_log.csv)")
files.download("openreview_results.csv")
files.download("openreview_hits.csv")
