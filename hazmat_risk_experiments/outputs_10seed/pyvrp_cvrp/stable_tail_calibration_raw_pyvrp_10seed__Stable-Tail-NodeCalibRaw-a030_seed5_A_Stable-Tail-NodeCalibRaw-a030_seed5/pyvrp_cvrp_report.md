# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.8 | 0.000% | 7.514656 | 0.000% | 0.236282 | 2.111723 | 0.157515 | 0.871145 | 88.676% |
| 0.25 | 0 | 142399.7 | 6.059% | 5.518052 | 26.569% | 0.155593 | 1.749168 | 0.212247 | 0.864895 | 87.182% |
| 0.5 | 0 | 147860.4 | 10.126% | 3.497185 | 53.462% | 0.101811 | 1.415924 | 0.344794 | 0.822278 | 80.853% |
| 1 | 0 | 156132.1 | 16.287% | 2.589568 | 65.540% | 0.067856 | 0.944062 | 0.267353 | 0.778197 | 74.462% |
| 2 | 0 | 167265.8 | 24.579% | 1.904223 | 74.660% | 0.041578 | 0.656871 | 0.245197 | 0.720005 | 66.109% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
