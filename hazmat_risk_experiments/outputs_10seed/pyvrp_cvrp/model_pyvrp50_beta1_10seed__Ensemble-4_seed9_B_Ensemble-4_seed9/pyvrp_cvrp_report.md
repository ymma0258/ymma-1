# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.046726 | 0.000% | 0.220795 | 2.760978 | 0.252562 | 0.849298 | 87.564% |
| 1 | 0 | 177115.5 | 20.708% | 3.762220 | 53.245% | 0.095399 | 1.382251 | 0.306948 | 0.773031 | 77.410% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
