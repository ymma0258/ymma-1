# Risk Matrix Export Report

## Model

- Model: `stable_tail_gate`; split: `B`; seed: `0`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gate_splitB_seed0_epochs50_paper_stable_tail_gate_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4925, MAE=1.0386, QWK=0.6717, Recall@6-8=0.7000.
- `data_2021_train`: Macro-F1=0.5890, MAE=0.8063, QWK=0.6869, Recall@6-8=0.7500.
- `data_2021_val`: Macro-F1=0.1935, MAE=1.3491, QWK=0.3446, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.3416, MAE=1.3675, QWK=0.3067, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021329, P75=0.004114, P90=0.008563, P95=0.134128, P99=0.432415, max=0.857007, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018361, P75=0.003987, P90=0.008502, P95=0.126677, P99=0.387205, max=0.856347, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
