# Results reproducibility scope

This repository is a minimal public reproducibility package for the manuscript. It is designed to support transparency for the machine-learning and XAI workflow components without releasing the full spectral dataset.

## What can be reproduced directly from this repository

1. **Preprocessing workflow on representative sample spectra**
   - Command: `python preprocessing/preprocess_sers_spectra.py --input data_sample/sample_spectra.csv --output data_sample/sample_spectra_preprocessed.csv`
   - Expected output shape: `(60, 463)`
   - Meaning: demonstrates the public baseline-correction and smoothing workflow on 60 representative spectra.

2. **Group-wise split summary inspection**
   - Command: `python models/evaluate_groupwise.py --split-summary metadata/groupwise_split_summary.csv`
   - Expected split definition:
     - train groups: `1-66`
     - validation groups: `67-132`
     - test groups: `133-200`
   - Meaning: reports the group-level separation used to prevent spectra from the same acquisition group from being shared across subsets.

3. **Public workflow check**
   - Command: `python scripts/run_public_workflow.py`
   - Meaning: runs the sample preprocessing workflow and prints the group-wise split summary.

## What cannot be fully reproduced from this repository alone

The representative sample spectra are not the full training/test dataset. Therefore, this repository is not intended to retrain the full Transformer model or reproduce the full manuscript performance metrics from raw data. The full spectral datasets used for model training and evaluation are available from the corresponding author upon reasonable request.

## Manuscript consistency note

Reference performance tables and internal test files are not included in this minimal public repository. Performance values should be checked against the revised manuscript and Supporting Information.
