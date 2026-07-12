# Risk Matrix Export Report

## Model

- Model: `stable_tail_gnn`; split: `B`; seed: `8`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gnn_splitB_seed8_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5169, MAE=0.7785, QWK=0.7641, Recall@6-8=0.9500.
- `data_2021_train`: Macro-F1=0.6992, MAE=0.5125, QWK=0.8819, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.3670, MAE=1.2366, QWK=0.6024, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2787, MAE=1.2491, QWK=0.4023, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018747, P75=0.003960, P90=0.008624, P95=0.074604, P99=0.435492, max=0.883400, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.015450, P75=0.003576, P90=0.008490, P95=0.073684, P99=0.370429, max=0.859126, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
