# Risk Matrix Export Report

## Model

- Model: `gat`; split: `B`; seed: `1`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gat_splitB_seed1_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6390, MAE=0.8466, QWK=0.7365, Recall@6-8=0.8250.
- `data_2021_train`: Macro-F1=0.7579, MAE=0.6043, QWK=0.8410, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.3016, MAE=1.3121, QWK=0.2132, Recall@6-8=0.2000.
- `data_2021_test`: Macro-F1=0.2298, MAE=1.4096, QWK=0.2169, Recall@6-8=0.1923.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020604, P75=0.003997, P90=0.008469, P95=0.131262, P99=0.427698, max=0.875844, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.016152, P75=0.003449, P90=0.007417, P95=0.092754, P99=0.352267, max=0.970423, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
