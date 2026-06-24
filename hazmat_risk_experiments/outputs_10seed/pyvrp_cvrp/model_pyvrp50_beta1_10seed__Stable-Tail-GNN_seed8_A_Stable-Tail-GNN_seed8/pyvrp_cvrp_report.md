# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.481776 | 0.000% | 0.219625 | 2.238807 | 0.159102 | 0.884400 | 90.223% |
| 1 | 0 | 157997.4 | 17.911% | 3.011525 | 59.749% | 0.074084 | 0.869025 | 0.199251 | 0.822900 | 80.016% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
