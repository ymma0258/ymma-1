# Fixed-OD Multi-Model Path Comparison

| Risk source | Method | Hop inc. | Total risk red. | CVaR90 red. | MaxRisk red. | RE red. | Wilcoxon p(total) | Wilcoxon p(CVaR90) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| GCN | CVaR-risk | 10.486% | 83.720% | 89.637% | 90.159% | 91.873% | 1.23e-19 | 1.92e-20 |
| TEG-default | CVaR-risk | 11.050% | 79.937% | 89.103% | 90.191% | 91.754% | 1.05e-18 | 1.31e-20 |
| TEG-low-tail | CVaR-risk | 11.365% | 80.416% | 89.258% | 90.304% | 91.661% | 1.26e-18 | 4.2e-21 |
| GCN+TEG-low | CVaR-risk | 11.176% | 82.385% | 89.338% | 90.054% | 91.801% | 1.29e-19 | 1.97e-21 |
| Ensemble-4 | CVaR-risk | 10.689% | 81.542% | 89.181% | 89.917% | 90.996% | 2.29e-19 | 1.92e-20 |
| Label-Oracle | CVaR-risk | 9.948% | 82.240% | 90.912% | 92.141% | 92.987% | 8.71e-19 | 1.28e-19 |