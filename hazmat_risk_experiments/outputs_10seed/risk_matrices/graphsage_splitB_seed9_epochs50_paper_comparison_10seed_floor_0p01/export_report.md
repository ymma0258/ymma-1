# Risk Matrix Export Report

## Model

- Model: `graphsage`; split: `B`; seed: `9`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_splitB_seed9_epochs50_paper_comparison_10seed.pt`; selected epoch: `19`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3136, MAE=1.2671, QWK=0.4551, Recall@6-8=0.4250.
- `data_2021_train`: Macro-F1=0.4879, MAE=1.0988, QWK=0.6139, Recall@6-8=0.6500.
- `data_2021_val`: Macro-F1=0.2383, MAE=1.5470, QWK=0.4799, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2439, MAE=1.4937, QWK=0.1657, Recall@6-8=0.1154.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.022245, P75=0.003914, P90=0.008396, P95=0.158943, P99=0.423997, max=0.865589, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.020431, P75=0.003784, P90=0.008314, P95=0.143117, P99=0.419858, max=0.863522, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
