# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 133997.4 | 0.000% | 7.728159 | 0.000% | 0.220355 | 2.529866 | 0.215567 | 0.845743 | 87.525% |
| 1 | 159260.8 | 18.854% | 2.976418 | 61.486% | 0.062455 | 1.131393 | 0.267445 | 0.722505 | 71.432% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
