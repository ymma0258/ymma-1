# Risk Matrix Export Report

## Model

- Model: `stable_tail_gnn`; split: `B`; seed: `6`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gnn_splitB_seed6_epochs50_paper_no_tail_loss_10seed.pt`; selected epoch: `24`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.2036, MAE=1.1443, QWK=0.0427, Recall@6-8=0.0000.
- `data_2021_train`: Macro-F1=0.2284, MAE=1.1293, QWK=0.0331, Recall@6-8=0.0000.
- `data_2021_val`: Macro-F1=0.1187, MAE=1.2404, QWK=0.0917, Recall@6-8=0.0000.
- `data_2021_test`: Macro-F1=0.1834, MAE=1.2903, QWK=0.0095, Recall@6-8=0.0000.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.011414, P75=0.002570, P90=0.003472, P95=0.086492, P99=0.196609, max=0.363073, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.011385, P75=0.002567, P90=0.003449, P95=0.076111, P99=0.243517, max=0.375054, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
