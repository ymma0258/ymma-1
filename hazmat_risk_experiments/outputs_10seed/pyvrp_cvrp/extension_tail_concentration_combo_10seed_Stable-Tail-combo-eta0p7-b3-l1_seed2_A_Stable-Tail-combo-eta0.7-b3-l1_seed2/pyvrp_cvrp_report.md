# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 8.852208 | 0.000% | 0.281601 | 2.646365 | 0.161443 | 0.878704 | 90.379% |
| 3 | 1 | 203713.0 | 52.027% | 2.677333 | 69.755% | 0.054737 | 1.597681 | 0.454990 | 0.788452 | 73.730% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
