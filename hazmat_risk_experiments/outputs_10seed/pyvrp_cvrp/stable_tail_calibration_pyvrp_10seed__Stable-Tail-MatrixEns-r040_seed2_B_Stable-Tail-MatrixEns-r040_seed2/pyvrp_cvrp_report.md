# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 5.374582 | 0.000% | 0.168755 | 2.063676 | 0.313848 | 0.875339 | 89.647% |
| 0.25 | 0 | 156356.8 | 6.464% | 4.410241 | 17.943% | 0.137475 | 1.757117 | 0.327854 | 0.871836 | 88.718% |
| 0.5 | 0 | 164969.6 | 12.328% | 3.775969 | 29.744% | 0.110179 | 1.360862 | 0.258214 | 0.860743 | 86.961% |
| 1 | 0 | 177186.2 | 20.647% | 2.686852 | 50.008% | 0.073246 | 1.144735 | 0.329672 | 0.844901 | 83.450% |
| 2 | 0 | 195824.6 | 33.337% | 2.143498 | 60.118% | 0.053877 | 0.965965 | 0.361363 | 0.824148 | 79.661% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
