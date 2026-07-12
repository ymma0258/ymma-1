# Risk Matrix Export Report

## Model

- Model: `sgformer_adapted`; split: `B`; seed: `1`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_adapted_splitB_seed1_epochs50_paper_strong_baselines_10seed.pt`; selected epoch: `49`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.7686, MAE=0.4036, QWK=0.8879, Recall@6-8=1.0000.
- `data_2021_train`: Macro-F1=0.8474, MAE=0.2014, QWK=0.9496, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.2540, MAE=1.2071, QWK=0.4701, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2893, MAE=1.2505, QWK=0.3975, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.017170, P75=0.004255, P90=0.008571, P95=0.055575, P99=0.432857, max=0.935061, zero_ratio=0.000151.
- `data_2021`: edges=7647, mean=0.016902, P75=0.004498, P90=0.008572, P95=0.053540, P99=0.434095, max=0.872652, zero_ratio=0.000131.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
