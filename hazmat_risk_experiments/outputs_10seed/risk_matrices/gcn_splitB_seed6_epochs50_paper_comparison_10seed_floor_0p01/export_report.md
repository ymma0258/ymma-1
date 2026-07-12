# Risk Matrix Export Report

## Model

- Model: `gcn`; split: `B`; seed: `6`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gcn_splitB_seed6_epochs50_paper_comparison_10seed.pt`; selected epoch: `21`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3715, MAE=1.4097, QWK=0.4183, Recall@6-8=0.4000.
- `data_2021_train`: Macro-F1=0.5027, MAE=1.3221, QWK=0.3756, Recall@6-8=0.4500.
- `data_2021_val`: Macro-F1=0.2603, MAE=1.4155, QWK=0.4717, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2439, MAE=1.5643, QWK=0.2897, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.022034, P75=0.004049, P90=0.007880, P95=0.165314, P99=0.419613, max=0.830917, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.020588, P75=0.003857, P90=0.007228, P95=0.154656, P99=0.411225, max=0.835319, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
