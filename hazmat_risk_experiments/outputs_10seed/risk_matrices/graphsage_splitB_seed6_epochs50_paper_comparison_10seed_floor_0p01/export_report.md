# Risk Matrix Export Report

## Model

- Model: `graphsage`; split: `B`; seed: `6`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_splitB_seed6_epochs50_paper_comparison_10seed.pt`; selected epoch: `18`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3555, MAE=1.2894, QWK=0.4813, Recall@6-8=0.5500.
- `data_2021_train`: Macro-F1=0.4745, MAE=1.1878, QWK=0.4686, Recall@6-8=0.6000.
- `data_2021_val`: Macro-F1=0.2591, MAE=1.3729, QWK=0.4824, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2414, MAE=1.4682, QWK=0.2988, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.022709, P75=0.004403, P90=0.008287, P95=0.153525, P99=0.424804, max=0.841197, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.020216, P75=0.004017, P90=0.007067, P95=0.132056, P99=0.419094, max=0.841291, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
