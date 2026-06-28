# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 6.282950 | 0.000% | 0.177174 | 1.869566 | 0.168377 | 0.875220 | 89.237% |
| 1 | 0 | 155535.2 | 16.073% | 2.202071 | 64.952% | 0.057789 | 0.828697 | 0.300631 | 0.770454 | 73.534% |
| 1 | 0.5 | 159951.1 | 19.369% | 1.686711 | 73.154% | 0.037788 | 0.560655 | 0.263093 | 0.721095 | 66.608% |
| 1 | 1 | 163238.4 | 21.822% | 1.639028 | 73.913% | 0.035980 | 0.533702 | 0.257307 | 0.714251 | 65.618% |
| 1 | 2 | 169709.6 | 26.651% | 1.604834 | 74.457% | 0.034652 | 0.536799 | 0.254456 | 0.713154 | 64.068% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
