# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.8 | 0.000% | 7.299589 | 0.000% | 0.218739 | 2.293116 | 0.197672 | 0.879184 | 89.686% |
| 1 | 0 | 154883.0 | 15.528% | 2.443706 | 66.523% | 0.061250 | 0.810802 | 0.247975 | 0.774290 | 74.831% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
