#!/usr/bin/env python3
"""Smoke tests for the public repository package."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def require(path):
    p = ROOT / path
    if not p.exists():
        raise AssertionError(f'missing required file: {path}')
    return p


def main():
    spectra = pd.read_csv(require('data_sample/sample_spectra.csv'))
    metadata = pd.read_csv(require('data_sample/sample_metadata.csv'))
    labels = pd.read_csv(require('data_sample/sample_labels.csv'))
    assert spectra.shape[0] == metadata.shape[0] == labels.shape[0], 'sample row counts differ'
    assert spectra.shape[0] == 60, f'expected 60 sample spectra, got {spectra.shape[0]}'
    assert spectra.shape[1] == 463, f'expected sample_id + 462 wavenumber columns, got {spectra.shape[1]}'
    assert set(['PS','CV','Thi','PE','R6G']).issubset(labels.columns), 'missing label columns'

    groupwise = pd.read_csv(require('results_reference/table_s2a_groupwise_validation.csv')).iloc[0]
    assert round(float(groupwise['micro_f1']), 4) == 0.9619
    assert round(float(groupwise['macro_f1']), 4) == 0.9469
    assert round(float(groupwise['exact_match']), 4) == 0.8799

    table_s2 = pd.read_csv(require('results_reference/table_s2_unseen_conditions.csv'))
    cv_thi = table_s2.loc[table_s2['condition'] == 'CV+Thi', 'micro_f1'].iloc[0]
    assert round(float(cv_thi), 4) == 0.4962

    print('OK: repository schema and reference values verified')

if __name__ == '__main__':
    main()
