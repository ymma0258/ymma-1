# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 146531.2 | 0.000% | 7.561921 | 0.000% | 0.225242 | 2.582790 | 0.227575 | 0.823689 | 85.790% |
| 1 | 179360.2 | 22.404% | 3.490043 | 53.847% | 0.078904 | 1.077883 | 0.199833 | 0.699237 | 69.979% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
