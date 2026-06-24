# Risk Matrix Export Report

## Model

- Model: `weighted_gcn`; split: `B`; seed: `3`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5892, MAE=1.1730, QWK=0.6867, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.6895, MAE=0.9443, QWK=0.8333, Recall@6-8=0.8400.
- `data_2021_test`: Macro-F1=0.3025, MAE=1.6104, QWK=0.1630, Recall@6-8=0.0385.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021037, P75=0.004763, P90=0.008571, P95=0.104541, P99=0.432821, max=0.882941, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017330, P75=0.004600, P90=0.008504, P95=0.090586, P99=0.401972, max=0.857131, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
