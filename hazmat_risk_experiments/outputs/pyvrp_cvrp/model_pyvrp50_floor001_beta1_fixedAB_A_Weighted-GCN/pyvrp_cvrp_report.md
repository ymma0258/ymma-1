# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 133997.4 | 0.000% | 7.176161 | 0.000% | 0.217662 | 2.390349 | 0.222728 | 0.827960 | 85.657% |
| 1 | 157914.4 | 17.849% | 3.040409 | 57.632% | 0.072293 | 0.940554 | 0.217739 | 0.694960 | 68.937% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
