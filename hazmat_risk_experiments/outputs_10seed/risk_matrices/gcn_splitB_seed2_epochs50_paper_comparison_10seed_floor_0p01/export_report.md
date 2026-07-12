# Risk Matrix Export Report

## Model

- Model: `gcn`; split: `B`; seed: `2`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gcn_splitB_seed2_epochs50_paper_comparison_10seed.pt`; selected epoch: `45`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5782, MAE=0.9683, QWK=0.6041, Recall@6-8=0.7000.
- `data_2021_train`: Macro-F1=0.7434, MAE=0.6982, QWK=0.8002, Recall@6-8=0.8500.
- `data_2021_val`: Macro-F1=0.2469, MAE=1.5793, QWK=-0.0428, Recall@6-8=0.0000.
- `data_2021_test`: Macro-F1=0.3073, MAE=1.3296, QWK=0.2535, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021545, P75=0.004010, P90=0.008552, P95=0.131977, P99=0.432144, max=0.945984, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.019765, P75=0.003864, P90=0.008527, P95=0.119868, P99=0.430638, max=0.911198, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
