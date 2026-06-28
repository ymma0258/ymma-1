# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 10.261333 | 0.000% | 0.209177 | 3.260987 | 0.217861 | 0.880283 | 90.001% |
| 1 | 0 | 156910.7 | 17.100% | 3.347351 | 67.379% | 0.052954 | 1.304364 | 0.308762 | 0.793661 | 75.283% |
| 2 | 0 | 168014.8 | 25.387% | 2.317154 | 77.419% | 0.031250 | 0.685251 | 0.197282 | 0.708441 | 63.120% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
