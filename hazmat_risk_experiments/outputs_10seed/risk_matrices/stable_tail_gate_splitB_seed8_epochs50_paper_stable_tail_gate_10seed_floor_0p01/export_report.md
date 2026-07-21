# Risk Matrix Export Report

## Model

- Model: `stable_tail_gate`; split: `B`; seed: `8`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gate_splitB_seed8_epochs50_paper_stable_tail_gate_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5741, MAE=0.9410, QWK=0.6863, Recall@6-8=0.7500.
- `data_2021_train`: Macro-F1=0.7824, MAE=0.6655, QWK=0.8148, Recall@6-8=0.9000.
- `data_2021_val`: Macro-F1=0.3824, MAE=1.4051, QWK=0.5124, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.3296, MAE=1.2793, QWK=0.3961, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020282, P75=0.004084, P90=0.008531, P95=0.120971, P99=0.432762, max=0.857121, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017317, P75=0.003852, P90=0.008239, P95=0.103696, P99=0.387936, max=0.857091, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
