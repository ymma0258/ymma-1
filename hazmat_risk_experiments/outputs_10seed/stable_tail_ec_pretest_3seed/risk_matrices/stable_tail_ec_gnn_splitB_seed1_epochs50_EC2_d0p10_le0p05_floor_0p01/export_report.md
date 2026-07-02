# Risk Matrix Export Report

## Model

- Model: `stable_tail_ec_gnn`; split: `B`; seed: `1`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.2518, MAE=1.0992, QWK=0.5150, Recall@6-8=0.6000.
- `data_2021_train`: Macro-F1=0.2559, MAE=1.0302, QWK=0.4852, Recall@6-8=0.5200.
- `data_2021_test`: Macro-F1=0.1996, MAE=1.3582, QWK=0.2628, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019846, P75=0.004531, P90=0.007480, P95=0.106383, P99=0.475563, max=0.779157, zero_ratio=0.054672.
- `data_2021`: edges=7647, mean=0.018366, P75=0.004547, P90=0.007055, P95=0.089213, P99=0.449991, max=0.784329, zero_ratio=0.045770.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
