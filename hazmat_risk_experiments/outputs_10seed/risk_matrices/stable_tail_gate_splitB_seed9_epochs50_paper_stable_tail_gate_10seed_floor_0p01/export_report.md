# Risk Matrix Export Report

## Model

- Model: `stable_tail_gate`; split: `B`; seed: `9`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gate_splitB_seed9_epochs50_paper_stable_tail_gate_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5845, MAE=0.9109, QWK=0.7007, Recall@6-8=0.7500.
- `data_2021_train`: Macro-F1=0.7539, MAE=0.6731, QWK=0.7424, Recall@6-8=0.7500.
- `data_2021_val`: Macro-F1=0.2277, MAE=1.4229, QWK=0.2134, Recall@6-8=0.2000.
- `data_2021_test`: Macro-F1=0.2486, MAE=1.3806, QWK=0.1544, Recall@6-8=0.1538.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020360, P75=0.003826, P90=0.008567, P95=0.118503, P99=0.432657, max=0.926624, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017455, P75=0.003779, P90=0.008425, P95=0.101027, P99=0.424697, max=0.863631, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
