#!/usr/bin/env python3
"""Compact Transformer model for multi-label SERS classification."""
import torch
from torch import nn


class SERSTransformer(nn.Module):
    def __init__(self, n_features: int, n_labels: int = 5, d_model: int = 64,
                 nhead: int = 4, num_layers: int = 2, dim_feedforward: int = 128,
                 dropout: float = 0.1):
        super().__init__()
        self.input_projection = nn.Linear(1, d_model)
        self.position_embedding = nn.Parameter(torch.zeros(1, n_features, d_model))
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=nhead,
            dim_feedforward=dim_feedforward,
            dropout=dropout,
            batch_first=True,
            activation='gelu',
        )
        self.encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.classifier = nn.Sequential(
            nn.LayerNorm(d_model),
            nn.Linear(d_model, n_labels),
        )

    def forward(self, x):
        # x shape: (batch, n_features)
        x = x.unsqueeze(-1)
        h = self.input_projection(x) + self.position_embedding[:, :x.shape[1], :]
        h = self.encoder(h)
        pooled = h.mean(dim=1)
        return self.classifier(pooled)


def predict_probabilities(model, spectra):
    model.eval()
    with torch.no_grad():
        logits = model(spectra)
        return torch.sigmoid(logits)
