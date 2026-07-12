# Risk Matrix Export Report

## Model

- Model: `sgformer_teg_gate`; split: `B`; seed: `9`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_teg_gate_splitB_seed9_epochs50_paper_teg_gate_fusions_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6579, MAE=0.4858, QWK=0.8535, Recall@6-8=0.9500.
- `data_2021_train`: Macro-F1=0.8871, MAE=0.2401, QWK=0.9581, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.2796, MAE=1.5220, QWK=0.0847, Recall@6-8=0.2000.
- `data_2021_test`: Macro-F1=0.2874, MAE=1.2731, QWK=0.3915, Recall@6-8=0.3846.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019594, P75=0.006070, P90=0.008570, P95=0.070760, P99=0.432788, max=0.952416, zero_ratio=0.000151.
- `data_2021`: edges=7647, mean=0.016074, P75=0.005452, P90=0.008564, P95=0.054701, P99=0.418720, max=0.904931, zero_ratio=0.000654.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
