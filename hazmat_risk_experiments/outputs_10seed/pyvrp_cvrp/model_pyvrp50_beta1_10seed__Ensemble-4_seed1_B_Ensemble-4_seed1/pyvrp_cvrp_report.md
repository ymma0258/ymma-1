# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.345586 | 0.000% | 0.257613 | 2.734707 | 0.218655 | 0.851272 | 88.060% |
| 1 | 0 | 175646.4 | 19.706% | 3.678219 | 55.926% | 0.084218 | 1.155379 | 0.240163 | 0.768790 | 76.209% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
