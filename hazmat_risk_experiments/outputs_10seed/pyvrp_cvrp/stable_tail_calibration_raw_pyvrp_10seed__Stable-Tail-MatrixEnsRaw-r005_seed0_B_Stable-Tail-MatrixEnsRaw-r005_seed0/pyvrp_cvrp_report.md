# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.3 | 0.000% | 7.178763 | 0.000% | 0.196814 | 2.419108 | 0.249691 | 0.876900 | 89.492% |
| 0.25 | 0 | 156712.4 | 6.464% | 6.123974 | 14.693% | 0.150403 | 1.979987 | 0.235160 | 0.873945 | 88.489% |
| 0.5 | 0 | 165038.7 | 12.121% | 4.254670 | 40.733% | 0.109280 | 1.407854 | 0.230640 | 0.850038 | 84.282% |
| 1 | 0 | 175398.0 | 19.158% | 2.837364 | 60.476% | 0.069995 | 1.050725 | 0.291728 | 0.803315 | 77.125% |
| 2 | 0 | 190210.9 | 29.222% | 2.247813 | 68.688% | 0.045422 | 0.818960 | 0.273211 | 0.772653 | 71.688% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
