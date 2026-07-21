# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.3 | 0.000% | 9.257168 | 0.000% | 0.305129 | 2.662282 | 0.171509 | 0.873517 | 89.771% |
| 0.25 | 0 | 141973.1 | 5.951% | 6.697905 | 27.646% | 0.204544 | 1.987629 | 0.204879 | 0.869960 | 88.304% |
| 0.5 | 0 | 147780.2 | 10.285% | 4.774162 | 48.427% | 0.125912 | 1.603576 | 0.201817 | 0.840448 | 84.032% |
| 1 | 0 | 156124.8 | 16.513% | 3.169902 | 65.757% | 0.067929 | 1.062378 | 0.260566 | 0.790574 | 76.574% |
| 2 | 0 | 169007.2 | 26.126% | 2.705818 | 70.771% | 0.056290 | 0.773546 | 0.230061 | 0.772435 | 73.398% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
