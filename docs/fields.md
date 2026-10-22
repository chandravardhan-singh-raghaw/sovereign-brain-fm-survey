# Field definitions for `papers/models.csv`

| Field | Meaning | Values |
| --- | --- | --- |
| `model_id` | Stable identifier from the screening log (`Uxxxxx`). | |
| `model_name` | Short name used in the paper. | |
| `title`, `year`, `venue`, `venue_type` | Bibliographic. `venue_type` ∈ journal, conference, preprint (preprint includes under-review conference submissions). | |
| `architectural_family` | Six-family taxonomy (see `taxonomy.md`). | I Signal Transformer; II 3D Neuroimaging; III CNN/Transformer hybrid; IV Graph-based; V Multimodal; VI Specialized |
| `modality` | Input modalities, `;`-separated. | EEG, iEEG, MEG, fMRI, sMRI, CT, PET, DTI, text/reports |
| `pretraining_objective` | `;`-separated. | masked, contrastive, self-distillation, JEPA/latent-pred, autoregressive, generative/diffusion, supervised pretraining, multi-task |
| `data_scale` | As reported (hours, subjects, scans, volumes, datasets). | free text or NR |
| `dataset_origin` | Countries/regions of the pretraining data. | free text or NR |
| `developer_country` | Country of the lead institution. | free text or NR |
| `south_asian_data_in_corpus` | Whether any South-Asian cohort is in the pretraining data. | Yes / No / NR |
| `evaluated_on_indian_cohort` | Whether any Indian cohort is used in evaluation. | Yes / No |
| `code_available`, `code_url` | Public code mentioned / URL. | yes / NR |
| `doi_or_arxiv`, `paper_url` | Identifier and resolvable link. | |
| `curated` | `yes (manuscript v0)` = fields from full paper; `auto-extracted; verify` = abstract-level; `yes (community-verified)` after review. | |
| `last_checked` | Date fields were last verified. | ISO date |
