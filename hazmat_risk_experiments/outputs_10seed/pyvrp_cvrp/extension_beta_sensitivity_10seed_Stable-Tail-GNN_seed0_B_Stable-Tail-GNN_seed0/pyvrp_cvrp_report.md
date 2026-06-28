# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.003160 | 0.000% | 0.253942 | 2.625387 | 0.223399 | 0.881536 | 90.545% |
| 0.5 | 0 | 165856.9 | 13.035% | 4.789536 | 40.154% | 0.127600 | 1.470778 | 0.213897 | 0.862862 | 86.128% |
| 1 | 0 | 176581.3 | 20.344% | 2.863800 | 64.217% | 0.060660 | 1.029346 | 0.281005 | 0.813975 | 78.114% |
| 1.5 | 0 | 184155.7 | 25.506% | 2.629682 | 67.142% | 0.056106 | 1.010688 | 0.292181 | 0.804079 | 76.291% |
| 2 | 0 | 191338.2 | 30.401% | 2.407683 | 69.916% | 0.051014 | 0.984439 | 0.310561 | 0.788973 | 73.644% |
| 3 | 0 | 204069.3 | 39.077% | 2.215671 | 72.315% | 0.045250 | 0.986399 | 0.326632 | 0.773110 | 71.214% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
