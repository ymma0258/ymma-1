# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `8`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4997, MAE=0.7401, QWK=0.7565, Recall@6-8=0.8500.
- `data_2021_train`: Macro-F1=0.6268, MAE=0.5659, QWK=0.8581, Recall@6-8=0.9200.
- `data_2021_test`: Macro-F1=0.2631, MAE=1.2227, QWK=0.3276, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018081, P75=0.003669, P90=0.008721, P95=0.072129, P99=0.440434, max=0.910604, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.015547, P75=0.003302, P90=0.008608, P95=0.065888, P99=0.403829, max=0.872989, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
