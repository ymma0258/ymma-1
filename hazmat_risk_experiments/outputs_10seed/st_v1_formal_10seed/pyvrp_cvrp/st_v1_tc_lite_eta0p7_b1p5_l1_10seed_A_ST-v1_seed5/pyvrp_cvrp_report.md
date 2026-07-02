# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 6.152819 | 0.000% | 0.175570 | 1.791873 | 0.170529 | 0.873796 | 89.035% |
| 1.5 | 1 | 170810.4 | 27.473% | 1.604874 | 73.916% | 0.034550 | 0.523400 | 0.247666 | 0.712468 | 64.243% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
