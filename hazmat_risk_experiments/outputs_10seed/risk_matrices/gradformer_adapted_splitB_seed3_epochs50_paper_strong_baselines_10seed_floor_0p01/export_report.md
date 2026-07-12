# Risk Matrix Export Report

## Model

- Model: `gradformer_adapted`; split: `B`; seed: `3`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gradformer_adapted_splitB_seed3_epochs50_paper_strong_baselines_10seed.pt`; selected epoch: `41`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5221, MAE=1.0596, QWK=0.5928, Recall@6-8=0.6250.
- `data_2021_train`: Macro-F1=0.7538, MAE=0.7825, QWK=0.7881, Recall@6-8=0.8000.
- `data_2021_val`: Macro-F1=0.2346, MAE=1.2954, QWK=0.2167, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2687, MAE=1.3745, QWK=0.1562, Recall@6-8=0.1154.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021732, P75=0.003884, P90=0.008571, P95=0.139991, P99=0.432821, max=0.921859, zero_ratio=0.016811.
- `data_2021`: edges=7647, mean=0.017817, P75=0.003703, P90=0.007768, P95=0.119672, P99=0.383276, max=0.857143, zero_ratio=0.008762.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
