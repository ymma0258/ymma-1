# Risk Matrix Export Report

## Model

- Model: `gradformer_adapted`; split: `B`; seed: `4`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gradformer_adapted_splitB_seed4_epochs50_paper_strong_baselines_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6053, MAE=0.9815, QWK=0.6890, Recall@6-8=0.7500.
- `data_2021_train`: Macro-F1=0.8218, MAE=0.6397, QWK=0.7868, Recall@6-8=0.8500.
- `data_2021_val`: Macro-F1=0.3489, MAE=1.1784, QWK=0.5320, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.3028, MAE=1.3708, QWK=0.2574, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021260, P75=0.004341, P90=0.008476, P95=0.129077, P99=0.432854, max=0.966033, zero_ratio=0.012721.
- `data_2021`: edges=7647, mean=0.018454, P75=0.004050, P90=0.008562, P95=0.100388, P99=0.431308, max=0.864736, zero_ratio=0.005362.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
