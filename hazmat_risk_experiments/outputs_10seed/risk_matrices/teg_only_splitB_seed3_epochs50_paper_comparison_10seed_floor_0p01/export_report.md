# Risk Matrix Export Report

## Model

- Model: `teg_only`; split: `B`; seed: `3`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\teg_only_splitB_seed3_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5743, MAE=1.3030, QWK=0.6533, Recall@6-8=0.7500.
- `data_2021_train`: Macro-F1=0.7521, MAE=0.9711, QWK=0.8361, Recall@6-8=0.8500.
- `data_2021_val`: Macro-F1=0.2684, MAE=1.5610, QWK=0.3010, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2926, MAE=1.6503, QWK=0.2681, Recall@6-8=0.1923.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021356, P75=0.004767, P90=0.008569, P95=0.117954, P99=0.432712, max=0.901686, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017980, P75=0.004613, P90=0.008223, P95=0.104964, P99=0.383635, max=0.857022, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
