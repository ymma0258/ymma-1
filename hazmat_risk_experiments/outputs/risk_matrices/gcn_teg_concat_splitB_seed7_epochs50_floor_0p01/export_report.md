# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `7`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5530, MAE=0.6855, QWK=0.7856, Recall@6-8=0.9250.
- `data_2021_train`: Macro-F1=0.6485, MAE=0.4689, QWK=0.8604, Recall@6-8=1.0000.
- `data_2021_test`: Macro-F1=0.2486, MAE=1.3294, QWK=0.2086, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018737, P75=0.004584, P90=0.008580, P95=0.070919, P99=0.433757, max=0.864854, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017072, P75=0.004352, P90=0.008506, P95=0.062015, P99=0.429832, max=0.859665, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
