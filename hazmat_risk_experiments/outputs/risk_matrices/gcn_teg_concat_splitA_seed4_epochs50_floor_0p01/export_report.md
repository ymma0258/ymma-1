# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `A`; seed: `4`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5416, MAE=0.5141, QWK=0.8304, Recall@6-8=0.9032.
- `data_2020_val`: Macro-F1=0.2104, MAE=1.5434, QWK=0.0791, Recall@6-8=0.1111.
- `data_2021_test`: Macro-F1=0.3270, MAE=1.2080, QWK=0.3904, Recall@6-8=0.3529.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019374, P75=0.003919, P90=0.008695, P95=0.068362, P99=0.443991, max=0.893432, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.016765, P75=0.003546, P90=0.008313, P95=0.071169, P99=0.419798, max=0.865119, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
