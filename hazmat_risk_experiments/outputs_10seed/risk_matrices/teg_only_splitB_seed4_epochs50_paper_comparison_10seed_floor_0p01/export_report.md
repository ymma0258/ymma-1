# Risk Matrix Export Report

## Model

- Model: `teg_only`; split: `B`; seed: `4`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\teg_only_splitB_seed4_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5535, MAE=1.3684, QWK=0.6498, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.7895, MAE=1.0652, QWK=0.8464, Recall@6-8=0.9000.
- `data_2021_val`: Macro-F1=0.2497, MAE=1.6612, QWK=0.0051, Recall@6-8=0.0000.
- `data_2021_test`: Macro-F1=0.2286, MAE=1.7745, QWK=0.1542, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020036, P75=0.004827, P90=0.008557, P95=0.106245, P99=0.417510, max=0.879383, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017908, P75=0.004750, P90=0.008431, P95=0.094301, P99=0.392524, max=0.861051, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
