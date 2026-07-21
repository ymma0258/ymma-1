# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.8 | 0.000% | 9.215013 | 0.000% | 0.302280 | 2.568299 | 0.172941 | 0.874751 | 89.824% |
| 0.25 | 0 | 143253.7 | 6.695% | 6.154571 | 33.211% | 0.179730 | 1.807685 | 0.197392 | 0.861926 | 87.235% |
| 0.5 | 0 | 149163.9 | 11.097% | 4.575872 | 50.343% | 0.132717 | 1.675105 | 0.257868 | 0.837867 | 83.358% |
| 1 | 0 | 158622.7 | 18.142% | 3.377839 | 63.344% | 0.091853 | 1.296171 | 0.286811 | 0.801067 | 77.674% |
| 2 | 0 | 171731.5 | 27.905% | 2.552790 | 72.297% | 0.059836 | 0.811074 | 0.258209 | 0.763761 | 71.682% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
