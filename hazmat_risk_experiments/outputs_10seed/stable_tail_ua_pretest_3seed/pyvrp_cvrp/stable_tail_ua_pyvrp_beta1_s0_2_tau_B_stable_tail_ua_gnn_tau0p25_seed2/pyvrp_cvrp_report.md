# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 13.208931 | 0.000% | 0.217011 | 4.260989 | 0.209736 | 0.859307 | 90.108% |
| 1 | 0 | 181807.3 | 24.338% | 6.938623 | 47.470% | 0.122865 | 2.304128 | 0.282538 | 0.821868 | 83.369% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
