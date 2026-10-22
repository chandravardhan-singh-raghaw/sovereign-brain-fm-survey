#!/usr/bin/env python3
"""Regenerate latex/tab_catalogue.tex and latex/tab_summary.tex from papers/models.csv."""
import csv, collections, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
models = list(csv.DictReader(open(f'{ROOT}/papers/models.csv', encoding='utf-8')))
def tex(s): return s.replace('&','\\&').replace('%','\\%').replace('_','\\_').replace('#','\\#').replace('$','\\$').replace('^','\\^{}')
fam = {'I Signal Transformer':'I','II 3D Neuroimaging':'II','III CNN/Transformer hybrid':'III','IV Graph-based':'IV','V Multimodal':'V','VI Specialized':'VI'}
models.sort(key=lambda m: (m['architectural_family'], -int(m['year']) if m['year'].isdigit() else 0, m['model_name'].lower()))
head = r"""\begingroup\scriptsize\setlength{\tabcolsep}{3pt}\renewcommand{\arraystretch}{1.05}
\begin{longtable}{@{}P{2.9cm} c P{2.0cm} P{2.2cm} P{3.4cm} P{3.0cm} c c@{}}
\caption{Complete catalogue of the \Nmodels{} brain foundation models included in this survey. Family: I signal transformers, II 3D neuroimaging, III CNN/Transformer hybrids, IV graph-based, V multimodal, VI specialized. NR = not reported in the abstract.}\label{tab:catalogue}\\
\toprule \textbf{Model} & \textbf{Year} & \textbf{Venue} & \textbf{Modality} & \textbf{Pretraining objective} & \textbf{Data scale (as reported)} & \textbf{Fam.} & \textbf{Code} \\ \midrule \endfirsthead
\toprule \textbf{Model} & \textbf{Year} & \textbf{Venue} & \textbf{Modality} & \textbf{Pretraining objective} & \textbf{Data scale (as reported)} & \textbf{Fam.} & \textbf{Code} \\ \midrule \endhead
\midrule \multicolumn{8}{r}{\emph{continued}}\\ \endfoot \bottomrule \endlastfoot"""
rows = [head]
for m in models:
    code = r'\checkmark' if m['code_available']=='yes' else 'NR'
    nm = m['model_name'] or (m['title'][:48] + ('…' if len(m['title'])>48 else ''))
    rows.append(f"{tex(nm)} & {m['year']} & {tex(m['venue'])} & {tex(m['modality'])} & {tex(m['pretraining_objective'])} & {tex(m['data_scale'][:60])} & {fam.get(m['architectural_family'],'')} & {code} \\\\")
rows.append(r"\end{longtable}\endgroup")
open(f'{HERE}/tab_catalogue.tex','w',encoding='utf-8').write('\n'.join(rows))
by = collections.Counter((m['architectural_family'], m['year']) for m in models); years = sorted({m['year'] for m in models})
fams = list(fam.keys())
L = [r"\begin{table}[!t]\centering\footnotesize\caption{Included brain foundation models by architectural family and year.}\label{tab:family_year}\setlength{\tabcolsep}{4pt}",
     r"\begin{tabular}{@{}l" + 'r'*len(years) + r"r@{}}\toprule \textbf{Family} & " + ' & '.join(f"\\textbf{{{y}}}" for y in years) + r" & \textbf{Total} \\ \midrule"]
for f_ in fams:
    c = [by[(f_, y)] for y in years]; L.append(f"{f_} & " + ' & '.join(map(str, c)) + f" & {sum(c)} \\\\")
L.append(r"\midrule Total & " + ' & '.join(str(sum(by[(f_, y)] for f_ in fams)) for y in years) + f" & {len(models)} \\\\ \\bottomrule\\end{{tabular}}\\end{{table}}")
open(f'{HERE}/tab_summary.tex','w').write('\n'.join(L))
print(f'wrote tab_catalogue.tex and tab_summary.tex for {len(models)} models')
