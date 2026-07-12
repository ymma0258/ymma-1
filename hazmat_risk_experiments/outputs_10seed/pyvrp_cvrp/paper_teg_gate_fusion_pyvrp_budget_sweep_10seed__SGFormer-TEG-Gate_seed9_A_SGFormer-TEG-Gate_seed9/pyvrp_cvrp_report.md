# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 6.977035 | 0.000% | 0.211091 | 2.155747 | 0.219970 | 0.859817 | 87.111% |
| 0.25 | 0 | 141185.2 | 5.364% | 4.057094 | 41.851% | 0.102659 | 1.308268 | 0.204869 | 0.822166 | 80.354% |
| 0.5 | 0 | 145945.8 | 8.916% | 3.431234 | 50.821% | 0.083490 | 1.252490 | 0.226357 | 0.803058 | 77.391% |
| 1 | 0 | 153511.5 | 14.562% | 2.151225 | 69.167% | 0.046899 | 0.636944 | 0.189913 | 0.711286 | 64.246% |
| 2 | 0 | 164193.9 | 22.534% | 2.041220 | 70.744% | 0.044069 | 0.565450 | 0.153660 | 0.704053 | 63.082% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
