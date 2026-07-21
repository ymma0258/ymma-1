# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.6 | 0.000% | 9.121188 | 0.000% | 0.293901 | 2.679511 | 0.180038 | 0.873700 | 89.846% |
| 0.25 | 0 | 143049.2 | 6.543% | 5.978885 | 34.451% | 0.185031 | 1.747305 | 0.199868 | 0.860508 | 87.688% |
| 0.5 | 0 | 149409.5 | 11.280% | 4.458667 | 51.117% | 0.116936 | 1.737578 | 0.269121 | 0.831718 | 83.842% |
| 1 | 0 | 158385.2 | 17.965% | 2.977108 | 67.361% | 0.070452 | 1.103406 | 0.282740 | 0.776963 | 76.108% |
| 2 | 0 | 172396.9 | 28.401% | 2.463212 | 72.995% | 0.053876 | 0.767501 | 0.241626 | 0.745172 | 71.321% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
