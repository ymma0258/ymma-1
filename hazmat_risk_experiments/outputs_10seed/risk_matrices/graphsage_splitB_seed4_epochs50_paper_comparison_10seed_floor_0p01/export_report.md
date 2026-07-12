# Risk Matrix Export Report

## Model

- Model: `graphsage`; split: `B`; seed: `4`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_splitB_seed4_epochs50_paper_comparison_10seed.pt`; selected epoch: `47`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6292, MAE=0.7023, QWK=0.7854, Recall@6-8=0.9000.
- `data_2021_train`: Macro-F1=0.7546, MAE=0.5313, QWK=0.8542, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.2719, MAE=1.2017, QWK=0.2801, Recall@6-8=0.2000.
- `data_2021_test`: Macro-F1=0.2770, MAE=1.2159, QWK=0.3083, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019535, P75=0.003904, P90=0.008571, P95=0.104365, P99=0.433029, max=0.959090, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017527, P75=0.003711, P90=0.008571, P95=0.081959, P99=0.432848, max=0.938314, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
