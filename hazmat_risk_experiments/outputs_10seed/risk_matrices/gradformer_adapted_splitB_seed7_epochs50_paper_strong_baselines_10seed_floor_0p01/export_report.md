# Risk Matrix Export Report

## Model

- Model: `gradformer_adapted`; split: `B`; seed: `7`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gradformer_adapted_splitB_seed7_epochs50_paper_strong_baselines_10seed.pt`; selected epoch: `23`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3508, MAE=1.3577, QWK=0.4482, Recall@6-8=0.4000.
- `data_2021_train`: Macro-F1=0.4956, MAE=1.0992, QWK=0.5269, Recall@6-8=0.5000.
- `data_2021_val`: Macro-F1=0.1933, MAE=1.3570, QWK=0.5168, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.1926, MAE=1.6408, QWK=0.1499, Recall@6-8=0.1538.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021428, P75=0.003826, P90=0.008187, P95=0.153761, P99=0.424173, max=0.922616, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.019571, P75=0.003965, P90=0.007165, P95=0.142935, P99=0.379597, max=0.850569, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
