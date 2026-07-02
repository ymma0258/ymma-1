# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 7.634359 | 0.000% | 0.229405 | 2.385096 | 0.166464 | 0.885783 | 90.393% |
| 3 | 1 | 196831.1 | 46.892% | 1.942652 | 74.554% | 0.035197 | 0.908675 | 0.330646 | 0.751180 | 68.325% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
