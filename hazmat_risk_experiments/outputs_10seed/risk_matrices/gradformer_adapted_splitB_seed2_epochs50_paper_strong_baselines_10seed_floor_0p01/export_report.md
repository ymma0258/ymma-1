# Risk Matrix Export Report

## Model

- Model: `gradformer_adapted`; split: `B`; seed: `2`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gradformer_adapted_splitB_seed2_epochs50_paper_strong_baselines_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5699, MAE=0.9876, QWK=0.6425, Recall@6-8=0.7000.
- `data_2021_train`: Macro-F1=0.7307, MAE=0.7263, QWK=0.7597, Recall@6-8=0.7500.
- `data_2021_val`: Macro-F1=0.2315, MAE=1.5657, QWK=-0.0834, Recall@6-8=0.0000.
- `data_2021_test`: Macro-F1=0.3047, MAE=1.2699, QWK=0.4052, Recall@6-8=0.3846.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019722, P75=0.003925, P90=0.008514, P95=0.113557, P99=0.429938, max=0.971871, zero_ratio=0.013933.
- `data_2021`: edges=7647, mean=0.019247, P75=0.003857, P90=0.008419, P95=0.116313, P99=0.432444, max=0.920138, zero_ratio=0.006539.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
