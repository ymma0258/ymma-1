# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 7.171628 | 0.000% | 0.206406 | 2.203406 | 0.181827 | 0.876059 | 89.386% |
| 0.25 | 0 | 141624.4 | 5.639% | 5.052500 | 29.549% | 0.146124 | 1.626599 | 0.225194 | 0.859995 | 87.158% |
| 0.5 | 0 | 147059.0 | 9.693% | 3.676977 | 48.729% | 0.106418 | 1.281105 | 0.241342 | 0.835115 | 83.114% |
| 1 | 0 | 154509.1 | 15.250% | 2.464097 | 65.641% | 0.064990 | 0.782704 | 0.233205 | 0.772667 | 74.906% |
| 2 | 0 | 165887.4 | 23.737% | 2.171970 | 69.714% | 0.053204 | 0.703928 | 0.256384 | 0.753165 | 71.745% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
