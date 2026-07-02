# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 13.040232 | 0.000% | 0.256916 | 4.381839 | 0.237001 | 0.876822 | 91.035% |
| 1 | 0 | 178054.0 | 21.347% | 5.633450 | 56.799% | 0.082376 | 1.991059 | 0.299758 | 0.847949 | 82.752% |
| 2 | 0 | 195721.9 | 33.388% | 4.660804 | 64.258% | 0.065323 | 1.822257 | 0.325463 | 0.828021 | 79.165% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
