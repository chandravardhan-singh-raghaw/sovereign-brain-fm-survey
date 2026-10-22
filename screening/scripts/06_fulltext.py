import csv, re, collections
rows = list(csv.DictReader(open('/mnt/user-data/outputs/candidates_for_fulltext_v2_annotated.csv', encoding='utf-8')))

FM_TITLE = re.compile(r"foundation(al)? model|\bgeneralist\b|universal (model|representation|eeg|brain|neural|encoder)|large[- ]?(brain|eeg|neural|neuro|physiolog)\w* model|general[- ]purpose|brain (language|signal) model|(eeg|brain|fmri|neuro|neural)[- ]?(gpt|bert|clip|mamba|jepa|dino|mae|lm)\b", re.I)
FM_ABS   = re.compile(r"foundation model", re.I)
PROPOSE  = re.compile(r"we (propose|present|introduce|develop|build|release|pre-?train|train)\b|\bour (model|framework|approach|method|foundation model)\b|in this (paper|work|study),? we|this (paper|work) (proposes|presents|introduces)", re.I)
PRETRAIN = re.compile(r"pre-?train|self-?supervised|foundation model", re.I)
MULTI    = re.compile(r"(\b(\d+|two|three|four|five|six|seven|eight|nine|ten|several|multiple|diverse|various|a range of|a variety of|wide range)\b[^.]{0,40}\b(downstream )?(tasks|datasets|benchmarks|cohorts|applications))|multi-?task|across (subjects|datasets|sites|tasks|modalities|cohorts|institutions)|zero-?shot|few-?shot|generali[sz]|transfer", re.I)
BRAINMOD = re.compile(r"\beeg\b|electroencephal|\bieeg\b|\bseeg\b|\becog\b|intracranial|\bmeg\b|magnetoencephal|\bfmri\b|\bmri\b|magnetic resonance|neuroimag|\bct\b|computed tomography|\bpet\b|brain (signal|recording|activity|imag|network|scan)|connectom|neural (signal|record|activ|time series|population)", re.I)
APPLIES  = re.compile(r"segment anything|\bSAM\b|MedSAM|GPT-?4|ChatGPT|large language models?|\bLLMs?\b|DINOv2|stable diffusion|CLIP", re.I)
PRETRAIN_ON_BRAIN = re.compile(r"pre-?train(ed|ing)? (on|using|with|from) [^.]{0,100}\b(eeg|fmri|mri|ct|brain|neural|intracranial|hours|subjects|participants|scans|recordings|volumes|images)", re.I)
EVAL     = re.compile(r"\b(benchmark(ing)?|comparative evaluation|comparison of|evaluat(e|ing|ion of) (existing|several|multiple|the generali[sz]ation|foundation)|do foundation models|are foundation models|how well do|revisiting|an empirical study|a study of|can foundation models|probing|what do)\b", re.I)
NONHUMAN = re.compile(r"\b(mouse|mice|rodent|rats?|monkeys?|macaques?|zebrafish|drosophila|c\. elegans|animal|non-?human primate)\b", re.I)
HUMAN    = re.compile(r"\bhuman|patients?|participants?|subjects?|clinical|hospital|cohort", re.I)
NEUROMORPHIC = re.compile(r"neuromorphic|spiking neural|event camera|brain-inspired|brain-like", re.I)
OUT_OF_SCOPE_TASK = re.compile(r"\b(speech|image) (synthesis|generation) from (fmri|eeg|brain)|visual stimul(us|i) (reconstruction|decoding)|reconstruct(ing|ion of)? (visual|images?|video|speech) from", re.I)

def decide(r):
    T, A = r['title'], r['abstract']; both = T + ' ' + A
    if r['tier'] == 'SEED':
        return 'include', '', 'seed'
    if NEUROMORPHIC.search(T) and not BRAINMOD.search(A):
        return 'exclude', 'not brain data', 'neuromorphic/brain-inspired computing'
    if not A:
        if FM_TITLE.search(T) and BRAINMOD.search(T):
            return 'include', '', 'title-only: explicit brain foundation model in title; verify full text'
        return 'exclude', 'insufficient technical detail', 'title-only record without explicit FM claim'
    if EVAL.search(T) and not re.search(r"we (propose|introduce|present) (a |an |the )?(new |novel )?(\w+ )?(foundation model|pre-?trained model)", A, re.I):
        return 'exclude', 'evaluation/benchmark of existing FMs', ''
    if NONHUMAN.search(T) and not HUMAN.search(both):
        return 'exclude', 'no brain downstream task', 'non-human data only'
    if APPLIES.search(A) and not PRETRAIN_ON_BRAIN.search(A) and not FM_TITLE.search(T):
        return 'exclude', 'not pretrained on brain data', 'applies general-domain FM'
    if not BRAINMOD.search(both):
        return 'exclude', 'no brain downstream task', ''
    if not PROPOSE.search(A):
        return 'exclude', 'insufficient technical detail', 'no model proposed in abstract'
    if not PRETRAIN.search(both):
        return 'exclude', 'no pretraining stage', ''
    fm_claim = bool(FM_TITLE.search(T) or FM_ABS.search(A))
    multi = bool(MULTI.search(A))
    if fm_claim and (multi or r['data_scale_detected']):
        return 'include', '', 'explicit FM claim + multi-task/scale'
    if fm_claim:
        return 'include', '', 'explicit FM claim; verify multi-task evaluation'
    if multi and r['data_scale_detected'] and re.search(r"pre-?train", A, re.I):
        return 'include', '', 'large-scale pretraining + multi-task transfer, no FM label'
    return 'exclude', 'no pretraining stage', 'task-specific self-supervised model (single task)'

for r in rows:
    d, reason, note = decide(r)
    r['stage_full_text'] = d; r['decision'] = d; r['exclusion_reason'] = reason
    r['notes'] = ('abstract-level screening: ' + note).strip(': ')
    r['screen_pass_2'] = 'assisted:' + d
print(collections.Counter(r['decision'] for r in rows))
print(collections.Counter(r['exclusion_reason'] for r in rows if r['decision']=='exclude'))
csv.DictWriter(open('ft_decisions.csv','w',newline='',encoding='utf-8'), fieldnames=rows[0].keys()).writeheader()
w = csv.DictWriter(open('ft_decisions.csv','w',newline='',encoding='utf-8'), fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
inc = [r for r in rows if r['decision']=='include']
with open('include_titles.txt','w') as f:
    for r in sorted(inc, key=lambda x: (x['modality_detected'], x['year'])):
        f.write(f"{r['record_id']} | {r['year']} | {r['modality_detected'][:18]:18s} | {r['title'][:110]}\n")
print('include list written:', len(inc))
