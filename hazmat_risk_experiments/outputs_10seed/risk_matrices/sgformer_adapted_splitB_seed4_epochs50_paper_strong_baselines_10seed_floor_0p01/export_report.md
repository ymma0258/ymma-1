# Risk Matrix Export Report

## Model

- Model: `sgformer_adapted`; split: `B`; seed: `4`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_adapted_splitB_seed4_epochs50_paper_strong_baselines_10seed.pt`; selected epoch: `48`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.7324, MAE=0.3770, QWK=0.8802, Recall@6-8=0.9750.
- `data_2021_train`: Macro-F1=0.9066, MAE=0.1576, QWK=0.9660, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.4335, MAE=0.9867, QWK=0.6806, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.3696, MAE=1.2983, QWK=0.3234, Recall@6-8=0.4231.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019367, P75=0.005398, P90=0.008576, P95=0.059456, P99=0.437530, max=0.979268, zero_ratio=0.001666.
- `data_2021`: edges=7647, mean=0.016853, P75=0.005286, P90=0.008596, P95=0.042008, P99=0.432924, max=0.978573, zero_ratio=0.001046.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
