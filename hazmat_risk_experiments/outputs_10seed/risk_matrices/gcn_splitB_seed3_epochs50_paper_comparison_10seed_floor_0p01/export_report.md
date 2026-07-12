# Risk Matrix Export Report

## Model

- Model: `gcn`; split: `B`; seed: `3`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gcn_splitB_seed3_epochs50_paper_comparison_10seed.pt`; selected epoch: `46`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6011, MAE=0.8648, QWK=0.7190, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.7295, MAE=0.6288, QWK=0.8237, Recall@6-8=0.8500.
- `data_2021_val`: Macro-F1=0.2913, MAE=1.0794, QWK=0.6446, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2548, MAE=1.3347, QWK=0.1664, Recall@6-8=0.0769.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020680, P75=0.003608, P90=0.008571, P95=0.120160, P99=0.433027, max=0.869352, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017208, P75=0.003491, P90=0.007545, P95=0.105783, P99=0.376751, max=0.857059, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
