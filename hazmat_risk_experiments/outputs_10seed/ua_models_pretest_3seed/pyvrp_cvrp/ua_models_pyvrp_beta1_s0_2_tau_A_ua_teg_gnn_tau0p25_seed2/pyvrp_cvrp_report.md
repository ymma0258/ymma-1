# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 7.615044 | 0.000% | 0.257881 | 1.946207 | 0.104809 | 0.833170 | 87.186% |
| 1 | 0 | 158041.3 | 17.944% | 3.958094 | 48.023% | 0.112951 | 1.098105 | 0.109857 | 0.780253 | 79.992% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
