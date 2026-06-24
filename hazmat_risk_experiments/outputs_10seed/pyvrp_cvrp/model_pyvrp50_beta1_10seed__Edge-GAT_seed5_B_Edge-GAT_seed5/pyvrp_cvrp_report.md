# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.354694 | 0.000% | 0.256946 | 2.761413 | 0.218976 | 0.853492 | 88.440% |
| 1 | 0 | 178871.2 | 21.904% | 4.132431 | 50.538% | 0.105364 | 1.355986 | 0.261510 | 0.802359 | 80.987% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
