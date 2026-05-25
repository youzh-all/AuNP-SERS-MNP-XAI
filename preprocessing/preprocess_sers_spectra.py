#!/usr/bin/env python3
"""Preprocess SERS spectra for the Au-SAM/RC SERS Transformer workflow.

Input format: wide CSV with one row per spectrum and Raman shift columns after
`sample_id`, as provided in `data_sample/sample_spectra.csv`.

The manuscript workflow used baseline correction followed by Savitzky-Golay
smoothing. This compact script implements a lightweight asymmetric least-squares
baseline correction and Savitzky-Golay smoothing for public reproducibility.
"""
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import sparse
from scipy.sparse.linalg import spsolve
from scipy.signal import savgol_filter


def baseline_als(y, lam=1e5, p=0.01, niter=10):
    y = np.asarray(y, dtype=float)
    L = len(y)
    D = sparse.diags([1, -2, 1], [0, 1, 2], shape=(L - 2, L))
    w = np.ones(L)
    for _ in range(niter):
        W = sparse.spdiags(w, 0, L, L)
        Z = W + lam * D.T @ D
        z = spsolve(Z, w * y)
        w = p * (y > z) + (1 - p) * (y < z)
    return z


def preprocess_frame(df, window_length=11, polyorder=3):
    id_col = df.iloc[:, [0]]
    values = df.iloc[:, 1:].astype(float).to_numpy()
    processed = []
    for row in values:
        corrected = row - baseline_als(row)
        if window_length >= len(corrected):
            window_length = len(corrected) - 1 if len(corrected) % 2 == 0 else len(corrected)
        if window_length % 2 == 0:
            window_length += 1
        smoothed = savgol_filter(corrected, window_length=window_length, polyorder=polyorder)
        processed.append(smoothed)
    out = pd.concat([id_col.reset_index(drop=True), pd.DataFrame(processed, columns=df.columns[1:])], axis=1)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', required=True)
    ap.add_argument('--output', required=True)
    ap.add_argument('--window-length', type=int, default=11)
    ap.add_argument('--polyorder', type=int, default=3)
    args = ap.parse_args()
    df = pd.read_csv(args.input)
    out = preprocess_frame(df, args.window_length, args.polyorder)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.output, index=False)
    print(f'wrote {args.output} with shape {out.shape}')

if __name__ == '__main__':
    main()
