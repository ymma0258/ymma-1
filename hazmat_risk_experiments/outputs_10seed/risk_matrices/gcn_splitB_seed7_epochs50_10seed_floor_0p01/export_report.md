# Risk Matrix Export Report

## Model

- Model: `gcn`; split: `B`; seed: `7`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3861, MAE=1.3034, QWK=0.5677, Recall@6-8=0.5750.
- `data_2021_train`: Macro-F1=0.4932, MAE=1.0802, QWK=0.5848, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2637, MAE=1.5881, QWK=0.2184, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.022671, P75=0.004088, P90=0.008489, P95=0.158646, P99=0.431726, max=0.858010, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.021344, P75=0.004182, P90=0.008421, P95=0.149150, P99=0.433384, max=0.858187, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
