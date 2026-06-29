# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.474608 | 0.000% | 0.242450 | 2.979681 | 0.273301 | 0.883457 | 90.209% |
| 1 | 0 | 172893.8 | 17.831% | 3.126641 | 63.106% | 0.062276 | 1.082182 | 0.296037 | 0.817119 | 77.332% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
