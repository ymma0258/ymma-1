# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 8.431310 | 0.000% | 0.227881 | 2.868769 | 0.236120 | 0.846715 | 87.400% |
| 1 | 0 | 175969.6 | 20.090% | 3.630981 | 56.935% | 0.072227 | 1.237468 | 0.234951 | 0.727902 | 72.194% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
