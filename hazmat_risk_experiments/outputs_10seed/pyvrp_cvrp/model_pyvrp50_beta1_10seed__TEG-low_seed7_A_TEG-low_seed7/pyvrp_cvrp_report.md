# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.522296 | 0.000% | 0.241884 | 2.464672 | 0.144134 | 0.838407 | 86.896% |
| 1 | 0 | 161137.6 | 20.254% | 3.570777 | 58.101% | 0.087276 | 1.223560 | 0.280018 | 0.732697 | 72.470% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
