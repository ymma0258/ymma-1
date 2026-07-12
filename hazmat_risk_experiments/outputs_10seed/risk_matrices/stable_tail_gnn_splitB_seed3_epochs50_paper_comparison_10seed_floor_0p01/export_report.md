# Risk Matrix Export Report

## Model

- Model: `stable_tail_gnn`; split: `B`; seed: `3`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gnn_splitB_seed3_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6042, MAE=0.6850, QWK=0.7694, Recall@6-8=0.8000.
- `data_2021_train`: Macro-F1=0.7781, MAE=0.4285, QWK=0.8971, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.2978, MAE=1.0312, QWK=0.5312, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2611, MAE=1.2543, QWK=0.1842, Recall@6-8=0.0385.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.017844, P75=0.003692, P90=0.008502, P95=0.076608, P99=0.430083, max=0.898726, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.014597, P75=0.003357, P90=0.007890, P95=0.065751, P99=0.369917, max=0.856905, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
