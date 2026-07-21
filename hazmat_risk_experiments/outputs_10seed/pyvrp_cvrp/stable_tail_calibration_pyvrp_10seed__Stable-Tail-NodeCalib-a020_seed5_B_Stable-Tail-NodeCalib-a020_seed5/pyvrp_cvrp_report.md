# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.6 | 0.000% | 7.752907 | 0.000% | 0.235513 | 2.584316 | 0.229887 | 0.874108 | 89.024% |
| 0.25 | 0 | 156350.5 | 6.363% | 6.522620 | 15.869% | 0.157141 | 2.203600 | 0.243395 | 0.870963 | 88.184% |
| 0.5 | 0 | 164881.2 | 12.166% | 5.173159 | 33.275% | 0.129498 | 1.695861 | 0.236811 | 0.851970 | 85.165% |
| 1 | 0 | 175078.5 | 19.103% | 3.351401 | 56.772% | 0.085373 | 1.201473 | 0.298079 | 0.813537 | 78.784% |
| 2 | 0 | 190835.1 | 29.822% | 2.751056 | 64.516% | 0.065162 | 0.893603 | 0.276105 | 0.790419 | 74.690% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
