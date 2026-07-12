# Risk Matrix Export Report

## Model

- Model: `teg_only`; split: `B`; seed: `6`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\teg_only_splitB_seed6_epochs50_paper_comparison_10seed.pt`; selected epoch: `47`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5460, MAE=1.2654, QWK=0.6205, Recall@6-8=0.7500.
- `data_2021_train`: Macro-F1=0.7684, MAE=1.0680, QWK=0.8364, Recall@6-8=0.9000.
- `data_2021_val`: Macro-F1=0.2968, MAE=1.7276, QWK=0.2779, Recall@6-8=0.2000.
- `data_2021_test`: Macro-F1=0.3264, MAE=1.5585, QWK=0.3356, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020469, P75=0.005234, P90=0.008538, P95=0.104092, P99=0.431169, max=0.930859, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017485, P75=0.005037, P90=0.008156, P95=0.089908, P99=0.375853, max=0.854778, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
