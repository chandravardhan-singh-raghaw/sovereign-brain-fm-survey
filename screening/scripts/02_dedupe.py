import json, re
from collections import defaultdict
recs = json.load(open('merged.json'))

def norm_title(t):
    t = t.lower()
    t = re.sub(r'<[^>]+>', '', t)
    t = re.sub(r'[^a-z0-9]', '', t)
    return t

def norm_id(d):
    d = d.lower().strip()
    d = re.sub(r'^(https?://(dx\.)?doi\.org/|doi:\s*)', '', d)
    d = re.sub(r'^arxiv:', 'arxiv:', d)
    d = re.sub(r'v\d+$', '', d)            # arXiv versions
    if re.fullmatch(r'10\.\d{4,9}/arxiv\.(\d{4}\.\d{4,5})', d):   # DataCite arXiv DOIs
        d = 'arxiv:' + re.sub(r'10\.\d{4,9}/arxiv\.', '', d)
    return d

# union-find
parent = {}
def find(x):
    while parent.setdefault(x, x) != x:
        parent[x] = parent[parent[x]]; x = parent[x]
    return x
def union(a, b): parent[find(a)] = find(b)

by_id, by_title = {}, {}
for r in recs:
    rid = r['raw_id']; find(rid)
    nid = norm_id(r['doi_or_arxiv'])
    if nid and not nid.startswith('ppr:'):
        if nid in by_id: union(rid, by_id[nid])
        else: by_id[nid] = rid
    nt = norm_title(r['title'])
    if len(nt) >= 25:                      # skip very short titles for title-matching
        if nt in by_title: union(rid, by_title[nt])
        else: by_title[nt] = rid

groups = defaultdict(list)
for r in recs: groups[find(r['raw_id'])].append(r)

def score(r):   # prefer the richest record as representative
    return (bool(r['abstract']), bool(r['doi_or_arxiv']), len(r['venue']), r['source_database'] != 'Scopus')

unique = []
for i, (k, grp) in enumerate(sorted(groups.items(), key=lambda kv: kv[0]), 1):
    rep = dict(max(grp, key=score))
    rep['record_id'] = f'U{i:05d}'
    rep['all_sources'] = '; '.join(sorted({g['source_database'] for g in grp}))
    rep['n_copies'] = len(grp)
    if not rep['abstract']:
        for g in grp:
            if g['abstract']: rep['abstract'] = g['abstract']; break
    if not rep['doi_or_arxiv']:
        for g in grp:
            if g['doi_or_arxiv']: rep['doi_or_arxiv'] = g['doi_or_arxiv']; break
    unique.append(rep)

json.dump(unique, open('unique.json','w'))
print('identified', len(recs), '| unique', len(unique), '| duplicates removed', len(recs)-len(unique))
print('unique with abstract', sum(1 for u in unique if u['abstract']))
