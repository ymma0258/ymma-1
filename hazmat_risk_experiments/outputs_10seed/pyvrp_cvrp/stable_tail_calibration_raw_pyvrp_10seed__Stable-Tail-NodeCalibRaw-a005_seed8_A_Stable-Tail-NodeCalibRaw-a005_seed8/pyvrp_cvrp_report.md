# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134398.0 | 0.000% | 8.285031 | 0.000% | 0.263821 | 2.489190 | 0.172230 | 0.868427 | 88.268% |
| 0.25 | 0 | 143074.6 | 6.456% | 5.534147 | 33.203% | 0.160089 | 1.699334 | 0.212288 | 0.858771 | 87.018% |
| 0.5 | 0 | 150075.8 | 11.665% | 3.623407 | 56.266% | 0.102289 | 1.031501 | 0.165525 | 0.811494 | 80.375% |
| 1 | 0 | 158790.7 | 18.150% | 2.827698 | 65.870% | 0.069280 | 0.784822 | 0.164541 | 0.783649 | 75.910% |
| 2 | 0 | 173968.8 | 29.443% | 2.242207 | 72.937% | 0.043183 | 0.645951 | 0.180795 | 0.745381 | 69.908% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
