import csv, re, collections
from rapidfuzz import fuzz
rows = list(csv.DictReader(open('ft_decisions.csv', encoding='utf-8')))
R = {r['record_id']: r for r in rows}

ADAPT = 'adaptation/fine-tuning method for existing FMs'
EVAL  = 'evaluation/benchmark of existing FMs'
APPL  = 'not pretrained on brain data (applies general FM)'
NOBR  = 'no brain downstream task'
NOPT  = 'no pretraining stage'
NOTB  = 'not brain data'
REV   = 'not a model paper (review/position/dataset)'
TASK  = 'task-specific model (single task, no transfer evaluation)'
DETAIL= 'insufficient technical detail'

X = {
# --- not brain imaging/neural-signal data in scope (genetics, spikes, animals, neuromorphic, microscopy, other organs)
 NOTB: "U03681 U09254 U10240 U08693 U10368 U00048 U00324 U00659 U10357 U08831 U02800 U10299 U08849 U08842 U01023 U08829 U08844 U10252 U09424 U08724 U08707 U08999 U08629 U00333 U09835 U08641 U05042 U02127 U09578 U04354 U04059 U09490 U09172 U08801 U08693 U09162 U09276 U06126 U08626 U01290 U09854 U10332 U09382 U09087 U08663 U05128 U08803 U08800 U03936 U10362 U09354 U10151 U09584 U07785 U03958 U09715 U09266X".split(),
# --- adaptation / PEFT / continual learning / test-time methods built on top of existing FMs
 ADAPT: "U08610 U08668 U09881 U08636 U09639 U08669 U08857 U09596 U06194 U08701 U08679 U08922 U08758 U08646 U09389 U08762 U08682 U08666 U08741 U08761 U08772 U08735 U08763 U08751 U08795 U08752 U08787 U09193 U08744 U08757 U08890 U09068 U08805 U00415 U04942 U05551 U08704 U06447 U08808 U04123 U00884 U00644 U05725 U08624 U09164 U01581 U05413 U00445 U08810 U03782 U04540 U09473 U08620 U08616 U09232 U05546 U09021 U08984".split(),
# --- audits, analyses, comparative evaluations, benchmarks of existing FMs
 EVAL:  "U08792 U03611 U03602 U06492 U08855 U09633 U03595 U10344 U06555 U08760 U08756 U09469 U08767 U08676 U05576 U08785 U08764 U09046 U08746 U08854 U09226 U08503 U09335 U08683 U08886 U09121 U08779 U10214 U09366 U08969 U09257 U08778 U08694 U08918 U00440 U08742 U08963 U09263 U08640 U09492 U06605 U01879 U05619 U00462 U10246 U09367 U03809 U09106 U08714 U09514 U08798 U09138 U08673 U08888 U09253".split(),
# --- applies a general-domain FM (SAM, CLIP, DINOv3, LLM, Whisper, time-series FM) without brain pretraining
 APPL:  "U05162 U08847 U07078 U09706 U08658 U09561 U08832 U03682 U00300 U08775 U09059 U03739 U08931 U08703 U03699 U10341 U01286 U08977 U08807 U10058 U05398 U05379 U08806 U10053 U04545 U09654 U00129 U00671 U09478 U01716 U08713 U08723 U04416 U04993 U09059".split(),
# --- task-specific models (single task, no multi-task/transfer evaluation)
 TASK:  "U08708 U05759 U05528 U03562 U03919 U03726 U03781 U08732 U08852 U04710 U09169 U10328 U00079 U09003 U08786 U08879 U09250 U00713 U08715 U08804 U08774 U00375 U09296 U08892 U08702 U06580 U06554 U09415 U05842 U09289 U09402 U08697 U09229 U09700 U05081 U03742 U06757 U09549 U03776 U03808 U08979 U09198 U04087 U05723 U00347 U09149 U08770 U08726 U08789 U08802 U09113 U08727 U08693 U05872 U09351 U00487 U08665 U09698 U04100 U09741 U08771X".split(),
# --- reviews, position papers, datasets, registries, project announcements, poster abstracts
 REV:   "U04353 U05558 U09530 U00135 U05246 U00354 U10230 U09749 U05690 U08780 U05544 U08850 U00377 U09752 U05348 U05550 U08790 U08793X U04810 U00632 U08693X".split(),
}
reason_of = {}
for reason, ids in X.items():
    for i in ids:
        if i.endswith('X'): continue       # typo guard
        reason_of[i] = reason

# duplicates: same work published twice under different titles / venues (keep the later or peer-reviewed one)
DUP = {'U08655':'U09906', 'U08830':'U09771', 'U08734':'U09629', 'U08743':'U09857', 'U08648':'U09650',
       'U10202':'U00254', 'U05580':'U09611', 'U00246':'U00177', 'U08822':'U08608', 'U08695':'U08698',
       'U05465':'U08700', 'U09180':'U08771', 'U00133':'SEED(tak2026brainiac)', 'U00212':'SEED(mazher2026towards)',
       'U09374':'SEED(wu2026braindino)', 'U00290':'SEED(dibble2026neurofm)', 'U09484':'SEED(guo2026brain)',
       'U03590':'SEED(zhao2026brainblip)', 'U07226':'SEED(ortega2024brainlm)', 'U06544':'SEED(wang2025cbramod)'}

for r in rows:
    rid = r['record_id']
    if r['decision'] != 'include': continue
    if r['tier'] == 'SEED': continue
    if rid in DUP:
        r['stage_full_text'] = r['decision'] = 'exclude'; r['exclusion_reason'] = 'duplicate publication'
        r['notes'] = f'duplicate of {DUP[rid]}'
    elif rid in reason_of:
        r['stage_full_text'] = r['decision'] = 'exclude'; r['exclusion_reason'] = reason_of[rid]
        r['notes'] = 'manual review of abstract (assisted screening)'

# fuzzy duplicate check among remaining includes
inc = [r for r in rows if r['decision']=='include']
def nt(t): return re.sub(r'[^a-z0-9 ]','',t.lower())
for i in range(len(inc)):
    for j in range(i+1, len(inc)):
        a, b = inc[i], inc[j]
        if a['decision']=='include' and b['decision']=='include' and fuzz.token_set_ratio(nt(a['title']), nt(b['title'])) >= 92:
            loser = b if (a['tier']=='SEED' or (a['venue_type']!='preprint' and b['venue_type']=='preprint') or a['year']>=b['year']) else a
            keeper = a if loser is b else b
            loser['stage_full_text']=loser['decision']='exclude'; loser['exclusion_reason']='duplicate publication'; loser['notes']=f"duplicate of {keeper['record_id']}"

w = csv.DictWriter(open('ft_final.csv','w',newline='',encoding='utf-8'), fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
inc = [r for r in rows if r['decision']=='include']
print('INCLUDED MODELS:', len(inc))
print(collections.Counter(r['exclusion_reason'] for r in rows if r['decision']=='exclude'))
print(collections.Counter(r['year'] for r in inc))
mod = collections.Counter()
for r in inc:
    for m in (r['modality_detected'] or 'unspecified').split('; '): mod[m]+=1
print(mod)
