# Risk Matrix Export Report

## Model

- Model: `gat`; split: `B`; seed: `5`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gat_splitB_seed5_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5539, MAE=0.7436, QWK=0.7518, Recall@6-8=0.8250.
- `data_2021_train`: Macro-F1=0.7660, MAE=0.4759, QWK=0.9306, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.2932, MAE=1.4153, QWK=0.2547, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2343, MAE=1.3046, QWK=0.2528, Recall@6-8=0.1923.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019844, P75=0.003608, P90=0.008456, P95=0.107559, P99=0.430232, max=0.870849, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.015573, P75=0.003437, P90=0.006952, P95=0.089909, P99=0.391859, max=0.842885, zero_ratio=0.000131.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
