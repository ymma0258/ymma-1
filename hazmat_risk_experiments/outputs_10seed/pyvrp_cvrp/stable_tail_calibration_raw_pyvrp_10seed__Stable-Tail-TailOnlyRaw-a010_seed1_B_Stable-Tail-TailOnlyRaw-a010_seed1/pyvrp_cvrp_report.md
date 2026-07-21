# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 10.188720 | 0.000% | 0.323387 | 3.538137 | 0.252431 | 0.875546 | 90.309% |
| 0.25 | 0 | 156098.5 | 6.191% | 8.344853 | 18.097% | 0.234605 | 2.802280 | 0.232117 | 0.872006 | 89.130% |
| 0.5 | 0 | 164766.4 | 12.088% | 6.981663 | 31.477% | 0.188816 | 2.249778 | 0.233526 | 0.862805 | 87.339% |
| 1 | 0 | 174395.9 | 18.639% | 4.061222 | 60.140% | 0.091118 | 1.364980 | 0.260783 | 0.820529 | 80.026% |
| 2 | 0 | 188412.3 | 28.174% | 3.427948 | 66.355% | 0.069404 | 1.171654 | 0.263449 | 0.802980 | 76.873% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
