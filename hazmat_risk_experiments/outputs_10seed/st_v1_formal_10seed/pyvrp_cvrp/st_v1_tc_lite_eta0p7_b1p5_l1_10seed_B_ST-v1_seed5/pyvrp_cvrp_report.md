# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.035684 | 0.000% | 0.219598 | 2.415906 | 0.234400 | 0.876974 | 89.513% |
| 1.5 | 1 | 195400.4 | 33.169% | 2.295196 | 67.378% | 0.050805 | 0.864105 | 0.334529 | 0.778845 | 72.814% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
