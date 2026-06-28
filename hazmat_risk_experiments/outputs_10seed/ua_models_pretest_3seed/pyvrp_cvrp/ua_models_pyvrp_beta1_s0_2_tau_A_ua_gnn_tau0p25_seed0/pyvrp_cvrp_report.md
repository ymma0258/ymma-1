# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 10.019146 | 0.000% | 0.265131 | 3.004464 | 0.149083 | 0.848296 | 88.264% |
| 1 | 0 | 159672.7 | 19.161% | 4.077218 | 59.306% | 0.086285 | 1.414014 | 0.232540 | 0.769664 | 77.236% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
