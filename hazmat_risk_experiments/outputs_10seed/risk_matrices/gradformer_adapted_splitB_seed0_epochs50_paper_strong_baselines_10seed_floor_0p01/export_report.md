# Risk Matrix Export Report

## Model

- Model: `gradformer_adapted`; split: `B`; seed: `0`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gradformer_adapted_splitB_seed0_epochs50_paper_strong_baselines_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5787, MAE=0.9794, QWK=0.6921, Recall@6-8=0.7000.
- `data_2021_train`: Macro-F1=0.6230, MAE=0.7100, QWK=0.7270, Recall@6-8=0.7000.
- `data_2021_val`: Macro-F1=0.2635, MAE=1.2169, QWK=0.5205, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.3254, MAE=1.3780, QWK=0.2556, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020802, P75=0.004377, P90=0.008602, P95=0.119355, P99=0.434404, max=0.950670, zero_ratio=0.014236.
- `data_2021`: edges=7647, mean=0.017056, P75=0.004127, P90=0.008572, P95=0.101311, P99=0.384770, max=0.937055, zero_ratio=0.003531.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
