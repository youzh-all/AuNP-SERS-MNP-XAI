#!/usr/bin/env python3
"""Run the public smoke workflow and manuscript-reference consistency checks."""
from pathlib import Path
import subprocess
import sys
import pandas as pd

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


def check_reference_values():
    checks = []
    g = pd.read_csv(ROOT / "results_reference/table_s2a_groupwise_validation.csv").iloc[0]
    checks += [
        ("Table S2a exact_match", float(g["exact_match"]), 0.8799),
        ("Table S2a micro_f1", float(g["micro_f1"]), 0.9619),
        ("Table S2a macro_f1", float(g["macro_f1"]), 0.9469),
    ]
    s2 = pd.read_csv(ROOT / "results_reference/table_s2_unseen_conditions.csv")
    cv_thi = float(s2.loc[s2["condition"] == "CV+Thi", "micro_f1"].iloc[0])
    low_pscv = float(s2.loc[s2["condition"] == "0.001 mg/mL", "micro_f1"].iloc[0])
    checks += [
        ("Table S2 CV+Thi micro_f1", cv_thi, 0.4962),
        ("Table S2 PS+CV 0.001 mg/mL micro_f1", low_pscv, 0.5277),
    ]
    s3 = pd.read_csv(ROOT / "results_reference/table_s3_label_prevalence.csv")
    ps_prev = s3.loc[s3["label"] == "PS", "label_prevalence"].iloc[0]
    pe_prop = s3.loc[s3["label"] == "PE", "label_proportion"].iloc[0]
    r6g_prop = s3.loc[s3["label"] == "R6G", "label_proportion"].iloc[0]
    if ps_prev != "100.00%" or pe_prop != "7.68%" or r6g_prop != "7.68%":
        raise AssertionError("Table S3 label prevalence/proportion values do not match expected manuscript values")
    for name, observed, expected in checks:
        if round(observed, 4) != round(expected, 4):
            raise AssertionError(f"{name}: observed {observed}, expected {expected}")
        print(f"PASS: {name} = {observed:.4f}")
    print("PASS: Table S3 label prevalence/proportion values match expected manuscript values")


def main():
    run([sys.executable, "tests/verify_repository_contents.py"])
    run([sys.executable, "preprocessing/preprocess_sers_spectra.py", "--input", "data_sample/sample_spectra.csv", "--output", "data_sample/sample_spectra_preprocessed.csv"])
    run([sys.executable, "models/evaluate_groupwise.py", "--reference", "results_reference/table_s2a_groupwise_validation.csv"])
    check_reference_values()
    print()
    print("OK: public workflow and manuscript-reference consistency checks completed")


if __name__ == "__main__":
    main()
