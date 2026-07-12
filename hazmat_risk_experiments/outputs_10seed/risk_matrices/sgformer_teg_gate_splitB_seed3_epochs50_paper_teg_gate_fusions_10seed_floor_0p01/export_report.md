# Risk Matrix Export Report

## Model

- Model: `sgformer_teg_gate`; split: `B`; seed: `3`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_teg_gate_splitB_seed3_epochs50_paper_teg_gate_fusions_10seed.pt`; selected epoch: `36`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5248, MAE=0.8175, QWK=0.6913, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.6893, MAE=0.5697, QWK=0.8159, Recall@6-8=0.8000.
- `data_2021_val`: Macro-F1=0.2738, MAE=1.1122, QWK=0.3755, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2755, MAE=1.3251, QWK=0.2907, Recall@6-8=0.1538.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020063, P75=0.003973, P90=0.008561, P95=0.115728, P99=0.432331, max=0.866169, zero_ratio=0.000303.
- `data_2021`: edges=7647, mean=0.017191, P75=0.003876, P90=0.008301, P95=0.098507, P99=0.397854, max=0.856097, zero_ratio=0.000392.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
