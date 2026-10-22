# Contributing

This is a living catalogue. Two kinds of contribution are welcome.

## 1. Add a brain foundation model

Open an issue using the **Add a model** template, or a pull request that adds one row to `papers/models.csv`. A model qualifies if it:

1. was pretrained on human brain imaging (MRI, CT, PET, dMRI) or neural-signal data (EEG, iEEG, MEG);
2. was evaluated on at least one downstream brain task;
3. is described in a peer-reviewed paper or a preprint with sufficient technical detail;
4. is presented as a reusable pretrained model, not a single-task system.

Not in scope: applications of SAM/CLIP/LLMs to brain data without brain pretraining; adapters, fine-tuning, auditing or benchmarking of existing models; non-human, spiking or neuromorphic data only; reviews.

## 2. Correct a field

Most entries carry abstract-level fields (`curated = auto-extracted; verify`). If you know a model's parameter count, pretraining-data origin, developer country, or whether South-Asian data were used, please edit the row and **quote the sentence from the primary paper** that supports the value in the PR description. Set `curated` to `yes (community-verified)` and `last_checked` to today's date.

## Field definitions

See `docs/fields.md`. Use `NR` for "not reported", never leave a cell blank.

## Review

Maintainers check the primary source for every changed field before merging. Please be patient; this is a volunteer effort.
