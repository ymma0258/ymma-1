# Risk Matrix Export Report

## Model

- Model: `gat`; split: `B`; seed: `6`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gat_splitB_seed6_epochs50_paper_comparison_10seed.pt`; selected epoch: `31`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4306, MAE=1.1555, QWK=0.5418, Recall@6-8=0.5750.
- `data_2021_train`: Macro-F1=0.5811, MAE=0.9922, QWK=0.6352, Recall@6-8=0.7500.
- `data_2021_val`: Macro-F1=0.2888, MAE=1.4319, QWK=0.4495, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2446, MAE=1.4073, QWK=0.3053, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020903, P75=0.003949, P90=0.008236, P95=0.142154, P99=0.420050, max=0.837877, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.019175, P75=0.003849, P90=0.007260, P95=0.127712, P99=0.400763, max=0.847614, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
