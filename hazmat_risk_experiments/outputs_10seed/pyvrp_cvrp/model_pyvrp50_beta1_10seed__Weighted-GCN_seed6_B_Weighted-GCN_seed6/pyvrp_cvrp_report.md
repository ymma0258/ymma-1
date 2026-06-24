# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.310693 | 0.000% | 0.249667 | 2.668586 | 0.205363 | 0.836745 | 86.410% |
| 1 | 0 | 179866.3 | 22.582% | 4.550277 | 45.248% | 0.104442 | 1.448670 | 0.239177 | 0.765741 | 76.914% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
