# Risk Matrix Export Report

## Model

- Model: `edge_gat`; split: `B`; seed: `1`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6343, MAE=0.8236, QWK=0.7300, Recall@6-8=0.8250.
- `data_2021_train`: Macro-F1=0.6824, MAE=0.6550, QWK=0.7542, Recall@6-8=0.8400.
- `data_2021_test`: Macro-F1=0.2634, MAE=1.3813, QWK=0.2663, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021625, P75=0.003964, P90=0.008566, P95=0.120360, P99=0.432589, max=0.928076, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018094, P75=0.003889, P90=0.008548, P95=0.101032, P99=0.419489, max=0.856950, zero_ratio=0.000785.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
