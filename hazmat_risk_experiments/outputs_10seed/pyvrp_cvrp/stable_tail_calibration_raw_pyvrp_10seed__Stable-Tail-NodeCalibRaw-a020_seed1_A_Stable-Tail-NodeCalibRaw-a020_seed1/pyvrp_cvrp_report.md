# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134530.9 | 0.000% | 9.741747 | 0.000% | 0.333105 | 2.717208 | 0.159714 | 0.871667 | 89.573% |
| 0.25 | 0 | 142057.0 | 5.594% | 6.524041 | 33.030% | 0.200327 | 2.177187 | 0.221532 | 0.864928 | 87.796% |
| 0.5 | 0 | 148105.6 | 10.090% | 4.765336 | 51.083% | 0.121271 | 1.601111 | 0.238901 | 0.842448 | 84.014% |
| 1 | 0 | 156556.6 | 16.372% | 3.224564 | 66.900% | 0.073060 | 1.039965 | 0.227731 | 0.793532 | 76.853% |
| 2 | 0 | 169476.1 | 25.976% | 2.832873 | 70.920% | 0.056673 | 0.865345 | 0.227345 | 0.773597 | 73.713% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
