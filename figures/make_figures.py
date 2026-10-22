#!/usr/bin/env python3
"""Regenerate the data figures from papers/models.csv."""
import csv, collections, os
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
models = list(csv.DictReader(open(f'{ROOT}/papers/models.csv', encoding='utf-8')))
plt.rcParams.update({'font.size': 8, 'font.family': 'serif', 'axes.spines.top': False, 'axes.spines.right': False})
fams = ['I Signal Transformer','II 3D Neuroimaging','III CNN/Transformer hybrid','IV Graph-based','V Multimodal','VI Specialized']
greys = ['#1f1f1f','#4d4d4d','#7a7a7a','#a6a6a6','#c9c9c9','#e3e3e3']
years = sorted({m['year'] for m in models}); by = collections.Counter((m['architectural_family'], m['year']) for m in models)
fig, ax = plt.subplots(figsize=(3.4, 2.3)); bottom = [0]*len(years)
for f_, c in zip(fams, greys):
    v = [by[(f_, y)] for y in years]; ax.bar(years, v, bottom=bottom, color=c, edgecolor='white', linewidth=0.4, label=f_.split(' ',1)[1]); bottom = [b+x for b, x in zip(bottom, v)]
ax.set_ylabel('Models'); ax.set_xlabel('Year'); ax.legend(fontsize=6, frameon=False, ncol=2); plt.tight_layout(); plt.savefig(f'{HERE}/fig_models_per_year_family.pdf'); plt.close()
modc, objc = collections.Counter(), collections.Counter(); venc = collections.Counter(m['venue_type'] for m in models)
for m in models:
    for x in m['modality'].split('; '): modc[x]+=1
    for x in m['pretraining_objective'].split('; '): objc[x]+=1
fig, axes = plt.subplots(1, 3, figsize=(7.0, 2.2))
for ax, cnt, t in zip(axes, [modc, objc, venc], ['Modality (multi-label)', 'Pretraining objective (multi-label)', 'Venue type']):
    it = cnt.most_common(9); ax.barh([k for k,_ in it][::-1], [v for _,v in it][::-1], color='#4d4d4d'); ax.set_title(t, fontsize=8)
plt.tight_layout(); plt.savefig(f'{HERE}/fig_modality_objective_venue.pdf'); plt.close(); print('figures written')
