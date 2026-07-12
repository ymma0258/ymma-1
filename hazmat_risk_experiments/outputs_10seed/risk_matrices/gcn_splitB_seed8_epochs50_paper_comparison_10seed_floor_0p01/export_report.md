# Risk Matrix Export Report

## Model

- Model: `gcn`; split: `B`; seed: `8`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gcn_splitB_seed8_epochs50_paper_comparison_10seed.pt`; selected epoch: `38`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5606, MAE=1.0665, QWK=0.6136, Recall@6-8=0.5750.
- `data_2021_train`: Macro-F1=0.6961, MAE=0.8538, QWK=0.7113, Recall@6-8=0.7000.
- `data_2021_val`: Macro-F1=0.3578, MAE=1.4698, QWK=0.4250, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2726, MAE=1.4075, QWK=0.2651, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020641, P75=0.003851, P90=0.008532, P95=0.134783, P99=0.431731, max=0.860085, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018315, P75=0.003687, P90=0.007879, P95=0.119454, P99=0.393279, max=0.858468, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
