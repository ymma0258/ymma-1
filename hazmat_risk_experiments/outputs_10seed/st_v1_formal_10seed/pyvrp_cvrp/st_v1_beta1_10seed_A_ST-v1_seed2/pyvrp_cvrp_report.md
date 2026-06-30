# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.698254 | 0.000% | 0.272341 | 2.457054 | 0.145302 | 0.877596 | 90.238% |
| 1 | 0 | 158073.4 | 17.967% | 3.477257 | 60.024% | 0.091958 | 1.133147 | 0.281515 | 0.827169 | 80.233% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
