# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.4 | 0.000% | 9.866223 | 0.000% | 0.289799 | 3.207581 | 0.212653 | 0.877207 | 90.361% |
| 1 | 0 | 177633.1 | 20.841% | 3.928199 | 60.185% | 0.082998 | 1.396573 | 0.261908 | 0.824936 | 79.586% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
