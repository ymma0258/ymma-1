# Risk Matrix Export Report

## Model

- Model: `gat`; split: `B`; seed: `7`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gat_splitB_seed7_epochs50_paper_comparison_10seed.pt`; selected epoch: `39`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4611, MAE=1.0095, QWK=0.6438, Recall@6-8=0.6750.
- `data_2021_train`: Macro-F1=0.6754, MAE=0.6638, QWK=0.7998, Recall@6-8=0.8500.
- `data_2021_val`: Macro-F1=0.2099, MAE=1.2117, QWK=0.4395, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2922, MAE=1.4853, QWK=0.2428, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021413, P75=0.003808, P90=0.008429, P95=0.139896, P99=0.429060, max=0.904665, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.019050, P75=0.003946, P90=0.008261, P95=0.113964, P99=0.420006, max=0.850460, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
