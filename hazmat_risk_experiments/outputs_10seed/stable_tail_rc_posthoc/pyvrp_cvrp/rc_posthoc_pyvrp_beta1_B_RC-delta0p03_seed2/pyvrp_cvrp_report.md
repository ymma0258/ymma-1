# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 10.036561 | 0.000% | 0.311025 | 3.496235 | 0.249976 | 0.876903 | 90.765% |
| 1 | 0 | 178697.4 | 21.565% | 4.672199 | 53.448% | 0.122914 | 1.710985 | 0.282547 | 0.851460 | 83.844% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
