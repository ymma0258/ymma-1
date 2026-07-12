# Risk Matrix Export Report

## Model

- Model: `sgformer_adapted`; split: `B`; seed: `2`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_adapted_splitB_seed2_epochs50_paper_strong_baselines_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.7276, MAE=0.4274, QWK=0.8548, Recall@6-8=0.9750.
- `data_2021_train`: Macro-F1=0.8516, MAE=0.2272, QWK=0.9188, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.2448, MAE=1.4863, QWK=0.0348, Recall@6-8=0.0000.
- `data_2021_test`: Macro-F1=0.3522, MAE=1.1372, QWK=0.4184, Recall@6-8=0.4231.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.017912, P75=0.005777, P90=0.008551, P95=0.037168, P99=0.432091, max=0.998865, zero_ratio=0.000454.
- `data_2021`: edges=7647, mean=0.016783, P75=0.005524, P90=0.008565, P95=0.034759, P99=0.432643, max=0.988966, zero_ratio=0.000523.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
