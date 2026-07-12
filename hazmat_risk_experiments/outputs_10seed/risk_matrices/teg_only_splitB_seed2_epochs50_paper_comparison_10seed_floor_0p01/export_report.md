# Risk Matrix Export Report

## Model

- Model: `teg_only`; split: `B`; seed: `2`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\teg_only_splitB_seed2_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5475, MAE=1.2742, QWK=0.6247, Recall@6-8=0.7750.
- `data_2021_train`: Macro-F1=0.7583, MAE=1.1006, QWK=0.8059, Recall@6-8=0.8500.
- `data_2021_val`: Macro-F1=0.2569, MAE=1.9130, QWK=0.1030, Recall@6-8=0.2000.
- `data_2021_test`: Macro-F1=0.2973, MAE=1.6062, QWK=0.2826, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.022558, P75=0.005035, P90=0.008571, P95=0.126043, P99=0.432864, max=0.945923, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.020208, P75=0.004872, P90=0.008569, P95=0.112336, P99=0.431736, max=0.860343, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
