import csv, re, collections, json
rows = list(csv.DictReader(open('ft_final.csv', encoding='utf-8')))
inc = [r for r in rows if r['decision']=='include']
seedmeta = {r[0]: r for r in csv.reader(open('/home/claude/mia/bibrows.csv'))}

def model_name(t):
    m = re.match(r"^\s*([A-Za-z0-9\-\$\^\{\}\[\]\+²\.\s]{2,40}?)\s*[:：]\s", t)
    if m and len(m.group(1).split()) <= 4: return m.group(1).strip()
    m = re.search(r"\b([A-Z][A-Za-z0-9\-]*(?:[A-Z][a-z]|[A-Z]{2,}|GPT|BERT|CLIP|JEPA|DINO|MAE|Mamba|FM|LM)[A-Za-z0-9\-]*)\b", t)
    if m and m.group(1).lower() not in ('eeg','meg','mri','fmri','mri','ct','pet','dti','bci','a','an'): return m.group(1)
    return (t[:45] + ('…' if len(t) > 45 else ''))

SEED_FAM = {k:'I Signal Transformer' for k in 'wang2023brainbert zhang2023brant yang2023biot wang2024eegpt jiang2024large zhang2024brant yuan2024brainwave shi2024fome wang2025cbramod dimofte2025cerebro zhou2026csbrain ortega2024brainlm doner2026luna yue2024braingpt cui2024neurogpt'.split()}
SEED_FAM.update({k:'II 3D Neuroimaging' for k in 'cox2024brainsegfounder wu2026braindino liu2024brainid he2024fm karimi2024fmbim dibble2026neurofm luu2026brainfm kondepudi2026health kondepudi2026neurovfm tak2026brainiac rui2025brainmvp mazher2026towards'.split()})
SEED_FAM.update({k:'III CNN/Transformer hybrid' for k in 'kostas2021bendr chien2022maeeg barbano2025antcl'.split()})
SEED_FAM.update({k:'IV Graph-based' for k in 'sihag2024veurovnn sihag2023predicting cai2023mbrain'.split()})
SEED_FAM.update({k:'V Multimodal' for k in 'ma2025brainclip zhao2026brainblip dong2026brain'.split()})
SEED_FAM.update({k:'VI Specialized' for k in 'guo2026brain dong2024brain'.split()})
def family(r):
    if r['bibkey'] in SEED_FAM: return SEED_FAM[r['bibkey']]
    T, A, M = r['title'], r['abstract'], r['modality_detected']
    both = (T + ' ' + A).lower()
    if re.search(r"graph (neural|network|transformer|foundation)|connectom|brain network|gnn\b", both) and not re.search(r"\beeg\b", T.lower()): return 'IV Graph-based'
    if re.search(r"vision[- ]language|language|text|report|llm|clip|blip|multimodal|multi-modal|cross-modal|eeg.fnirs|eeg.meg|fmri.*(eeg|meg)|(eeg|meg).*fmri", T.lower()): return 'V Multimodal'
    if re.search(r"jepa|mixture[- ]of[- ]experts|\bmoe\b|flow matching|world model|diffusion|generative|mamba|state[- ]space", T.lower()): return 'VI Specialized'
    if re.search(r"cnn|convolution|u-?net|hybrid", T.lower()): return 'III CNN/Transformer hybrid'
    if re.search(r"\bmri\b|\bct\b|neuroimag|brain imag|volumetric|3d|structural|diffusion mri|dmri|pet|tractogram|lesion|tumor|tumour", T.lower()) or ('sMRI' in M or 'CT' in M or 'DTI' in M or 'PET' in M) and 'EEG' not in M: return 'II 3D Neuroimaging'
    return 'I Signal Transformer'

def venue_short(v):
    v = re.sub(r"\s+", " ", v)
    for pat, rep in [(r"Submitted to|Conference Submission|Rejected|Withdrawn", "under review"), (r"International Conference on Learning Representations|ICLR", "ICLR"), (r"Neural Information Processing Systems|NeurIPS", "NeurIPS"),
                     (r"International Conference on Machine Learning|ICML", "ICML"), (r"Medical Image Analysis", "MedIA"), (r"IEEE Transactions on Medical Imaging|TMI", "IEEE TMI"),
                     (r"Nature Medicine", "Nat. Med."), (r"Nature Neuroscience", "Nat. Neurosci."), (r"Nature Communications", "Nat. Commun."), (r"MICCAI|Medical Image Computing", "MICCAI"),
                     (r"KDD", "KDD"), (r"ICASSP", "ICASSP"), (r"AAAI", "AAAI"), (r"Submitted to|Conference Submission|Rejected|Withdrawn", "under review"), (r"arXiv", "arXiv"), (r"bioRxiv", "bioRxiv"), (r"medRxiv", "medRxiv")]:
        if re.search(pat, v, re.I): return rep
    return v[:28]

