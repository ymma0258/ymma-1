# Risk Matrix Export Report

## Model

- Model: `gcn`; split: `B`; seed: `9`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gcn_splitB_seed9_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5856, MAE=0.9182, QWK=0.7030, Recall@6-8=0.7500.
- `data_2021_train`: Macro-F1=0.7898, MAE=0.6289, QWK=0.7953, Recall@6-8=0.8500.
- `data_2021_val`: Macro-F1=0.2258, MAE=1.4494, QWK=0.3006, Recall@6-8=0.2000.
- `data_2021_test`: Macro-F1=0.2746, MAE=1.3716, QWK=0.2300, Recall@6-8=0.1923.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021369, P75=0.003813, P90=0.008565, P95=0.131843, P99=0.432723, max=0.957860, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018306, P75=0.003634, P90=0.008292, P95=0.104931, P99=0.424744, max=0.856941, zero_ratio=0.000262.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
