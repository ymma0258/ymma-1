# Risk Matrix Export Report

## Model

- Model: `gat`; split: `B`; seed: `0`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gat_splitB_seed0_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6300, MAE=0.8516, QWK=0.6845, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.7816, MAE=0.5261, QWK=0.8399, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.4472, MAE=1.1373, QWK=0.6925, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.3515, MAE=1.3326, QWK=0.2073, Recall@6-8=0.1923.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019295, P75=0.003967, P90=0.008484, P95=0.117623, P99=0.425930, max=0.891576, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.015921, P75=0.003547, P90=0.007142, P95=0.091112, P99=0.360695, max=0.855304, zero_ratio=0.000785.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
