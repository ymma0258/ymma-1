# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.033840 | 0.000% | 0.244086 | 2.316733 | 0.136974 | 0.845207 | 86.834% |
| 0.5 | 0 | 150506.0 | 12.320% | 4.748404 | 40.895% | 0.105305 | 1.793631 | 0.274180 | 0.803216 | 80.653% |
| 1 | 0 | 160133.0 | 19.504% | 3.251072 | 59.533% | 0.063925 | 1.004495 | 0.246543 | 0.739278 | 72.175% |
| 1.5 | 0 | 168761.9 | 25.944% | 3.163286 | 60.625% | 0.063657 | 1.023992 | 0.272058 | 0.733868 | 71.385% |
| 2 | 0 | 176589.4 | 31.785% | 2.787547 | 65.302% | 0.057599 | 0.987297 | 0.241587 | 0.704347 | 67.717% |
| 3 | 0 | 189703.4 | 41.572% | 2.538575 | 68.401% | 0.045404 | 0.960312 | 0.288401 | 0.677714 | 64.382% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
