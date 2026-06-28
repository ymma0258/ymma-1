# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 9.326196 | 0.000% | 0.258139 | 3.149724 | 0.233913 | 0.874557 | 90.790% |
| 1 | 0 | 180357.0 | 23.346% | 4.732627 | 49.254% | 0.122250 | 1.602061 | 0.294287 | 0.845845 | 84.009% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
