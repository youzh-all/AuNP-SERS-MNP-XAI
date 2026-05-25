#!/usr/bin/env python3
"""Read and report the group-wise validation reference metrics.

This script is intentionally lightweight. The representative sample data in this
repository are not the full training/test set, so this script verifies and prints
the reference group-wise metrics reported in the Supporting Information.
"""
import argparse
import pandas as pd


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--reference', default='results_reference/table_s2a_groupwise_validation.csv')
    args = ap.parse_args()
    df = pd.read_csv(args.reference)
    required = {'validation_protocol','test_spectra','exact_match','micro_f1','macro_f1'}
    missing = required - set(df.columns)
    if missing:
        raise SystemExit(f'missing columns: {missing}')
    print(df.to_string(index=False))

if __name__ == '__main__':
    main()
