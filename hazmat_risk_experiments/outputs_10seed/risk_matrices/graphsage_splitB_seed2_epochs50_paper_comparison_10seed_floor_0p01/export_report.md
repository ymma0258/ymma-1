# Risk Matrix Export Report

## Model

- Model: `graphsage`; split: `B`; seed: `2`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_splitB_seed2_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5974, MAE=0.7341, QWK=0.7241, Recall@6-8=0.8750.
- `data_2021_train`: Macro-F1=0.7916, MAE=0.5168, QWK=0.8770, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.2894, MAE=1.4763, QWK=0.1393, Recall@6-8=0.2000.
- `data_2021_test`: Macro-F1=0.4314, MAE=1.1351, QWK=0.4824, Recall@6-8=0.5000.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020094, P75=0.004123, P90=0.008573, P95=0.096271, P99=0.432909, max=0.987553, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018706, P75=0.004326, P90=0.008568, P95=0.085037, P99=0.433145, max=0.958848, zero_ratio=0.000131.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
