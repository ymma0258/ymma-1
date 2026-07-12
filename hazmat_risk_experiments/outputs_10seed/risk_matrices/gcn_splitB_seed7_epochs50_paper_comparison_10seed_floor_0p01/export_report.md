# Risk Matrix Export Report

## Model

- Model: `gcn`; split: `B`; seed: `7`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gcn_splitB_seed7_epochs50_paper_comparison_10seed.pt`; selected epoch: `46`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4886, MAE=1.0385, QWK=0.6405, Recall@6-8=0.6750.
- `data_2021_train`: Macro-F1=0.6645, MAE=0.7377, QWK=0.8323, Recall@6-8=0.8500.
- `data_2021_val`: Macro-F1=0.2149, MAE=1.1444, QWK=0.3857, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2987, MAE=1.4823, QWK=0.2112, Recall@6-8=0.1923.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021506, P75=0.003949, P90=0.008428, P95=0.138268, P99=0.434362, max=0.860124, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.019097, P75=0.003902, P90=0.008520, P95=0.117847, P99=0.430816, max=0.856823, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
