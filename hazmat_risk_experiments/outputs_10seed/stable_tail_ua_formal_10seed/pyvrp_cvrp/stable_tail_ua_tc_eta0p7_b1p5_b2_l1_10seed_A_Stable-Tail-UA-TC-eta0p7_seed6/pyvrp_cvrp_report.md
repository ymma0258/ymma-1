# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 12.505550 | 0.000% | 0.376147 | 3.393210 | 0.134154 | 0.845374 | 88.155% |
| 1.5 | 1 | 187160.7 | 39.675% | 3.597371 | 71.234% | 0.072697 | 1.792214 | 0.393064 | 0.663586 | 64.594% |
| 2 | 1 | 195320.1 | 45.764% | 3.594192 | 71.259% | 0.072692 | 1.791562 | 0.393289 | 0.663765 | 64.596% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
