# Risk Matrix Export Report

## Model

- Model: `weighted_gcn`; split: `B`; seed: `6`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6466, MAE=1.2736, QWK=0.6930, Recall@6-8=0.8500.
- `data_2021_train`: Macro-F1=0.7504, MAE=1.1269, QWK=0.7795, Recall@6-8=0.8400.
- `data_2021_test`: Macro-F1=0.3204, MAE=1.5801, QWK=0.3401, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019860, P75=0.004955, P90=0.008344, P95=0.105999, P99=0.422590, max=0.861009, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017438, P75=0.004847, P90=0.008292, P95=0.080742, P99=0.384892, max=0.855179, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
