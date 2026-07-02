# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `6`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\st_v1_formal_10seed\models\checkpoints\gcn_teg_concat_splitB_seed6_epochs50_st_v1_formal_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4529, MAE=0.8532, QWK=0.6023, Recall@6-8=0.6500.
- `data_2021_train`: Macro-F1=0.6301, MAE=0.7276, QWK=0.6933, Recall@6-8=0.8000.
- `data_2021_test`: Macro-F1=0.2565, MAE=1.2200, QWK=0.3425, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019096, P75=0.003988, P90=0.008226, P95=0.073192, P99=0.422312, max=0.844502, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.016727, P75=0.004008, P90=0.007592, P95=0.058614, P99=0.414436, max=0.845283, zero_ratio=0.000785.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
