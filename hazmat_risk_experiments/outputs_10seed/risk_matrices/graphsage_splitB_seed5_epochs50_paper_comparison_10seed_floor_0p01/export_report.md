# Risk Matrix Export Report

## Model

- Model: `graphsage`; split: `B`; seed: `5`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_splitB_seed5_epochs50_paper_comparison_10seed.pt`; selected epoch: `45`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6326, MAE=0.6946, QWK=0.7579, Recall@6-8=0.8250.
- `data_2021_train`: Macro-F1=0.8258, MAE=0.4922, QWK=0.9293, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.3339, MAE=1.4969, QWK=0.1920, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.3199, MAE=1.1766, QWK=0.4029, Recall@6-8=0.3846.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019235, P75=0.003953, P90=0.008707, P95=0.089489, P99=0.438331, max=0.893571, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.016080, P75=0.003765, P90=0.008452, P95=0.082068, P99=0.409009, max=0.860118, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
