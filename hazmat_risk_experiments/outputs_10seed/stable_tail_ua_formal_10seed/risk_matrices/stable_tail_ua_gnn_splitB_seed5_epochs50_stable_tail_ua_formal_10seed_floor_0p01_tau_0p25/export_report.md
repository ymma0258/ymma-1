# Risk Matrix Export Report

## Model

- Model: `stable_tail_ua_gnn`; split: `B`; seed: `5`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.2999, MAE=0.9700, QWK=0.5646, Recall@6-8=0.5750.
- `data_2021_train`: Macro-F1=0.3589, MAE=0.8681, QWK=0.6239, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2366, MAE=1.2339, QWK=0.2912, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.028024, P75=0.005478, P90=0.010000, P95=0.182308, P99=0.515040, max=1.000000, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.025050, P75=0.005150, P90=0.009208, P95=0.157657, P99=0.505000, max=1.000000, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
