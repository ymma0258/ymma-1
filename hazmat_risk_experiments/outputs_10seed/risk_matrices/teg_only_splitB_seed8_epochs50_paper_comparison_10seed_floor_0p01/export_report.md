# Risk Matrix Export Report

## Model

- Model: `teg_only`; split: `B`; seed: `8`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\teg_only_splitB_seed8_epochs50_paper_comparison_10seed.pt`; selected epoch: `46`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5174, MAE=1.3664, QWK=0.6156, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.7498, MAE=1.0313, QWK=0.7998, Recall@6-8=0.8000.
- `data_2021_val`: Macro-F1=0.3038, MAE=1.7474, QWK=0.4497, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2782, MAE=1.6297, QWK=0.3815, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020730, P75=0.004860, P90=0.008569, P95=0.118936, P99=0.432509, max=0.859097, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018445, P75=0.004816, P90=0.008539, P95=0.101086, P99=0.389389, max=0.856592, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
