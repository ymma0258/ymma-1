# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 9.329840 | 0.000% | 0.297259 | 2.587242 | 0.150374 | 0.875799 | 90.203% |
| 1 | 0 | 160100.6 | 19.480% | 3.371225 | 63.866% | 0.074301 | 1.210181 | 0.318154 | 0.807043 | 78.411% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
