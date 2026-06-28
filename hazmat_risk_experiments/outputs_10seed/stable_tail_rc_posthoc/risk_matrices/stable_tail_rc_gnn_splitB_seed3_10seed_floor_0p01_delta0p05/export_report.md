# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `3`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5387, MAE=0.6857, QWK=0.7201, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.6433, MAE=0.4895, QWK=0.8308, Recall@6-8=0.8800.
- `data_2021_test`: Macro-F1=0.2638, MAE=1.2102, QWK=0.1618, Recall@6-8=0.0385.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.017826, P75=0.003456, P90=0.008565, P95=0.072193, P99=0.432546, max=0.913878, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.014514, P75=0.003225, P90=0.008289, P95=0.056944, P99=0.373186, max=0.857133, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
