# Risk Matrix Export Report

## Model

- Model: `graphsage`; split: `B`; seed: `3`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_splitB_seed3_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6518, MAE=0.6408, QWK=0.8011, Recall@6-8=0.9000.
- `data_2021_train`: Macro-F1=0.8465, MAE=0.4005, QWK=0.9294, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.2825, MAE=0.9080, QWK=0.5882, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2322, MAE=1.2722, QWK=0.2160, Recall@6-8=0.1154.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019395, P75=0.004499, P90=0.008572, P95=0.095255, P99=0.432879, max=0.900265, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.015794, P75=0.003901, P90=0.008536, P95=0.072308, P99=0.390144, max=0.889094, zero_ratio=0.000131.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
