# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134398.0 | 0.000% | 9.034191 | 0.000% | 0.296380 | 2.586118 | 0.178926 | 0.871812 | 89.347% |
| 0.25 | 0 | 143249.0 | 6.586% | 6.204087 | 31.327% | 0.184190 | 2.239320 | 0.254717 | 0.861091 | 87.021% |
| 0.5 | 0 | 149480.3 | 11.222% | 4.760936 | 47.301% | 0.138200 | 1.642888 | 0.225238 | 0.839286 | 83.783% |
| 1 | 0 | 158520.6 | 17.949% | 3.258656 | 63.930% | 0.088253 | 1.241989 | 0.299716 | 0.795381 | 76.803% |
| 2 | 0 | 171800.7 | 27.830% | 2.507300 | 72.247% | 0.058785 | 0.840805 | 0.262414 | 0.755083 | 70.522% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
