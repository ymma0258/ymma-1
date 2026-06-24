# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.741809 | 0.000% | 0.252371 | 2.907900 | 0.225426 | 0.849658 | 87.914% |
| 1 | 0 | 180375.1 | 22.929% | 4.402443 | 49.639% | 0.116104 | 1.543493 | 0.287276 | 0.784904 | 78.763% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
