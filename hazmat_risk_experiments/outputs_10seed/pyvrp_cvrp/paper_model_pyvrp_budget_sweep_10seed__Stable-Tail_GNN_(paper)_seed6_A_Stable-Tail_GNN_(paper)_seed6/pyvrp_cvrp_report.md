# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134065.0 | 0.000% | 7.706513 | 0.000% | 0.224989 | 2.174801 | 0.159284 | 0.866372 | 88.669% |
| 0.25 | 0 | 143445.0 | 6.997% | 4.893108 | 36.507% | 0.138592 | 1.740921 | 0.282547 | 0.841161 | 84.726% |
| 0.5 | 0 | 149829.0 | 11.758% | 4.040701 | 47.568% | 0.117933 | 1.482959 | 0.285467 | 0.817954 | 81.654% |
| 1 | 0 | 159443.8 | 18.930% | 2.881111 | 62.615% | 0.076012 | 0.968869 | 0.285404 | 0.775090 | 75.432% |
| 2 | 0 | 174074.9 | 29.844% | 2.288432 | 70.305% | 0.052516 | 0.823500 | 0.270178 | 0.728190 | 69.018% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
