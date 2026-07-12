# Risk Matrix Export Report

## Model

- Model: `teg_only`; split: `B`; seed: `9`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\teg_only_splitB_seed9_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5968, MAE=1.1928, QWK=0.6769, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.7876, MAE=0.8953, QWK=0.8649, Recall@6-8=0.9000.
- `data_2021_val`: Macro-F1=0.3879, MAE=1.6540, QWK=0.2368, Recall@6-8=0.2000.
- `data_2021_test`: Macro-F1=0.2554, MAE=1.6677, QWK=0.2770, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020842, P75=0.004857, P90=0.008527, P95=0.100319, P99=0.431141, max=0.928633, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017653, P75=0.004670, P90=0.007988, P95=0.092327, P99=0.401684, max=0.856434, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
