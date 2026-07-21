# Risk Matrix Export Report

## Model

- Model: `stable_tail_gate`; split: `B`; seed: `5`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gate_splitB_seed5_epochs50_paper_stable_tail_gate_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5640, MAE=0.8587, QWK=0.6989, Recall@6-8=0.7750.
- `data_2021_train`: Macro-F1=0.8313, MAE=0.6416, QWK=0.8858, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.2549, MAE=1.4717, QWK=0.1762, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.3192, MAE=1.2250, QWK=0.3911, Recall@6-8=0.3846.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020751, P75=0.003964, P90=0.008612, P95=0.109194, P99=0.434921, max=0.879206, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.016479, P75=0.003594, P90=0.007646, P95=0.087480, P99=0.386141, max=0.853314, zero_ratio=0.001177.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
