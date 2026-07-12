# Risk Matrix Export Report

## Model

- Model: `graphsage_teg_gate`; split: `B`; seed: `3`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_teg_gate_splitB_seed3_epochs50_paper_teg_gate_fusions_10seed.pt`; selected epoch: `47`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4892, MAE=0.8476, QWK=0.6483, Recall@6-8=0.6500.
- `data_2021_train`: Macro-F1=0.6397, MAE=0.7123, QWK=0.7908, Recall@6-8=0.8000.
- `data_2021_val`: Macro-F1=0.3091, MAE=0.9673, QWK=0.6408, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2290, MAE=1.2427, QWK=0.0684, Recall@6-8=0.0385.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018380, P75=0.003544, P90=0.007902, P95=0.097364, P99=0.427082, max=0.845706, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.015113, P75=0.003161, P90=0.007233, P95=0.074523, P99=0.349273, max=0.820345, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
