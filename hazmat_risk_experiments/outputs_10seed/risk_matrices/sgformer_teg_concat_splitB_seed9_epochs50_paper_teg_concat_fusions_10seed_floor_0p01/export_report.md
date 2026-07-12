# Risk Matrix Export Report

## Model

- Model: `sgformer_teg_concat`; split: `B`; seed: `9`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_teg_concat_splitB_seed9_epochs50_paper_teg_concat_fusions_10seed.pt`; selected epoch: `49`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5941, MAE=0.4532, QWK=0.8453, Recall@6-8=0.9750.
- `data_2021_train`: Macro-F1=0.7401, MAE=0.2787, QWK=0.9511, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.2470, MAE=1.3666, QWK=0.2553, Recall@6-8=0.2000.
- `data_2021_test`: Macro-F1=0.2739, MAE=1.2280, QWK=0.3853, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018197, P75=0.005272, P90=0.008646, P95=0.058743, P99=0.436642, max=0.911469, zero_ratio=0.000303.
- `data_2021`: edges=7647, mean=0.014215, P75=0.005019, P90=0.008456, P95=0.043361, P99=0.373530, max=0.901941, zero_ratio=0.000523.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
