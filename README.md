# AuNP-SERS-MNP-XAI

Public repository for the manuscript:

**Reconfigurable Au Nanoparticle Monolayers on Regenerated Cellulose Hydrogels: Highly Sensitive SERS Detection of Polystyrene Micro/Nanoplastics with Interpretable Deep Learning**

This repository provides the public materials needed to inspect the data format, preprocessing workflow, label definitions, group-wise validation summary, Transformer model implementation, and XAI analysis workflow used in the manuscript.

## What is included

- `data_sample/`: representative sample spectra (60 spectra) for format and workflow demonstration only.
- `metadata/`: label definitions, dataset schema, and group-wise split summary.
- `preprocessing/`: baseline-correction and smoothing workflow used to prepare SERS spectra.
- `models/`: compact Transformer multi-label model implementation and group-wise metric evaluator.
- `xai/`: Integrated Gradients / gradient-saliency utilities.
- `results_reference/`: reference tables corresponding to manuscript/SI values.
- `tests/`: lightweight checks that verify schema consistency and reference table values.

## Important note about the sample data

The representative sample spectra are provided to demonstrate the input structure, label encoding, preprocessing pipeline, and model/evaluation workflow. They are **not** intended to reproduce the full performance metrics reported in the manuscript. The full spectral datasets used for model training and evaluation are available from the corresponding author upon reasonable request.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python preprocessing/preprocess_sers_spectra.py --input data_sample/sample_spectra.csv --output data_sample/sample_spectra_preprocessed.csv
python models/evaluate_groupwise.py --reference results_reference/table_s2a_groupwise_validation.csv
python tests/verify_repository_contents.py
```

## Repository structure

```text
metadata/               label definitions, dataset schema, split summary
data_sample/            representative spectra, metadata, labels
preprocessing/          SERS preprocessing workflow
models/                 Transformer architecture and evaluation utility
xai/                    attribution utilities
results_reference/      manuscript/SI reference result tables
tests/                  reproducibility and consistency checks
```

## Data availability

See [`DATA_AVAILABILITY.md`](DATA_AVAILABILITY.md).
