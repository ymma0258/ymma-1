# Risk Matrix Export Report

## Model

- Model: `stable_tail_gnn`; split: `B`; seed: `9`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gnn_splitB_seed9_epochs50_paper_comparison_10seed.pt`; selected epoch: `39`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4222, MAE=0.9519, QWK=0.6170, Recall@6-8=0.6500.
- `data_2021_train`: Macro-F1=0.6236, MAE=0.6937, QWK=0.7382, Recall@6-8=0.7500.
- `data_2021_val`: Macro-F1=0.2306, MAE=1.4299, QWK=0.1676, Recall@6-8=0.2000.
- `data_2021_test`: Macro-F1=0.2719, MAE=1.3798, QWK=0.2537, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021028, P75=0.004292, P90=0.008502, P95=0.113520, P99=0.441327, max=0.874075, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018291, P75=0.003918, P90=0.008093, P95=0.092222, P99=0.408718, max=0.858782, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
