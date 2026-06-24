# Risk Matrix Export Report

## Model

- Model: `edge_gat`; split: `B`; seed: `7`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6231, MAE=0.8818, QWK=0.6983, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.6683, MAE=0.6229, QWK=0.7432, Recall@6-8=0.8000.
- `data_2021_test`: Macro-F1=0.2729, MAE=1.3900, QWK=0.1997, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020946, P75=0.004027, P90=0.008559, P95=0.119981, P99=0.432725, max=0.896374, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018049, P75=0.003897, P90=0.008514, P95=0.097158, P99=0.428591, max=0.856812, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
