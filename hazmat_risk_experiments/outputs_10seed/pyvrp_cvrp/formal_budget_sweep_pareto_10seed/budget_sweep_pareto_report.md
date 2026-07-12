# Budget Sweep and Pareto Pool Evaluation

## B-sweep summary

| Model | Set A Win Rate | Set B Win Rate | Mean AUBRC | Average Risk@B |
|---|---:|---:|---:|---:|
| GCN | 28.6% | 14.3% | 1.24990 | 4.3498 |
| Stable-Tail-GNN | 71.4% | 42.9% | 1.18931 | 4.1511 |
| TEG-low | 0.0% | 42.9% | 1.23878 | 4.3223 |

## Budget-free J selection

J = D_norm + CommonRisk_norm + 2 CVaR90_norm + LoadRisk_norm + 0.5 Top10Share_norm.

| Model | Set | CostInc | CommonRisk | CVaR90 | LoadRisk | Top10Share |
|---|---|---:|---:|---:|---:|---:|
| GCN | A | 33.04% | 2.3601 | 0.04219 | 1.1735 | 65.95% |
| GCN | B | 36.94% | 3.1292 | 0.06865 | 1.4858 | 72.17% |
| Stable-Tail-GNN | A | 27.57% | 2.5562 | 0.04680 | 1.2318 | 68.65% |
| Stable-Tail-GNN | B | 30.20% | 3.2910 | 0.07412 | 1.5601 | 73.45% |
| TEG-low | A | 32.74% | 2.4338 | 0.04550 | 1.2159 | 66.77% |
| TEG-low | B | 34.34% | 3.1511 | 0.06842 | 1.4645 | 72.29% |

## Five-objective Pareto routes

| Model | Set | Unique routes | Pareto routes | Share | CommonRisk | CVaR90 | LoadRisk |
|---|---|---:|---:|---:|---:|---:|---:|
| GCN | A | 510 | 76 | 14.9% | 3.4283 | 0.08446 | 1.6371 |
| GCN | B | 510 | 93 | 18.2% | 3.8582 | 0.08994 | 1.7886 |
| Stable-Tail-GNN | A | 510 | 80 | 15.7% | 3.2851 | 0.07643 | 1.5959 |
| Stable-Tail-GNN | B | 510 | 67 | 13.1% | 3.7661 | 0.08690 | 1.7568 |
| TEG-low | A | 511 | 65 | 12.7% | 3.0381 | 0.06814 | 1.5032 |
| TEG-low | B | 511 | 75 | 14.7% | 3.6713 | 0.08320 | 1.7049 |

## Risk-cost AUC (10%-40%)

| Model | Set | Metric | AUC | Normalized AUC |
|---|---|---|---:|---:|
| GCN | A | CommonRisk | 1.038320 | 3.46107 |
| GCN | B | CommonRisk | 1.456225 | 4.85408 |
| Stable-Tail-GNN | A | CommonRisk | 0.994635 | 3.31545 |
| Stable-Tail-GNN | B | CommonRisk | 1.354318 | 4.51439 |
| TEG-low | A | CommonRisk | 1.070708 | 3.56903 |
| TEG-low | B | CommonRisk | 1.394644 | 4.64881 |
| GCN | A | CVaR90 | 0.025189 | 0.08396 |
| GCN | B | CVaR90 | 0.036787 | 0.12262 |
| Stable-Tail-GNN | A | CVaR90 | 0.023293 | 0.07764 |
| Stable-Tail-GNN | B | CVaR90 | 0.033228 | 0.11076 |
| TEG-low | A | CVaR90 | 0.026326 | 0.08775 |
| TEG-low | B | CVaR90 | 0.034451 | 0.11484 |
| GCN | A | LoadRisk | 0.525790 | 1.75263 |
| GCN | B | LoadRisk | 0.704470 | 2.34823 |
| Stable-Tail-GNN | A | LoadRisk | 0.490830 | 1.63610 |
| Stable-Tail-GNN | B | LoadRisk | 0.652806 | 2.17602 |
| TEG-low | A | LoadRisk | 0.542495 | 1.80832 |
| TEG-low | B | LoadRisk | 0.678656 | 2.26219 |

注：三模型使用相同 beta 候选网格和 common evaluator。Risk@B 与 AUC 均先在每个 model_seed × solver_seed 内选择，再对 10 个 solver seeds 和 10 个 model seeds 分层聚合。
