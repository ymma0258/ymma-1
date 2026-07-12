# Risk Matrix Export Report

## Model

- Model: `graphsage_teg_gate`; split: `B`; seed: `7`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_teg_gate_splitB_seed7_epochs50_paper_teg_gate_fusions_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3758, MAE=0.7408, QWK=0.6713, Recall@6-8=0.8000.
- `data_2021_train`: Macro-F1=0.3656, MAE=0.4832, QWK=0.8632, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.1673, MAE=1.1178, QWK=0.2580, Recall@6-8=0.2000.
- `data_2021_test`: Macro-F1=0.2405, MAE=1.2991, QWK=0.2050, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019082, P75=0.004356, P90=0.008477, P95=0.087276, P99=0.429299, max=0.855055, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.016130, P75=0.003891, P90=0.008073, P95=0.069063, P99=0.406125, max=0.856635, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
