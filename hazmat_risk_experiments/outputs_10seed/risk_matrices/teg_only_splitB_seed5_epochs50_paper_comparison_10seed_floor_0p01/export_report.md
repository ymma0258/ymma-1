# Risk Matrix Export Report

## Model

- Model: `teg_only`; split: `B`; seed: `5`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\teg_only_splitB_seed5_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5388, MAE=1.3668, QWK=0.6627, Recall@6-8=0.8500.
- `data_2021_train`: Macro-F1=0.7904, MAE=1.2478, QWK=0.8372, Recall@6-8=0.9000.
- `data_2021_val`: Macro-F1=0.2667, MAE=1.8329, QWK=0.2140, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.3266, MAE=1.6361, QWK=0.4567, Recall@6-8=0.4615.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.022779, P75=0.004932, P90=0.008555, P95=0.139738, P99=0.432486, max=0.880743, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018993, P75=0.004776, P90=0.008372, P95=0.116070, P99=0.367173, max=0.850231, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