models = []
for r in inc:
    seed = seedmeta.get(r['bibkey'])
    models.append({
        'model_id': r['record_id'], 'bibkey': r['bibkey'], 'model_name': model_name(r['title']), 'title': r['title'],
        'year': r['year'], 'venue': venue_short(r['venue']), 'venue_full': r['venue'], 'venue_type': r['venue_type'],
        'architectural_family': family(r), 'modality': r['modality_detected'].replace('text','text/reports') or 'NR',
        'pretraining_objective': r['objective_detected'] or 'NR', 'data_scale': r['data_scale_detected'] or 'NR',
        'dataset_origin': 'NR', 'developer_country': 'NR', 'south_asian_data_in_corpus': 'NR', 'evaluated_on_indian_cohort': 'No',
        'code_available': 'yes' if r['code_mentioned'] else 'NR', 'doi_or_arxiv': r['doi_or_arxiv'], 'url': r['url'],
        'authors': r['authors'][:200], 'source_database': r['all_sources'] or r['source_database'],
        'curated': 'yes (manuscript v0)' if r['tier']=='SEED' else 'auto-extracted; verify', 'abstract': r['abstract'],
    })
models.sort(key=lambda m: (m['architectural_family'], -int(m['year']) if m['year'].isdigit() else 0, m['model_name'].lower()))
with open('out/models_v1.csv','w',newline='',encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=models[0].keys()); w.writeheader(); w.writerows(models)

# ---------------------- LaTeX: full catalogue as appendix longtable
def tex(s): return s.replace('&','\\&').replace('%','\\%').replace('_','\\_').replace('#','\\#').replace('$','\\$').replace('^','\\^{}')
fam_label = {'I Signal Transformer':'I','II 3D Neuroimaging':'II','III CNN/Transformer hybrid':'III','IV Graph-based':'IV','V Multimodal':'V','VI Specialized':'VI'}
lines = [r"""%% tab_catalogue_v1.tex -- GENERATED from models_v1.csv (screening_08_tables_v1.py). Do not edit by hand.
%% Appendix table: complete catalogue of included brain foundation models.
%% Requires: longtable, booktabs, array, ragged2e (P column type). Place inside \onecolumn ... \twocolumn or in a one-column appendix.
\begingroup
\scriptsize
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.05}
\begin{longtable}{@{}P{2.9cm} c P{2.0cm} P{2.2cm} P{3.4cm} P{3.0cm} c c@{}}
\caption{Complete catalogue of the \Nmodels{} brain foundation models included in this survey (\cref{sec:method}). Family: I signal transformers, II 3D neuroimaging, III CNN/Transformer hybrids, IV graph-based, V multimodal, VI specialized. Fields are extracted from the primary paper's abstract where available; NR = not reported in the abstract. The repository holds the full record.}\label{tab:catalogue}\\
\toprule
\textbf{Model} & \textbf{Year} & \textbf{Venue} & \textbf{Modality} & \textbf{Pretraining objective} & \textbf{Data scale (as reported)} & \textbf{Fam.} & \textbf{Code} \\
\midrule
\endfirsthead
\toprule
\textbf{Model} & \textbf{Year} & \textbf{Venue} & \textbf{Modality} & \textbf{Pretraining objective} & \textbf{Data scale (as reported)} & \textbf{Fam.} & \textbf{Code} \\
\midrule
\endhead
\midrule \multicolumn{8}{r}{\emph{continued}}\\
\endfoot
\bottomrule
\endlastfoot"""]
for m in models:
    cite = f"~\\citep{{{m['bibkey']}}}" if m['bibkey'] else ''
    code = r'\checkmark' if m['code_available']=='yes' else 'NR'
    lines.append(f"{tex(m['model_name'])}{cite} & {m['year']} & {tex(m['venue'])} & {tex(m['modality'])} & {tex(m['pretraining_objective'])} & {tex(m['data_scale'][:60])} & {fam_label[m['architectural_family']]} & {code} \\\\")
lines.append(r"\end{longtable}" + "\n" + r"\endgroup")
open('out/tab_catalogue_v1.tex','w',encoding='utf-8').write('\n'.join(lines))

# ---------------------- LaTeX: summary table (counts) for the main text
by = collections.Counter((m['architectural_family'], m['year']) for m in models)
years = sorted({m['year'] for m in models})
fams = ['I Signal Transformer','II 3D Neuroimaging','III CNN/Transformer hybrid','IV Graph-based','V Multimodal','VI Specialized']
L = [r"""%% tab_summary_v1.tex -- GENERATED. Models per architectural family and year.
\begin{table}[!t]
\centering\footnotesize
\caption{Included brain foundation models by architectural family and year of first appearance (\Nmodels{} models; 2027 denotes journal issues dated ahead of print).}
\label{tab:family_year}
\setlength{\tabcolsep}{4pt}
\begin{tabular}{@{}l""" + 'r'*len(years) + r"""r@{}}
\toprule
\textbf{Family} & """ + ' & '.join(f"\\textbf{{{y}}}" for y in years) + r""" & \textbf{Total} \\
\midrule"""]
for f_ in fams:
    cnt = [by[(f_, y)] for y in years]
    L.append(f"{f_} & " + ' & '.join(str(c) for c in cnt) + f" & {sum(cnt)} \\\\")
