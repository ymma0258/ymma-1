# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 6.878324 | 0.000% | 0.198600 | 2.291333 | 0.216493 | 0.878165 | 89.534% |
| 1 | 0 | 154684.6 | 15.438% | 2.445659 | 64.444% | 0.059101 | 0.803774 | 0.233534 | 0.775441 | 74.944% |
| 1 | 0.5 | 159325.4 | 18.902% | 2.215859 | 67.785% | 0.049153 | 0.723229 | 0.228675 | 0.762191 | 73.112% |
| 1 | 1 | 163678.4 | 22.150% | 2.093692 | 69.561% | 0.045909 | 0.711673 | 0.281794 | 0.750105 | 71.334% |
| 1 | 2 | 169346.8 | 26.381% | 1.525249 | 77.825% | 0.025424 | 0.490953 | 0.240834 | 0.674751 | 60.196% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
