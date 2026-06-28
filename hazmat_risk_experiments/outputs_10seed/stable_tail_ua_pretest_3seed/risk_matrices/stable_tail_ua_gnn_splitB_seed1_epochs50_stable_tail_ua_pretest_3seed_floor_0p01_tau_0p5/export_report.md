# Risk Matrix Export Report

## Model

- Model: `stable_tail_ua_gnn`; split: `B`; seed: `1`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3751, MAE=0.8739, QWK=0.6288, Recall@6-8=0.6750.
- `data_2021_train`: Macro-F1=0.4120, MAE=0.7661, QWK=0.6400, Recall@6-8=0.6800.
- `data_2021_test`: Macro-F1=0.2300, MAE=1.2963, QWK=0.2606, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.042186, P75=0.009052, P90=0.010000, P95=0.327729, P99=0.908174, max=1.000000, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.039981, P75=0.008933, P90=0.010000, P95=0.311894, P99=0.814105, max=1.000000, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
