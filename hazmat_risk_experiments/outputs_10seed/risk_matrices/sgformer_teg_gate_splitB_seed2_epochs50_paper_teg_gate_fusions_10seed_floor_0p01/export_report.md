# Risk Matrix Export Report

## Model

- Model: `sgformer_teg_gate`; split: `B`; seed: `2`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_teg_gate_splitB_seed2_epochs50_paper_teg_gate_fusions_10seed.pt`; selected epoch: `45`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6478, MAE=0.6134, QWK=0.7621, Recall@6-8=0.9750.
- `data_2021_train`: Macro-F1=0.8630, MAE=0.4400, QWK=0.9142, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.2962, MAE=1.4322, QWK=0.1316, Recall@6-8=0.2000.
- `data_2021_test`: Macro-F1=0.3513, MAE=1.1569, QWK=0.3987, Recall@6-8=0.3846.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018718, P75=0.004951, P90=0.008609, P95=0.070802, P99=0.432845, max=0.984718, zero_ratio=0.000151.
- `data_2021`: edges=7647, mean=0.017979, P75=0.005087, P90=0.008571, P95=0.064472, P99=0.432849, max=0.965929, zero_ratio=0.000262.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
