# Risk Matrix Export Report

## Model

- Model: `teg_gnn`; split: `B`; seed: `0`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5517, MAE=1.1965, QWK=0.6801, Recall@6-8=0.8000.
- `data_2021_train`: Macro-F1=0.6047, MAE=1.0758, QWK=0.7774, Recall@6-8=0.8400.
- `data_2021_test`: Macro-F1=0.2892, MAE=1.5107, QWK=0.3246, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.022152, P75=0.005099, P90=0.008571, P95=0.119015, P99=0.432752, max=0.960079, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018854, P75=0.004933, P90=0.008532, P95=0.091036, P99=0.422037, max=0.862639, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
