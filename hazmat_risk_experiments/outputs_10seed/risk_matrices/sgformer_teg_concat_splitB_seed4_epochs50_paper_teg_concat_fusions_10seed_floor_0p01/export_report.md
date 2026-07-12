# Risk Matrix Export Report

## Model

- Model: `sgformer_teg_concat`; split: `B`; seed: `4`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_teg_concat_splitB_seed4_epochs50_paper_teg_concat_fusions_10seed.pt`; selected epoch: `40`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3339, MAE=0.7462, QWK=0.6997, Recall@6-8=0.9250.
- `data_2021_train`: Macro-F1=0.4665, MAE=0.5638, QWK=0.8575, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.2997, MAE=1.1556, QWK=0.4722, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2032, MAE=1.4502, QWK=0.1587, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019378, P75=0.005123, P90=0.008718, P95=0.083505, P99=0.439145, max=0.872953, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017624, P75=0.004753, P90=0.008581, P95=0.074790, P99=0.433346, max=0.882407, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
