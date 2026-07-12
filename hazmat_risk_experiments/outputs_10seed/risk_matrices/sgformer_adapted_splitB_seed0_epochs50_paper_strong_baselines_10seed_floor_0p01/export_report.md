# Risk Matrix Export Report

## Model

- Model: `sgformer_adapted`; split: `B`; seed: `0`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_adapted_splitB_seed0_epochs50_paper_strong_baselines_10seed.pt`; selected epoch: `30`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3713, MAE=1.1206, QWK=0.5758, Recall@6-8=0.7000.
- `data_2021_train`: Macro-F1=0.4555, MAE=0.9872, QWK=0.6082, Recall@6-8=0.7000.
- `data_2021_val`: Macro-F1=0.3193, MAE=1.2939, QWK=0.5092, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2855, MAE=1.3126, QWK=0.4639, Recall@6-8=0.4231.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.023189, P75=0.004852, P90=0.008571, P95=0.135343, P99=0.449492, max=0.890370, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.020015, P75=0.004267, P90=0.008529, P95=0.136175, P99=0.418507, max=0.856744, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
