# Risk Matrix Export Report

## Model

- Model: `gcn`; split: `B`; seed: `4`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gcn_splitB_seed4_epochs50_paper_comparison_10seed.pt`; selected epoch: `43`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4456, MAE=0.9980, QWK=0.6100, Recall@6-8=0.6000.
- `data_2021_train`: Macro-F1=0.5919, MAE=0.8129, QWK=0.6641, Recall@6-8=0.7000.
- `data_2021_val`: Macro-F1=0.2344, MAE=1.3907, QWK=0.0946, Recall@6-8=0.0000.
- `data_2021_test`: Macro-F1=0.2697, MAE=1.3407, QWK=0.2381, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020591, P75=0.003747, P90=0.008563, P95=0.130297, P99=0.432411, max=0.885579, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018644, P75=0.003708, P90=0.008090, P95=0.119031, P99=0.432412, max=0.861920, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
