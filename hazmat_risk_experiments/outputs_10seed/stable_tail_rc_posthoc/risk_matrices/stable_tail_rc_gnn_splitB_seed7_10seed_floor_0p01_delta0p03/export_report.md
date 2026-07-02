# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `7`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4928, MAE=0.7065, QWK=0.7326, Recall@6-8=0.8000.
- `data_2021_train`: Macro-F1=0.6327, MAE=0.4653, QWK=0.8028, Recall@6-8=0.9200.
- `data_2021_test`: Macro-F1=0.2509, MAE=1.3149, QWK=0.2446, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018968, P75=0.004546, P90=0.008628, P95=0.069750, P99=0.439192, max=0.869776, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.016999, P75=0.004415, P90=0.008424, P95=0.060751, P99=0.434920, max=0.863183, zero_ratio=0.000131.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
