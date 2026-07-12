# Risk Matrix Export Report

## Model

- Model: `sgformer_teg_concat`; split: `B`; seed: `6`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_teg_concat_splitB_seed6_epochs50_paper_teg_concat_fusions_10seed.pt`; selected epoch: `30`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3790, MAE=1.0579, QWK=0.5294, Recall@6-8=0.6250.
- `data_2021_train`: Macro-F1=0.5134, MAE=0.8947, QWK=0.6309, Recall@6-8=0.7500.
- `data_2021_val`: Macro-F1=0.3600, MAE=1.4453, QWK=0.5147, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.3321, MAE=1.3611, QWK=0.3564, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020756, P75=0.004583, P90=0.007904, P95=0.121179, P99=0.422140, max=0.835921, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017827, P75=0.004203, P90=0.006358, P95=0.101723, P99=0.379240, max=0.850729, zero_ratio=0.000131.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
