# Risk Matrix Export Report

## Model

- Model: `sgformer_teg_concat`; split: `B`; seed: `5`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_teg_concat_splitB_seed5_epochs50_paper_teg_concat_fusions_10seed.pt`; selected epoch: `37`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3407, MAE=0.7466, QWK=0.7408, Recall@6-8=0.9750.
- `data_2021_train`: Macro-F1=0.4173, MAE=0.5606, QWK=0.8592, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.2892, MAE=1.3779, QWK=0.3169, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2747, MAE=1.1285, QWK=0.4919, Recall@6-8=0.5385.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020046, P75=0.004407, P90=0.008553, P95=0.090116, P99=0.433198, max=0.875994, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.016591, P75=0.004270, P90=0.008345, P95=0.078014, P99=0.418764, max=0.868258, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
