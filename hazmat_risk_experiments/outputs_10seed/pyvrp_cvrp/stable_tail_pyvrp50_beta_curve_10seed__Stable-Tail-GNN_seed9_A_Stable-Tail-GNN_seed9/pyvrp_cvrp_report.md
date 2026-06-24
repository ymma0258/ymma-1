# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.072629 | 0.000% | 0.224033 | 2.220910 | 0.199043 | 0.877152 | 89.589% |
| 0.25 | 0 | 141868.1 | 5.874% | 4.403315 | 37.741% | 0.135282 | 1.448002 | 0.235331 | 0.854694 | 85.758% |
| 0.5 | 0 | 147106.9 | 9.783% | 3.706090 | 47.600% | 0.086215 | 1.541035 | 0.301149 | 0.838164 | 83.532% |
| 1 | 0 | 154374.9 | 15.207% | 2.292019 | 67.593% | 0.046838 | 0.707972 | 0.170744 | 0.760009 | 72.492% |
| 2 | 0 | 165052.4 | 23.176% | 1.847968 | 73.872% | 0.033920 | 0.557268 | 0.200566 | 0.732811 | 68.116% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
