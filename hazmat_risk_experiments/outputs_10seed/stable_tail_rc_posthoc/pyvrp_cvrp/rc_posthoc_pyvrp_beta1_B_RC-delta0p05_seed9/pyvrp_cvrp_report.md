# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.017645 | 0.000% | 0.229534 | 2.728319 | 0.246039 | 0.880167 | 90.312% |
| 1 | 0 | 172318.2 | 17.438% | 2.575156 | 67.881% | 0.053727 | 0.869365 | 0.272007 | 0.787321 | 74.478% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
