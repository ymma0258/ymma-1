# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.439930 | 0.000% | 0.223720 | 2.517445 | 0.240042 | 0.826931 | 85.102% |
| 1 | 0 | 176224.2 | 20.100% | 3.512793 | 52.785% | 0.066383 | 1.133908 | 0.235404 | 0.706303 | 70.574% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
