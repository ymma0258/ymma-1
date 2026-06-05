# Risk Matrix Export Report

## Model

- Model: `teg_gnn`; split: `B`; seed: `3`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5558, MAE=1.2762, QWK=0.6560, Recall@6-8=0.7500.
- `data_2021_train`: Macro-F1=0.6755, MAE=1.0457, QWK=0.7670, Recall@6-8=0.8400.
- `data_2021_test`: Macro-F1=0.2689, MAE=1.6328, QWK=0.1516, Recall@6-8=0.0769.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020815, P75=0.004794, P90=0.008566, P95=0.113563, P99=0.432598, max=0.860798, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017795, P75=0.004699, P90=0.008519, P95=0.098520, P99=0.370585, max=0.856770, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
