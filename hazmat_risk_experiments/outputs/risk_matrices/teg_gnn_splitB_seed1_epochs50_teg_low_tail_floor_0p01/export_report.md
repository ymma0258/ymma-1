# Risk Matrix Export Report

## Model

- Model: `teg_gnn`; split: `B`; seed: `1`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6038, MAE=1.2786, QWK=0.7203, Recall@6-8=0.8250.
- `data_2021_train`: Macro-F1=0.7191, MAE=1.1524, QWK=0.7898, Recall@6-8=0.8000.
- `data_2021_test`: Macro-F1=0.3183, MAE=1.7058, QWK=0.2935, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020934, P75=0.004819, P90=0.008568, P95=0.113066, P99=0.431737, max=0.882032, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018210, P75=0.004709, P90=0.008529, P95=0.093986, P99=0.402726, max=0.856786, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
