#!/usr/bin/env python3
"""Integrated Gradients and gradient-saliency utilities for SERS spectra."""
import torch


def integrated_gradients(model, inputs, target_index, baseline=None, steps=50):
    model.eval()
    if baseline is None:
        baseline = torch.zeros_like(inputs)
    scaled = [baseline + (float(i) / steps) * (inputs - baseline) for i in range(1, steps + 1)]
    grads = []
    for x in scaled:
        x = x.clone().detach().requires_grad_(True)
        logits = model(x)
        score = logits[:, target_index].sum()
        model.zero_grad(set_to_none=True)
        score.backward()
        grads.append(x.grad.detach())
    avg_grad = torch.stack(grads).mean(dim=0)
    return (inputs - baseline) * avg_grad


def gradient_saliency(model, inputs, target_index):
    model.eval()
    x = inputs.clone().detach().requires_grad_(True)
    logits = model(x)
    score = logits[:, target_index].sum()
    model.zero_grad(set_to_none=True)
    score.backward()
    return x.grad.detach() * x.detach()
