# Results reproducibility scope

This repository is a minimal public reproducibility package for the manuscript. It is designed to support transparency for the machine-learning and XAI components without releasing the full spectral dataset.

## What can be reproduced directly from this repository

1. **Sample-data schema verification**
   - Command: `python tests/verify_repository_contents.py`
   - Expected output: `OK: repository schema and reference values verified`
   - Meaning: verifies that the sample spectra, metadata, labels, and key reference result values are internally consistent.

2. **Preprocessing workflow on representative sample spectra**
   - Command: `python preprocessing/preprocess_sers_spectra.py --input data_sample/sample_spectra.csv --output data_sample/sample_spectra_preprocessed.csv`
   - Expected output shape: `(60, 463)`
   - Meaning: demonstrates the public baseline-correction and smoothing workflow on 60 representative spectra.

3. **Reference group-wise validation values reported in the Supporting Information**
   - Command: `python models/evaluate_groupwise.py --reference results_reference/table_s2a_groupwise_validation.csv`
   - Expected values:
     - test spectra: 408
     - exact match: 0.8799
     - micro-F1: 0.9619
     - macro-F1: 0.9469
   - Meaning: prints the reference group-wise validation values reported in Table S2a of the Supporting Information.

4. **Reference values for selected manuscript/SI tables**
   - Files:
     - `results_reference/table_s2_unseen_conditions.csv`
     - `results_reference/table_s2a_groupwise_validation.csv`
     - `results_reference/table_s2a_groupwise_subgroups.csv`
     - `results_reference/table_s3_label_prevalence.csv`
     - `results_reference/table_s5_ig_peak_alignment_summary.csv`
   - Meaning: provides machine-readable versions of the values discussed in the revised manuscript and Supporting Information.

## What cannot be fully reproduced from this repository alone

The representative sample spectra are not the full training/test dataset. Therefore, this repository is not intended to retrain the full Transformer model or reproduce the full manuscript performance metrics from raw data. The full spectral datasets used for model training and evaluation are available from the corresponding author upon reasonable request.

## Manuscript consistency check

The public reference values in this repository are intended to match the revised manuscript and Supporting Information as follows:

| Repository file | Manuscript/SI location | Key value(s) |
|---|---|---|
| `results_reference/table_s2a_groupwise_validation.csv` | Supporting Information Table S2a | exact match = 0.8799; micro-F1 = 0.9619; macro-F1 = 0.9469 |
| `results_reference/table_s2_unseen_conditions.csv` | Supporting Information Table S2 and Section 2.7 cautious interpretation | CV+Thi micro-F1 = 0.4962; PS+CV 0.001 mg/mL micro-F1 = 0.5277 |
| `results_reference/table_s3_label_prevalence.csv` | Supporting Information Table S3 and Section 2.7 label-imbalance discussion | PS prevalence = 100.00%; PE and R6G label proportions = 7.68% |
| `results_reference/table_s5_ig_peak_alignment_summary.csv` | Supporting Information Table S5 and Section 2.7 XAI interpretation | includes both strong and partial/weak attribution support examples |
