# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 16.604444 | 0.000% | 0.282637 | 4.523800 | 0.146166 | 0.819306 | 86.173% |
| 1 | 0 | 167487.0 | 24.993% | 7.603244 | 54.210% | 0.054752 | 2.789189 | 0.229501 | 0.741846 | 75.153% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
