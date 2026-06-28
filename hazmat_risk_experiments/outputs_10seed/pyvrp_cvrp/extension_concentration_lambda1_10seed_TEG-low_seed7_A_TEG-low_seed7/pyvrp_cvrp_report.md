# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 8.686336 | 0.000% | 0.252551 | 2.577769 | 0.147709 | 0.840437 | 87.132% |
| 1 | 0 | 161137.6 | 20.254% | 3.570777 | 58.892% | 0.087276 | 1.223560 | 0.280018 | 0.732697 | 72.470% |
| 1 | 1 | 172487.1 | 28.724% | 2.690853 | 69.022% | 0.045321 | 0.884542 | 0.263461 | 0.655708 | 62.997% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
