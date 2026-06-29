# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.141328 | 0.000% | 0.289023 | 2.794505 | 0.181699 | 0.865393 | 89.883% |
| 1 | 0 | 181394.5 | 23.624% | 4.118556 | 54.946% | 0.107507 | 1.385467 | 0.257772 | 0.834459 | 82.713% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
