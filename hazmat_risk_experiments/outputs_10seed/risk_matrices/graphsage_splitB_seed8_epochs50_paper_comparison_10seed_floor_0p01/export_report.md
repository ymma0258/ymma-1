# Risk Matrix Export Report

## Model

- Model: `graphsage`; split: `B`; seed: `8`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_splitB_seed8_epochs50_paper_comparison_10seed.pt`; selected epoch: `47`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6078, MAE=0.7677, QWK=0.7254, Recall@6-8=0.8250.
- `data_2021_train`: Macro-F1=0.8354, MAE=0.4852, QWK=0.8997, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.3805, MAE=1.2351, QWK=0.5169, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2908, MAE=1.2646, QWK=0.2962, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019917, P75=0.004407, P90=0.008560, P95=0.096453, P99=0.432270, max=0.958162, zero_ratio=0.000151.
- `data_2021`: edges=7647, mean=0.017035, P75=0.004038, P90=0.008431, P95=0.086279, P99=0.406808, max=0.856647, zero_ratio=0.001177.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
