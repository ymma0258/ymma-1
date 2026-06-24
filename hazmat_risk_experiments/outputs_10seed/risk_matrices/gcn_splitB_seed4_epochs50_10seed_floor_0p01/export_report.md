# Risk Matrix Export Report

## Model

- Model: `gcn`; split: `B`; seed: `4`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5983, MAE=0.8682, QWK=0.7018, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.7160, MAE=0.7666, QWK=0.7352, Recall@6-8=0.7200.
- `data_2021_test`: Macro-F1=0.3146, MAE=1.2940, QWK=0.2152, Recall@6-8=0.1923.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020357, P75=0.003740, P90=0.008570, P95=0.122065, P99=0.432761, max=0.932443, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018507, P75=0.003666, P90=0.008399, P95=0.107067, P99=0.431731, max=0.862964, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
