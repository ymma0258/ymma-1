# Risk Matrix Export Report

## Model

- Model: `graphsage_teg_gate`; split: `B`; seed: `0`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_teg_gate_splitB_seed0_epochs50_paper_teg_gate_fusions_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3137, MAE=0.8443, QWK=0.6215, Recall@6-8=0.6750.
- `data_2021_train`: Macro-F1=0.3600, MAE=0.7058, QWK=0.7463, Recall@6-8=0.9000.
- `data_2021_val`: Macro-F1=0.2583, MAE=1.0928, QWK=0.6214, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2750, MAE=1.1411, QWK=0.3404, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018901, P75=0.003908, P90=0.008323, P95=0.077488, P99=0.435738, max=0.864459, zero_ratio=0.002272.
- `data_2021`: edges=7647, mean=0.015993, P75=0.003369, P90=0.007894, P95=0.071183, P99=0.412287, max=0.862369, zero_ratio=0.001308.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
