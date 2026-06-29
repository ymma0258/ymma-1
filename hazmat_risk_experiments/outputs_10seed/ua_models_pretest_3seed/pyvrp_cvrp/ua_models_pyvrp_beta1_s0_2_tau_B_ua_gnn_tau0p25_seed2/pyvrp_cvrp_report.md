# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 11.241175 | 0.000% | 0.295509 | 3.890977 | 0.243462 | 0.847246 | 89.372% |
| 1 | 0 | 182929.3 | 25.105% | 6.386676 | 43.185% | 0.139594 | 2.261200 | 0.277569 | 0.810058 | 83.041% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
