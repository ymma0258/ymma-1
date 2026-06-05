# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `5`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4585, MAE=0.7279, QWK=0.7062, Recall@6-8=0.7750.
- `data_2021_train`: Macro-F1=0.5368, MAE=0.6347, QWK=0.7840, Recall@6-8=0.8400.
- `data_2021_test`: Macro-F1=0.2933, MAE=1.2218, QWK=0.3195, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018534, P75=0.003741, P90=0.008598, P95=0.076586, P99=0.436195, max=0.882674, zero_ratio=0.000151.
- `data_2021`: edges=7647, mean=0.014606, P75=0.003261, P90=0.007595, P95=0.067485, P99=0.379143, max=0.870412, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
