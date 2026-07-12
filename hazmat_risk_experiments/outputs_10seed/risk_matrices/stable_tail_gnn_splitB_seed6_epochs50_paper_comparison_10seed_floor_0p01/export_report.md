# Risk Matrix Export Report

## Model

- Model: `stable_tail_gnn`; split: `B`; seed: `6`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gnn_splitB_seed6_epochs50_paper_comparison_10seed.pt`; selected epoch: `42`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4536, MAE=1.0273, QWK=0.5543, Recall@6-8=0.6250.
- `data_2021_train`: Macro-F1=0.6607, MAE=0.8668, QWK=0.7105, Recall@6-8=0.8500.
- `data_2021_val`: Macro-F1=0.2567, MAE=1.2769, QWK=0.3899, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2637, MAE=1.3037, QWK=0.3161, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019784, P75=0.004192, P90=0.008363, P95=0.096823, P99=0.422314, max=0.839073, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017062, P75=0.003986, P90=0.007201, P95=0.070163, P99=0.392082, max=0.848354, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
