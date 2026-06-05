# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `A`; seed: `2`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4551, MAE=0.6003, QWK=0.6902, Recall@6-8=0.7742.
- `data_2020_val`: Macro-F1=0.2481, MAE=1.2356, QWK=0.1624, Recall@6-8=0.1111.
- `data_2021_test`: Macro-F1=0.2689, MAE=1.1869, QWK=0.2412, Recall@6-8=0.2157.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.017219, P75=0.003206, P90=0.008373, P95=0.081106, P99=0.423280, max=0.857766, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.014970, P75=0.003014, P90=0.007428, P95=0.076029, P99=0.370232, max=0.869408, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
