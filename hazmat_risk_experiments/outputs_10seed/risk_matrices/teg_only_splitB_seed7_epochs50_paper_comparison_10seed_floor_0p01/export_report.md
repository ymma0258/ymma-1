# Risk Matrix Export Report

## Model

- Model: `teg_only`; split: `B`; seed: `7`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\teg_only_splitB_seed7_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5280, MAE=1.3151, QWK=0.6177, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.8106, MAE=0.9141, QWK=0.8569, Recall@6-8=0.9000.
- `data_2021_val`: Macro-F1=0.3320, MAE=1.6891, QWK=0.1762, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2510, MAE=1.8512, QWK=0.1931, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021795, P75=0.005551, P90=0.008567, P95=0.118264, P99=0.432658, max=0.856758, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018822, P75=0.005161, P90=0.008344, P95=0.100107, P99=0.398988, max=0.855974, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
