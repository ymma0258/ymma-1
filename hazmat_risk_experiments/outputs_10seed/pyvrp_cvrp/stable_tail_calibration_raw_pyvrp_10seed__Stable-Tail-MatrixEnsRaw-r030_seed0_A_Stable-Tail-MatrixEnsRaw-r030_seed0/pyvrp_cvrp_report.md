# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.8 | 0.000% | 5.352940 | 0.000% | 0.161172 | 1.705343 | 0.219408 | 0.883744 | 90.294% |
| 0.25 | 0 | 142292.0 | 6.137% | 3.498967 | 34.635% | 0.105666 | 1.196705 | 0.244759 | 0.866849 | 87.160% |
| 0.5 | 0 | 147992.0 | 10.388% | 2.617587 | 51.100% | 0.077880 | 0.988942 | 0.294033 | 0.839543 | 83.378% |
| 1 | 0 | 155539.6 | 16.018% | 1.748978 | 67.327% | 0.042551 | 0.691225 | 0.282078 | 0.786328 | 75.492% |
| 2 | 0 | 167283.0 | 24.778% | 1.293135 | 75.843% | 0.023212 | 0.413870 | 0.225534 | 0.732222 | 67.028% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
