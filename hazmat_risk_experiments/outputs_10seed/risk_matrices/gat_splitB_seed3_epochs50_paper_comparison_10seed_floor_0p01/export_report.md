# Risk Matrix Export Report

## Model

- Model: `gat`; split: `B`; seed: `3`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gat_splitB_seed3_epochs50_paper_comparison_10seed.pt`; selected epoch: `49`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6544, MAE=0.7765, QWK=0.7699, Recall@6-8=0.8500.
- `data_2021_train`: Macro-F1=0.8545, MAE=0.5278, QWK=0.9072, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.2675, MAE=1.1155, QWK=0.4984, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2067, MAE=1.3856, QWK=0.1484, Recall@6-8=0.0769.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020406, P75=0.003611, P90=0.008531, P95=0.118653, P99=0.430838, max=0.923684, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017397, P75=0.003670, P90=0.007826, P95=0.115408, P99=0.366987, max=0.856612, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
