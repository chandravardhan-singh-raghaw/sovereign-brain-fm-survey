import csv, re
rows = list(csv.DictReader(open('out/candidates_for_fulltext.csv', encoding='utf-8')))

MOD = [('EEG', r"\beeg\b|electroencephal"), ('iEEG', r"\bieeg\b|\bseeg\b|\becog\b|intracranial|electrocorticogra"), ('MEG', r"\bmeg\b|magnetoencephal"),
       ('fMRI', r"\bfmri\b|functional (mri|magnetic)|bold signal|resting[- ]state"), ('sMRI', r"\bstructural mri|\bt1-?weighted|\bt2|flair|\bmri\b|magnetic resonance"),
       ('CT', r"\bct\b|computed tomography"), ('PET', r"\bpet\b|positron"), ('DTI', r"\bdti\b|diffusion (mri|tensor|weighted)"), ('text', r"radiology report|report generation|image[- ]text|vision[- ]language|language model")]
OBJ = [('masked', r"masked (auto|model|signal|image|patch|reconstruction|prediction)|\bmae\b|\bmasked\b"), ('contrastive', r"contrastive|\bclip\b|simclr|moco"),
       ('self-distillation', r"self-?distill|\bdino"), ('JEPA/latent-pred', r"\bjepa\b|joint[- ]embedding|latent prediction"), ('autoregressive', r"autoregressive|next[- ]token|\bgpt\b"),
       ('generative/diffusion', r"diffusion|generative pre"), ('supervised pretraining', r"supervised pre-?train"), ('multi-task', r"multi-?task")]
SCALE = re.compile(r"(\d[\d,\.]*\s?(k|m|million|thousand|billion)?\+?\s?(hours?|subjects?|participants?|patients?|scans?|volumes?|images?|recordings?|sessions?|studies|datasets?|samples?|electrode-hours?|TB|GB)\b)", re.I)
PROPOSE = re.compile(r"we (propose|present|introduce|develop|build|release|pre-?train|train)\b|\bour (model|framework|approach|method|foundation model)\b|in this (paper|work|study),? we", re.I)
PRETRAIN = re.compile(r"pre-?train|self-?supervised|foundation model|large[- ]scale (training|model)", re.I)
TRANSFER = re.compile(r"downstream|transfer|generali[sz]|multiple (tasks|datasets)|multi-?task|across (subjects|datasets|sites|tasks|modalities|cohorts)|cross-(subject|dataset|site|modal)|zero-?shot|few-?shot|fine-?tun|linear prob", re.I)
APPLIES = re.compile(r"segment anything|\bSAM\b|MedSAM|GPT-?4|ChatGPT|large language model|\bLLMs?\b|DINOv2|stable diffusion", re.I)
EVAL = re.compile(r"\b(benchmark(ing)?|comparative evaluation|comparison of|evaluat(e|ing) (existing|several|multiple|the generali[sz]ation)|do foundation models|are foundation models|how well do|revisiting|an empirical study|a study of)\b", re.I)
CODE = re.compile(r"github\.com/\S+|code (is|will be) (publicly )?available|publicly available at|open[- ]source", re.I)
NONHUMAN = re.compile(r"\b(mouse|mice|rodent|rat|monkey|macaque|zebrafish|drosophila|c\. elegans|animal)\b", re.I)

def ann(r):
    T, A = r['title'], r['abstract']; both = T + ' ' + A
    mods = [m for m, p in MOD if re.search(p, both, re.I)]
    objs = [o for o, p in OBJ if re.search(p, A, re.I)]
    scale = '; '.join(sorted({m[0] for m in SCALE.findall(A)})[:4])
    proposes, pretrain, transfer = bool(PROPOSE.search(A)), bool(PRETRAIN.search(both)), bool(TRANSFER.search(A))
    applies, evalp, code, nonhuman = bool(APPLIES.search(A)), bool(EVAL.search(T)), bool(CODE.search(A)), bool(NONHUMAN.search(T))
    if r['tier'] == 'SEED':
        return mods, objs, scale, code, 'include', 'seed model', 'high'
    if not A:
        return mods, objs, scale, code, 'look up abstract', 'title only', 'low'
    if evalp and not re.search(r"we (propose|introduce|present) (a |an |the )?(new |novel )?(foundation model|model)", A, re.I):
        return mods, objs, scale, code, 'exclude', 'evaluation/benchmark of existing FMs', 'medium'
    if applies and not re.search(r"pre-?trained on [^.]{0,80}\b(eeg|fmri|mri|ct|brain|neural|intracranial|hours|subjects|scans|recordings)", A, re.I):
        return mods, objs, scale, code, 'exclude', 'not pretrained on brain data (applies general FM)', 'medium'
    if nonhuman and not re.search(r"\bhuman\b", both, re.I):
        return mods, objs, scale, code, 'exclude', 'no brain downstream task (non-human only)', 'medium'
    if proposes and pretrain and transfer and mods:
        conf = 'high' if (re.search(r"foundation model", both, re.I) and scale) else 'medium'
        return mods, objs, scale, code, 'include', 'proposes pretrained brain model with transfer claims', conf
    if proposes and pretrain and mods:
        return mods, objs, scale, code, 'check', 'pretraining present but no explicit transfer/multi-task claim', 'low'
    return mods, objs, scale, code, 'exclude', 'no pretraining stage', 'medium'

out = []
for r in rows:
    mods, objs, scale, code, rec, why, conf = ann(r)
    r.update(modality_detected='; '.join(mods), objective_detected='; '.join(objs), data_scale_detected=scale,
             code_mentioned='yes' if code else '', recommendation=rec, recommendation_reason=why, confidence=conf)
    out.append(r)
order = {'include':0,'check':1,'look up abstract':2,'exclude':3}
out.sort(key=lambda r: (order[r['recommendation']], {'high':0,'medium':1,'low':2}[r['confidence']], -(int(r['year']) if r['year'].isdigit() else 0)))
cols = list(rows[0].keys()); 
for c in ['modality_detected','objective_detected','data_scale_detected','code_mentioned','recommendation','recommendation_reason','confidence']:
    if c not in cols: cols.insert(cols.index('stage_full_text'), c)
with open('/mnt/user-data/outputs/candidates_for_fulltext_v2_annotated.csv','w',newline='',encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(out)
import collections
print(collections.Counter(r['recommendation'] for r in out))
print(collections.Counter((r['recommendation'], r['confidence']) for r in out))
for r in [x for x in out if x['recommendation']=='include' and x['confidence']=='high'][:12]:
    print('  ', r['year'], '|', r['title'][:80], '|', r['modality_detected'], '|', r['data_scale_detected'][:40])
