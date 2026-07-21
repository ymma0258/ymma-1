# Risk Matrix Export Report

## Model

- Model: `stable_tail_gate`; split: `B`; seed: `6`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gate_splitB_seed6_epochs50_paper_stable_tail_gate_10seed.pt`; selected epoch: `27`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3978, MAE=1.3452, QWK=0.4483, Recall@6-8=0.4000.
- `data_2021_train`: Macro-F1=0.4900, MAE=1.2445, QWK=0.3996, Recall@6-8=0.4000.
- `data_2021_val`: Macro-F1=0.2448, MAE=1.3685, QWK=0.5039, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2287, MAE=1.5208, QWK=0.2470, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021164, P75=0.003942, P90=0.008046, P95=0.146174, P99=0.418959, max=0.829626, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.019919, P75=0.003876, P90=0.007563, P95=0.136180, P99=0.409617, max=0.833775, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
