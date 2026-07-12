# Risk Matrix Export Report

## Model

- Model: `sgformer_adapted`; split: `B`; seed: `7`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_adapted_splitB_seed7_epochs50_paper_strong_baselines_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.7760, MAE=0.4104, QWK=0.8460, Recall@6-8=0.9750.
- `data_2021_train`: Macro-F1=0.9914, MAE=0.1497, QWK=0.9943, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.3468, MAE=1.0206, QWK=0.5922, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.3454, MAE=1.3002, QWK=0.2868, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019703, P75=0.006780, P90=0.008571, P95=0.054128, P99=0.433933, max=0.999845, zero_ratio=0.001212.
- `data_2021`: edges=7647, mean=0.017216, P75=0.006287, P90=0.008571, P95=0.047606, P99=0.431117, max=0.893323, zero_ratio=0.001438.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
