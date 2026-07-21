# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134398.2 | 0.000% | 10.286422 | 0.000% | 0.336611 | 3.008690 | 0.163525 | 0.875289 | 90.358% |
| 0.25 | 0 | 141769.6 | 5.485% | 7.210289 | 29.905% | 0.219366 | 2.206547 | 0.210667 | 0.874301 | 89.190% |
| 0.5 | 0 | 147385.5 | 9.663% | 5.200033 | 49.448% | 0.150452 | 1.854533 | 0.226210 | 0.851027 | 85.455% |
| 1 | 0 | 155941.4 | 16.029% | 3.513720 | 65.841% | 0.078453 | 1.213328 | 0.245288 | 0.810011 | 78.879% |
| 2 | 0 | 167838.9 | 24.882% | 2.834648 | 72.443% | 0.058937 | 0.804872 | 0.214318 | 0.781444 | 74.459% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
