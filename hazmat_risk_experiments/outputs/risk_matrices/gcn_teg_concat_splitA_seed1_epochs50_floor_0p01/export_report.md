# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `A`; seed: `1`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5109, MAE=0.5776, QWK=0.7595, Recall@6-8=0.8387.
- `data_2020_val`: Macro-F1=0.2861, MAE=1.2134, QWK=0.4375, Recall@6-8=0.4444.
- `data_2021_test`: Macro-F1=0.3320, MAE=1.1723, QWK=0.3488, Recall@6-8=0.3137.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019462, P75=0.003876, P90=0.008615, P95=0.083937, P99=0.439840, max=0.896118, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.016800, P75=0.003399, P90=0.007893, P95=0.077529, P99=0.415340, max=0.859494, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
