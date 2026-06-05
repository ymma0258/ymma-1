# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 7.032832 | 0.000% | 0.198435 | 2.241083 | 0.200711 | 0.864061 | 88.376% |
| 1 | 0 | 157110.4 | 17.249% | 2.974202 | 57.710% | 0.077705 | 0.923159 | 0.214100 | 0.787886 | 77.080% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
