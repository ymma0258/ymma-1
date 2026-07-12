# Risk Matrix Export Report

## Model

- Model: `sgformer_adapted`; split: `B`; seed: `9`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_adapted_splitB_seed9_epochs50_paper_strong_baselines_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.7618, MAE=0.3818, QWK=0.8959, Recall@6-8=0.9500.
- `data_2021_train`: Macro-F1=0.8610, MAE=0.1978, QWK=0.9742, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.2614, MAE=1.3237, QWK=0.2255, Recall@6-8=0.2000.
- `data_2021_test`: Macro-F1=0.2907, MAE=1.2156, QWK=0.3301, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018385, P75=0.004593, P90=0.008570, P95=0.057438, P99=0.432836, max=0.997354, zero_ratio=0.000757.
- `data_2021`: edges=7647, mean=0.014124, P75=0.004293, P90=0.008566, P95=0.043554, P99=0.375048, max=0.932148, zero_ratio=0.000915.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
