import csv, re, json
import bibtexparser
U = '/mnt/user-data/uploads/'
recs = []

def add(src, title, year, venue, doi, url, authors, abstract, vtype=''):
    recs.append(dict(source_database=src, title=(title or '').strip(), year=str(year or '').strip()[:4],
                     venue=(venue or '').strip(), doi_or_arxiv=(doi or '').strip(), url=url or '',
                     authors=(authors or '').strip(), abstract=re.sub(r'\s+', ' ', abstract or '').strip(),
                     venue_type=vtype))

# 1 PubMed (title only)
for r in csv.DictReader(open(U+'1_pubmed.csv', encoding='utf-8-sig')):
    add('PubMed', r['Title'], r['Publication Year'], r['Journal/Book'], r['DOI'],
        f"https://pubmed.ncbi.nlm.nih.gov/{r['PMID']}/", r['Authors'], '', 'journal')
# 2 IEEE
for r in csv.DictReader(open(U+'2_ieee.csv', encoding='utf-8-sig')):
    add('IEEE Xplore', r['Document Title'], r['Publication Year'], r['Publication Title'], r['DOI'],
        r.get('PDF Link',''), r['Authors'], r.get('Abstract',''),
        'conference' if 'Conference' in r['Publication Title'] or 'Symposium' in r['Publication Title'] or 'Workshop' in r['Publication Title'] else 'journal')
# 3 Scopus (title only)
for r in csv.DictReader(open(U+'3_scopus.csv', encoding='utf-8-sig')):
    add('Scopus', r['Title'], r['Year'], r['Source title'], r['DOI'], r['Link'], r['Authors'], '',
        'conference' if r['Document Type'].startswith('Conference') else 'journal')
# 4 ACM bib
lib = bibtexparser.parse_file(U+'4_acm.bib')
for e in lib.entries:
    g = lambda k: (e.fields_dict[k].value if k in e.fields_dict else '')
    add('ACM Digital Library', g('title'), g('year'), g('journal') or g('booktitle'),
        g('doi'), g('url'), g('author').replace(' and ', '; '), g('abstract'),
        'conference' if e.entry_type=='inproceedings' else 'journal')
# 5 OpenReview, 6 preprints (already in our format)
for f, src in (('5_openreview.csv','OpenReview'), ('6_preprints.csv','Preprints')):
    for r in csv.DictReader(open(U+f, encoding='utf-8')):
        add(r['source_database'], r['title'], r['year'], r['venue'], r['doi_or_arxiv'], r['url'], r['authors'], r['abstract'], r['venue_type'])

for i, r in enumerate(recs, 1):
    r['raw_id'] = f'R{i:05d}'
json.dump(recs, open('merged.json','w'))
from collections import Counter
print(len(recs), Counter(r['source_database'] for r in recs))
print('with abstract:', sum(1 for r in recs if r['abstract']))
