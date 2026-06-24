# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 9.261776 | 0.000% | 0.267855 | 2.627362 | 0.138775 | 0.857044 | 89.183% |
| 1 | 0 | 160937.3 | 20.105% | 3.905087 | 57.837% | 0.105940 | 1.338075 | 0.244476 | 0.786946 | 78.431% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
