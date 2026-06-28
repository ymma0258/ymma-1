# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 17.654361 | 0.000% | 0.135087 | 5.134263 | 0.182178 | 0.844014 | 89.705% |
| 1 | 0 | 187028.7 | 27.909% | 9.842131 | 44.251% | 0.074426 | 3.004105 | 0.227298 | 0.809789 | 82.586% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
