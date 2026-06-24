# Risk Matrix Export Report

## Model

- Model: `weighted_gcn`; split: `B`; seed: `2`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5916, MAE=1.2091, QWK=0.6780, Recall@6-8=0.7750.
- `data_2021_train`: Macro-F1=0.7226, MAE=1.0920, QWK=0.7886, Recall@6-8=0.8000.
- `data_2021_test`: Macro-F1=0.3626, MAE=1.4997, QWK=0.3338, Recall@6-8=0.3846.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021852, P75=0.004692, P90=0.008557, P95=0.124500, P99=0.431953, max=0.953566, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.019810, P75=0.004598, P90=0.008456, P95=0.104559, P99=0.423954, max=0.894184, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
