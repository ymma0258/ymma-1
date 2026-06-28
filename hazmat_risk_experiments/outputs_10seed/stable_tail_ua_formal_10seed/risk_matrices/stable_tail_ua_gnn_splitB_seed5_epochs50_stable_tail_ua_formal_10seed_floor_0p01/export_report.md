# Risk Matrix Export Report

## Model

- Model: `stable_tail_ua_gnn`; split: `B`; seed: `5`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.2999, MAE=0.9700, QWK=0.5646, Recall@6-8=0.5750.
- `data_2021_train`: Macro-F1=0.3589, MAE=0.8681, QWK=0.6239, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2366, MAE=1.2339, QWK=0.2912, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018957, P75=0.003676, P90=0.008070, P95=0.097284, P99=0.416573, max=0.824897, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.016522, P75=0.003555, P90=0.006853, P95=0.085681, P99=0.401760, max=0.821418, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
