# Risk Matrix Export Report

## Model

- Model: `stable_tail_ua_gnn`; split: `B`; seed: `6`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.2959, MAE=1.0277, QWK=0.4641, Recall@6-8=0.5250.
- `data_2021_train`: Macro-F1=0.3635, MAE=0.9211, QWK=0.5797, Recall@6-8=0.7200.
- `data_2021_test`: Macro-F1=0.2174, MAE=1.2858, QWK=0.3323, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.033041, P75=0.007169, P90=0.010000, P95=0.219942, P99=0.736086, max=1.000000, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.030873, P75=0.006860, P90=0.009611, P95=0.193631, P99=0.650079, max=1.000000, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
