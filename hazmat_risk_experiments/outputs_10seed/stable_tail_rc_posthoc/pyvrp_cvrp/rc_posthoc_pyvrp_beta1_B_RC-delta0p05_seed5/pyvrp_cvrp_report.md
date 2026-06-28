# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.156126 | 0.000% | 0.223314 | 2.451486 | 0.233333 | 0.876785 | 89.502% |
| 1 | 0 | 174410.9 | 18.864% | 2.906345 | 59.387% | 0.066849 | 1.182643 | 0.344371 | 0.807199 | 77.637% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
