import json, re, csv, collections
U = json.load(open('screened_auto.json'))

APPLIES = re.compile(r"segment anything|\bSAM\b|MedSAM|GPT-?4|ChatGPT|large language model|\bLLMs?\b|\bCLIP\b|DINOv2|stable diffusion|vision[- ]language model", re.I)
BUILDS = re.compile(r"we (pre-?train|train|propose|present|introduce|develop|build)\b[^.]{0,120}\b(foundation model|pre-?trained|pre-?training|large[- ]scale)|pre-?trained on [^.]{0,80}\b(eeg|fmri|mri|ct|brain|neural|intracranial|hours|subjects|participants|scans|recordings)", re.I)
for r in U:
    if r['tier'] in ('A', 'B', 'B-weak') and r['abstract']:
        if APPLIES.search(r['abstract']) and not BUILDS.search(r['abstract']) and not re.search(r"(eeg|brain|neuro|fmri|mri)[- ]?(gpt|clip|bert|mamba|jepa|dino|mae|llm)", r['title'], re.I):
            r['tier'] = 'B-app'
            r['auto_reason'] = 'applies an existing general FM (SAM/CLIP/LLM); check whether pretrained on brain data'
    if r['tier'] == 'B-noabs':
        if re.search(r"foundation|generalist|universal|large[- ]?(pre-?trained|scale)\b|massive|multi-?task|zero-?shot|few-?shot|across (subjects|datasets|tasks|sites|modalities)|cross-(subject|dataset|task|site|modal)|\bunified\b|general[- ]purpose", r['title'], re.I):
            r['tier'] = 'B-noabs'
            r['auto_reason'] = 'title only (no abstract in export): pretraining + generalisation/multi-task cue in title'
        else:
            r['tier'] = 'C-noabs'; r['stage_title_abstract'] = 'exclude'
            r['auto_reason'] = 'title only (no abstract in export): task-specific pretraining/transfer learning'

order = {'SEED':0,'A':1,'B':2,'B-app':3,'B-weak':4,'B-noabs':5,'C-review':6,'C-noabs':7,'C':8}
U.sort(key=lambda r: (order.get(r['tier'],9), -(int(r['year']) if r['year'].isdigit() else 0), r['title']))

cols = ['record_id','bibkey','seed','tier','title','year','venue','venue_type','source_database','all_sources','n_copies',
        'doi_or_arxiv','url','authors','stage_title_abstract','auto_reason','screen_pass_1','screen_pass_2','adjudicated',
        'stage_full_text','decision','exclusion_reason','notes','abstract']
def row(r):
    d = {c: r.get(c, '') for c in cols}
    d['screen_pass_1'] = 'auto:' + r['stage_title_abstract']
    return d

with open('out/screened.csv','w',newline='',encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
    for r in U: w.writerow(row(r))

inc = [r for r in U if r['stage_title_abstract']=='include']
with open('out/candidates_for_fulltext.csv','w',newline='',encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
    for r in inc: w.writerow(row(r))

# related surveys found (useful for Section 1.4)
surv = [r for r in U if r['tier']=='C-review' and re.search(r"foundation|pre-?train|self-?supervised|large[- ]scale|representation learning", r['title'], re.I)]
with open('out/related_surveys_found.csv','w',newline='',encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['record_id','title','year','venue','doi_or_arxiv','url','source_database']); w.writeheader()
    for r in surv: w.writerow({k: r.get(k,'') for k in w.fieldnames})

# search log (hits = records exported per database/source)
raw = json.load(open('merged.json'))
cnt = collections.Counter(r['source_database'] for r in raw)
name = {'Preprints (arXiv)':'Preprints','Preprints (bioRxiv)':'Preprints','Preprints (medRxiv)':'Preprints',
        'OpenReview (ICLR)':'OpenReview','OpenReview (NeurIPS)':'OpenReview','OpenReview (ICML)':'OpenReview'}
with open('out/search_log.csv','w',newline='') as f:
    w = csv.writer(f); w.writerow(['database','query','date','hits'])
    for src, n in sorted(cnt.items()):
        w.writerow([name.get(src, src), f'protocol query [{src}]', '2026-10-22', n])

# grey.csv skeleton from manuscript bib (misc/techreport = policy & web sources)
import bibtexparser
lib = bibtexparser.parse_file('/home/claude/mia/refs.bib')
with open('out/grey.csv','w',newline='',encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['source','type','organisation','url','archived_url','date_accessed','decision','bibkey'])
    for e in lib.entries:
        if e.entry_type in ('misc','techreport'):
            g = lambda k: (e.fields_dict[k].value if k in e.fields_dict else '')
            if 'arxiv' in g('howpublished').lower() or 'arxiv' in g('url').lower(): continue
            typ = 'guidance' if 'guid' in g('title').lower() else 'rules' if 'rules' in g('title').lower() else 'statute' if 'act' in g('title').lower().split() else 'web page'
            w.writerow([g('title'), typ, g('author') or g('institution'), g('url'), '', re.sub(r'.*ccessed:?\s*','',g('note')) if 'ccessed' in g('note') else '', 'include', e.key])

tiers = collections.Counter(r['tier'] for r in U)
n_id, n_u = len(raw), len(U)
n_exTA = sum(1 for r in U if r['stage_title_abstract']=='exclude')
n_ft = len(inc)
with open('out/survey_numbers_v1.tex','w') as f:
    f.write(f"""%% survey_numbers_v1.tex -- PROVISIONAL (title/abstract stage complete; full-text pending)
%% Generated 2026-10-22 from the six database exports. \\input in the PREAMBLE.
\\newcommand{{\\Nidentified}}{{{n_id:,}}}
\\newcommand{{\\Nduplicates}}{{{n_id-n_u:,}}}
\\newcommand{{\\Nscreened}}{{{n_u:,}}}
\\newcommand{{\\Nexcludedta}}{{{n_exTA:,}}}
\\newcommand{{\\Nfulltext}}{{{n_ft:,}}}
\\newcommand{{\\Nexcludedft}}{{---}}   % after full-text screening
\\newcommand{{\\Nmodels}}{{---}}       % after full-text screening
\\newcommand{{\\Ngreyidentified}}{{---}}
\\newcommand{{\\Ngrey}}{{---}}
\\newcommand{{\\FinalSearchDate}}{{22 October 2026}}
\\newcommand{{\\AsOfDate}}{{October 2026}}
\\newcommand{{\\RepoURL}}{{\\url{{https://github.com/---}}}}
\\newcommand{{\\RepoDOI}}{{---}}
\\newcommand{{\\HitsPubMed}}{{{cnt['PubMed']:,}}}
\\newcommand{{\\HitsIEEE}}{{{cnt['IEEE Xplore']:,}}}
\\newcommand{{\\HitsScopus}}{{{cnt['Scopus']:,}}}
\\newcommand{{\\HitsACM}}{{{cnt['ACM Digital Library']:,}}}
\\newcommand{{\\HitsOpenReview}}{{{cnt['OpenReview (ICLR)']+cnt['OpenReview (NeurIPS)']+cnt['OpenReview (ICML)']:,}}}
\\newcommand{{\\HitsArxiv}}{{{cnt['Preprints (arXiv)']+cnt['Preprints (bioRxiv)']+cnt['Preprints (medRxiv)']:,}}}
""")
print('tiers:', dict(tiers))
print(f'identified {n_id} | unique {n_u} | excluded T/A {n_exTA} | to full text {n_ft}')
print('related surveys found:', len(surv))
