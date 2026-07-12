# Risk Matrix Export Report

## Model

- Model: `gat`; split: `B`; seed: `8`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gat_splitB_seed8_epochs50_paper_comparison_10seed.pt`; selected epoch: `40`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4813, MAE=1.0847, QWK=0.5820, Recall@6-8=0.5750.
- `data_2021_train`: Macro-F1=0.6759, MAE=0.8520, QWK=0.7586, Recall@6-8=0.7500.
- `data_2021_val`: Macro-F1=0.2782, MAE=1.5208, QWK=0.4622, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2364, MAE=1.3814, QWK=0.2436, Recall@6-8=0.1923.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019980, P75=0.003584, P90=0.007880, P95=0.141918, P99=0.407459, max=0.848199, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018055, P75=0.003624, P90=0.007541, P95=0.128270, P99=0.391619, max=0.848627, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