L.append(r"\midrule")
L.append("Total & " + ' & '.join(str(sum(by[(f_, y)] for f_ in fams)) for y in years) + f" & {len(models)} \\\\")
L.append(r"\bottomrule" + "\n" + r"\end{tabular}" + "\n" + r"\end{table}")
open('out/tab_summary_v1.tex','w').write('\n'.join(L))

# ---------------------- figures
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 8, 'font.family': 'serif', 'axes.spines.top': False, 'axes.spines.right': False})
greys = ['#1f1f1f','#4d4d4d','#7a7a7a','#a6a6a6','#c9c9c9','#e3e3e3']
# F6: models per year by family (stacked)
fig, ax = plt.subplots(figsize=(3.4, 2.3))
bottom = [0]*len(years)
for f_, c in zip(fams, greys):
    vals = [by[(f_, y)] for y in years]
    ax.bar(years, vals, bottom=bottom, color=c, edgecolor='white', linewidth=0.4, label=f_.split(' ',1)[1])
    bottom = [b+v for b, v in zip(bottom, vals)]
ax.set_ylabel('Models'); ax.set_xlabel('Year'); ax.legend(fontsize=6, frameon=False, ncol=2)
plt.tight_layout(); plt.savefig('out/fig_models_per_year_family_v1.pdf'); plt.close()
# F8: modality and objective
modc = collections.Counter(); objc = collections.Counter(); venc = collections.Counter(m['venue_type'] for m in models)
for m in models:
    for x in m['modality'].split('; '): modc[x]+=1
    for x in m['pretraining_objective'].split('; '): objc[x]+=1
fig, axes = plt.subplots(1, 3, figsize=(7.0, 2.2))
for ax, cnt, title in zip(axes, [modc, objc, venc], ['Modality (multi-label)', 'Pretraining objective (multi-label)', 'Venue type']):
    items = cnt.most_common(9)
    ax.barh([k for k,_ in items][::-1], [v for _,v in items][::-1], color='#4d4d4d')
    ax.set_title(title, fontsize=8)
plt.tight_layout(); plt.savefig('out/fig_modality_objective_venue_v1.pdf'); plt.close()

# ---------------------- final screened_v2 (all 10,377 with decisions) and survey numbers
allrows = list(csv.DictReader(open('/mnt/user-data/outputs/screened_v1.csv', encoding='utf-8')))
dec = {r['record_id']: r for r in rows}
for r in allrows:
    if r['record_id'] in dec:
        d = dec[r['record_id']]
        for k in ('stage_full_text','decision','exclusion_reason','notes','screen_pass_2'):
            r[k] = d.get(k,'')
    else:
        r['decision'] = 'exclude'; r['exclusion_reason'] = r['exclusion_reason'] or r['auto_reason']
cols = list(allrows[0].keys())
with open('out/screened_v2.csv','w',newline='',encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(allrows)

n_models = len(models); n_ft = len(rows); n_exft = n_ft - n_models
ftreasons = collections.Counter(r['exclusion_reason'] for r in rows if r['decision']=='exclude')
grey = list(csv.DictReader(open('out/grey_v2.csv', encoding='utf-8')))
ng_id = len(grey); ng_inc = sum(1 for g in grey if g['decision']=='include')
s = open('out/survey_numbers_v1.tex').read()
s = s.replace('PROVISIONAL (title/abstract stage complete; full-text pending)', 'FINAL (assisted screening complete 2026-10-22)')
s = re.sub(r"\\newcommand\{\\Nexcludedft\}\{---\}.*", f"\\\\newcommand{{\\\\Nexcludedft}}{{{n_exft:,}}}", s)
s = re.sub(r"\\newcommand\{\\Nmodels\}\{---\}.*", f"\\\\newcommand{{\\\\Nmodels}}{{{n_models}}}", s)
s = s.replace(r"\newcommand{\Ngreyidentified}{---}", f"\\newcommand{{\\Ngreyidentified}}{{{ng_id}}}")
s = s.replace(r"\newcommand{\Ngrey}{---}", f"\\newcommand{{\\Ngrey}}{{{ng_inc}}}")
open('out/survey_numbers_v2.tex','w').write(s)
print(f"models {n_models} | full text {n_ft} | excluded FT {n_exft} | grey {ng_inc}/{ng_id}")
print('FT exclusion reasons:', dict(ftreasons))
print('families:', collections.Counter(m['architectural_family'] for m in models))
json.dump(dict(ftreasons), open('out/ft_reasons.json','w'))
