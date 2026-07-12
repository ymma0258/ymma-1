# Risk Matrix Export Report

## Model

- Model: `sgformer_adapted`; split: `B`; seed: `5`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_adapted_splitB_seed5_epochs50_paper_strong_baselines_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.7414, MAE=0.4639, QWK=0.9007, Recall@6-8=1.0000.
- `data_2021_train`: Macro-F1=0.9534, MAE=0.2649, QWK=0.9793, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.3765, MAE=1.3880, QWK=0.3723, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.3620, MAE=1.1172, QWK=0.4871, Recall@6-8=0.5385.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.017740, P75=0.004152, P90=0.008571, P95=0.058024, P99=0.432857, max=0.970782, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.015528, P75=0.004273, P90=0.008571, P95=0.055094, P99=0.431592, max=0.988820, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
