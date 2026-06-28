# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `5`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4511, MAE=0.7462, QWK=0.6747, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.5370, MAE=0.6454, QWK=0.7101, Recall@6-8=0.7200.
- `data_2021_test`: Macro-F1=0.2602, MAE=1.1962, QWK=0.2462, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.017636, P75=0.003249, P90=0.008305, P95=0.072000, P99=0.419777, max=0.858755, zero_ratio=0.000303.
- `data_2021`: edges=7647, mean=0.013687, P75=0.003042, P90=0.007398, P95=0.056644, P99=0.373623, max=0.858196, zero_ratio=0.000262.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
