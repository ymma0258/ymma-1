# Risk Matrix Export Report

## Model

- Model: `gcn`; split: `B`; seed: `8`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6470, MAE=0.8335, QWK=0.7072, Recall@6-8=0.7750.
- `data_2021_train`: Macro-F1=0.8170, MAE=0.6969, QWK=0.8256, Recall@6-8=0.8400.
- `data_2021_test`: Macro-F1=0.2742, MAE=1.3042, QWK=0.2274, Recall@6-8=0.1923.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019438, P75=0.003665, P90=0.008568, P95=0.109517, P99=0.432699, max=0.931346, zero_ratio=0.000454.
- `data_2021`: edges=7647, mean=0.017333, P75=0.003634, P90=0.008469, P95=0.096991, P99=0.413603, max=0.860725, zero_ratio=0.001177.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
