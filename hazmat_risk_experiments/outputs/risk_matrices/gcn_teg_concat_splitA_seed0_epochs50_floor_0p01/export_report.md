# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `A`; seed: `0`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4796, MAE=0.4702, QWK=0.8149, Recall@6-8=0.9677.
- `data_2020_val`: Macro-F1=0.2685, MAE=1.2581, QWK=0.2222, Recall@6-8=0.2222.
- `data_2021_test`: Macro-F1=0.2733, MAE=1.1712, QWK=0.2755, Recall@6-8=0.2549.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.016537, P75=0.003354, P90=0.008170, P95=0.061125, P99=0.431874, max=0.858118, zero_ratio=0.000454.
- `data_2021`: edges=7647, mean=0.014313, P75=0.003181, P90=0.007247, P95=0.057166, P99=0.374639, max=0.844820, zero_ratio=0.000654.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
