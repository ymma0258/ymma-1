# Risk Matrix Export Report

## Model

- Model: `gcn`; split: `B`; seed: `1`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gcn_splitB_seed1_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5899, MAE=0.8431, QWK=0.7034, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.7824, MAE=0.5996, QWK=0.8484, Recall@6-8=0.8500.
- `data_2021_val`: Macro-F1=0.3896, MAE=1.2456, QWK=0.5812, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.3300, MAE=1.3704, QWK=0.2891, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020379, P75=0.003803, P90=0.008568, P95=0.115796, P99=0.432701, max=0.891310, zero_ratio=0.001363.
- `data_2021`: edges=7647, mean=0.017346, P75=0.003575, P90=0.008319, P95=0.102738, P99=0.385834, max=0.855258, zero_ratio=0.001438.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
