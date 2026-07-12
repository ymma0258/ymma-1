# Risk Matrix Export Report

## Model

- Model: `gat`; split: `B`; seed: `9`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gat_splitB_seed9_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5676, MAE=0.9096, QWK=0.6711, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.7719, MAE=0.6057, QWK=0.8519, Recall@6-8=0.9000.
- `data_2021_val`: Macro-F1=0.2873, MAE=1.4863, QWK=0.3160, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2173, MAE=1.5044, QWK=0.1108, Recall@6-8=0.1154.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020759, P75=0.003870, P90=0.008381, P95=0.133752, P99=0.432694, max=0.891473, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018860, P75=0.003934, P90=0.007677, P95=0.118233, P99=0.409821, max=0.858501, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
