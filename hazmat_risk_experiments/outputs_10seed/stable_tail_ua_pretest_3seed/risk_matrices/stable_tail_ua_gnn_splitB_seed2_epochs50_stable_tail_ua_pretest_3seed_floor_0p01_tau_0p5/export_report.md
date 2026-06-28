# Risk Matrix Export Report

## Model

- Model: `stable_tail_ua_gnn`; split: `B`; seed: `2`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3143, MAE=1.0011, QWK=0.4950, Recall@6-8=0.5000.
- `data_2021_train`: Macro-F1=0.3624, MAE=0.8810, QWK=0.5507, Recall@6-8=0.5600.
- `data_2021_test`: Macro-F1=0.2551, MAE=1.2280, QWK=0.2891, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.036468, P75=0.007769, P90=0.010000, P95=0.270677, P99=0.781432, max=1.000000, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.034535, P75=0.007813, P90=0.010000, P95=0.227452, P99=0.756363, max=1.000000, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
