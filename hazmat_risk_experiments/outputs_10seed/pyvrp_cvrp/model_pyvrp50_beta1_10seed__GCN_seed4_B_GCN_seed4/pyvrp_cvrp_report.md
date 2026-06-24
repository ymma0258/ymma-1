# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.772931 | 0.000% | 0.256644 | 3.007084 | 0.249171 | 0.861805 | 89.101% |
| 1 | 0 | 180642.3 | 23.111% | 4.402333 | 49.819% | 0.093574 | 1.586136 | 0.287053 | 0.822655 | 81.768% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
