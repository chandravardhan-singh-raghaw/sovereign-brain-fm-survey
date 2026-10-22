# Search and screening protocol (v1)

Goal: produce three small CSV files; the script then fills every number in the paper.

| File | One row per | You create it by |
| --- | --- | --- |
| `search_log.csv` | database search run | typing the hit count each database shows |
| `screened.csv` | record found (all databases, before dedup) | exporting results from each database and appending |
| `grey.csv` | Indian data / compute / governance source | listing the sources you cite in §5 and §8 |

Time: about two working days for the searches and export, three to four for screening.

---

## Step 1: Decide and record the window

- Start: **1 January 2021** (BENDR, first self-supervised EEG foundation model).
- End: the day you run the last search. Run all six searches within the same week and use the last date as `FINAL_SEARCH_DATE`.

## Step 2: Run the searches (copy-paste exactly)

Record every run in `search_log.csv` with columns `database,query,date,hits`.

**PubMed** (pubmed.ncbi.nlm.nih.gov → Advanced)
```
("foundation model"[Title/Abstract] OR "self-supervised"[Title/Abstract] OR pretrain*[Title/Abstract] OR "representation learning"[Title/Abstract])
AND (brain[Title/Abstract] OR neuroimaging[Title/Abstract] OR MRI[Title/Abstract] OR "computed tomography"[Title/Abstract] OR fMRI[Title/Abstract] OR EEG[Title/Abstract] OR MEG[Title/Abstract])
AND ("2021/01/01"[Date - Publication] : "3000"[Date - Publication])
```
Hit count: the number shown above the result list. Export: *Save → All results → CSV*.

**IEEE Xplore** (ieeexplore.ieee.org → Advanced Search → Command Search)
```
(("Abstract":"foundation model" OR "Abstract":"self-supervised" OR "Abstract":pretrain* OR "Abstract":"representation learning")
AND ("Abstract":brain OR "Abstract":neuroimaging OR "Abstract":MRI OR "Abstract":"computed tomography" OR "Abstract":fMRI OR "Abstract":EEG OR "Abstract":MEG))
```
Set year range 2021–2026 in the filter. Export: *Export → CSV* (max 2,000 per export; page if needed).

**Scopus** (Advanced search)
```
TITLE-ABS-KEY(("foundation model" OR "self-supervised" OR pretrain* OR "representation learning")
AND (brain OR neuroimaging OR MRI OR "computed tomography" OR fMRI OR EEG OR MEG))
AND PUBYEAR > 2020 AND LANGUAGE(english)
```
Export: *Export → CSV* with Title, Year, DOI, Source title.

**ACM Digital Library** (dl.acm.org → Advanced Search)
```
[[Abstract: "foundation model"] OR [Abstract: "self-supervised"] OR [Abstract: pretrain*] OR [Abstract: "representation learning"]]
AND [[Abstract: brain] OR [Abstract: neuroimaging] OR [Abstract: MRI] OR [Abstract: fMRI] OR [Abstract: EEG] OR [Abstract: MEG]]
AND [E-Publication Date: (01/01/2021 TO *)]
```
Export: BibTeX or CSV.

**OpenReview** (openreview.net → Search; filters ICLR, NeurIPS, ICML)
```
"foundation model" brain
"foundation model" EEG
"foundation model" fMRI
"foundation model" MRI
```
Log the four queries as four rows (same database). Export by copying title/URL into the CSV (no bulk export).

**Preprints: arXiv, bioRxiv, medRxiv** (arxiv.org/search/advanced; biorxiv.org and medrxiv.org advanced search)
```
abstract: ("foundation model" OR "self-supervised" OR pretrain OR "representation learning")
AND abstract: (brain OR neuroimaging OR MRI OR CT OR fMRI OR EEG OR MEG)
```
arXiv: restrict to categories cs.CV, cs.LG, eess.IV, q-bio.NC; date 2021-01-01 to today. Log the three servers as separate rows with database = `Preprints`.

Supplementary (RQ2–3, goes into `grey.csv`, not `screened.csv`): same databases with
`("Indian brain template" OR IBA100 OR ("Indian population" AND (MRI OR CT)) OR (neurocysticercosis AND imaging))`, plus the government sites: icmr.gov.in, meity.gov.in, indiaai.gov.in, cdsco.gov.in, pib.gov.in, abdm.gov.in, and each cohort's website.

## Step 3: Build `screened.csv`

1. Open `screened_template_v1.csv`. It already contains the 40 models in your current tables (marked include at every stage, source `manuscript-v0 (seed)`) and 9 new 2026 models to screen.
2. Append every exported record from Step 2 as a new row: fill `title`, `year`, `venue`, `source_database`, `doi_or_arxiv`. Leave decision columns blank.
3. Do not delete duplicates yourself; the script detects them by DOI/arXiv id or identical title and counts them.

## Step 4: Screen

Pass 1 (title/abstract): set `stage_title_abstract` to `include` or `exclude` for every row. Record the same value in `screen_pass_1`.

Exclude at this stage only for: not brain data; no pretraining stage (task-specific model); not a model paper (review, editorial, dataset-only); not English.

Pass 2, one week later: re-screen a shuffled copy without looking at pass 1, record in `screen_pass_2`. Rows where the two passes disagree → mark `adjudicated = yes` and send me the list; I will give a reasoned recommendation for each, and your final call goes in `stage_title_abstract`.

Full text: for every `include`, read the paper and set `stage_full_text` and `decision`. Exclude reasons (use exactly these strings in `exclusion_reason`): `no pretraining stage`, `no brain downstream task`, `insufficient technical detail`, `provenance not reported`, `duplicate publication`.

## Step 5: Build `grey.csv`

Columns: `source,type,organisation,url,archived_url,date_accessed,decision`. One row per Indian source you cite in §5 (cohorts, templates, archives, compute) and §8 (statutes, rules, guidance). `type` ∈ {statute, rules, guidance, cohort paper, dataset page, dashboard, press release}. Everything you cite is `include`; anything you looked at and rejected is `exclude` with a note.

## Step 6: Generate the numbers

```
python compute_survey_numbers_v1.py screened.csv grey.csv search_log.csv
```
Edit `FINAL_SEARCH_DATE`, `AS_OF_DATE`, `REPO_URL`, `REPO_DOI` at the top of the script first. It writes `survey_numbers_v1.tex`, prints the PRISMA arithmetic, and stops with an assertion error if any row lacks a decision.

## Step 7: What to send me

- The three CSVs (or the database exports as-is; I can merge and dedupe them).
- The disagreement list from the two passes.
I return: deduplicated `screened.csv`, screening recommendations with reasons, the filled `survey_numbers_v1.tex`, and the regenerated model tables once `models.csv` is populated.

## Sanity checks reviewers apply

- identified − duplicates = screened; screened − excluded(T/A) = full text; full text − excluded(FT) = included. The script asserts these.
- Every model in Tables 4/6/7 must appear as `include` in `screened.csv`, and vice versa.
- Hit counts in Table 2 must be those you logged, not re-run later.
