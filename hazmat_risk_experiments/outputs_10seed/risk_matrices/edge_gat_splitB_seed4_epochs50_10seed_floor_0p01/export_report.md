# Risk Matrix Export Report

## Model

- Model: `edge_gat`; split: `B`; seed: `4`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5837, MAE=0.8825, QWK=0.6913, Recall@6-8=0.7000.
- `data_2021_train`: Macro-F1=0.6742, MAE=0.7723, QWK=0.6971, Recall@6-8=0.6800.
- `data_2021_test`: Macro-F1=0.2500, MAE=1.3187, QWK=0.2084, Recall@6-8=0.1923.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020520, P75=0.003700, P90=0.008570, P95=0.119770, P99=0.432809, max=0.950519, zero_ratio=0.001212.
- `data_2021`: edges=7647, mean=0.018783, P75=0.003649, P90=0.008573, P95=0.115222, P99=0.432913, max=0.881758, zero_ratio=0.000654.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
