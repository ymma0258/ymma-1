# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 7.258409 | 0.000% | 0.219926 | 2.838030 | 0.304224 | 0.880829 | 90.007% |
| 1 | 0 | 175220.3 | 19.833% | 2.806524 | 61.334% | 0.058429 | 0.953788 | 0.260494 | 0.805542 | 77.373% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
