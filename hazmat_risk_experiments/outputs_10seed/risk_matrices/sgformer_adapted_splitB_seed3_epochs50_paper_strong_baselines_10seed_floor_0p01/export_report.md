# Risk Matrix Export Report

## Model

- Model: `sgformer_adapted`; split: `B`; seed: `3`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_adapted_splitB_seed3_epochs50_paper_strong_baselines_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.8172, MAE=0.3185, QWK=0.9269, Recall@6-8=0.9750.
- `data_2021_train`: Macro-F1=0.9969, MAE=0.1180, QWK=0.9993, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.2463, MAE=0.9153, QWK=0.5636, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.3203, MAE=1.2045, QWK=0.2803, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.016857, P75=0.005630, P90=0.008571, P95=0.039541, P99=0.432826, max=0.969423, zero_ratio=0.001817.
- `data_2021`: edges=7647, mean=0.012665, P75=0.004950, P90=0.008251, P95=0.027967, P99=0.357462, max=0.857019, zero_ratio=0.002092.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
