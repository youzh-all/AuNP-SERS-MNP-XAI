#!/usr/bin/env python3
"""Read and report the group-wise split summary."""
import argparse
import pandas as pd


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--split-summary', default='metadata/groupwise_split_summary.csv')
    args = ap.parse_args()
    df = pd.read_csv(args.split_summary)
    required = {'protocol', 'train_groups', 'validation_groups', 'test_groups'}
    missing = required - set(df.columns)
    if missing:
        raise SystemExit(f'missing columns: {missing}')
    print(df.to_string(index=False))


if __name__ == '__main__':
    main()
