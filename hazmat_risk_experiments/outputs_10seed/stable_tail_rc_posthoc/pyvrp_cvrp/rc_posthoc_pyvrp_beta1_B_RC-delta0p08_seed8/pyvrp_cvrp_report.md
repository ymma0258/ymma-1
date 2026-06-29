# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.609167 | 0.000% | 0.223309 | 2.414967 | 0.192535 | 0.877974 | 89.064% |
| 1 | 0 | 175516.2 | 19.618% | 3.377508 | 55.613% | 0.087028 | 1.332010 | 0.320894 | 0.821257 | 79.396% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
