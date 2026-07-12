# Risk Matrix Export Report

## Model

- Model: `gradformer_adapted`; split: `B`; seed: `6`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gradformer_adapted_splitB_seed6_epochs50_paper_strong_baselines_10seed.pt`; selected epoch: `18`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3274, MAE=1.4210, QWK=0.4309, Recall@6-8=0.4250.
- `data_2021_train`: Macro-F1=0.4536, MAE=1.3559, QWK=0.3368, Recall@6-8=0.4000.
- `data_2021_val`: Macro-F1=0.2754, MAE=1.3534, QWK=0.5601, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2014, MAE=1.5301, QWK=0.2604, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021779, P75=0.004019, P90=0.008198, P95=0.157005, P99=0.421269, max=0.845634, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.020456, P75=0.003944, P90=0.007664, P95=0.144458, P99=0.404453, max=0.814148, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
