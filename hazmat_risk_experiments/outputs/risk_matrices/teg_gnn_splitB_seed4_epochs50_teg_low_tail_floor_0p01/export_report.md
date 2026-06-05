# Risk Matrix Export Report

## Model

- Model: `teg_gnn`; split: `B`; seed: `4`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5658, MAE=1.3359, QWK=0.6365, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.7372, MAE=1.1392, QWK=0.7962, Recall@6-8=0.8800.
- `data_2021_test`: Macro-F1=0.2858, MAE=1.7353, QWK=0.1944, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021510, P75=0.004730, P90=0.008554, P95=0.120370, P99=0.431648, max=0.907733, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.019621, P75=0.004797, P90=0.008460, P95=0.112954, P99=0.426130, max=0.861318, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
