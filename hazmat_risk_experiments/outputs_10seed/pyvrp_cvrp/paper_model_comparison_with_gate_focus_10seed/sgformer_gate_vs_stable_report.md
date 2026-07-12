# SGFormer-TEG-Gate vs Stable-Tail GNN focused analysis

Positive `reference - target` means SGFormer-TEG-Gate is lower/better.

## AUBRC / Risk@20 / burden summary

| Model | Set | Common AUBRC | CVaR AUBRC | LoadRisk AUBRC | Risk@20 | CVaR@20 | LoadRisk@20 | Top10 share@20 |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| SGFormer-TEG-Gate | A | 4.4265 | 0.1171 | 2.2861 | 3.5075 | 0.0902 | 1.7388 | 76.77% |
| SGFormer-TEG-Gate | B | 5.5204 | 0.1425 | 2.7284 | 4.9264 | 0.1184 | 2.4733 | 81.38% |
| Stable-Tail GNN | A | 4.4074 | 0.1171 | 2.2956 | 3.2726 | 0.0814 | 1.6563 | 75.49% |
| Stable-Tail GNN | B | 5.5517 | 0.1426 | 2.7745 | 5.1154 | 0.1227 | 2.6069 | 82.13% |

## Paired significance: AUBRC

| Scope | Metric | Gate mean | Stable mean | Stable - Gate | Relative | 95% CI | Holm p | Sig |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Set A | common_risk_aubrc | 4.4265 | 4.4074 | -0.0192 | -0.44% | [-0.0965, 0.0549] | 1.0000 | False |
| Set B | common_risk_aubrc | 5.5204 | 5.5517 | 0.0313 | 0.56% | [-0.0796, 0.1218] | 1.0000 | False |
| Average(A,B) | common_risk_aubrc | 4.9735 | 4.9795 | 0.0061 | 0.12% | [-0.0689, 0.0757] | 1.0000 | False |
| Set A | cvar90_aubrc | 0.1171 | 0.1171 | -0.0000 | -0.01% | [-0.0034, 0.0033] | 1.0000 | False |
| Set B | cvar90_aubrc | 0.1425 | 0.1426 | 0.0001 | 0.09% | [-0.0031, 0.0029] | 1.0000 | False |
| Average(A,B) | cvar90_aubrc | 0.1298 | 0.1298 | 0.0001 | 0.05% | [-0.0025, 0.0027] | 1.0000 | False |
| Set A | load_risk_aubrc | 2.2861 | 2.2956 | 0.0095 | 0.42% | [-0.0396, 0.0634] | 0.9219 | False |
| Set B | load_risk_aubrc | 2.7284 | 2.7745 | 0.0460 | 1.66% | [-0.0010, 0.0864] | 0.1934 | False |
| Average(A,B) | load_risk_aubrc | 2.5073 | 2.5351 | 0.0278 | 1.10% | [-0.0086, 0.0662] | 0.4648 | False |

## Paired significance: B=20%

| Scope | Metric | Gate mean | Stable mean | Stable - Gate | Relative | 95% CI | Holm p | Sig |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Set A | common_global_risk_mean | 3.5075 | 3.2726 | -0.2349 | -7.18% | [-0.6054, 0.0488] | 1.0000 | False |
| Set B | common_global_risk_mean | 4.9264 | 5.1154 | 0.1890 | 3.70% | [-0.2309, 0.6834] | 1.0000 | False |
| Average(A,B) | common_global_risk_mean | 4.2169 | 4.1940 | -0.0229 | -0.55% | [-0.3146, 0.2944] | 1.0000 | False |
| Set A | common_global_cvar90_mean | 0.0902 | 0.0814 | -0.0088 | -10.75% | [-0.0225, 0.0021] | 1.0000 | False |
| Set B | common_global_cvar90_mean | 0.1184 | 0.1227 | 0.0043 | 3.48% | [-0.0076, 0.0178] | 1.0000 | False |
| Average(A,B) | common_global_cvar90_mean | 0.1043 | 0.1021 | -0.0022 | -2.19% | [-0.0116, 0.0068] | 1.0000 | False |
| Set A | load_global_risk_mean | 1.7388 | 1.6563 | -0.0824 | -4.98% | [-0.2733, 0.0716] | 1.0000 | False |
| Set B | load_global_risk_mean | 2.4733 | 2.6069 | 0.1336 | 5.12% | [-0.0823, 0.4028] | 0.3926 | False |
| Average(A,B) | load_global_risk_mean | 2.1060 | 2.1316 | 0.0256 | 1.20% | [-0.1090, 0.1791] | 1.0000 | False |
| Set A | common_top10_burden_share_mean | 0.7677 | 0.7549 | -0.0127 | -1.68% | [-0.0332, 0.0030] | 1.0000 | False |
| Set B | common_top10_burden_share_mean | 0.8138 | 0.8213 | 0.0075 | 0.91% | [-0.0075, 0.0263] | 1.0000 | False |
| Average(A,B) | common_top10_burden_share_mean | 0.7907 | 0.7881 | -0.0026 | -0.33% | [-0.0168, 0.0116] | 1.0000 | False |

## Complexity proxy

CPU benchmark uses the actual exported 2021 graph shape (5261 nodes, 7647 directed edges), synthetic node features with checkpoint in_dim, one CPU thread, and seed-0 checkpoints.

| Model | Params | Checkpoint MB | Forward ms | Train-step ms | Param ratio | Forward ratio | Step ratio | GPU memory |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| SGFormer-TEG-Gate | 104457 | 0.419 | 59.544 ± 21.094 | 135.923 ± 4.282 | 1.187 | 1.349 | 1.408 | not logged |
| Stable-Tail GNN | 88008 | 0.354 | 44.155 ± 1.725 | 96.508 ± 2.628 | 1.000 | 1.000 | 1.000 | not logged |

## Interpretation

- SGFormer-TEG-Gate is competitive and improves Set B Common/LoadRisk AUBRC relative to Stable-Tail GNN, but Holm-corrected paired tests do not show significance at 0.05.
- SGFormer-TEG-Gate has substantially more parameters and slower CPU forward/step proxy than Stable-Tail GNN, so Stable-Tail GNN remains the more efficient main model unless Set-B-specific performance is prioritized.
- GPU peak memory was not logged in the original run; reporting it requires a rerun with CUDA memory instrumentation.
