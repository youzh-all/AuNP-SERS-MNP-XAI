#!/usr/bin/env python3
"""Run the public sample-data workflow."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def run(cmd):
    print()
    print("$ " + " ".join(cmd))
    result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, file=sys.stderr, end="")
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def main():
    run([
        sys.executable,
        "preprocessing/preprocess_sers_spectra.py",
        "--input",
        "data_sample/sample_spectra.csv",
        "--output",
        "data_sample/sample_spectra_preprocessed.csv",
    ])
    run([
        sys.executable,
        "models/evaluate_groupwise.py",
        "--split-summary",
        "metadata/groupwise_split_summary.csv",
    ])
    print()
    print("OK: public sample-data workflow completed")


if __name__ == "__main__":
    main()
