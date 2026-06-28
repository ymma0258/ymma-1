# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 17.228102 | 0.000% | 0.157213 | 5.310498 | 0.195177 | 0.833982 | 88.590% |
| 1 | 0 | 187609.0 | 28.305% | 7.860279 | 54.375% | 0.067092 | 2.583125 | 0.281971 | 0.760324 | 76.525% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
