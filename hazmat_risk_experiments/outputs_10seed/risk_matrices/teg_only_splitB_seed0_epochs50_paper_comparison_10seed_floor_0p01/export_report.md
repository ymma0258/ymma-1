# Risk Matrix Export Report

## Model

- Model: `teg_only`; split: `B`; seed: `0`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\teg_only_splitB_seed0_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5536, MAE=1.2243, QWK=0.6883, Recall@6-8=0.7750.
- `data_2021_train`: Macro-F1=0.6205, MAE=1.0564, QWK=0.7877, Recall@6-8=0.8000.
- `data_2021_val`: Macro-F1=0.2681, MAE=1.6955, QWK=0.2665, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.3415, MAE=1.5312, QWK=0.3875, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.022590, P75=0.005084, P90=0.008571, P95=0.128570, P99=0.432787, max=0.960354, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018589, P75=0.004822, P90=0.008536, P95=0.103584, P99=0.421818, max=0.856165, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
