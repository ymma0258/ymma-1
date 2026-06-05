# Risk Matrix Export Report

## Model

- Model: `teg_gnn`; split: `B`; seed: `0`; epochs: `20`.
- Risk mode: `raw`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3290, MAE=1.8863, QWK=0.4939, Recall@6-8=0.6500.
- `data_2021_train`: Macro-F1=0.5008, MAE=1.8281, QWK=0.4885, Recall@6-8=0.6400.
- `data_2021_test`: Macro-F1=0.2516, MAE=2.0624, QWK=0.4452, Recall@6-8=0.4615.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021448, P75=0.000000, P90=0.000000, P95=0.196855, P99=0.428293, max=0.856586, zero_ratio=0.928366.
- `data_2021`: edges=7647, mean=0.019466, P75=0.000000, P90=0.000000, P95=0.191936, P99=0.428320, max=0.856639, zero_ratio=0.931476.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
