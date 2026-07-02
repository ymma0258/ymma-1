# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 6.152819 | 0.000% | 0.175570 | 1.791873 | 0.170529 | 0.873796 | 89.035% |
| 1 | 0 | 155572.1 | 16.101% | 2.186110 | 64.470% | 0.057180 | 0.819288 | 0.296969 | 0.770235 | 73.476% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
