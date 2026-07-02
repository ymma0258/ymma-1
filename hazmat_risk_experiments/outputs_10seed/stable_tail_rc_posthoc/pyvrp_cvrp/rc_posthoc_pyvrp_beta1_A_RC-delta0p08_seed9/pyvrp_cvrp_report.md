# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.228112 | 0.000% | 0.228822 | 2.262160 | 0.197846 | 0.876379 | 89.529% |
| 1 | 0 | 154240.4 | 15.107% | 2.302998 | 68.138% | 0.053411 | 0.800005 | 0.251471 | 0.763088 | 72.744% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
