# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `9`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4742, MAE=0.7278, QWK=0.6674, Recall@6-8=0.6750.
- `data_2021_train`: Macro-F1=0.6552, MAE=0.5184, QWK=0.7551, Recall@6-8=0.8000.
- `data_2021_test`: Macro-F1=0.2910, MAE=1.2655, QWK=0.2058, Recall@6-8=0.1923.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018204, P75=0.003473, P90=0.008540, P95=0.073478, P99=0.431261, max=0.880392, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.015774, P75=0.003502, P90=0.008352, P95=0.060061, P99=0.421755, max=0.875590, zero_ratio=0.000523.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
