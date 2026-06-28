# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 10.068832 | 0.000% | 0.301523 | 3.095250 | 0.187626 | 0.868262 | 90.418% |
| 1 | 0 | 180488.8 | 23.007% | 4.942657 | 50.911% | 0.140738 | 1.782511 | 0.272964 | 0.847397 | 85.102% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
