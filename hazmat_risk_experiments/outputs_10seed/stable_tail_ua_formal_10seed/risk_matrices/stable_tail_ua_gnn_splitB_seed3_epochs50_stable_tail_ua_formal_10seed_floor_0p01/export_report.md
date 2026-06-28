# Risk Matrix Export Report

## Model

- Model: `stable_tail_ua_gnn`; split: `B`; seed: `3`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4631, MAE=0.8264, QWK=0.6202, Recall@6-8=0.6000.
- `data_2021_train`: Macro-F1=0.5414, MAE=0.6905, QWK=0.7400, Recall@6-8=0.8000.
- `data_2021_test`: Macro-F1=0.3168, MAE=1.2544, QWK=0.2054, Recall@6-8=0.1154.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018079, P75=0.003539, P90=0.008354, P95=0.085548, P99=0.430681, max=0.855197, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.015353, P75=0.003338, P90=0.007434, P95=0.075109, P99=0.397502, max=0.856029, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
