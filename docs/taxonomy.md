# Architectural taxonomy

| Family | Defining mechanism | Typical data | Examples |
| --- | --- | --- | --- |
| I Signal transformers | Patch/token sequence modelling of neural signals with temporal, channel and cross-scale attention | EEG, iEEG, MEG, fMRI time series | BrainBERT, LaBraM, CBraMod, CSBrain, LUNA, REVE |
| II 3D neuroimaging | Slice-based or volumetric encoders (3D CNN, 3D ViT) for brain images | MRI, CT, PET, dMRI | BrainSegFounder, Brain-ID, BrainIAC, NeuroVFM, BrainFound, BrainDINO |
| III CNN/Transformer hybrids | Convolutional local feature extraction feeding a Transformer | EEG, sMRI | BENDR, MAEEG, AnatCL |
| IV Graph-based | Explicit relational structure over channels, regions or connectomes | fMRI connectivity, EEG graphs, cortical features | MBrain, NeuroVNN, Brain Graph FM, BrainNetGFM |
| V Multimodal | Alignment or fusion across brain modalities or with text | MRI + reports, EEG + text, sMRI + fMRI | BrainCLIP, BrainBLIP, Brain Harmony, NeuroLM |
| VI Specialized | JEPA latent prediction, sparse MoE, state-space, generative/world models | fMRI, EEG, MEG | Brain-JEPA, Brain-OF, Brain-DiT, BrainMamba |

For the 37 models characterised in depth in the paper the family was assigned manually; for the remainder it was assigned by keyword rules from title and abstract (`screening/scripts/08_tables.py`) and should be verified against the paper.
