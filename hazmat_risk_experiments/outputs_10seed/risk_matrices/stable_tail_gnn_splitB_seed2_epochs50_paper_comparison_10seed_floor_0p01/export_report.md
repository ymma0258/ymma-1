# Risk Matrix Export Report

## Model

- Model: `stable_tail_gnn`; split: `B`; seed: `2`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gnn_splitB_seed2_epochs50_paper_comparison_10seed.pt`; selected epoch: `47`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4774, MAE=0.8577, QWK=0.7065, Recall@6-8=0.8250.
- `data_2021_train`: Macro-F1=0.5518, MAE=0.6034, QWK=0.8122, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.2278, MAE=1.4797, QWK=0.0630, Recall@6-8=0.0000.
- `data_2021_test`: Macro-F1=0.2503, MAE=1.2049, QWK=0.2781, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019487, P75=0.004125, P90=0.008485, P95=0.085007, P99=0.431663, max=0.974663, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017272, P75=0.003884, P90=0.008358, P95=0.067927, P99=0.419567, max=0.946626, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
