# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 6.878324 | 0.000% | 0.198600 | 2.291333 | 0.216493 | 0.878165 | 89.534% |
| 0.5 | 0 | 147510.4 | 10.084% | 3.785268 | 44.968% | 0.110578 | 1.534270 | 0.320593 | 0.840222 | 83.888% |
| 1 | 0 | 154684.6 | 15.438% | 2.445659 | 64.444% | 0.059101 | 0.803774 | 0.233534 | 0.775441 | 74.944% |
| 1.5 | 0 | 160841.1 | 20.033% | 2.299396 | 66.570% | 0.053275 | 0.754598 | 0.257995 | 0.767454 | 73.976% |
| 2 | 0 | 166477.1 | 24.239% | 2.040797 | 70.330% | 0.043108 | 0.718972 | 0.268362 | 0.745340 | 70.462% |
| 3 | 0 | 175801.7 | 31.198% | 1.624171 | 76.387% | 0.029626 | 0.509137 | 0.225551 | 0.688955 | 62.453% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
