# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 133997.4 | 0.000% | 8.096137 | 0.000% | 0.225235 | 2.608916 | 0.213907 | 0.842542 | 87.221% |
| 1 | 159881.8 | 19.317% | 3.293531 | 59.320% | 0.081298 | 1.148208 | 0.256267 | 0.726127 | 71.859% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
