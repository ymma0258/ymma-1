# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `1`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\stable_tail_v2_pretest_3seed\models\checkpoints\gcn_teg_concat_splitB_seed1_epochs50_st_v1_3seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4277, MAE=0.7175, QWK=0.7165, Recall@6-8=0.8000.
- `data_2021_train`: Macro-F1=0.4648, MAE=0.6218, QWK=0.7184, Recall@6-8=0.8000.
- `data_2021_test`: Macro-F1=0.2841, MAE=1.2205, QWK=0.3234, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019377, P75=0.003803, P90=0.008566, P95=0.078095, P99=0.437030, max=0.895985, zero_ratio=0.000606.
- `data_2021`: edges=7647, mean=0.016397, P75=0.003443, P90=0.008491, P95=0.059453, P99=0.428811, max=0.868153, zero_ratio=0.001308.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
