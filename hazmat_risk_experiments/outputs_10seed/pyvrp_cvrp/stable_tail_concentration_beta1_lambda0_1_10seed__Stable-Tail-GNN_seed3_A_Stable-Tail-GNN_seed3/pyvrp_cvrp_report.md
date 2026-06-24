# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 6.878324 | 0.000% | 0.198600 | 2.291333 | 0.216493 | 0.878165 | 89.534% |
| 1 | 0 | 154686.9 | 15.440% | 2.406249 | 65.017% | 0.058053 | 0.797910 | 0.244994 | 0.771325 | 74.399% |
| 1 | 1 | 163678.4 | 22.150% | 2.093692 | 69.561% | 0.045909 | 0.711673 | 0.281794 | 0.750105 | 71.334% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
