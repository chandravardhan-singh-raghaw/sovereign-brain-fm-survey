# export_preprints_v1.py  --  paste as ONE cell in Google Colab and run.
# Exports the protocol's preprint searches to CSV for screened.csv / search_log.csv:
#   * arXiv            via the official arXiv API (export.arxiv.org), restricted to
#                      cs.CV, cs.LG, eess.IV, q-bio.NC, submitted 2021-01-01 .. today
#   * bioRxiv, medRxiv via Europe PMC (indexes both; supports abstract search + dates)
# Outputs: preprints_results.csv (append to screened.csv), preprints_hits.csv (append to search_log.csv)
# Takes 10-20 minutes; progress is printed and partial results are saved as it goes.

import csv, time, datetime, re, requests, xml.etree.ElementTree as ET
from google.colab import files        # remove if not on Colab

START = datetime.date(2021, 1, 1)
TODAY = datetime.date.today()
FM_TERMS  = '("foundation model" OR "self-supervised" OR pretrain OR pretrained OR pretraining OR "representation learning")'
BRAIN_TERMS = '(brain OR neuroimaging OR MRI OR CT OR fMRI OR EEG OR MEG)'

COLS = ["record_id","bibkey","title","year","venue","venue_type","source_database",
        "doi_or_arxiv","query","url","authors","abstract"]
rows, hits = [], []

def save():
    seen, uniq = set(), []
    for r in rows:
        if r["doi_or_arxiv"] in seen: continue
        seen.add(r["doi_or_arxiv"]); uniq.append(r)
    with open("preprints_results.csv","w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=COLS); w.writeheader(); w.writerows(uniq)
    with open("preprints_hits.csv","w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["database","query","date","hits"]); w.writeheader(); w.writerows(hits)
    return uniq

# ----------------------------------------------------------------- arXiv API
ARXIV = "http://export.arxiv.org/api/query"
NS = {"a":"http://www.w3.org/2005/Atom","os":"http://a9.com/-/spec/opensearch/1.1/"}
cats = "(cat:cs.CV OR cat:cs.LG OR cat:eess.IV OR cat:q-bio.NC)"
arxiv_query = f"abs:{FM_TERMS} AND abs:{BRAIN_TERMS} AND {cats}"

def arxiv_page(start, n=500, tries=6):
    for t in range(tries):
        r = requests.get(ARXIV, params={"search_query": arxiv_query, "start": start, "max_results": n,
                                        "sortBy": "submittedDate", "sortOrder": "descending"}, timeout=120)
        if r.status_code == 200 and r.text.strip():
            return ET.fromstring(r.text)
        print(f"   arXiv returned {r.status_code}; retry in {15*(t+1)}s"); time.sleep(15*(t+1))
    raise RuntimeError("arXiv API not responding; finished parts are saved.")

print("arXiv:", arxiv_query)
start, kept, total = 0, 0, None
while True:
    root = arxiv_page(start)
    if total is None:
        total = int(root.find("os:totalResults", NS).text)
        print(f"   arXiv reports {total} matches in these categories (all years); filtering to >= {START}")
    entries = root.findall("a:entry", NS)
    if not entries: break
    stop = False
    for e in entries:
        pub = datetime.date.fromisoformat(e.find("a:published", NS).text[:10])
        if pub < START:                      # sorted newest-first, so we can stop here
            stop = True; break
        aid = e.find("a:id", NS).text.rsplit("/abs/",1)[-1]
        rows.append({
            "record_id":"", "bibkey":"",
            "title": re.sub(r"\s+"," ", e.find("a:title", NS).text or ""),
            "year": pub.year, "venue": "arXiv", "venue_type": "preprint",
            "source_database": "Preprints (arXiv)",
            "doi_or_arxiv": f"arXiv:{re.sub(r'v\\d+$','',aid)}",
            "query": arxiv_query, "url": f"https://arxiv.org/abs/{aid}",
            "authors": "; ".join(a.find("a:name", NS).text for a in e.findall("a:author", NS)),
            "abstract": re.sub(r"\s+"," ", e.find("a:summary", NS).text or ""),
        })
        kept += 1
    start += len(entries)
    print(f"   fetched {start}/{total}, kept {kept} (>= 2021)")
    save()
    if stop or start >= total: break
    time.sleep(3.5)                           # arXiv asks for >= 3 s between requests
hits.append({"database":"Preprints","query":f"arXiv API: {arxiv_query}","date":TODAY.isoformat(),"hits":kept})
print(f"arXiv done: {kept} records 2021+\n")

# ------------------------------------------------- bioRxiv / medRxiv via Europe PMC
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
def epmc(server):
    q = (f'(SRC:PPR) AND (PUBLISHER:"{server}") AND '
         f'(ABSTRACT:{FM_TERMS}) AND (ABSTRACT:{BRAIN_TERMS}) AND '
         f'(FIRST_PDATE:[{START.isoformat()} TO {TODAY.isoformat()}])')
    cursor, n, hitcount = "*", 0, None
    while True:
        r = requests.get(EPMC, params={"query": q, "format": "json", "pageSize": 1000,
                                       "cursorMark": cursor, "resultType": "core"}, timeout=120)
        r.raise_for_status(); j = r.json()
        if hitcount is None:
            hitcount = j.get("hitCount", 0); print(f"{server}: Europe PMC reports {hitcount} hits")
        for p in j.get("resultList", {}).get("result", []):
            doi = p.get("doi","")
            rows.append({
                "record_id":"", "bibkey":"",
                "title": p.get("title",""), "year": (p.get("firstPublicationDate") or "")[:4],
                "venue": server, "venue_type": "preprint",
                "source_database": f"Preprints ({server})",
                "doi_or_arxiv": doi or f"PPR:{p.get('id','')}",
                "query": q, "url": f"https://doi.org/{doi}" if doi else "",
                "authors": p.get("authorString",""),
                "abstract": re.sub(r"\s+"," ", p.get("abstractText","") or ""),
            })
            n += 1
        nxt = j.get("nextCursorMark")
        if not nxt or nxt == cursor or n >= hitcount: break
        cursor = nxt; save(); time.sleep(1)
    hits.append({"database":"Preprints","query":f"Europe PMC ({server}): {q}","date":TODAY.isoformat(),"hits":n})
    print(f"{server} done: {n} records\n")

for server in ("bioRxiv", "medRxiv"):
    epmc(server)

uniq = save()
print(f"TOTAL: {len(rows)} records, {len(uniq)} unique -> preprints_results.csv; hit counts -> preprints_hits.csv")
files.download("preprints_results.csv"); files.download("preprints_hits.csv")
