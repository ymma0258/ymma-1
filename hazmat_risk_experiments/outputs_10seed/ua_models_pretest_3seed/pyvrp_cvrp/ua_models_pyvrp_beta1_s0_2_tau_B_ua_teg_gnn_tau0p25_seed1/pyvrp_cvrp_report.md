# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 12.484170 | 0.000% | 0.223749 | 4.041008 | 0.215749 | 0.865689 | 90.583% |
| 1 | 0 | 180043.0 | 23.131% | 6.159277 | 50.663% | 0.115368 | 2.187255 | 0.288367 | 0.825446 | 82.780% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
