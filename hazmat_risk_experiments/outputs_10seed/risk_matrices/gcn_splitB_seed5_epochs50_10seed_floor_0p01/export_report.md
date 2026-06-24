# Risk Matrix Export Report

## Model

- Model: `gcn`; split: `B`; seed: `5`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6388, MAE=0.7995, QWK=0.7208, Recall@6-8=0.7750.
- `data_2021_train`: Macro-F1=0.8150, MAE=0.6758, QWK=0.8517, Recall@6-8=0.9600.
- `data_2021_test`: Macro-F1=0.3005, MAE=1.2819, QWK=0.1892, Recall@6-8=0.1923.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020174, P75=0.003659, P90=0.008647, P95=0.115958, P99=0.436697, max=0.887057, zero_ratio=0.000151.
- `data_2021`: edges=7647, mean=0.016501, P75=0.003455, P90=0.007988, P95=0.092854, P99=0.378720, max=0.860972, zero_ratio=0.001308.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
