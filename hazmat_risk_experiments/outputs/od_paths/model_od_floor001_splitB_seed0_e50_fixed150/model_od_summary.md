# Fixed-OD Multi-Model Path Comparison

| Risk source | Method | Hop inc. | Total risk red. | CVaR90 red. | MaxRisk red. | RE red. | Wilcoxon p(total) | Wilcoxon p(CVaR90) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| GCN | CVaR-risk | 10.486% | 83.720% | 89.637% | 90.159% | 91.873% | 1.23e-19 | 1.92e-20 |
| Weighted-GCN | CVaR-risk | 11.026% | 78.569% | 88.917% | 89.461% | 91.502% | 1.38e-18 | 1.31e-20 |
| Edge-GAT | CVaR-risk | 10.211% | 83.768% | 89.141% | 89.901% | 91.342% | 1.79e-19 | 2.8e-20 |
| TEG-GNN | CVaR-risk | 11.050% | 79.937% | 89.103% | 90.191% | 91.754% | 1.05e-18 | 1.31e-20 |
| Label-Oracle | CVaR-risk | 9.948% | 82.240% | 90.912% | 92.141% | 92.987% | 8.71e-19 | 1.28e-19 |