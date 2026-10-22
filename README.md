# Toward Sovereign Indian Brain Foundation Models — Survey Repository

[![Last update](https://img.shields.io/badge/last%20update-2026-10-22-blue)](CHANGELOG.md)
[![Models](https://img.shields.io/badge/models-240-green)](papers/models.csv)
[![License: CC BY 4.0](https://img.shields.io/badge/data-CC%20BY%204.0-lightgrey)](LICENSE)
[![Code: MIT](https://img.shields.io/badge/code-MIT-lightgrey)](LICENSE)
[![DOI](https://img.shields.io/badge/Zenodo-pending-orange)](#citation)

Companion repository for the survey **"Toward Sovereign Indian Brain Foundation Models: Opportunities, Challenges, and Future Directions"**, submitted to *Medical Image Analysis*. It is the single source of truth for every model table and data figure in the paper, and a living catalogue of brain foundation models (BFMs) with their pretraining-data provenance.

- **240 brain foundation models** identified by a PRISMA-ScR scoping review of 15,366 records from PubMed, IEEE Xplore, Scopus, ACM DL, OpenReview (ICLR/NeurIPS/ICML), arXiv, bioRxiv and medRxiv (search closed 2026-10-22).
- Full **screening log** (10,377 unique records with decision and reason) and the **scripts** that reproduce de-duplication, screening, tables and figures.
- A register of **Indian neuroimaging data, compute and governance sources** used in the paper, with access dates.

> ✔︎ marks the models characterised in depth from the full paper in the survey's main tables. All other entries carry abstract-level fields; `NR` = not reported in the abstract. Corrections are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

## Contents

| Path | What it is |
| --- | --- |
| [`papers/models.csv`](papers/models.csv) | The catalogue: one row per model, 22 fields (architecture family, modality, objective, data scale, provenance, code, links). |
| [`papers/related_surveys.csv`](papers/related_surveys.csv) | Reviews, surveys and roadmaps retrieved by the search. |
| [`papers/governance.csv`](papers/governance.csv) | Indian and international statutes, rules and guidance cited in the paper. |
| [`datasets/indian_assets.csv`](datasets/indian_assets.csv) | Indian cohorts, archives, dashboards and benchmarks. |
| [`datasets/templates.csv`](datasets/templates.csv) | Indian and reference brain templates. |
| [`screening/`](screening/) | Protocol, exact queries, hit counts, the screening log, and all scripts. |
| [`latex/`](latex/) | Generated LaTeX tables and the `survey_numbers.tex` macro file used by the manuscript. |
| [`figures/`](figures/) | Generated data figures (PDF). |
| [`docs/`](docs/) | Field definitions and the architectural taxonomy. |

## Selection summary (PRISMA-ScR)

| Stage | n |
| --- | ---: |
| Records identified | 15,366 |
| Duplicates removed | 4,989 |
| Screened on title/abstract | 10,377 |
| Excluded at title/abstract | 8,957 |
| Assessed against eligibility criteria | 1,420 |
| Excluded at eligibility assessment | 1,180 |
| **Models included** | **240** |

Models by year: 2021: 1, 2022: 1, 2023: 8, 2024: 29, 2025: 77, 2026: 123, 2027: 1.

## Catalogue

Grouped by the six-family architectural taxonomy used in the paper. Within each family, newest first. Format: **name** — title (year, venue). *modality*; pretraining objective; data scale. [paper] [code].

### 3D neuroimaging (MRI, CT, PET, dMRI) (54)

- A foundation model for brain tumor MRI analysis: WHO grading and subtype classification (2026, Radiotherapy and Oncology). *sMRI*. [[paper]](https://doi.org/10.1016/j.radonc.2025.111297)
- A generalizable structural brain MRI foundation model built through dual-priority federated pretraining (2026, arXiv). *sMRI*. [[paper]](https://arxiv.org/abs/2609.27611v1)
- Brain-Semantoks: Learning Semantic Tokens of Brain Dynamics with a Self-Distilled Foundation Model (2026, ICLR). *fMRI; sMRI*; self-distillation. [[paper]](https://openreview.net/forum?id=ANkm27vNuk)
- Foundation Model Based on Routine Magnetic Resonance Imaging for Brain Tumor Molecular Profiling and Progression Prediction (2026, JCO Precision Oncology). *sMRI*. [[paper]](https://doi.org/10.1200/PO-25-00930)
- Foundation models for discovering robust biomarkers of neurological disorders from dynamic functional connectivity (2026, arXiv). *fMRI; sMRI*. [[paper]](https://arxiv.org/abs/2604.22018v1) [[code]](https://github.com/SCSE-Biomedical-Computing-Group/RE-CONFIRM)
- Large-Scale Modality-Invariant Foundation Models for Brain Mri Analysis: Application to Lesion Segmentation (2026, 2026 IEEE 23rd International). *sMRI*. [[paper]](https://doi.org/10.1109/ISBI61048.2026.11515369) [[code]](https://github.com/BraveDistribution/UMBRA)
- Neuro-Anatomy–Informed Self-Supervised Learning for Structural Brain MRI (2026, ICML). *sMRI*; contrastive. [[paper]](https://openreview.net/forum?id=x5zDSkJEsw)
- Masked and Predictive Self-Supervised Foundation Models for 3D Brain MRI (2026, arXiv). *sMRI*; masked; JEPA/latent-pred; supervised pretraining. [[paper]](https://arxiv.org/abs/2606.13315v1)
- Normal is All You Need: A Symmetry-Informed Inverse Learning Foundation Model for Neuroimaging Diagnostics (2026, medRxiv). *sMRI*. [[paper]](https://doi.org/10.64898/2026.04.10.26350553)
- Learning Robust and Task-Invariant Functional Representation from fMRI through Siamese Self-Supervised Learning (2026, arXiv). *fMRI; sMRI*. [[paper]](https://arxiv.org/abs/2605.28990v1)
- Tractogram foundation model (2026, arXiv). *sMRI; DTI*; generative/diffusion. [[paper]](https://arxiv.org/abs/2606.09893v1)
- **Brain2Vec** — Brain2Vec: A Self-Supervised 3D Foundation Model for Structural Brain MRI (2026, arXiv). *sMRI*. [[paper]](https://arxiv.org/abs/2610.28411v1) [[code]](https://github.com/CBICA/Brain2Vec)
- **BrainDINO** — BrainDINO: A Brain MRI Foundation Model for Generalizable Clinical Representation Learning (2026, arXiv). *sMRI*; self-distillation; 20 datasets. [[paper]](https://arxiv.org/abs/2604.27277v3) [[code]](https://github.com/mclwu22/BrainDINO) ✔︎
- **BrainFIBRE** — BrainFIBRE: A Foundation Model via Information Decomposition for Brain Microstructure (2026, arXiv). *sMRI; DTI*; contrastive; generative/diffusion. [[paper]](https://arxiv.org/abs/2607.00573v2)
- **BrainFM** — A Foundation Model for Brain MRI with Dynamic Modality Integration (Student Abstract) (2026, AAAI). *sMRI*. [[paper]](https://doi.org/10.1609/aaai.v40i48.42245) ✔︎
- **BrainIAC** — A generalizable foundation model for analysis of human brain MRI (2026, Nat. Neurosci.). *sMRI*. [[paper]](https://doi.org/10.1038/s41593-026-02202-6) ✔︎
- **BrainNext** — BrainNext: A General-Purpose Self-Supervised Foundation Model for Brain MRI Analysis (2026, arXiv). *sMRI*; masked; supervised pretraining. [[paper]](https://arxiv.org/abs/2607.17782v1)
- **BrainNorm** — BrainNorm: A Foundation Model that knows Normal via Semantic Atlas Pretraining (2026, arXiv). *sMRI*; contrastive. [[paper]](https://arxiv.org/abs/2608.17521v1)
- **BrainPFN** — BrainPFN: Amortized Brain-Behaviour Prediction via Prior-Data Fitted Networks (2026, under review). *fMRI; sMRI*. [[paper]](https://openreview.net/forum?id=NXCIy3ulhn)
- **brat** — brat : Aligned Multi-View Embeddings for Brain MRI Analysis (2026, 2026 IEEE/CVF Winter Confere). *sMRI; text/reports*. [[paper]](https://doi.org/10.1109/WACV61042.2026.00568)
- **CoFlu-Brain** — CoFlu-Brain: An fMRI Connectivity Foundation Model with Cofluctuation-Based Pretraining (2026, under review). *fMRI; sMRI*; 13,444 subjects. [[paper]](https://openreview.net/forum?id=EyfLgNSMJk)
- **ICHOR** — ICHOR: A Robust Representation Learning Approach for ASL CBF Maps with Self-Supervised Masked Autoencoders (2026, arXiv). *sMRI*; masked; supervised pretraining; 14 studies. [[paper]](https://arxiv.org/abs/2603.05247v1)
- **NeuroFM** — NeuroFM: Toward Precision Neuroimaging with Foundation Models for Individualized Brain Health Estimation (2026, medRxiv). *sMRI*. [[paper]](https://doi.org/10.64898/2026.03.27.26349489) ✔︎
- **NeuroVFM** — Health system learning enables generalist neuroimaging models (2026, Nat. Med.). *sMRI; CT*. [[paper]](https://doi.org/10.1038/s41591-026-04497-1) ✔︎
- **ReMAP-PET** — ReMAP-PET: Beyond Visual Understanding -- Learning Region-Guided Metabolic Alignment Semantics from Brain PET (2026, arXiv). *PET; text/reports*; masked; contrastive. [[paper]](https://arxiv.org/abs/2606.29577v1)
- **STH-Brain** — STH-Brain: A Hierarchical Spatiotemporal Brain Time-Series Foundation Model (2026, under review). *fMRI; sMRI*; JEPA/latent-pred; supervised pretraining. [[paper]](https://openreview.net/forum?id=b7zAXKPh7W)
- 3D Foundation Model for Generalizable Disease Detection in Head Computed Tomography (2025, arXiv). *CT*; masked; self-distillation. [[paper]](https://arxiv.org/abs/2502.02779v3)
- A Foundation Model for Lesion Segmentation on Brain MRI With Mixture of Modality Experts (2025, IEEE TMI). *sMRI*. [[paper]](https://doi.org/10.1109/TMI.2025.3540809)
- A Modality-agnostic Multi-task Foundation Model for Human Brain Imaging (2025, arXiv). *sMRI; CT*; multi-task. [[paper]](https://arxiv.org/abs/2509.00549v1) [[code]](https://github.com/jhuldr/BrainFM)
- Automatic identification of Parkinsonism using clinical multi-contrast brain MRI: a large self-supervised vision foundation model strategy (2025, EBioMedicine). *sMRI*. [[paper]](https://doi.org/10.1016/j.ebiom.2025.105773)
- Bridging Foundation Models and Efficient Architectures: A Modular Brain Imaging Framework with Local Masking and Pretrained Representation Learning (2025, arXiv). *fMRI*; masked. [[paper]](https://arxiv.org/abs/2508.16597v1)
- From Slices to Volumes: A Scalable Pipeline for Developing General-Purpose Brain MRI Foundation Models (2025, medRxiv). *sMRI*; 42,297 subjects. [[paper]](https://doi.org/10.1101/2025.04.12.25325728)
- Associations of Postencephalitic Epilepsy Using Multi-Contrast Whole Brain MRI: A Large Self-Supervised Vision Foundation Model Strategy (2025, Journal of Magnetic Resonanc). *sMRI*. [[paper]](https://doi.org/10.1002/jmri.29734)
- A Non-contrast Head CT Foundation Model for Comprehensive Neuro-Trauma Triage (2025, arXiv). *CT; text/reports*; contrastive. [[paper]](https://arxiv.org/abs/2502.21106v1)
- Region-Aware Reconstruction Strategy for Pre-training fMRI Foundation Model (2025, NeurIPS). *fMRI; sMRI*; supervised pretraining; 200 dataset; 973 subjects. [[paper]](https://openreview.net/forum?id=52HyCgZrgv)
- Building a General SimCLR Self-Supervised Foundation Model Across Neurological Diseases to Advance 3D Brain MRI Diagnoses (2025, 2025 IEEE/CVF International ). *sMRI*; masked; contrastive; 18,759 patients; 44,958 scans. [[paper]](https://doi.org/10.1109/ICCVW69036.2025.00141) [[code]](https://github.com/emilykaczmarek/3D-Neuro-SimCLR)
- Towards a general-purpose foundation model for fMRI analysis (2025, arXiv). *fMRI; sMRI*; 50,000 subjects. [[paper]](https://arxiv.org/abs/2506.11167v2)
- **BrainFound** — Towards Generalisable Foundation Models for Brain MRI (2025, arXiv). *sMRI*; self-distillation; supervised pretraining. [[paper]](https://arxiv.org/abs/2510.23415v3) ✔︎
- **BrainMVP** — Multi-modal Vision Pre-training for Medical Image Analysis (2025, 2025 IEEE/CVF Conference on ). *sMRI*; contrastive; 16,022 scans; 2.4 million images; 3,755 patients. [[paper]](https://doi.org/10.1109/CVPR52734.2025.00487) ✔︎
- **FM-APP** — FM-APP: Foundation Model for Any Phenotype Prediction via fMRI to sMRI Knowledge Transfer (2025, IEEE TMI). *fMRI*. [[paper]](https://doi.org/10.1109/TMI.2024.3506734) ✔︎
- **NeuroRAD-FM** — NeuroRAD-FM: A Foundation Model for Neuro-Oncology with Distributionally Robust Training (2025, arXiv). *sMRI*; masked; contrastive; self-distillation. [[paper]](https://arxiv.org/abs/2509.15416v1)
- **SSL-AD** — SSL-AD: Spatiotemporal Self-Supervised Learning for Generalizability and Adaptability Across Alzheimer's Prediction Tasks and Datasets (2025, arXiv). *sMRI*; contrastive; 3,161 patients. [[paper]](https://arxiv.org/abs/2509.10453v1) [[code]](https://github.com/emilykaczmarek/SSL-AD)
- **UniBrain** — UniBrain: Universal Brain MRI diagnosis with hierarchical knowledge-enhanced pre-training (2025, Computerized Medical Imaging). *sMRI*. [[paper]](https://doi.org/10.1016/j.compmedimag.2025.102516)
- A foundation model for generalized brain MRI analysis (2024, medRxiv). *sMRI*. [[paper]](https://doi.org/10.1101/2024.12.02.24317992)
- General-Purpose Brain Foundation Models for Time-Series Neuroimaging Data (2024, NeurIPS). *EEG; fMRI; sMRI*. [[paper]](https://openreview.net/forum?id=HwDQH0r37I)
- Domain Aware Multi-Task Pretraining of 3D Swin Transformer for T1-weighted Brain MRI (2024, arXiv). *sMRI*; contrastive; multi-task; 13,687 samples. [[paper]](https://arxiv.org/abs/2410.00410v1)
- **AMAES** — AMAES: Augmented Masked Autoencoder Pretraining on Public Brain MRI Data for 3D-Native Segmentation (2024, arXiv). *sMRI*; masked; supervised pretraining; 45K dataset. [[paper]](https://arxiv.org/abs/2408.00640v2) [[code]](https://github.com/asbjrnmunk/amaes)
- **BrainMorph** — BrainMorph: A Foundational Keypoint Model for Robust and Flexible Brain MRI Registration (2024, arXiv). *sMRI*. [[paper]](https://arxiv.org/abs/2405.14019v3) [[code]](https://github.com/alanqrwang/brainmorph)
- **BrainSegFounder** — BrainSegFounder: Towards 3D Foundation Models for Neuroimage Segmentation (2024, arXiv). *sMRI*; 41,400 participants. [[paper]](https://arxiv.org/abs/2406.10395v3) [[code]](https://github.com/lab-smile/GatorBrain) ✔︎
- **FM-BIM** — An approach to building foundation models for brain image analysis (2024, Med Image Comput Comput Assi). *sMRI*. [[paper]](https://doi.org/10.1007/978-3-031-72390-2_40) ✔︎
- **Medical Transformer** — Medical Transformer: Universal Encoder for 3-D Brain MRI Analysis (2024, IEEE Transactions on Neural ). *sMRI*; masked. [[paper]](https://doi.org/10.1109/TNNLS.2023.3308712)
- Multi-task Collaborative Pre-training and Individual-adaptive-tokens Fine-tuning: A Unified Framework for Brain Representation Learning (2023, arXiv). *sMRI*; multi-task; 200 dataset. [[paper]](https://arxiv.org/abs/2306.11378v1)
- Meta Transfer of Self-Supervised Knowledge: Foundation Model in Action for Post-Traumatic Epilepsy Prediction (2023, arXiv). *fMRI; sMRI*. [[paper]](https://arxiv.org/abs/2312.14204v1)
- **Brain-ID** — Brain-ID: Learning Contrast-agnostic Anatomical Representations for Brain Imaging (2023, arXiv). *sMRI; CT*. [[paper]](https://arxiv.org/abs/2311.16914v2) [[code]](https://github.com/peirong26/Brain-ID) ✔︎

### Multimodal (brain + text or other modality) (35)

- A unified foundation model for heterogeneous EEG signal modeling via language-aligned semi-supervised learning (2027, Neural Networks). *EEG*. [[paper]](https://doi.org/10.1016/j.neunet.2026.109544)
- A foundation model of vision, audition, and language for in-silico neuroscience (2026, arXiv). *fMRI*; 1,000 hours; 720 subjects. [[paper]](https://arxiv.org/abs/2605.04326v1)
- A multimodal foundation model for emergency head CT interpretation (2026, medRxiv). *CT; text/reports*; contrastive. [[paper]](https://doi.org/10.64898/2026.07.07.26357429)
- Continuous-Latent Predictive Modeling with Semantic Alignment for EEG-Language Foundation Models (2026, arXiv). *EEG; text/reports*; masked; autoregressive. [[paper]](https://arxiv.org/abs/2608.11656v1)
- Foundation models meet multimodal neuroimaging: A generative transformer-based framework for Alzheimer's disease diagnosis (2026, Neurocomputing). *NR*. [[paper]](https://doi.org/10.1016/j.neucom.2026.133916)
- From Noisy Neural Time Series to Structured Language: A Foundation Model for Imagined Speech Decoding from EEG signals (2026, ICLR). *EEG*; masked; JEPA/latent-pred. [[paper]](https://openreview.net/forum?id=ul5vGlPtOs)
- Learning Sparse Latent Predictive Foundation Model for Multimodal Neuroimaging (2026, arXiv). *sMRI*; JEPA/latent-pred; 1,551,862 scans; 428,647 studies. [[paper]](https://arxiv.org/abs/2606.14957v5)
- Mind-Omni: A Unified Multi-Task Framework for Brain-Vision-Language Modeling via Discrete Diffusion (2026, ICML). *text/reports*; generative/diffusion; multi-task. [[paper]](https://openreview.net/forum?id=3gCdh3u2GK)
- **Brain3D** — Brain3D: Brain Report Automation via Inflated Vision Transformers in 3D (2026, 2026 IEEE 39th International). *sMRI; text/reports*; contrastive; 468 subjects. [[paper]](https://doi.org/10.1109/CBMS69103.2026.00091) [[code]](https://github.com/PRAISELab-PicusLab/BrainGemma3D)
- **BrainAnytime** — BrainAnytime: Anatomy-Aware Cross-Modal Pretraining for Brain Image Analysis with Arbitrary Modality Availability (2026, arXiv). *sMRI; PET*; masked; 1 scan. [[paper]](https://arxiv.org/abs/2605.13059v1) [[code]](https://github.com/SDH-Lab/BrainAnytime)
- **BrainBLIP** — BrainBLIP: Bootstrapping Language-Image Pretraining from MRI and Cognition Alignment to Diagnose Multiple Brain Disorders (2026, ICASSP). *sMRI; text/reports*. [[paper]](https://doi.org/10.1109/ICASSP55912.2026.11461812) ✔︎
- **BrainWM** — BrainWM: A Multimodal World Model for Representing, Forecasting, and Simulating Whole-Brain Dynamics (2026, under review). *fMRI; sMRI*. [[paper]](https://openreview.net/forum?id=z4sz98xfCJ)
- **CAMEL-CLIP** — CAMEL-CLIP: Channel-aware Multimodal Electroencephalography-text Alignment for Generalizable Brain Foundation Models (2026, arXiv). *EEG*; contrastive. [[paper]](https://arxiv.org/abs/2603.13272v1)
- **CoLaP** — CoLaP: Coupled Latent Prediction for a Synchronized EEG–fNIRS Foundation Model (2026, under review). *EEG*; masked; JEPA/latent-pred. [[paper]](https://openreview.net/forum?id=Dp6Dd5ue6N)
- **MEG-XL** — MEG-XL: Data-Efficient Brain-to-Text via Long-Context Pre-Training (2026, ICLR). *MEG*. [[paper]](https://openreview.net/forum?id=v05JsJkMiW)
- **MindMix** — MindMix: A Multimodal Foundation Model for Auditory Perception Decoding via Deep Neural-Acoustic Alignment (2026, ICLR). *EEG*; 100 hours; 3,000 hours. [[paper]](https://openreview.net/forum?id=1ifQzlETeG) [[code]](https://github.com/CookieMikeLiu/MindMix)
- **Mr3D-VL** — Mr3D-VL: A generalist vision language foundation model for Multiparametric 3D Magnetic Resonance Imaging (2026, arXiv). *sMRI; CT; text/reports*; supervised pretraining. [[paper]](https://arxiv.org/abs/2608.12689v1)
- **NeuroNarrator** — NeuroNarrator: A Generalist EEG-to-Text Foundation Model for Clinical Interpretation via Spectro-Spatial Grounding and Temporal State-Space Reasoning (2026, bioRxiv). *EEG; text/reports*; contrastive. [[paper]](https://doi.org/10.64898/2026.03.07.707799)
- **UniBrain** — UniBrain: Synergistic EEG-FMRI Modeling via Temporal-Spatial Constrained Representation (2026, under review). *EEG; fMRI; sMRI*. [[paper]](https://openreview.net/forum?id=JNlwURai4J)
- A vision–language foundation model for Alzheimer's disease diagnosis using MRI and clinical data (2025, Alzheimer's and Dementia). *sMRI*. [[paper]](https://doi.org/10.1002/alz.71029)
- Towards a Multimodal MRI-Based Foundation Model for Multi-Level Feature Exploration in Segmentation, Molecular Subtyping, and Grading of Glioma (2025, arXiv). *sMRI*; multi-task. [[paper]](https://arxiv.org/abs/2503.06828v1)
- Pretraining Large Brain Language Model for Active BCI: Silent Speech (2025, Proceedings of the 33rd ACM ). *EEG; text/reports*; masked; autoregressive; 12 subjects; 120 hours. [[paper]](https://doi.org/10.1145/3746027.3754810)
- Towards Robust Multimodal Physiological Foundation Models: Handling Arbitrary Missing Modalities (2025, arXiv). *EEG*; masked. [[paper]](https://arxiv.org/abs/2504.19596v3)
- **Brain Harmony** — Brain Harmony: A Multimodal Foundation Model Unifying Morphology and Function into 1D Tokens (2025, NeurIPS). *fMRI; sMRI*; 14 million images. [[paper]](https://openreview.net/forum?id=tPJg65EB7D) ✔︎
- **BrainCLIP** — BrainCLIP: Brain Representation via CLIP for Generic Natural Visual Stimulus Decoding (2025, IEEE Trans Med Imaging). *fMRI; text/reports*. [[paper]](https://doi.org/10.1109/TMI.2025.3537287) ✔︎
- **BrainFCIR** — BrainFCIR: Functional Context Informed Representation Learning for Intracranial Neural Signals (2025, under review). *EEG; iEEG*. [[paper]](https://openreview.net/forum?id=DJqcBAVjdE)
- **ECHO** — ECHO: Toward Contextual Seq2Seq Paradigms in Large EEG Models (2025, arXiv). *EEG*; multi-task. [[paper]](https://arxiv.org/abs/2509.22556v1)
- **ELASTIQ** — ELASTIQ: EEG–Language Alignment with Semantic Task Instruction and Querying (2025, under review). *EEG*; 20 datasets. [[paper]](https://openreview.net/forum?id=Qkeu3hMoUr)
- **GenBrain** — GenBrain: A Generative Foundation Model of Multimodal Brain Imaging (2025, medRxiv). *NR*. [[paper]](https://doi.org/10.64898/2025.12.19.25342614)
- **LEAF** — LEAF: Language-EEG Aligned Foundation Model for Brain-Computer Interfaces (2025, arXiv). *EEG*; 16 datasets. [[paper]](https://arxiv.org/abs/2509.24302v2)
- **NeuroLM** — NeuroLM: A Universal Multi-task Foundation Model for Bridging the Gap between Language and EEG Signals (2025, ICLR). *EEG; text/reports*; multi-task. [[paper]](https://openreview.net/forum?id=Io9yFt7XH7)
- **SAMBA** — SAMBA: Toward a Long-Context EEG Foundation Model via Spatial Embedding and Differential Mamba (2025, arXiv). *EEG*. [[paper]](https://arxiv.org/abs/2511.18571v1)
- **WaveMind** — WaveMind: Towards a Conversational EEG Foundation Model Aligned to Textual and Visual Modalities (2025, arXiv). *EEG; text/reports*. [[paper]](https://arxiv.org/abs/2510.00032v1)
- Advancing Stroke Risk Prediction Using a Multi-modal Foundation Model (2024, arXiv). *sMRI*; contrastive. [[paper]](https://arxiv.org/abs/2411.09822v2)
- Towards neural foundation models for vision: Aligning EEG, MEG and fMRI representations to perform decoding, encoding and modality conversion (2024, ICLR). *EEG; MEG; fMRI*; contrastive. [[paper]](https://openreview.net/forum?id=nxoKCdmteM)

### Specialized architectures (JEPA, MoE, state-space, generative) (25)

- A physics-informed foundation model for quantitative diffusion MRI (2026, arXiv). *sMRI; DTI*; generative/diffusion; 11375 scans. [[paper]](https://arxiv.org/abs/2606.00156v1)
- **B[FM]²** — B[FM]$^2$: Brain Foundation Model via Flow Matching with SplitUNet (2026, arXiv). *EEG*; masked. [[paper]](https://arxiv.org/abs/2606.20812v1)
- **Brain-OF** — Brain-OF: An Omnifunctional Foundation Model for fMRI, EEG and MEG (2026, arXiv). *EEG; MEG; fMRI*; masked; 40 datasets. [[paper]](https://arxiv.org/abs/2602.23410v4) ✔︎
- **BrainMamba** — BrainMamba: A Scalable EEG Foundation Model for Coupled Multi-Channel Spatiotemporal Evolution (2026, under review). *EEG*; masked; 10 datasets. [[paper]](https://openreview.net/forum?id=QChRzNBzza)
- **BrainWorld** — BrainWorld: A Structural-Prior-Conditioned Generative Model for Whole-Brain 4D fMRI Dynamics (2026, arXiv). *fMRI*; 22 datasets. [[paper]](https://arxiv.org/abs/2606.17742v1)
- **dMRI-F** — dMRI-F: A Foundation Model for Generalizable Diffusion MRI Analysis from Sparse Acquisitions (2026, arXiv). *sMRI; DTI*; masked; generative/diffusion. [[paper]](https://arxiv.org/abs/2610.17968v1)
- **EEGDM** — EEGDM: Label-Efficient EEG Representation Learning with Generative Diffusion Model (2026, IEEE Journal of Biomedical a). *EEG*; generative/diffusion; supervised pretraining. [[paper]](https://doi.org/10.1109/JBHI.2026.3737616)
- **FEMBA on the Edge** — FEMBA on the Edge: Physiologically-Aware Pre-Training, Quantization, and Deployment of a Bidirectional Mamba EEG Foundation Model on an Ultra-low Power Microcontroller (2026, arXiv). *EEG*; contrastive; 21,000 hours. [[paper]](https://arxiv.org/abs/2603.26716v1)
- **Laya** — Laya: A LeJEPA Approach to EEG via Latent Prediction over Reconstruction (2026, arXiv). *EEG*; masked; JEPA/latent-pred. [[paper]](https://arxiv.org/abs/2603.16281v2)
- **MEG-GPT-2** — MEG-GPT-2: A Generative Foundation Model for MEG with Structured Neural Representations (2026, ICML). *EEG; MEG*; autoregressive. [[paper]](https://openreview.net/forum?id=yrVRaS2Ocu)
- **MEG-Mamba** — MEG-Mamba: A Scalable State-Space Foundation Model for Magnetoencephalography (2026, arXiv). *EEG; MEG*; autoregressive. [[paper]](https://arxiv.org/abs/2610.00746v1)
- **Rhamba** — Rhamba: Region-Aware Hybrid Attention-Mamba Framework for Self-Supervised Learning in Resting-State fMRI (2026, arXiv). *fMRI; sMRI*; supervised pretraining; 200 datasets. [[paper]](https://arxiv.org/abs/2605.01240v3)
- **SpecMoE** — SpecMoE: Spectral Mixture-of-Experts Foundation Model for Cross-Species EEG Decoding (2026, arXiv). *EEG*; masked; supervised pretraining. [[paper]](https://arxiv.org/abs/2603.16739v2)
- **STEAM** — STEAM: A Spatio-TEmporal Alignment Mixture-of-Experts Model with Hierarchical Pre-training for EEG Decoding (2026, arXiv). *EEG*. [[paper]](https://arxiv.org/abs/2608.02070v2)
- **STST-JEPA** — STST-JEPA: Shallow-Target Spatio-Temporal Joint Embedding Prediction Architecture For EEG Self-Supervised Learning (2026, arXiv). *EEG; fMRI*; masked; JEPA/latent-pred; 3,367 sessions; 47,703 sessions. [[paper]](https://arxiv.org/abs/2607.06629v2)
- **TopoJEPA** — TopoJEPA: Topology-Grounded Joint-Embedding Prediction for EEG Foundation Models (2026, under review). *EEG*; masked; JEPA/latent-pred; autoregressive. [[paper]](https://openreview.net/forum?id=7zTRbIwQQz)
- A Deep Generative Model for Resting-State EEG Synthesis and Transferable Representation Learning (2025, arXiv). *EEG; fMRI*. [[paper]](https://arxiv.org/abs/2503.02636v5) [[code]](https://github.com/Yeganehfrh/REST-GAN)
- **BrainMoE** — BrainMoE: Towards Universal EEG Foundation Models with Channel-wise Mixture-of-Experts (2025, under review). *EEG*. [[paper]](https://openreview.net/forum?id=hWyeiVFZ0q)
- **DenseFormer-MoE** — DenseFormer-MoE: A Dense Transformer Foundation Model With Mixture of Experts for Multi-Task Brain Image Analysis (2025, IEEE TMI). *sMRI*; masked; multi-task. [[paper]](https://doi.org/10.1109/TMI.2025.3551514)
- **EEGMamba** — EEGMamba: An EEG foundation model with Mamba (2025, Neural Networks). *EEG*. [[paper]](https://doi.org/10.1016/j.neunet.2025.107816)
- **FEMBA** — FEMBA: Efficient and Scalable EEG Analysis with a Bidirectional Mamba Foundation Model (2025, 2025 47th Annual Internation). *EEG*; 21,000 hours. [[paper]](https://doi.org/10.1109/EMBC58623.2025.11252697)
- **NeuroMamba** — NeuroMamba: A State-Space Foundation Model for Functional MRI (2025, NeurIPS). *fMRI; sMRI*; autoregressive. [[paper]](https://openreview.net/forum?id=kftg4lmQi8)
- **NeuroRVQ** — NeuroRVQ: Multi-Scale Biosignal Tokenization for Generative Foundation Models (2025, arXiv). *EEG*; masked. [[paper]](https://arxiv.org/abs/2510.13068v4)
- Brain-Mamba: Encoding Brain Activity via Selective State Space Models (2024, Proceedings of Machine Learn). *NR*. [[paper]](https://www.scopus.com/pages/publications/85203841480?origin=resultslist)
- **Brain-JEPA** — Brain-JEPA: Brain Dynamics Foundation Model with Gradient Positioning and Spatiotemporal Masking (2024, NeurIPS). *fMRI*; JEPA/latent-pred. [[paper]](https://openreview.net/forum?id=gtU2eLSAmO) ✔︎

### Graph-based (connectome) models (20)

- A Connectome Interpreter for Brain Foundation Model: From Direct to Directed Connectivity (2026, under review). *fMRI*. [[paper]](https://openreview.net/forum?id=wcPaLT8GKW)
- Diffusion-Guided Pretraining for Brain Graph Foundation Models (2026, arXiv). *NR*; masked; contrastive; generative/diffusion; 25,000 subjects; 60,000 scans. [[paper]](https://arxiv.org/abs/2602.09437v3)
- Toward a Multi-View Brain Network Foundation Model: Cross-View Consistency Learning across Arbitrary Atlases (2026, IEEE Transactions on Pattern). *fMRI*; 20,000 subjects. [[paper]](https://doi.org/10.1109/TPAMI.2026.3736359) [[code]](https://github.com/AngusMonroe/MV-BrainFM)
- A Brain Graph Foundation Model: Pre-Training and Prompt-Tuning across Broad Atlases and Disorders (2026, ICLR). *fMRI; text/reports*; masked; contrastive; 25,000 subjects. [[paper]](https://openreview.net/forum?id=PeGHkAaRxs) [[code]](https://github.com/weixinxu666/BrainGFM)
- **AREION** — AREION: A Foundation Model for Atlas-Agnostic Representation Learning of Brain Connectome (2026, under review). *fMRI; sMRI*. [[paper]](https://openreview.net/forum?id=z796tbMrQ1)
- **BrainNetGFM** — BrainNetGFM: A Graph-Based Foundation Model for Brain Network Construction Integrating Individualized Geometry and Joint Self-Supervised Learning (2026, KDD). *fMRI*; masked; contrastive; 44,476 samples. [[paper]](https://doi.org/10.1145/3770855.3818988) [[code]](https://github.com/BrainLabA/BrainNetGFM)
- **ConnectoFM** — ConnectoFM: A Foundation Model for Learning the Language of the Connectome (2026, bioRxiv). *NR*; masked; contrastive. [[paper]](https://doi.org/10.64898/2026.06.06.730367)
- **FedFound** — FedFound: a federated foundation model for lifespan brain morphological connectome analysis (2026, NPJ Digit Med). *NR*. [[paper]](https://doi.org/10.1038/s41746-026-02925-7)
- Large Connectome Model: An fMRI Foundation Model of Brain Connectomes Empowered by Brain-Environment Interaction in Multitask Learning Landscape (2025, arXiv). *fMRI*; multi-task. [[paper]](https://arxiv.org/abs/2510.18910v1)
- Whole-brain Transferable Representations from Large-Scale fMRI Data Improve Task-Evoked Brain Activity Decoding (2025, arXiv). *fMRI; sMRI*; contrastive; 995 subjects. [[paper]](https://arxiv.org/abs/2507.22378v1)
- Scaling Vision Transformers for Functional MRI with Flat Maps (2025, NeurIPS). *fMRI; sMRI*; masked; 2.3K hours. [[paper]](https://openreview.net/forum?id=L0CpmKEVHw) [[code]](https://github.com/MedARC-AI/fmri-fm)
- Self-Supervised Transformer-Based Foundation Model for functional Magnetic resonance Imaging (2025, 2025 47th Annual Internation). *fMRI; sMRI*; masked; contrastive; 1200 dataset. [[paper]](https://doi.org/10.1109/EMBC58623.2025.11254125)
- **BaRISTA** — BaRISTA: Brain Scale Informed Spatiotemporal Representation of Human Intracranial Neural Activity (2025, NeurIPS). *iEEG*; masked; supervised pretraining. [[paper]](https://openreview.net/forum?id=LDjBDk3Czb)
- **BrainCSD** — BrainCSD: A Hierarchical Consistency-Driven MoE Foundation Model for Unified Connectome Synthesis and Multitask Brain Trait Prediction (2025, arXiv). *fMRI*; masked; contrastive. [[paper]](https://arxiv.org/abs/2511.05630v1) [[code]](https://github.com/SXR3015/BrainCSD)
- **BrainMoE** — BrainMoE: Cognition Joint Embedding via Mixture-of-Expert Towards Robust Brain Foundation Model (2025, NeurIPS). *EEG; fMRI; sMRI*. [[paper]](https://openreview.net/forum?id=05cVmYJJnb)
- **BrainSymphony** — BrainSymphony: A parameter-efficient multimodal foundation model for brain dynamics with limited data (2025, arXiv). *fMRI; sMRI; DTI*; generative/diffusion. [[paper]](https://arxiv.org/abs/2506.18314v2)
- **BrainMAE** — BrainMAE: A Region-aware Self-supervised Learning Framework for Brain Signals (2024, arXiv). *fMRI; sMRI*; masked. [[paper]](https://arxiv.org/abs/2406.17086v1)
- **BrainMass** — BrainMass: Advancing Brain Network Analysis for Diagnosis With Large-Scale Self-Supervised Learning (2024, IEEE TMI). *fMRI*; 30 datasets; 46,686 participants; 70,781 samples. [[paper]](https://doi.org/10.1109/TMI.2024.3414476)
- **NeuroVNN** — Towards a Foundation Model for Brain Age Prediction using coVariance Neural Networks (2024, arXiv). *sMRI*. [[paper]](https://arxiv.org/abs/2402.07684v1) ✔︎
- **MBrain** — MBrain: A Multi-channel Self-Supervised Learning Framework for Brain Signals (2023, KDD). *EEG; iEEG*. [[paper]](https://doi.org/10.1145/3580305.3599426) ✔︎

### CNN/Transformer hybrids (4)

- **Beyond Patch-Level EEG Reconstruction** — Beyond Patch-Level EEG Reconstruction: Contrastive Pretraining and Multiscale Convolutional Transformer for EEG Decoding (2026, under review). *EEG*; masked; contrastive; supervised pretraining. [[paper]](https://openreview.net/forum?id=S1JZfLsLID)
- **AnatCL** — Anatomical Foundation Models for Brain MRIs (2024, arXiv). *sMRI*; contrastive; supervised pretraining. [[paper]](https://arxiv.org/abs/2408.07079v4) [[code]](https://github.com/EIDOSLAB/AnatCL) ✔︎
- **MAEEG** — MAEEG: Masked Auto-encoder for EEG Representation Learning (2022, arXiv). *EEG*; masked. [[paper]](https://arxiv.org/abs/2211.02625v1) ✔︎
- **BENDR** — BENDR: using transformers and a contrastive self-supervised learning task to learn from massive amounts of EEG data (2021, arXiv). *EEG; text/reports*. [[paper]](https://arxiv.org/abs/2101.12037v1) ✔︎

### Signal transformers (EEG, iEEG, MEG) (102)

- A pretrained foundation model for headache disorders based on magnetoencephalography (2026, Journal of Neural Engineerin). *MEG*. [[paper]](https://doi.org/10.1088/1741-2552/ae2805)
- Balanced Latent Semantics and Signal Fidelity for EEG representation learning (2026, ICLR). *EEG*; masked; JEPA/latent-pred. [[paper]](https://openreview.net/forum?id=ofwQZjoI4c)
- Large EEG Foundation Model Learns Informative Low-Frequency Representations from Intracranial Brain Signals (2026, ICLR). *EEG; iEEG*. [[paper]](https://openreview.net/forum?id=SAubA0V3Du)
- Latent-Space Predictive Learning for EEG Foundation Models via Geometric Modeling and Masking (2026, under review). *EEG*; masked. [[paper]](https://openreview.net/forum?id=NehFZdk5Jv)
- Learning EEG Structure in Its Native Coordinates: Operator-Preconditioned Multi-View Pretraining (2026, under review). *EEG*. [[paper]](https://openreview.net/forum?id=vXtOh1O1xt)
- Lightweight Semantic EEG Foundation Model for Frozen Cross-Disorder Transfer (2026, arXiv). *EEG*; supervised pretraining. [[paper]](https://arxiv.org/abs/2610.05503v1)
- Adaptive Multi-Objective Alignment in Pretraining Time-Series Foundation Models for EEG tasks (2026, under review). *EEG*; masked; supervised pretraining. [[paper]](https://openreview.net/forum?id=SB9MyQ9sAX)
- From Static Descriptions to State Dynamics: Multi-Scale Pretraining for EEG Transfer (2026, under review). *EEG*; masked; autoregressive; 2,115 hours. [[paper]](https://openreview.net/forum?id=GHdqwWT2Rp)
- Neural Signals Generate Clinical Notes in the Wild (2026, ICLR). *EEG; text/reports*. [[paper]](https://openreview.net/forum?id=OgSSKlnfBQ) [[code]](https://github.com/Jathurshan0330/CELM)
- Scaling Next-Brain-Token Prediction for MEG (2026, ICLR). *MEG*; autoregressive; 500 hours. [[paper]](https://openreview.net/forum?id=Nfzob9aK4E)
- Next-Token Prediction Enables Scalable Learning of Sleep Physiology (2026, ICML). *EEG*; masked; contrastive; autoregressive. [[paper]](https://openreview.net/forum?id=QVavRSyjmj)
- Omni-Sleep: A Sleep Foundation Model via Hierarchical Contrastive Learning of CNS-ANS Dynamics (2026, arXiv). *EEG*; masked; 100,000 hours. [[paper]](https://arxiv.org/abs/2607.07720v2) [[code]](https://github.com/AutoBrain-sleep/OmniSleep)
- Standing on the Shoulders of Giants: Rethinking EEG Foundation Model Pretraining via Multi-Teacher Distillation (2026, arXiv). *EEG*; masked; self-distillation; 12 datasets. [[paper]](https://arxiv.org/abs/2603.04478v1)
- Taming foundation model with invariance-oriented pre-training for broad-spectrum EEG analysis across signal-level, brain-state, and brain-health tasks (2026, arXiv). *EEG*; 11,000 hours. [[paper]](https://arxiv.org/abs/2608.24597v1)
- **BandVQ** — BandVQ: Band-Wise Vector-Quantized EEG Foundation Model (2026, arXiv). *EEG*; masked; 9,200 subjects. [[paper]](https://arxiv.org/abs/2605.24921v1)
- **Brain-DiT** — Brain-DiT: A Universal Multi-state fMRI Foundation Model with Metadata-Conditioned Pretraining (2026, arXiv). *fMRI*; masked; generative/diffusion; 24 datasets; 349,898 sessions. [[paper]](https://arxiv.org/abs/2604.12683v2)
- **BrainCodes** — BrainCodes: A Lightweight EEG Foundation Model over Discrete Neural Codes (2026, under review). *EEG*; 1,000 participants; 800 hours. [[paper]](https://openreview.net/forum?id=YFbfgStGTr)
- **BrainDuo** — BrainDuo: Dual-Domain Tokenization and Pretraining for EEG Foundation Models (2026, under review). *EEG*; supervised pretraining; 14 datasets. [[paper]](https://openreview.net/forum?id=Ut4T0sM2Jy)
- **BrainRVQ** — BrainRVQ: A High-Fidelity EEG Foundation Model via Dual-Domain Residual Quantization and Hierarchical Autoregression (2026, arXiv). *EEG*; masked; autoregressive. [[paper]](https://arxiv.org/abs/2602.16951v1) [[code]](https://github.com/keqicmz/BrainRVQ)
- **BRIDGE-EEG** — BRIDGE-EEG: Bridging Self-Supervised Pretraining and Efficient Deployment for Cross-Dataset EEG Classification (2026, arXiv). *EEG*; contrastive; multi-task. [[paper]](https://arxiv.org/abs/2609.12218v1)
- **CodeBrain** — CodeBrain: Bridging Decoupled Tokenizer and Multi-Scale Architecture for EEG Foundation Model (2026, ICLR). *EEG*. [[paper]](https://openreview.net/forum?id=msJgEkjwh5) [[code]](https://github.com/jingyingma01/CodeBrain)
- **DANCE** — DANCE: Domain-Aware Network-Coupling Encoder for Coordinate-Free Intracranial EEG Representation Learning (2026, under review). *EEG; iEEG*. [[paper]](https://openreview.net/forum?id=LaGB9LEo2J)
- **DARE-EEG** — DARE-EEG: A Foundation Model for Mining Dual-Aligned Representation of EEG (2026, arXiv). *EEG*; masked; contrastive. [[paper]](https://arxiv.org/abs/2605.18298v1)
- **DeeperBrain** — DeeperBrain: A Neuro-Grounded EEG Foundation Model Towards Universal BCI (2026, under review). *EEG*; masked; 200 hours. [[paper]](https://openreview.net/forum?id=S2FVm50WjS)
- **DIVER-1** — DIVER-1: Scaling Intracranial EEG Foundation Models for Transferable Representations (2026, under review). *EEG; iEEG*; masked; 5,310 hours. [[paper]](https://openreview.net/forum?id=2mzHlw5ctC)
- **DualBrain** — DualBrain: Modeling Bidirectional Spatiotemporal Dependencies in EEG Foundation Models (2026, under review). *EEG*; masked; 11 datasets. [[paper]](https://openreview.net/forum?id=1nCeO53bQq)
- **EEG-DINO** — EEG-DINO: Learning EEG Foundation Models via Hierarchical Self-distillation (2026, Lecture Notes in Computer Sc). *EEG*. [[paper]](https://doi.org/10.1007/978-3-032-04927-8_19)
- **EpilepsyFM** — EpilepsyFM: A domain-specific foundation model for epileptic representation learning using EEG signals (2026, Neural Networks). *EEG*. [[paper]](https://doi.org/10.1016/j.neunet.2025.108060)
- **Ewen** — Ewen: A Covariate-Aware Foundation Model for EEG Understanding (2026, under review). *EEG; text/reports*. [[paper]](https://openreview.net/forum?id=KvMIeBWgq8)
- **GeoLPE** — GeoLPE: Geometry-Aware Latent Prediction for EEG Foundation Modeling (2026, under review). *EEG; iEEG*; JEPA/latent-pred. [[paper]](https://openreview.net/forum?id=Lm99aA49k6)
- **KAST-BAR** — KAST-BAR: Knowledge-Anchored Semantically-Dynamic Topology Brain Autoregressive Modeling for Universal Neural Interpretation (2026, ICML). *EEG*. [[paper]](https://openreview.net/forum?id=Ee4j4zMir5) [[code]](https://github.com/KAST-BAR/KAST-BAR)
- **MANAS-2** — MANAS-2: Constrained Reconstruction for EEG Foundation Models (2026, arXiv). *EEG*; masked. [[paper]](https://arxiv.org/abs/2609.13717v2)
- **M²-EEG** — M²-EEG: A Macro–Micro Pretraining Paradigm for Expanding the Temporal Scope of EEG Foundation Models (2026, under review). *EEG*. [[paper]](https://openreview.net/forum?id=YgmiXqg3bX)
- **NeurDuo-EEG** — NeurDuo-EEG: A Long-Sequence EEG Foundation Model with Persistent State and Explicit Memory (2026, under review). *EEG*; autoregressive; 3,955 hours. [[paper]](https://openreview.net/forum?id=d3k0gdclVC)
- **Neuro-KE** — Neuro-KE: Scaling EEG Foundation Models via Label-Free Knowledge Integration (2026, under review). *EEG; text/reports*; masked; contrastive. [[paper]](https://openreview.net/forum?id=y7vaftM0NX)
- **NeuroCLUS** — NeuroCLUS: A Foundation Model with Functional Clustering for Intracranial Neural Decoding (2026, ICML). *iEEG*. [[paper]](https://openreview.net/forum?id=pFweJM4Uw8)
- **NeuroMI** — NeuroMI: Progressive EEG Foundation Modeling for Neural Decoding of Motor Intention (2026, under review). *EEG*; 300,000 samples. [[paper]](https://openreview.net/forum?id=sIJA6a7xWk)
- **NeuroShield** — NeuroShield: A Device-Agnostic Foundation Model for EEG Authentication (2026, arXiv). *EEG*; 116 sessions; 762 subjects. [[paper]](https://arxiv.org/abs/2606.20673v2)
- **Omni-fMRI** — Omni-fMRI: A Universal Atlas-Free fMRI Foundation Model (2026, ICML). *fMRI*; 11 datasets. [[paper]](https://openreview.net/forum?id=Rc8th2rXXe)
- **PATCHCODE** — PATCHCODE: Discrete Latent Predictive Learning for EEG Foundation Model (2026, ICML). *EEG*; masked; autoregressive. [[paper]](https://openreview.net/forum?id=NWcZ5vualM) [[code]](https://github.com/kierenyyu/Patchcode)
- **PHASE** — PHASE: A Physiology-Guided Hierarchical Foundation Model for Intracranial EEG (2026, under review). *EEG; iEEG*; masked; JEPA/latent-pred; 222 participants. [[paper]](https://openreview.net/forum?id=mALVTjwHBq)
- **PRiSE-EEG** — PRiSE-EEG: A Prior-Guided Foundation Model with Depth-Stratified Experts for Cross-Paradigm EEG Representation Learning (2026, under review). *EEG*. [[paper]](https://openreview.net/forum?id=YP4r4SXdm4)
- **S-CEReBrO** — S-CEReBrO: Breaking the Memory Barrier in Continuous EEG Monitoring (2026, arXiv). *EEG*; 12,000 subjects; 25,000 hours. [[paper]](https://arxiv.org/abs/2607.27913v3)
- **SingLEM** — SingLEM: Single-Channel Large EEG Model (2026, IEEE Journal of Biomedical a). *EEG*; 68 datasets; 71 datasets; 9,200 subjects. [[paper]](https://doi.org/10.1109/JBHI.2026.3732223) [[code]](https://github.com/ttlabtuat/SingLEM)
- **SleepFM-2** — Learning transferable human physiology from two million hours of sleep with SleepFM-2 (2026, NeurIPS). *EEG*; 235,865 recordings. [[paper]](https://openreview.net/forum?id=15dDySBI8T)
- **SPERA** — SPERA: Spherical Prior EEG Foundation Model with Geometry- and Frequency-Aware Latent Prediction (2026, arXiv). *EEG*; JEPA/latent-pred; 106 datasets; 29,048 subjects; 80,000 hours. [[paper]](https://arxiv.org/abs/2610.10571v1)
- **SPOTR** — SPOTR: Spatio-temporal Pooling One-Token Reconstruction for Universal Physiological Signal Self-supervised Learning (2026, arXiv). *EEG; iEEG*; 20 datasets. [[paper]](https://arxiv.org/abs/2606.21973v1) [[code]](https://github.com/5GYYYYY/SPOTR)
- **SSDDB** — SSDDB: A Semantic-Structural Dual-Drive Pretraining Framework for Brain Signals (2026, ICASSP). *EEG; iEEG*; contrastive; self-distillation. [[paper]](https://doi.org/10.1109/ICASSP55912.2026.11462229)
- **ST-CoG-XAI** — ST-CoG-XAI: A Spectrotemporal Contrastive Generation Foundation Model for Explainable EEG Decoding (2026, IEEE Journal on Flexible Ele). *EEG*; contrastive. [[paper]](https://doi.org/10.1109/JFLEX.2025.3620380)
- **TAHLP** — TAHLP: A Topology-Aware Hierarchical Latent Prediction Foundation Model for Cross-Electrode Motor Imagery (2026, under review). *EEG*; self-distillation; JEPA/latent-pred. [[paper]](https://openreview.net/forum?id=0oybptDsvX)
- **Uni-DMFM** — Uni-DMFM: A universal dynamic multi-scale foundation model for EEG representation learning (2026, Pattern Recognition). *EEG*. [[paper]](https://doi.org/10.1016/j.patcog.2026.114221)
- **Uni-NTFM** — Uni-NTFM: A Unified Foundation Model for EEG Signal Representation Learning (2026, ICLR). *EEG*; 28,000 hours. [[paper]](https://openreview.net/forum?id=oUMiuYHW21) [[code]](https://github.com/czs-ict/Uni-NTFM)
- **UniPopT** — UniPopT: Where Does Intracranial EEG Help a Brain-Signal Foundation Model? (2026, under review). *EEG; iEEG*. [[paper]](https://openreview.net/forum?id=JcIG5NkCvk)
- **vNeuro** — vNeuro: Foundation for EEG Vision Models (2026, under review). *EEG*; JEPA/latent-pred. [[paper]](https://openreview.net/forum?id=6QNkVpV1Ux)
- A foundation model with multi-variate parallel attention to generate neuronal activity (2025, NeurIPS). *EEG; iEEG*; 10,000 hours. [[paper]](https://openreview.net/forum?id=hFpCdq5QNl)
- A Foundational fMRI Model for Representing Continuous Brain States (2025, IEEE Journal of Biomedical a). *fMRI*; 1,256 hours. [[paper]](https://doi.org/10.1109/JBHI.2025.3569627)
- Advancing Brainwave Modeling with a Codebook-Based Foundation Model (2025, arXiv). *EEG*. [[paper]](https://arxiv.org/abs/2505.16724v2)
- Large Cognition Model: Towards Pretrained EEG Foundation Model (2025, arXiv). *EEG*. [[paper]](https://arxiv.org/abs/2502.17464v1)
- Learning Structured Sleep Transitions with Sequential EEG Foundation Models (2025, NeurIPS). *EEG; text/reports*; masked. [[paper]](https://openreview.net/forum?id=uqHvhm6BQM)
- Subject-Aware Contrastive Learning for EEG Foundation Models (2025, NeurIPS). *EEG*; contrastive. [[paper]](https://openreview.net/forum?id=MdgBATPjEu)
- **ADFound** — ADFound: A Foundation Model for Diagnosis and Prognosis of Alzheimer’s Disease (2025, IEEE Journal of Biomedical a). *sMRI; PET*; masked; contrastive. [[paper]](https://doi.org/10.1109/JBHI.2025.3576436)
- **ALFEE** — ALFEE: Adaptive Large Foundation Model for EEG Representation (2025, arXiv). *EEG*; 25,000 hours. [[paper]](https://arxiv.org/abs/2505.06291v1) [[code]](https://github.com/xw1216/ALFEE)
- **BioSerenity-E1** — BioSerenity-E1: a self-supervised EEG model for medical applications (2025, arXiv). *EEG*; masked; supervised pretraining. [[paper]](https://arxiv.org/abs/2503.10362v1)
- **BrainOmni** — BrainOmni: A Brain Foundation Model for Unified EEG and MEG Signals (2025, NeurIPS). *EEG; MEG*; supervised pretraining; 1,997 hours; 656 hours. [[paper]](https://openreview.net/forum?id=cjHQj0tCy6) [[code]](https://github.com/OpenTSLab/BrainOmni)
- **BrainPro** — BrainPro: Process-conditioned Pretraining with Topographic Retrieval for Large EEG Models (2025, arXiv). *EEG*; masked; supervised pretraining. [[paper]](https://arxiv.org/abs/2509.22050v3) [[code]](https://github.com/yi-ding-cs/BrainPro)
- **CBraMod** — CBraMod: A Criss-Cross Brain Foundation Model for EEG Decoding (2025, ICLR). *EEG; text/reports*; masked. [[paper]](https://openreview.net/forum?id=NPNUHgHF2w) [[code]](https://github.com/wjq-learning/CBraMod) ✔︎
- **CEReBrO** — CEReBrO: Compact Encoder for Representations of Brain Oscillations Using Efficient Alternating Attention (2025, arXiv). *EEG*; 20,000 hours. [[paper]](https://arxiv.org/abs/2501.10885v4) ✔︎
- **CSBrain** — CSBrain: A Cross-scale Spatiotemporal Brain Foundation Model for EEG Decoding (2025, NeurIPS). *EEG*; 16 datasets. [[paper]](https://openreview.net/forum?id=agcXjEHmyW) ✔︎
- **DIVER-0** — DIVER-0 : A Fully Channel Equivariant EEG Foundation Model (2025, GenBio 2025 Spotlight). *EEG*. [[paper]](https://openreview.net/forum?id=QTfifcFEiE)
- **EEG-X** — EEG-X: Device-Agnostic and Noise-Robust Foundation Model for EEG (2025, under review). *EEG*. [[paper]](https://openreview.net/forum?id=pJlXo9TlW1)
- **GEFM** — GEFM: Graph-Enhanced EEG Foundation Model (2025, 2025 47th Annual Internation). *EEG*; masked. [[paper]](https://doi.org/10.1109/EMBC58623.2025.11254706)
- **HEAR** — HEAR: An EEG Foundation Model with Heterogeneous Electrode Adaptive Representation (2025, under review). *EEG*; 8,782 hours. [[paper]](https://openreview.net/forum?id=eue8OGzkxI)
- **LEAD** — LEAD: An EEG Foundation Model for Alzheimer's Disease Detection (2025, arXiv). *EEG*; contrastive; 13 datasets; 2,238 subjects. [[paper]](https://arxiv.org/abs/2502.01678v5) [[code]](https://github.com/DL4mHealth/LEAD) ✔︎
- **LUNA** — LUNA: Efficient and Topology-Agnostic Foundation Model for EEG Signal Analysis (2025, NeurIPS). *EEG*; masked. [[paper]](https://openreview.net/forum?id=uazfjnFL0G) [[code]](https://github.com/pulp-bio/biofoundation) ✔︎
- **M4CEA** — M4CEA: A Knowledge-guided Foundation Model for Childhood Epilepsy Analysis (2025, IEEE Journal of Biomedical a). *EEG*; multi-task; 1,000 hours. [[paper]](https://doi.org/10.1109/JBHI.2025.3590463) [[code]](https://github.com/Evigouse/M4CEA)
- **MEG-GPT** — MEG-GPT: A transformer-based foundation model for magnetoencephalography data (2025, arXiv). *MEG*; autoregressive. [[paper]](https://arxiv.org/abs/2510.18080v1)
- **MIRepNet** — MIRepNet: A Pipeline and Foundation Model for EEG-Based Motor Imagery Classification (2025, arXiv). *EEG*; masked. [[paper]](https://arxiv.org/abs/2507.20254v1) [[code]](https://github.com/staraink/MIRepNet)
- **NERVE** — NERVE: Noise-Variability-Robust EEG Foundation Model with Electrode-Brain Interactions (2025, under review). *EEG*; masked. [[paper]](https://openreview.net/forum?id=03jzVlLxEe)
- **NeurIPT** — NeurIPT: Foundation Model for Neural Interfaces (2025, NeurIPS). *EEG*; masked. [[paper]](https://openreview.net/forum?id=D4hcJPkJ3y)
- **Neuro-MoBRE** — Neuro-MoBRE: Exploring Multi-subject Multi-task Intracranial Decoding via Explicit Heterogeneity Resolving (2025, under review). *iEEG*; masked; 11 subjects. [[paper]](https://openreview.net/forum?id=eTmjZ82hXa)
- **Neurofusion** — Neurofusion: A Task-Aware EEG Foundation Model with Adaptive Frequency and Spatial Self-Supervised Learning (2025, 2025 21st International Conf). *EEG*. [[paper]](https://doi.org/10.1109/CIS69366.2025.11433883)
- **REVE** — REVE: A Foundation Model for EEG - Adapting to Any Setup with Large-Scale Pretraining on 25,000 Subjects (2025, NeurIPS). *EEG*; masked; 25,000 subjects; 60,000 hours; 92 datasets. [[paper]](https://openreview.net/forum?id=ZeFMtRBy4Z)
- **SLIM-Brain** — SLIM-Brain: A Data- and Training-Efficient Foundation Model for fMRI Data Analysis (2025, under review). *fMRI*; masked; JEPA/latent-pred. [[paper]](https://openreview.net/forum?id=fFgzAQAUqs)
- **STELAR** — STELAR: Dual-space training EEG Foundation Models for Transferable Representations (2025, under review). *EEG*; masked. [[paper]](https://openreview.net/forum?id=WzVHEkp4cK)
- **stLaBraM** — stLaBraM: Interpretable EEG Foundation Models with Factorized Spatial-Temporal Patch Embedding for Self-Supervised Learning (2025, under review). *EEG; text/reports*; masked; supervised pretraining. [[paper]](https://openreview.net/forum?id=Lb0npz4e2d)
- Brant-X: A Unified Physiological Signal Alignment Framework (2024, KDD). *EEG*. [[paper]](https://doi.org/10.1145/3637528.3671953) [[code]](https://github.com/zjunet/Brant-X) ✔︎
- Learning Robust EEG Representations with a Large Spatiotemporal Transformer as a Foundation Model (2024, under review). *EEG*; masked; 300 dataset. [[paper]](https://openreview.net/forum?id=V5Zn0VVvBE)
- Self-Supervised Transformer Model Training for a Sleep-EEG Foundation Model (2024, 2024 46th Annual Internation). *EEG*; masked; supervised pretraining. [[paper]](https://doi.org/10.1109/EMBC53108.2024.10782281)
- **BrainGPT** — BrainGPT: Unleashing the Potential of EEG Generalist Foundation Model by Autoregressive Pre-training (2024, arXiv). *EEG*; masked; autoregressive; multi-task. [[paper]](https://arxiv.org/abs/2410.19779v2) ✔︎
- **BrainLM** — BrainLM: A foundation model for brain activity recordings (2024, ICLR). *fMRI; text/reports*; masked; 6,700 hours. [[paper]](https://openreview.net/forum?id=RwI7ZEfR27) ✔︎
- **BrainSF** — BrainSF: A Foundation Model for Whole Brain Functional Signals Forecasting (2024, under review). *fMRI*. [[paper]](https://openreview.net/forum?id=SDG0EBoqpp)
- **BrainWave** — BrainWave: A Brain Signal Foundation Model for Clinical Applications (2024, arXiv). *EEG; iEEG*; 13.79 TB; 40,000 hours. [[paper]](https://arxiv.org/abs/2402.10251v8) ✔︎
- **EEGFormer** — EEGFormer: Towards Transferable and Interpretable Large-Scale EEG Foundation Model (2024, arXiv). *EEG*. [[paper]](https://arxiv.org/abs/2401.10278v1)
- **EEGPT** — EEGPT: Pretrained Transformer for Universal and Reliable Representation of EEG Signals (2024, NeurIPS). *EEG*. [[paper]](https://www.scopus.com/pages/publications/105000473324?origin=resultslist) ✔︎
- **FoME** — FoME: A Foundation Model for EEG using Adaptive Temporal-Lateral Attention Scaling (2024, arXiv). *EEG; iEEG*; 1.7TB. [[paper]](https://arxiv.org/abs/2409.12454v1) [[code]](https://github.com/1061413241/FoME) ✔︎
- **GPT2MEG** — GPT2MEG: Quantizing MEG for Autoregressive Generation (2024, arXiv). *MEG*; autoregressive. [[paper]](https://arxiv.org/abs/2404.09256v2) [[code]](https://github.com/ricsinaruto/MEG-transfer-decoding)
- **LaBraM** — Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI (2024, ICLR). *EEG; text/reports*; masked; supervised pretraining; 2,500 hours; 20 datasets. [[paper]](https://openreview.net/forum?id=QzTpTRVtrP) [[code]](https://github.com/935963004/LaBraM) ✔︎
- **Neuro-GPT** — Neuro-GPT: Towards A Foundation Model For EEG (2024, 2024 IEEE International Symp). *EEG*; masked; autoregressive; 9 subjects. [[paper]](https://doi.org/10.1109/ISBI56570.2024.10635453) [[code]](https://github.com/wenhui0206/NeuroGPT) ✔︎
- **BIOT** — BIOT: Cross-data Biosignal Learning in the Wild (2023, arXiv). *EEG; text/reports*. [[paper]](https://arxiv.org/abs/2305.10351v1) ✔︎
- **BrainBERT** — BrainBERT: Self-supervised representation learning for intracranial recordings (2023, arXiv). *iEEG; text/reports*. [[paper]](https://arxiv.org/abs/2302.14367v1) ✔︎
- **Brant** — Brant: Foundation Model for Intracranial Neural Signal (2023, NeurIPS). *iEEG*. [[paper]](https://openreview.net/forum?id=DDkl9vaJyE) ✔︎
- **PPi** — PPi: Pretraining Brain Signal Model for Patient-independent Seizure Detection (2023, NeurIPS). *EEG; iEEG*. [[paper]](https://www.scopus.com/pages/publications/85186203889?origin=resultslist)

## Related surveys retrieved by the search

See [`papers/related_surveys.csv`](papers/related_surveys.csv) (48 entries), including roadmaps for MEG foundation models and systematic reviews of brain-imaging and EEG foundation models.

## Indian data, compute and governance register

[`datasets/indian_assets.csv`](datasets/indian_assets.csv) and [`papers/governance.csv`](papers/governance.csv) list every Indian cohort (CBR-SANSCOG, CBR-TLSA, LoCARPoN, cVEDA, LASI-DAD), benchmark (CQ500), template (IBT, IBA100), digital-health rail (ABDM/ABHA), compute programme (IndiaAI, AIRAWAT, AIKosh) and legal instrument (DPDP Act 2023 and Rules 2025, ICMR 2017/2023 guidelines, CDSCO MDR 2017 and MDSW guidance 2026) cited in the paper, with organisation, URL, access date and archived copy where available.

## Reproducing the paper's tables and figures

```bash
pip install -r requirements.txt
python latex/make_tables.py       # -> latex/tab_catalogue.tex, latex/tab_summary.tex
python figures/make_figures.py    # -> figures/*.pdf
python screening/scripts/compute_survey_numbers.py screening/screened.csv papers/governance.csv screening/search_log.csv
```

To reproduce the selection itself, follow [`screening/protocol.md`](screening/protocol.md): run the logged queries, place the exports in `screening/exports_readme/`, and run `screening/scripts/01_merge.py` … `08_tables.py` in order. Every exclusion is recorded with a reason in `screening/screened.csv`.

## Scope and inclusion criteria

A model is included if it (i) was pretrained on human brain imaging or neural-signal data, (ii) was evaluated on at least one downstream brain task, (iii) is described in a peer-reviewed paper or a preprint with sufficient technical detail, and (iv) is presented as a reusable pretrained model rather than a single-task system. Excluded: task-specific models without pretraining or transfer evaluation; applications of general-domain foundation models (SAM, CLIP, LLMs) to brain data without brain pretraining; adaptation, fine-tuning, auditing or benchmarking studies of existing models; non-human, spiking or neuromorphic data only; reviews and position papers. Full criteria in the paper's Section 2 and [`docs/fields.md`](docs/fields.md).

## Contributing

Add a model or correct a field by opening an issue with the **Add a model** template or a pull request editing `papers/models.csv`. Please cite the primary paper and quote the sentence that supports each field you change. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Citation

Until the paper is published, cite the repository (see [`CITATION.cff`](CITATION.cff)). A Zenodo DOI will be minted at submission and recorded here.

## License

Data (CSV, Markdown) are released under CC BY 4.0; code under MIT. See [LICENSE](LICENSE). Paper PDFs are not redistributed; all entries link to the publisher, arXiv or OpenReview.
