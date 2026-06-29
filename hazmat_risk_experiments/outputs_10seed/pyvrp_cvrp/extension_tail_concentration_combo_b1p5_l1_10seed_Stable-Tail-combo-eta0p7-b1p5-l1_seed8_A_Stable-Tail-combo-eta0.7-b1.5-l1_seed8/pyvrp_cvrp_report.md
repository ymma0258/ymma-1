# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.481776 | 0.000% | 0.219625 | 2.238807 | 0.159102 | 0.884400 | 90.223% |
| 1.5 | 1 | 179342.3 | 33.840% | 2.053472 | 72.554% | 0.038345 | 0.889913 | 0.330240 | 0.764741 | 70.506% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
