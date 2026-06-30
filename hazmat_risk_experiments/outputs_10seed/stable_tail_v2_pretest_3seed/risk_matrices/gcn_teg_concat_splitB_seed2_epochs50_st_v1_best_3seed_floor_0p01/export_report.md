# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `2`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\stable_tail_v2_pretest_3seed\models\checkpoints\gcn_teg_concat_splitB_seed2_epochs50_st_v1_best_3seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4640, MAE=0.8131, QWK=0.6651, Recall@6-8=0.7500.
- `data_2021_train`: Macro-F1=0.5837, MAE=0.5414, QWK=0.8354, Recall@6-8=0.9000.
- `data_2021_val`: Macro-F1=0.2562, MAE=1.4621, QWK=0.0418, Recall@6-8=0.0000.
- `data_2021_test`: Macro-F1=0.2668, MAE=1.1619, QWK=0.3163, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019276, P75=0.003967, P90=0.008462, P95=0.076420, P99=0.428990, max=0.965847, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017392, P75=0.003611, P90=0.008256, P95=0.067566, P99=0.411722, max=0.949660, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
