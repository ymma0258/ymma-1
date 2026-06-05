# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 8.526357 | 0.000% | 0.238717 | 3.052249 | 0.266011 | 0.862680 | 89.409% |
| 1 | 0 | 180497.8 | 23.180% | 4.548686 | 46.651% | 0.098458 | 1.694684 | 0.305688 | 0.826317 | 82.391% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
