# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.2 | 0.000% | 8.946187 | 0.000% | 0.300662 | 2.779993 | 0.200674 | 0.875532 | 89.408% |
| 0.25 | 0 | 142499.0 | 6.185% | 5.695442 | 36.337% | 0.166279 | 2.137757 | 0.299381 | 0.863059 | 87.390% |
| 0.5 | 0 | 148880.1 | 10.940% | 4.597585 | 48.608% | 0.133911 | 1.646878 | 0.274957 | 0.850957 | 84.976% |
| 1 | 0 | 158235.1 | 17.911% | 3.245326 | 63.724% | 0.087052 | 1.289943 | 0.309685 | 0.810162 | 78.961% |
| 2 | 0 | 172486.6 | 28.531% | 2.904871 | 67.530% | 0.069034 | 1.180437 | 0.335905 | 0.793567 | 76.304% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
