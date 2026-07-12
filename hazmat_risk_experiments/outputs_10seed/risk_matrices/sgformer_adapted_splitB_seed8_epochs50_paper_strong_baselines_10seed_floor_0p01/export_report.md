# Risk Matrix Export Report

## Model

- Model: `sgformer_adapted`; split: `B`; seed: `8`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_adapted_splitB_seed8_epochs50_paper_strong_baselines_10seed.pt`; selected epoch: `49`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.7465, MAE=0.4094, QWK=0.8722, Recall@6-8=0.9500.
- `data_2021_train`: Macro-F1=0.9791, MAE=0.1413, QWK=0.9870, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.3520, MAE=0.9670, QWK=0.5872, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.3152, MAE=1.1623, QWK=0.3763, Recall@6-8=0.4231.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.016424, P75=0.005833, P90=0.008515, P95=0.038777, P99=0.432346, max=0.998987, zero_ratio=0.001060.
- `data_2021`: edges=7647, mean=0.014693, P75=0.005791, P90=0.008525, P95=0.041009, P99=0.396766, max=0.858906, zero_ratio=0.001177.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
