# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `4`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4443, MAE=0.7304, QWK=0.7112, Recall@6-8=0.8000.
- `data_2021_train`: Macro-F1=0.5175, MAE=0.6304, QWK=0.7454, Recall@6-8=0.8000.
- `data_2021_test`: Macro-F1=0.3158, MAE=1.2170, QWK=0.3036, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019630, P75=0.003982, P90=0.008678, P95=0.085374, P99=0.438262, max=0.913119, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018122, P75=0.003694, P90=0.008580, P95=0.071733, P99=0.433288, max=0.901223, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
