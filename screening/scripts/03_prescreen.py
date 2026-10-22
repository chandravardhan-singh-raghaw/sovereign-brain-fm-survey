import json, re, csv
from rapidfuzz import fuzz, process
unique = json.load(open('unique.json'))

BRAIN = re.compile(r"\bbrain|neuroimag|neurolog|neurosci|neurodegen|neuropsych|neurodevelop|\beeg\b|\bmeg\b|\bfmri\b|\bieeg\b|\bseeg\b|\becog\b|intracranial|electroencephal|magnetoencephal|electrocorticogra|\bcortical|\bcortex|cerebr|connectom|brain[- ]computer|\bbci\b|neural (signal|record|activ|decod|data|dynamic|time series|population)|glioma|alzheimer|dementia|epilep|seizure|\bstroke\b|hippocamp|white[- ]matter|\bsleep stag|head ct|skull strip|\bmind\b", re.I)
STRONG_FM = re.compile(r"foundation(al)? model|\bgeneralist\b|universal (model|representation|eeg|brain|neural|encoder|decoder)|large[- ]?(brain|eeg|neural|neuro|physiolog)\w* model|\bLBM\b|brain (language|signal) model|pre-?trained (vision |visual )?(model|transformer|encoder|backbone)s? (for|on|across) (brain|eeg|fmri|mri|neuro|neural|medical)|scalable (eeg|brain|fmri|neural)|(eeg|brain|fmri|neural)[- ]?(gpt|bert|clip|mamba|jepa|dino|mae)\b", re.I)
WEAK_FM = re.compile(r"pre-?train|self-?supervised|masked (auto|model|signal|image|patch|reconstruction)|contrastive|representation learning|zero-?shot|few-?shot|downstream task|transfer(able)? (representation|learning)|generali[sz]able", re.I)
TRANSFER = re.compile(r"downstream|transfer|generali[sz]|multiple tasks|multi-?task|across (subjects|datasets|sites|tasks|modalities)|cross-(subject|dataset|site|modal)|zero-?shot|few-?shot|fine-?tun|linear prob", re.I)
REVIEW = re.compile(r"\b(review|survey|overview|perspective|roadmap|tutorial|commentary|editorial|position paper|challenges and opportunities|systematic)\b", re.I)
NON_MODEL = re.compile(r"\bbenchmark(ing)?\b|\bdataset\b|\bprotocol\b|\bcohort\b|\bprevalence\b|\bcase report\b|\bmeta-analysis\b|\bchallenge\b", re.I)

def classify(r):
    title, abst = r['title'], r['abstract']
    both = title + ' ' + abst
    try: y = int(r['year'])
    except: y = 0
    if y and y < 2021:
        return 'exclude', 'outside date window', 'C'
    if REVIEW.search(title) and not re.search(r"foundation model.*(we (propose|present|introduce)|\bour\b)", abst, re.I):
        return 'exclude', 'not a model paper (review/survey)', 'C-review'
    if not BRAIN.search(both):
        return 'exclude', 'not brain data', 'C'
    sfm_t, sfm_a = STRONG_FM.search(title), STRONG_FM.search(abst)
    wfm_t, wfm_a = WEAK_FM.search(title), WEAK_FM.search(abst)
    if sfm_t:
        if NON_MODEL.search(title) and not re.search(r"we (propose|present|introduce)", abst, re.I):
            return 'include', 'FM term in title; check if dataset/benchmark paper', 'B'
        return 'include', 'FM term in title + brain term', 'A'
    if sfm_a and BRAIN.search(both):
        if re.search(r"we (propose|present|introduce|develop)|\bour (model|framework|approach|method)\b", abst, re.I):
            return 'include', 'FM term in abstract, proposes model', 'B'
        return 'include', 'FM term in abstract only (may be an application of an FM)', 'B-weak'
    if wfm_t and BRAIN.search(both):
        if abst and TRANSFER.search(abst):
            return 'include', 'pretraining/SSL in title + transfer claims', 'B'
        if not abst:
            return 'include', 'pretraining/SSL in title, no abstract available', 'B-noabs'
        return 'exclude', 'no pretraining stage / task-specific SSL without transfer claims', 'C'
    return 'exclude', 'no pretraining stage (task-specific model)', 'C'

for r in unique:
    d, reason, tier = classify(r)
    r['stage_title_abstract'] = d
    r['auto_reason'] = reason
    r['tier'] = tier

# ---- match seed models from the manuscript
seeds = {row[0]: row[1] for row in csv.reader(open('/home/claude/mia/bibrows.csv')) if row[1]}
seed_keys = """kondepudi2026health guo2026brain mazher2026towards dong2026brain doner2026luna wang2025cbramod zhou2026csbrain wang2025lead ebrahimkhani2025brain dibble2026neurofm yue2024braingpt ortega2024brainlm cox2024brainsegfounder zhao2026brainblip ma2025brainclip guo2024neuroclip wu2026braindino jiang2024large yang2023biot wang2023brainbert zhang2023brant wang2024eegpt zhang2024brant tak2026brainiac liu2024brainid he2024fm karimi2024fmbim yuan2024brainwave shi2024fome dimofte2025cerebro luu2026brainfm kondepudi2026neurovfm kostas2021bendr chien2022maeeg cui2024neurogpt barbano2025antcl sihag2024veurovnn cai2023mbrain dong2024brain rui2025brainmvp sihag2023predicting""".split()
titles = [u['title'] for u in unique]
def nt(t): return re.sub(r'[^a-z0-9 ]','',t.lower())
found, missing = {}, []
for k in seed_keys:
    if k not in seeds: continue
    best = process.extractOne(nt(seeds[k]), [nt(t) for t in titles], scorer=fuzz.token_set_ratio)
    if best and best[1] >= 90:
        u = unique[best[2]]
        u['bibkey'] = k; u['seed'] = 'yes'
        u['stage_title_abstract'] = 'include'; u['tier'] = 'SEED'
        u['auto_reason'] = 'seed model from manuscript v0'
        found[k] = u['title']
    else:
        missing.append((k, seeds[k], best[1] if best else 0))

json.dump(unique, open('screened_auto.json','w'))
from collections import Counter
print(Counter(r['tier'] for r in unique))
print(Counter(r['stage_title_abstract'] for r in unique))
print(f'seeds matched {len(found)}/{len(seed_keys)}')
for m in missing: print('  MISSING:', m)
