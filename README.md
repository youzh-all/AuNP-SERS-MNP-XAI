# AuNP-SERS-MNP-XAI

Public repository for the manuscript:

**Reconfigurable Au Nanoparticle Monolayers on Regenerated Cellulose Hydrogels: Highly Sensitive SERS Detection of Polystyrene Micro/Nanoplastics with Interpretable Deep Learning**

This repository provides the public materials needed to inspect the data format, preprocessing workflow, label definitions, group-wise split summary, Transformer model implementation, and XAI analysis utilities used in the manuscript.

## What is included

- `data_sample/`: representative sample spectra (60 spectra) for format and workflow demonstration only.
- `metadata/`: label definitions, dataset schema, and group-wise split summary.
- `preprocessing/`: baseline-correction and smoothing workflow used to prepare SERS spectra.
- `models/`: compact Transformer multi-label model implementation and group-wise split summary utility.
- `xai/`: Integrated Gradients / gradient-saliency utilities.

## Important note about the sample data

The representative sample spectra are provided to demonstrate the input structure, label encoding, preprocessing pipeline, and public analysis workflow. They are **not** intended to reproduce the full performance metrics reported in the manuscript. The full spectral datasets used for model training and evaluation are available from the corresponding author upon reasonable request.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python preprocessing/preprocess_sers_spectra.py --input data_sample/sample_spectra.csv --output data_sample/sample_spectra_preprocessed.csv
python models/evaluate_groupwise.py --split-summary metadata/groupwise_split_summary.csv
python scripts/run_public_workflow.py
```

## Repository structure

```text
metadata/               label definitions, dataset schema, split summary
data_sample/            representative spectra, metadata, labels
preprocessing/          SERS preprocessing workflow
models/                 Transformer architecture and split summary utility
xai/                    attribution utilities
scripts/                public workflow runner
```

## Data availability

See [`DATA_AVAILABILITY.md`](DATA_AVAILABILITY.md).
