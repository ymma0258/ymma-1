# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 8.301355 | 0.000% | 0.265163 | 2.275132 | 0.151224 | 0.873127 | 89.811% |
| 0.25 | 0 | 141938.2 | 5.926% | 5.690549 | 31.450% | 0.177995 | 1.679972 | 0.190032 | 0.865766 | 87.786% |
| 0.5 | 0 | 147828.6 | 10.321% | 4.278269 | 48.463% | 0.115347 | 1.455351 | 0.230480 | 0.842757 | 84.120% |
| 1 | 0 | 156323.1 | 16.661% | 2.890457 | 65.181% | 0.065735 | 1.004880 | 0.240188 | 0.796139 | 77.226% |
| 2 | 0 | 169214.9 | 26.282% | 2.202436 | 73.469% | 0.042116 | 0.705539 | 0.232783 | 0.752882 | 70.509% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
