# Fixed-OD Multi-Model Path Comparison

| Risk source | Method | Hop inc. | Total risk red. | CVaR90 red. | MaxRisk red. | RE red. | Wilcoxon p(total) | Wilcoxon p(CVaR90) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| GCN | CVaR-risk | 10.486% | 83.720% | 89.637% | 90.159% | 91.873% | 1.23e-19 | 1.92e-20 |
| TEG-low | CVaR-risk | 11.365% | 80.416% | 89.258% | 90.304% | 91.661% | 1.26e-18 | 4.2e-21 |
| GCN+TEG-concat | CVaR-risk | 10.266% | 85.115% | 90.028% | 90.616% | 91.883% | 4.25e-20 | 1.31e-20 |
| Edge-GAT | CVaR-risk | 10.211% | 83.768% | 89.141% | 89.901% | 91.342% | 1.79e-19 | 2.8e-20 |
| Label-reference | CVaR-risk | 9.948% | 82.240% | 90.912% | 92.141% | 92.987% | 8.71e-19 | 1.28e-19 |