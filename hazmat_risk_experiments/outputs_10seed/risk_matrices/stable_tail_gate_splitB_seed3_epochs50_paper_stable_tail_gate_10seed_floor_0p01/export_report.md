# Risk Matrix Export Report

## Model

- Model: `stable_tail_gate`; split: `B`; seed: `3`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gate_splitB_seed3_epochs50_paper_stable_tail_gate_10seed.pt`; selected epoch: `49`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5556, MAE=0.8638, QWK=0.6913, Recall@6-8=0.7000.
- `data_2021_train`: Macro-F1=0.7778, MAE=0.5955, QWK=0.8670, Recall@6-8=0.9000.
- `data_2021_val`: Macro-F1=0.2721, MAE=1.0532, QWK=0.5350, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.3175, MAE=1.2822, QWK=0.2087, Recall@6-8=0.0769.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019992, P75=0.003878, P90=0.008566, P95=0.110497, P99=0.432841, max=0.894318, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.016522, P75=0.003744, P90=0.007474, P95=0.085043, P99=0.379562, max=0.857132, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
