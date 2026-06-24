# Risk Matrix Export Report

## Model

- Model: `gcn`; split: `B`; seed: `0`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5933, MAE=0.9202, QWK=0.6922, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.6687, MAE=0.7528, QWK=0.7622, Recall@6-8=0.7600.
- `data_2021_test`: Macro-F1=0.3252, MAE=1.2612, QWK=0.2466, Recall@6-8=0.1923.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019236, P75=0.003502, P90=0.008563, P95=0.114348, P99=0.432415, max=0.865876, zero_ratio=0.000454.
- `data_2021`: edges=7647, mean=0.017186, P75=0.003439, P90=0.007901, P95=0.099022, P99=0.374005, max=0.852805, zero_ratio=0.000785.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
