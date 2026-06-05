# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `6`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4822, MAE=0.8506, QWK=0.6591, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.6581, MAE=0.7317, QWK=0.7470, Recall@6-8=0.8800.
- `data_2021_test`: Macro-F1=0.2888, MAE=1.2380, QWK=0.3694, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019468, P75=0.004238, P90=0.008438, P95=0.080643, P99=0.426281, max=0.849514, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.016958, P75=0.004022, P90=0.008020, P95=0.066849, P99=0.418064, max=0.846067, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
